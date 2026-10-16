# [MEC] **Proportional Valve Replacement**

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

:::{warning}
Disconnect the electrical and pneumatic power supply before proceeding with the replacement of the proportional valve.
:::

:::{warning}
Some parts involved in the maintenance process described here may have reached {ref}`high temperatures <temp>` during operation; make sure to leave the FlexiBowl® switched off long enough for all its parts to be handled safely.
:::

## What you need

:::{list-table}
:widths: 40 40
:header-rows: 1

* - Item/equipment
  - Quantity

* - H5 hex key
  - 1

* - H4 hex key
  - 1

* - H2.5 hex key
  - 1

* - Replacement proportional valve
  - 1

:::

## Procedure

| Step | Operation |
|:----:|-----------|
| 1 | {ref}`Remove the surface or rigid disc <sost-disco>` |
| 2 | Remove the flip screen assembly |
| 3 | Remove the cover plate of the flip assembly (use two of the fixing screws for removal through the dedicated threaded holes) |
| 4 | Disconnect, remove the pneumatic connections and remove the proportional valve bracket |
| 5 | Replace the damaged proportional valve with the new one |
| 6 | Once the replacement is finished, refit all the components |

::::{raw} html
<figure style="text-align: center;">
  <video id="sostprop" width="100%" height="auto" controls>
    <source src="../../../../_shared/media/videos/AS000006_cambioprop.mp4" type="video/mp4">
    Your browser does not support the video.
  </video>
  <br>
  <label for="velcamprop">Speed:</label>
  <select id="velcamprop" onchange="document.getElementById('sostprop').playbackRate = this.value">
    <option value="0.5">0.5x</option>
    <option value="1" selected>1x</option>
    <option value="1.5">1.5x</option>
    <option value="2">2x</option>
  </select>
  <figcaption><i>Proportional valve replacement procedure shown on FlexiBowl® 800</i></figcaption>
</figure>
::::

:::{note}
Depending on whether blows are present, one or two proportional valves may be fitted: the second is located under the plate opposite the one that covers the flip assembly.
:::