# **Sustitución de la válvula proporcional**

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
* - {ref}`Cualificación del operario <operatori>`
  - {ref}`EPI necesarios <dpi>`

* - **Técnico de mantenimiento mecánico**
  - :::{raw} html
       <div class="ars-img-row">
         <img src="../../../../_shared/media/images/guanti.png" alt="guantes">
         <img src="../../../../_shared/media/images/scarpe.png" alt="calzado">
         <img src="../../../../_shared/media/images/tuta.png" alt="mono">
       </div>
    :::
::::
:::::

:::{warning}
Desconecte la alimentación eléctrica y neumática antes de proceder a la sustitución de la válvula proporcional.
:::

:::{warning}
Algunas partes implicadas en el proceso de mantenimiento aquí descrito pueden haber alcanzado {ref}`altas temperaturas <temp>` durante el funcionamiento; asegúrese de dejar el FlexiBowl® apagado el tiempo suficiente para que todas sus partes puedan manipularse con seguridad.
:::

## ¿Qué se necesita?

:::{list-table}
:widths: 40 40
:header-rows: 1

* - Objeto/equipo
  - Cantidad

* - Llave hexagonal H5
  - 1

* - Llave hexagonal H4
  - 1

* - Llave hexagonal H2.5
  - 1

* - Válvula proporcional de repuesto
  - 1

:::

## Procedimiento

| Paso | Operación |
|:----:|-----------|
| 1 | {ref}`Retirar la superficie o el disco rígido <sost-disco>` |
| 2 | Retirar el grupo de pantalla del flip |
| 3 | Retirar la placa de cubierta del grupo flip (utilizar dos de los tornillos de fijación para extraerla mediante los orificios roscados previstos) |
| 4 | Desconectar, retirar las conexiones neumáticas y desmontar el soporte de la válvula proporcional |
| 5 | Sustituir la válvula proporcional dañada por la nueva |
| 6 | Una vez terminada la sustitución, vuelva a montar todos los componentes |

::::{raw} html
<figure style="text-align: center;">
  <video id="sostprop" width="100%" height="auto" controls>
    <source src="../../../../_shared/media/videos/AS000006_cambioprop.mp4" type="video/mp4">
    Su navegador no admite el vídeo.
  </video>
  <br>
  <label for="velcamprop">Velocidad:</label>
  <select id="velcamprop" onchange="document.getElementById('sostprop').playbackRate = this.value">
    <option value="0.5">0.5x</option>
    <option value="1" selected>1x</option>
    <option value="1.5">1.5x</option>
    <option value="2">2x</option>
  </select>
  <figcaption><i>Procedimiento de sustitución de la válvula proporcional ilustrado en un FlexiBowl® 800</i></figcaption>
</figure>
::::

:::{note}
Según la presencia o no de los soplados, puede haber una o dos válvulas proporcionales: la segunda se encuentra bajo la placa opuesta a la que cubre el grupo flip.
:::