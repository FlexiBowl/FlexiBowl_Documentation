(tracking)=
# [SOF] **Tracking Mode**

## Operation in Tracking

The **Flexitracking** option maximizes the productivity of the FlexiBowl® by making it rotate continuously and without interruption.  
 Instead of stopping at every cycle to take the photo and give the robot time to pick up the parts present in the vision area, an encoder keeps track of the rotation angle covered by the rigid disc surface from the moment the photo is taken to the moment the robot picks the part.  

:::{figure} ../../../../_shared/media/images/Tracking.png
:width: 50%
:align: center
:::

:::{image} ../../../../_shared/media/videos/TRACKING_MODE.GIF
:width: 100%
:align: center
:::

::::{tip}
Tracking operation moves the picking area which, if it normally coincides with the vision area, in this case will be moved downstream.  
 Refer to the {ref}`Layout Best Practice <layoutbp>` chapter for more information on the recommended placement of the robot and of the other accessories in the case of standard and Flexitracking operation.  

:::{figure} ../../../../_shared/media/images/TrackingLayout.PNG
:width: 80%
:align: center
:::

::::
---

## Main features

<div class="tracking-features">

| Feature | Description |
|---|---|
| **Performance** | Ideal for maximizing performance (up to 100%) |
| **Vision area** | One sector ahead of the picking area |
| **Parallelism** | Hopper discharge, FlexiBowl® movement/pulse, vision and picking running simultaneously |
| **Stability** | Greater stability of the instantaneous cycle time |
| **Precision** | Lower accuracy compared to standard mode |

</div>

---

## Operating cycle

Tracking operation is based on a continuous cycle divided into four phases that
take place in parallel:

```{list-table}
:header-rows: 1
:widths: 20 80

* - Phase
  - Description
* - **Detect**
  - The camera acquires the image of a sector of the FlexiBowl®, anticipating the picking area.
* - **Move**
  - The bowl rotates continuously without stopping; the encoder records the angular displacement
    in real time.
* - **Flip / Drop**
  - Parts that are not correctly oriented are flipped or discharged into the correct position.
* - **Pick**
  - The robot picks the parts, compensating for the movement of the FlexiBowl® thanks to the encoder data.
```

---

## Required hardware and software

The following components are required to enable Flexitracking:

- **Encoder option** on the FlexiBowl®
- **Tracking option** on the robot

### Connection diagram

Flexitracking is based on a motor assembly modified with a support for a belt drive
that drives the external encoder.

:::{figure} ../../../../_shared/media/images/GM001788.PNG
:width: 80%
:align: center
:::

The encoder signal is distributed through an **internal splitter**, which sends it both
to the motor driver and to the robot:

<div class="hw-schema">

```{list-table}
:header-rows: 1
:widths: 35 65

* - Component
  - Function
* - **Internal encoder splitter**
  - Splits the encoder signal towards the driver and towards the robot.
* - **External encoder**
  - Mounted on a shaft connected to the driven pulley through a support bracket;
    measures the actual rotation of the disc surface.
```

</div>

---
## JOG page 

The **Jog Motor** page allows the FlexiBowl® to be operated in tracking mode, without using programmed sequences. It is mainly used during the setup, commissioning and testing phases of the system, allowing the operator to directly control the rotation of the FlexiBowl® and the accessory functions.
![jog monitor page](../../../../_shared/media/images/jog_motor.png)

For more information, see the [JOG Page](jog)

#### JOG EXE Commands

| Command | ControlWord | Busy during execution | ReturnData_1 | Explanation | 
|---|---|---|---|---|
| Start Jog Seq | 40 | SI | 40 | Avvia Jog |
| Stop Jog Seq | 41 | SI | 41 | Ferma Jog |

#### JOG WRITE Commands

The Jog commands (continuous manual operation) can be configured separately via ControlWord in block 20000.

| Command | ControlWord | Data_1 range | Notes |
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

#### JOG READ Commands

The same writable JOG commands (block 20000) can be read in block 20100:

| Command | READ ControlWord | ReturnData_2 range |
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

::::{tip}
For the Error Codes, see the dedicated page. 
:::{card} GO TO THE DEDICATED PAGE
:link: sec-err
:link-type: ref
:class-card: isw-card-field
:class-body: isw-card-body
:::
::::
---

## Operating notes

:::{warning}
Tracking mode offers maximum performance but with a **slightly lower precision**
compared to standard mode. Evaluate its suitability based on the tolerance requirements
of the component to be handled.
:::

:::{note}
For the configuration of the offset parameter between the vision area and the picking area, refer
to the software configuration section of the system.
:::

