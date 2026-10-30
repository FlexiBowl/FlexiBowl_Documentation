(layoutbp)=
# **Layout Best Practice**

Der Arbeitsbereich des FlexiBowl® ist virtuell in vier Sektoren unterteilt, die jeweils einer Phase des Zyklus gewidmet sind: **Abgabe** der Bauteile aus dem Bulk Feeder, **Vereinzelung** durch Flip, **Entnahme** durch den Roboter und **Rückführung** der nicht entnommenen Bauteile. Ein gutes Layout berücksichtigt diese Reihenfolge in Drehrichtung des FlexiBowl® und minimiert die *Pick-and-Place*-Wege.

:::{figure} ../../../../_shared/media/images/Funz-standard.PNG
:align: center
:width: 50%

Arbeitssektoren des FlexiBowl®: Abgabe, Vereinzelung, Entnahme und Rückführung.
:::

## Richtlinien für die Positionierung des Roboters

:::{tip}
Die beste Art, den Roboter relativ zum FlexiBowl® zu platzieren, ist diejenige, die die *Pick-and-Place*-Wege minimiert.
:::

(layoutbp-traditional)=
### Traditional Feeding

Beim {ref}`Traditional Feeding <sof-modalita-standard>` fällt der Entnahmebereich mit dem Sichtbereich zusammen. Der Arbeitsbereich des Roboters muss daher den Sichtbereich vollständig abdecken, damit der Roboter alle als greifbar erkannten Bauteile erreichen kann.

<!-- DA COMPLETARE: distanze consigliate robot/FlexiBowl® per taglia -->

(layoutbp-tracking)=
### Circular Tracking

Beim {ref}`Circular Tracking <tracking>` dreht sich der FlexiBowl® kontinuierlich: Der Sichtbereich liegt einen Sektor **vor** dem Entnahmebereich, der somit in Drehrichtung **nachgelagert** verschoben ist. Der Arbeitsbereich des Roboters muss den Entnahmesektor nach dem Sichtbereich abdecken.

:::{figure} ../../../../_shared/media/images/TrackingLayout.PNG
:width: 80%
:align: center
:::

<!-- DA COMPLETARE -->

## Richtlinien für die Positionierung der Bulk Feeder

### Allgemeine Vorsichtsmaßnahmen

- Den Bulk Feeder auf einer stabilen, waagerechten Fläche in der Nähe des FlexiBowl® aufstellen.
- Wird der Bulk Feeder auf dem Tisch einer vibrationsempfindlichen Maschine installiert, zwischen den Oberflächen Isolier- und Schwingungsdämpfungsmaterial einlegen, damit sich die Vibrationen nicht auf den FlexiBowl® übertragen (siehe {ref}`tramoggia-antivibrazione`).
- Den Bulk Feeder mit M8-Schrauben an der Halterung befestigen: 4 Bohrungen bei Standard-Bulk-Feedern, 2 Bohrungen beim Bulk Feeder mit 1,5 l.
- Ein einzelner FlexiBowl® verwaltet bis zu **4 Bulk Feeder**: Beim {ref}`Multiple Parts Feeding <funzionamento-in-mix-mode>` kann jeder Referenz ein eigener Bulk Feeder zugeordnet werden.

### Empfohlene Position

Die Rutsche des Bulk Feeders muss die Bauteile direkt in den **Abgabesektor** vor dem Flip entladen, mit einer Neigung, die dem Profil des FlexiBowl® folgt.

::::{tab-set}
:::{tab-item} Korrekte Positionierung
![Korrekte Positionierung des Bulk Feeders in Bezug auf den FlexiBowl®](../../../../_shared/media/images/posizione_giustatramoggia.png)
:::
:::{tab-item} Falsche Positionierung
![Beispiel für eine falsche Positionierung des Bulk Feeders](../../../../_shared/media/images/posizione_sbagliatatramoggia.png)

Eine Rutsche, die zu weit vom Arbeitsbereich entfernt ist, führt zu einer ungleichmäßigen Zuführung und beeinträchtigt die Leistung der Anwendung.
:::
::::

## Richtlinien für die Positionierung der Ablageplätze

### Allgemeine Hinweise

Die Ablageplätze (Trays, Förderbänder, Montagestationen) so nah wie möglich am Entnahmebereich platzieren, um den Verfahrweg des Roboters bei jedem Zyklus zu verkürzen.

<!-- DA COMPLETARE -->

### Empfohlene Position

<!-- DA COMPLETARE -->

## Richtlinien für die optimale Konfiguration der Bewegung

<!-- DA COMPLETARE -->

## Richtlinien für die Wahl des Greifwerkzeugs

<!-- DA COMPLETARE -->

## Richtlinien für die Positionierung des Toplight

Das {ref}`Toplight <toplight>` muss auf den Sichtbereich zentriert sein, mit der Lichtaustrittsfläche parallel zur Ebene des FlexiBowl® und der im zentralen Loch montierten Kamera. Der Abstand zur Oberfläche sollte dem der Kamera ähneln, um Schatten und direkte Reflexionen zu reduzieren. Zu den Befestigungsarten siehe {ref}`montaggio_staffa`.

## Richtlinien für die Positionierung der Kamera

Die Kamera muss auf den Sichtbereich zentriert sein, mit der optischen Achse senkrecht zur Oberfläche des FlexiBowl® und, falls vorhanden, konzentrisch zum Toplight. Die Kalibrierung mit dem ARS-Raster ist bei eingeschaltetem Backlight und ausgeschaltetem Toplight durchzuführen.

<!-- DA COMPLETARE: altezze di montaggio e ottiche consigliate per taglia -->
