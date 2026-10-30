# **Standard Mode**

The **Standard Mode** is the default operating configuration of the FlexiBowl® and suits any type of robotic feeding application. In this mode, the robot and the vision system share the same work area, operating in a coordinated and sequential manner to ensure high cycle performance.

---

## Operating principle

In Standard Mode, the FlexiBowl® runs a continuous cycle made up of three main phases, repeating in sequence:

```{figure} ../../../../_shared/media/images/flexibowl_standard_cycle.jpg
:align: center
:width: 50%
:alt: *Operating cycle in Standard Mode: Detect → Pick-Drop → Move-Flip*
```
```{image} ../../../../_shared/media/videos/STANDARD_MODE.gif
:align: center
:width: 100%
:alt: *Operating cycle in Standard Mode: Detect → Pick-Drop → Move-Flip*
```

### 1. Detect

The vision system acquires an image of the FlexiBowl® surface and identifies the position, orientation and type of the components present. The information is sent to the robot to plan the picking operations.

### 2. Pick-Drop (Picking and Placing)

The robot picks the correctly oriented components from the FlexiBowl® and places them in the destination position (e.g. tray, conveyor belt, assembly station). The vision and picking activities are performed **sequentially**: first the vision system scans the scene, then the robot intervenes.

### 3. Move-Flip (Movement and Flipping)

At the end of the picking, the FlexiBowl® performs a combined rotation and vibration movement (**flip**) to reshuffle the remaining components and promote the correct presentation of new parts. At the same time, the **hopper discharge** and the **bowl movement** are performed **simultaneously**, optimizing the cycle times.

---

## Main features

| Feature | Description |
|---|---|
| **Shared work area** | The robot and the vision system operate in the same area of the FlexiBowl® |
| **Applicability** | Suitable for all types of application |
| **Hopper discharge** | Performed simultaneously with the movement/pulse of the FlexiBowl® |
| **Vision and picking** | Performed in sequence |
| **Cycle measurement** | The cycle time is measured on a per-minute basis |

---

## Operating cycle diagram

The cycle runs according to the following closed-loop scheme:

1. **Detect** — The vision system scans the FlexiBowl® and locates the components.
2. **Pick-Drop** — The robot picks the identified parts and places them at the destination.
3. **Move-Flip** — The FlexiBowl® reshuffles the components for the next cycle.
4. The cycle starts again from point 1.

:::{note} 
During the Move-Flip phase, the hopper discharge takes place in parallel with the movement of the FlexiBowl®, reducing dead times and maximizing productivity.
:::

---
## Layout example

:::{figure} ../../../../_shared/media/images/Funz-standard.PNG
:align: center
:width: 60%

Layout example in Standard Mode: the Bulk Feeder discharges into the release sector, the flip separates the components, the robot picks in the vision area and the parts not picked recirculate.
:::

The robot work area must fully cover the vision area, so that the robot can reach all the components recognized as pickable. For the positioning of the robot, Bulk Feeder, deposit points, camera and lighting, refer to {ref}`Layout Best Practice <layoutbp-traditional>`.


---

## Advantages 


:::{grid-item-card} Advantages
- **Accuracy**: .
- **Separation**: .
- **Speed**: .
:::
