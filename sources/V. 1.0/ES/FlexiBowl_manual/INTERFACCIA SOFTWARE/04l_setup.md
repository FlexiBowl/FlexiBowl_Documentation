# **Setup**
## Descripción general

La página **Setup** agrupa los ajustes de red y comunicación del FlexiBowl®. Permite configurar la dirección IP del dispositivo, el tipo de protocolo de comunicación con el sistema externo (p. ej. PLC o PC supervisor) y supervisar el estado de la conexión en tiempo real.

En la parte superior derecha se indica la **versión del firmware** instalado (en el ejemplo: `1.0.2`).

![página Setup](../../../../_shared/media/images/setup.png)

---

## Barra superior

| Elemento | Descripción |
|---|---|
| **Menu** (icono ☰) | Abre el menú de navegación entre las páginas del software |
| **READY** | Indicador de estado del dispositivo: señala que el FlexiBowl® está listo para su uso |
| **USER** | Indica el usuario conectado actualmente a la interfaz de software |
| **REBOOT** | Reinicia el software del FlexiBowl® sin apagar el sistema |
| **Version** | Versión del firmware instalado actualmente en el dispositivo |
| **ENABLE MOTOR** | Habilita la alimentación del motor del FlexiBowl®. Con el motor deshabilitado, el dispositivo no realiza ningún movimiento |

:::{warning}
El botón **REBOOT** interrumpe temporalmente todas las operaciones en curso. No realice el reinicio durante una secuencia activa ni durante una transferencia de archivos.
:::

:::{warning}
Antes de pulsar **ENABLE MOTOR**, asegúrese de que la zona alrededor del FlexiBowl® esté despejada: la habilitación del motor deja el dispositivo listo para moverse.
:::

---

## Panel GET IP

El panel izquierdo muestra los parámetros de red asignados actualmente al FlexiBowl®.

| Campo | Valor de ejemplo | Descripción |
|---|---|---|
| **IP** | 192.168.1.90 | Dirección IP actual del dispositivo |
| **SUBNET** | 255.255.255.0 | Máscara de subred actual |
| **MAC** | 00:30:de:77:fe:74 | Dirección MAC de la tarjeta de red del dispositivo |
| **Info** | Done | Resultado de la última operación de lectura |

El botón **GET IP** actualiza los campos leyendo los parámetros de red configurados actualmente en el dispositivo.

---

## Panel SET IP

El panel central permite modificar la dirección IP y la máscara de subred del FlexiBowl®.

| Campo | Valor de ejemplo | Descripción |
|---|---|---|
| **IP** | 192.168.1.90 | Nueva dirección IP que se asignará al dispositivo (se puede introducir octeto por octeto) |
| **SUBNET** | 255.255.255.0 | Nueva máscara de subred que se asignará |
| **Info** | All Done. | Resultado de la última operación de configuración |

El botón **SET IP** aplica los valores introducidos y los guarda en la configuración de red del dispositivo.

:::{important}
Después de modificar la dirección IP con **SET IP**, es necesario realizar un **REBOOT** del sistema para que los cambios surtan efecto. El software deberá reconectarse a la nueva dirección IP.
:::

:::{warning}
Asegúrese de que la nueva dirección IP no esté ya en uso por otro dispositivo de la misma red, para evitar conflictos de direcciones que podrían dejar el FlexiBowl® inaccesible.
:::

---

## Panel SELECT THE COMMUNICATION TYPE

El panel derecho permite configurar el protocolo de comunicación entre el FlexiBowl® y el sistema externo (PLC, PC supervisor, sistema de visión).

![panel de comunicación](../../../../_shared/media/images/comm_type.png)

| Campo |  Descripción |
|---|---|
| **Tipo de comunicación** |  Protocolo de comunicación seleccionado. Se puede seleccionar mediante el menú desplegable |
| **Puerto** |  Puerto TCP en el que el FlexiBowl® escucha como servidor |
| **Cadena de terminación** | Carácter o secuencia de caracteres que delimita los mensajes intercambiados. Se puede seleccionar mediante el menú desplegable |

El botón **APPLY** confirma y aplica los ajustes de comunicación seleccionados.

:::{note}
El modo **TCP Server** indica que el FlexiBowl® actúa como servidor: es el sistema externo (cliente) quien debe iniciar la conexión hacia la dirección IP y el puerto configurados.
:::

:::{tip}
Compruebe que el puerto configurado (p. ej. 8123) no esté bloqueado por un cortafuegos en el PC o en la red de la empresa. En caso de problemas de conexión, consulte al responsable de TI.
:::

---

## Selección de la cadena de terminación

El tercer menú desplegable del panel **SELECT THE COMMUNICATION TYPE** permite elegir el **terminador** de los mensajes intercambiados con el sistema externo, es decir, la secuencia de caracteres que señala el final de cada comando enviado y de cada respuesta recibida.

![menú desplegable de la cadena de terminación](../../../../_shared/media/images/tendina_stringa.png)

| Opción | Terminador | Descripción |
|---|---|---|
| **% only** | `%` | Solo el carácter `%`, sin caracteres de fin de línea |
| **% + CR** | `%` + `\r` | Carácter `%` seguido de Carriage Return (0x0D) |
| **% + LF** | `%` + `\n` | Carácter `%` seguido de Line Feed (0x0A) |
| **% + CR/LF** | `%` + `\r\n` | Carácter `%` seguido de Carriage Return y Line Feed (0x0D 0x0A) |

Tras seleccionar la opción deseada, pulse **APPLY** para que el ajuste surta efecto.

:::{important}
La cadena de terminación seleccionada debe coincidir con la esperada por el sistema externo (PLC, PC supervisor o sistema de visión). Si los dos ajustes no coinciden, los comandos enviados no se reconocen y la comunicación falla, incluso con el servidor en línea y el cliente conectado.
:::

:::{tip}
Si los comandos parecen enviarse pero no obtienen respuesta, compruebe en el panel de estado el campo **Last message received**: si el mensaje llega pero no produce ningún efecto, la causa suele ser una cadena de terminación incorrecta.
:::

---

## Panel de estado de la comunicación

El panel inferior muestra en tiempo real el estado de la conexión entre el FlexiBowl® y el cliente externo.

### Indicadores de estado

| Indicador | Color activo |  Descripción |
|---|---|---|
| **SERVER ONLINE** | 🟢 Verde |  El servidor TCP del FlexiBowl® está activo y a la escucha |
| **CLIENT CONNECTED** | 🟢 Verde |  Un cliente externo está conectado actualmente al servidor |
| **CLIENT IP** | — | Dirección IP del cliente conectado actualmente |

:::{note}
Cuando un indicador está en gris, la condición correspondiente no se cumple: en el ejemplo el servidor está en línea pero todavía no hay ningún cliente conectado.
:::

### Monitor de mensajes

| Campo |  Descripción |
|---|---|
| **Last message received** | Último mensaje recibido del cliente externo |
| **Last message sent** | Último mensaje enviado por el FlexiBowl® al cliente |

:::{note}
El monitor de mensajes es útil durante la integración y la depuración de la comunicación con el sistema externo. Los mensajes mostrados siguen el protocolo de comunicación del FlexiBowl®; consulte la documentación del protocolo para ver la lista completa de comandos disponibles.
:::

### Botón RESTART SERVER

El botón **RESTART SERVER** reinicia el servicio TCP del FlexiBowl® sin realizar un reinicio completo del sistema. Es útil para restablecer la conexión en caso de desconexión inesperada del cliente o de bloqueo del servidor.

:::{warning}
**RESTART SERVER** interrumpe la conexión TCP actual. Si el FlexiBowl® está ejecutando una secuencia controlada a distancia, esta se interrumpirá. Utilice esta función solo cuando el sistema esté en stand-by.
:::
