# **Standardmodus**

Der **Standardmodus** ist die Standard-Betriebskonfiguration des FlexiBowl® und eignet sich für jede Art von robotergestützter Zuführanwendung. In diesem Modus teilen sich Roboter und Bildverarbeitungssystem denselben Arbeitsbereich und arbeiten koordiniert und nacheinander, um eine hohe Zyklusleistung zu gewährleisten.

---

## Funktionsprinzip

Im Standardmodus führt der FlexiBowl® einen kontinuierlichen Zyklus aus drei Hauptphasen aus, die sich nacheinander wiederholen:

```{figure} ../../../../_shared/media/images/flexibowl_standard_cycle.jpg
:align: center
:width: 50%
:alt: *Betriebszyklus im Standardmodus: Detect → Pick-Drop → Move-Flip*
```
```{image} ../../../../_shared/media/videos/STANDARD_MODE.gif
:align: center
:width: 100%
:alt: *Betriebszyklus im Standardmodus: Detect → Pick-Drop → Move-Flip*
```

### 1. Detect (Erkennung)

Das Bildverarbeitungssystem erfasst ein Bild der Oberfläche des FlexiBowl® und erkennt Position, Ausrichtung und Typ der vorhandenen Bauteile. Die Informationen werden an den Roboter übermittelt, um die Entnahmevorgänge zu planen.

### 2. Pick-Drop (Entnahme und Ablage)

Der Roboter entnimmt die korrekt ausgerichteten Bauteile aus dem FlexiBowl® und legt sie an der Zielposition ab (z. B. Tray, Förderband, Montagestation). Bildverarbeitung und Entnahme werden **nacheinander** ausgeführt: Zuerst scannt das Bildverarbeitungssystem die Szene, dann greift der Roboter ein.

### 3. Move-Flip (Bewegung und Wenden)

Nach der Entnahme führt der FlexiBowl® eine kombinierte Dreh- und Vibrationsbewegung (**Flip**) aus, um die verbleibenden Bauteile neu zu durchmischen und die korrekte Präsentation neuer Teile zu begünstigen. Gleichzeitig erfolgen die **Entladung des Hoppers** und die **Bewegung des Bowls** **simultan**, wodurch die Zykluszeiten optimiert werden.

---

## Hauptmerkmale

| Merkmal | Beschreibung |
|---|---|
| **Gemeinsamer Arbeitsbereich** | Roboter und Bildverarbeitungssystem arbeiten im selben Bereich des FlexiBowl® |
| **Anwendbarkeit** | Für alle Anwendungsarten geeignet |
| **Hopper-Entladung** | Erfolgt gleichzeitig mit der Bewegung/dem Impuls des FlexiBowl® |
| **Bildverarbeitung und Entnahme** | Erfolgen nacheinander |
| **Zyklusmessung** | Die Zykluszeit wird auf Minutenbasis gemessen |

---

## Schema des Betriebszyklus

Der Zyklus läuft nach folgendem Regelkreisschema ab:

1. **Detect** — Das Bildverarbeitungssystem scannt den FlexiBowl® und lokalisiert die Bauteile.
2. **Pick-Drop** — Der Roboter entnimmt die erkannten Teile und legt sie am Ziel ab.
3. **Move-Flip** — Der FlexiBowl® durchmischt die Bauteile für den nächsten Zyklus neu.
4. Der Zyklus beginnt wieder bei Punkt 1.

:::{note} 
Während der Phase Move-Flip erfolgt die Entladung des Hoppers parallel zur Bewegung des FlexiBowl®, wodurch Totzeiten reduziert und die Produktivität maximiert werden.
:::

---
## Layoutbeispiel

:::{figure} ../../../../_shared/media/images/Funz-standard.PNG
:align: center
:width: 60%

Layoutbeispiel im Standardmodus: Der Bulk Feeder entlädt in den Abgabesektor, der Flip vereinzelt die Bauteile, der Roboter entnimmt im Sichtbereich und die nicht entnommenen Teile werden zurückgeführt.
:::

Der Arbeitsbereich des Roboters muss den Sichtbereich vollständig abdecken, damit der Roboter alle als greifbar erkannten Bauteile erreichen kann. Zur Positionierung von Roboter, Bulk Feeder, Ablageplätzen, Kamera und Beleuchtung siehe {ref}`Layout Best Practice <layoutbp-traditional>`.


---

## Vorteile 


:::{grid-item-card} Vorteile
- **Genauigkeit**: .
- **Vereinzelung**: .
- **Geschwindigkeit**: .
:::
