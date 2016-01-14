from anagrafica.permessi.costanti import GESTIONE_CORSI_SEDE
from base.utils import remove_none

__author__ = 'alfioemanuele'

"""
Questa pagina contiene i vari menu che vengono mostrati nella barra laterale dei template.
La costante MENU e' accessibile attraverso "menu" nei template.
"""


def menu(request):
    """
    Ottiene il menu per una data richiesta.
    """
    me = request.me if hasattr(request, 'me') else None

    gestione_corsi_sede = me.ha_permesso(GESTIONE_CORSI_SEDE) if me else False

    return remove_none({
        "utente": (
            (("Persona", (
                ("Benvenuto", "fa-bolt", "/utente/"),
                ("Anagrafica", "fa-edit", "/utente/anagrafica/"),
                ("Storico", "fa-clock-o", "/utente/storico/"),
                ("Documenti", "fa-folder", "/utente/documenti/"),
                ("Contatti", "fa-envelope", "/utente/contatti/"),
                ("Fotografie", "fa-credit-card", "/utente/fotografia/"),
            )),
            ("Volontario", (
                ("Estensione", "fa-arrow-right", "/utente/estensione/"),
                ("Trasferimento", "fa-arrow-right", "/utente/trasferimento/"),
            )) ,
            ("Curriculum", (
                ("Competenze personali", "fa-arrow-right", "/utente/curriculum/CP/"),
                ("Patenti Civili", "fa-arrow-right", "/utente/curriculum/PP/"),
                ("Patenti CRI", "fa-arrow-right", "/utente/curriculum/PC/"),
                ("Titoli di Studio", "fa-arrow-right", "/utente/curriculum/TS/"),
                ("Titoli CRI", "fa-arrow-right", "/utente/curriculum/TC/"),
            )),
            ("Donatore", (
                ("Profilo Donatore", "fa-user", "/utente/donazioni/profilo/"),
                ("Donazioni di Sangue", "fa-flask", "/utente/donazioni/sangue/")
                    if hasattr(me, 'donatore') else None,
            )) if me and me.volontario else None,
            ("Sicurezza", (
                ("Cambia password", "fa-key", "/utente/cambia-password/"),
            )),
        )),
        "posta": (
            ("Posta", (
                ("Scrivi", "fa-pencil", "/posta/scrivi/"),
                ("In arrivo", "fa-inbox", "/posta/in-arrivo/"),
                ("In uscita", "fa-mail-forward", "/posta/in-uscita/"),
            )),
        ),
        "veicoli": (
            ("Veicoli", (
                ("Dashboard", "fa-gears", "/veicoli/"),
                ("Veicoli", "fa-car", "/veicoli/elenco/"),
                ("Autoparchi", "fa-dashboard", "/veicoli/autoparchi/"),
            )),
        ),
        "attivita": (
            ("Attività", (
                ("Calendario", "fa-calendar", "/attivita/calendario/"),
                ("Miei turni", "fa-list", "/attivita/storico/"),
                ("Gruppi", "fa-users", "/attivita/gruppi/"),
                ("Reperibilità", "fa-thumb-tack", "/attivita/reperibilita/"),
            )),
        ),
        "autorizzazioni": (
            ("Richieste", (
                ("In attesa", "fa-user-plus", "/autorizzazioni/"),
                ("Storico", "fa-clock-o", "/autorizzazioni/storico/"),
            )),
        ),
        "us": (
            ("Elenchi", (
                ("Volontari", "fa-list", "/us/elenchi/volontari/"),
                ("Soci", "fa-list", "/us/elenchi/soci/"),
                ("Sostenitori", "fa-list", "/us/elenchi/sostenitori/"),
                ("Elettorato", "fa-list", "/us/elenchi/elettorato/"),
            )),
            ("Aggiungi", (
                ("Persona", "fa-plus-square", "/us/aggiungi/"),
                ("Reclama Socio", "fa-plus-square", "/us/reclama/"),
            )),
            ("Pratiche", (
                ("Nuovo trasferimento", "fa-file-o", "/us/trasferimento/"),
                ("Nuova estensione", "fa-file-o", "/us/estensione/"),
                ("Messa in riserva", "fa-file-o", "/us/riserva/"),
                ("Nuovo provvedimento", "fa-file-o", "/us/provvedimento/"),
            )),
            ("Quote e ricevute", (
                ("Quote associative", "fa-money", "/us/quote/"),
                ("Ricerca quote", "fa-search", "/us/quote/ricerca/"),
                ("Ricevute", "fa-search", "/us/quote/ricevute/"),
            )),
            ("Tesserini", (
                ("Non riconsegnati", "fa-credit-card", "/us/non-riconsegnati/"),
            )),
        ),
        "formazione": (
            ("Corsi Base", (
                ("Elenco Corsi Base", "fa-list", "/formazione/corsi-base/elenco/"),
                ("Domanda formativa", "fa-area-chart", "/formazione/corsi-base/domanda/")
                    if gestione_corsi_sede else None,
                ("Pianifica nuovo", "fa-asterisk", "/formazione/corsi-base/nuovo/")
                    if gestione_corsi_sede else None,
            )),
            ("Corsi di Formazione", (
                ("Elenco Corsi di Formazione", "fa-list", "/formazione/corsi-formazione/"),
                ("Pianifica nuovo", "fa-asterisk", "/formazione/corsi-formazione/nuovo/"),
            )) if False else None,
        ),
        "aspirante": (
            ("Aspirante", (
                ("Home page", "fa-home", "/aspirante/"),
                ("Impostazioni", "fa-gears", "/aspirante/impostazioni/")
            )),
            ("Nelle vicinanze", (
                ("Corsi Base", "fa-list", "/aspirante/corsi-base/"),
                ("Sedi CRI", "fa-list", "/aspirante/sedi/"),
            )),
        ) if me and hasattr(me, 'aspirante') else (
            ("Gestione Corsi", (
                ("Elenco Corsi Base", "fa-list", "/formazione/corsi-base/elenco/"),
            )),
        ),
    })