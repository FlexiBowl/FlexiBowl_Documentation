# **Monitor**

## Übersicht

Die Seite **Monitor** bietet eine Echtzeitansicht des Zustands des Motors und des Kommunikationssystems und protokolliert alle Ereignisse und Alarme, die während des Betriebs des FlexiBowl® auftreten. Sie ist die Referenzseite für Diagnose und Fehlersuche.
![Seite Monitor](../../../../_shared/media/images/monitor.png)

---

## Abschnitt STATE MOTOR

Der Bereich **STATE MOTOR** zeigt den aktuellen Betriebszustand des Motortreibers mithilfe mehrerer Anzeigeleuchten (virtuelle LEDs).
Jede LED kann sein:
🟢 **Grün** : aktiver Zustand
⚫ **Grau** : inaktiver Zustand

### Statusanzeigen

| Anzeige | Beschreibung |
|---|---|
| **Not Ready To Switch On** | Der Treiber ist nicht bereit für die Aktivierung  |
| **Switch On Disabled** | Die Aktivierung des Motors ist gesperrt  |
| **Ready To Switch On** | Der Treiber ist bereit, den Aktivierungsbefehl zu empfangen |
| **Switched On** | Der Motor ist mit Spannung versorgt, aber noch nicht in aktiver Regelung |
| **Target Reached** | Der FlexiBowl® hat die Zielposition bzw. den Sollwert erreicht |
| **Operation Enabled** | Der Motor ist aktiviert und betriebsbereit |
| **Quick Stop Active** | Schnellstopp des Motors angefordert |
| **Fault Reaction Active** | Der Treiber führt die Fehlerreaktionsprozedur aus |
| **Fault** | Am Motortreiber liegt ein aktiver Fehler vor |
| **SetPoint in process** | Das System verarbeitet bzw. erreicht einen neuen Positionssollwert |

:::{note}
Im normalen Betrieb müssen die LEDs **Operation Enabled** und **Target Reached** grün sein. Jede andere grüne LED weist auf einen anomalen Zustand hin, der Aufmerksamkeit erfordert.
:::

---

## Abschnitt Communication State

Der Bereich auf der rechten Seite zeigt den Status der Kommunikation zwischen der Software und dem Motortreiber.

| Feld | Beispielwert | Beschreibung |
|---|---|---|
| **Communication State** | `RUNNING` | Zeigt an, dass die Kommunikation mit dem Treiber aktiv ist und funktioniert |
| **Error Code** | `0` | Vom Treiber zurückgegebener Fehlercode. Der Wert `0` bedeutet, dass keine Fehler vorliegen |

### Schaltfläche Reset Driver

Die Schaltfläche **Reset Driver** führt einen Reset des Motortreibers durch. Sie ist nützlich, um einen Fehlerzustand zu verlassen oder die Kommunikation neu zu initialisieren.

:::{warning}
**Reset Driver** erst drücken, nachdem die Ursache des Fehlers erkannt und behoben wurde. Ein Reset ohne Beseitigung der Problemursache kann dazu führen, dass der Fehler erneut auftritt, oder das System beschädigen.
:::

---

## Ereignisprotokoll (Meldungstabelle)

Die zentrale Tabelle protokolliert in Echtzeit alle Ereignisse, Alarme und Systemmeldungen, die während des Betriebs auftreten.

### Spalten der Tabelle

| Spalte | Beschreibung |
|---|---|
| **Timestamp** | Datum und Uhrzeit des Ereignisses im Format `GG.MM.AAAA HH:MM:SS` |
| **Message** | Textbeschreibung des Ereignisses oder Alarms |
| **Bitmap** | Symbol, das die Art des Ereignisses anzeigt (⚠️ Warnung, ❌ Fehler usw.) |

### Beispielmeldung

| # | Timestamp | Message | Bitmap |
|---|---|---|---|
| 0 | 14.05.2026 15:59:57 | Air pressure does not match the set value | ⚠️ |

:::{warning}
Die Meldung **„Air pressure does not match the set value“** zeigt an, dass der vom System erfasste Luftdruck nicht mit dem in den Parametern eingestellten Wert übereinstimmt. Die pneumatische Versorgung prüfen und die Werte **Flip Pressure** und **Blow Pressure** auf der Seite **Main Command > OPTION** kontrollieren.
:::

:::{tip}
Warnmeldungen werden in der Spalte Timestamp in **Rot** und in der Spalte Message in **Orange** angezeigt, damit sie auch bei vielen Zeilen im Protokoll sofort erkennbar sind.
:::

---

## Schaltflächen zur Protokollverwaltung

| Schaltfläche | Funktion |
|---|---|
| **ACK selected** | Quittiert die in der Tabelle ausgewählte Meldung und markiert sie als übernommen |
| **ACK all visible** | Quittiert alle derzeit in der Tabelle sichtbaren Meldungen |
| **History** | Öffnet den vollständigen Verlauf der vom System aufgezeichneten Ereignisse |
| **Freeze Scrl Pos** | Sperrt das automatische Scrollen der Tabelle, sodass frühere Meldungen geprüft werden können, ohne dass die Ansicht zu neuen Ereignissen springt |

:::{note}
Es ist empfehlenswert, Alarme erst dann zu **quittieren (ACK)**, nachdem die Ursache geprüft und behoben wurde, und nicht, um die Meldung ohne Eingriff zu unterdrücken.
:::
