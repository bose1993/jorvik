
SCOPE_ANAGRAFICA_LETTURA_BASE = 'anagrafica_lettura_base'
SCOPE_ANAGRAFICA_LETTURA_COMPLETA = 'anagrafica_lettura_completa'
SCOPE_ANAGRAFICA_LETTURA_TELEFONO = 'anagrafica_lettura_telefono'
SCOPE_APPARTENENZE_LETTURA = 'appartenenze_lettura'
SCOPE_TURNI_COMITATO = 'turni_comitato'


OAUTH2_PROVIDER = {
    'SCOPES': {
        SCOPE_ANAGRAFICA_LETTURA_BASE:     "Lettura anagrafica di base (nome, cognome, indirizzo email di contatto)",
        SCOPE_ANAGRAFICA_LETTURA_COMPLETA: "Lettura anagrafica completa (data e luogo di nascita, luogo di residenza, "
                                           "sesso e codice fiscale).",
        SCOPE_ANAGRAFICA_LETTURA_TELEFONO: "Lettura dei numeri di telefono",
        SCOPE_APPARTENENZE_LETTURA:        "Lettura delle appartenenze attuali",
        SCOPE_TURNI_COMITATO: "Ottiene i turni disponibili per il comitato"
    },

    'DEFAULT_SCOPES': [SCOPE_ANAGRAFICA_LETTURA_BASE]
}
