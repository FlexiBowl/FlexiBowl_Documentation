# **Graphs**

## Übersicht

Die Seite **Graphs** bietet ein Echtzeit-Überwachungs-Dashboard der elektrischen und thermischen Größen des Motortreibers des FlexiBowl®. Auf dieser Seite kann der Bediener die Leistung des Systems überprüfen und eventuelle Anomalien während des Betriebs erkennen.

![Startseite](../../../../_shared/media/images/pagina_Graphs.png)

---

## Leiste mit Zählern und Anzeigen

Der obere Teil der Seite fasst die wichtigsten Statusparameter des Systems zusammen, aufgeteilt in drei Spalten.

### Linke Spalte

| Feld | Beispielwert | Beschreibung |
|---|---|---|
| **Timer Global** | 30 d: 0 h: 14 min: 48 s | Gesamte Einschaltzeit des Systems seit dem letzten Zurücksetzen des globalen Zählers |
| **Drive Temperature** | 45.2 °C | Aktuelle Temperatur des Motortreibers |
| **DC Voltage** | 48.4 V | Spannung des DC-Busses, der den Motortreiber versorgt |

### Mittlere Spalte

| Feld | Beispielwert | Beschreibung |
|---|---|---|
| **Timer Run** | 4 d: 14 h: 8 min: 34 s | Gesamte Laufzeit des Motors (tatsächliche Bewegungszeit) seit dem letzten Zurücksetzen |
| **Dsp Temperature** | 50.7 °C | Temperatur des DSP-Prozessors im Inneren des Treibers |
| **Total Revolutions** | 127023 | Gesamtzahl der vom FlexiBowl® seit dem letzten Zurücksetzen des Zählers ausgeführten Umdrehungen |

### Rechte Spalte

| Feld | Beispielwert | Beschreibung |
|---|---|---|
| **Utilization** | 15 % | Aktueller Auslastungsgrad des Motors in Prozent bezogen auf die maximale Kapazität. Dargestellt durch einen Fortschrittsbalken mit dem Prozentwert in farbigem Text |
| **Max Drive Temperature** | 45.7 °C | Höchste vom Motortreiber seit dem letzten Zurücksetzen erreichte Temperatur |
| **Max Dsp Temperature** | 51.1 °C | Höchste vom DSP seit dem letzten Zurücksetzen erreichte Temperatur |

### ECO LOAD %

Das Tachometer **ECO LOAD %** oben rechts zeigt die durchschnittliche Motorlast in Prozent an. Der im Beispiel angezeigte Wert beträgt **9,1 %** und weist auf eine geringe Last hin – ein typischer Zustand bei Systemen mit kurzen Arbeitszyklen oder niedrigen Geschwindigkeiten.

:::{tip}
Der Wert **ECO LOAD %** ist ein nützlicher Indikator zur Beurteilung der Betriebseffizienz des Systems im Zeitverlauf. Dauerhaft hohe Werte können auf eine mechanische Überlastung oder zu aggressive Geschwindigkeitsparameter hinweisen.
:::

---

## Echtzeit-Diagramme

Der untere Teil der Seite zeigt drei Oszilloskop-Diagramme, die den zeitlichen Verlauf der Motorgrößen darstellen. Die horizontale Achse zeigt die seit dem Start vergangene Zeit im Format `Xh Ym Zs` (Felder mit dem Wert null, wie die Stunden, werden möglicherweise nicht angezeigt – z. B. `33m46s`).

### Velocity Motor %

Diagramm der **Motorgeschwindigkeit**, ausgedrückt in Prozent der maximalen Geschwindigkeit.

| Achse | Beschreibung |
|---|---|
| **Y** | Geschwindigkeit in **Prozent** der maximalen Geschwindigkeit, mit Vorzeichen: **Negative** Werte bedeuten Drehung **gegen den Uhrzeigersinn**, **positive** Werte Drehung **im Uhrzeigersinn**. Der Wert **0** entspricht einem stillstehenden Motor |
| **X** | Ausführungszeit |

:::{note}
Ein negativer Geschwindigkeitswert bedeutet Drehung **gegen den Uhrzeigersinn**; ein positiver Wert bedeutet Drehung **im Uhrzeigersinn**. Dies entspricht dem Parameter **Speed** auf der Seite Jog Motor.
:::

### Current Motor %

Diagramm des **vom Motor aufgenommenen Stroms**, ausgedrückt in Prozent des maximalen Nennstroms.

| Achse | Beschreibung |
|---|---|
| **Y** | Auf Prozent normierter Strom. Er kann je nach Betriebsphase (z. B. Beschleunigung/Verzögerung) sowohl **positive** als auch **negative** Werte annehmen; die Spitzen entsprechen den abruptesten Geschwindigkeitsänderungen |
| **X** | Ausführungszeit |

:::{tip}
Hohe, wiederkehrende Stromspitzen können auf zu aggressive Beschleunigungsrampen hinweisen. In diesem Fall die Werte für **Acceleration** und **Deceleration** erhöhen, um die Belastung auf einen längeren Zeitraum zu verteilen.
:::

### Torque Motor %

Diagramm des **vom Motor abgegebenen Drehmoments**, ausgedrückt in Prozent des maximalen Nenndrehmoments.

| Achse | Beschreibung |
|---|---|
| **Y** | Auf Prozent normiertes Drehmoment. Wie beim Strom kann es je nach Bewegungsphase sowohl **positive** als auch **negative** Werte annehmen |
| **X** | Ausführungszeit |

:::{note}
Die Diagramme **Current Motor %** und **Torque Motor %** zeigen typischerweise einen sehr ähnlichen Verlauf, da bei einem Gleichstrommotor das Drehmoment direkt proportional zum Strom ist. Deutliche Unterschiede zwischen beiden können auf Anomalien im Treiber hinweisen.
:::

---

## Hinweise zur Verwendung

:::{warning}
Dauerhaft über 70 °C liegende Werte von **Drive Temperature** oder **Dsp Temperature** können die Lebensdauer des Treibers verkürzen und Abschaltungen durch den Thermoschutz verursachen. Die Belüftungsbedingungen des Schaltschranks und den Arbeitszyklus des Systems überprüfen.
:::

:::{warning}
Ein Wert von **DC Voltage** außerhalb des Nennbereichs (typischerweise 48 V ± 10 %) kann auf Probleme mit dem Netzteil hinweisen. Den Betrieb unterbrechen und den technischen Service kontaktieren.
:::
