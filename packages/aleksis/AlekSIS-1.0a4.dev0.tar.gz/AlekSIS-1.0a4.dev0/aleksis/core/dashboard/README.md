# Dashboard
Das Dashboard dient dazu, den Benutzer zu begrüßen (> Startseite)
und seine letzten Aktivitäten anzuzeigen.

Edit: Außerdem zeigt das Dashboard aktuelle Nachrichten für den Benutzer an.

## Aktivitäten
Als Aktivität gilt alles, was der Nutzer selbst macht, d.h., bewusst.

### Eine Aktivität registrieren
1. Importieren

        from .apps import <Meine App>Config
        from dashboard.models import Activity

2. Registrieren

        act = Activity(title="<Titel der Aktion>", description="<Beschreibung der Aktion>", app=<Meine App>Config.verbose_name, user=<Benutzer Objekt>)
        act.save()

## Benachrichtigungen
Als Benachrichtigung gilt eine Aktion, die den Nutzer betrifft.

### Eine Benachrichtigung verschicken
1. Importieren

        from .apps import <Meine App>Config
        from dashboard.models import Notification

2. Verschicken

          register_notification(title="<Titel der Nachricht>",
                                      description="<Weitere Informationen>",
                                      app=<Meine App>Config.verbose_name, user=<Benutzer Objekt>,
                                      link=request.build_absolute_uri(<Link für weitere Informationen>))

    **Hinweis:** Der angegebene Link muss eine absolute URL sein.
    Dies wird durch übergabe eines dynamischen Linkes (z. B. /aub/1) an die Methode `request.build_absolute_uri()` erreicht.

    Um einen dynamischen Link durch den Namen einer Django-URL zu "errechnen", dient die Methode `reverse()`.

    Literatur:
    - [1] https://docs.djangoproject.com/en/2.1/ref/request-response/#django.http.HttpRequest.build_absolute_uri
    - [2] https://docs.djangoproject.com/en/2.1/ref/urlresolvers/#reverse

