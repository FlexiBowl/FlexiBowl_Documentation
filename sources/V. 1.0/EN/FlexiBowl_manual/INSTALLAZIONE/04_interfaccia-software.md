(int_software)=
# **Software Interface**

<script src="https://unpkg.com/@phosphor-icons/web"></script>

<div class="isw-page">
<style>
  /* ── Reset & base ── */
  .isw-page { font-family: inherit; max-width: 860px; margin: 0 auto; padding: 0 0 3rem; }

 /* ── NAV CARDS ── */
  .isw-nav {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    gap: 0.75rem;
    margin: 1.5rem 0 2.5rem;
  }
  .isw-nav-card {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 0.45rem;
    padding: 0.9rem 1rem;
    border: 1.5px solid #d0e4f0;
    border-radius: 10px;
    background: #fff;
    text-decoration: none;
    color: inherit;
    transition: border-color 0.18s, background 0.18s, transform 0.18s;
  }
  .isw-nav-card:hover {
    border-color: #2980b9;
    background: #f0f7ff;
    transform: translateY(-2px);
    text-decoration: none;
  }
  .isw-nav-card i {
    font-size: 1.4rem;
    color: #2980b9;
  }
  .isw-nav-card-title {
    font-weight: 700;
    font-size: 0.82rem;
    color: #1a3a52;
    line-height: 1.3;
  }
  .isw-nav-card-sub {
    font-size: 0.72rem;
    color: #7a9ab0;
  }

  /* ── FLOW DIAGRAM — orizzontale ── */
  .isw-flow {
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 0;
    margin: 1.5rem 0 2rem;
    overflow-x: auto;
    padding-bottom: 0.5rem;
    flex-wrap: nowrap;
  }
  .isw-flow-step {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.35rem;
    min-width: 110px;
    flex: 1;
  }
  .isw-flow-bubble {
    width: 48px;
    height: 48px;
    border-radius: 50%;
    background: #e3f1fb;
    border: 2px solid #2980b9;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #2980b9;
    font-size: 1.2rem;
    flex-shrink: 0;
  }
  .isw-flow-label {
    font-size: 0.72rem;
    font-weight: 600;
    color: #1a3a52;
    text-align: center;
    line-height: 1.3;
  }
  .isw-flow-sub {
    font-size: 0.65rem;
    color: #7a9ab0;
    text-align: center;
  }
  .isw-flow-arrow {
    color: #bcd6ec;
    font-size: 1.6rem;
    flex-shrink: 0;
    margin: 0 2px;
    padding-bottom: 1.8rem;
    display: flex;
    align-items: flex-start;
    padding-top: 0.2rem;
  }

  /* ── FORMULA BOX ── */
  .isw-formula {
    background: #f0f7ff;
    border-left: 4px solid #2980b9;
    border-radius: 0 8px 8px 0;
    padding: 1rem 1.25rem;
    margin: 1rem 0 1.5rem;
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    align-items: center;
  }
  .isw-formula-main {
    font-family: monospace;
    font-size: 1.05rem;
    font-weight: 700;
    color: #1a3a52;
    white-space: nowrap;
  }
  .isw-formula-example {
    font-size: 0.8rem;
    color: #556b7d;
    border-left: 1px solid #bcd6ec;
    padding-left: 1rem;
  }
  .isw-formula-example strong { color: #2980b9; }

  /* ── SECTION BADGES ── */
  .isw-section-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    border-radius: 5px;
    padding: 3px 10px;
    margin-bottom: 0.6rem;
  }
  .isw-badge-exe  { background: #dbeafe; color: #1d4ed8; }
  .isw-badge-write{ background: #fef3c7; color: #92400e; }
  .isw-badge-read { background: #d1fae5; color: #065f46; }
  .isw-badge-io   { background: #ede9fe; color: #5b21b6; }
  .isw-badge-tcp  { background: #fce7f3; color: #9d174d; }
  .isw-badge-err  { background: #fee2e2; color: #991b1b; }
  .isw-badge-field { background: #dcfce7; color: #166534; }
  .isw-badge-hop  { background: #ffe4e6; color: #9f1239; }

  /* ── TABLES ── */
  .isw-table-wrap {
    overflow-x: auto;
    border-radius: 8px;
    border: 1px solid #e2eef6;
    margin: 0.75rem 0 1.5rem;
  }
  .isw-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.82rem;
  }
  .isw-table thead tr {
    background: #1a3a52;
    color: #fff;
    position: sticky;
    top: 0;
    z-index: 1;
  }
  .isw-table thead th {
    padding: 0.6rem 0.9rem;
    text-align: left;
    font-weight: 600;
    white-space: nowrap;
  }
  .isw-table tbody tr:nth-child(even) { background: #f7fbfe; }
  .isw-table tbody tr:hover { background: #e8f4fc; }
  .isw-table tbody td {
    padding: 0.5rem 0.9rem;
    border-bottom: 1px solid #e9f2f9;
    color: #334e5e;
    vertical-align: top;
  }
  .isw-table tbody td:first-child {
    font-weight: 600;
    color: #1a3a52;
    white-space: nowrap;
  }
  .isw-table code {
    background: #e3f1fb;
    color: #1d4ed8;
    border-radius: 3px;
    padding: 1px 5px;
    font-size: 0.8rem;
  }
  .isw-table tbody tr.isw-hidden { display: none; }

  /* ── TABELLA ERRORI DRIVER — stile Sphinx standard ── */
  .isw-err-wrap {
    overflow-x: auto;
    margin: 0.75rem 0 1.5rem;
  }
  .isw-err-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.85rem;
  }
  .isw-err-table thead tr {
    background: #f0f4f8;
  }
  .isw-err-table thead th {
    padding: 0.55rem 0.8rem;
    text-align: left;
    font-weight: 700;
    color: #1a3a52;
    border: 1px solid #c8d8e4;
  }
  .isw-err-table tbody tr:nth-child(even) { background: #f7fbfe; }
  .isw-err-table tbody tr:hover { background: #cfe2ff; }
  .isw-err-table tbody td {
    padding: 0.45rem 0.8rem;
    border: 1px solid #c8d8e4;
    color: #334e5e;
    vertical-align: top;
  }
  .isw-err-table tbody td:first-child {
    font-weight: 600;
    color: #1a3a52;
    white-space: nowrap;
  }
  .isw-err-table code {
    font-family: monospace;
    font-size: 0.82rem;
    color: #1a3a52;
    background: none;
    padding: 0;
  }
  .isw-err-table tbody tr.isw-hidden { display: none; }

  /* ── SEARCH BOX ── */
  .isw-search-wrap {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-bottom: 0.75rem;
  }
  .isw-search {
    flex: 1;
    max-width: 340px;
    padding: 0.45rem 0.75rem 0.45rem 2.2rem;
    border: 1.5px solid #d0e4f0;
    border-radius: 7px;
    font-size: 0.85rem;
    color: #1a3a52;
    outline: none;
    background: #fff url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='14' height='14' viewBox='0 0 256 256'%3E%3Cpath fill='%237a9ab0' d='M229.66 218.34l-50.07-50.07a88.11 88.11 0 1 0-11.31 11.31l50.06 50.07a8 8 0 0 0 11.32-11.31ZM40 112a72 72 0 1 1 72 72 72.08 72.08 0 0 1-72-72Z'/%3E%3C/svg%3E") no-repeat 0.6rem center;
    transition: border-color 0.18s;
  }
  .isw-search:focus { border-color: #2980b9; }
  .isw-search-count {
    font-size: 0.75rem;
    color: #7a9ab0;
  }

  /* ── RETURN DATA — tabella leggibile ── */
  .isw-return-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.88rem;
    margin: 0.75rem 0 1.5rem;
  }
  .isw-return-table thead tr {
    background: #e3f1fb;
  }
  .isw-return-table thead th {
    padding: 0.55rem 1rem;
    text-align: left;
    font-weight: 700;
    color: #1a3a52;
    border-bottom: 2px solid #2980b9;
  }
  .isw-return-table tbody tr:nth-child(even) { background: #f7fbfe; }
  .isw-return-table tbody tr:hover { background: #cfe2ff; }
  .isw-return-table tbody td {
    padding: 0.55rem 1rem;
    border-bottom: 1px solid #d0e4f0;
    color: #334e5e;
    vertical-align: middle;
  }
  .isw-return-table tbody td:first-child {
    font-family: monospace;
    font-size: 1rem;
    font-weight: 700;
    color: #2980b9;
    white-space: nowrap;
    width: 90px;
  }

  /* ── ESEMPI PRATICI (pacchetto dati) ── */
  .isw-example {
    border: 1px solid #d0e4f0;
    border-radius: 10px;
    margin: 1rem 0 1.75rem;
    overflow: hidden;
  }
  .isw-example-title {
    background: #f0f7ff;
    padding: 0.6rem 1rem;
    font-weight: 700;
    font-size: 0.88rem;
    color: #1a3a52;
    border-bottom: 1px solid #d0e4f0;
  }
  .isw-example-body {
    padding: 1rem;
    display: grid;
    grid-template-columns: 1fr;
    gap: 1.25rem;
  }
  .isw-example-body > div + div {
    border-top: 1px solid #e2eef6;
    padding-top: 1rem;
  }
  .isw-example-col-title {
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    color: #2980b9;
    margin-bottom: 0.5rem;
    text-transform: uppercase;
  }
  .isw-example-body table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.78rem;
    margin-bottom: 0.5rem;
  }
  .isw-example-body table th {
    background: #f0f4f8;
    padding: 0.35rem 0.5rem;
    text-align: center;
    font-weight: 700;
    color: #1a3a52;
    border: 1px solid #d0e4f0;
    white-space: nowrap;
  }
  .isw-example-body table td {
    padding: 0.35rem 0.5rem;
    text-align: center;
    border: 1px solid #d0e4f0;
    color: #334e5e;
  }
  .isw-example-tcp {
    font-family: monospace;
    font-size: 0.85rem;
    background: #f7fbfe;
    border-radius: 6px;
    padding: 0.6rem 0.8rem;
    margin: 0.35rem 0;
  }
  .isw-example-tcp .ok { color: #166534; font-weight: 700; }
  .isw-example-tcp .ko { color: #991b1b; font-weight: 700; }
</style>

## Introduction

The new FlexiBowl® interface is fully web-based. To access it, simply enter the default IP address of the FlexiBowl® `192.168.1.10` in the address bar of your browser.

:::{video} ../../../../_shared/media/videos/IP_Home.mp4
:width: 90%
:::


## Communication 

The communication system is based on **Input/Output variables** and numeric **Control Words**: the external system sends a number (the ControlWord) that identifies the action to be performed and the FlexiBowl® responds with status signals and return data.

Supported protocols:
- **TCP Server**
- **EtherNet/IP**
- **Profinet**
- **Modbus**

:::{important}
The variables, ControlWords and all the **EXE**, **WRITE** and **READ** commands described on this page are **identical for all four communication protocols**. What changes from protocol to protocol is **only the way in which this data is physically exchanged**:

- **EtherNet/IP, Profinet and Modbus** behave the same way as each other: they exchange a **cyclic I/O packet** with fixed fields (see [Fieldbus Transport](#sec-fieldbus)).
- **TCP Server**, on the other hand, uses **text messages** over a socket (see [TCP Syntax](#sec-tcp)).

For this reason, every practical example on this page is shown in both modes.
:::

---

### Navigate the page

<div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:1rem; margin:1.5rem 0 2.5rem;">

  <a href="#sec-io" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit; transition:border-color 0.18s, background 0.18s;">
    <i class="ph ph-arrows-left-right" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">I/O Variables</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Input & Output</span>
  </a>

  <a href="#sec-fieldbus" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-swap" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Fieldbus Transport</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">EtherNet/IP, Profinet, Modbus</span>
  </a>

  <a href="#sec-tcp" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-network" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">TCP Syntax</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Socket messages</span>
  </a>

  <a href="#sec-exe" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-play-circle" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">EXE Commands</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Start sequences & jog</span>
  </a>

  <a href="#sec-write" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-pencil-simple" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">WRITE Commands</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Writing parameters</span>
  </a>

  <a href="#sec-read" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-eye" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">READ Commands</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Reading parameters</span>
  </a>

  <a href="#sec-hopper" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-funnel" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Hopper Commands</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Bulk Feeder</span>
  </a>

  <a href="#sec-empty" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-arrow-counter-clockwise" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Quick Emptying</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Emptying Option</span>
  </a>

  <a href="#sec-err" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-warning-circle" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Error Codes</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Diagnostics</span>
  </a>

</div>

---

### How a command works

This logic is **identical for all protocols**: only the way in which the 4 steps are physically transmitted changes (I/O packet for fieldbus protocols, text message for TCP — see the following sections).

<table style="width:100%; border-collapse:collapse; margin: 1.5rem 0 2rem;">
  <tr>
    <td style="text-align:center; padding:0 8px; width:22%;">
      <div style="width:52px; height:52px; border-radius:50%; background:#e3f1fb; border:2px solid #2980b9; display:inline-flex; align-items:center; justify-content:center; color:#2980b9; font-size:1.4rem; font-weight:700; margin-bottom:0.5rem;">
        1
      </div><br>
      <span style="font-size:0.92rem; font-weight:700; color:#1a3a52; line-height:1.4;">Set<br>ControlWord</span><br>
      <span style="font-size:0.8rem; color:#7a9ab0;">command number</span>
    </td>
    <td style="text-align:center; color:#bcd6ec; font-size:1.6rem; width:4%; vertical-align:middle; padding-bottom:1.8rem;">
      <i class="ph ph-caret-right"></i>
    </td>
    <td style="text-align:center; padding:0 8px; width:22%;">
      <div style="width:52px; height:52px; border-radius:50%; background:#e3f1fb; border:2px solid #2980b9; display:inline-flex; align-items:center; justify-content:center; color:#2980b9; font-size:1.4rem; font-weight:700; margin-bottom:0.5rem;">
        2
      </div><br>
      <span style="font-size:0.92rem; font-weight:700; color:#1a3a52; line-height:1.4;">Set<br>Data_1</span><br>
      <span style="font-size:0.8rem; color:#7a9ab0;">if required</span>
    </td>
    <td style="text-align:center; color:#bcd6ec; font-size:1.6rem; width:4%; vertical-align:middle; padding-bottom:1.8rem;">
      <i class="ph ph-caret-right"></i>
    </td>
    <td style="text-align:center; padding:0 8px; width:22%;">
      <div style="width:52px; height:52px; border-radius:50%; background:#e3f1fb; border:2px solid #2980b9; display:inline-flex; align-items:center; justify-content:center; color:#2980b9; font-size:1.4rem; font-weight:700; margin-bottom:0.5rem;">
        3
      </div><br>
      <span style="font-size:0.92rem; font-weight:700; color:#1a3a52; line-height:1.4;">Rising edge<br>ExecuteCW</span><br>
      <span style="font-size:0.8rem; color:#7a9ab0;">trigger 0 → 1</span>
    </td>
    <td style="text-align:center; color:#bcd6ec; font-size:1.6rem; width:4%; vertical-align:middle; padding-bottom:1.8rem;">
      <i class="ph ph-caret-right"></i>
    </td>
    <td style="text-align:center; padding:0 8px; width:22%;">
      <div style="width:52px; height:52px; border-radius:50%; background:#e3f1fb; border:2px solid #2980b9; display:inline-flex; align-items:center; justify-content:center; color:#2980b9; font-size:1.4rem; font-weight:700; margin-bottom:0.5rem;">
        4
      </div><br>
      <span style="font-size:0.92rem; font-weight:700; color:#1a3a52; line-height:1.4;">Wait<br>Busy = 0</span><br>
      <span style="font-size:0.8rem; color:#7a9ab0;">and ReturnData_1 = CW</span>
    </td>
  </tr>
</table>


1. The external system sets the **ControlWord** with the number of the desired command.
2. If the command requires an argument, it also sets **Data_1**.
3. Sends a rising edge on **ExecuteControlWord**.
4. Waits for **Busy** to return to `0` and for **ReturnData_1** to return the ControlWord value (confirmation of correct execution).

:::{warning}
Do not send a new command while **Busy** is `1`. The system will ignore the command and **ReturnData_1** will return the value `3` (system busy).
:::

---

(sec-io)=
## Input and Output Variables 

These variables are **the same for all communication protocols**: only the way they are exchanged changes (see [Fieldbus Transport](#sec-fieldbus) and [TCP Syntax](#sec-tcp)).

### INPUT — Signals sent to the FlexiBowl®

| Variable | Type | Description |
|---|---|---|
| **ControlWord** | UDINT | Integer that identifies the command to be executed. Each value corresponds to a specific action (see command table). |
| **Data_1** | UDINT | Numeric argument associated with the ControlWord, when required (e.g. the speed value to be written). The meaning depends on the selected command. |
| **ExecuteControlWord** | BOOL | Trigger signal: on the **rising edge** (from 0 to 1) the ControlWord is read and the command is executed. |
| **Hopper_1** | BOOL | Directly activates Hopper 1, independently of the ControlWord. |
| **Hopper_2** | BOOL | Directly activates Hopper 2. |
| **Hopper_3** | BOOL | Directly activates Hopper 3. |
| **Hopper_4** | BOOL | Directly activates Hopper 4. |
| **Reset** | BOOL | On the rising edge, resets the active errors on the device. |

### OUTPUT — Signals sent by the FlexiBowl®

| Variable | Type | Description |
|---|---|---|
| **Busy** | BOOL | Is `1` while the FlexiBowl® is executing a command. As long as it is active, do not send new commands. |
| **Ready** | BOOL | Is `1` when the device is ready to receive new commands. |
| **In_Error** | BOOL | Is `1` if there are active errors on the device. Check **ErrorCode** to identify the type of error. |
| **ReturnData_1** | UDINT | Confirmation of the command received (echo). The possible values are: `0` = initial state (no command), `1` = command not interpretable, `2` = wrong Data_1 but command recognized, `3` = system busy (Busy), or the ControlWord value itself = command executed correctly. |
| **ReturnData_2** | UDINT | Contains the data requested by the read (READ) commands. |
| **ErrorCode** | UDINT | Numeric code of the active error. Is `0` if there are no errors. See the [Error Codes](#codici-di-errore) section for the meaning of each code. |
| **InPowerOn** | BOOL | Is `1` if the device is powered and operational. |


### ReturnData_1 values

<div class="isw-ret">
<style>
.isw-ret table thead tr,
.isw-ret table thead tr th {
  background: #f0f4f8 !important;
  color: #1a3a52 !important;
  border-bottom: 2px solid #2980b9 !important;
}
</style>
<table style="width:100%; border-collapse:collapse; font-size:0.95rem; margin:0.75rem 0 1.5rem;">
  <thead>
    <tr>
      <th style="padding:0.6rem 0.9rem; text-align:left; font-weight:700; white-space:nowrap; width:100px;">Value</th>
      <th style="padding:0.6rem 0.9rem; text-align:left; font-weight:700;">Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#fff;" onmouseover="this.style.background='#e8f4fc'" onmouseout="this.style.background='#fff'">
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; font-family:monospace; font-size:1.05rem; font-weight:700; color:#2980b9;">0</td>
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; color:#334e5e;">NULL — no command in progress (initial state)</td>
    </tr>
    <tr style="background:#f7fbfe;" onmouseover="this.style.background='#e8f4fc'" onmouseout="this.style.background='#f7fbfe'">
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; font-family:monospace; font-size:1.05rem; font-weight:700; color:#2980b9;">1</td>
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; color:#334e5e;">Command not interpretable (unknown ControlWord)</td>
    </tr>
    <tr style="background:#fff;" onmouseover="this.style.background='#e8f4fc'" onmouseout="this.style.background='#fff'">
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; font-family:monospace; font-size:1.05rem; font-weight:700; color:#2980b9;">2</td>
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; color:#334e5e;">Data_1 out of range, command recognized</td>
    </tr>
    <tr style="background:#f7fbfe;" onmouseover="this.style.background='#e8f4fc'" onmouseout="this.style.background='#f7fbfe'">
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; font-family:monospace; font-size:1.05rem; font-weight:700; color:#2980b9;">3</td>
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; color:#334e5e;">System busy (Busy) — try again</td>
    </tr>
    <tr style="background:#fff;" onmouseover="this.style.background='#e8f4fc'" onmouseout="this.style.background='#fff'">
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; font-family:monospace; font-size:1.05rem; font-weight:700; color:#2980b9;">= CW</td>
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; color:#334e5e;">Command executed correctly</td>
    </tr>
  </tbody>
</table>
</div>

---

(sec-fieldbus)=
## EtherNet/IP, Profinet, Modbus - <span class="isw-section-badge isw-badge-field"><i class="ph ph-swap"></i> FIELDBUS</span>

For **EtherNet/IP**, **Profinet** and **Modbus**, the [Input](#sec-io) and [Output](#sec-io) variables are exchanged as a **cyclic I/O packet**: there are no text messages, each variable occupies a fixed position in the data packet. For all detailed information on this protocol, refer to the [next](fieldbus) page.

### Data packet — Input (to the FlexiBowl®)

| ControlWord | Data_1 | ExecuteControlWord | Hopper_1 | Hopper_2 | Hopper_3 | Hopper_4 | Reset |
|---|---|---|---|---|---|---|---|
| *(command number)* | *(argument)* | *(trigger bit 0→1)* | *(bit)* | *(bit)* | *(bit)* | *(bit)* | *(bit)* |

### Data packet — Output (from the FlexiBowl®)

| Busy | Ready | In_Error | In_PowerOn | ReturnData_1 | ReturnData_2 | ErrorCode |
|---|---|---|---|---|---|---|
| *(bit)* | *(bit)* | *(bit)* | *(bit)* | *(ControlWord echo)* | *(data read)* | *(error code)* |

:::{note}
The write sequence is always the same: set **ControlWord** (and **Data_1** if required) with **ExecuteControlWord = 0**, then bring **ExecuteControlWord** to `1` to generate the rising edge that starts execution.
:::

:::{card} GO TO THE DEDICATED PAGE
:link: fieldbus
:link-type: ref
:class-card: isw-card-field
:class-body: isw-card-body

Complete documentation of the Fieldbus protocol (EtherNet/IP, Profinet, Modbus)
:::

---

(sec-tcp)=
## Message Syntax <span class="isw-section-badge isw-badge-tcp"><i class="ph ph-network"></i> TCP SERVER</span>

When **TCP Server** communication is used, commands are not sent as binary variables but as **text strings** through a socket connection on the configured port (default: 8123). For all detailed information on this protocol, refer to the [next](tcp) page.

### Message structure

Each message has the form:

```
NomeVariabile[Valore]%
```

The `%` character is the **message terminator** and must always be present at the end. The `[Valore]` field contains the associated numeric data (ControlWord, status, etc.).

:::{card} GO TO THE DEDICATED PAGE
:link: tcp
:link-type: ref
:class-card: isw-card-tcp
:class-body: isw-card-body

Complete syntax of TCP Server messages, commands and terminators
:::
---

## Command Protocol

The command protocol defines all the actions available through the ControlWord. The ControlWords are **the same for all protocols**; only the transport changes (see [Fieldbus Transport](#sec-fieldbus) and [TCP Syntax](#sec-tcp)). Commands are grouped into categories:

<div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:1rem; margin:1.5rem 0 2.5rem;">

  <a href="#sec-exe" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-play-circle" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">EXE Commands</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Execution commands (start sequences, jog, reset)</span>
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
### Commands <span class="isw-section-badge isw-badge-exe"><i class="ph ph-play-circle"></i> EXE</span>

EXE commands start an immediate action on the FlexiBowl®. During execution **Busy** remains at `1`.

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
The **Reset Return Data** command (ControlWord 50) resets the value of ReturnData_1 and ReturnData_2, returning them to the initial state `0`. It is useful to verify that a new command is actually received and processed.
:::

#### Practical example 

To view a practical example of an EXE command over fieldbus, see the [Practical Example EXE](fieldbus_exe) section.
To view a practical example of an EXE command over TCP, see the [Practical Example EXE TCP](TCP_EXE) section.

(sec-write)=
### Commands <span class="isw-section-badge isw-badge-write"><i class="ph ph-pencil-simple"></i> WRITE</span>

WRITE commands allow the operating parameters of the FlexiBowl® (speed, angles, times, etc.) to be modified directly from the external system, without having to access the graphical interface.

#### Sequence addressing logic

Each sequence (from 1 to 20) has its own block of parameters. The ControlWord is calculated with the formula:

> **ControlWord = N × 100 + parameter_offset**

where `N` is the sequence number (1–20) and `offset_parametro` identifies the specific parameter.

#### Writable parameters for each sequence

| Parameter | Offset | Range Data_1 | Notes |
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
| SpeedShake | 09 | 1–100 | Speed of the shake (%) |
| FlipCount | 10 | 0–20 | Number of flips per cycle |
| FlipDelay | 11 | 0–500 | Pause between one flip and the next (ms) |
| BlowDelay | 12 | 0–500 | Pause between one blow pulse and the next (ms) |
| ProportionalValve_Flip | 13 | 0–600 | Flip proportional valve pressure (value /100 = Bar) |
| ProportionalValve_Blow | 14 | 0–600 | Blow proportional valve pressure (value /100 = Bar) |
| Delete all sequence | 30 | — | Deletes all commands from the sequence list |
| Emptying Sequence | 40 | 0–1 | 0 = normal mode, 1 = Quick Emptying mode |
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

#### Practical example 

To view a practical example of a WRITE command over fieldbus, see the [Practical Example WRITE](fieldbus_write) section.
To view a practical example of a WRITE command over TCP, see the [Practical Example WRITE TCP](TCP_write) section.

#### WRITE JOG parameters

The Jog parameters (continuous manual operation) are configurable separately via ControlWord in block 20000.

| Parameter | ControlWord | Range Data_1 | Notes |
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

---

(sec-read)=
### Commands <span class="isw-section-badge isw-badge-read"><i class="ph ph-eye"></i> READ</span>

READ commands allow the parameters currently configured in the FlexiBowl® to be read. The value read is returned in **ReturnData_2**.

#### READ addressing logic for sequences

The ControlWord for reading is calculated with the formula:

> **ControlWord = 10000 + N × 100 + parameter_offset**

where `N` is the sequence number (1–20) and `offset_parametro` is the same one used in the WRITE commands.

The readable parameters are the same as in the WRITE block, with the addition of the 10 command list slots:

| Additional parameter | Offset | Description |
|---|---|---|
| Seq Slot 1 Cmd | 50 | Command at position 1 in the sequence list |
| Seq Slot 2 Cmd | 51 | Command at position 2 |
| … | … | … |
| Seq Slot 10 Cmd | 59 | Command at position 10 |

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

#### Practical example 

To view a practical example of a READ command over fieldbus, see the [Practical Example READ](fieldbus_read) section.
To view a practical example of a READ command over TCP, see the [Practical Example READ TCP](TCP_read) section.

#### READ JOG parameters

The same writable JOG parameters (block 20000) can be read in block 20100:

| Parameter | READ ControlWord | Range ReturnData_2 |
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
## Commands <span class="isw-section-badge isw-badge-hop"><i class="ph ph-funnel"></i> HOPPER</span>

Hopper commands control the Bulk Feeders connected to the system (up to 4). They follow the same ControlWord/WRITE/READ logic described above, valid for all protocols, plus a dedicated TCP syntax for quick start.

### Hopper WRITE commands

| Parameter | ControlWord | Range Data_1 | Description |
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
| Hopper_1_Enable | 30017 | — | Enable hopper 1 (immediate action) |
| Hopper_1_Disable | 30018 | — | Disable hopper 1 (immediate action) |
| Hopper_2_Enable | 30019 | — | Enable hopper 2 |
| Hopper_2_Disable | 30020 | — | Disable hopper 2 |
| Hopper_3_Enable | 30021 | — | Enable hopper 3 |
| Hopper_3_Disable | 30022 | — | Disable hopper 3 |
| Hopper_4_Enable | 30023 | — | Enable hopper 4 |
| Hopper_4_Disable | 30024 | — | Disable hopper 4 |

:::{note}
In the training material, ControlWord `30005` (Hopper_2_Id) mistakenly reported the same range as Amplitude (50–220). In this table it has been corrected to **1–100**, consistent with Hopper_1_Id, Hopper_3_Id and Hopper_4_Id. Verify this value against the firmware/datasheet before publishing the page.
:::

#### Practical example

To view a practical example of a WRITE HOPPER command over fieldbus, see the [Practical Example WRITE HOPPER](fieldbus_WRITEHOPPER) section.
To view a practical example of a WRITE HOPPER command over TCP, see the [Practical Example WRITE HOPPER TCP](TCP_WRITEHOPPER) section.

### Hopper READ commands

| Parameter | READ ControlWord | Range ReturnData_2 | Notes |
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

#### Practical example 

To view a practical example of a READ HOPPER command over fieldbus, see the [Practical Example READ HOPPER](fieldbus_READHOPPER) section.
To view a practical example of a READ HOPPER command over TCP, see the [Practical Example READ HOPPER TCP](TCP_READHOPPER) section.

---

(sec-empty)=
## Quick Emptying commands — <span class="isw-section-badge isw-badge-exe"><i class="ph ph-arrow-counter-clockwise"></i> EMPTYING</span>

The **Emptying** function allows the FlexiBowl® plate to be emptied by running up to 4 dedicated sequences, each with its own number of loops. These commands also follow the same ControlWord logic, valid for all protocols.

### EXE Commands

| Command | ControlWord | Busy during execution | ReturnData_1 | Explanation |
|---|---|---|---|---|
| Start Emptying | 45 | YES (Emptying active) | 45 | Starts Quick Emptying  |
| Stop Emptying | 46 | YES (Emptying active) | 46 | Stops Quick Emptying  |
| Emptying Active | 47 | NO | 47 | Checks whether Quick Emptying is active |

### WRITE Commands

| Command | ControlWord | Range Data_1 | Busy during execution | ReturnData_1 |
|---|---|---|---|---|
| FirstSequence | 20200 | 1–20 | NO | 20200 |
| FirstLoop | 20201 | 0–500 | NO | 20201 |
| SecondSequence | 20202 | 1–20 | NO | 20202 |
| SecondLoop | 20203 | 0–500 | NO | 20203 |
| ThirdSequence | 20204 | 1–20 | NO | 20204 |
| ThirdLoop | 20205 | 0–500 | NO | 20205 |
| FourthSequence | 20206 | 1–20 | NO | 20206 |
| FourthLoop | 20207 | 0–500 | NO | 20207 |

### READ Commands

| Command | ControlWord | Busy during execution | ReturnData_1 | Range ReturnData_2 |
|---|---|---|---|---|
| FirstSequence | 20300 | NO | 20300 | 1–20 |
| FirstLoop | 20301 | NO | 20301 | 0–500 |
| SecondSequence | 20302 | NO | 20302 | 1–20 |
| SecondLoop | 20303 | NO | 20303 | 0–500 |
| ThirdSequence | 20304 | NO | 20304 | 1–20 |
| ThirdLoop | 20305 | NO | 20305 | 0–500 |
| FourthSequence | 20306 | NO | 20306 | 1–20 |
| FourthLoop | 20307 | NO | 20307 | 0–500 |

:::{note}
`FirstSequence`...`FourthSequence` indicate which of the 20 programmed sequences is executed in each of the 4 steps of the Quick Emptying; `FirstLoop`...`FourthLoop` indicate how many times that step is repeated.
:::

---

(sec-err)=
## Error Codes

:::{warning}
In the presence of an error, the **In_Error** LED turns on and the system will not execute new motion commands until the reset. Before performing the reset, identify and resolve the cause of the error.
:::


### General Codes

| ErrorCode | Description |
|---|---|
| 1 | The jog movement did not trigger any action on the motor |
| 2 | Motor not connected |
| 3 | EtherNet/IP selected but not connected |
| 4 | The motor did not reach operating power within the preset time |
| 5 | Motor movement requested, but the motor is not powered |
| 6 | Digital I/O module error: module missing |
| 7 | Digital I/O module error: configuration error |
| 8 | Digital I/O module error: general error |

### Driver Error Codes

<div class="isw-search-wrap">
  <input class="isw-search" id="errSearch" type="text" placeholder="Filter by code or description…" oninput="filterErrors()">
  <span class="isw-search-count" id="errCount"></span>
</div>

<div style="margin-top: 2rem;"></div>

<div class="isw-err-wrap">
<table class="isw-err-table" id="errTable">
<thead><tr><th>Code</th><th>Hex</th><th>Error</th><th>Description</th></tr></thead>
<tbody>
<tr><td><code>50</code></td><td><code>0x7500</code></td><td>EtherCAT communication error</td><td></td></tr>
<tr><td><code>51</code></td><td><code>0xFF01</code></td><td>Drive Over Current</td><td>Excessive motor current</td></tr>
<tr><td><code>52</code></td><td><code>0xFF02</code></td><td>Drive Over Voltage</td><td>Excessive DC bus voltage</td></tr>
<tr><td><code>53</code></td><td><code>0xFF03</code></td><td>Drive Over Temperature</td><td>Driver temperature too high</td></tr>
<tr><td><code>54</code></td><td><code>0xFF04</code></td><td>Reserved</td><td></td></tr>
<tr><td><code>55</code></td><td><code>0xFF05</code></td><td>Drive Internal Voltage Error</td><td>Internal voltage error</td></tr>
<tr><td><code>56</code></td><td><code>0xFF06</code></td><td>Position Error</td><td>Positioning error</td></tr>
<tr><td><code>57</code></td><td><code>0xFF07</code></td><td>Motor Encoder Disconnected</td><td>Encoder not connected or faulty</td></tr>
<tr><td><code>58</code></td><td><code>0xFF0A</code></td><td>Regen Failed</td><td>Error in the regeneration circuit</td></tr>
<tr><td><code>59</code></td><td><code>0xFF0B</code></td><td>Safe Torque Off (STO)</td><td>Safety function active</td></tr>
<tr><td><code>60</code></td><td><code>0xFF0C</code></td><td>Reserved</td><td></td></tr>
<tr><td><code>61</code></td><td><code>0xFF0D</code></td><td>Bad FPGA</td><td>Internal error of the driver FPGA</td></tr>
<tr><td><code>62</code></td><td><code>0xFF0E</code></td><td>Parameter Read Failed</td><td>Parameter read failed</td></tr>
<tr><td><code>63</code></td><td><code>0xFF0F</code></td><td>Motor Encoder Multi-turn Error</td><td>Multi-turn encoder error</td></tr>
<tr><td><code>64</code></td><td><code>0xFF10</code></td><td>Motor Stall Protection</td><td>Motor stall protection active</td></tr>
<tr><td><code>65</code></td><td><code>0xFF11</code></td><td>Drive Power Module Over Temperature</td><td>Power module overheated</td></tr>
<tr><td><code>66</code></td><td><code>0xFF31</code></td><td>N Limit</td><td>Negative position limit reached</td></tr>
<tr><td><code>67</code></td><td><code>0xFF32</code></td><td>P Limit</td><td>Positive position limit reached</td></tr>
<tr><td><code>68</code></td><td><code>0xFF33</code></td><td>N&P Limit</td><td>Both position limits reached</td></tr>
<tr><td><code>69</code></td><td><code>0xFF34</code></td><td>Current Foldback</td><td>Current reduction for thermal protection</td></tr>
<tr><td><code>70</code></td><td><code>0xFF35</code></td><td>Move @ Disabled</td><td>Attempted movement with the driver disabled</td></tr>
<tr><td><code>71</code></td><td><code>0xFF36</code></td><td>Drive Low Voltage</td><td>Insufficient DC bus voltage</td></tr>
<tr><td><code>72</code></td><td><code>0xFF37</code></td><td>Blank Q Segment</td><td>Undefined trajectory segment</td></tr>
<tr><td><code>73</code></td><td><code>0xFF38</code></td><td>Velocity Limit</td><td>Speed limit exceeded</td></tr>
<tr><td><code>74</code></td><td><code>0xFF39</code></td><td>Drive Power Phase Lost</td><td>Loss of a power supply phase</td></tr>
<tr><td><code>75</code></td><td><code>0xFF3A</code></td><td>Emergency Stop</td><td>Emergency stop active</td></tr>
<tr><td><code>76</code></td><td><code>0xFF3B</code></td><td>Abs. Encoder Battery</td><td>Absolute encoder battery low or missing</td></tr>
<tr><td><code>77</code></td><td><code>0xFF3C</code></td><td>Abs. Position Lost Warning</td><td>Absolute position loss warning</td></tr>
<tr><td><code>78</code></td><td><code>0xFF3D</code></td><td>Abs. Position Overflow</td><td>Absolute position overflow</td></tr>
<tr><td><code>79</code></td><td><code>0xFF3E</code></td><td>Motor Over Temperature</td><td>Excessive motor temperature</td></tr>
<tr><td><code>80</code></td><td><code>0xFF3F</code></td><td>Drive Voltage Warning</td><td>Driver voltage out of range warning</td></tr>
<tr><td><code>81</code></td><td><code>0xFF41</code></td><td>Save Failed</td><td>Parameter saving failed</td></tr>
<tr><td><code>82</code></td><td><code>0xFFFF</code></td><td>Other Error</td><td>Generic unclassified error</td></tr>
</tbody>
</table>
</div>

<script>
function filterErrors() {
  var input = document.getElementById('errSearch').value.toLowerCase();
  var rows = document.querySelectorAll('#errTable tbody tr');
  var count = 0;
  rows.forEach(function(row) {
    var text = row.textContent.toLowerCase();
    if (text.includes(input)) {
      row.classList.remove('isw-hidden');
      count++;
    } else {
      row.classList.add('isw-hidden');
    }
  });
  var countEl = document.getElementById('errCount');
  if (input) {
    countEl.textContent = count + ' ' + (count === 1 ? 'result' : 'results');
  } else {
    countEl.textContent = '';
  }
}
</script>

</div>


:::{toctree}
:hidden:
04a_interfaccia_software.md
04b_interfaccia_software.md
04c_interfaccia_software.md
:::