
# [SOF] **Main Command**

## Overview

The **Main Command** page is the main operating section of the FlexiBowl® software interface. It allows the operator to configure and test the movement parameters and the accessory options of the system.

The page is divided into **three subpages**, selectable via the central drop-down menu located under the navigation bar, labeled **"Chose Visualization Page"**:

| Subpage | Brief description |
|---|---|
| **OPTION** | Parameters for flip, blow and backlight |
| **MOVE** | Parameters for the rotary movement of the FlexiBowl® |
| **SHAKE** | Parameters for the oscillating movement of the FlexiBowl® |

---

## Subpage: OPTION

The **OPTION** subpage collects the parameters relating to the accessory functions of the FlexiBowl®: the component flipping system (flip), the blowing system (blow) and the backlight.
![option page](../../../../_shared/media/images/main_command_option.png)

| Parameter | Unit | Description |
|---|---|---|
| **Flip Pressure** | Bar  | Air pressure used to actuate the flip. Adjustable via slider |
| **Flip Count** | N°  | Number of flips performed in sequence during a cycle |
| **Flip Delay** | ms  | Time interval between one flip and the next |
| **Blow Pressure** | Bar  | Air pressure used to blow the components on the FlexiBowl® |
| **Blow Time** | ms  | Duration of the blow pulse |

Each parameter is adjustable via a **horizontal slider**; the current value is shown in the numeric box to the right of the slider.

### Backlight controls

| Control | Description |
|---|---|
| **Backlight_1** | On/off toggle for backlight 1  |
| **Backlight_2** | On/off toggle for backlight 2  |

The toggles show red when the backlight is **active**.

### Test buttons

At the bottom of the page there are three buttons for testing the functions in real time:

| Button | Function |
|---|---|
| **TEST FLIP** | Performs a flip with the currently set parameters |
| **TEST BLOWe** | Activates the external blow with the set parameters |
| **TEST BLOWc** | Activates the central blow with the set parameters |

:::{attention}  
 Before running the tests, make sure the motor is enabled (**ENABLE MOTOR** button active) and that the system status is **READY**.
:::

---

## Subpage: MOVE

The **MOVE** subpage allows the rotary movement parameters of the FlexiBowl® to be configured and tested directly from the interface.
![move page](../../../../_shared/media/images/main_command_move.png)

| Parameter | Unit | Default value | Description |
|---|---|---|---|
| **Acceleration** | % | 50 | Motor acceleration ramp at the start of the movement. Higher values produce a more abrupt start |
| **Deceleration** | % | 50 | Motor deceleration ramp during stopping. Higher values produce a more abrupt stop |
| **Speed** | % | 50 | Rotation speed of the FlexiBowl® during the movement |
| **Angle** | Degree | 45 | Rotation angle covered by the FlexiBowl® during each single movement |

Each parameter is adjustable via a **horizontal slider**; the current value is shown in the numeric box to the right of the slider.

### Test button

| Button | Adjacent field | Function |
|---|---|---|
| **TEST MOVE** | Execution time (ms) | Performs a rotation movement with the currently set parameters. The field on the right shows the actual duration of the last movement performed, in milliseconds |

:::{note}  
 The **ms** field shows the actual time taken by the bowl to complete the set movement. This value is useful for synchronizing the FlexiBowl® with the machine vision system.
:::

:::{attention}   
Before running the test, make sure the motor is enabled (**ENABLE MOTOR** button active) and that the system status is **READY**.
:::

---

## Subpage: SHAKE

The **SHAKE** subpage allows the oscillating movement parameters of the FlexiBowl® (shake), used to redistribute the components on the plate, to be configured and tested directly from the interface.
![shake page](../../../../_shared/media/images/main_command_shake.png)

| Parameter | Unit | Default value | Description |
|---|---|---|---|
| **Acceleration** | % | 50 | Motor acceleration ramp during the shake phase |
| **Deceleration** | % | 50 | Motor deceleration ramp during the shake phase |
| **Speed** | % | 50 | Rotation speed during the shake movement |
| **Ccw Angle** | Degree | -45 | Rotation angle in the **counterclockwise** direction (Counter-ClockWise) during each oscillation |
| **Cw Angle** | Degree | 45 | Rotation angle in the **clockwise** direction (ClockWise) during each oscillation |
| **Count** | N° | 2 | Number of complete oscillations performed during a shake cycle |

Each parameter is adjustable via a **horizontal slider**; the current value is shown in the numeric box to the right of the slider.

:::{note}  
 The **shake** movement consists of a series of alternating clockwise and counterclockwise rotations, defined by **Cw Angle** and **Ccw Angle** respectively. The number of complete oscillations is controlled by the **Count** parameter.
:::

### Test button

| Button | Adjacent field | Function |
|---|---|---|
| **TEST SHAKE** | Execution time (ms) | Performs a shake cycle with the currently set parameters. The field on the right shows the actual duration of the last shake performed, in milliseconds |

:::{attention}  
 Before running the test, make sure the motor is enabled (**ENABLE MOTOR** button active) and that the system status is **READY**.
:::