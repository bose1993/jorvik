from rest_framework import serializers

from attivita.models import Turno, Attivita, Partecipazione


class TurnoSerializzatore(serializers.ModelSerializer):
    class Meta:
        model = Turno
        fields = "__all__"


class AttivitaSerializzatore(serializers.ModelSerializer):
    class Meta:
        model = Attivita
        fields = "__all__"


class PartecipazioneSerializzatore(serializers.ModelSerializer):
    turno = TurnoSerializzatore(many=False)

    class Meta:
        model = Partecipazione
        fields = "__all__"
