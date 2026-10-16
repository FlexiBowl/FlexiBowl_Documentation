(fieldbus)=
# Ethernet/IP, Profinet, Modbus

For **EtherNet/IP**, **Profinet** and **Modbus** the [Input](#sec-io) and [Output](#sec-io) variables are exchanged as a **cyclic I/O packet**: there are no text messages, and each variable occupies a fixed position in the data packet.

### Data packet — Input (to the FlexiBowl®)

| ControlWord | Data_1 | ExecuteControlWord | Hopper_1 | Hopper_2 | Hopper_3 | Hopper_4 | Reset |
|---|---|---|---|---|---|---|---|
| *(command number)* | *(argument)* | *(trigger bit 0→1)* | *(bit)* | *(bit)* | *(bit)* | *(bit)* | *(bit)* |

### Data packet — Output (from the FlexiBowl®)

| Busy | Ready | In_Error | In_PowerOn | ReturnData_1 | ReturnData_2 | ErrorCode |
|---|---|---|---|---|---|---|
| *(bit)* | *(bit)* | *(bit)* | *(bit)* | *(ControlWord echo)* | *(data read)* | *(error code)* |

:::{note}
The write sequence is always the same: set **ControlWord** (and **Data_1** if required) with **ExecuteControlWord = 0**, then set **ExecuteControlWord** to `1` to generate the rising edge that starts execution.
:::


## Command Protocol

The command protocol defines all the actions available through the ControlWord. The ControlWords are **the same for all protocols**; only the transport changes (see [Fieldbus Transport](#sec-fieldbus) and [TCP Syntax](#sec-tcp)). The commands are grouped into categories:

<div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:1rem; margin:1.5rem 0 2.5rem;">

  <a href="#sec-exe" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-play-circle" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">EXE Commands</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Execution commands (sequence start, jog, reset)</span>
  </a>

  <a href="#sec-write" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-pencil-simple" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">WRITE Commands</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Writing parameters (speed, angles, times, etc.)</span>
  </a>

  <a href="#sec-read" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-eye" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">READ Commands</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Reading the currently configured parameters</span>
  </a>

</div>

(sec-exe)=
### <span class="isw-section-badge isw-badge-exe"><i class="ph ph-play-circle"></i> EXE</span>

The EXE commands start an immediate action on the FlexiBowl®. During execution **Busy** remains at `1`.

| Command | ControlWord | Busy during execution | ReturnData_1 | Explanation | 
|---|---|---|---|---|
| Exe Seq 1 | 10 | YES | 10 | Execute Sequence 1 |
| Exe Seq 2 | 11 | YES | 11 | Execute Sequence 2 |
| Exe Seq 3 | 12 | YES | 12 | Execute Sequence 3 |
| Exe Seq 4 | 13 | YES | 13 | Execute Sequence 4 |
| Exe Seq 5 | 14 | YES | 14 | Execute Sequence 5 |
| Exe Seq 6 | 15 | YES | 15 | Execute Sequence 6 |
| Exe Seq 7 | 16 | YES | 16 | Execute Sequence 7 |
| Exe Seq 8 | 17 | YES | 17 | Execute Sequence 8 |
| Exe Seq 9 | 18 | YES | 18 | Execute Sequence 9 |
| Exe Seq 10 | 19 | YES | 19 | Execute Sequence 10 |
| Exe Seq 11 | 20 | YES | 20 | Execute Sequence 11 |
| Exe Seq 12 | 21 | YES | 21 | Execute Sequence 12 |
| Exe Seq 13 | 22 | YES | 22 | Execute Sequence 13 |
| Exe Seq 14 | 23 | YES | 23 | Execute Sequence 14 |
| Exe Seq 15 | 24 | YES | 24 | Execute Sequence 15 |
| Exe Seq 16 | 25 | YES | 25 | Execute Sequence 16 |
| Exe Seq 17 | 26 | YES | 26 | Execute Sequence 17 |
| Exe Seq 18 | 27 | YES | 27 | Execute Sequence 18 |
| Exe Seq 19 | 28 | YES | 28 | Execute Sequence 19 |
| Exe Seq 20 | 29 | YES | 29 | Execute Sequence 20 |
| Start Jog Seq | 40 | YES | 40 | Start Jog |
| Stop Jog Seq | 41 | YES | 41 | Stop Jog |
| Reset Return Data | 50 | NO | 0 | Resets the value of ReturnData_1 and ReturnData_2, returning them to the initial state `0` |

:::{note}
The **Reset Return Data** command (ControlWord 50) resets the value of ReturnData_1 and ReturnData_2, returning them to the initial state `0`. It is useful to check that a new command is actually received and processed.
:::

(fieldbus_exe)=
#### Practical example — “Execute Sequence 3”

<div class="isw-example">
<div class="isw-example-title">Execute Sequence 3 → ControlWord 12</div>
<div class="isw-example-body">
<div>
<div class="isw-example-col-title">EtherNet/IP · Profinet · Modbus</div>

Packet sent:

| ControlWord | Data_1 | ExecuteCW | Hopper_1 | Hopper_2 | Hopper_3 | Hopper_4 | Reset |
|---|---|---|---|---|---|---|---|
| 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 12 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |

Packet received:

| Busy | Ready | In_Error | In_PowerOn | ReturnData_1 | ReturnData_2 | ErrorCode |
|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 1 | 12 | 0 | 0 |


(sec-write)=
### <span class="isw-section-badge isw-badge-write"><i class="ph ph-pencil-simple"></i> WRITE</span>

The WRITE commands allow the operating parameters of the FlexiBowl® (speed, angles, times, etc.) to be modified directly from the external system, without having to access the graphical interface.

#### Sequence addressing logic

Each sequence (from 1 to 20) has its own block of parameters. The ControlWord is calculated with the formula:

> **ControlWord = N × 100 + parameter_offset**

where `N` is the sequence number (1–20) and `parameter_offset` identifies the specific parameter.

#### Writable parameters for each sequence

| Parameter | Offset | Data_1 range | Notes |
|---|---|---|---|
| AccelerationMove | 00 | 1–100 | Acceleration ramp of the rotary movement (%) |
| DecelerationMove | 01 | 1–100 | Deceleration ramp of the rotary movement (%) |
| SpeedMove | 02 | 1–100 | Speed of the rotary movement (%) |
| AngleMove | 03 | 0–720 | Rotation angle in degrees. Values 1000–1720 = negative angle (opposite direction) |
| AccelerationShake | 04 | 1–100 | Acceleration ramp of the shake (%) |
| DecelerationShake | 05 | 1–100 | Deceleration ramp of the shake (%) |
| CountShake | 06 | 2–20 | Number of oscillations per shake cycle |
| CwAngleShake | 07 | 0–360 | Clockwise rotation angle during the shake. Values 1000–1360 = negative angle |
| CcwAngleShake | 08 | 0–360 | Counterclockwise rotation angle during the shake. Values 1000–1360 = negative angle |
| SpeedShake | 09 | 1–100 | Shake speed (%) |
| FlipCount | 10 | 0–20 | Number of flips per cycle |
| FlipDelay | 11 | 0–500 | Pause between one flip and the next (ms) |
| BlowDelay | 12 | 0–500 | Pause between one blow pulse and the next (ms) |
| ProportionalValve_Flip | 13 | 0–600 | Flip proportional valve pressure (value /100 = Bar) |
| ProportionalValve_Blow | 14 | 0–600 | Blow proportional valve pressure (value /100 = Bar) |
| Delete all sequence | 30 | — | Deletes all commands from the sequence list |
| Emptying Sequence | 40 | 0–1 | 0 = normal mode, 1 = emptying mode |
| Seq Add Cmd | 50 | FLB COMMAND | Adds a command to the sequence list |

#### WRITE ControlWord examples

| Sequence | Parameter | Offset associated with the parameter | Formula (N x 100 + Offset) | ControlWord |
|---|---|---|---|---|
| SEQ 1 (N=1) | AccelerationMove | 00 | 1 x 100 + 00 | 100 |
| SEQ 1 (N=1) | SpeedMove | 02 | 1 x 100 + 02 | 102 |
| SEQ 1 (N=1) | FlipCount | 10 | 1 x 100 + 10 | 110 |
| SEQ 1 (N=1) | Emptying Sequence | 40 | 1 x 100 + 40 | 140 |
| SEQ 1 (N=1) | Seq Add Cmd | 50 | 1 x 100 + 50 | 150 |
| SEQ 2 (N=2) | AccelerationMove | 00 | 2 x 100 + 00 | 200 |
| SEQ 2 (N=2) | SpeedMove | 02 | 2 x 100 + 02 | 202 |
| SEQ 5 (N=5) | AngleMove | 03 | 5 x 100 + 03 | 503 |
| SEQ 10 (N=10) | FlipDelay | 11 | 10 x 100 + 11 |1011 |
| SEQ 20 (N=20) | SpeedMove | 02 | 20 x 100 + 02 | 2002 |

:::{tip}
The formula is simple:  
- To write the speed (offset 02) of sequence 7, the ControlWord is `7 × 100 + 2 = 702`.  
- To write the FlipCount (offset 10) of sequence 15, the ControlWord is `15 × 100 + 10 = 1510`.
:::

(fieldbus_write)=
#### Practical example — “Set the Move acceleration to 80 in Sequence 7”

<div class="isw-example">
<div class="isw-example-title">SpeedMove Seq 7 → ControlWord 700, Data_1 = 80</div>
<div class="isw-example-body">
<div>
<div class="isw-example-col-title">EtherNet/IP · Profinet · Modbus</div>

Packet sent:

| ControlWord | Data_1 | ExecuteCW | Hopper_1 | Hopper_2 | Hopper_3 | Hopper_4 | Reset |
|---|---|---|---|---|---|---|---|
| 700 | 80 | 0 | 0 | 0 | 0 | 0 | 0 |
| 700 | 80 | 1 | 0 | 0 | 0 | 0 | 0 |

Packet received:

| Busy | Ready | In_Error | In_PowerOn | ReturnData_1 | ReturnData_2 | ErrorCode |
|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 1 | 700 | 0 | 0 |


#### WRITE JOG parameters

The Jog parameters (continuous manual operation) can be configured separately via ControlWord in block 20000.

| Parameter | ControlWord | Data_1 range | Notes |
|---|---|---|---|
| AccelerationJog | 20001 | 0–100 | Jog acceleration ramp (%) |
| DecelerationJog | 20002 | 0–100 | Jog deceleration ramp (%) |
| SpeedJog | 20003 | 0–100 | Jog speed (%). Values 1000–1100 = negative speed (reverse rotation) |
| FlipJog_Enable | 20004 | 0–1 | 0 = flip disabled, 1 = flip enabled during jog |
| FlipJog_Duration | 20005 | 0–1000 | Flip pulse duration (ms) |
| FlipJog_Pressure | 20006 | 0–600 | Flip pressure (/100 = Bar) |
| FlipJog_Pause | 20007 | 0–1000 | Pause between consecutive flips (ms) |
| BlowJog_Enable | 20008 | 0–1 | 0 = blow disabled, 1 = blow enabled during jog |
| BlowJog_Duration | 20009 | 0–1000 | Blow pulse duration (ms) |
| BlowJog_Pressure | 20010 | 0–600 | Blow pressure (/100 = Bar) |
| BlowJog_Pause | 20011 | 0–1000 | Pause between consecutive blows (ms) |
| BlowJog_Type | 20012 | 0–2 | Blow type: 0 = BLOWc, 1 = BLOWe, 2 = BLOWc+BLOWe |
| Backlight_1 | 20013 | 0–1 | 0 = off, 1 = on |
| Backlight_2 | 20014 | 0–1 | 0 = off, 1 = on |


(sec-read)=
### <span class="isw-section-badge isw-badge-read"><i class="ph ph-eye"></i> READ</span>

The READ commands allow the parameters currently configured in the FlexiBowl® to be read. The value read is returned in **ReturnData_2**.

#### READ sequence addressing logic

The ControlWord for reading is calculated with the formula:

> **ControlWord = 10000 + N × 100 + parameter_offset**

where `N` is the sequence number (1–20) and `parameter_offset` is the same one used in the WRITE commands.

The readable parameters are the same as in the WRITE block, with the addition of the 10 slots of the command list:

| Additional parameter | Offset | Description |
|---|---|---|
| Seq Slot 1 Cmd | 50 | Command in position 1 in the sequence list |
| Seq Slot 2 Cmd | 51 | Command in position 2 |
| … | … | … |
| Seq Slot 10 Cmd | 59 | Command in position 10 |

#### READ ControlWord examples

| Sequence | Parameter | ControlWord |
|---|---|---|
| SEQ 1 | AccelerationMove | 10100 |
| SEQ 1 | SpeedMove | 10102 |
| SEQ 1 | FlipCount | 10110 |
| SEQ 1 | Emptying Sequence | 10140 |
| SEQ 1 | Slot 1 Cmd | 10150 |
| SEQ 1 | Slot 10 Cmd | 10159 |
| SEQ 5 | AngleMove | 10503 |
| SEQ 10 | SpeedMove | 11002 |
| SEQ 20 | Emptying Sequence | 12040 |

:::{tip}
Quick formula:  
 To read the speed (offset 02) of sequence 12, the ControlWord is `10000 + 12 × 100 + 2 = 11202`.
:::

(fieldbus_read)=
#### Practical example — “Read the angle of Sequence 16”

<div class="isw-example">
<div class="isw-example-title">AngleMove Seq 16 → ControlWord 11603</div>
<div class="isw-example-body">
<div>
<div class="isw-example-col-title">EtherNet/IP · Profinet · Modbus</div>

Packet sent:

| ControlWord | Data_1 | ExecuteCW | Hopper_1 | Hopper_2 | Hopper_3 | Hopper_4 | Reset |
|---|---|---|---|---|---|---|---|
| 11603 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 11603 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |

Packet received (angle read = 45°):

| Busy | Ready | In_Error | In_PowerOn | ReturnData_1 | ReturnData_2 | ErrorCode |
|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 1 | 11603 | 45 | 0 |


#### Parametri READ JOG

The same writable JOG parameters (block 20000) can be read in block 20100:

| Parameter | READ ControlWord | ReturnData_2 range |
|---|---|---|
| AccelerationJog | 20101 | 0–100 |
| DecelerationJog | 20102 | 0–100 |
| SpeedJog | 20103 | 0–100 (1000–1100 = negative) |
| FlipJog_Enable | 20104 | 0–1 |
| FlipJog_Duration | 20105 | 0–1000 |
| FlipJog_Pressure | 20106 | 0–600 (/100) |
| FlipJog_Pause | 20107 | 0–1000 |
| BlowJog_Enable | 20108 | 0–1 |
| BlowJog_Duration | 20109 | 0–1000 |
| BlowJog_Pressure | 20110 | 0–600 (/100) |
| BlowJog_Pause | 20111 | 0–1000 |
| BlowJog_Type | 20112 | 0–2 |
| Backlight_1 | 20113 | 0–1 |
| Backlight_2 | 20114 | 0–1 |

---

(sec-hopper)=
## <span class="isw-section-badge isw-badge-hop"><i class="ph ph-funnel"></i> HOPPER</span>

The Hopper commands control the vibratory hoppers connected to the system (up to 4). They follow the same ControlWord/WRITE/READ logic described above, valid for all protocols, plus a dedicated TCP syntax for quick start.

### Quick start via TCP

In addition to the general ControlWord syntax, the **TCP Server** protocol offers dedicated messages to start a hopper directly:

| Operation | Message to send | Response |
|---|---|---|
| Start Hopper 1 | `Hopper1Start%` | `Hopper1Start *` |
| Start Hopper 2 | `Hopper2Start%` | `Hopper2Start *` |
| Start Hopper 3 | `Hopper3Start%` | `Hopper3Start *` |
| Start Hopper 4 | `Hopper4Start%` | `Hopper4Start *` |

On the fieldbus protocols (EtherNet/IP, Profinet, Modbus) the same immediate start is obtained by directly setting the **Hopper_1**...**Hopper_4** bit of the [I/O packet](#sec-fieldbus) to `1`, without going through the ControlWord.

### Hopper WRITE Commands

| Parameter | ControlWord | Data_1 range | Description |
|---|---|---|---|
| Hopper_1_Id | 30001 | 1–100 | Unique ID of hopper 1 on the network |
| Hopper_1_Amplitude | 30002 | 50–220 | Vibration amplitude of hopper 1 |
| Hopper_1_Frequency | 30003 | 40–70 | Vibration frequency of hopper 1 |
| Hopper_1_Activation_Time | 30004 | 400–60000 | Activation time of hopper 1 (ms) |
| Hopper_2_Id | 30005 | 1–100 | Unique ID of hopper 2 |
| Hopper_2_Amplitude | 30006 | 50–220 | Vibration amplitude of hopper 2 |
| Hopper_2_Frequency | 30007 | 40–70 | Vibration frequency of hopper 2 |
| Hopper_2_Activation_Time | 30008 | 400–60000 | Activation time of hopper 2 (ms) |
| Hopper_3_Id | 30009 | 1–100 | Unique ID of hopper 3 |
| Hopper_3_Amplitude | 30010 | 50–220 | Vibration amplitude of hopper 3 |
| Hopper_3_Frequency | 30011 | 40–70 | Vibration frequency of hopper 3 |
| Hopper_3_Activation_Time | 30012 | 400–60000 | Activation time of hopper 3 (ms) |
| Hopper_4_Id | 30013 | 1–100 | Unique ID of hopper 4 |
| Hopper_4_Amplitude | 30014 | 50–220 | Vibration amplitude of hopper 4 |
| Hopper_4_Frequency | 30015 | 40–70 | Vibration frequency of hopper 4 |
| Hopper_4_Activation_Time | 30016 | 400–60000 | Activation time of hopper 4 (ms) |
| Hopper_1_Enable | 30017 | — | Enables hopper 1 (immediate action) |
| Hopper_1_Disable | 30018 | — | Disables hopper 1 (immediate action) |
| Hopper_2_Enable | 30019 | — | Enables hopper 2 |
| Hopper_2_Disable | 30020 | — | Disables hopper 2 |
| Hopper_3_Enable | 30021 | — | Enables hopper 3 |
| Hopper_3_Disable | 30022 | — | Disables hopper 3 |
| Hopper_4_Enable | 30023 | — | Enables hopper 4 |
| Hopper_4_Disable | 30024 | — | Disables hopper 4 |

:::{note}
In the training material, ControlWord `30005` (Hopper_2_Id) mistakenly showed the same range as Amplitude (50–220). In this table it has been corrected to **1–100**, consistent with Hopper_1_Id, Hopper_3_Id and Hopper_4_Id. Check this value against the firmware/datasheet before publishing the page.
:::

(fieldbus_WRITEHOPPER)=
#### Practical example — “Enable Hopper 1”

<div class="isw-example">
<div class="isw-example-title">Hopper_1_Enable → ControlWord 30017</div>
<div class="isw-example-body">
<div>
<div class="isw-example-col-title">EtherNet/IP · Profinet · Modbus</div>

Packet sent:

| ControlWord | Data_1 | ExecuteCW | Hopper_1 | Hopper_2 | Hopper_3 | Hopper_4 | Reset |
|---|---|---|---|---|---|---|---|
| 30017 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 30017 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |

Packet received:

| Busy | Ready | In_Error | In_PowerOn | ReturnData_1 | ReturnData_2 | ErrorCode |
|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 1 | 30017 | 0 | 0 |



#### Practical example — “Set the amplitude of Hopper 2 to 220”

<div class="isw-example">
<div class="isw-example-title">Hopper_2_Amplitude → ControlWord 30006, Data_1 = 220</div>
<div class="isw-example-body">
<div>
<div class="isw-example-col-title">EtherNet/IP · Profinet · Modbus</div>

Packet sent:

| ControlWord | Data_1 | ExecuteCW | Hopper_1 | Hopper_2 | Hopper_3 | Hopper_4 | Reset |
|---|---|---|---|---|---|---|---|
| 30006 | 220 | 0 | 0 | 0 | 0 | 0 | 0 |
| 30006 | 220 | 1 | 0 | 0 | 0 | 0 | 0 |

Packet received:

| Busy | Ready | In_Error | In_PowerOn | ReturnData_1 | ReturnData_2 | ErrorCode |
|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 1 | 30006 | 0 | 0 |


### Hopper READ Commands

| Parameter | READ ControlWord | ReturnData_2 range | Notes |
|---|---|---|---|
| Hopper_1_Id | 30101 | 1–100 | |
| Hopper_1_Amplitude | 30102 | 50–220 | |
| Hopper_1_Frequency | 30103 | 40–70 | |
| Hopper_1_Activation_Time | 30104 | 400–60000 | |
| Hopper_2_Id | 30105 | 1–100 | |
| Hopper_2_Amplitude | 30106 | 50–220 | |
| Hopper_2_Frequency | 30107 | 40–70 | |
| Hopper_2_Activation_Time | 30108 | 400–60000 | |
| Hopper_3_Id | 30109 | 1–100 | |
| Hopper_3_Amplitude | 30110 | 50–220 | |
| Hopper_3_Frequency | 30111 | 40–70 | |
| Hopper_3_Activation_Time | 30112 | 400–60000 | |
| Hopper_4_Id | 30113 | 1–100 | |
| Hopper_4_Amplitude | 30114 | 50–220 | |
| Hopper_4_Frequency | 30115 | 40–70 | |
| Hopper_4_Activation_Time | 30116 | 400–60000 | |
| Hopper_1_Ready | 30117 | 0–1 | 0 = not ready, 1 = ready |
| Hopper_2_Ready | 30118 | 0–1 | 0 = not ready, 1 = ready |
| Hopper_3_Ready | 30119 | 0–1 | 0 = not ready, 1 = ready |
| Hopper_4_Ready | 30120 | 0–1 | 0 = not ready, 1 = ready |
| Hopper_1_InVibration | 30121 | 0–1 | 0 = stopped, 1 = vibrating |
| Hopper_2_InVibration | 30122 | 0–1 | 0 = stopped, 1 = vibrating |
| Hopper_3_InVibration | 30123 | 0–1 | 0 = stopped, 1 = vibrating |
| Hopper_4_InVibration | 30124 | 0–1 | 0 = stopped, 1 = vibrating |
| Hopper_1_Enabled | 30125 | 0–1 | 0 = disabled, 1 = enabled |
| Hopper_2_Enabled | 30126 | 0–1 | 0 = disabled, 1 = enabled |
| Hopper_3_Enabled | 30127 | 0–1 | 0 = disabled, 1 = enabled |
| Hopper_4_Enabled | 30128 | 0–1 | 0 = disabled, 1 = enabled |

(fieldbus_READHOPPER)=
#### Practical example — “Read the frequency of Hopper 4”

<div class="isw-example">
<div class="isw-example-title">Hopper_4_Frequency → ControlWord 30115</div>
<div class="isw-example-body">
<div>
<div class="isw-example-col-title">EtherNet/IP · Profinet · Modbus</div>

Packet sent:

| ControlWord | Data_1 | ExecuteCW | Hopper_1 | Hopper_2 | Hopper_3 | Hopper_4 | Reset |
|---|---|---|---|---|---|---|---|
| 30115 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 30115 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |

Packet received (frequency read = 40):

| Busy | Ready | In_Error | In_PowerOn | ReturnData_1 | ReturnData_2 | ErrorCode |
|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 1 | 30115 | 40 | 0 |


:::{note}
For the Emptying commands, refer to the [Emptying Commands](sec-empty) section
:::

:::{important}
For the Error Codes, refer to the [Error Codes](sec-err) section
:::