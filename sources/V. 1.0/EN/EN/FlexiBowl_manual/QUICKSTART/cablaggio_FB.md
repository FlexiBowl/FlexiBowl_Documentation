# **[ELE]** FlexiBowl® Wiring

<style>
.ars-dropdown {
  margin-top: 0.35rem;
}
.ars-dropdown summary {
  cursor: pointer;
  color: #2980b9;
  font-weight: 600;
  font-size: 0.82rem;
  padding: 0.35rem 0.7rem;
  border: 1px solid #d0e4f0;
  border-radius: 6px;
  display: inline-block;
  background: #f0f7ff;
  list-style: none;
  user-select: none;
}
.ars-dropdown summary::-webkit-details-marker { display: none; }
.ars-dropdown summary::before {
  content: "▸ ";
}
.ars-dropdown[open] summary::before {
  content: "▾ ";
}
.ars-dropdown[open] summary {
  border-radius: 6px 6px 0 0;
}
.ars-dropdown .ars-dropdown-body {
  border: 1px solid #d0e4f0;
  border-top: none;
  border-radius: 0 0 6px 6px;
  padding: 0.6rem;
  background: #fff;
}
.ars-dropdown img {
  display: block;
  max-width: 100%;
  width: 360px;
  border-radius: 4px;
}
.ars-step-warn, .ars-step-attn, .ars-step-note {
  border-radius: 5px;
  padding: 0.5rem 0.75rem;
  font-size: 0.83rem;
  margin-top: 0.55rem;
  line-height: 1.4;
}
.ars-step-warn { background:#fff3cd; border-left:4px solid #f0ad4e; color:#7a5b00; }
.ars-step-attn { background:#fee2e2; border-left:4px solid #dc2626; color:#8a1c1c; }
.ars-step-note { background:#eef6fc; border-left:4px solid #2980b9; color:#1a3a52; }
.ars-pin-table { width:100%; border-collapse:collapse; font-size:0.8rem; margin-top:0.4rem; }
.ars-pin-table th { background:#f0f4f8; padding:0.3rem 0.5rem; text-align:left; border:1px solid #d0e4f0; }
.ars-pin-table td { padding:0.3rem 0.5rem; border:1px solid #d0e4f0; }


.ars-zoom-img {
  transition: transform 0.35s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.35s ease;
  cursor: zoom-in;
  position: relative;
}
.ars-zoom-img:hover {
  transform: scale(1.8);
  box-shadow: 0 12px 40px rgba(0,0,0,0.22);
  z-index: 10;
}
</style>

:::::{important}

:::{raw} html
   <style>
     .ars-img-row { display: flex; gap: 12px; align-items: center; justify-content: center; }
     .ars-img-row img { width: 25%; }
   </style>
:::

::::{list-table}
:widths: 30 60
:header-rows: 1
* - {ref}`Operator qualification <operatori>`
  - {ref}`Required PPE <dpi>`

* - **Electrical maintenance technician**
  - :::{raw} html
       <div class="ars-img-row">
         <img src="../../../../_shared/media/images/guanti.png" alt="gloves">
         <img src="../../../../_shared/media/images/scarpe.png" alt="shoes">
         <img src="../../../../_shared/media/images/tuta.png" alt="overalls">
       </div>
    :::
::::
:::::

:::{warning}
Before making any electrical connection, make sure that the power supply is switched off and that the system is in a safe state. 
:::

The wiring of the FlexiBowl® changes depending on the machine size:

- **FlexiBowl® 500 – 1200**: all connections (STO, Ethernet, Hopper, power supply, air) are located on a single **standard electrical panel**, mounted directly on the machine.
- **FlexiBowl® 200 / 350**: the main connections are located on an external **rack**; the rack is then connected to the machine via 4 dedicated cables (Ethernet, Motor+STO, signal A, signal B). Only the compressed air remains to be connected on the machine.

---

## FlexiBowl® 500 – 1200 — Standard Electrical Panel

```{list-table}
:widths: 8 52 40
:header-rows: 1

* - #
  - Action
  - Image
* - 1
  - **Connect the STO.**

    <div class="ars-step-note">
    10-pin connector. The <strong>+STO1</strong> and <strong>+STO2</strong> inputs must receive <strong>+24 Vdc</strong> from the safety circuit; <strong>−STO1</strong> and <strong>−STO2</strong> must be connected to the −24 Vdc reference.
    </div>

    <details class="ars-dropdown"><summary>Pinout connettore 10 pin</summary><div class="ars-dropdown-body">

    | Pin | Description |
    |---|---|
    | 1 | +24 Vdc |
    | 2 | −24 Vdc |
    | 3 | +STO1 |
    | 4 | −STO1 |
    | 5 | +STO2 |
    | 6 | −STO2 |
    | 7–10 | NC |

    </div></details>
  - 
    ```{image} ../../../../_shared/media/images/connectSTO.png
    :alt: Connect the STO
    :class: ars-zoom-img
    ```

* - 2
  - **Collegare l'Ethernet (C-ETH).**

    <div class="ars-step-attn">
    When the FlexiBowl® is powered, the Ethernet connection is <strong>mandatory</strong>: if absent, the machine enters the <strong>ERROR</strong> state (red Ready/Fault LED).
    </div>

    <details class="ars-dropdown"><summary>Pinout M12 → RJ45</summary><div class="ars-dropdown-body">

    M12 8-pole → RJ45 adapter:

    | Pin | Color |
    |---|---|
    | 1 | Yellow |
    | 2 | Orange |
    | 3 | White |
    | 4 | Unassigned |
    | 5 | Unassigned |
    | 6 | Blue |
    | 7 | Unassigned |
    | 8 | Unassigned |

    M12 D-code 4-pole connector:

    | Pin | Color |
    |---|---|
    | 1 | Yellow |
    | 2 | White |
    | 3 | Orange |
    | 4 | Blue |

    </div></details>
  - 
    ```{image} ../../../../_shared/media/images/connectEthernet.png
    :alt: Connect the Ethernet
    :class: ars-zoom-img
    ```

* - 3
  - **Connect the Hopper.**

    <div class="ars-step-note">
    M12 A-code connector, used to communicate with the ARS hopper controllers via the <strong>Modbus RTU</strong> protocol.
    </div>

    <details class="ars-dropdown"><summary>Pinout M12 A-code</summary><div class="ars-dropdown-body">

    | Pin | Color |
    |---|---|
    | 1 | Brown |
    | 2 | White |
    | 3 | Blue |
    | 4 | Black |
    | 5 | Gray |

    </div></details>
  - 
    ```{image} ../../../../_shared/media/images/connectHopper.png
    :alt: Connect the Hopper
    :class: ars-zoom-img
    ```

* - 4
  - **Connect the power supply (Power Supply).**

    <div class="ars-step-attn">
    Make sure the FlexiBowl® is <strong>switched off</strong> before connecting the power supply.
    </div>

    <div class="ars-step-warn">
    Permitted voltage: <strong>120–230 Vac, 50/60 Hz</strong>.
    </div>

    <div class="ars-step-note">
    At first start-up, check the condition of the fuses. After switching on, wait for the status LED (Ready/Fault) to light up: if Hopper and C-ETH are connected correctly, the LED will be <strong>green</strong>.
    </div>

    <details class="ars-dropdown"><summary>Power cable pinout diagram</summary><div class="ars-dropdown-body">

    | Color | Type | Label |
    |---|---|---|
    | Brown | Fase | L1 |
    | Blue | Neutro | N1 |
    | Yellow/Green | Terra | PE1 |

    </div></details>
  - 
    ```{image} ../../../../_shared/media/images/connectSupply.png
    :alt: Connect the power supply
    :class: ars-zoom-img
    ```

* - 5
  - **Connect the compressed air** with a **Ø 8 mm** tube.

    :::{note}
    For the required air characteristics (pressure, ISO cleanliness class) refer to the [Pneumatic Technical Data](datipneum).
    :::
  - 
    ```{image} ../../../../_shared/media/images/connectAir.png
    :alt: Collegare l'aria compressa Ø8mm
    :class: ars-zoom-img
    ```
```
:::{video} ../../../../_shared/media/videos/cablaggio_FB800.mp4
:width: 100% 
:::

---

## FlexiBowl® 200 / 350 — External Rack

For these sizes, the connections to the customer's systems are located on the external **rack** (not on the machine). The rack is then connected to the machine via 4 dedicated cables.

### Connections on the rack

The rack connectors are the same as those of the standard panel (same pinout), simply placed on an external box instead of on the machine.

```{list-table}
:header-rows: 1

* - #
  - Action

* - 1
  - **Connect the STO** on the rack — same 10-pin connector as the standard panel (see pinout table above).

* - 2
  - **Connect the C-ETH IN** on the rack — same M12 D-code connector as the standard panel. The same rule applies: connection is mandatory, otherwise the machine goes into ERROR.

* - 3
  - **Connect the Hopper** on the rack — same M12 A-code connector (Modbus RTU) as the standard panel.

* - 4
  - **Connect the power supply** on the rack — 120–230 Vac.

    <div class="ars-step-attn">
    Make sure the FlexiBowl® is <strong>switched off</strong> before connecting the power supply.
    </div>
```

### Connection between Rack and FlexiBowl®

The rack communicates with the FlexiBowl® via 4 dedicated cables, each to be connected **only** to the port with the corresponding label on the panel.

:::{attention}
Connect each cable to the port with the **corresponding label** (e.g. MOTOR ↔ MOTOR, C-A SIGNAL ↔ C-A SIGNAL). A crossed connection can damage the system.
:::

```{list-table}
:widths: 8 52 40
:header-rows: 1

* - #
  - Action
  - Image
* - 5
  - **Connect the Ethernet cable (C-ETH FB)** between Rack and FlexiBowl® — M12 D-code connector.
  - 
    ```{image} ../../../../_shared/media/images/connectEthernet200.png
    :width: 110%
    :alt: Connect the C-ETH FB cable
    :class: ars-zoom-img
    ```
* - 6
  - **Connect the MOTOR cable.**

    <div class="ars-step-note">
    9-pole connector: carries both the motor power supply and the <strong>STO</strong> signals to the FlexiBowl® (on the rack, STO and Motor are separate connectors; on the cable to the machine they are combined in a single 9-pole connector).
    </div>
  - 
    ```{image} ../../../../_shared/media/images/connectMotor.png
    :width:110%
    :alt: Connect the Motor cable
    :class: ars-zoom-img
    ```
* - 7
  - **Connect the C-A SIGNAL cable** — 19-pole connector for analog signals.
  - 
    ```{image} ../../../../_shared/media/images/connectASignal.png
    :width:110%
    :alt: Connect the C-A Signal cable
    :class: ars-zoom-img
    ```
* - 8
  - **Connect the C-B SIGNAL cable** — 19-pole connector for digital signals.
  - 
    ```{image} ../../../../_shared/media/images/connectBSignal.png
    :width:110%
    :alt: Connect the C-B Signal cable
    :class: ars-zoom-img
    ```
* - 9
  - **Connect the compressed air** with a **Ø 6 mm** tube, directly on the machine panel.

    :::{note}
    For the required air characteristics (pressure, ISO cleanliness class) refer to the [Pneumatic Technical Data](datipneum).
    :::
  - 
    ```{image} ../../../../_shared/media/images/connectAir200.png
    :width:110%
    :alt: Collegare l'aria compressa Ø6mm
    :class: ars-zoom-img
    ```
```
:::{video} ../../../../_shared/media/videos/cablaggio_FB200.mp4
:width: 100% 
:::