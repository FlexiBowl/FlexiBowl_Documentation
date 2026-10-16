# **Hopper Configuration**


This page guides you through the commissioning of the vibratory hopper, the optional accessory that feeds the FlexiBowl® continuously and uniformly. Follow the four phases in sequence: positioning and mechanical assembly, electrical connections, setting the communication address and configuring the parameters from the software interface.

<script src="https://unpkg.com/@phosphor-icons/web"></script>

<div class="quickstart-workflow">
  <style>
    .quickstart-workflow {
      font-family: inherit;
      max-width: 680px;
      margin: 2.5rem auto;
      padding: 0 1rem;
    }

    .qs-step {
      display: flex;
      align-items: stretch;
      gap: 1.25rem;
      margin-bottom: 0;
    }

    .qs-step:hover .qs-card {
      border-color: #2980b9;
      background: #f0f7ff;
      transform: translateX(4px);
    }

    .qs-step:hover .qs-number {
      background: #2980b9;
    }

    .qs-left {
      display: flex;
      flex-direction: column;
      align-items: center;
      flex-shrink: 0;
      width: 44px;
    }

    .qs-number {
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: #3498db;
      color: #fff;
      font-weight: 700;
      font-size: 1rem;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      transition: background 0.2s;
    }

    .qs-connector {
      flex: 1;
      width: 3px;
      background: linear-gradient(to bottom, #3498db 0%, #bcd6ec 100%);
      margin: 6px auto 0;
      min-height: 32px;
    }

    .qs-last .qs-connector {
      display: none;
    }

    .qs-card {
      flex: 1;
      border: 1.5px solid #d0e4f0;
      border-radius: 10px;
      padding: 0.85rem 1.1rem;
      background: #fff;
      transition: border-color 0.2s, background 0.2s, transform 0.2s;
      margin-bottom: 0.65rem;
    }

    .qs-card-title {
      font-weight: 700;
      font-size: 1rem;
      color: #1a3a52;
      margin-bottom: 0.3rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .qs-card-title i {
      font-size: 1.2rem;
      color: #1a3a52;
      flex-shrink: 0;
    }

    .qs-title-link {
      color: inherit;
      text-decoration: none;
    }

    .qs-title-link:hover {
      color: #2980b9;
      text-decoration: none;
    }

    .qs-card-desc {
      font-size: 0.875rem;
      color: #556b7d;
      margin: 0;
      line-height: 1.45;
    }
  </style>

  <!-- Step 1 -->
  <div class="qs-step">
    <div class="qs-left">
      <div class="qs-number">1</div>
      <div class="qs-connector"></div>
    </div>
    <div class="qs-card">
      <div class="qs-card-title">
        <i class="ph ph-package"></i>
        <a class="qs-title-link" href="conf_tramoggia.html#posizionamento-e-installazione-meccanica">Positioning and mechanical installation</a>
      </div>
      <p class="qs-card-desc">
        Position the hopper respecting the correct orientation relative to the FlexiBowl® and fix it to the support bracket.
      </p>
    </div>
  </div>

  <!-- Step 2 -->
  <div class="qs-step">
    <div class="qs-left">
      <div class="qs-number">2</div>
      <div class="qs-connector"></div>
    </div>
    <div class="qs-card">
      <div class="qs-card-title">
        <i class="ph ph-plugs"></i>
        <a class="qs-title-link" href="conf_tramoggia.html#collegamenti-elettrici">Electrical connections</a>
      </div>
      <p class="qs-card-desc">
        Connect the controller to the hopper, to the FlexiBowl® (or to the rack) and to the power supply, respecting the connection order.
      </p>
    </div>
  </div>

  <!-- Step 3 -->
  <div class="qs-step">
    <div class="qs-left">
      <div class="qs-number">3</div>
      <div class="qs-connector"></div>
    </div>
    <div class="qs-card">
      <div class="qs-card-title">
        <i class="ph ph-hash"></i>
        <a class="qs-title-link" href="conf_tramoggia.html#indirizzo-di-comunicazione-rs485">RS485 communication address</a>
      </div>
      <p class="qs-card-desc">
        Set a unique address from the controller panel, required to communicate with the FlexiBowl® and any other hoppers.
      </p>
    </div>
  </div>

  <!-- Step 4 -->
  <div class="qs-step">
    <div class="qs-left">
      <div class="qs-number">4</div>
      <div class="qs-connector"></div>
    </div>
    <div class="qs-card">
      <div class="qs-card-title">
        <i class="ph ph-hash"></i>
        <a class="qs-title-link" href="conf_tramoggia.html#configurazione-da-interfaccia-software">Configuration from the software interface</a>
      </div>
      <p class="qs-card-desc">
        Enable the hopper from the FlexiBowl® web interface and set the amplitude, frequency and activation time of the vibration.
      </p>
    </div>
  </div>
</div>

---

(posizionamento-e-installazione-meccanica)=
## 1. Positioning and mechanical installation

Vibratory hoppers are available in different sizes, each with its own maximum load:

| Capacity | Maximum load |
|---|---|
| 1.5 l | 1 kg |
| 3 l | 1.5 kg |
| 5 l | 6 kg |
| 10 l | 6 kg |
| 20 l | 6 kg |
| 40 l | 15 kg |

The hopper arrives already assembled: it does not need to be assembled, only positioned and fixed.

::::{tab-set}
:::{tab-item} Correct positioning
![Correct positioning of the hopper relative to the FlexiBowl®](../../../../_shared/media/images/posizione_giustatramoggia.png)

The hopper chute must discharge the components directly into the working area of the plate, with an inclination that follows the profile of the FlexiBowl®.
:::
:::{tab-item} Incorrect positioning
![Example of incorrect positioning of the hopper](../../../../_shared/media/images/posizione_sbagliatatramoggia.png)

A chute too far from the working area produces inconsistent feeding and penalizes the performance of the application.
:::
::::

**Steps:**

1. Place the hopper on a stable, horizontal surface, close to the FlexiBowl®, respecting the correct orientation shown above.
2. If the hopper is installed on the table of a machine that is sensitive to vibrations, place an insulating, anti-vibration material between the two surfaces, to prevent the vibrations of the hopper from being transmitted to the FlexiBowl®.
3. Fix the hopper to the support bracket through the dedicated holes, using M8 screws: the standard hopper has 4 holes at the base, while the smallest version (1.5 l) has 2.

(collegamenti-elettrici)=
## 2. Electrical connections

:::{warning}
Before making or changing any electrical connection, make sure the system is switched off. Always check that the earth conductor is correctly installed and intact: the electrical connection, including earthing, must always be guaranteed for the correct operation of the machine.
:::

![Diagram of the connectors on the hopper controller](../../../../_shared/media/images/tramoggia-schema-elettrico-controller.png)

The hopper controller has: mains power input (earth, line, neutral), RS485 connector for communication (A+, B-, GND), power output to the hopper motor and main switch.

**Steps:**

1. Connect the controller to the hopper using the dedicated cable.
2. Connect the controller to the FlexiBowl® through the M12 A-code connector (Modbus RTU communication). In multi-hopper installations with a rack, connect the controller to the rack instead.
3. Cap any unused connector with the appropriate cap, to protect it from dust and debris. The cap must provide a resistance of 120 Ω between the A+ and B- channels of the RS485 line.
4. Connect the power cable to the controller: always connect the controller side of the cable first, before connecting the other end.
5. With the controller switch in the OFF position, connect the power cable to the mains socket. The standard power supply is 115 or 230 VAC ±5% (the 115 V version is available only on explicit request).
6. Switch on the controller from the main switch.

:::{note}
A single FlexiBowl® supports up to **4 hoppers**. For multi-hopper installations, connect each hopper to its own controller, connect the first controller to the FlexiBowl® (or to the rack) and chain the following controllers through the hopper connector port (daisy-chain). Cap the unused port on the last controller in the chain and connect the power cable to each controller.
:::

(indirizzo-di-comunicazione-rs485)=
## 3. RS485 communication address

Each hopper controller must have a unique communication address on the RS485 network (parameter **r**, range 1–31). When there are several hoppers, make sure that each controller on the same network has a different address.

![Controller front panel: indicators, display and controls](../../../../_shared/media/images/tramoggia-pannello-controller.jpg)


**Steps from the controller panel:**

1. Hold **FUNC** for 2 seconds to enter the basic parameter adjustment state.
2. Press **FUNC** repeatedly to select parameter **r** (communication address).
3. Press **▲** or **▼** to change the value (1–31).
4. Hold **FUNC** again for 2 seconds to exit and save.

(configurazione-da-interfaccia-software)=
## 4. Configuration from the software interface

Once the connections are complete and the address has been set, the hopper can be configured and controlled from the dedicated page of the FlexiBowl® web interface.

![Hopper configuration software interface](../../../../_shared/media/images/tramoggia-interfaccia-software.png)

For each of the 4 available hoppers it is possible to set:

| Field | Description |
|---|---|
| **Enable** | Enables the corresponding hopper. |
| **ID** | RS485 address of the connected controller; use **Set New ID** to assign a new one via software. |
| **Status** | Current state of the hopper (e.g. Disabled). |
| **Amplitude** | Vibration amplitude. |
| **Frequency** | Vibration frequency. |
| **Activation Time** | Duration, in milliseconds, of each vibration pulse. |

**Steps:**

1. Access the FlexiBowl® web interface and open the hoppers page.
2. Select **Enable** on the hopper to be activated.
3. Check that the **ID** field matches the address set on the controller (step 3); if not, use **Set New ID**.
4. Set the initial values of **Amplitude**, **Frequency** and **Activation Time** according to the component to be fed.
5. Press **Start Hopper** to start the hopper and check its operation; adjust the parameters until the feeding of the components is continuous and uniform.

:::{note}
The optimal values of amplitude, frequency and activation time depend on the component and on the geometry of the hopper: adjust them progressively while observing the feeding flow, starting from low values and increasing until constant feeding without jams is achieved.
:::

<details>
<summary><strong>Advanced controller parameters</strong> (adjustable from the physical panel)</summary>

**Common parameters** — adjustable at any time with the **Vol+** / **Vol-** keys, even while another parameter is displayed:

![Common controller parameters](../../../../_shared/media/images/tramoggia-parametri-comuni.png)

| Definition | Symbol | Range | Default |
|---|---|---|---|
| Output voltage | U | 0–260 V | 50 |

**Basic parameters** — hold **FUNC** for 2 seconds to enter, press **FUNC** to scroll through the parameters, **▲/▼** to change them, hold **FUNC** for 2 seconds to exit:

![Basic controller parameters](../../../../_shared/media/images/tramoggia-parametri-base.png)

| Definition | Symbol | Range | Default |
|---|---|---|---|
| Output frequency | E | 40.0–200.0 Hz | 100.0 |
| Maximum adjustable output voltage | h | 0–260 V | 260 |
| Communication address | r | 1–31 | 1 |
| Communication baud rate | c | 0.3–115.2 kbps | 115.2 |
| Controller reset | — | — | — |

**Controller reset:**

![Controller reset procedure](../../../../_shared/media/images/tramoggia-reset-controller.png)

1. Hold **FUNC** for 2 seconds to enter the basic parameter adjustment state.
2. Press **FUNC** until the reset parameter (`88888`) flashes on the display.
3. Hold **▲** until `-----` appears on the display.
4. Release **▲** to complete the reset: the display will show `U 50`, confirming that the operation was successful.

</details>
