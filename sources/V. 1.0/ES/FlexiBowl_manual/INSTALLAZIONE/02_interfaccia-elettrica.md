(intele)=
# **Interfaz eléctrica**

El panel de conectores del FlexiBowl® varía según la versión de la máquina:

:::{raw} html
<style>
.ie-tabs, .ie-wrap, .ie-tabs *, .ie-wrap * {
  box-sizing: border-box;
}
/* Applica margin e padding zero solo ai componenti del tuo pannello se necessario, 
   senza toccare il resto del sito di Sphinx */
.ie-tabs, .ie-panel, .ie-wrap, .ie-row, .ie-bubble, .ie-name, .ie-desc {
  margin: 0;
  padding: 0;
}
:root{
  --acc:#1a6fc4;--acc-dk:#0d4a8a;--acc-bg:#e8f1fb;
  --bd:#e0e0e0;--bg-p:#ffffff;--bg-s:#f7f8f9;--bg-h:#f0f4fa;
  --tx1:#1a1a1a;--tx2:#555;--tx3:#888;
  --r:10px;--tr:0.35s cubic-bezier(.4,0,.2,1);
}
.ie-tabs{display:flex;gap:6px;margin-bottom:12px;flex-wrap:wrap}
.ie-tab{padding:5px 14px;border-radius:6px;border:1.5px solid var(--bd);background:#fff;font-size:13px;font-weight:600;color:var(--tx2);cursor:pointer;transition:background var(--tr),color var(--tr),border-color var(--tr)}
.ie-tab:hover{background:var(--bg-h)}
.ie-tab.on{background:var(--acc-bg);color:var(--acc-dk);border-color:var(--acc)}
.ie-panel{display:none}
.ie-panel.on{display:block}
.ie-wrap{border:1px solid var(--bd);border-radius:var(--r);overflow:hidden;background:var(--bg-p);box-shadow:0 2px 12px rgba(0,0,0,0.07)}
.ie-img-outer{position:relative;width:100%;padding-top:70.71%}
.ie-img-outer img{position:absolute;inset:0;width:100%;height:100%;object-fit:contain;padding:0;transition:opacity var(--tr)}
.ie-img-base{opacity:1;z-index:1}
.ie-img-hl{opacity:0;z-index:2}
.ie-badge{position:absolute;top:12px;left:14px;z-index:3;background:var(--acc);color:#fff;font-size:12px;font-weight:600;padding:4px 10px;border-radius:20px;opacity:0;transform:translateY(-4px);transition:opacity var(--tr),transform var(--tr);pointer-events:none;white-space:nowrap}
.ie-badge.on{opacity:1;transform:translateY(0)}
.ie-hint{position:absolute;bottom:14px;left:50%;z-index:3;transform:translateX(-50%);font-size:13px;color:#fff;background:rgba(0,0,0,0.38);padding:6px 16px;border-radius:20px;pointer-events:none;transition:opacity var(--tr);white-space:nowrap}
.ie-list-panel{border-top:1px solid var(--bd);background:var(--bg-p)}
.ie-list-head{display:grid;grid-template-columns:40px 140px 1fr;gap:8px;padding:8px 14px;background:var(--bg-s);border-bottom:1px solid var(--bd);font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:.05em;color:var(--tx3)}
.ie-row{display:grid;grid-template-columns:40px 140px 1fr;gap:8px;align-items:center;padding:9px 14px;border-bottom:1px solid var(--bd);cursor:pointer;transition:background var(--tr);user-select:none}
.ie-row:last-child{border-bottom:none}
.ie-row:hover{background:var(--bg-h)}
.ie-row.on{background:var(--acc-bg)}
.ie-bubble{width:26px;height:26px;border-radius:50%;border:1.5px solid var(--bd);background:#fff;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:600;color:var(--tx2);flex-shrink:0;transition:background var(--tr),color var(--tr),border-color var(--tr)}
.ie-row.on .ie-bubble{background:var(--acc);color:#fff;border-color:var(--acc)}
.ie-name{font-size:13px;font-weight:600;color:var(--tx1);font-family:monospace;transition:color var(--tr)}
.ie-row.on .ie-name{color:var(--acc-dk)}
.ie-desc{font-size:12px;color:var(--tx2);line-height:1.55}
</style>
 
<!-- Tab bar -->
<div class="ie-tabs">
  <button class="ie-tab on" onclick="ieSwitchTab('smallpanel',this)">Panel FlexiBowl® 200-350</button>
  <button class="ie-tab"    onclick="ieSwitchTab('rack',this)">Rack</button>
  <button class="ie-tab"    onclick="ieSwitchTab('stpanel',this)">Panel estándar</button>
  <button class="ie-tab"    onclick="ieSwitchTab('encpanel',this)">Panel Circular Tracking</button>
</div>
<!-- ══════════ PANNELLO FB200-350 ══════════ -->
<div class="ie-panel on" id="ie-panel-smallpanel">
  <div class="ie-wrap">
    <div class="ie-img-outer">
      <img class="ie-img-base" id="smallpanel-img-base" src="../../../../_shared/media/images/smallpanel0.PNG" alt="Panel FlexiBowl® 200-350" />
      <img class="ie-img-hl"   id="smallpanel-img-hl"   src="" alt="" aria-hidden="true" />
      <div class="ie-badge" id="smallpanel-badge"></div>
      <div class="ie-hint"  id="smallpanel-hint">Seleccione un conector de la lista</div>
    </div>
    <div class="ie-list-panel">
      <div class="ie-list-head"><span>N.º</span><span>Conector</span><span>Descripción</span></div>
      <div id="smallpanel-list"></div>
    </div>
  </div>
</div>
<!-- ══════════ RACK ══════════ -->
<div class="ie-panel" id="ie-panel-rack">
  <div class="ie-wrap">
    <div class="ie-img-outer">
      <img class="ie-img-base" id="rack-img-base" src="../../../../_shared/media/images/rack0.PNG" alt="Rack FlexiBowl®" />
      <img class="ie-img-hl"   id="rack-img-hl"   src="" alt="" aria-hidden="true" />
      <div class="ie-badge" id="rack-badge"></div>
      <div class="ie-hint"  id="rack-hint">Seleccione un conector de la lista</div>
    </div>
    <div class="ie-list-panel">
      <div class="ie-list-head"><span>N.º</span><span>Conector</span><span>Descripción</span></div>
      <div id="rack-list"></div>
    </div>
  </div>
</div>
<!-- ══════════ PANNELLO STANDARD ══════════ -->
<div class="ie-panel" id="ie-panel-stpanel">
  <div class="ie-wrap">
    <div class="ie-img-outer">
      <img class="ie-img-base" id="stpanel-img-base" src="../../../../_shared/media/images/stpanel0.PNG" alt="Panel estándar FlexiBowl®" />
      <img class="ie-img-hl"   id="stpanel-img-hl"   src="" alt="" aria-hidden="true" />
      <div class="ie-badge" id="stpanel-badge"></div>
      <div class="ie-hint"  id="stpanel-hint">Seleccione un conector de la lista</div>
    </div>
    <div class="ie-list-panel">
      <div class="ie-list-head"><span>N.º</span><span>Conector</span><span>Descripción</span></div>
      <div id="stpanel-list"></div>
    </div>
  </div>
</div>
<!-- ══════════ PANNELLO FLEXITRACKING ══════════ -->
<div class="ie-panel" id="ie-panel-encpanel">
  <div class="ie-wrap">
    <div class="ie-img-outer">
      <img class="ie-img-base" id="encpanel-img-base" src="../../../../_shared/media/images/encpanel0.PNG" alt="Panel Circular Tracking FlexiBowl®" />
      <img class="ie-img-hl"   id="encpanel-img-hl"   src="" alt="" aria-hidden="true" />
      <div class="ie-badge" id="encpanel-badge"></div>
      <div class="ie-hint"  id="encpanel-hint">Seleccione un conector de la lista</div>
    </div>
    <div class="ie-list-panel">
      <div class="ie-list-head"><span>N.º</span><span>Conector</span><span>Descripción</span></div>
      <div id="encpanel-list"></div>
    </div>
  </div>
</div>
<script>
(function(){
  var models = {
    smallpanel: {
      imgPath: '../../../../_shared/media/images/smallpanel',
      imgExt: '.PNG',
      comps: [
        {n:1, name:'C-A SIGNAL', desc:'Conector C-A signal'},
        {n:2, name:'C-B SIGNAL', desc:'Conector C-B signal'},
        {n:3, name:'MOTOR',      desc:'Conector del cable del motor'},
        {n:4, name:'C-ETH FB',   desc:'Conexión Ethernet al rack'},
        {n:5, name:'AIR SUPPLY', desc:'Entrada de aire'}
      ]
    },
    rack: {
      imgPath: '../../../../_shared/media/images/rack',
      imgExt: '.PNG',
      comps: [
        {n:1, name:'POWER SUPPLY', desc:'Toma de corriente e interruptor; incluye también un filtro IEC'},
        {n:2, name:'STO',          desc:'Conector STO'},
        {n:3, name:'MOTOR',        desc:'Conector del cable del motor'},
        {n:4, name:'C-A SIGNAL',   desc:'Conector C-A signal'},
        {n:5, name:'C-B SIGNAL',   desc:'Conector C-B signal'},
        {n:6, name:'C-ETH IN',     desc:'Conector Ethernet'},
        {n:7, name:'HOPPER',       desc:'Conector Bulk Feeder'},
        {n:8, name:'C-ETH FB',     desc:'Conexión Ethernet al FlexiBowl®'}
      ]
    },
    stpanel: {
      imgPath: '../../../../_shared/media/images/stpanel',
      imgExt: '.PNG',
      comps: [
        {n:1, name:'POWER SUPPLY', desc:'Toma de corriente e interruptor; incluye también un filtro IEC'},
        {n:2, name:'AIR SUPPLY',   desc:'Entrada de aire'},
        {n:3, name:'LIGHT ON',     desc:'LED de estado del backlight'},
        {n:4, name:'READY/FAULT',  desc:'LED de estado Ready/Fault'},
        {n:5, name:'HOPPER',       desc:'Conector Bulk Feeder'},
        {n:6, name:'C-ETH',        desc:'Conector Ethernet'},
        {n:7, name:'STO',          desc:'Conector STO'}
      ]
    },
    encpanel: {
      imgPath: '../../../../_shared/media/images/encpanel',
      imgExt: '.PNG',
      comps: [
        {n:1, name:'POWER SUPPLY', desc:'Toma de corriente e interruptor; incluye también un filtro IEC'},
        {n:2, name:'LIGHT ON',     desc:'LED de estado del backlight'},
        {n:3, name:'READY/FAULT',  desc:'LED de estado Ready/Fault'},
        {n:4, name:'HOPPER',       desc:'Conector Bulk Feeder'},
        {n:5, name:'C-ETH',        desc:'Conector Ethernet'},
        {n:6, name:'ENCODER',      desc:'Paso del cable del encoder'},
        {n:7, name:'AIR SUPPLY',   desc:'Entrada de aire'},
        {n:8, name:'I/O',          desc:'Conector de E/S'},
        {n:9, name:'STO',          desc:'Conector STO'}
      ]
    }
  };
  var state = {};
  Object.keys(models).forEach(function(id){ state[id]={activeN:null,activeRow:null}; });
  Object.keys(models).forEach(function(id){
    var m  = models[id];
    var el = document.getElementById(id+'-list');
    m.comps.forEach(function(c){
      var row = document.createElement('div');
      row.className = 'ie-row';
      row.innerHTML = '<div class="ie-bubble">'+c.n+'</div>'
                    + '<div class="ie-name">'+c.name+'</div>'
                    + '<div class="ie-desc">'+c.desc+'</div>';
      row.addEventListener('click', function(){ toggle(id, c, row); });
      el.appendChild(row);
    });
  });
  function toggle(id, c, row){
    var s       = state[id];
    var m       = models[id];
    var imgBase = document.getElementById(id+'-img-base');
    var imgHl   = document.getElementById(id+'-img-hl');
    var badge   = document.getElementById(id+'-badge');
    var hint    = document.getElementById(id+'-hint');
    if(s.activeN === c.n){ reset(id); return; }
    if(s.activeRow) s.activeRow.classList.remove('on');
    row.classList.add('on');
    s.activeRow = row; s.activeN = c.n;
    badge.textContent = c.name + ' \u2014 ' + c.desc;
    badge.classList.add('on');
    hint.style.opacity = '0';
    var newImg = new Image();
    newImg.onload = function(){
      imgHl.src = newImg.src;
      imgHl.style.opacity = '1';
      imgBase.style.opacity = '0';
    };
    newImg.onerror = function(){
      imgBase.style.opacity = '1';
      imgHl.style.opacity = '0';
    };
    newImg.src = m.imgPath + c.n + m.imgExt;
  }
  function reset(id){
    var s       = state[id];
    var imgBase = document.getElementById(id+'-img-base');
    var imgHl   = document.getElementById(id+'-img-hl');
    var badge   = document.getElementById(id+'-badge');
    var hint    = document.getElementById(id+'-hint');
    if(s.activeRow) s.activeRow.classList.remove('on');
    s.activeRow = null; s.activeN = null;
    imgBase.style.opacity = '1';
    imgHl.style.opacity = '0';
    setTimeout(function(){ imgHl.src = ''; }, 350);
    badge.classList.remove('on');
    hint.style.opacity = '1';
  }
  window.ieSwitchTab = function(id, btn){
    document.querySelectorAll('.ie-panel.on').forEach(function(p){
      var oldId = p.id.replace('ie-panel-','');
      reset(oldId);
    });
    document.querySelectorAll('.ie-tab').forEach(function(b){ b.classList.remove('on'); });
    document.querySelectorAll('.ie-panel').forEach(function(p){ p.classList.remove('on'); });
    btn.classList.add('on');
    document.getElementById('ie-panel-'+id).classList.add('on');
  };
})();
</script>
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

:::{warning}
Antes de realizar cualquier conexión eléctrica, asegurarse de que la alimentación esté desconectada y de que el sistema se encuentre en estado seguro.
:::

:::{important}
Dejar unos {ref}`100 mm de espacio libre <dim800>` alrededor de los conectores de alimentación para facilitar las operaciones de cableado y mantenimiento.
:::

La interfaz eléctrica del FlexiBowl® cambia según el tamaño de la máquina:

- **FlexiBowl® 500 – 1200**: todos los conectores (STO, Ethernet, Hopper, alimentación, aire) se encuentran en un único **panel eléctrico estándar**, montado directamente en la máquina.
- **FlexiBowl® 200 / 350**: los conectores principales se encuentran en un **rack** externo; el rack se conecta después a la máquina mediante 4 cables específicos (Ethernet, Motor+STO, señal A, señal B). En la máquina solo queda por conectar el aire comprimido.

---

(pannello-standard)=
## FlexiBowl® 500 – 1200 — Panel eléctrico estándar

```{list-table}
:widths: 8 52 40
:header-rows: 1

* - #
  - Acción
  - Imagen
* - 1
  - **Conectar el STO.**

    Conector de 10 pines. Necesario para activar el motor.

    <div class="ars-step-note">
    Las entradas <strong>+STO1</strong> y <strong>+STO2</strong> deben recibir <strong>+24 Vdc</strong> del circuito de seguridad; <strong>−STO1</strong> y <strong>−STO2</strong> deben conectarse a la referencia −24 Vdc.
    </div>

    <details class="ars-dropdown"><summary>Distribución de pines del conector STO (10 pines)</summary><div class="ars-dropdown-body">

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
    ```{image} ../../../../_shared/media/images/stpanel7.PNG
    :alt: Conectar el STO
    :class: ars-zoom-img
    ```

* - 2
  - **Conectar el Ethernet (C-ETH).**

    Conector M12, codificación D. Permite la comunicación con el FlexiBowl®, al que también se puede acceder mediante navegador web.

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
    ```{image} ../../../../_shared/media/images/stpanel6.PNG
    :alt: Conectar el Ethernet
    :class: ars-zoom-img
    ```

* - 3
  - **Conectar el Hopper.**

    Conector M12 código A, utilizado para comunicarse con los controladores de hopper ARS mediante el protocolo **Modbus RTU**.

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
    ```{image} ../../../../_shared/media/images/stpanel5.PNG
    :alt: Conectar el Hopper
    :class: ars-zoom-img
    ```

* - 4
  - **Conectar la alimentación (Power Supply) — en último lugar.**

    Conector suministrado con la unidad, identificado con la sigla **POWER SUPPLY**. El pulsador de alimentación permite encender/apagar el dispositivo.

    <div class="ars-step-attn">
    Asegurarse de que el FlexiBowl® esté <strong>apagado</strong> antes de conectar la alimentación y de que el dispositivo esté conectado a tierra.
    </div>

    <div class="ars-step-warn">
    Tensión admitida: <strong>120–230 Vac, 50/60 Hz</strong>.
    </div>

    <div class="ars-step-note">
    El conector de alimentación dispone de un soporte para alojar <strong>2 fusibles</strong>, con función de protección frente a posibles anomalías eléctricas. En el primer arranque, comprobar siempre su estado antes de encender el dispositivo.
    </div>

    <details class="ars-dropdown"><summary>Esquema de distribución de pines del cable de alimentación</summary><div class="ars-dropdown-body">

    | Color | Tipo | Etiqueta |
    |---|---|---|
    | Marrón | Fase | L1 |
    | Azul | Neutro | N1 |
    | Amarillo/Verde | Tierra | PE1 |

    </div></details>
  -
    ```{image} ../../../../_shared/media/images/stpanel1.PNG
    :alt: Conectar la alimentación
    :class: ars-zoom-img
    ```

```

:::{note}
Tras el encendido, comprobar siempre el estado de la máquina mediante los **LED de estado** del panel frontal — véase la sección {ref}`LED de estado <led-stato>` más abajo en esta página.
:::

:::{tip}
Los cables de alimentación y Ethernet están disponibles como opción en longitudes de 3, 5 y 10 m: véase {ref}`cavo-alim` y {ref}`cavo-eth`.
:::

---

(rack-esterno)=
## FlexiBowl® 200 / 350 — Rack externo

Los modelos FlexiBowl® FB 200 y FB 350 están dotados de un **Rack** externo, que contiene todos los dispositivos electrónicos necesarios para el funcionamiento. Los conectores hacia las instalaciones del cliente se encuentran en el rack (no en la máquina) y tienen la **misma distribución de pines** que los correspondientes conectores del panel estándar, simplemente colocados en una caja externa.

### Conexiones en el rack

```{list-table}
:widths: 8 52 40
:header-rows: 1

* - #
  - Acción
  - Imagen
* - 1
  - **Conectar el STO** en el rack.

    Conector de 10 pines, misma función y distribución de pines que el panel estándar.

    <div class="ars-step-note">
    Las entradas <strong>+STO1</strong> y <strong>+STO2</strong> deben recibir <strong>+24 Vdc</strong> del circuito de seguridad; <strong>−STO1</strong> y <strong>−STO2</strong> deben conectarse a la referencia −24 Vdc.
    </div>

    <details class="ars-dropdown"><summary>Distribución de pines del conector STO (10 pines)</summary><div class="ars-dropdown-body">

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
    ```{image} ../../../../_shared/media/images/rack2.PNG
    :alt: Conectar el STO
    :class: ars-zoom-img
    ```

* - 2
  - **Conectar el C-ETH IN** en el rack.

    Conector M12, codificación D.

    <div class="ars-step-attn">
    Conexión <strong>obligatoria</strong> con la máquina alimentada: si falta, la máquina pasa a ERROR (LED Ready/Fault rojo).
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
    ```{image} ../../../../_shared/media/images/rack6.PNG
    :width: 110%
    :alt: Panel del rack
    :class: ars-zoom-img
    ```

* - 3
  - **Conectar el Hopper** en el rack.

    Conector M12 código A, protocolo **Modbus RTU**.

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
    ```{image} ../../../../_shared/media/images/rack7.PNG
    :width: 110%
    :alt: Panel del rack
    :class: ars-zoom-img
    ```

* - 4
  - **Conectar la alimentación** en el rack — en último lugar.

    Toma de corriente con interruptor; incluye también un filtro IEC.

    <div class="ars-step-attn">
    Asegurarse de que el FlexiBowl® esté <strong>apagado</strong> antes de conectar la alimentación.
    </div>

    <div class="ars-step-warn">
    Tensión admitida: <strong>120–230 Vac, 50/60 Hz</strong>.
    </div>

    <div class="ars-step-note">
    También en el rack, el conector de alimentación dispone del alojamiento para los <strong>2 fusibles</strong> de protección: comprobar su estado en el primer arranque.
    </div>

    <details class="ars-dropdown"><summary>Esquema de distribución de pines del cable de alimentación</summary><div class="ars-dropdown-body">

    | Color | Tipo | Etiqueta |
    |---|---|---|
    | Marrón | Fase | L1 |
    | Azul | Neutro | N1 |
    | Amarillo/Verde | Tierra | PE1 |

    </div></details>
  -
    ```{image} ../../../../_shared/media/images/rack1.PNG
    :width: 110%
    :alt: Panel del rack
    :class: ars-zoom-img
    ```
```

(collegamento-rack)=
### Conexión entre el rack y el FlexiBowl®

El rack se comunica con el FlexiBowl® mediante 4 cables específicos, cada uno de los cuales debe conectarse **exclusivamente** al puerto con la etiqueta correspondiente del panel de la máquina.

:::{attention}
Conectar cada cable al puerto con la **etiqueta correspondiente** (p. ej., MOTOR ↔ MOTOR, C-A SIGNAL ↔ C-A SIGNAL). Una conexión cruzada puede dañar el sistema.
:::

:::{tip}
Los cables de 3 m entre el rack y el FlexiBowl® están incluidos en el suministro; las versiones de 5 y 10 m están disponibles como opción: véase {ref}`cavo-rack`.
:::

```{list-table}
:widths: 8 52 40
:header-rows: 1

* - #
  - Acción
  - Imagen
* - 5
  - **Conectar el cable Ethernet (C-ETH FB)** entre el rack y el FlexiBowl®.

    Conector M12 código D.
  -
    ```{image} ../../../../_shared/media/images/rack8.PNG
    :width: 110%
    :alt: Conectar el cable C-ETH FB
    :class: ars-zoom-img
    ```
    ```{image} ../../../../_shared/media/images/smallpanel4.PNG
    :width: 110%
    :alt: Conectar el cable C-ETH FB
    :class: ars-zoom-img
    ```
* - 6
  - **Conectar el cable MOTOR.**

    <div class="ars-step-note">
    Conector de 9 pines: transporta tanto la alimentación del motor como las señales <strong>STO</strong> hacia el FlexiBowl® (en el rack, STO y Motor son conectores separados; en el cable hacia la máquina están combinados en un único conector de 9 pines).
    </div>

    <details class="ars-dropdown"><summary>Distribución de pines del conector Motor (9 pines)</summary><div class="ars-dropdown-body">

    | Pin | Descripción |
    |---|---|
    | 1 | +STO1 – Safe Torque Off |
    | 2 | +24 Vdc – Alimentación auxiliar |
    | 3 | +STO2 – Safe Torque Off |
    | 4 | −24 Vdc – Alimentación auxiliar |
    | 5 | NC |
    | 6 | +48 Vdc – Motor Power |
    | 7 | −STO1 – Safe Torque Off |
    | 8 | −48 Vdc – Motor Power |
    | 9 | −STO2 – Safe Torque Off |

    </div></details>
  -
    ```{image} ../../../../_shared/media/images/rack3.PNG
    :width: 110%
    :alt: Conectar el cable Motor
    :class: ars-zoom-img
    ```
    ```{image} ../../../../_shared/media/images/smallpanel3.PNG
    :width: 110%
    :alt: Conectar el cable C-ETH FB
    :class: ars-zoom-img
    ```
* - 7
  - **Conectar el cable C-A SIGNAL.**

    Conector de 12 pines para señales analógicas.

    <details class="ars-dropdown"><summary>Distribución de pines C-A Signal (12 pines)</summary><div class="ars-dropdown-body">

    | Pin | Descripción |
    |---|---|
    | 1 | Analog Output 1 |
    | 2 | −24 Vdc |
    | 3 | Analog Input 1 |
    | 4 | +24 Vdc |
    | 5–12 | NC |

    </div></details>
  -
    ```{image} ../../../../_shared/media/images/rack4.PNG
    :width: 110%
    :alt: Conectar el cable C-A Signal
    :class: ars-zoom-img
    ```
    ```{image} ../../../../_shared/media/images/smallpanel1.PNG
    :width: 110%
    :alt: Conectar el cable C-ETH FB
    :class: ars-zoom-img
    ```
* - 8
  - **Conectar el cable C-B SIGNAL.**

    Conector de 19 pines para señales digitales, incluidas las activaciones de los LED de estado.

    <details class="ars-dropdown"><summary>Distribución de pines C-B Signal (19 pines)</summary><div class="ars-dropdown-body">

    | Pin | Descripción |
    |---|---|
    | 1 | +24 Vdc – Activación del LED de estado verde |
    | 2 | −24 Vdc – Común de los LED de estado |
    | 3 | +24 Vdc – Activación del LED de estado rojo |
    | 4 | +24 Vdc – Activación del LED de estado del Backlight |
    | 5 | −24 Vdc – Activación del LED de estado del Backlight |
    | 6 | +24 Vdc – Activación del Backlight |
    | 7 | −24 Vdc – Activación del Backlight |
    | 8 | +24 Vdc – Activación del Flip |
    | 9 | −24 Vdc – Activación del Flip |
    | 10 | +24 Vdc – Activación del Blow |
    | 11 | −24 Vdc – Activación del Blow |
    | 12–19 | NC |

    </div></details>
  -
    ```{image} ../../../../_shared/media/images/rack5.PNG
    :width: 110%
    :alt: Conectar el cable C-B Signal
    :class: ars-zoom-img
    ```
    ```{image} ../../../../_shared/media/images/smallpanel2.PNG
    :width: 110%
    :alt: Conectar el cable C-ETH FB
    :class: ars-zoom-img
    ```
```

:::{note}
Tras el encendido, comprobar siempre el estado de la máquina mediante los **LED de estado** del panel frontal — véase la sección {ref}`LED de estado <led-stato>` más abajo en esta página.
:::

---

(led-stato)=
## LED de estado

En el panel frontal del FlexiBowl® hay dos LED de estado, comunes a **todos los tamaños** (500–1200 y 200/350):

| LED | Color | Significado |
|---|---|---|
| **Light ON** | Verde (único estado) | Indica si el backlight a bordo del FlexiBowl® está ON u OFF. El backlight lo utiliza el sistema de visión para iluminar los componentes y hacerlos reconocibles. Se puede activar mediante el software de visión o mediante comandos procedentes de un sistema externo que se comunique por Ethernet. |
| **Ready / Fault** | Verde | Sistema operativo y sin anomalías. Conexión Ethernet correcta. |
| **Ready / Fault** | Rojo | Anomalía interna o anomalía en la conexión Ethernet. Consulte la tabla de anomalías. |

:::{note}
Tras el encendido, esperar a que se encienda el LED **Ready/Fault**: si el Hopper y el C-ETH están correctamente conectados, el LED será **verde**.
:::

---

(io-flexitrack)=
## Opción Circular Tracking — Panel de interfaz

El pequeño panel suministrado con la opción Circular Tracking añade, además de las conexiones ya descritas, los siguientes conectores específicos:

- **Conector de E/S**: intercambio de señales digitales, incluida la función Latch.
- **Pasacables del encoder**: destinado al encoder interno del FlexiBowl®.

```{list-table}
:widths: 8 52 40
:header-rows: 1

* - #
  - Acción
  - Imagen
* - 10
  - **Conectar el conector de E/S** de 19 pines.

    <details class="ars-dropdown"><summary>Distribución de pines del conector de E/S (19 pines)</summary><div class="ars-dropdown-body">

    | Pin | Señal |
    |---|---|
    | 1 | IN – Bit 1 – Seq. Cmd |
    | 2 | IN – Bit 2 – Seq. Cmd |
    | 3 | IN – Bit 3 – Seq. Cmd |
    | 4 | IN – Bit 4 – Seq. Cmd |
    | 5 | IN – Bit 5 – Seq. Cmd |
    | 6 | IN – Latch |
    | 7–8 | NC |
    | 9 | OUT – Ready |
    | 10 | OUT – Fault |
    | 11 | OUT – Busy |
    | 12 | OUT – Hopper_1_IsVibrating |
    | 13 | OUT – Hopper_2_IsVibrating |
    | 14 | OUT – Hopper_3_IsVibrating |
    | 15 | OUT – Hopper_4_IsVibrating |
    | 16–19 | NC |

    </div></details>
  -
    ```{image} ../../../../_shared/media/images/encpanel6.PNG
    :alt: Conector de E/S Circular Tracking
    :class: ars-zoom-img
    ```
* - 11
  - **Conectar el pasacables del encoder**, destinado al encoder interno del FlexiBowl®.
  -
    ```{image} ../../../../_shared/media/images/encpanel8.PNG
    :alt: Pasacables del encoder Circular Tracking
    :class: ars-zoom-img
    ```
```

---

## Notas y advertencias generales

:::{attention}
Todas las operaciones de conexión deben realizarse con el dispositivo apagado y desconectado de la alimentación.
:::

:::{attention}
La conexión a tierra es obligatoria y debe comprobarse antes de cada encendido.
:::

:::{attention}
En caso de anomalía indicada por el LED rojo (Ready/Fault), consulte la tabla de anomalías específica del modelo.
:::

:::{attention}
Para más información técnica o asistencia, póngase en contacto con ARS s.r.l. – FlexiBowl® Division.
:::


