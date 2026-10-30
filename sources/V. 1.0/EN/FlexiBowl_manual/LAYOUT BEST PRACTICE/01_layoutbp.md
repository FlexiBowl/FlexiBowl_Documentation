(layoutbp)=
# **Layout Best Practice**

The FlexiBowl® work area is virtually divided into four sectors, each dedicated to a phase of the cycle: **release** of the components from the Bulk Feeder, **separation** by flip, **picking** by the robot and **recirculation** of the components not picked. A good layout respects this sequence in the direction of rotation of the FlexiBowl® and minimizes *pick and place* paths.

:::{figure} ../../../../_shared/media/images/Funz-standard.PNG
:align: center
:width: 50%

Work sectors of the FlexiBowl®: release, separation, picking and recirculation.
:::

## Guidelines for positioning the robot

:::{tip}
The best way to place the robot relative to the FlexiBowl® is the one that minimizes *pick and place* paths.
:::

(layoutbp-traditional)=
### Traditional Feeding

In {ref}`Traditional Feeding <sof-modalita-standard>` the picking area coincides with the vision area. The robot work area must therefore fully cover the vision area, so as to ensure that the robot can reach all the components identified as pickable.

<!-- DA COMPLETARE: distanze consigliate robot/FlexiBowl® per taglia -->

(layoutbp-tracking)=
### Circular Tracking

In {ref}`Circular Tracking <tracking>` the FlexiBowl® rotates continuously: the vision area is located one sector **upstream** of the picking area, which is therefore shifted **downstream** in the direction of rotation. The robot work area must cover the picking sector downstream of the vision area.

:::{figure} ../../../../_shared/media/images/TrackingLayout.PNG
:width: 80%
:align: center
:::

<!-- DA COMPLETARE -->

## Guidelines for positioning the Bulk Feeders

### General precautions

- Place the Bulk Feeder on a stable, horizontal surface, close to the FlexiBowl®.
- If the Bulk Feeder is installed on the table of a machine that is sensitive to vibrations, place insulating and anti-vibration material between the surfaces, to prevent the vibrations from being transmitted to the FlexiBowl® (see {ref}`tramoggia-antivibrazione`).
- Fasten the Bulk Feeder to the support bracket with M8 screws: 4 holes for standard Bulk Feeders, 2 holes for the 1.5 l Bulk Feeder.
- A single FlexiBowl® manages up to **4 Bulk Feeders**: in {ref}`Multiple Parts Feeding <funzionamento-in-mix-mode>` a Bulk Feeder can be dedicated to each part number.

### Recommended position

The chute of the Bulk Feeder must discharge the components directly into the **release sector**, upstream of the flip, with an inclination that follows the profile of the FlexiBowl®.

::::{tab-set}
:::{tab-item} Correct positioning
![Correct positioning of the Bulk Feeder relative to the FlexiBowl®](../../../../_shared/media/images/posizione_giustatramoggia.png)
:::
:::{tab-item} Incorrect positioning
![Example of incorrect positioning of the Bulk Feeder](../../../../_shared/media/images/posizione_sbagliatatramoggia.png)

A chute that is too far from the work area results in inconsistent feeding and penalizes the performance of the application.
:::
::::

## Guidelines for positioning the deposit points

### General guidelines

Place the deposit points (trays, conveyors, assembly stations) as close as possible to the picking area, to reduce the robot's travel on every cycle.

<!-- DA COMPLETARE -->

### Recommended position

<!-- DA COMPLETARE -->

## Guidelines for optimal movement configuration

<!-- DA COMPLETARE -->

## Guidelines for choosing the gripping tool

<!-- DA COMPLETARE -->

## Guidelines for positioning the Toplight

The {ref}`Toplight <toplight>` must be centered on the vision area, with the emitting surface parallel to the plane of the FlexiBowl® and the camera mounted in the central hole. The distance from the surface should be similar to that of the camera, to reduce shadows and direct reflections. For the mounting methods see {ref}`montaggio_staffa`.

## Guidelines for positioning the camera

The camera must be centered on the vision area, with the optical axis perpendicular to the surface of the FlexiBowl® and, if present, concentric with the Toplight. Calibration with the ARS grid must be performed with the Backlight on and the Toplight off.

<!-- DA COMPLETARE: altezze di montaggio e ottiche consigliate per taglia -->
