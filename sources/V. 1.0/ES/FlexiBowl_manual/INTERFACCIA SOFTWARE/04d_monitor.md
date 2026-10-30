# **Monitor**

## Descripción general

La página **Monitor** ofrece una vista en tiempo real del estado del motor y del sistema de comunicación, y registra todos los eventos y alarmas generados durante el funcionamiento del FlexiBowl®. Es la página de referencia para el diagnóstico y la resolución de problemas.
![página monitor](../../../../_shared/media/images/monitor.png)

---

## Sección STATE MOTOR

El panel **STATE MOTOR** muestra el estado operativo actual del driver del motor mediante una serie de indicadores luminosos (LED virtuales).
Cada LED puede estar:
🟢 **Verde** : estado activo
⚫ **Gris** : estado inactivo

### Indicadores de estado

| Indicador | Descripción |
|---|---|
| **Not Ready To Switch On** | El driver no está listo para la habilitación  |
| **Switch On Disabled** | La habilitación del motor está bloqueada  |
| **Ready To Switch On** | El driver está listo para recibir el comando de habilitación |
| **Switched On** | El motor está alimentado pero todavía no está bajo control activo |
| **Target Reached** | El FlexiBowl® ha alcanzado la posición o consigna de destino |
| **Operation Enabled** | El motor está habilitado y operativo |
| **Quick Stop Active** | Parada rápida del motor solicitada |
| **Fault Reaction Active** | El driver está ejecutando el procedimiento de reacción a un fallo |
| **Fault** | Hay un fallo activo en el driver del motor |
| **SetPoint in process** | El sistema está procesando o alcanzando una nueva consigna de posición |

:::{note}
Durante el funcionamiento normal, los LED **Operation Enabled** y **Target Reached** deben estar en verde. Cualquier otro LED verde indica una condición anómala que requiere atención.
:::

---

## Sección Communication State

El panel lateral derecho muestra el estado de la comunicación entre el software y el driver del motor.

| Campo | Valor de ejemplo | Descripción |
|---|---|---|
| **Communication State** | `RUNNING` | Indica que la comunicación con el driver está activa y funciona correctamente |
| **Error Code** | `0` | Código de error devuelto por el driver. El valor `0` indica ausencia de errores |

### Botón Reset Driver

El botón **Reset Driver** realiza un reinicio del driver del motor, útil para salir de un estado de fallo o para reinicializar la comunicación.

:::{warning}
Pulsar **Reset Driver** solo después de haber identificado y resuelto la causa del fallo. Realizar el reinicio sin haber eliminado la causa del problema podría provocar la repetición del error o daños en el sistema.
:::

---

## Registro de eventos (tabla de mensajes)

La tabla central registra en tiempo real todos los eventos, alarmas y mensajes del sistema generados durante el funcionamiento.

### Columnas de la tabla

| Columna | Descripción |
|---|---|
| **Timestamp** | Fecha y hora del evento en el formato `GG.MM.AAAA HH:MM:SS` |
| **Message** | Descripción textual del evento o de la alarma |
| **Bitmap** | Icono que indica el tipo de evento (⚠️ advertencia, ❌ error, etc.) |

### Ejemplo de mensaje

| # | Timestamp | Message | Bitmap |
|---|---|---|---|
| 0 | 14.05.2026 15:59:57 | Air pressure does not match the set value | ⚠️ |

:::{warning}
El mensaje **«Air pressure does not match the set value»** indica que la presión de aire detectada por el sistema no coincide con el valor establecido en los parámetros. Compruebe la alimentación neumática y revise los valores **Flip Pressure** y **Blow Pressure** en la página **Main Command > OPTION**.
:::

:::{tip}
Los mensajes de advertencia se muestran en **rojo** en la columna Timestamp y en **naranja** en la columna Message, para facilitar su reconocimiento inmediato incluso cuando el registro contiene muchas filas.
:::

---

## Botones de gestión del registro

| Botón | Función |
|---|---|
| **ACK selected** | Confirma el mensaje seleccionado en la tabla, marcándolo como atendido |
| **ACK all visible** | Confirma todos los mensajes visibles actualmente en la tabla |
| **History** | Abre el historial completo de los eventos registrados por el sistema |
| **Freeze Scrl Pos** | Bloquea el desplazamiento automático de la tabla, permitiendo examinar los mensajes anteriores sin que la vista se desplace hacia los nuevos eventos |

:::{note}
Es una buena práctica realizar el **ACK** de las alarmas solo después de haber verificado y resuelto la condición que las generó, y no para suprimir la notificación sin intervenir.
:::
