# **File Transfer**

## Übersicht

Die Seite **File Transfer** ermöglicht es, die vollständige Parameterkonfiguration des FlexiBowl® zu exportieren und zu importieren und die Daten zwischen dem System und einem PC zu übertragen. Sie ist die Funktion für Sicherung und Wiederherstellung der Betriebskonfiguration.

![Seite File Transfer](../../../../_shared/media/images/file_transfer.png)

---

## Verfügbare Funktionen

### DOWNLOAD FILE — Parameter speichern (FlexiBowl® → PC)

Der obere Bereich mit der Beschriftung **„Save the Current Parameters, from FlexiBowl® to PC“** ermöglicht es, alle aktuell im System konfigurierten Parameter in eine Datei zu exportieren.

Beim Drücken der Schaltfläche **DOWNLOAD FILE** erzeugt die Software eine Konfigurationsdatei und stellt sie zum Speichern auf dem angeschlossenen PC bereit.

:::{tip}
Vor jeder wesentlichen Änderung der Betriebsparameter einen **DOWNLOAD FILE** ausführen. Die heruntergeladene Datei ist eine vollständige Sicherung der Konfiguration und ermöglicht es, im Fehlerfall schnell den vorherigen Zustand wiederherzustellen.
:::

---

### UPLOAD FILE — Parameter laden (PC → FlexiBowl®)

Der untere Bereich mit der Beschriftung **„Load in the Current Parameters, from PC to FlexiBowl®“** ermöglicht es, eine zuvor gespeicherte Konfigurationsdatei in das System zu importieren.

Beim Drücken der Schaltfläche **UPLOAD FILE** öffnet sich die Dateiauswahl des Betriebssystems. Nach der Auswahl der Datei werden die Parameter in den FlexiBowl® geladen und sofort angewendet.

:::{warning}
Das Laden einer Konfigurationsdatei **überschreibt alle aktuellen Parameter** des Systems. Vor dem Fortfahren sicherstellen, dass die ausgewählte Datei mit dem verwendeten FlexiBowl®-Modell und der installierten Softwareversion kompatibel ist.
:::

:::{warning}
Das System während der Dateiübertragung nicht ausschalten und die Verbindung nicht unterbrechen. Eine Unterbrechung während des Uploads kann zu einer unvollständigen oder beschädigten Konfiguration führen.
:::

---

## Statusanzeigen der Übertragung

Am unteren Seitenrand befinden sich drei Anzeigeleuchten (virtuelle LEDs), die das Ergebnis des Übertragungsvorgangs signalisieren.

| Anzeige | Aktive Farbe | Beschreibung |
|---|---|---|
| **Active** | 🟡 Gelb | Die Übertragung läuft |
| **Successful** | 🟢 Grün | Die Übertragung wurde erfolgreich abgeschlossen |
| **Error** | 🔴 Rot | Bei der Übertragung ist ein Fehler aufgetreten |

:::{note}
Während eines Download- oder Upload-Vorgangs warten, bis die LED **Successful** leuchtet, bevor weitere Vorgänge ausgeführt werden. Leuchtet die LED **Error**, die Verbindung zum PC überprüfen und den Vorgang wiederholen.
:::
