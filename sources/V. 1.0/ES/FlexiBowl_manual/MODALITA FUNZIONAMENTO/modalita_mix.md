# **Modo Mix**

(funzionamento-in-mix-mode)=
## Funcionamiento en MIX Mode

El **modo Mix** permite alimentar simultáneamente piezas de tipos diferentes sobre la misma superficie del FlexiBowl®.

Este modo es especialmente indicado para aplicaciones de **clasificación** (sorting) en las que se requiere la presencia de varias referencias en el mismo plano de trabajo sin tener que multiplicar las estaciones robotizadas.

```{figure}  ../../../../_shared/media/images/flexibowl_standard_cycle.jpg
:align: center
:width: 50%
:alt: *Ciclo operativo en modo Mix: Detect → Pick-Drop → Move-Flip*
```

```{image}  ../../../../_shared/media/videos/MIX_MODE.gif
:align: center
:width: 100%
:alt: *Ciclo operativo en modo Mix: Detect → Pick-Drop → Move-Flip*
```
---

## Características principales

| Característica | Descripción |
|---|---|
| **Aplicación** | Ideal para aplicaciones de clasificación con varios tipos de piezas |
| **Flexibilidad** | Alimentación de piezas mixtas sobre la misma superficie |

---

## Ciclo operativo

El ciclo del MIX Mode está simplificado respecto al modo estándar, con solo tres etapas que se repiten en secuencia:

```{list-table}
:header-rows: 1
:widths: 20 80

* - Fase
  - Descripción
* - **Detect**
  - La cámara captura la imagen de la superficie común, identificando la posición y la orientación de todas las piezas presentes, independientemente de su tipo.
* - **Move-Flip**
  - El FlexiBowl® gira y las piezas que no están correctamente orientadas se voltean o se reposicionan.
* - **Pick-Drop**
  - El robot toma la pieza correcta según la lógica de clasificación y la deposita en la posición de destino.
```


---
## Ventajas 


:::{grid-item-card} Ventajas
- **Máxima flexibilidad**: .
- **Costes reducidos**: .
- **Menor huella de espacio**: .
:::


:::{note}
El modo Mix está disponible para los FlexiBowl® 500, 650 y 800.
:::

---
## Notas operativas

:::{tip}
El modo Mix no requiere hardware adicional respecto a una configuración estándar.
 Basta con configurar el software de visión para el reconocimiento de varias referencias y establecer la lógica de clasificación en el programa del robot.
:::

:::{note}
Para la colocación óptima del FlexiBowl® y del robot, consulte el capítulo {ref}`Layout Best Practice <layoutbp>`.
:::
