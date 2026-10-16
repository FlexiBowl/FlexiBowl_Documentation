<style>
.compare-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  margin: 1rem 0 1.5rem;
}
@media (max-width: 680px) {
  .compare-grid { grid-template-columns: 1fr; }
}
.compare-card {
  border: 1px solid #5a9fd4;
  border-radius: 7px;
  overflow: hidden;
  font-size: 0.92rem;
}
.compare-card-header {
  padding: 0.5rem 1rem;
  font-weight: 700;
  font-size: 0.82rem;
  letter-spacing: 0.05em;
  color: #ffffff;
}
.v20 .compare-card-header { background: #1a4a7a; }
.v30 .compare-card-header { background: #1e6fbf; }
.compare-card-body {
  padding: 0.85rem 1rem;
}
.compare-card-body p, .compare-card-body li { margin: 0.25rem 0; }
.compare-card-body ul, .compare-card-body ol { padding-left: 1.2rem; margin: 0.4rem 0; }
.compare-card-body table {
  width: 100%;
  border-collapse: collapse;
  margin: 0.5rem 0;
  font-size: 0.88rem;
}
.compare-card-body table th {
  padding: 0.35rem 0.6rem;
  text-align: left;
  font-size: 0.78rem;
  font-weight: 700;
  border-bottom: 2px solid #5a9fd4;
  opacity: 0.75;
}
.compare-card-body table td {
  padding: 0.35rem 0.6rem;
  border-bottom: 1px solid rgba(90, 159, 212, 0.3);
}
.compare-card-body table tr:last-child td { border-bottom: none; }
.compare-card-body pre {
  border: 1px solid rgba(90, 159, 212, 0.4);
  border-radius: 5px;
  padding: 0.7rem 0.9rem;
  font-size: 0.8rem;
  overflow-x: auto;
  margin: 0.5rem 0 0;
}
</style>
 
# [SOF] **Software Comparison**
 
This page compares the main software differences between **FlexiBowl® 2.0** and **FlexiBowl® 3.0**, with the aim of guiding the user in understanding the new features and the operational changes introduced by the new generation.
 
:::{important}
Before reading the contents of the current page, it is good practice to be familiar with the information given in the [Software Interface](int_software) page
:::
---
 
## 1. Available communication protocols
 
| Protocol | FlexiBowl® 2.0 | FlexiBowl® 3.0 |
|---|---|---|
| TCP/IP – UDP | ✓ | ✓ (TCP Server) |
| EtherNet/IP | ✓ | ✓ |
| Profinet | ✗ | ✓ |
| Modbus | ✗ | ✓ |
| Digital I/O | ✓ | ✓ (optional) |
 
---
 
## 2. User interface: what it looks like and how to access it
 
<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0 — Software Parameters</div>
<div class="compare-card-body">
 
**Desktop** interface called **FlexiBowl® Parameters**, to be installed on the control PC.
 
**Installation and access:**
 
1. Install the **FlexiBowl® Parameters** program on the PC (supplied by ARS).
2. Connect the PC to the FlexiBowl® via an **Ethernet cable** (direct LAN or via switch).
3. Start the program and enter the **IP address** of the FlexiBowl® to connect.
 
From the **Main Commands** screen, the **Move**, **Shake** and **Option** panels are accessible via tabs at the top.
 
</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0 — Web Interface</div>
<div class="compare-card-body">
 
**Fully web-based** interface: no installation is required. A modern browser is sufficient.
 
**Access:**
 
1. Connect the PC to the FlexiBowl® via Ethernet.
2. Open the browser and type the **IP address** of the FlexiBowl® in the address bar.
3. The interface **Home page** opens.
 
**Interface structure:**
 
The side menu includes pages dedicated to each operating function (Main Command, Jog Motor, Setup, Monitor, etc.), accessible directly from the browser.
 
</div>
</div>
</div>
 
:::{note}
If the system in use is **FlexiVision One**, the configuration is managed from its dedicated interface. It is not necessary to use the FlexiBowl® software interface described in this section.
:::
 
---
 
## 3. How to change the IP address
 
<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0</div>
<div class="compare-card-body">
 
1. Use the program supplied on the USB drive.
2. Connect the FlexiBowl® via Ethernet cable.
3. Switch on the device.
4. Start the program.
5. In the **IP Address** box, enter the address: `192.168.1.10`  
   *(The connected PC must be in the same Class B subnet mask — 255.255.0.0)*
6. Press **Ping** → pop-up **"FlexiBowl® found"**.
7. Press **Ok** to enable **CONNECT** and start the connection.
8. After connecting, the home screen will be displayed.
 
</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0</div>
<div class="compare-card-body">
 
1. Open the browser and access the interface via the current IP.
2. From the side menu, open the **Setup** page.
3. Click **Get IP** to read the current network parameters.
4. Enter the new IP address in the dedicated fields and click **Set IP**.
5. Click **Apply** to confirm, then **Reboot** to make the changes effective.
 
</div>
</div>
</div>
 
:::{note}
**FlexiBowl® 2.0** — If a previous version of the program is installed, it must be uninstalled first.
:::
 
:::{important}
**FlexiBowl® 3.0** — After the reboot, reconnect to the FlexiBowl® using the new IP address that was set.
:::
 
---
 
## 4. How to manage movements
 
<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0</div>
<div class="compare-card-body">
 
Movements are configured and tested from **Main Commands**, with three panels:
 
- **Move**: sets Acceleration, Deceleration, Speed and Angle via slider or numeric field. **Test Move** executes the movement with the set values.
- **Shake**: parameters CCW Angle, CW Angle, Count, Acceleration, Deceleration and Speed. **Test Shake** executes the shake.
- **Try Commands**: combines several commands into a sequence with a configurable loop, by selecting from **All Commands** and adding to **Selected Commands**.
 
For production via protocol, ASCII commands are sent (e.g. `QX2` for Move, `QX6` for Shake) through the configured TCP/UDP channel.
 
</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0</div>
<div class="compare-card-body">
 
Movements are organized into **sequences** (up to 20), configurable from the **Main Command** page. Each sequence contains up to 10 command slots (Move, Shake, Flip, Blow).
 
From the **Main Command** page it is possible to:
 
- Select the sequence via **Select the sequence**.
- Set all the parameters in the numeric fields.
- Add commands with **Command Available** + **ADD**; reorder them with **UP/DOWN**; delete them with **DELETE** or clear all with **CLEAR**.
- Test with **TEST SEQUENCE** or start production with **RUN**.
 
The **Jog Motor** page allows continuous rotation (positive Speed = clockwise, negative = counterclockwise) with integrated Flip and Blow.
 
For production via protocol: `10[0]%` for Sequence 1 via TCP, or ControlWord `10` via EtherNet/IP or Profinet.
 
</div>
</div>
</div>
 
---
 
## 5. How to change the parameters
 
<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0</div>
<div class="compare-card-body">
 
The operating parameters are modified in two ways:
 
- **Graphical interface**: sliders or numeric fields in the Move and Shake screens of **Main Commands**.
- **Via protocol (runtime)**: `RW` (Write) and `RL` (Read) commands via TCP/UDP. The values must be multiplied by the machine **reduction factor** (obtained with the `RR114` command), since the parameters are expressed in internal driver units.
 
</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0</div>
<div class="compare-card-body">
 
The parameters are modified in three ways:
 
- **Web interface**: directly in the numeric fields of the **Main Command** page for each sequence.
- **Via WRITE protocol**: WRITE block ControlWord with formula `N × 100 + parameter_offset`
- **Via READ protocol**: READ block ControlWord with formula `10000 + N × 100 + parameter_offset`
 
</div>
</div>
</div>
 
---
 
### Practical example: Move + Shake on FlexiBowl® 800
 
The scenario is as follows: execute a **Move** at 360°, then a **Shake**, then a 200 ms wait.
 
<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0 — TCP command sequence</div>
<div class="compare-card-body">
 
The parameters must be scaled using the machine **reduction factor**:
 
<pre>QX7                     → Switch on backlight
RR114                   → Read reduction factor
reduction_variable = RX 1
 
RL1 (50 × reduction_variable), RW11   → Acceleration Move = 50%
RL1 (50 × reduction_variable), RW12   → Deceleration Move = 50%
RL1 (35 × reduction_variable), RW13   → Speed Move = 35%
RL1 (360 × reduction_variable), RW14  → Angle Move = 360°
QX2                     → Execute Move
 
RL1 (50 × reduction_variable), RW15  → Acceleration Shake = 50%
RL1 (50 × reduction_variable), RW16  → Deceleration Shake = 50%
RL1 (50 × reduction_variable), RW110 → Speed Shake = 50%
RL1 (30 × reduction_variable), RW18  → Angle CW Shake = -30°
RL1 (30 × reduction_variable), RW19  → Angle CCW Shake = -45°
RL1 2, RW17                           → Count Shake = 2
QX6                     → Execute Shake</pre>
 
The 200 ms wait is handled by the calling system (robot or PLC).
 
</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0 — Web interface configuration</div>
<div class="compare-card-body">
 
From the **Main Command** page, select **SEQUENCE 1** and set:
 
| Parameter | Value |
|---|---|
| Acceleration Move | 50 % |
| Deceleration Move | 50 % |
| Speed Move | 35 % |
| Angle Move | 360° |
| Acceleration Shake | 50 % |
| Deceleration Shake | 50 % |
| Speed Shake | 50 % |
| Ccw Angle Shake | −45° |
| Cw Angle Shake | −30° |
| Count Shake | 2 |
 
Add to the list: `FLB_MOVE` → `FLB_SHAKE`. Check Backlight from the **Option** page. The 200 ms wait is handled by adding `FLB_WAIT` to the list or on the calling system side.
 
To execute the sequence via TCP:
 
<pre>10[0]%    → Execute Sequence 1</pre>
 
The system replies with `10[0]` as confirmation.
 
</div>
</div>
</div>
 
---
 
## 6. How to read the alarms
 
<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0</div>
<div class="compare-card-body">
 
Alarms are consulted from **Monitor → Alarm Status** of the **FlexiBowl® Parameters** program. The screen shows the driver statuses with LED indicators (green = OK, red = error). The **Driver Status** screen shows all the operating variables in real time.
 
Alarm reset via protocol:
 
<pre>Chr(0)Chr(7)QX12Chr(13)    → Alarm reset and motor re-enable</pre>
 
</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0</div>
<div class="compare-card-body">
 
Alarms are consulted from the **Monitor** page (tabs: **I/O Status**, **Driver Status**, **Alarm Status**).
 
Via protocol, the alarm signal is exposed by **In_Error** (BOOL) and the active code by **ErrorCode** (UDINT):
 
<pre>InError%         → InError[1]% if there is an error, InError[0]% if OK
ErrorCode%       → ErrorCode[N]% with the code of the active error</pre>
 
Alarm reset:
- Via TCP protocol: `Reset%`
- Via digital variable: rising edge on the **Reset** input signal (BOOL)
 
</div>
</div>
</div>
 
:::{warning}
Before performing the reset, identify and resolve the cause of the error. The system will not execute new movement commands while an error is active.
:::
 
:::{note}
For the complete list of error codes, refer to the [Error Codes](sec-err) section
:::
 
---
 
## 7. Tracking mode (FlexiTrack)
 
<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0</div>
<div class="compare-card-body">
 
The **FlexiTrack** mode is an option that can be purchased separately and allows the FlexiBowl® to be kept in **continuous rotation** (jog) by synchronizing the encoder signal with the pick robot.
 
**Required hardware:**
 
- Connection to the **internal encoder** via the control panel connector (TTL quadrature signal, 4000 counts/rev on the motor; for FlexiBowl® 500/650/800 with 1:3 reduction → 12000 counts/rev on the disc).
- Alternatively, an **external encoder** (incremental, TTL RS422, ≥ 12000 ppr) on the pin integral with the driven pulley.
 
**Main FlexiTrack commands (via TCP/UDP):**
 
| Command | Description |
|---|---|
| `JA<value>` | Acceleration/deceleration in rev/s² |
| `JL<value>` | Deceleration (if different from JA, send after JA) |
| `JS<value>` | Rotation speed in rev/s |
| `CC<value>` | Current directed to the motor |
| `DI1` | Clockwise direction |
| `DI-1` | Counterclockwise direction |
| `CJ` | Start jog (continuous rotation) |
| `SJ` | Stop jog (with JL ramp) |
| `IL2` / `IH2` | Activate / deactivate Flip |
| `IL3` / `IH3` | Activate / deactivate Blow |
 
**Recommended parameters:**
 
<pre>JA0.2    → acceleration 0.2 rev/s²
JL0.2    → deceleration 0.2 rev/s²
JS0.2    → speed 0.2 rev/s
CC1.3    → motor current
DI1      → clockwise rotation</pre>
 
Flip and Blow must be implemented through a **background program** with an iterative loop that toggles the state of the valves.
 
</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0</div>
<div class="compare-card-body">
 
The jog mode is **natively integrated** into the **Jog Motor** page — without additional hardware options.
 
**Jog motion parameters:**
 
| Parameter | Unit | Description |
|---|---|---|
| Acceleration | % | Acceleration ramp at start-up |
| Deceleration | % | Deceleration ramp at stop |
| Speed | % | Speed — positive = clockwise; negative = counterclockwise |
 
**Accessory functions during Jog:**
 
- **Flip Enable**: automatic cyclic flip with Flip Duration, Flip Pression, Flip Pause.
- **Blow Enable**: automatic cyclic blow with Blow Duration, Blow Pression, Blow Pause, Blow Type (BLOWc, BLOWe, BLOWc+BLOWe).
- **Backlight 1 / 2**: backlight toggle, independent of the jog state.
 
**Start and stop:**
 
- **START JOG**: starts continuous rotation.
- **STOP JOG**: stops with a deceleration ramp.
 
Control via protocol:
 
<pre>40[0]%    → Start Jog Seq (via TCP)
41[0]%    → Stop Jog Seq (via TCP)</pre>
 
</div>
</div>
</div>
 
:::{important}
Before starting the jog, check that the motor is enabled (**ENABLE MOTOR** active) and that the system status is **READY**.
:::
 
:::{important}
With FlexiTrack **(FlexiBowl® 2.0)**, motion control is possible **only via Ethernet protocol** (TCP/UDP). The Digital I/O protocol is not supported.
:::