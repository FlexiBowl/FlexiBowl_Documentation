(hopper)=
# **Hopper**
## Übersicht

Auf der Seite **Hopper** lassen sich bis zu **4 Bulk Feeder**, die an den FlexiBowl® angeschlossen sind, konfigurieren und verwalten. Jeder Hopper ist eine eigenständige Zuführeinheit, die den FlexiBowl® mit Bauteilen versorgt und unabhängig mit eigenen Vibrations- und Zeitparametern gesteuert werden kann.

Jeder Hopper wird durch eine vertikale Spalte mit denselben Bedienelementen dargestellt und als **HOPPER 1**, **HOPPER 2**, **HOPPER 3** und **HOPPER 4** bezeichnet.

![Seite Hopper](../../../../_shared/media/images/hopper.png) ---

## Aufbau jedes Hopper-Bereichs

### ENABLE

Das Kontrollkästchen **ENABLE** oben im Bereich aktiviert oder deaktiviert den entsprechenden Hopper. Nur aktivierte Hopper können gestartet werden und reagieren auf Systembefehle.

Im gezeigten Beispiel ist nur bei **HOPPER 1** das Kontrollkästchen ENABLE ausgewählt (blauer Haken); die Hopper 2, 3 und 4 sind deaktiviert.

:::{note}
Ein deaktivierter Hopper reagiert nicht auf die Schaltfläche **Start Hopper** und wird bei automatischen Sequenzen nicht aktiviert, auch wenn er physisch mit dem System verbunden ist.
:::

---

### ID und Set New ID

| Feld |  Beschreibung |
|---|---|
| **ID** |  Eindeutige Kennung, die dem Hopper im Kommunikationsnetzwerk zugewiesen ist |
| **Set New ID** | Schaltfläche zum Zuweisen einer neuen ID an den Hopper. Wird bei der Erstkonfiguration oder beim Austausch der Einheit verwendet |

:::{warning}
Die ID eines Hoppers nur ändern, wenn es unbedingt erforderlich ist. Eine falsche oder doppelte ID verhindert die Kommunikation mit dem Hopper und kann Fehlfunktionen in der gesamten Zuführkette verursachen. Nach dem Festlegen einer neuen ID anhand der Anzeige **STATUS** prüfen, ob sie korrekt übernommen wurde.
:::

---

### STATUS

Die Anzeige **STATUS** zeigt den aktuellen Betriebszustand des Hoppers.

| LED-Farbe | Beschriftung | Beschreibung |
|---|---|---|
| 🔴 Rot | **DISABLED** | Der Hopper ist deaktiviert |
| 🟢 Grün | **ENABLED** | Der Hopper ist aktiviert |


---

### Vibrationsparameter

| Parameter |  Beschreibung |
|---|---|
| **Amplitude** |  Amplitude der Vibration des Hoppers, ausgedrückt in dimensionslosen Einheiten. Höhere Werte erzeugen eine stärkere Vibration und einen größeren Bauteilfluss |
| **Frequency** | Vibrationsfrequenz des Hoppers. Sie beeinflusst die Taktung, mit der die Bauteile zum FlexiBowl® befördert werden |


---

### Activation Time und Status-LED

| Feld  | Beschreibung |
|---|---|
| **Activation Time** | Dauer der Aktivierung des Hoppers, wenn er manuell mit **Start Hopper** gestartet oder von einer Sequenz aufgerufen wird |
| **LED** (grau/grün) |  Anzeigeleuchte, die während der Aktivierung des Hoppers leuchtet |

:::{note}
**HOPPER 1** hat eine **Activation Time** von 2000 ms, während die anderen Hopper auf 800 ms eingestellt sind. Längere Aktivierungszeiten führen zu einer größeren Bauteilzufuhr zum FlexiBowl® pro Aktivierungszyklus.
:::

---

### Start Hopper

Die Schaltfläche **Start Hopper** startet den Hopper manuell für die in **Activation Time** eingestellte Dauer. Nach Ablauf der Zeit stoppt der Hopper automatisch.

:::{important}
Die Schaltfläche **Start Hopper** ist nur aktiv, wenn das Kontrollkästchen **ENABLE** des entsprechenden Hoppers ausgewählt ist. Vor dem manuellen Start prüfen, ob der Hopper aktiviert ist.
:::

---

