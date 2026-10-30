
# **Main Command**

## Descripción general

La página **Main Command** es la sección operativa principal de la interfaz de software del FlexiBowl®. Permite al operador configurar y probar los parámetros de movimiento y de las opciones accesorias del sistema.

La página se divide en **tres subpáginas**, seleccionables mediante el menú desplegable central situado bajo la barra de navegación, con la etiqueta **«Chose Visualization Page»**:

| Subpágina | Descripción resumida |
|---|---|
| **OPTION** | Parámetros para flip, blow y retroiluminación |
| **MOVE** | Parámetros del movimiento rotatorio del FlexiBowl® |
| **SHAKE** | Parámetros del movimiento oscilatorio del FlexiBowl® |

---

## Subpágina: OPTION

La subpágina **OPTION** reúne los parámetros relativos a las funciones accesorias del FlexiBowl®: el sistema de vuelco de componentes (flip), el sistema de soplado (blow) y la retroiluminación (backlight).
![página option](../../../../_shared/media/images/main_command_option.png)

| Parámetro | Unidad | Descripción |
|---|---|---|
| **Flip Pressure** | Bar  | Presión de aire utilizada para el accionamiento del flip. Regulable mediante deslizador |
| **Flip Count** | N.º  | Número de flips realizados en secuencia durante un ciclo |
| **Flip Delay** | ms  | Intervalo de tiempo entre un flip y el siguiente |
| **Blow Pressure** | Bar  | Presión de aire utilizada para el soplado de los componentes en el FlexiBowl® |
| **Blow Time** | ms  | Duración del impulso de soplado |

Cada parámetro es regulable mediante un **deslizador horizontal**; el valor actual se muestra en el recuadro numérico situado a la derecha del deslizador.

### Controles de la retroiluminación

| Control | Descripción |
|---|---|
| **Backlight_1** | Interruptor on/off de la retroiluminación 1  |
| **Backlight_2** | Interruptor on/off de la retroiluminación 2  |

Los interruptores se muestran en rojo cuando la retroiluminación está **activa**.

### Botones de prueba

En la parte inferior de la página hay tres botones para probar las funciones en tiempo real:

| Botón | Función |
|---|---|
| **TEST FLIP** | Ejecuta un flip con los parámetros establecidos actualmente |
| **TEST BLOWe** | Activa el soplado externo (blow externo) con los parámetros establecidos |
| **TEST BLOWc** | Activa el soplado central (blow central) con los parámetros establecidos |

:::{attention}  
 Antes de ejecutar las pruebas, asegurarse de que el motor esté habilitado (botón **ENABLE MOTOR** activo) y de que el estado del sistema sea **READY**.
:::

---

## Subpágina: MOVE

La subpágina **MOVE** permite configurar los parámetros del movimiento rotatorio del FlexiBowl® y probarlo directamente desde la interfaz.
![página move](../../../../_shared/media/images/main_command_move.png)

| Parámetro | Unidad | Valor predeterminado | Descripción |
|---|---|---|---|
| **Acceleration** | % | 50 | Rampa de aceleración del motor al inicio del movimiento. Valores más altos producen un arranque más brusco |
| **Deceleration** | % | 50 | Rampa de deceleración del motor durante la parada. Valores más altos producen una parada más brusca |
| **Speed** | % | 50 | Velocidad de rotación del FlexiBowl® durante el movimiento |
| **Angle** | Grado | 45 | Ángulo de rotación recorrido por el FlexiBowl® durante cada movimiento |

Cada parámetro es regulable mediante un **deslizador horizontal**; el valor actual se muestra en el recuadro numérico situado a la derecha del deslizador.

### Botón de prueba

| Botón | Campo contiguo | Función |
|---|---|---|
| **TEST MOVE** | Tiempo de ejecución (ms) | Ejecuta un movimiento de rotación con los parámetros establecidos actualmente. El campo de la derecha muestra la duración real del último movimiento ejecutado, en milisegundos |

:::{note}  
 El campo **ms** muestra el tiempo real que tarda el bowl en completar el movimiento establecido. Este valor es útil para sincronizar el FlexiBowl® con el sistema de visión artificial.
:::

:::{attention}   
Antes de ejecutar la prueba, asegurarse de que el motor esté habilitado (botón **ENABLE MOTOR** activo) y de que el estado del sistema sea **READY**.
:::

---

## Subpágina: SHAKE

La subpágina **SHAKE** permite configurar los parámetros del movimiento oscilatorio del FlexiBowl® (shake), utilizado para redistribuir los componentes en el plato, y probarlo directamente desde la interfaz.
![página shake](../../../../_shared/media/images/main_command_shake.png)

| Parámetro | Unidad | Valor predeterminado | Descripción |
|---|---|---|---|
| **Acceleration** | % | 50 | Rampa de aceleración del motor durante la fase de shake |
| **Deceleration** | % | 50 | Rampa de deceleración del motor durante la fase de shake |
| **Speed** | % | 50 | Velocidad de rotación durante el movimiento de shake |
| **Ccw Angle** | Grado | -45 | Ángulo de rotación en sentido **antihorario** (Counter-ClockWise) durante cada oscilación |
| **Cw Angle** | Grado | 45 | Ángulo de rotación en sentido **horario** (ClockWise) durante cada oscilación |
| **Count** | N.º | 2 | Número de oscilaciones completas realizadas durante un ciclo de shake |

Cada parámetro es regulable mediante un **deslizador horizontal**; el valor actual se muestra en el recuadro numérico situado a la derecha del deslizador.

:::{note}  
 El movimiento de **shake** consiste en una serie de rotaciones alternadas en sentido horario y antihorario, definidas respectivamente por **Cw Angle** y **Ccw Angle**. El número de oscilaciones completas se controla mediante el parámetro **Count**.
:::

### Botón de prueba

| Botón | Campo contiguo | Función |
|---|---|---|
| **TEST SHAKE** | Tiempo de ejecución (ms) | Ejecuta un ciclo de shake con los parámetros establecidos actualmente. El campo de la derecha muestra la duración real del último shake ejecutado, en milisegundos |

:::{attention}  
 Antes de ejecutar la prueba, asegurarse de que el motor esté habilitado (botón **ENABLE MOTOR** activo) y de que el estado del sistema sea **READY**.
:::