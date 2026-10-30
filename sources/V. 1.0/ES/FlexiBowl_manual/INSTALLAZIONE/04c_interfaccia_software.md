(digIO)=
# **Digital I/O**

La comunicación con E/S digitales es una opción que se adquiere por separado y no forma parte del FlexiBowl® estándar. El conector de entrada de la nueva generación de FlexiBowl® admite señales digitales y analógicas para la integración directa con un PLC sin necesidad de comunicación Ethernet.

### Entradas disponibles en el conector principal

| Tipo | Señal | Tipo eléctrico | Nivel activo | Descripción |
|---|---|---|---|---|
| Estándar | Bit 1 | Digital | 0–24Vdc, activo alto | Bit de codificación del comando (véase la tabla de codificación) |
| Estándar | Bit 2 | Digital | 0–24Vdc, activo alto | Bit de codificación del comando |
| Estándar | Bit 3 | Digital | 0–24Vdc, activo alto | Bit de codificación del comando |
| Estándar | Bit 4 | Digital | 0–24Vdc, activo alto | Bit de codificación del comando |
| Estándar | Bit 5 | Digital | 0–24Vdc, activo alto | Bit de codificación del comando |
| Estándar | Latch | Digital | 0–24Vdc, activo alto | Ejecución del comando (flanco ascendente) |
| Estándar | Empty Sensor | Digital | 0–24Vdc, activo alto | Sensor de detección de FlexiBowl® vacío |
| Estándar | Zeroing | Digital | 0–24Vdc, activo alto | Previsto para sensor de fijación de disco multisector |
| Opción | Retorno de la válvula proporcional flip | Analógico | 0–10Vdc | Señal de retorno de la válvula proporcional flip |
| Opción | Retorno de la válvula proporcional blow | Analógico | 0–10Vdc | Señal de retorno de la válvula proporcional blow |
| Opción | Strobe Backlight + / − | — | — | Comando strobe externo del backlight (se requiere protección con diodo y fusible) |
| Opción | Strobe Backlight 2+ / 2− | — | — | Comando strobe externo secundario del backlight |

### Conector STO (Safe Torque Off)

El conector STO está destinado a la función de seguridad para la parada del motor:

| Pin | Señal | Descripción |
|---|---|---|
| 1 | STO1+ | Safe Torque Off 1 |
| 2 | STO1- | Retorno STO1 |
| 3 | STO2+ | Safe Torque Off 2 |
| 4 | STO2- | Retorno STO2 |
| 5 | 24V | Alimentación |
| 6 | 0V | Masa |

### Codificación de comandos mediante bits digitales (Bit 1–5)

Los 5 bits de entrada digital forman una palabra binaria de 5 cifras que identifica el comando que se debe ejecutar. El comando se adquiere en el flanco de subida de la señal **Latch**.

| Código binario (Bit5–Bit1) | Comando |
|---|---|
| `00000` | Reinicio de alarmas |
| `00001` | Exe Seq 1 |
| `00010` | Exe Seq 2 |
| `00011` | Exe Seq 3 |
| `00100` | Exe Seq 4 |
| `00101` | Exe Seq 5 |
| `00110` | Exe Seq 6 |
| `00111` | Exe Seq 7 |
| `01000` | Exe Seq 8 |
| `01001` | Exe Seq 9 |
| `01010` | Exe Seq 10 |
| `01011` | Exe Seq 11 |
| `01100` | Exe Seq 12 |
| `01101` | Exe Seq 13 |
| `01110` | Exe Seq 14 |
| `01111` | Exe Seq 15 |
| `10000` | Exe Seq 16 |
| `10001` | Exe Seq 17 |
| `10010` | Exe Seq 18 |
| `10011` | Exe Seq 19 |
| `10100` | Exe Seq 20 |
| `10101` | Hopper Activation 1 |
| `10110` | Hopper Activation 2 |
| `10111` | Hopper Activation 3 |
| `11000` | Hopper Activation 4 |
| `11001`–`11111` | Spare |

:::{tip}
Ejemplo: para ejecutar la Secuencia 5, establecer Bit1=1, Bit2=0, Bit3=1, Bit4=0, Bit5=0 (código binario `00101`) y a continuación enviar un flanco de subida en **Latch**.
:::
