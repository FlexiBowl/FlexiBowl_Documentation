(tracking)=
# **Flexitracking**

## Funcionamiento en tracking

La opción Flexitracking permite maximizar la productividad del FlexiBowl® haciéndolo girar de forma continua y sin interrupciones. En lugar de detenerse en cada ciclo para tomar la foto y dar tiempo al robot para recoger las piezas presentes en el área de visión, un encoder registra el ángulo de rotación que ha recorrido la superficie o el disco rígido entre el momento de la captura de la foto y el de la recogida de la pieza por parte del robot.

::::{tip}
El funcionamiento en tracking desplaza el área de recogida que, si normalmente coincide con la de visión, en este caso estará desplazada hacia abajo en el sentido de giro. Consulte el capítulo {ref}`Layout Best Practice <layoutbp>` para más información sobre la colocación recomendada del robot y de los demás accesorios en funcionamiento estándar y en Flexitracking.

:::{figure} ../../../../_shared/media/images/TrackingLayout.PNG
:width: 80%
:align: center
:::

::::

El Flexitracking consiste en un grupo motor modificado con un soporte para una transmisión por correa que acciona el encoder:

:::{figure} ../../../../_shared/media/images/GM001788.PNG
:width: 80%
:align: center
:::

