# **Cableado del FlexiBowl®**

<style>
.ars-dropdown {
  margin-top: 0.35rem;
}
.ars-dropdown summary {
  cursor: pointer;
  color: #2980b9;
  font-weight: 600;
  font-size: 0.82rem;
  padding: 0.35rem 0.7rem;
  border: 1px solid #d0e4f0;
  border-radius: 6px;
  display: inline-block;
  background: #f0f7ff;
  list-style: none;
  user-select: none;
}
.ars-dropdown summary::-webkit-details-marker { display: none; }
.ars-dropdown summary::before {
  content: "▸ ";
}
.ars-dropdown[open] summary::before {
  content: "▾ ";
}
.ars-dropdown[open] summary {
  border-radius: 6px 6px 0 0;
}
.ars-dropdown .ars-dropdown-body {
  border: 1px solid #d0e4f0;
  border-top: none;
  border-radius: 0 0 6px 6px;
  padding: 0.6rem;
  background: #fff;
}
.ars-dropdown img {
  display: block;
  max-width: 100%;
  width: 360px;
  border-radius: 4px;
}
.ars-step-warn, .ars-step-attn, .ars-step-note {
  border-radius: 5px;
  padding: 0.5rem 0.75rem;
  font-size: 0.83rem;
  margin-top: 0.55rem;
  line-height: 1.4;
}
.ars-step-warn { background:#fff3cd; border-left:4px solid #f0ad4e; color:#7a5b00; }
.ars-step-attn { background:#fee2e2; border-left:4px solid #dc2626; color:#8a1c1c; }
.ars-step-note { background:#eef6fc; border-left:4px solid #2980b9; color:#1a3a52; }
.ars-pin-table { width:100%; border-collapse:collapse; font-size:0.8rem; margin-top:0.4rem; }
.ars-pin-table th { background:#f0f4f8; padding:0.3rem 0.5rem; text-align:left; border:1px solid #d0e4f0; }
.ars-pin-table td { padding:0.3rem 0.5rem; border:1px solid #d0e4f0; }


.ars-zoom-img {
  transition: transform 0.35s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.35s ease;
  cursor: zoom-in;
  position: relative;
}
.ars-zoom-img:hover {
  transform: scale(1.8);
  box-shadow: 0 12px 40px rgba(0,0,0,0.22);
  z-index: 10;
}
</style>

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

* - **Técnico de mantenimiento eléctrico**
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
Antes de realizar cualquier conexión eléctrica, asegurarse de que la alimentación esté desconectada y de que el sistema se encuentre en estado seguro.
:::

El cableado del FlexiBowl® varía según el tamaño de la máquina:

- **FlexiBowl® 500 – 1200**: todas las conexiones (STO, Ethernet, Hopper, alimentación, aire) se encuentran en un único **panel eléctrico estándar**, montado directamente en la máquina.
- **FlexiBowl® 200 / 350**: las conexiones principales se encuentran en un **rack** externo; el rack se conecta después a la máquina mediante 4 cables dedicados (Ethernet, Motor+STO, señal A, señal B). En la máquina solo queda por conectar el aire comprimido.

---

## FlexiBowl® 500 – 1200 — Panel eléctrico estándar

```{list-table}
:widths: 8 52 40
:header-rows: 1

* - #
  - Acción
  - Imagen
* - 1
  - **Conectar el STO.**

    <div class="ars-step-note">
    Conector de 10 pines. Las entradas <strong>+STO1</strong> y <strong>+STO2</strong> deben recibir <strong>+24 Vdc</strong> del circuito de seguridad; <strong>−STO1</strong> y <strong>−STO2</strong> deben conectarse a la referencia de −24 Vdc.
    </div>

    <details class="ars-dropdown"><summary>Pinout del conector de 10 pines</summary><div class="ars-dropdown-body">

    | Pin | Descripción |
    |---|---|
    | 1 | +24 Vdc |
    | 2 | −24 Vdc |
    | 3 | +STO1 |
    | 4 | −STO1 |
    | 5 | +STO2 |
    | 6 | −STO2 |
    | 7–10 | NC |

    </div></details>
  - 
    ```{image} ../../../../_shared/media/images/connectSTO.png
    :alt: Conectar el STO
    :class: ars-zoom-img
    ```

* - 2
  - **Conectar el Ethernet (C-ETH).**

    <div class="ars-step-attn">
    Cuando el FlexiBowl® está alimentado, la conexión Ethernet es <strong>obligatoria</strong>: si falta, la máquina pasa al estado <strong>ERROR</strong> (LED Ready/Fault rojo).
    </div>

    <details class="ars-dropdown"><summary>Distribución de pines M12 → RJ45</summary><div class="ars-dropdown-body">

    Adaptador M12 de 8 polos → RJ45:

    | Pin RJ45 | Señal | Función | Color |
    |---|---|---|---|
    | 1 | TD+ | Transmisión de datos (+) | Amarillo |
    | 2 | TD− | Transmisión de datos (−) | Naranja |
    | 3 | RD+ | Recepción de datos (+) | Blanco |
    | 4 | NC | No asignado | — |
    | 5 | NC | No asignado | — |
    | 6 | RD− | Recepción de datos (−) | Azul |
    | 7 | NC | No asignado | — |
    | 8 | NC | No asignado | — |

    Conector M12 código D de 4 polos:

    | Pin M12 | Señal | Función | Color |
    |---|---|---|---|
    | 1 | TD+ | Transmisión de datos (+) | Amarillo |
    | 2 | RD+ | Recepción de datos (+) | Blanco |
    | 3 | TD− | Transmisión de datos (−) | Naranja |
    | 4 | RD− | Recepción de datos (−) | Azul |

    </div></details>
  - 
    ```{image} ../../../../_shared/media/images/connectEthernet.png
    :alt: Conectar el Ethernet
    :class: ars-zoom-img
    ```

* - 3
  - **Conectar el Hopper.**

    <div class="ars-step-note">
    Conector M12 con codificación A, utilizado para comunicarse con los controladores de hopper ARS mediante el protocolo <strong>Modbus RTU</strong>.
    </div>

    <details class="ars-dropdown"><summary>Distribución de pines M12 código A</summary><div class="ars-dropdown-body">

    | Pin M12 | Señal | Función | Color |
    |---|---|---|---|
    | 1 | A+ | Línea de datos RS485 (+) | Marrón |
    | 2 | NC | No asignado | Blanco |
    | 3 | B− | Línea de datos RS485 (−) | Azul |
    | 4 | GND | Referencia común | Negro |
    | 5 | NC | No asignado | Gris |

    </div></details>
  - 
    ```{image} ../../../../_shared/media/images/connectHopper.png
    :alt: Conectar el Hopper
    :class: ars-zoom-img
    ```

* - 4
  - **Conecte la alimentación (Power Supply).**

    <div class="ars-step-attn">
    Asegurarse de que el FlexiBowl® esté <strong>apagado</strong> antes de conectar la alimentación.
    </div>

    <div class="ars-step-warn">
    Tensión admitida: <strong>120–230 Vac, 50/60 Hz</strong>.
    </div>

    <div class="ars-step-note">
    En el primer arranque, compruebe el estado de los fusibles. Tras el encendido, espere a que se ilumine el LED de estado (Ready/Fault): si el Hopper y el C-ETH están correctamente conectados, el LED será <strong>verde</strong>.
    </div>

    <details class="ars-dropdown"><summary>Esquema de distribución de pines del cable de alimentación</summary><div class="ars-dropdown-body">

    | Color | Tipo | Etiqueta |
    |---|---|---|
    | Marrón | Fase | L1 |
    | Azul | Neutro | N1 |
    | Amarillo/Verde | Tierra | PE1 |

    </div></details>
  - 
    ```{image} ../../../../_shared/media/images/connectSupply.png
    :alt: Conectar la alimentación
    :class: ars-zoom-img
    ```

* - 5
  - **Conecte el aire comprimido** con un tubo **Ø 8 mm**.

    :::{note}
    Para las características del aire requeridas (presión, clase de limpieza ISO) consulte los [Datos técnicos neumáticos](datipneum).
    :::
  - 
    ```{image} ../../../../_shared/media/images/connectAir.png
    :alt: Conectar el aire comprimido Ø8mm
    :class: ars-zoom-img
    ```
```
:::{video} ../../../../_shared/media/videos/cablaggio_FB800.mp4
:width: 100% 
:::

---

## FlexiBowl® 200 / 350 — Rack externo

Para estos tamaños, las conexiones con las instalaciones del cliente se encuentran en el **rack** externo (no en la máquina). El rack debe conectarse después a la máquina mediante 4 cables dedicados.

### Conexiones en el rack

Los conectores del rack son los mismos que los del panel estándar (mismo pinout), simplemente ubicados en una caja externa en lugar de en la máquina.

```{list-table}
:header-rows: 1

* - #
  - Acción

* - 1
  - **Conecte el STO** en el rack — mismo conector de 10 pines que el panel estándar (véase la tabla de pinout anterior).

* - 2
  - **Conecte el C-ETH IN** en el rack — mismo conector M12 con codificación D que el panel estándar. Se aplica la misma regla: la conexión es obligatoria; de lo contrario, la máquina pasa a ERROR.

* - 3
  - **Conecte el Hopper** en el rack — mismo conector M12 con codificación A (Modbus RTU) que el panel estándar.

* - 4
  - **Conecte la alimentación** en el rack — 120–230 Vac.

    <div class="ars-step-attn">
    Asegurarse de que el FlexiBowl® esté <strong>apagado</strong> antes de conectar la alimentación.
    </div>
```

### Conexión entre el rack y el FlexiBowl®

El rack se comunica con el FlexiBowl® mediante 4 cables dedicados, cada uno de los cuales debe conectarse **exclusivamente** al puerto con la etiqueta correspondiente en el panel.

:::{attention}
Conectar cada cable al puerto con la **etiqueta correspondiente** (p. ej., MOTOR ↔ MOTOR, C-A SIGNAL ↔ C-A SIGNAL). Una conexión cruzada puede dañar el sistema.
:::

```{list-table}
:widths: 8 52 40
:header-rows: 1

* - #
  - Acción
  - Imagen
* - 5
  - **Conecte el cable Ethernet (C-ETH FB)** entre el rack y el FlexiBowl® — conector M12 con codificación D.
  - 
    ```{image} ../../../../_shared/media/images/connectEthernet200.png
    :width: 110%
    :alt: Conectar el cable C-ETH FB
    :class: ars-zoom-img
    ```
* - 6
  - **Conectar el cable MOTOR.**

    <div class="ars-step-note">
    Conector de 9 pines: transporta tanto la alimentación del motor como las señales <strong>STO</strong> hacia el FlexiBowl® (en el rack, STO y Motor son conectores separados; en el cable hacia la máquina se combinan en un único conector de 9 pines).
    </div>
  - 
    ```{image} ../../../../_shared/media/images/connectMotor.png
    :width:110%
    :alt: Conectar el cable Motor
    :class: ars-zoom-img
    ```
* - 7
  - **Conecte el cable C-A SIGNAL** — conector de 19 pines para las señales analógicas.
  - 
    ```{image} ../../../../_shared/media/images/connectASignal.png
    :width:110%
    :alt: Conectar el cable C-A Signal
    :class: ars-zoom-img
    ```
* - 8
  - **Conecte el cable C-B SIGNAL** — conector de 19 pines para las señales digitales.
  - 
    ```{image} ../../../../_shared/media/images/connectBSignal.png
    :width:110%
    :alt: Conectar el cable C-B Signal
    :class: ars-zoom-img
    ```
* - 9
  - **Conecte el aire comprimido** con un tubo **Ø 6 mm**, directamente en el panel de la máquina.

    :::{note}
    Para las características del aire requeridas (presión, clase de limpieza ISO) consulte los [Datos técnicos neumáticos](datipneum).
    :::
  - 
    ```{image} ../../../../_shared/media/images/connectAir200.png
    :width:110%
    :alt: Conectar el aire comprimido Ø6mm
    :class: ars-zoom-img
    ```
```
:::{video} ../../../../_shared/media/videos/cablaggio_FB200.mp4
:width: 100% 
:::