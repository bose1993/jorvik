# coding=utf-8

"""
Questo modulo definisce i modelli del modulo di Formazione di Gaia.
"""
from base.models import ConAutorizzazioni
from base.geo import ConGeolocalizzazione, ConGeolocalizzazioneRaggio
from base.models import ModelloSemplice
from base.tratti import ConMarcaTemporale
from social.models import ConCommenti, ConGiudizio


class Corso(ModelloSemplice, ConMarcaTemporale, ConGeolocalizzazione, ConCommenti, ConGiudizio):

    class Meta:
        verbose_name = "Corso di formazione"
        verbose_name_plural = "Corsi di formazione"


class Partecipazione(ModelloSemplice, ConAutorizzazioni, ConMarcaTemporale):

    class Meta:
        verbose_name = "Richiesta di partecipazione"
        verbose_name_plural = "Richieste di partecipazione"


class Lezione(ModelloSemplice, ConMarcaTemporale, ConGiudizio):

    class Meta:
        verbose_name_plural = "Lezioni"


class Assenza(ModelloSemplice, ConMarcaTemporale):

    class Meta:
        verbose_name_plural = "Assenze"


class Aspirante(ModelloSemplice, ConGeolocalizzazioneRaggio, ConMarcaTemporale):

    class Meta:
        verbose_name_plural = "Aspiranti"