(cavi)=
# **Cables de conexión**

Los cables de conexión del FlexiBowl® se pueden adquirir por separado como opción, en longitudes de **3, 5 o 10 metros**. Esta página resume los cables disponibles en el catálogo, sus requisitos previos y sus asignaciones de pines.

:::{note}
Los cables de los Bulk Feeder (cable Modbus RTU y cable de entrada del controlador) se describen en la página {ref}`Accesorios y opciones de los Bulk Feeder <tramoggia-cavi>`.
:::

:::{warning}
Conectar y desconectar los cables únicamente con el equipo apagado y desconectado de la alimentación.
:::

## Resumen

:::{list-table}
:widths: 24 32 22 22
:header-rows: 1

* - Cable
  - Requisitos previos
  - Tamaños compatibles
  - Longitudes
* - [Cable para opción de E/S](cavo-io)
  - Opción **Digital I/O** (adquirida por separado)
  - Todos los tamaños
  - · 3
    · 5
    · 10 m
* - [Cable para armario remoto (rack)](cavo-rack)
  - FlexiBowl® con rack externo
  - FlexiBowl® 200 · 350
  - · 3 m incluido en el suministro;
    · 5
    · 10 m
* - [Cable de alimentación](cavo-alim)
  - Ninguno
  - Todos los tamaños
  - · 3
    · 5
    · 10 m
* - [Cable Ethernet](cavo-eth)
  - Ninguno
  - Todos los tamaños
  - · 3
    · 5
    · 10 m
:::

### Artículos del catálogo

:::{list-table}
:widths: 28 24 24 24
:header-rows: 1

* - Cable
  - 3 m
  - 5 m
  - 10 m
* - **Opción de E/S**
  - FlexiBowl cable for I/O option, 3m
  - FlexiBowl cable for I/O option, 5m
  - FlexiBowl cable for I/O option, 10m
* - **Armario remoto (rack)**
  - Cable for remote electronic cabinet, 3m
  - Cable for remote electronic cabinet, 5m
  - Cable for remote electronic cabinet, 10m
* - **Alimentación**
  - FlexiBowl Power Supply Cable, 3m
  - FlexiBowl Power Supply Cable, 5m
  - FlexiBowl Power Supply Cable, 10m
* - **Ethernet**
  - Ethernet Cable 3m
  - Ethernet Cable 5m
  - Ethernet Cable 10m
:::

---

(cavo-io)=
## Cable para opción de E/S

**Descripción.** Cable para la conexión de las señales de la opción **Digital I/O**, que permite controlar el FlexiBowl® desde un PLC mediante entradas y salidas digitales, sin comunicación Ethernet. Señales y codificación de los comandos: [Digital I/O](digIO).

:::{list-table}
:widths: 30 70
:stub-columns: 1

* - Requisitos previos
  - Opción **Digital I/O**, adquirida por separado y no incluida en la configuración estándar.
* - Conector del lado FlexiBowl®
  - Conector de E/S de 19 pines
    :::{dropdown} **Asignación de pines del conector de E/S (19 pines)**
    | Pin | Señal | Uso | 
    |---|---|---|
    | 1 | IN – Bit 1 | Codificación del comando (Seq. Cmd) | 
    | 2 | IN – Bit 2 | Codificación del comando (Seq. Cmd) | 
    | 3 | IN – Bit 3 | Codificación del comando (Seq. Cmd) | 
    | 4 | IN – Bit 4 | Codificación del comando (Seq. Cmd) | 
    | 5 | IN – Bit 5 | Codificación del comando (Seq. Cmd) | 
    | 6 | IN – Latch | Ejecución del comando (flanco ascendente) | 
    | 7–8 | NC | Sin asignar | 
    | 9 | OUT – Ready | Salida de estado | 
    | 10 | OUT – Fault | Salida de estado | 
    | 11 | OUT – Busy | Salida de estado | 
    | 12 | OUT – Hopper_1_IsVibrating | Salida de estado Hopper 1 | 
    | 13 | OUT – Hopper_2_IsVibrating | Salida de estado Hopper 2 | 
    | 14 | OUT – Hopper_3_IsVibrating | Salida de estado Hopper 3 | 
    | 15 | OUT – Hopper_4_IsVibrating | Salida de estado Hopper 4 |
    | 16–19 | NC | Sin asignar | 
    :::
* - Longitudes disponibles
  - · 3 m
    · 5 m
    · 10 m
:::


---

(cavo-rack)=
## Cable para armario electrónico remoto (rack)

**Descripción.** Cables de conexión entre el **rack** externo y el FlexiBowl®. El rack se comunica con la máquina mediante 4 cables dedicados, cada uno de los cuales debe conectarse exclusivamente al puerto con la etiqueta correspondiente. Procedimiento de conexión: {ref}`collegamento-rack`.

:::{list-table}
:widths: 30 70
:stub-columns: 1

* - Requisitos previos
  - FlexiBowl® con rack externo (ninguna opción que adquirir).
* - Tamaños compatibles
  - · FlexiBowl® 200
    · FlexiBowl® 350
* - Longitudes disponibles
  - · 3 m (incluido en el suministro)
    · 5 m
    · 10 m
:::

:::{attention}
Conectar cada cable al puerto con la **etiqueta correspondiente** (p. ej., MOTOR ↔ MOTOR, C-A SIGNAL ↔ C-A SIGNAL). Una conexión cruzada puede dañar el sistema.
:::

:::{list-table}
:header-rows: 1 

* - Cable
  - Conector
  - Función

* - **C-ETH FB**
  - M12 D-code
    :::{dropdown} **Asignación de pines C-ETH FB (M12 codificación D)**
    | Señal | Función | Color | Pin M12 (lado FlexiBowl®) | Pin RJ45 (lado cliente) |
    |---|---|---|---|---|
    | TD+ | Transmisión de datos (+) | Amarillo | 1 | 1 |
    | TD− | Transmisión de datos (−) | Naranja | 3 | 2 |
    | RD+ | Recepción de datos (+) | Blanco | 2 | 3 |
    | RD− | Recepción de datos (−) | Azul | 4 | 6 |
    :::

  - Conexión Ethernet entre el rack y el FlexiBowl®

* - **MOTOR**
  - 9 pines
    :::{dropdown} **Asignación de pines MOTOR (9 pines)**

    | Pin | Uso | 
    |---|---|
    | 1 | +STO1 – Safe Torque Off | 
    | 2 | +24 Vdc – Alimentación auxiliar | 
    | 3 | +STO2 – Safe Torque Off | 
    | 4 | −24 Vdc – Alimentación auxiliar | 
    | 5 | NC |
    | 6 | +48 Vdc – Motor Power | 
    | 7 | −STO1 – Safe Torque Off | 
    | 8 | −48 Vdc – Motor Power | 
    | 9 | −STO2 – Safe Torque Off | 
    :::
  - Alimentación del motor y señales STO

* - **C-A SIGNAL**
  - 12 pines
    :::{dropdown} **Asignación de pines C-A SIGNAL (12 pines)**

    | Pin | Uso |
    |---|---|
    | 1 | Analog Output 1 | 
    | 2 | −24 Vdc | 
    | 3 | Analog Input 1 | 
    | 4 | +24 Vdc | 
    | 5–12 | NC | 
    :::
  - Señales analógicas

* - **C-B SIGNAL**
  - 19 pines
    :::{dropdown} **Asignación de pines C-B SIGNAL (19 pines)**
    | Pin | Uso | 
    |---|---|
    | 1 | +24 Vdc – Activación del LED de estado verde | 
    | 2 | −24 Vdc – Común de los LED de estado | 
    | 3 | +24 Vdc – Activación del LED de estado rojo | 
    | 4 | +24 Vdc – Activación del LED de estado del Backlight | 
    | 5 | −24 Vdc – Activación del LED de estado del Backlight | 
    | 6 | +24 Vdc – Activación del Backlight |
    | 7 | −24 Vdc – Activación del Backlight | 
    | 8 | +24 Vdc – Activación del Flip | 
    | 9 | −24 Vdc – Activación del Flip | 
    | 10 | +24 Vdc – Activación del Blow | 
    | 11 | −24 Vdc – Activación del Blow | 
    | 12–19 | NC | 
    :::
  - Señales digitales, incluidas las activaciones de los LED de estado
:::


---

(cavo-alim)=
## Cable de alimentación

**Descripción.** Cable de alimentación de red, que debe conectarse al conector **POWER SUPPLY** del panel eléctrico estándar (FlexiBowl® 500 – 1200) o del rack (FlexiBowl® 200 / 350). Procedimiento de conexión: {ref}`pannello-standard` · {ref}`rack-esterno`.

:::{list-table}
:widths: 30 70
:stub-columns: 1

* - Requisitos previos
  - Ninguno. Equipo apagado, conexión a tierra obligatoria. El conector alberga 2 fusibles de protección.
* - Tamaños compatibles
  - Todos los tamaños de FlexiBowl®
* - Tensión admitida
  - 120–230 Vac, 50/60 Hz ({ref}`dati_elettrici`)
* - Longitudes disponibles
  - · 3 m
    · 5 m
    · 10 m
:::

| Etiqueta (lado FlexiBowl®) | Tipo | Color |
|---|---|---|
| L1 | Fase | Marrón |
| N1 | Neutro | Azul |
| PE1 | Tierra | Amarillo/Verde |

:::{attention}
Conectar la alimentación **en último lugar**, con el FlexiBowl® apagado. La conexión a tierra es obligatoria y debe verificarse antes de cada encendido.
:::


---

(cavo-eth)=
## Cable Ethernet

**Descripción.** Cable para la conexión Ethernet del FlexiBowl® con el sistema (conector **C-ETH** del panel estándar o **C-ETH IN** del rack). Permite la comunicación con el FlexiBowl®, al que también se puede acceder mediante un navegador web.

:::{list-table}
:widths: 30 70
:stub-columns: 1

* - Requisitos previos
  - Ninguno. Con el FlexiBowl® alimentado, la conexión Ethernet es **obligatoria**: si falta, la máquina entra en estado **ERROR** (LED Ready/Fault en rojo).
* - Tamaños compatibles
  - Todos los tamaños de FlexiBowl®
* - Conectores
  - Lado FlexiBowl®: M12 codificación D
    :::{dropdown} **Asignación de pines M12 codificación D y RJ45**
    | Señal | Función | Color | Pin M12 (lado FlexiBowl®) | Pin RJ45 (lado cliente) |
    |---|---|---|---|---|
    | TD+ | Transmisión de datos (+) | Amarillo | 1 | 1 |
    | TD− | Transmisión de datos (−) | Naranja | 3 | 2 |
    | RD+ | Recepción de datos (+) | Blanco | 2 | 3 |
    | RD− | Recepción de datos (−) | Azul | 4 | 6 |

    Los pines RJ45 4, 5, 7 y 8 no están asignados.
    :::
* - Longitudes disponibles
  - · 3 m
    · 5 m
    · 10 m
:::
