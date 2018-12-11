from django.conf.urls import url

from api.v1.anagrafica import viste
from api.v1.attivita.viste import VistaMiePartecipazione, VistaTurni, PartecipaTurno, VistaAttivita, \
    VistaAttivitaDettaglio, VistaTurniPerAttivita

urlpatterns = [
    url(r'^me/anagrafica/base/$', viste.MiaAnagraficaBase.as_view()),
    url(r'^me/anagrafica/completa/$', viste.MiaAnagraficaCompleta.as_view()),
    url(r'^me/appartenenze/attuali/$', viste.MieAppartenenzeAttuali.as_view()),
    url(r'^me/appartenenza/completa/$', viste.MiaAppartenenzaComplaeta.as_view()),
    url(r'^me/partecipazioni/$', VistaMiePartecipazione.as_view()),
    url(r'^turni/$', VistaTurni.as_view()),
    url(r'^turni/(?P<turno_pk>[0-9]+)/partecipa/$', PartecipaTurno.as_view()),
    url(r'^attivita/$', VistaAttivita.as_view()),
    url(r'^attivita/(?P<pk>[0-9]+)/$', VistaAttivitaDettaglio.as_view()),
    url(r'^attivita/(?P<pk>[0-9]+)/turni/$', VistaTurniPerAttivita.as_view()),

]
