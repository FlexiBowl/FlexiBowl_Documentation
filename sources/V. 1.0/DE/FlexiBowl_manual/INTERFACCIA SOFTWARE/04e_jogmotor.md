(jog)=
# **Jog Motor**

## Übersicht

Die Seite **Jog Motor** ermöglicht es, den FlexiBowl® im kontinuierlichen manuellen Modus (Jog) zu betreiben, ohne programmierte Sequenzen zu verwenden. Sie wird hauptsächlich bei Einrichtung, Inbetriebnahme und Test des Systems eingesetzt und erlaubt dem Bediener, die Drehung des FlexiBowl® und die Zusatzfunktionen direkt zu steuern.
![Seite Jog Motor](../../../../_shared/media/images/jog_motor.png)

---

## Bewegungsparameter

Die drei Schieberegler oben legen das Verhalten des Motors während des Jogs fest.

| Parameter | Einheit | Beispielwert | Beschreibung |
|---|---|---|---|
| **Acceleration** | % | 50 | Beschleunigungsrampe beim Start des Jogs |
| **Deceleration** | % | 50 | Verzögerungsrampe beim Stopp des Jogs |
| **Speed** | % | -30 | Drehgeschwindigkeit des FlexiBowl®. Ein **negativer** Wert bedeutet Drehung **gegen den Uhrzeigersinn**; ein **positiver** Wert bedeutet Drehung **im Uhrzeigersinn** |

:::{tip}
Um die Drehrichtung des FlexiBowl® während des Jogs umzukehren, genügt es, den Schieberegler **Speed** auf einen negativen Wert zu stellen. Der Jog muss für die Änderung des Parameters nicht gestoppt werden.
:::

---

## Bereich FLIP

Der Bereich **Flip Enable** steuert die Aktivierung und die Parameter des Flip-Systems während des Jogs.

| Steuerung | Beispielwert | Beschreibung |
|---|---|---|
| **Flip Enable** (Umschalter) | Aktiv (rot) | Aktiviert den automatischen Flip während des Jogs |
| **Flip Duration** | 200 ms | Dauer des Flip-Betätigungsimpulses |
| **Flip Pression** | 3,00 Bar | Für den Flip verwendeter Luftdruck |
| **Flip Pause** | 200 ms | Pause zwischen einem Flip und dem nächsten während des Jogs |

:::{note}
Der Flip wird während des Jogs zyklisch ausgeführt, im durch **Flip Pause** festgelegten Takt, jedoch nur, wenn der Umschalter **Flip Enable** aktiv ist.
:::

---

## Bereich BLOW

Der Bereich **Blow Enable** steuert die Aktivierung und die Parameter des Blassystems während des Jogs.

| Steuerung | Beispielwert | Beschreibung |
|---|---|---|
| **Blow Enable** (Umschalter) | Aktiv (rot) | Aktiviert die automatische Blasluft während des Jogs |
| **Blow Duration** | 200 ms | Dauer des Blasimpulses |
| **Blow Pression** | 3,00 Bar | Für die Blasluft verwendeter Luftdruck |
| **Blow Pause** | 200 ms | Pause zwischen einem Blasimpuls und dem nächsten während des Jogs |
| **Blow Type** | BLOWc + BLOWe | Aktivierte Art der Blasluft. Die Optionen kombinieren zentrale Blasluft (BLOWc) und/oder äußere Blasluft (BLOWe) |

### Optionen für Blow Type

| Wert | Beschreibung |
|---|---|
| **BLOWc** | Nur zentrale Blasluft |
| **BLOWe** | Nur äußere Blasluft |
| **BLOWc + BLOWe** | Beide Blasluftarten gleichzeitig aktiviert |

---

## Bereich BACKLIGHT

Der Bereich **Backlight** steuert den Zustand der Hintergrundbeleuchtungen unabhängig vom Jog.

| Steuerung | Beschreibung |
|---|---|
| **Backlight 1** (Umschalter) | Aktiviert/deaktiviert die Hintergrundbeleuchtung 1 |
| **Backlight 2** (Umschalter) | Aktiviert/deaktiviert die Hintergrundbeleuchtung 2 |

Die Umschalter zeigen Rot, wenn das Backlight **eingeschaltet** ist.

---

## Starten und Stoppen des Jogs

| Schaltfläche | Funktion |
|---|---|
| **START JOG** | Startet die kontinuierliche Drehung des FlexiBowl® mit den eingestellten Parametern und aktiviert gleichzeitig Flip und Blow, wenn die jeweiligen Umschalter aktiviert sind |
| **STOP JOG** | Beendet den Jog und stoppt den FlexiBowl® |

:::{important}
Vor dem Drücken von **START JOG** prüfen, dass:
- der Motor aktiviert ist (**ENABLE MOTOR** aktiv)
- der Systemstatus **READY** lautet
- die Parameter Speed, Flip und Blow korrekt eingestellt sind, um unerwünschte Bewegungen zu vermeiden
:::

:::{warning}
Während des Jogs dreht sich der FlexiBowl® kontinuierlich. Vor dem Start des Jogs sicherstellen, dass der Bereich um den FlexiBowl® frei von Hindernissen ist und sich keine Personen in Kontakt mit den beweglichen Teilen befinden.
:::
