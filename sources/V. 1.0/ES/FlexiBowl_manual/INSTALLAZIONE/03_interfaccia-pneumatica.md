(intpneum)=
# **Interfaz neumática**

La máquina está equipada con accionamiento neumático. Antes de realizar la **conexión neumática**, comprobar que:
- la instalación de suministro de aire comprimido existente garantice a la máquina la cantidad de aire a la presión adecuada;
- el depósito de aire comprimido previsto esté correctamente dimensionado.

La conexión neumática debe realizarse conectando la línea principal al circuito de la máquina. El cliente debe además garantizar un suministro de aire con las características indicadas en el apartado {ref}`«Datos técnicos neumáticos» <datipneum>` de este manual.

:::{warning}
No superar nunca los 7 bar de presión en el sistema neumático de la máquina.
:::

:::{warning}
El FlexiBowl® se suministra sin dispositivo manual de corte y descarga de la alimentación neumática. El integrador debe prever aguas arriba un dispositivo claramente identificado, fácilmente accesible y bloqueable en posición cerrada, que permita interrumpir la alimentación, descargar la presión residual y evitar reactivaciones involuntarias. Las tuberías y los racores deben ser adecuados para la presión de servicio, estar correctamente fijados y protegidos contra el desprendimiento. Los posibles dispositivos neumáticos de seguridad adicionales deben definirse mediante la evaluación de riesgos de la máquina final.
:::

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

Para la conexión a la red neumática, conectar un tubo de aire {ref}`del tamaño adecuado <datipneum>` a la entrada «Air Supply» situada en el {ref}`panel de control <intele>`.

:::{raw} html
<style>
.img-zoom-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 16px;
  padding: 1rem 0;
}
.img-zoom-wrap {
  flex: 1 1 0;
  min-width: 0;
  overflow: visible;
  display: flex;
  align-items: center;
  justify-content: center;
}
.img-zoom-wrap img {
  width: 100%;
  border-radius: 8px;
  transition: transform 0.35s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.35s ease;
  cursor: zoom-in;
  position: relative;
  transform: scale(1);
}
.img-zoom-wrap img:hover {
  transform: scale(1.85);
  box-shadow: 0 12px 40px rgba(0,0,0,0.22);
  z-index: 10;
}
</style>

<div class="img-zoom-grid">
  <div class="img-zoom-wrap">
    <img src="../../../../_shared/media/images/smallpanel5.PNG" alt="Panel small" />
  </div>
  <div class="img-zoom-wrap">
    <img src="../../../../_shared/media/images/stpanel2.PNG" alt="Panel ST" />
  </div>
  <div class="img-zoom-wrap">
    <img src="../../../../_shared/media/images/encpanel7.PNG" alt="Panel ENC" />
  </div>
</div>
:::

<style>
.ars-dropdown {
  margin: 0.9rem 0 0.4rem 0;
  border: 2px solid #7fb3dd;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 6px rgba(26,111,196,0.10);
}
.ars-dropdown summary {
  cursor: pointer;
  color: #2980b9;
  font-weight: 600;
  font-size: 0.83rem;
  padding: 0.5rem 0.9rem;
  display: block;
  background: #eaf3fb;
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
  border-bottom: 2px solid #7fb3dd;
}
.ars-dropdown .ars-dropdown-body {
  padding: 0.9rem 1rem;
  background: #fff;
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

---

## Características del aire requeridas

| Parámetro | Valor |
|---|---|
| Calidad del aire | Aire comprimido limpio y seco, según **ISO 8573-1:2010, clase 1.3.2** |
| Presión de alimentación recomendada | **7 bar** (no debe superarse nunca) |
| Diámetro del tubo — FB200 / FB350 | **Ø 6 mm** |
| Diámetro del tubo — FB500E / FB500 / FB650 / FB800 / FB1200 | **Ø 8 mm** |

<details class="ars-dropdown"><summary>Consumo de aire indicativo por modelo (acción Flip)</summary><div class="ars-dropdown-body">

| Modelo | Consumo medio | Consumo máximo |
|---|---|---|
| FB200 | 25 l/min | 45 l/min |
| FB350 | 15 l/min | 24 l/min |
| FB500E | 55 l/min | 74 l/min |
| FB500 | 35 l/min | 48 l/min |
| FB650 | 30 l/min | 45 l/min |
| FB800 | 45 l/min | 60 l/min |
| FB1200 | 135 l/min | 176 l/min |

Los valores indicados se refieren únicamente a la acción Flip; para los detalles completos sobre los consumos, consulte el apartado {ref}`«Datos técnicos neumáticos» <datipneum>`.

</div></details>

:::{note}
En el FlexiBowl® 3.0, la regulación de la presión y la lectura del manómetro se realizan mediante la **interfaz de software**, y ya no con un regulador y un manómetro físicos en el panel como en la generación anterior 2.0.
:::

---

## Procedimiento guiado — Conexión neumática

También en la conexión neumática el procedimiento cambia ligeramente según el tamaño de la máquina, en particular en cuanto al diámetro del tubo y la posición del conector **AIR SUPPLY**.

:::{attention}
Antes de iniciar cualquier conexión neumática, asegurarse de que la alimentación de aire comprimido esté **desconectada** y de que la presión residual del circuito se haya **descargado**.
:::

### FlexiBowl® 500 – 1200 — Panel eléctrico estándar

```{list-table}
:widths: 8 52 40
:header-rows: 1

* - #
  - Acción
  - Imagen
* - 1
  - **Comprobaciones preliminares.**

    Comprobar que la instalación de suministro garantice la presión y el caudal requeridos, y que el depósito de aire comprimido esté correctamente dimensionado para el modelo instalado.

    <div class="ars-step-note">
    Aire limpio y seco según ISO 8573-1:2010, clase 1.3.2. Presión recomendada: 7 bar.
    </div>
  -

* - 2
  - **Desconectar la alimentación de aire** aguas arriba de la instalación, antes de conectar el tubo.

    <div class="ars-step-attn">
    No conectar ni desconectar nunca el tubo de aire con la instalación todavía bajo presión.
    </div>
  -

* - 3
  - **Conectar el tubo de aire** a la entrada **AIR SUPPLY** del panel eléctrico estándar, utilizando un tubo con diámetro exterior de **Ø 8 mm**.
  -
    ```{image} ../../../../_shared/media/images/connectAir.png
    :alt: Conectar el aire comprimido Ø8mm
    :class: ars-zoom-img
    ```

* - 4
  - **Comprobar la estanqueidad de la conexión**: verificar que el racor esté correctamente insertado y que no haya fugas audibles o perceptibles al tacto a lo largo del tubo y del racor.
  -

* - 5
  - **Restablecer la alimentación de aire** y comprobar que la presión aguas abajo se encuentre dentro de los parámetros previstos.

    <div class="ars-step-note">
    En el FlexiBowl® 3.0, la presión se puede leer y regular directamente desde la interfaz de software.
    </div>
  -
```

### FlexiBowl® 200 / 350

En estos tamaños, el conector **AIR SUPPLY** se encuentra directamente en el panel de la máquina (no en el rack externo), a continuación de todos los demás cableados.

```{list-table}
:widths: 8 52 40
:header-rows: 1

* - #
  - Acción
  - Imagen
* - 1
  - **Comprobaciones preliminares.**

    Comprobar que la instalación de suministro garantice la presión y el caudal requeridos, y que el depósito de aire comprimido esté correctamente dimensionado para el modelo instalado.

    <div class="ars-step-note">
    Aire limpio y seco según ISO 8573-1:2010, clase 1.3.2. Presión recomendada: 7 bar.
    </div>
  -

* - 2
  - **Desconectar la alimentación de aire** aguas arriba de la instalación, antes de conectar el tubo.

    <div class="ars-step-attn">
    No conectar ni desconectar nunca el tubo de aire con la instalación todavía bajo presión.
    </div>
  -

* - 3
  - **Conectar el tubo de aire** directamente al panel de la máquina, utilizando un tubo con diámetro exterior de **Ø 6 mm**.
  -
    ```{image} ../../../../_shared/media/images/connectAir200.png
    :width: 110%
    :alt: Conectar el aire comprimido Ø6mm
    :class: ars-zoom-img
    ```

* - 4
  - **Comprobar la estanqueidad de la conexión**: verificar que el racor esté correctamente insertado y que no haya fugas audibles o perceptibles al tacto a lo largo del tubo y del racor.
  -

* - 5
  - **Restablecer la alimentación de aire** y comprobar que la presión aguas abajo se encuentre dentro de los parámetros previstos.

    <div class="ars-step-note">
    En el FlexiBowl® 3.0, la presión se puede leer y regular directamente desde la interfaz de software.
    </div>
  -
```

---

## Notas y advertencias generales

:::{attention}
Todas las operaciones de conexión y desconexión neumática deben realizarse con la instalación **desconectada** y la **presión residual descargada**.
:::

:::{attention}
No superar nunca los **7 bar** de presión en el sistema neumático de la máquina.
:::

:::{attention}
El FlexiBowl® no está equipado con un dispositivo manual de corte y descarga: es responsabilidad del integrador prever uno aguas arriba, claramente identificado, accesible y bloqueable en posición cerrada.
:::

:::{attention}
Utilizar exclusivamente tubos y racores adecuados para la presión de servicio, correctamente fijados y protegidos contra el desprendimiento.
:::

:::{attention}
Para más información técnica o asistencia, póngase en contacto con ARS s.r.l. – FlexiBowl® Division.
:::
