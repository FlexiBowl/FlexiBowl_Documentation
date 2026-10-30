(tracking)=
# **Circular-Tracking-Modus**

## Betrieb im Tracking

Die Option **Circular Tracking** maximiert die Produktivität des FlexiBowl®, indem sie ihn kontinuierlich und ohne Unterbrechung drehen lässt.
 Anstatt in jedem Zyklus anzuhalten, um das Foto aufzunehmen und dem Roboter Zeit zu geben, die im Sichtbereich befindlichen Teile zu entnehmen, verfolgt ein Encoder den Drehwinkel, den die Oberfläche der starren Scheibe vom Moment der Aufnahme bis zum Moment der Entnahme des Teils durch den Roboter zurückgelegt hat.

:::{figure} ../../../../_shared/media/images/Tracking.png
:width: 50%
:align: center
:::

:::{image} ../../../../_shared/media/videos/TRACKING_MODE.GIF
:width: 100%
:align: center
:::

::::{tip}
Der Betrieb im Circular Tracking verschiebt den Entnahmebereich, der normalerweise mit dem Sichtbereich zusammenfällt und in diesem Fall nachgelagert verschoben ist.
 Weitere Informationen zur empfohlenen Platzierung des Roboters und des übrigen Zubehörs bei Standardbetrieb und Circular Tracking finden sich im Kapitel {ref}`Layout Best Practice <layoutbp>`.

:::{figure} ../../../../_shared/media/images/TrackingLayout.PNG
:width: 80%
:align: center
:::

::::
---

## Hauptmerkmale

<div class="tracking-features">

| Merkmal | Beschreibung |
|---|---|
| **Leistung** | Ideal zur Maximierung der Leistung (bis zu 100 %) |
| **Sichtbereich** | Ein Sektor vor dem Entnahmebereich |
| **Parallelität** | Hopper-Entladung, Bewegung/Impuls des FlexiBowl®, Bildverarbeitung und Entnahme laufen gleichzeitig ab |
| **Stabilität** | Höhere Stabilität der momentanen Zykluszeit |
| **Genauigkeit** | Geringere Genauigkeit als im Standardmodus |

</div>

---

## Betriebszyklus

Der Betrieb im Circular Tracking basiert auf einem kontinuierlichen Zyklus, der in vier parallel ablaufende Phasen unterteilt ist:

```{list-table}
:header-rows: 1
:widths: 20 80

* - Phase
  - Beschreibung
* - **Detect**
  - Die Kamera erfasst das Bild eines Sektors des FlexiBowl® und nimmt damit den Entnahmebereich vorweg.
* - **Move**
  - Der Bowl dreht sich kontinuierlich, ohne anzuhalten; der Encoder erfasst die Winkelverschiebung in Echtzeit.
* - **Flip / Drop**
  - Nicht korrekt ausgerichtete Teile werden gewendet oder in die richtige Position entladen.
* - **Pick**
  - Der Roboter entnimmt die Teile und kompensiert dabei die Bewegung des FlexiBowl® anhand der Encoderdaten.
```

---

## Erforderliche Hardware und Software

Zur Aktivierung des Circular Tracking sind die folgenden Komponenten erforderlich:

- Option **Circular Tracking** am FlexiBowl®, in der Preisliste erhältlich für:

  | Baugröße | Preislistencode |
  |---|---|
  | FlexiBowl® 500 | Circular Tracking 500C · Circular Tracking 500CC |
  | FlexiBowl® 650 | Circular Tracking 650CC |
  | FlexiBowl® 800 | Circular Tracking 800C · Circular Tracking 800CC |
  | FlexiBowl® 1200 | Circular Tracking 1200C · Circular Tracking 1200CC |

- Option **Conveyor Tracking** an der Robotersteuerung

(schema-di-collegamento)=
### Technische Daten des Encoders

Die Option Circular Tracking umfasst einen mit der Rotation der Scheibe verbundenen Encoder. Das Encodersignal wird im Inneren des FlexiBowl® aufgeteilt und sowohl an den Motortreiber als auch an die Robotersteuerung gesendet.

:::{list-table}
:widths: 35 65
:stub-columns: 1

* - Modell
  - 
* - Max. Impulszahl
  - 49152 / 65536 Impulse/Umdrehung, je nach Geschwindigkeit des FlexiBowl®
* - Kommunikationsschnittstelle
  - Inkremental, TTL / HTL (Werkseinstellung: TTL)
* - Zertifizierungen
  - EU-Konformitätserklärung · UK-Konformitätserklärung · ACMA-Konformitätserklärung · Marokko-Konformitätserklärung · China RoHS · cULus
* - Anschluss am FlexiBowl®
  - {ref}`Encoder-Kabeldurchführung <io-flexitrack>`
:::

---
## Seite JOG 

Die Seite **Jog Motor** ermöglicht es, den FlexiBowl® im Circular-Tracking-Modus zu betreiben, ohne programmierte Sequenzen zu verwenden. Sie wird hauptsächlich bei Einrichtung, Inbetriebnahme und Test des Systems eingesetzt und erlaubt dem Bediener, die Drehung des FlexiBowl® und die Zusatzfunktionen direkt zu steuern.
![Seite Jog Motor](../../../../_shared/media/images/jog_motor.png)

Weitere Informationen finden Sie auf der [Seite JOG](jog)

#### Comandi EXE JOG

| Befehl | ControlWord | Busy während der Ausführung | ReturnData_1 | Erläuterung | 
|---|---|---|---|---|
| Start Jog Seq | 40 | JA | 40 | Jog starten |
| Stop Jog Seq | 41 | JA | 41 | Jog stoppen |

#### Comandi WRITE JOG

Die Jog-Befehle (kontinuierlicher manueller Betrieb) lassen sich separat über ControlWord im Block 20000 konfigurieren.

| Befehl | ControlWord | Range Data_1 | Hinweise |
|---|---|---|---|
| AccelerationJog | 20001 | 0–100 | Jog-Beschleunigungsrampe (%) |
| DecelerationJog | 20002 | 0–100 | Jog-Verzögerungsrampe (%) |
| SpeedJog | 20003 | 0–100 | Jog-Geschwindigkeit (%). Werte 1000–1100 = negative Geschwindigkeit (Drehrichtungsumkehr) |
| FlipJog_Enable | 20004 | 0–1 | 0 = Flip deaktiviert, 1 = Flip während des Jog aktiviert |
| FlipJog_Duration | 20005 | 0–1000 | Dauer des Flip-Impulses (ms) |
| FlipJog_Pressure | 20006 | 0–600 | Flip-Druck (/100 = Bar) |
| FlipJog_Pause | 20007 | 0–1000 | Pause zwischen aufeinanderfolgenden Flips (ms) |
| BlowJog_Enable | 20008 | 0–1 | 0 = Blow deaktiviert, 1 = Blow während des Jog aktiviert |
| BlowJog_Duration | 20009 | 0–1000 | Dauer des Blow-Impulses (ms) |
| BlowJog_Pressure | 20010 | 0–600 | Blow-Druck (/100 = Bar) |
| BlowJog_Pause | 20011 | 0–1000 | Pause zwischen aufeinanderfolgenden Blows (ms) |
| BlowJog_Type | 20012 | 0–2 | Blow-Typ: 0 = BLOWc, 1 = BLOWe, 2 = BLOWc+BLOWe |
| Backlight_1 | 20013 | 0–1 | 0 = aus, 1 = ein |
| Backlight_2 | 20014 | 0–1 | 0 = aus, 1 = ein |

#### Comandi READ JOG

Dieselben schreibbaren JOG-Befehle (Block 20000) können im Block 20100 gelesen werden:

| Befehl | READ-ControlWord | Bereich ReturnData_2 |
|---|---|---|
| AccelerationJog | 20101 | 0–100 |
| DecelerationJog | 20102 | 0–100 |
| SpeedJog | 20103 | 0–100 (1000–1100 = negativ) |
| FlipJog_Enable | 20104 | 0–1 |
| FlipJog_Duration | 20105 | 0–1000 |
| FlipJog_Pressure | 20106 | 0–600 (/100) |
| FlipJog_Pause | 20107 | 0–1000 |
| BlowJog_Enable | 20108 | 0–1 |
| BlowJog_Duration | 20109 | 0–1000 |
| BlowJog_Pressure | 20110 | 0–600 (/100) |
| BlowJog_Pause | 20111 | 0–1000 |
| BlowJog_Type | 20112 | 0–2 |
| Backlight_1 | 20113 | 0–1 |
| Backlight_2 | 20114 | 0–1 |

::::{tip}
Die Fehlercodes sind auf der entsprechenden Seite zu finden.
:::{card} ZUR ENTSPRECHENDEN SEITE
:link: sec-err
:link-type: ref
:class-card: isw-card-field
:class-body: isw-card-body
:::
::::

---
## Vorteile 


:::{grid-item-card} Vorteile
- **Geschwindigkeit**: .
- **Stabilität der Zykluszeit**: .
- **Geringer Platzbedarf**: .
:::

---
## Betriebshinweise

:::{warning}
Der Circular-Tracking-Modus bietet maximale Leistung, jedoch mit **etwas geringerer Genauigkeit** als der Standardmodus. Die Eignung anhand der Toleranzanforderungen des zu handhabenden Bauteils beurteilen.
:::

:::{note}
Zur Konfiguration des Offset-Parameters zwischen Sichtbereich und Entnahmebereich siehe den Abschnitt zur Softwarekonfiguration des Systems.
:::

