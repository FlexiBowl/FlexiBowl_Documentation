(layoutbp)=
# **Layout Best Practice**

El área de trabajo del FlexiBowl® está dividida virtualmente en cuatro sectores, cada uno dedicado a una fase del ciclo: **liberación** de los componentes desde el Bulk Feeder, **separación** mediante flip, **toma** por parte del robot y **recirculación** de los componentes no tomados. Una buena disposición respeta esta secuencia en el sentido de rotación del FlexiBowl® y reduce al mínimo los recorridos de *pick and place*.

:::{figure} ../../../../_shared/media/images/Funz-standard.PNG
:align: center
:width: 50%

Sectores de trabajo del FlexiBowl®: liberación, separación, toma y recirculación.
:::

## Directrices para el posicionamiento del robot

:::{tip}
La mejor forma de colocar el robot respecto al FlexiBowl® es la que minimiza los recorridos de *pick and place*.
:::

(layoutbp-traditional)=
### Traditional Feeding

En el {ref}`Traditional Feeding <sof-modalita-standard>` el área de toma coincide con el área de visión. Por lo tanto, el área de trabajo del robot debe cubrir por completo el área de visión, de modo que se garantice que el robot pueda alcanzar todos los componentes identificados como tomables.

<!-- DA COMPLETARE: distanze consigliate robot/FlexiBowl® per taglia -->

(layoutbp-tracking)=
### Circular Tracking

En el {ref}`Circular Tracking <tracking>` el FlexiBowl® gira de forma continua: el área de visión se encuentra un sector **aguas arriba** del área de toma, que por tanto queda desplazada **aguas abajo** en el sentido de rotación. El área de trabajo del robot debe cubrir el sector de toma situado aguas abajo del área de visión.

:::{figure} ../../../../_shared/media/images/TrackingLayout.PNG
:width: 80%
:align: center
:::

<!-- DA COMPLETARE -->

## Directrices para el posicionamiento de los Bulk Feeders

### Precauciones generales

- Coloque el Bulk Feeder sobre una superficie estable y horizontal, cerca del FlexiBowl®.
- Si el Bulk Feeder se instala sobre la mesa de una máquina sensible a las vibraciones, coloque material aislante y antivibratorio entre las superficies para evitar que las vibraciones se transmitan al FlexiBowl® (véase {ref}`tramoggia-antivibrazione`).
- Fije el Bulk Feeder al soporte con tornillos M8: 4 orificios para los Bulk Feeders estándar, 2 orificios para el Bulk Feeder de 1,5 l.
- Un único FlexiBowl® gestiona hasta **4 Bulk Feeders**: en el {ref}`Multiple Parts Feeding <funzionamento-in-mix-mode>` es posible dedicar un Bulk Feeder a cada referencia.

### Posición recomendada

La rampa del Bulk Feeder debe descargar los componentes directamente en el **sector de liberación**, aguas arriba del flip, con una inclinación que siga el perfil del FlexiBowl®.

::::{tab-set}
:::{tab-item} Posicionamiento correcto
![Posicionamiento correcto del Bulk Feeder respecto al FlexiBowl®](../../../../_shared/media/images/posizione_giustatramoggia.png)
:::
:::{tab-item} Posicionamiento incorrecto
![Ejemplo de posicionamiento incorrecto del Bulk Feeder](../../../../_shared/media/images/posizione_sbagliatatramoggia.png)

Una rampa demasiado alejada del área de trabajo genera una alimentación irregular y penaliza el rendimiento de la aplicación.
:::
::::

## Directrices para el posicionamiento de los puntos de depósito

### Indicaciones generales

Coloque los puntos de depósito (bandejas, cintas, estaciones de montaje) lo más cerca posible del área de toma, para reducir el recorrido del robot en cada ciclo.

<!-- DA COMPLETARE -->

### Posición recomendada

<!-- DA COMPLETARE -->

## Directrices para la configuración óptima del movimiento

<!-- DA COMPLETARE -->

## Directrices para la elección de la herramienta de agarre

<!-- DA COMPLETARE -->

## Directrices para el posicionamiento del Toplight

El {ref}`Toplight <toplight>` debe estar centrado sobre el área de visión, con la superficie emisora paralela al plano del FlexiBowl® y la cámara montada en el orificio central. La distancia a la superficie debe ser similar a la de la cámara, para reducir las sombras y los reflejos directos. Para los métodos de fijación, véase {ref}`montaggio_staffa`.

## Directrices para el posicionamiento de la cámara

La cámara debe estar centrada sobre el área de visión, con el eje óptico perpendicular a la superficie del FlexiBowl® y, si existe, concéntrica con el Toplight. La calibración con la rejilla ARS debe realizarse con el Backlight encendido y el Toplight apagado.

<!-- DA COMPLETARE: altezze di montaggio e ottiche consigliate per taglia -->
