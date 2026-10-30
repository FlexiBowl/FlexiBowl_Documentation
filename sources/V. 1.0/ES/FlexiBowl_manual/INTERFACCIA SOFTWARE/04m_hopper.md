(hopper)=
# **Hopper**
## Descripción general

La página **Hopper** permite configurar y gestionar hasta **4 Bulk Feeders** conectados al FlexiBowl®. Cada hopper es una unidad de alimentación autónoma que abastece al FlexiBowl® de componentes y puede controlarse de forma independiente con sus propios parámetros de vibración y temporización.

Cada hopper está representado por una columna vertical con los mismos controles, identificada como **HOPPER 1**, **HOPPER 2**, **HOPPER 3** y **HOPPER 4**.

![página hopper](../../../../_shared/media/images/hopper.png) ---

## Estructura de cada panel Hopper

### ENABLE

La casilla **ENABLE** de la parte superior del panel activa o desactiva el hopper correspondiente. Solo los hoppers habilitados pueden ponerse en marcha y responderán a los comandos del sistema.

En el ejemplo mostrado, solo **HOPPER 1** tiene la casilla ENABLE seleccionada (marca azul); los hoppers 2, 3 y 4 están deshabilitados.

:::{note}
Un hopper deshabilitado no responde al botón **Start Hopper** y no se activa durante las secuencias automáticas, aunque esté conectado físicamente al sistema.
:::

---

### ID y Set New ID

| Campo |  Descripción |
|---|---|
| **ID** |  Identificador único asignado al hopper en la red de comunicación |
| **Set New ID** | Botón para asignar un nuevo ID al hopper. Se utiliza durante la configuración inicial o en caso de sustitución de la unidad |

:::{warning}
Modifique el ID de un hopper solo si es estrictamente necesario. Un ID erróneo o duplicado impide la comunicación con el hopper y puede causar fallos de funcionamiento en toda la cadena de alimentación. Tras establecer un nuevo ID, compruebe que se haya adquirido correctamente mediante el indicador **STATUS**.
:::

---

### STATUS

El indicador **STATUS** muestra el estado operativo actual del hopper.

| Color de los LED | Etiqueta | Descripción |
|---|---|---|
| 🔴 Rojo | **DISABLED** | El hopper está deshabilitado |
| 🟢 Verde | **ENABLED** | El hopper está habilitado |


---

### Parámetros de vibración

| Parámetro |  Descripción |
|---|---|
| **Amplitude** |  Amplitud de la vibración del hopper, expresada en unidades adimensionales. Valores más altos producen una vibración más intensa y un mayor flujo de componentes |
| **Frequency** | Frecuencia de vibración del hopper. Influye en la cadencia con la que los componentes se conducen hacia el FlexiBowl® |


---

### Activation Time y LED de estado

| Campo  | Descripción |
|---|---|
| **Activation Time** | Duración de la activación del hopper cuando se pone en marcha manualmente con **Start Hopper** o es llamado por una secuencia |
| **LED** (gris/verde) |  Indicador luminoso que se enciende durante la activación del hopper |

:::{note}
**HOPPER 1** tiene un **Activation Time** de 2000 ms, mientras que los demás hoppers están configurados a 800 ms. Tiempos de activación más largos suponen un mayor aporte de componentes al FlexiBowl® en cada ciclo de activación.
:::

---

### Start Hopper

El botón **Start Hopper** pone en marcha manualmente el hopper durante el tiempo establecido en **Activation Time**. Al terminar el tiempo, el hopper se detiene automáticamente.

:::{important}
El botón **Start Hopper** solo está activo si la casilla **ENABLE** del hopper correspondiente está seleccionada. Compruebe que el hopper esté habilitado antes de intentar ponerlo en marcha manualmente.
:::

---

