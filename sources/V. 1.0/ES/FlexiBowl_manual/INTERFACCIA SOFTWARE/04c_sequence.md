# **Sequence**

## Descripción general

La página **Sequence** permite crear, modificar y gestionar secuencias operativas personalizadas para el FlexiBowl®. Una secuencia es una lista ordenada de comandos que el sistema ejecuta en sucesión automática, combinando movimientos de rotación (MOVE), oscilación (SHAKE), flip y soplado.

---

## Estructura de la interfaz
![página sequence](../../../../_shared/media/images/sequence.png)

La página se organiza en cuatro áreas principales:

| N.º | Área | Posición | Descripción |
|---|---|---|---|
| 1 | [**Selección de secuencia**](seq) | Arriba a la izquierda | Menú desplegable para seleccionar la secuencia activa |
| 2 | [**Emptying Sequence**](empty) | Arriba en el centro | Interruptor para activar el modo de vaciado |
| 3 | [**Panel de parámetros**](param) | Izquierda | Parámetros de MOVE, SHAKE y OPTION; adición de comandos a la secuencia |
| 4 | [**Panel de comandos**](comm) | Derecha | Lista ordenada de los comandos de la secuencia activa y herramientas de gestión |

---
(seq)=
## 1. Selección de la secuencia

:::{important}
**Antes de cualquier operación**, seleccionar la secuencia que se desea modificar mediante el menú desplegable **«Select the sequence»** situado arriba a la izquierda.
:::

![select the sequence](../../../../_shared/media/images/sequence_combo_box.png)

El sistema admite hasta **20 secuencias independientes** (SEQUENCE 1 – SEQUENCE 20), cada una con su propia lista de comandos y parámetros independientes. La secuencia seleccionada pasa a ser la activa, sobre la que se aplican todas las modificaciones posteriores.

---
(empty)=
## 2. Emptying Sequence

![panel de comandos](../../../../_shared/media/images/empty_sequence.png)

El interruptor **Emptying Sequence** (arriba en el centro) activa un modo en el que la secuencia se ejecuta con el objetivo de vaciar el FlexiBowl® de los componentes presentes. Se utiliza cuando se ha adquirido la opción de vaciado.
Para más información sobre la opción de vaciado, consulte la [página específica](svuotamento).

---
(param)=
## 3. Panel de parámetros

### Parámetros MOVE

| Parámetro | Valor de ejemplo | Descripción |
|---|---|---|
| **Acceleration Move** | 50 % | Rampa de aceleración para el movimiento de rotación |
| **Deceleration Move** | 50 % | Rampa de deceleración para el movimiento de rotación |
| **Speed Move** | 35 % | Velocidad de rotación del FlexiBowl® |
| **Angle Move** | 360 grados | Ángulo de rotación recorrido durante el comando MOVE |

### Parámetros SHAKE

| Parámetro | Valor de ejemplo | Descripción |
|---|---|---|
| **Acceleration Shake** | 50 % | Rampa de aceleración durante el shake |
| **Deceleration Shake** | 50 % | Rampa de deceleración durante el shake |
| **Speed Shake** | 50 % | Velocidad de rotación durante el shake |
| **Ccw Angle Shake** | -45 grados | Ángulo de rotación en sentido antihorario durante cada oscilación |
| **Cw Angle Shake** | -30 grados | Ángulo de rotación en sentido horario durante cada oscilación |
| **Count Shake** | 2 N° | Número de oscilaciones completas por ciclo de shake |

### Parámetros OPTION (flip y blow)

| Parámetro | Valor de ejemplo | Descripción |
|---|---|---|
| **Flip Pressure** | 5,00 Bar | Presión de aire para el accionamiento del flip |
| **Flip Count** | 4 N° | Número de flips realizados por ciclo |
| **Flip Delay** | 100 ms | Intervalo entre un flip y el siguiente |
| **Blow Pressure** | 5,00 Bar | Presión de aire para el soplado |
| **Blow Time** | 200 ms | Duración del impulso de soplado |

:::{note}
Los parámetros mostrados en el panel izquierdo se aplican a los comandos de la secuencia. Antes de añadir un comando con **ADD**, comprobar que los valores sean correctos: los parámetros se asocian al comando en el momento de la inserción.
:::

---
(comm)=
## 4. Panel de comandos
### Selección y adición de un comando

![panel de comandos](../../../../_shared/media/images/pannello_comandi_sequence.png)

El panel central superior contiene:

- El menú desplegable **«Command Available»**: permite seleccionar el tipo de comando que se añadirá a la secuencia.
- El botón **ADD** (flecha →): añade el comando seleccionado al final de la lista de comandos activos.

Los comandos disponibles son:

| Comando | Descripción |
|---|---|
| `FLB_NULL` | Comando nulo, no se ejecuta ninguna acción |
| `FLB_MOVE` | Rotación del FlexiBowl® según los parámetros MOVE |
| `FLB_MOVE_FLIP` | Rotación combinada con flip (vuelco) del plato |
| `FLB_MOVE_BLOWe` | Rotación combinada con soplado externo |
| `FLB_MOVE_BLOWc` | Rotación combinada con soplado central |
| `FLB_MOVE_BLOWce` | Rotación combinada con soplado central y externo |
| `FLB_MOVE_BLOWe_FLIP` | Rotación, soplado externo y flip combinados |
| `FLB_MOVE_BLOWc_FLIP` | Rotación, soplado central y flip combinados |
| `FLB_MOVE_BLOWce_FLIP` | Rotación, soplado central y externo y flip combinados |
| `FLB_SHAKE` | Sacudida del plato sin rotación |
| `FLB_BLOWe` | Soplado externo, sin rotación |
| `FLB_BLOWc` | Soplado central, sin rotación |
| `FLB_BLOWce` | Soplado central y externo, sin rotación |
| `FLB_FLIP` | Flip (vuelco) del plato, sin rotación |
| `FLB_PAUSE_100ms` | Pausa de 100 milisegundos |
| `FLB_PAUSE_200ms` | Pausa de 200 milisegundos |
| `FLB_PAUSE_500ms` | Pausa de 500 milisegundos |
| `FLB_LIGHT_1_ON` | Encendido de la luz 1 |
| `FLB_LIGHT_1_OFF` | Apagado de la luz 1 |
| `FLB_LIGHT_2_ON` | Encendido de la luz 2 |
| `FLB_LIGHT_2_OFF` | Apagado de la luz 2 |
| `FLB_ENABLE` | Habilitación del FlexiBowl® |
| `FLB_DISABLE` | Deshabilitación del FlexiBowl® |
| `FLB_BARRIER_DOWN` | Descenso de la barrera |
| `FLB_BARRIER_UP` | Elevación de la barrera |

:::{tip}
Seleccione el comando deseado en el menú desplegable antes de pulsar **ADD**. El comando se insertará en la primera fila libre de la lista **Command Active**.
:::

La tabla **Command Active** muestra la secuencia de comandos en orden de ejecución, numerados del 1 al 10.

En el ejemplo mostrado, la secuencia contiene un solo comando:

| N.º | Comando |
|---|---|
| 1 | FLB_MOVE |
| 2–10 | *(vacío)* |

### Herramientas de gestión de la lista

| Botón | Función |
|---|---|
| **DELETE** | Elimina el comando seleccionado de la lista |
| **UP** | Mueve el comando seleccionado una posición hacia arriba |
| **DOWN** | Mueve el comando seleccionado una posición hacia abajo |
| **CLEAR** | Elimina todos los comandos presentes en la lista |

:::{warning}
El botón **CLEAR** elimina **todos** los comandos de la secuencia sin posibilidad de recuperación. Utilícelo con precaución.
:::

---

## 5. Ejecución de la secuencia

En la parte inferior derecha hay dos botones de ejecución:

| Botón | Campo contiguo | Función |
|---|---|---|
| **TEST SEQUENCE** | Tiempo de ejecución (ms) | Ejecuta la secuencia una sola vez. El campo de la derecha muestra la duración total de la última ejecución en milisegundos |
| **RUN** | — | Inicia la secuencia en modo operativo continuo (bucle), a la espera de los disparos del sistema de visión |

:::{note}
El campo **ms** junto a **TEST SEQUENCE** indica el tiempo total de ejecución de la secuencia completa. En el ejemplo mostrado el valor es **1140 ms**. Este dato es útil para la sincronización con el sistema de visión artificial.
:::

:::{important}
Antes de pulsar **RUN**, comprobar que:
- el motor está habilitado (**ENABLE MOTOR** activo)
- el estado del sistema es **READY**
- la secuencia contiene al menos un comando válido en la lista **Command Active**
:::
