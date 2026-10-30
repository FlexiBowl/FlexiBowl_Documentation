(sostbl)=
# **Sustitución del Backlight**

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

El backlight debe sustituirse si presenta fallos de funcionamiento o si es necesario cambiar el tipo de luz tras un cambio de producción.

:::{warning}
Desconecte la alimentación eléctrica antes de proceder a la sustitución del Backlight.
:::

:::{warning}
Algunas partes implicadas en el proceso de mantenimiento aquí descrito pueden haber alcanzado {ref}`altas temperaturas <temp>` durante el funcionamiento; asegúrese de dejar el FlexiBowl® apagado el tiempo suficiente para que todas sus partes puedan manipularse con seguridad.
:::

:::{important}
El Backlight infrarrojo emite luz no visible y, por lo tanto, puede parecer que no funciona. Compruébelo con una cámara infrarroja para verificar su funcionamiento.

**Nota:** La mayoría de los smartphones muestran los infrarrojos.
:::

## ¿Qué se necesita?

:::{list-table}
:widths: 40 40
:header-rows: 1

* - Objeto/equipo
  - Cantidad

* - Llave hexagonal H2.5
  - 1

* - Llave hexagonal H5
  - 1

* - Backlight de repuesto
  - 1

:::

## Procedimiento

| Paso | Operación |
|:----:|-----------|
| 1 | {ref}`Retirar la superficie o el disco rígido <sost-disco>` |
| 2 | Retirar el cristal de protección del iluminador (utilizar los huecos laterales previstos) |
| 3 | Retirar los tornillos que fijan la placa del iluminador a su alojamiento |
| 4 | Extraer la placa del iluminador y desconectar su conector |
| 5 | Conectar la nueva placa y montarla en la posición correcta |
| 6 | Una vez terminada la sustitución, vuelva a montar todos los componentes |

::::{raw} html
<figure style="text-align: center;">
  <video id="myVideo" width="100%" height="auto" controls>
    <source src="../../../../_shared/media/videos/AS000006_cambio-backlight.mp4" type="video/mp4">
    Su navegador no admite el vídeo.
  </video>
  <br>
  <label for="speedControl">Velocidad:</label>
  <select id="speedControl" onchange="document.getElementById('myVideo').playbackRate = this.value">
    <option value="0.5">0.5x</option>
    <option value="1" selected>1x</option>
    <option value="1.5">1.5x</option>
    <option value="2">2x</option>
  </select>
  <figcaption><i>Procedimiento de sustitución del backlight ilustrado en un FlexiBowl® 800</i></figcaption>
</figure>
::::