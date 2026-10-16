# [SOF] **Home**

## Overview

The **Home** page is the main screen of the FlexiBowl® software interface. It is displayed at system start-up and gives the operator an immediate overview of the device status, as well as providing access to the main functions.
![home page](../../../../_shared/media/images/home.png)

| Element | Position | Description |
|---|---|---|
| **Menu** (☰) | Top left | Opens the main side navigation menu, which gives access to all the sections of the software (parameters, diagnostics, history, settings, etc.) |
| **Status icon** (READY ✓) | Center-left | Indicates the current operating state of the system. The green icon with the check mark and the word **READY** signals that the system is ready for operation |
| **User icon** | Center-right | Allows the active user profile to be managed (login, logout, change user) |
| **ENABLE MOTOR button** | Top right | Enables the FlexiBowl® motor. |
| **Language selector** | Below ENABLE MOTOR | Drop-down menu to select the interface language. It shows the flag of the active language (e.g. 🇺🇸 English) |

---

## Menu

<style>
.home-menu-wrap {
  display: flex;
  gap: 1.5rem;
  align-items: flex-start;
  margin: 1rem 0 1.5rem;
  flex-wrap: wrap;
}
.home-menu-img {
  flex: 0 0 auto;
  width: 200px;
  border: 1px solid #e2eef6;
  border-radius: 10px;
  overflow: hidden;
}
.home-menu-img img { display: block; width: 100%; }
.home-menu-cards {
  flex: 1 1 420px;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0.75rem;
}
@media (max-width: 560px) {
  .home-menu-cards { grid-template-columns: 1fr; }
}
.home-menu-card {
  display: block;
  padding: 0.7rem 0.9rem;
  border: 1.5px solid #d0e4f0;
  border-radius: 8px;
  background: #fff;
  text-decoration: none;
  color: inherit;
  transition: border-color 0.18s, background 0.18s;
}
.home-menu-card:hover {
  border-color: #2980b9;
  background: #f0f7ff;
  text-decoration: none;
}
.home-menu-card-title {
  font-weight: 700;
  font-size: 0.88rem;
  color: #1a3a52;
}
.home-menu-card-sub {
  font-size: 0.78rem;
  color: #556b7d;
  margin-top: 0.2rem;
  line-height: 1.35;
}
</style>

The side menu, which can be opened with the ☰ icon, gives access to all the pages of the interface:

<div class="home-menu-wrap">
<div class="home-menu-img">

```{image} ../../../../_shared/media/images/menu_laterale.png
:alt: Side navigation menu
```

</div>
<div class="home-menu-cards">

<a class="home-menu-card" href="04_home.html">
<div class="home-menu-card-title">Home</div>
<div class="home-menu-card-sub">Main screen with system status and quick access to the functions</div>
</a>

<a class="home-menu-card" href="04b_maincommand.html">
<div class="home-menu-card-title">Main Command</div>
<div class="home-menu-card-sub">Configures the general options of the unit and the Move and Shake movements (Option, Move, Shake tabs)</div>
</a>

<a class="home-menu-card" href="04c_sequence.html">
<div class="home-menu-card-title">Sequence</div>
<div class="home-menu-card-sub">Creates and edits the feeding sequences directly from the interface</div>
</a>

<a class="home-menu-card" href="04d_monitor.html">
<div class="home-menu-card-title">Monitor</div>
<div class="home-menu-card-sub">Real-time view of the FlexiBowl® status, with a time-stamped event log</div>
</a>

<a class="home-menu-card" href="04e_jogmotor.html">
<div class="home-menu-card-title">Jog Motor</div>
<div class="home-menu-card-sub">Manual movement of the motor, useful during setup, testing or troubleshooting</div>
</a>

<a class="home-menu-card" href="04f_wizard.html">
<div class="home-menu-card-title">Wizard Param</div>
<div class="home-menu-card-sub">Step-by-step guided procedure for configuring the FlexiBowl®</div>
</a>

<a class="home-menu-card" href="manual.html">
<div class="home-menu-card-title">Manual</div>
<div class="home-menu-card-sub">Allows the device documentation to be consulted directly from the interface</div>
</a>

<a class="home-menu-card" href="04h_graphs.html">
<div class="home-menu-card-title">Graphs</div>
<div class="home-menu-card-sub">Dashboard with real-time graphs of the electrical and thermal quantities of the motor driver</div>
</a>

<a class="home-menu-card" href="04i_filetransfer.html">
<div class="home-menu-card-title">File Transfer</div>
<div class="home-menu-card-sub">Transfer of parameters and recipes to and from the unit's backup</div>
</a>

<a class="home-menu-card" href="04l_setup.html">
<div class="home-menu-card-title">Setup</div>
<div class="home-menu-card-sub">Network configuration, selection of the communication protocol and other system settings</div>
</a>

<a class="home-menu-card" href="04m_hopper.html">
<div class="home-menu-card-title">Hopper</div>
<div class="home-menu-card-sub">Configuration and control of the connected hoppers (ID, amplitude, frequency, activation time)</div>
</a>

<a class="home-menu-card" href="04n_emptying.html">
<div class="home-menu-card-title">Emptying</div>
<div class="home-menu-card-sub">Automatic emptying of the plate by chaining up to 4 sequences with configurable loops</div>
</a>

</div>
</div>



---
## Operating notes

:::{attention}   
Before enabling the motor, check that the system status is **READY** (green icon visible in the top bar). If the icon is not green, check the error messages in the diagnostics sections.
:::

:::{note}  
The language selected from the Home page is applied to the entire software interface. The change is immediate and does not require restarting the system.
:::
