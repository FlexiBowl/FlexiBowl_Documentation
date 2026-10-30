(diverter)=
# **Standard-Abweiser**

Standard-Abweiser sind Polyethylenblöcke mit geformten Oberflächen, die einen Rutscheffekt für die Bauteile erzeugen, während sie sich zusammen mit der Oberfläche bzw. der starren Scheibe bewegen. Der Grundgedanke der Abweiser (Standard oder anderer Typen) besteht darin, die Position der Teile entlang des Radius des FlexiBowl® zu verändern, um die Wirksamkeit des Flips zu maximieren und sie in einem solchen Abstand zum Rückhaltering und zur Scheibenspannkappe zu halten, dass der Roboter sie greifen kann, ohne dass der *End Effector* mit einem der beiden kollidiert.

:::{figure} ../../../../_shared/media/images/deviatorisup.PNG
:width: 100%
Abweiser auf Oberfläche (FlexiBowl® 500-650-800-1200)
:::

## Empfohlene Anwendungen 
Standardmäßig montierte Option; sie eignet sich für die Handhabung von Bauteilen ohne Vorsprünge, die klein genug sind, um sich zwischen Abweiser und Scheibe zu verklemmen.

## Montageverfahren

:::{warning} Attenzione
Vor der Montage sicherstellen, dass der FlexiBowl® **ausgeschaltet ist und stillsteht**.
:::

%### Deviatori per disco rigido (FlexiBowl® 350-500E)

%:::{note}
%Nei FlexiBowl® con disco rigido i deviatore non sono fissati di default.
%:::

%I deviatori sono fissati sugli appositi fori ai lati dello schermo flip tramite due viti M6x22 ciascuno.

%:::{figure} ../../../../_shared/media/images/deviatoridisco_fissaggio.PNG
%:width: 100%
%:::

%### Deviatori per superficie (FlexiBowl® 500-650-800-1200)

| Schritt | Vorgang |
|:----:|-----------|
| 1 | Den Abweiser in die dafür vorgesehene Aussparung im Rückhaltering einsetzen |
| 2 | Mit einem Schlitzschraubendreher die Einstellschrauben eindrehen, bis sich der Abweiser auf der gewünschten Höhe befindet |
| 3 | Mit den Klemmschrauben den Abweiser in Position fixieren |

:::{figure} ../../../../_shared/media/images/deviatorisup_componenti.PNG
:width: 100%
:::

## Einstellverfahren

:::{warning} Attenzione
Vor der Einstellung sicherstellen, dass der FlexiBowl® **ausgeschaltet ist und stillsteht**.
:::

### Abweiser für starre Scheibe (FlexiBowl® 350-500E)

| Schritt | Vorgang |
|:----:|-----------|
| 1 | Die Schrauben für die radiale und vertikale Einstellung lösen |
| 2 | Ein Blatt Papier zwischen Scheibe und Abweiser legen, um den richtigen Abstand einzuhalten, und die Schrauben der vertikalen Einstellung festziehen |
| 3 | Ein Blatt Papier zwischen die Außenfläche des Abweisers und die Innenfläche des Scheibenrands legen, um den richtigen Abstand einzuhalten, und die Schrauben der %radialen Einstellung festziehen |

%:::{figure} ../../../../_shared/media/images/deviatoridisco_regolazione.PNG
%:width: 100%
%:::

### Abweiser auf Oberfläche (FlexiBowl® 500-650-800-1200)

:::{list-table}
:header-rows: 1
:widths: 10 90
:align: left

* - Schritt
  - Vorgang
* - 1
  - Die Stopfen an der Abweiserkartusche entfernen
* - 2
  - Die Befestigungsschrauben (2) lösen
* - 3
  - Die Einstellschrauben (1) lösen oder eindrehen, bis sich die Unterseite des Abweisers in ca. 0,1 mm Abstand zur Scheibenoberfläche befindet.

    :::{tip}
    Ein Blatt Papier zwischen Scheibe und Abweiser legen, um den richtigen Abstand einzuhalten, und die Schrauben der vertikalen Einstellung festziehen.
    :::
* - 4
  - Die Befestigungsschrauben (2) festziehen, um den Abweiser in Position zu fixieren
:::

:::{figure} ../../../../_shared/media/images/detdev.PNG
:width: 100%
:::

## Überprüfung der korrekten Funktion 

Die Abweiser sind korrekt eingestellt, wenn die Oberfläche bzw. die starre Scheibe ohne Widerstand gleitet und sich die zu handhabenden Bauteile nicht zwischen beiden verklemmen.

Für einen optimalen Betrieb ist außerdem zu überprüfen, dass:

- der **Abweiser vor dem Flip** die Teile in den Bereich der maximalen Flip-Effizienz bringt, d. h. in den mittleren Bereich;
- der **Abweiser nach dem Flip** die Teile gerade so weit vom Rand entfernt, dass der Roboter sie greifen kann, auch wenn ein Greifer verwendet wird, der den Rand selbst berühren könnte.