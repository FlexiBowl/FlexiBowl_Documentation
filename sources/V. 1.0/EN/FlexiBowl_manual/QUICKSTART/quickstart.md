(quickstart)=
# **Quickstart**
## Digital and Analog Inputs (Digital I/O)

:::{note}
The **Digital I/O** mode is an option that can be purchased separately and is not included in the standard configuration of the FlexiBowl®.
:::

The input connector of the FlexiBowl® EVO supports digital and analog signals for direct integration with a PLC without the need for Ethernet communication.

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
| Option | Flip proportional valve return | Analog | 0–10Vdc | Flip proportional valve feedback signal |
| Option | Blow proportional valve return | Analog | 0–10Vdc | Blow proportional valve feedback signal |
| Option | Strobe Backlight + / − | — | — | External backlight strobe command (diode and fuse protection required) |
| Option | Strobe Backlight 2+ / 2− | — | — | Secondary external backlight strobe command |

### STO (Safety Torque Off) connector

The STO connector is dedicated to the safety function for stopping the motor:

| Pin | Signal | Description |
|---|---|---|
| 1 | STO1+ | Safety Torque Off 1 |
| 2 | STO1- | STO1 return |
| 3 | STO2+ | Safety Torque Off 2 |
| 4 | STO2- | STO2 return |
| 5 | 24V | Power supply |
| 6 | 0V | Ground |

### Command coding via digital bits (Bit 1–5)

The 5 digital input bits form a 5-digit binary word that identifies the command to be executed. The command is acquired on the rising edge of the **Latch** signal.

| Binary Code (Bit5–Bit1) | Command |
|---|---|
| `00000` | Reset alarms |
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

---

## ConfigIO Diagram — PLC Configuration (Wago)

The following diagram describes the typical configuration of a Wago PLC used to control the FlexiBowl® via Digital I/O.

**Hardware used:**
- CPU: PFC300, 2× Ethernet, RS-485
- Digital I/O modules: 8DI/8DO (750-1502) — 2 modules
- Analog input module: 0–10V (750-467)
- Analog output module: 0–10V (750-550)

### Digital inputs (DI) — Module 1

| DI | Description |
|---|---|
| 1 | Bit 1 — Seq. Cmd |
| 2 | Bit 2 — Seq. Cmd |
| 3 | Bit 3 — Seq. Cmd |
| 4 | Bit 4 — Seq. Cmd |
| 5 | Latch |
| 6 | Empty Sensor |
| 7 | Zeroing |
| 8 | Spare |

### Digital outputs (DO) — Module 1

| DO | Description |
|---|---|
| 1 | Backlight 1 & 2 |
| 2 | Ready Led + Sgn |
| 3 | Fault Led + Sgn |
| 4 | Busy Sgn |
| 5 | Flip 1 Command |
| 6 | Blow 1 Command |
| 7 | Blow 2 Command |
| 8 | Empty Slide Cmd |

### Analog inputs (AI)

| AI | Description |
|---|---|
| 1 | Flip Valve Feedback |
| 2 | Blow Valve Feedback |

### Analog outputs (AO)

| AO | Description |
|---|---|
| 1 | Flip Valve Regulation |
| 2 | Blow Valve Regulation |
