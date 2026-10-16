# [SOF] **Sequence**

## Overview

The **Sequence** page allows custom operating sequences for the FlexiBowl® to be created, edited and managed. A sequence is an ordered list of commands that the system executes in automatic succession, combining rotation (MOVE), oscillation (SHAKE), flip and blow movements.

---

## Interface structure
![sequence page](../../../../_shared/media/images/sequence.png)

The page is organized into four main areas:

| No. | Area | Position | Description |
|---|---|---|---|
| 1 | [**Sequence selection**](seq) | Top left | Drop-down menu to select the active sequence |
| 2 | [**Emptying Sequence**](empty) | Top center | Toggle to activate emptying mode |
| 3 | [**Parameters panel**](param) | Left | MOVE, SHAKE and OPTION parameters; adding commands to the sequence |
| 4 | [**Commands panel**](comm) | Right | Ordered list of the commands in the active sequence and management tools |

---
(seq)=
## 1. Sequence selection

:::{important}
**Before any operation**, select the sequence to be edited using the **"Select the sequence"** drop-down menu at the top left.
:::

![select the sequence](../../../../_shared/media/images/sequence_combo_box.png)

The system supports up to **20 independent sequences** (SEQUENCE 1 – SEQUENCE 20), each with its own list of commands and independent parameters. The selected sequence becomes the active one on which all subsequent changes operate.

---
(empty)=
## 2. Emptying Sequence

![commands panel](../../../../_shared/media/images/empty_sequence.png)

The **Emptying Sequence** toggle (top center) activates a mode in which the sequence is executed with the aim of emptying the FlexiBowl® of the components present. It is used when the emptying option has been purchased.  
For more information on the emptying option, see the [dedicated page](svuotamento).

---
(param)=
## 3. Parameters panel

### MOVE parameters

| Parameter | Example value | Description |
|---|---|---|
| **Acceleration Move** | 50 % | Acceleration ramp for the rotation movement |
| **Deceleration Move** | 50 % | Deceleration ramp for the rotation movement |
| **Speed Move** | 35 % | Rotation speed of the FlexiBowl® |
| **Angle Move** | 360 Degree | Rotation angle covered during the MOVE command |

### SHAKE parameters

| Parameter | Example value | Description |
|---|---|---|
| **Acceleration Shake** | 50 % | Acceleration ramp during the shake |
| **Deceleration Shake** | 50 % | Deceleration ramp during the shake |
| **Speed Shake** | 50 % | Rotation speed during the shake |
| **Ccw Angle Shake** | -45 Degree | Rotation angle in the counterclockwise direction during each oscillation |
| **Cw Angle Shake** | -30 Degree | Rotation angle in the clockwise direction during each oscillation |
| **Count Shake** | 2 N° | Number of complete oscillations per shake cycle |

### OPTION parameters (flip and blow)

| Parameter | Example value | Description |
|---|---|---|
| **Flip Pressure** | 5.00 Bar | Air pressure for actuating the flip |
| **Flip Count** | 4 N° | Number of flips performed per cycle |
| **Flip Delay** | 100 ms | Interval between one flip and the next |
| **Blow Pressure** | 5.00 Bar | Air pressure for blowing |
| **Blow Time** | 200 ms | Duration of the blow pulse |

:::{note}
The parameters shown in the left panel apply to the sequence commands. Before adding a command with **ADD**, check that the values are correct: the parameters are associated with the command at the moment of insertion.
:::

---
(comm)=
## 4. Commands panel
### Selecting and adding a command

![commands panel](../../../../_shared/media/images/pannello_comandi_sequence.png)

The upper central panel contains:

- The **"Command Available"** drop-down menu: allows the type of command to be added to the sequence to be selected.
- The **ADD** button (arrow →): adds the selected command to the end of the list of active commands.

The available commands are:

| Command | Description |
|---|---|
| `FLB_NULL` | Null command, no action performed |
| `FLB_MOVE` | Rotation of the FlexiBowl® according to the MOVE parameters |
| `FLB_MOVE_FLIP` | Rotation combined with flip (tilting) of the plate |
| `FLB_MOVE_BLOWe` | Rotation combined with external blow |
| `FLB_MOVE_BLOWc` | Rotation combined with central blow |
| `FLB_MOVE_BLOWce` | Rotation combined with central and external blow |
| `FLB_MOVE_BLOWe_FLIP` | Rotation, external blow and flip combined |
| `FLB_MOVE_BLOWc_FLIP` | Rotation, central blow and flip combined |
| `FLB_MOVE_BLOWce_FLIP` | Rotation, central and external blow and flip combined |
| `FLB_SHAKE` | Shaking of the plate without rotation |
| `FLB_BLOWe` | External blow, without rotation |
| `FLB_BLOWc` | Central blow, without rotation |
| `FLB_BLOWce` | Central and external blow, without rotation |
| `FLB_FLIP` | Flip (tilting) of the plate, without rotation |
| `FLB_PAUSE_100ms` | Pause of 100 milliseconds |
| `FLB_PAUSE_200ms` | Pause of 200 milliseconds |
| `FLB_PAUSE_500ms` | Pause of 500 milliseconds |
| `FLB_LIGHT_1_ON` | Light 1 on |
| `FLB_LIGHT_1_OFF` | Light 1 off |
| `FLB_LIGHT_2_ON` | Light 2 on |
| `FLB_LIGHT_2_OFF` | Light 2 off |
| `FLB_ENABLE` | Enabling of the FlexiBowl® |
| `FLB_DISABLE` | Disabling of the FlexiBowl® |
| `FLB_BARRIER_DOWN` | Lowering of the barrier |
| `FLB_BARRIER_UP` | Raising of the barrier |

:::{tip}
Select the desired command from the drop-down menu before pressing **ADD**. The command will be inserted in the first free row of the **Command Active** list.
:::

The **Command Active** table shows the sequence of commands in execution order, numbered from 1 to 10.

In the example shown, the sequence contains only one command:

| No. | Command |
|---|---|
| 1 | FLB_MOVE |
| 2–10 | *(empty)* |

### List management tools

| Button | Function |
|---|---|
| **DELETE** | Deletes the selected command from the list |
| **UP** | Moves the selected command up one position |
| **DOWN** | Moves the selected command down one position |
| **CLEAR** | Clears all the commands in the list |

:::{warning}
The **CLEAR** button removes **all** the commands from the sequence with no possibility of recovery. Use it with caution.
:::

---

## 5. Executing the sequence

At the bottom right there are two execution buttons:

| Button | Adjacent field | Function |
|---|---|---|
| **TEST SEQUENCE** | Tempo esecuzione (ms) | Executes the sequence once only. The field on the right shows the total duration of the last execution in milliseconds |
| **RUN** | — | Starts the sequence in continuous operating mode (loop), waiting for triggers from the vision system |

:::{note}
The **ms** field next to **TEST SEQUENCE** indicates the total execution time of the complete sequence. In the example shown the value is **1140 ms**. This figure is useful for synchronization with the machine vision system.
:::

:::{important}
Before pressing **RUN**, check that:
- The motor is enabled (**ENABLE MOTOR** active)
- The system status is **READY**
- The sequence contains at least one valid command in the **Command Active** list
:::
