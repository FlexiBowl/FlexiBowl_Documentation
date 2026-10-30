(digIO)=
# **Digital I/O**

Communication with digital I/O is a purchasable option and is not part of the standard FlexiBowl®. The input connector of the new generation of FlexiBowl® supports digital and analog signals for direct integration with a PLC without the need for Ethernet communication.

### Inputs available on the main connector

| Type | Signal | Electrical type | Active level | Description |
|---|---|---|---|---|
| Standard | Bit 1 | Digital | 0–24Vdc, Active High | Command coding bit (see coding table) |
| Standard | Bit 2 | Digital | 0–24Vdc, Active High | Command coding bit |
| Standard | Bit 3 | Digital | 0–24Vdc, Active High | Command coding bit |
| Standard | Bit 4 | Digital | 0–24Vdc, Active High | Command coding bit |
| Standard | Bit 5 | Digital | 0–24Vdc, Active High | Command coding bit |
| Standard | Latch | Digital | 0–24Vdc, Active High | Command execution (rising edge) |
| Standard | Empty Sensor | Digital | 0–24Vdc, Active High | FlexiBowl® empty detection sensor |
| Standard | Zeroing | Digital | 0–24Vdc, Active High | Provision for multi-sector disc fixing sensor |
| Option | Flip proportional valve feedback | Analog | 0–10Vdc | Flip proportional valve feedback signal |
| Option | Blow proportional valve feedback | Analog | 0–10Vdc | Blow proportional valve feedback signal |
| Option | Strobe Backlight + / − | — | — | External backlight strobe command (diode and fuse protection required) |
| Option | Strobe Backlight 2+ / 2− | — | — | Secondary external backlight strobe command |

### STO connector (Safe Torque Off)

The STO connector is dedicated to the safety function for stopping the motor:

| Pin | Signal | Description |
|---|---|---|
| 1 | STO1+ | Safe Torque Off 1 |
| 2 | STO1- | STO1 return |
| 3 | STO2+ | Safe Torque Off 2 |
| 4 | STO2- | STO2 return |
| 5 | 24V | Power supply |
| 6 | 0V | Ground |

### Command coding via digital bits (Bit 1–5)

The 5 digital input bits form a 5-digit binary word that identifies the command to be executed. The command is acquired on the rising edge of the **Latch** signal.

| Binary code (Bit5–Bit1) | Command |
|---|---|
| `00000` | Alarm reset |
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
Example: to execute Sequence 5, set Bit1=1, Bit2=0, Bit3=1, Bit4=0, Bit5=0 (binary code `00101`) and then send a rising edge on **Latch**.
:::
