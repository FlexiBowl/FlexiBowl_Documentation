(sostbl)=
# [MEC] **Backlight Replacement**

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

* - **Mechanical maintenance technician**
  - :::{raw} html
       <div class="ars-img-row">
         <img src="../../../../_shared/media/images/guanti.png" alt="gloves">
         <img src="../../../../_shared/media/images/scarpe.png" alt="shoes">
         <img src="../../../../_shared/media/images/tuta.png" alt="overalls">
       </div>
    :::
::::
:::::

The backlight must be replaced if it malfunctions or if the type of light needs to be changed following a production changeover.

:::{warning}
Disconnect the electrical power supply before proceeding with the replacement of the Backlight.
:::

:::{warning}
Some parts involved in the maintenance process described here may have reached {ref}`high temperatures <temp>` during operation; make sure to leave the FlexiBowl® switched off long enough for all its parts to be handled safely.
:::

:::{important}
The infrared Backlight emits invisible light and may therefore appear not to be working. Check with an infrared camera to verify its operation.

**Note:** Most smartphones can display infrared.
:::

## What you need

:::{list-table}
:widths: 40 40
:header-rows: 1

* - Item/equipment
  - Quantity

* - H2.5 hex key
  - 1

* - H5 hex key
  - 1

* - Replacement Backlight
  - 1

:::

## Procedure

| Step | Operation |
|:----:|-----------|
| 1 | {ref}`Remove the surface or rigid disc <sost-disco>` |
| 2 | Remove the protective glass of the illuminator (use the dedicated side pockets) |
| 3 | Remove the screws that fix the illuminator board to its seat |
| 4 | Extract the illuminator board and disconnect its connector |
| 5 | Connect the new board and fit it in the correct position |
| 6 | Once the replacement is finished, refit all the components |

::::{raw} html
<figure style="text-align: center;">
  <video id="myVideo" width="100%" height="auto" controls>
    <source src="../../../../_shared/media/videos/AS000006_cambio-backlight.mp4" type="video/mp4">
    Your browser does not support the video.
  </video>
  <br>
  <label for="speedControl">Speed:</label>
  <select id="speedControl" onchange="document.getElementById('myVideo').playbackRate = this.value">
    <option value="0.5">0.5x</option>
    <option value="1" selected>1x</option>
    <option value="1.5">1.5x</option>
    <option value="2">2x</option>
  </select>
  <figcaption><i>Backlight replacement procedure shown on FlexiBowl® 800</i></figcaption>
</figure>
::::