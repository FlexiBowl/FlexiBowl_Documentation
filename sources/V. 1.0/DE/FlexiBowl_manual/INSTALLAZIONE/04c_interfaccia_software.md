(digIO)=
# **Digital I/O**

Die Kommunikation über digitale I/O ist eine käufliche Option und nicht Bestandteil des Standard-FlexiBowl®. Der Eingangsstecker der neuen FlexiBowl®-Generation unterstützt digitale und analoge Signale für die direkte Integration mit einer SPS, ohne dass eine Ethernet-Kommunikation erforderlich ist.

### Am Hauptstecker verfügbare Eingänge

| Typ | Signal | Elektrische Art | Aktiver Pegel | Beschreibung |
|---|---|---|---|---|
| Standard | Bit 1 | Digital | 0–24Vdc, Active High | Befehlscodierungs-Bit (siehe Codierungstabelle) |
| Standard | Bit 2 | Digital | 0–24Vdc, Active High | Befehlscodierungs-Bit |
| Standard | Bit 3 | Digital | 0–24Vdc, Active High | Befehlscodierungs-Bit |
| Standard | Bit 4 | Digital | 0–24Vdc, Active High | Befehlscodierungs-Bit |
| Standard | Bit 5 | Digital | 0–24Vdc, Active High | Befehlscodierungs-Bit |
| Standard | Latch | Digital | 0–24Vdc, Active High | Befehlsausführung (steigende Flanke) |
| Standard | Empty Sensor | Digital | 0–24Vdc, Active High | Sensor zur Erkennung eines leeren FlexiBowl® |
| Standard | Zeroing | Digital | 0–24Vdc, Active High | Vorgesehen für Sensor zur Fixierung der Mehrsektorenscheibe |
| Option | Rückmeldung des Proportionalventils Flip | Analog | 0–10Vdc | Rückmeldesignal des Proportionalventils Flip |
| Option | Rückmeldung des Proportionalventils Blow | Analog | 0–10Vdc | Rückmeldesignal des Proportionalventils Blow |
| Option | Strobe Backlight + / − | — | — | Externer Backlight-Strobe-Befehl (Schutz mit Diode und Sicherung erforderlich) |
| Option | Strobe Backlight 2+ / 2− | — | — | Sekundärer externer Backlight-Strobe-Befehl |

### STO-Stecker (Safe Torque Off)

Der STO-Stecker ist für die Sicherheitsfunktion zum Stoppen des Motors vorgesehen:

| Pin | Signal | Beschreibung |
|---|---|---|
| 1 | STO1+ | Safe Torque Off 1 |
| 2 | STO1- | STO1-Rückleiter |
| 3 | STO2+ | Safe Torque Off 2 |
| 4 | STO2- | STO2-Rückleiter |
| 5 | 24V | Spannungsversorgung |
| 6 | 0V | Masse |

### Befehlscodierung über digitale Bits (Bit 1–5)

Die 5 digitalen Eingangsbits bilden ein 5-stelliges Binärwort, das den auszuführenden Befehl kennzeichnet. Der Befehl wird bei der steigenden Flanke des Signals **Latch** übernommen.

| Binärcode (Bit5–Bit1) | Befehl |
|---|---|
| `00000` | Alarm-Reset |
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
Beispiel: Um Sequenz 5 auszuführen, Bit1=1, Bit2=0, Bit3=1, Bit4=0, Bit5=0 setzen (Binärcode `00101`) und anschließend eine steigende Flanke auf **Latch** senden.
:::
