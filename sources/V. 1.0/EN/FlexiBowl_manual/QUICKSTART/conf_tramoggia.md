# **Bulk Feeder Configuration**


This page guides you through commissioning the vibrating Bulk Feeder, the optional accessory that feeds the FlexiBowl® continuously and uniformly. Follow the four phases in sequence: mechanical positioning and mounting, electrical connections, setting the communication address, and configuring the parameters from the software interface.

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
        Position the Bulk Feeder with the correct orientation relative to the FlexiBowl® and secure it to the support bracket.
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
        Connect the controller to the Bulk Feeder, to the FlexiBowl® (or to the rack) and to the power supply, following the connection order.
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
        From the controller panel, set a unique address, required to communicate with the FlexiBowl® and any other Bulk Feeders.
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
        Enable the Bulk Feeder from the FlexiBowl® web interface and set the amplitude, frequency and activation time of the vibration.
      </p>
    </div>
  </div>
</div>

---

## 1. Positioning and mechanical installation

Bulk Feeders are available in different sizes, each with its own maximum load:

| Capacity | Maximum load |
|---|---|
| 1.5 l | 1 kg |
| 3 l | 1.5 kg |
| 5 l | 6 kg |
| 10 l | 6 kg |
| 20 l | 6 kg |
| 40 l | 15 kg |

The Bulk Feeder arrives already assembled: it does not need to be assembled, only positioned and secured.

::::{tab-set}
:::{tab-item} Correct positioning
![Correct positioning of the Bulk Feeder relative to the FlexiBowl®](../../../../_shared/media/images/posizione_giustatramoggia.png)

The Bulk Feeder chute must discharge the components directly into the working area of the plate, with an inclination that follows the profile of the FlexiBowl®.
:::
:::{tab-item} Incorrect positioning
![Example of incorrect positioning of the Bulk Feeder](../../../../_shared/media/images/posizione_sbagliatatramoggia.png)

A chute that is too far from the work area results in inconsistent feeding and penalizes the performance of the application.
:::
::::

**Steps:**

1. Place the Bulk Feeder on a stable, horizontal surface, close to the FlexiBowl®, observing the correct orientation shown above.
2. If the Bulk Feeder is installed on the surface of a machine sensitive to vibrations, place an insulating, anti-vibration material between the two surfaces, to prevent the Bulk Feeder's vibrations from being transmitted to the FlexiBowl®.
3. Secure the Bulk Feeder to the support bracket using the dedicated holes, with M8 screws: the standard Bulk Feeder has 4 holes in the base, while the smaller version (1.5 l) has 2.

## 2. Electrical connections

:::{warning}
Before making or changing any electrical connection, make sure the system is switched off. Always check that the earth conductor is correctly installed and intact: the electrical connection, including the earthing, must always be ensured for the machine to operate correctly.
:::

![Diagram of the connectors on the Bulk Feeder controller](../../../../_shared/media/images/controller_digitale_connettori.png)

The Bulk Feeder controller has: a mains power input (earth, line, neutral), an RS485 connector for communication (A+, B-, GND), a power output to the Bulk Feeder motor and a main switch.

**Steps:**

1. Connect the controller to the Bulk Feeder using the dedicated cable.
2. Connect the controller to the FlexiBowl® using the M12 A-code connector (Modbus RTU communication). In multi-feeder installations with a rack, connect the controller to the rack instead.
3. Plug any unused connector with the appropriate cap, to protect it from dust and debris. The cap must provide a resistance of 120 Ω between the A+ and B- channels of the RS485 line.
4. Connect the power cable to the controller: always connect the controller end of the cable first, before connecting the other end.
5. With the controller switch in the OFF position, connect the power cable to the mains socket. The standard supply is 115 or 230 VAC ±5% (the 115 V version is available only on explicit request).
6. Switch the controller on using the main switch.

:::{tip}
The Modbus RTU cable between the controller and the FlexiBowl® is available in lengths of 3, 5 and 10 m: see {ref}`cavo-modbus`.
:::

:::{note}
A single FlexiBowl® supports up to **4 Bulk Feeders**. For multi-feeder installations, connect each Bulk Feeder to its own controller, connect the first controller to the FlexiBowl® (or to the rack) and chain the following controllers through the Bulk Feeder connector port (daisy-chain). Plug the unused port on the last controller in the chain and connect the power cable to each controller.
:::

## 3. RS485 communication address

Each Bulk Feeder controller must have a unique communication address on the RS485 network (parameter **r**, range 1–31). When there are several Bulk Feeders, make sure every controller on the same network has a different address.

![Controller front panel: indicators, display and controls](../../../../_shared/media/images/tramoggia-pannello-controller.jpg)


**Steps from the controller panel:**

1. Hold **FUNC** for 2 seconds to enter the basic parameter adjustment state.
2. Press **FUNC** repeatedly to select parameter **r** (communication address).
3. Press **▲** or **▼** to change the value (1–31).
4. Hold **FUNC** again for 2 seconds to exit and save.

## 4. Configuration from the software interface

Once the connections are complete and the address is set, the Bulk Feeder can be configured and controlled from the dedicated page of the FlexiBowl® web interface.

![Bulk Feeder configuration software interface](../../../../_shared/media/images/tramoggia-interfaccia-software.png)

For each of the 4 available Bulk Feeders you can set:

| Field | Description |
|---|---|
| **Enable** | Enables the corresponding Bulk Feeder. |
| **ID** | RS485 address of the connected controller; use **Set New ID** to assign a new one via software. |
| **Status** | Current status of the Bulk Feeder (e.g. Disabled). |
| **Amplitude** | Amplitude of the vibration. |
| **Frequency** | Frequency of the vibration. |
| **Activation Time** | Duration, in milliseconds, of each vibration pulse. |

**Steps:**

1. Access the FlexiBowl® web interface and open the Bulk Feeder page.
2. Select **Enable** on the Bulk Feeder to be activated.
3. Check that the **ID** field matches the address set on the controller (step 3); if not, use **Set New ID**.
4. Set the initial values of **Amplitude**, **Frequency** and **Activation Time** according to the component to be fed.
5. Press **Start Hopper** to start the Bulk Feeder and check that it works; adjust the parameters until the component feed is continuous and uniform.

:::{note}
The optimal values of amplitude, frequency and activation time depend on the component and on the geometry of the Bulk Feeder: adjust them gradually while observing the feed flow, starting from low values and increasing until a steady feed without jams is obtained.
:::

## Advanced controller parameters 

### **Common parameters** 
The common parameters can be adjusted at any time with the **Vol+** / **Vol-** keys, even while another parameter is displayed:

![Common controller parameters](../../../../_shared/media/images/tramoggia-parametri-comuni.png)

| Definition | Symbol | Range | Default |
|---|---|---|---|
| Output voltage | U | 0–260 V | 50 |

### **Basic parameters**
To access the basic parameters, hold **FUNC** for 2 seconds to enter, press **FUNC** to scroll through the parameters, **▲/▼** to change them, and hold **FUNC** for 2 seconds to exit:

![Basic controller parameters](../../../../_shared/media/images/tramoggia-parametri-base.png)

| Definition | Symbol | Range | Default |
|---|---|---|---|
| Output frequency | E | 40.0–200.0 Hz | 100.0 |
| Maximum adjustable output voltage | h | 0–260 V | 260 |
| Communication address | r | 1–31 | 1 |
| Communication baud rate | c | 0.3–115.2 kbps | 115.2 |
| Controller reset | — | — | — |

### **Controller reset**

![Controller reset procedure](../../../../_shared/media/images/tramoggia-reset-controller.png)

1. Hold **FUNC** for 2 seconds to enter the basic parameter adjustment state.
2. Press **FUNC** until the reset parameter (`88888`) flashes on the display.
3. Hold **▲** until `-----` appears on the display.
4. Release **▲** to complete the reset: the display will show `U 50`, confirming that the operation was successful.


