from datetime import date, datetime, timedelta

from django.db.models import Count
from oauth2_provider.ext.rest_framework import TokenHasScope
from rest_framework import permissions
from rest_framework.exceptions import ValidationError, NotAuthenticated
from rest_framework.generics import RetrieveAPIView, CreateAPIView, get_object_or_404, ListAPIView
from rest_framework.response import Response

from anagrafica.permessi.costanti import GESTIONE_ATTIVITA
from api.settings import SCOPE_TURNI_COMITATO
from api.v1.attivita.serializzatori import AttivitaSerializzatore, PartecipazioneSerializzatore, TurnoSerializzatore
from attivita.models import Partecipazione, Turno, Attivita


class VistaTurni(ListAPIView):
    serializer_class = TurnoSerializzatore
    permission_classes = (permissions.IsAuthenticated,
                          TokenHasScope)
    required_scopes = [SCOPE_TURNI_COMITATO]

    def get_queryset(self):
        inizio = self.request.GET.get('inizio')
        fine = self.request.GET.get('fine')

        DEFAULT_GIORNI = 15
        MASSIMO_GIORNI = 31

        # Formato date URL
        FORMATO = "%d-%m-%Y"

        if inizio is None:
            inizio = date.today().strftime(FORMATO)

        inizio = datetime.strptime(inizio, FORMATO).date()

        if fine is None:
            fine = inizio + timedelta(DEFAULT_GIORNI)
        else:
            fine = datetime.strptime(fine, FORMATO).date()

        # Assicura che il range sia valido (non troppo breve, non troppo lungo)
        differenza = (fine - inizio)
        if differenza.days < 0 or differenza.days > MASSIMO_GIORNI:
            raise ValidationError(detail="Valore inizio o fine non valido")
        me = self.request.user.persona
        if not me.volontario:
            raise NotAuthenticated(detail="Utente non trovato")
        data = me.calendario_turni(inizio, fine)
        return data


class VistaTurniPerAttivita(VistaTurni):

    def get_queryset(self):
        # Eredito da Viste Turni. Specializzo il metodo per filtrare per attivita
        att_id = self.kwargs.get('pk')
        data = super(VistaTurniPerAttivita, self).get_queryset().filter(attivita_id=att_id)
        return data


class VistaAttivita(ListAPIView):
    serializer_class = AttivitaSerializzatore
    permission_classes = (permissions.IsAuthenticated,
                          TokenHasScope)
    required_scopes = [SCOPE_TURNI_COMITATO]

    def get_queryset(self):
        stato = self.request.GET.get('stato')
        me = self.request.user.persona
        attivita_tutte = me.oggetti_permesso(GESTIONE_ATTIVITA, solo_deleghe_attive=False)
        attivita_aperte = attivita_tutte.filter(apertura=Attivita.APERTA)
        attivita_chiuse = attivita_tutte.filter(apertura=Attivita.CHIUSA)

        if stato == "aperte":
            attivita = attivita_aperte

        else:  # stato == "chiuse"
            attivita = attivita_chiuse

        attivita = attivita.annotate(num_turni=Count('turni'))
        return attivita


class VistaAttivitaDettaglio(RetrieveAPIView):
    serializer_class = AttivitaSerializzatore
    permission_classes = (permissions.IsAuthenticated,
                          TokenHasScope)
    required_scopes = [SCOPE_TURNI_COMITATO]

    def get_queryset(self):
        me = self.request.user.persona
        attivita = me.oggetti_permesso(GESTIONE_ATTIVITA, solo_deleghe_attive=False)
        attivita = attivita.annotate(num_turni=Count('turni'))
        return attivita


class PartecipaTurno(CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,
                          TokenHasScope)
    required_scopes = [SCOPE_TURNI_COMITATO]

    def create(self, request, *args, **kwargs):
        turno_pk = kwargs.get('turno_pk', None)
        me = self.request.user.persona
        turno = get_object_or_404(Turno, pk=turno_pk)
        stato = turno.persona(me)

        if stato not in turno.TURNO_PUOI_PARTECIPARE:
            raise ValidationError(detail=[{"stato": "Impossibile partecipare al turno", "dettaglio": stato}], code=400)

        p = Partecipazione(
            turno=turno,
            persona=me,
        )
        p.save()
        p.richiedi()

        return Response(PartecipazioneSerializzatore(p).data, status=201)


class VistaMiePartecipazione(ListAPIView):
    permission_classes = (permissions.IsAuthenticated,
                          TokenHasScope)
    required_scopes = [SCOPE_TURNI_COMITATO]
    serializer_class = PartecipazioneSerializzatore

    def get_queryset(self):
        me = self.request.user.persona
        storico = Partecipazione.objects.filter(persona=me).order_by('-turno__inizio')
        return storico
