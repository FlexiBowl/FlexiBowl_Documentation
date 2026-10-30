# **Mix-Modus**

(funzionamento-in-mix-mode)=
## Betrieb im MIX-Modus

Der **Mix-Modus** ermöglicht es, Teile unterschiedlicher Typen gleichzeitig auf derselben Oberfläche des FlexiBowl® zuzuführen.

Dieser Modus eignet sich besonders für **Sortieranwendungen** (Sorting), bei denen mehrere Referenzen auf derselben Arbeitsfläche vorhanden sein müssen, ohne die Roboterstationen vervielfachen zu müssen.

```{figure}  ../../../../_shared/media/images/flexibowl_standard_cycle.jpg
:align: center
:width: 50%
:alt: *Betriebszyklus im Mix-Modus: Detect → Pick-Drop → Move-Flip*
```

```{image}  ../../../../_shared/media/videos/MIX_MODE.gif
:align: center
:width: 100%
:alt: *Betriebszyklus im Mix-Modus: Detect → Pick-Drop → Move-Flip*
```
---

## Hauptmerkmale

| Merkmal | Beschreibung |
|---|---|
| **Anwendung** | Ideal für Sortieranwendungen mit mehreren Teiletypen |
| **Flexibilität** | Zuführung gemischter Teile auf derselben Oberfläche |

---

## Betriebszyklus

Der Zyklus des MIX-Modus ist gegenüber dem Standardmodus vereinfacht, mit nur drei Stufen, die sich nacheinander wiederholen:

```{list-table}
:header-rows: 1
:widths: 20 80

* - Phase
  - Beschreibung
* - **Detect**
  - Die Kamera erfasst das Bild der gemeinsamen Oberfläche und erkennt Position und Ausrichtung aller vorhandenen Teile, unabhängig von ihrem Typ.
* - **Move-Flip**
  - Der FlexiBowl® dreht sich, und nicht korrekt ausgerichtete Teile werden gewendet oder neu positioniert.
* - **Pick-Drop**
  - Der Roboter entnimmt das richtige Teil gemäß der Sortierlogik und legt es an der Zielposition ab.
```


---
## Vorteile 


:::{grid-item-card} Vorteile
- **Maximale Flexibilität**: .
- **Geringere Kosten**: .
- **Geringer Platzbedarf**: .
:::


:::{note}
Der Mix-Modus ist für FlexiBowl® 500, 650 und 800 verfügbar.
:::

---
## Betriebshinweise

:::{tip}
Der Mix-Modus erfordert gegenüber einer Standardkonfiguration keine zusätzliche Hardware.
 Es genügt, die Bildverarbeitungssoftware auf die Erkennung mehrerer Referenzen zu konfigurieren und die Sortierlogik im Roboterprogramm einzustellen.
:::

:::{note}
Für die optimale Platzierung von FlexiBowl® und Roboter siehe das Kapitel {ref}`Layout Best Practice <layoutbp>`.
:::
