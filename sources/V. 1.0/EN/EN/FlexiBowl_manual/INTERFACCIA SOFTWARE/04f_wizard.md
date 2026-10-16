# [SOF] **Wizard**
The **FlexiBowl® Wizard** interface is an interactive tool designed to guide the user in configuring the feeding parameters according to the specific family of products to be handled.

![Wizard page](../../../../_shared/media/images/wizard_home_page.png)

## Step 0: Accessing the Wizard

:::{list-table}
* - **1**
  - To access the guided configuration of the FlexiBowl® parameters, simply click the **Wizard** page in the side menu. 
:::

:::{note}
The model and the direction of rotation of the FlexiBowl® are automatically detected by the software. 
:::

## Step 1: Component Characterization

The system requires information on the morphology of the parts in order to optimize separation.
````{list-table}
* - **2**
  - Select the size of the component:**

    **For FlexiBowl models 200, 350, 500, 650:**

    :::{card}
    <= 150mm
    :::

    :::{card}
    &gt; 150mm
    :::

    **For FlexiBowl models 800 and 1200:**

    :::{card}
    <= 250mm
    :::

    :::{card}
    &gt; 250mm
    :::

* - **3**
  - Select the geometry that best describes the component:
      * **FLAT**: Flat components.
      * **CYLINDRICAL**: Cylindrical components.
      * **COMPLEX**: Articulated or irregular geometries

      ![Flat Cylindrical or Complex](../../../../_shared/media/images/flatorcomplex.png)

      *Examples of geometries: Flat, Cylindrical and Complex.*

* - **4**
  - Define how the components interact with each other on the surface:
      * **Overlapping**: The parts tend to overlap.
      * **Not Overlapping**: The parts do not overlap.
      * **Tangling / Stacking**: The parts tend to hook together or stack.
      * **Not Tangling / Not Stacking**: The parts remain separate and do not jam.

      ![Overlapping](../../../../_shared/media/videos/overlapping.gif)

      *Not Overlapping: the parts do not overlap on the surface.*

      ::::{grid} 2
      :::{grid-item}
      ![Stacking](../../../../_shared/media/videos/stacking.gif)

      *Stacking: the parts stack up.*
      :::
      :::{grid-item}
      ![Tangling](../../../../_shared/media/videos/tangling.gif)

      *Tangling: the parts hook onto each other.*
      :::
      ::::
````
## Step 2: Accessory Test
```{list-table}
* - **5**
  - Select from the drop-down menu whether the FlexiBowl® is equipped with the **Air-blow** module.
* - **6**
  - Click **TEST Air-blow** to check that it works.
* - **7**
  - Select **USE** to enable it in the current application, otherwise click **DON'T USE**.
* - **8**
  - Click **TEST FLIP** to check that the striker is actually activated.
      The "Flip" is the unit that generates the mechanical pulse to flip the parts; it is essential for separating, untangling or turning over the components during the feeding cycle.
 
      :::{important}
      If the pulse cannot be felt, check that the compressed air is connected and act on the mechanical pressure regulator located on the control panel.
      :::
* - **9**
  - At the end of the Wizard, by clicking **FINISH**, the system will automatically calculate the parameters: 
    - Movement parameters (speed, acceleration, angle)
    - Shake parameters
    - Accessory timings (flip, blow)
* - **10**
  - You can then fine-tune them in the summary dashboard.
```
```{list-table} Parameters overview
   :widths: 20 30 50
   :header-rows: 1

   * - Group
     - Parameter
     - Description
   * - **Move**
     - Accel, Decel, Speed, Angle
     - Parameters of the main movement of the disc.
   * - **Option**
     - Flip Count, Flip Delay, Blow Time
     - Management of the accessory activation times.
   * - **Shake**
     - Accel, Speed, Angle CW/CCW
     - Parameters of the shaking vibration (separation).
```

## Step 3: Sequence Validation

Use the **...** function to check that the cycle meets the following efficiency criteria:
```{list-table}
:widths: 5 95
:header-rows: 0

* - **Synchronization**
  - The Flip pulse must end exactly at the same instant in which the movement (*Move*) ends. Adjust the *Flip Count* and *Delay* values to align them.

* - **Image Stability**
  - The components must be still at the moment the camera shot is taken.
    - If the parts move, reduce speed/acceleration or insert a pause (e.g. `pause 200ms`).

* - **Part positioning during the sequence**
  - During the movement, the parts must be conveyed towards the center of the radius of the FlexiBowl® to maximize the effectiveness of the Flip. At the end of the sequence, the parts must be arranged approximately in the center of the vision area.
```

:::{warning}
Always click **Synchronize Parameters** after every manual change to make the changes active in the controller.
:::
