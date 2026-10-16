# **[ELE]** Controller and Wiring

During operation, the machine does not require the continuous presence of an operator.

:::{attention}
Using the machine for a purpose other than that intended by the Manufacturer could cause serious damage to persons and/or property and/or animals.
ARS S.r.l. is not liable for damage caused by improper use of the machine.
:::

## Controller Description

The **Digital controller** (mod. SDVC34-XLRH) is a variable-frequency controller equipped with a microprocessor, **LED** display and control keypad (**Vol+/Vol-** buttons for the output voltage, **▲/▼** buttons for the parameters, **FUNC** key for selection, **ON/OFF** key for switching on/off and keypad lock).

By **default the controller does not generate any output at power-on** and remains in the stop state: to enable the main output, a **PNP signal** must be applied to the **Enable Output Port** (4-pin connector).

The controller integrates automatic protections:

- **Short circuit** → immediate output shutdown, error `Err01`
- **Overcurrent** → immediate output shutdown, error `Err02`
- **Overtemperature** → output shutdown above 65 °C, automatic restoration below 60 °C, error `Err03`

Communication takes place via the **RS485** port (**Modbus** protocol), with a network address that can be set from 1 to 31 and a configurable baud rate.


### Controller Technical Data

| Technical characteristic | Min | Typical | Max | Unit | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Input voltage** | 85 | 220 | 250 | V | AC RMS |
| **Adjustable output voltage range** | 0 | — | 260 | V | Below 150% of the input voltage |
| **Voltage adjustment accuracy** | — | 1 | — | V | — |
| **Voltage adjustment accuracy (ΔVout/ΔVin)** | 0 | — | 10 | % | ΔVout/ΔVin |
| **Adjustable output current range** | 0 | — | 6 | A | — |
| **Output power** | 0 | — | 1320 | VA | — |
| **Output frequency** | 30.0 | — | 130.0 | Hz | — |
| **Frequency adjustment accuracy** | — | 0.1 | — | Hz | — |
| **Output waveform** | — | Sinusoidal | — | — | — |
| **Overtemperature protection trip temperature** | 60 | 65 | 65 | °C | — |
| **Digital communication** | — | ModBus 485 | — | — | — |
| **Adjustment method** | — | 6 | — | Button | — |
| **Standby consumption** | — | 7 | — | W | — |
| **Display method** | — | 5 | — | Digit | LED |
| **Ambient temperature** | 0 | 25 | 40 | °C | Non-condensing |
| **Ambient humidity** | 10 | 60 | 85 | % | Non-condensing |
| **Storage ambient temperature** | -20 | 25 | 65 | °C | Non-condensing |

:::{attention}
Controllers other than the one supplied by the Manufacturer can be integrated, provided the Manufacturer has previously validated their technical characteristics. ARS s.r.l. is not liable for damage caused by the use of a controller that has not been validated or is not compatible with the machine.
:::

#### Front panel controls

```{image} ../../../../../_shared/media/images/controller_digitale_pannello.jpeg
:alt: Front panel of the CUH SDVC34-XLRH digital controller
:width: 90%
:align: center
```

| Element | Function |
|---|---|
| **LED display** | Shows the current parameter and its value |
| **Saturated indicator** | Signals saturation of the output signal |
| **Remote indicator** | Signals that remote control is active |
| **Speed A / Speed B indicators** | Signal the active speed/output |
| **Stop indicator** | Signals the stopped state |
| **Vol+ / Vol- buttons** | Adjust the **Common Parameters** (see below), at any time |
| **FUNC button** | Entry/exit and navigation between the **Basic Parameters** |
| **▲ / ▼ buttons** | Increase/decrease the value of the selected parameter |
| **Auto / Sync / Sensor / Sync Signal / Communicate indicators** | Operating and RS485 communication status |
| **ON/OFF button** | Switching the controller on/off |

#### Rear connectors

```{image} ../../../../../_shared/media/images/controller_digitale_connettori.png
:alt: Rear connector panel of the digital controller
:width: 85%
:align: center
```

```{list-table}
:widths: 30 45 25
:header-rows: 1

* - Connector
  - Function
  - Pinout
* - **Mains Power** (power supply)
  - Mains power supply
  - <details class="ars-dropdown"><summary>Connector pinout</summary><div class="ars-dropdown-body">

    | Pin | Description |
    |---|---|
    | PE-PE | ⏚ Ground |
    | 1 | L |
    | 2 | N |
    | 3 | NC |

    </div></details>
* - **Enable Output Port** (4 pin)
  - Enable output for external control of the hopper, used when the hopper is purchased separately and must be driven by an external device
  - <details class="ars-dropdown"><summary>4-pin connector pinout</summary><div class="ars-dropdown-body">

    | Pin | Description |
    |---|---|
    | 1 | +24V |
    | 2 | NC |
    | 3 | GND |
    | 4 | Input |

    </div></details>
* - **RS485 Port** (2× 5 pin)
  - Two identical RS485 connectors: one connects the controller to the FlexiBowl®, the other allows **daisy chain** connection between several hoppers. 
    
    :::{important}
    In a single-hopper configuration, the unused connector must be closed with the dedicated **termination plug** supplied, fitted with a **120 Ω** resistor between A+ and B-
    :::
  
  - <details class="ars-dropdown"><summary>5-pin connector pinout</summary><div class="ars-dropdown-body">

    | Pin | Description |
    |---|---|
    | 1 | A+ |
    | 2 | NC |
    | 3 | B- |
    | 4 | GND |
    | 5 | NC |

    </div></details>
* - **Power Output to Feeder** (output to the hopper)
  - Power supply to the hopper
  - <details class="ars-dropdown"><summary>Connector pinout</summary><div class="ars-dropdown-body">

    | Pin | Description |
    |---|---|
    | PE-PE | ⏚ Ground |
    | 1 | Output |
    | 2 | Output |
    | 3 | NC |

    </div></details>
* - **Power Switch**
  - On/off switch
  - —
```

## Operating procedures

### Preliminary checks

Before starting up the machine, carry out the following checks:

<div class="isw-symbol-grid">
  <div class="isw-symbol-item">
    <div>
      <div class="isw-symbol-label">Stability</div>
      <div class="isw-symbol-desc">Check that the machine is placed on a surface able to support its weight.</div>
    </div>
  </div>
  <div class="isw-symbol-item">
    <div>
       <div class="isw-symbol-label">Safety</div>
      <div class="isw-symbol-desc">Check the operation of the safety devices and make sure that all openable guards are firmly closed.</div>
    </div>
  </div>
  <div class="isw-symbol-item">
    <div>
      <div class="isw-symbol-label">Operating Space</div>
      <div class="isw-symbol-desc"> Check that the space around the machine is free of obstructions and/or tripping hazards.</div>
    </div>
  </div>
  <div class="isw-symbol-item">
    <div>
     <div class="isw-symbol-label">Power Supply</div>
      <div class="isw-symbol-desc">Check that the machine has been connected to the electrical mains and that the supply phases are correct.</div>
    </div>
  </div>
  <div class="isw-symbol-item">
    <div>
       <div class="isw-symbol-label">Mechanics</div>
      <div class="isw-symbol-desc">Check that the bowl is completely free to vibrate.</div>
    </div>
  </div>
  <div class="isw-symbol-item">
    <div>
      <div class="isw-symbol-label">Machine Status</div>
      <div class="isw-symbol-desc">Check that the machine is not in "Maintenance" state.</div>
    </div>
  </div>
</div>

### Electrical connection sequence

Regardless of the type of controller used (standard, analog or digital), the electrical connection between hopper, controller and FlexiBowl® follows a precise sequence. The sequence differs slightly depending on the model: the **FlexiBowl® 500/650/8 00/1200** have a standard panel with an integrated HOPPER connector, while the **FlexiBowl® 200/350** use an external rack with its own HOPPER connector.

#### FlexiBowl® 500 / 600 / 900 / 1200 — standard panel

<div style="display: flex; flex-direction: column; gap: 12px; margin: 20px 0;">
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #0f766e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">1</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Connect the <strong>Controller</strong> to the <strong>hopper</strong> (vibrating base).
    </div>
    <img src="../../../../../_shared/media/images/connect_Hopper.png" alt="Connecting the Hopper Controller to the hopper" style="display:block; width:100%; max-width:500px; margin-top:10px; border-radius:4px;" />
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #0f766e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">2</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Connect the <strong>Controller</strong> to the <strong>HOPPER</strong> connector on the standard panel of the FlexiBowl®.
    </div>
    <img src="../../../../../_shared/media/images/connect_FB.png" alt="Connecting the Hopper Controller to the hopper" style="display:block; width:100%; max-width:500px; margin-top:10px; border-radius:4px;" />
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #0f766e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">3</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      If the Hopper connector of the FlexiBowl® is not used, fit the dedicated <strong>termination cap</strong>*.
    </div>
    <img src="../../../../../_shared/media/images/cover_cap.png" alt="Connecting the Hopper Controller to the hopper" style="display:block; width:100%; max-width:500px; margin-top:10px; border-radius:4px;" />
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #0f766e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">4</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Connect the <strong>power</strong> cable to the Controller, checking that the power switch is in the <strong>OFF</strong> position.
    </div>
    <img src="../../../../../_shared/media/images/connect_Supply.png" alt="Connecting the Hopper Controller to the hopper" style="display:block; width:100%; max-width:500px; margin-top:10px; border-radius:4px;" />
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #0f766e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">5</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Connect the plug of the power cable to the <strong>power outlet</strong>, only after confirming that the controller switch is OFF.
    </div>
  </div>
</div>

:::{attention}
*The cap must ensure a resistance of **120 Ω** between channels A+ and B-.
:::

:::{important}
Always connect the **controller side** of the power cable **first**, and only then insert the plug into the power outlet.
:::

```{image} ../../../../../_shared/media/images/controller_side.png
:alt: Always connect the controller side first
:width: 70%
:align: center
```

```{image} ../../../../../_shared/media/images/power_outlet.png
:alt: Connecting the plug to the power outlet
:width: 70%
:align: center
```

#### **Cascade connection of several hoppers**

On models with a standard panel, several Hopper Controller units can be connected in cascade, powering each controller individually and connecting the connectors from one unit to the next.

```{image} ../../../../../_shared/media/images/daisy_chain.png
:alt: Cascade connection of several Hopper Controllers
:width: 100%
:align: center
```

#### FlexiBowl® 200 / 350 — rack panel

<div style="display: flex; flex-direction: column; gap: 12px; margin: 20px 0;">
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #0f766e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">1</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Connect the <strong>Controller</strong> to the <strong>hopper</strong> (vibrating base).
    </div>
    <img src="../../../../../_shared/media/images/connect_Hopper.png" alt="Connecting the Hopper Controller to the hopper" style="display:block; width:100%; max-width:500px; margin-top:10px; border-radius:4px;" />
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #0f766e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">2</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Connect the <strong>Controller</strong> to the <strong>HOPPER</strong> connector on the <strong>rack</strong> panel.
    </div>
    <img src="../../../../../_shared/media/images/controller_Rack.png" alt="Connecting the Hopper Controller to the hopper" style="display:block; width:100%; max-width:500px; margin-top:10px; border-radius:4px;" />
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #0f766e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">3</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      If the Hopper connector of the rack is not used, fit the dedicated <strong>termination cap</strong>*.
    </div>
    <img src="../../../../../_shared/media/images/cover_cap.png" alt="Connecting the Hopper Controller to the hopper" style="display:block; width:100%; max-width:500px; margin-top:10px; border-radius:4px;" />
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #0f766e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">4</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Connect the <strong>power</strong> cable to the Controller, checking that the power switch is in the <strong>OFF</strong> position.
    </div>
    <img src="../../../../../_shared/media/images/connect_Supply.png" alt="Connecting the Hopper Controller to the hopper" style="display:block; width:100%; max-width:500px; margin-top:10px; border-radius:4px;" />
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #0f766e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">5</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Connect the plug of the power cable to the <strong>power outlet</strong>, only after confirming that the controller switch is OFF.
    </div>
  </div>
</div>

:::{attention}
*The cap must ensure a resistance of **120 Ω** between channels A+ and B-.
:::

:::{important}
Always connect the **controller side** of the power cable **first**, and only then insert the plug into the power outlet.
:::

```{image} ../../../../../_shared/media/images/controller_side.png
:alt: Always connect the controller side first
:width: 70%
:align: center
```

```{image} ../../../../../_shared/media/images/power_outlet.png
:alt: Connecting the plug to the power outlet
:width: 70%
:align: center
```

:::{note}
Standard controller power supply: **115 Vac** or **230 Vac ±5%**. Always check that the earth conductor is correctly installed and intact before powering the system.
:::

---

#### Setting the communication address

Once the electrical wiring is complete, the next step is to set a **unique communication address** on each controller, via the **Communication Address** parameter (`r`).

:::{note}
The `r` parameter represents the **controller ID** on the **RS485** communication network. When several controllers are connected on the same network (e.g. several hoppers), it is **mandatory** to assign each one a different address, in the range **1–31**, so that they can be distinguished and controlled individually.
:::

<div style="display: flex; flex-direction: column; gap: 12px; margin: 20px 0;">
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #7c3aed; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">1</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Hold <strong>FUNC</strong> for 2 seconds to enter the Basic Parameters adjustment mode.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #7c3aed; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">2</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Press <strong>FUNC</strong> repeatedly to scroll to the <code>r</code> parameter.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #7c3aed; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">3</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Press <strong>▲</strong> or <strong>▼</strong> to change the value (1–31).
    </div>
  </div>
</div>

---

#### Hopper Software Interface

Once the unique address has been assigned to each controller, the hoppers are **integrated into the FlexiBowl® software** and can be controlled directly from its interface, without having to operate the individual controllers manually.

```{image} ../../../../../_shared/media/images/hopper.png
:alt: FlexiBowl software interface — hopper management (Hopper 1–4)
:width: 100%
:align: center
```

From the software interface, for each connected hopper, it is possible to:

| Field | Function |
|---|---|
| **ID** | Communication address of the controller (must match the one set manually) |
| **ENABLE** | Enables the hopper for operation |
| **Set New ID** | Assigns a new communication address from the software |
| **STATUS** | Current status of the hopper (e.g. Disabled) |
| **Amplitude** | Vibration amplitude |
| **Frequency** | Vibration frequency |
| **Activation Time** | Hopper activation time (ms) |
| **Start Hopper** | Manually starts the hopper |

:::{note}
All the adjustments available via the software interface can also be made **directly from the controller**, via the Common and Basic Parameters described below.
:::

---
#### Common Parameters

The **Common Parameters** can be adjusted at any time via the **Vol+ / Vol-** buttons, even while another parameter is shown on the display: at the end of the adjustment, the controller automatically returns to displaying the previous parameter.

```{image} ../../../../../_shared/media/images/controller_changing_common_parameters.png
:alt: Digital controller — adjusting Common Parameters with Vol+/Vol-
:width: 50%
:align: center
```

| Definition | Symbol | Range | Default |
|---|---|---|---|
| Output Voltage | `U` | 0–260 (V) | 50 |

#### Basic Parameters

<div style="display: flex; flex-direction: column; gap: 12px; margin: 20px 0;">
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #34495e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">1</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Hold <strong>FUNC</strong> for 2 seconds to enter the Basic Parameters adjustment mode.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #34495e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">2</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Press <strong>FUNC</strong> repeatedly to cycle through the different parameters.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #34495e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">3</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Press <strong>▲</strong> or <strong>▼</strong> to change the value of the parameter.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #34495e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">4</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Hold <strong>FUNC</strong> again for 2 seconds to exit the Basic Parameters adjustment mode.
      <img src="../../../../../_shared/media/images/controller_changing_basic_parameters.png" alt="Digital controller — Basic Parameters adjustment procedure" style="display:block; width:60%; max-width:500px; margin-top:10px; border-radius:4px;" />
    </div>
  </div>
</div>

| Definition | Symbol | Range | Default |
|---|---|---|---|
| Output Frequency | `E` | 40.0–200.0 (Hz) | 100.0 |
| Max Adjustable Output Voltage | `h` | 0–260 (V) | 260 |
| Communication Address (RS485 address) | `r` | 1–31 | 1 |
| Communication Baud Rate | `c` | 0.3–115.2 kbps | 115.2 |
| Controller Reset | `88888` | — | — |

#### Controller Reset procedure

<div style="display: flex; flex-direction: column; gap: 12px; margin: 20px 0;">
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #7c3aed; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">1</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Hold <strong>FUNC</strong> for 2 seconds to enter the Basic Parameters adjustment mode.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #7c3aed; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">2</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Press <strong>FUNC</strong> until the flashing <code>88888</code> parameter is shown on the display.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #7c3aed; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">3</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Hold <strong>▲</strong> until the display shows <code>-----</code> ("Ready to restore").
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #7c3aed; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">4</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Release <strong>▲</strong> to complete the reset ("Restore successfully"): the display shows <code>U 50</code> to confirm that the restoration has been completed.
      <img src="../../../../../_shared/media/images/controller_reset_procedure.png" alt="Digital controller — reset sequence, from Ready to restore to Restore successfully" style="display:block; width:100%; max-width:700px; margin-top:10px; border-radius:4px;" />
    </div>
  </div>
</div>

:::{warning}
The **Controller Reset** returns all Common and Basic Parameters to their default values (Output Voltage 50, Output Frequency 100.0 Hz, Max Output Voltage 260, Communication Address 1, Baud Rate 115.2 kbps). Use it with caution if custom configurations are present — in particular the communication address, which will need to be set again.
:::


---

## **Commissioning the hopper**

:::{important}
- If the system includes **FlexiVision One**, the configuration of the hopper parameters is guided in the [Hopper Configuration]() section.
- Otherwise, refer to the [Hopper](hopper) section of this manual.
:::

