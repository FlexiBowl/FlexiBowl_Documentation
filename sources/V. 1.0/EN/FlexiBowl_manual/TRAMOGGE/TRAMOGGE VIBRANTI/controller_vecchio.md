# Old Controller
## Standard controller

#### Electrical connections and controller setup

:::{attention}
Before switching on the controller, plug the Schuko plug into the power socket, checking that the system has an adequate earthing system.
:::

To start up, proceed as described:

<div style="display: flex; flex-direction: column; gap: 12px; margin: 20px 0;">
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #34495e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">1</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Connect the cable of the linear base to the output connector of the controller (i.e. connect the vibrator to the output connector <strong>(1)</strong>).
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #34495e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">2</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Turn the frequency adjustment knob <strong>(2)</strong> and the amplitude adjustment knob <strong>(3)</strong> of the controller to the "•" position.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #34495e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">3</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Switch on the controller with the ON/OFF button (button in position 1 <strong>(4)</strong>).
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #34495e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">4</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Slowly turn the adjustment knobs <strong>(2 and 3)</strong>. Before bringing the vibration to the maximum (Amplitude potentiometer <strong>(3)</strong>), it is recommended to find the correct resonance frequency (50 Hertz) with the Frequency potentiometer <strong>(2)</strong>.
    </div>
  </div>
</div>

![Controller with pointers](../../../../../_shared/media/images/controller_puntatori.png)

To comply with the EMC standard, the circuit is fitted with a filter with earth leakage currents below 1 mA.  
 The circuit supplies the vibrator with a PWM (pulse-width modulation) signal adjustable in amplitude and frequency, compensated for line voltage variations.  
  The control section is galvanically isolated from the power section.  
   At power-on, the circuit waits a few seconds before enabling the vibrator.

The circuit is microprocessor-controlled and is equipped with output current limitation via fuse F4 (4 A).

**Fuse protections**

| Fuse | Value | Position |
| :--- | :--- | :--- |
| **F1** | 6.3 A | Line input |
| **F3** | 250 mA | ON/OFF input — limits the current available for the NPN/PNP sensor and any solenoid valve |
| **F4** | 4 A | Vibrator output |

**LED indicators on the board**

| LED | Color | Status: on |
| :--- | :--- | :--- |
| **LD1** | Red | High voltage present on the filter capacitors (up to over 300 V with 230 V line) |
| **LD2** | Green | Voltage present in the control circuit. Off if F1, F2 or F3 are blown |
| **LD3** | Green | ON/OFF relay switched — vibrator running or stopped |
| **LD4** | Yellow | Relay switched due to the no-parts time being exceeded |

:::{attention}
Absolutely avoid touching the circuit while the red LED (LD1) is on.
:::

The relays associated with LD3 and LD4 expose a changeover contact on connectors **CONN4** and **CONN5**: **CONN4** allows cascade control of an additional module, **CONN5** the activation of a parts-flow alarm.

**Available adjustments**

The trimmers on the board allow the behavior of the vibrator to be adapted to the application:

- **TR2** — vibrator stop delay (0 ÷ 10 sec)
- **TR3** — vibrator start delay (0 ÷ 10 sec)
- **TR4** — maximum amplitude
- **TR5** — additional start-up delay
- **TR6** — minimum amplitude

The vibrator can be stopped and restarted via an external command on **CONN3**, compatible with a dry contact, NPN/PNP sensor or 0–24 V output, with or without the configured delays.  
 Via **DP1** it is possible to select the direct or inverted logic of the ON/OFF signal.

**Standard configuration recommended by ARS**

| Component | Setting |
| :--- | :--- |
| **DP1** | Both switches in the ON position |
| **DP2** | Switch 2 ON — Switch 1 OFF |
| **TR2 e TR3** | Adjustment screw turned counterclockwise to the end stop |
| **CONN3** | Hopper start with dry contact |

![Controller drawing](../../../../../_shared/media/images/disegno_controller.jpg)

---

### Analog controller

![Analog controller](../../../../../_shared/media/images/controller_analogico.png)

#### Electrical connections and controller setup

To start up, proceed as described and refer to the image at the end of the paragraph:

<div style="display: flex; flex-direction: column; gap: 12px; margin: 20px 0;">
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">1</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Connect the 80/250 Vac power supply to connector <strong>CONN 1</strong>.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">2</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Connect the cable coming from the vibrating base to connector <strong>CONN 2</strong>.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">3</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Connect the activation command to connector <strong>CONN 3</strong>.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">4</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Connect the analog input to connector <strong>CONN 7</strong>.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">5</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Adjust trimmer <strong>TR1</strong> so that the frequency is 50 Hertz.
    </div>
  </div>
</div>

To comply with the EMC standard, the circuit is fitted with a filter with earth leakage currents below 1 mA.  
 The circuit supplies the vibrator with a PWM signal adjustable in amplitude via an analog signal and in frequency via trimmer **TR1**.  
  The signal is compensated for line voltage variations. The control section is galvanically isolated from the power section.  
   At power-on, the circuit waits a few seconds before enabling the vibrator.

The circuit is microprocessor-controlled and is equipped with output current limitation via fuse F4 (4 A).

**Fuse protections**

| Fuse | Value | Position |
| :--- | :--- | :--- |
| **F1–F2** | 6.3 A | Line input |
| **F3** | 250 mA | ON/OFF input — limits the current available for the NPN/PNP sensor and any solenoid valve |
| **F4** | 4 A | Vibrator output |

**LED indicators on the board**

| LED | Color | Status: on |
| :--- | :--- | :--- |
| **LD1** | Red | High voltage present on the filter capacitors (up to over 300 V with 230 V line) |
| **LD2** | Green | Voltage present in the control circuit. Off if F1, F2 or F3 are blown |
| **LD3** | Green | ON/OFF relay switched — vibrator running or stopped |
| **LD4** | Yellow | Relay switched due to the no-parts time being exceeded |

:::{attention}
Absolutely avoid touching the circuit while the red LED (LD1) is on.
:::

The relays associated with LD3 and LD4 expose a changeover contact on connectors **CONN4** and **CONN5**: **CONN4** allows cascade control of an additional module, **CONN5** the activation of a parts-flow alarm.

**Available adjustments**

The trimmers on the board allow the behavior of the vibrator to be adapted to the application:

- **TR2** — vibrator stop delay (0 ÷ 10 sec)
- **TR3** — vibrator start delay (0 ÷ 10 sec)
- **TR4** — delay after which the no-parts alarm is triggered (0 ÷ 10 sec)
- **TR5** — additional activation time of the air-blow solenoid valve after the vibrator stops (0 ÷ 3 sec)
- **TR6** — ramp at vibrator start-up (0 ÷ 3 sec)
- **TR7** — maximum amplitude on the vibrator

The vibrator can be stopped and restarted via an external command on **CONN3**, compatible with a dry contact, NPN/PNP sensor or 0–24 V output, with or without the configured delays.  
 Via **DP1** it is possible to select the NC or NO logic of the ON/OFF signal.    
 The vibration amplitude is adjusted by setting the appropriate analog voltage on **CONN7**.

**Standard configuration recommended by ARS**

| Component | Setting |
| :--- | :--- |
| **DP1** | Both switches in the ON position |
| **DP2** | Switch 1 ON — Switch 2 OFF |
| **TR2 e TR3** | Adjustment screw turned counterclockwise to the end stop |
| **CONN3** | Hopper start with dry contact |


![Controller diagram](../../../../../_shared/media/images/controller_schema.png)