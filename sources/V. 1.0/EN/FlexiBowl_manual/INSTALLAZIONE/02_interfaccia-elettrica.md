(intele)=
# **Electrical Interface**

The FlexiBowl® connector panel varies depending on the machine version:

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
  <button class="ie-tab on" onclick="ieSwitchTab('smallpanel',this)">FlexiBowl® 200-350 panel</button>
  <button class="ie-tab"    onclick="ieSwitchTab('rack',this)">Rack</button>
  <button class="ie-tab"    onclick="ieSwitchTab('stpanel',this)">Standard panel</button>
  <button class="ie-tab"    onclick="ieSwitchTab('encpanel',this)">Circular Tracking panel</button>
</div>
<!-- ══════════ PANNELLO FB200-350 ══════════ -->
<div class="ie-panel on" id="ie-panel-smallpanel">
  <div class="ie-wrap">
    <div class="ie-img-outer">
      <img class="ie-img-base" id="smallpanel-img-base" src="../../../../_shared/media/images/smallpanel0.PNG" alt="FlexiBowl® 200-350 panel" />
      <img class="ie-img-hl"   id="smallpanel-img-hl"   src="" alt="" aria-hidden="true" />
      <div class="ie-badge" id="smallpanel-badge"></div>
      <div class="ie-hint"  id="smallpanel-hint">Select a connector from the list</div>
    </div>
    <div class="ie-list-panel">
      <div class="ie-list-head"><span>No.</span><span>Connector</span><span>Description</span></div>
      <div id="smallpanel-list"></div>
    </div>
  </div>
</div>
<!-- ══════════ RACK ══════════ -->
<div class="ie-panel" id="ie-panel-rack">
  <div class="ie-wrap">
    <div class="ie-img-outer">
      <img class="ie-img-base" id="rack-img-base" src="../../../../_shared/media/images/rack0.PNG" alt="FlexiBowl® rack" />
      <img class="ie-img-hl"   id="rack-img-hl"   src="" alt="" aria-hidden="true" />
      <div class="ie-badge" id="rack-badge"></div>
      <div class="ie-hint"  id="rack-hint">Select a connector from the list</div>
    </div>
    <div class="ie-list-panel">
      <div class="ie-list-head"><span>No.</span><span>Connector</span><span>Description</span></div>
      <div id="rack-list"></div>
    </div>
  </div>
</div>
<!-- ══════════ PANNELLO STANDARD ══════════ -->
<div class="ie-panel" id="ie-panel-stpanel">
  <div class="ie-wrap">
    <div class="ie-img-outer">
      <img class="ie-img-base" id="stpanel-img-base" src="../../../../_shared/media/images/stpanel0.PNG" alt="FlexiBowl® Standard panel" />
      <img class="ie-img-hl"   id="stpanel-img-hl"   src="" alt="" aria-hidden="true" />
      <div class="ie-badge" id="stpanel-badge"></div>
      <div class="ie-hint"  id="stpanel-hint">Select a connector from the list</div>
    </div>
    <div class="ie-list-panel">
      <div class="ie-list-head"><span>No.</span><span>Connector</span><span>Description</span></div>
      <div id="stpanel-list"></div>
    </div>
  </div>
</div>
<!-- ══════════ PANNELLO FLEXITRACKING ══════════ -->
<div class="ie-panel" id="ie-panel-encpanel">
  <div class="ie-wrap">
    <div class="ie-img-outer">
      <img class="ie-img-base" id="encpanel-img-base" src="../../../../_shared/media/images/encpanel0.PNG" alt="FlexiBowl® Circular Tracking panel" />
      <img class="ie-img-hl"   id="encpanel-img-hl"   src="" alt="" aria-hidden="true" />
      <div class="ie-badge" id="encpanel-badge"></div>
      <div class="ie-hint"  id="encpanel-hint">Select a connector from the list</div>
    </div>
    <div class="ie-list-panel">
      <div class="ie-list-head"><span>No.</span><span>Connector</span><span>Description</span></div>
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
        {n:1, name:'C-A SIGNAL', desc:'C-A signal connector'},
        {n:2, name:'C-B SIGNAL', desc:'C-B signal connector'},
        {n:3, name:'MOTOR',      desc:'Motor cable connector'},
        {n:4, name:'C-ETH FB',   desc:'Ethernet connection to the rack'},
        {n:5, name:'AIR SUPPLY', desc:'Air inlet'}
      ]
    },
    rack: {
      imgPath: '../../../../_shared/media/images/rack',
      imgExt: '.PNG',
      comps: [
        {n:1, name:'POWER SUPPLY', desc:'Power inlet and switch; also includes an IEC filter'},
        {n:2, name:'STO',          desc:'STO connector'},
        {n:3, name:'MOTOR',        desc:'Motor cable connector'},
        {n:4, name:'C-A SIGNAL',   desc:'C-A signal connector'},
        {n:5, name:'C-B SIGNAL',   desc:'C-B signal connector'},
        {n:6, name:'C-ETH IN',     desc:'Ethernet connector'},
        {n:7, name:'HOPPER',       desc:'Bulk Feeder connector'},
        {n:8, name:'C-ETH FB',     desc:'Ethernet connection to the FlexiBowl®'}
      ]
    },
    stpanel: {
      imgPath: '../../../../_shared/media/images/stpanel',
      imgExt: '.PNG',
      comps: [
        {n:1, name:'POWER SUPPLY', desc:'Power inlet and switch; also includes an IEC filter'},
        {n:2, name:'AIR SUPPLY',   desc:'Air inlet'},
        {n:3, name:'LIGHT ON',     desc:'Backlight status LED'},
        {n:4, name:'READY/FAULT',  desc:'Ready/Fault status LED'},
        {n:5, name:'HOPPER',       desc:'Bulk Feeder connector'},
        {n:6, name:'C-ETH',        desc:'Ethernet connector'},
        {n:7, name:'STO',          desc:'STO connector'}
      ]
    },
    encpanel: {
      imgPath: '../../../../_shared/media/images/encpanel',
      imgExt: '.PNG',
      comps: [
        {n:1, name:'POWER SUPPLY', desc:'Power inlet and switch; also includes an IEC filter'},
        {n:2, name:'LIGHT ON',     desc:'Backlight status LED'},
        {n:3, name:'READY/FAULT',  desc:'Ready/Fault status LED'},
        {n:4, name:'HOPPER',       desc:'Bulk Feeder connector'},
        {n:5, name:'C-ETH',        desc:'Ethernet connector'},
        {n:6, name:'ENCODER',      desc:'Encoder cable passage'},
        {n:7, name:'AIR SUPPLY',   desc:'Air inlet'},
        {n:8, name:'I/O',          desc:'I/O connector'},
        {n:9, name:'STO',          desc:'STO connector'}
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
Before making any electrical connection, make sure that the power supply is disconnected and that the system is in a safe state.
:::

:::{important}
Leave about {ref}`100 mm of free space <dim800>` around the power connectors to facilitate wiring and maintenance operations.
:::

The electrical interface of the FlexiBowl® changes depending on the size of the machine:

- **FlexiBowl® 500 – 1200**: all connectors (STO, Ethernet, Hopper, power supply, air) are located on a single **standard electrical panel**, mounted directly on the machine.
- **FlexiBowl® 200 / 350**: the main connectors are located on an external **rack**; the rack is then connected to the machine via 4 dedicated cables (Ethernet, Motor+STO, signal A, signal B). Only the compressed air remains to be connected on the machine.

---

(pannello-standard)=
## FlexiBowl® 500 – 1200 — Standard Electrical Panel

```{list-table}
:widths: 8 52 40
:header-rows: 1

* - #
  - Action
  - Image
* - 1
  - **Connect the STO.**

    10-pin connector. Required to enable the motor.

    <div class="ars-step-note">
    The <strong>+STO1</strong> and <strong>+STO2</strong> inputs must receive <strong>+24 Vdc</strong> from the safety circuit; <strong>−STO1</strong> and <strong>−STO2</strong> must be connected to the −24 Vdc reference.
    </div>

    <details class="ars-dropdown"><summary>STO connector pinout (10 pin)</summary><div class="ars-dropdown-body">

    | Pin | Description |
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
    :alt: Connect the STO
    :class: ars-zoom-img
    ```

* - 2
  - **Connect the Ethernet (C-ETH).**

    M12 connector, D-Code coding. It allows communication with the FlexiBowl®, which can also be accessed via web browser.

    <div class="ars-step-attn">
    When the FlexiBowl® is powered, the Ethernet connection is <strong>mandatory</strong>: if absent, the machine enters the <strong>ERROR</strong> state (red Ready/Fault LED).
    </div>

    <details class="ars-dropdown"><summary>M12 → RJ45 pinout</summary><div class="ars-dropdown-body">

    8-pole M12 → RJ45 adapter:

    | RJ45 pin | Signal | Function | Color |
    |---|---|---|---|
    | 1 | TD+ | Data transmission (+) | Yellow |
    | 2 | TD− | Data transmission (−) | Orange |
    | 3 | RD+ | Data reception (+) | White |
    | 4 | NC | Not assigned | — |
    | 5 | NC | Not assigned | — |
    | 6 | RD− | Data reception (−) | Blue |
    | 7 | NC | Not assigned | — |
    | 8 | NC | Not assigned | — |

    4-pole M12 D-code connector:

    | M12 pin | Signal | Function | Color |
    |---|---|---|---|
    | 1 | TD+ | Data transmission (+) | Yellow |
    | 2 | RD+ | Data reception (+) | White |
    | 3 | TD− | Data transmission (−) | Orange |
    | 4 | RD− | Data reception (−) | Blue |

    </div></details>
  -
    ```{image} ../../../../_shared/media/images/stpanel6.PNG
    :alt: Connect the Ethernet
    :class: ars-zoom-img
    ```

* - 3
  - **Connect the Hopper.**

    M12 A-code connector, used to communicate with ARS hopper controllers via **Modbus RTU** protocol.

    <details class="ars-dropdown"><summary>M12 A-code pinout</summary><div class="ars-dropdown-body">

    | M12 pin | Signal | Function | Color |
    |---|---|---|---|
    | 1 | A+ | RS485 data line (+) | Brown |
    | 2 | NC | Not assigned | White |
    | 3 | B− | RS485 data line (−) | Blue |
    | 4 | GND | Common reference | Black |
    | 5 | NC | Not assigned | Gray |

    </div></details>
  -
    ```{image} ../../../../_shared/media/images/stpanel5.PNG
    :alt: Connect the Hopper
    :class: ars-zoom-img
    ```

* - 4
  - **Connect the power supply (Power Supply) — last.**

    Connector supplied with the unit, identified by the label **POWER SUPPLY**. The power button allows the device to be switched on/off.

    <div class="ars-step-attn">
    Make sure the FlexiBowl® is <strong>switched off</strong> before connecting the power supply, and that the device is earthed.
    </div>

    <div class="ars-step-warn">
    Permitted voltage: <strong>120–230 Vac, 50/60 Hz</strong>.
    </div>

    <div class="ars-step-note">
    The power connector is equipped with a holder for <strong>2 fuses</strong>, which protect against possible electrical faults. At first start-up, always check their condition before switching on the device.
    </div>

    <details class="ars-dropdown"><summary>Power cable pinout diagram</summary><div class="ars-dropdown-body">

    | Color | Type | Label |
    |---|---|---|
    | Brown | Phase | L1 |
    | Blue | Neutral | N1 |
    | Yellow/Green | Earth | PE1 |

    </div></details>
  -
    ```{image} ../../../../_shared/media/images/stpanel1.PNG
    :alt: Connect the power supply
    :class: ars-zoom-img
    ```

```

:::{note}
After power-up, always check the state of the machine via the **status LEDs** on the front panel — see the {ref}`Status LEDs <led-stato>` section further down on this page.
:::

:::{tip}
The power and Ethernet cables are available as an option in lengths of 3, 5 and 10 m: see {ref}`cavo-alim` and {ref}`cavo-eth`.
:::

---

(rack-esterno)=
## FlexiBowl® 200 / 350 — External Rack

The FlexiBowl® FB 200 and FB 350 models are equipped with an external **Rack**, containing all the electronic devices needed for operation. The connectors to the customer's systems are located on the rack (not on the machine) and have the **same pinout** as the corresponding connectors of the standard panel, simply placed on an external box.

### Rack connections

```{list-table}
:widths: 8 52 40
:header-rows: 1

* - #
  - Action
  - Image
* - 1
  - **Connect the STO** on the rack.

    10-pin connector, same function and pinout as the standard panel.

    <div class="ars-step-note">
    The <strong>+STO1</strong> and <strong>+STO2</strong> inputs must receive <strong>+24 Vdc</strong> from the safety circuit; <strong>−STO1</strong> and <strong>−STO2</strong> must be connected to the −24 Vdc reference.
    </div>

    <details class="ars-dropdown"><summary>STO connector pinout (10 pin)</summary><div class="ars-dropdown-body">

    | Pin | Description |
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
    :alt: Connect the STO
    :class: ars-zoom-img
    ```

* - 2
  - **Connect the C-ETH IN** on the rack.

    M12 connector, D-Code coding.

    <div class="ars-step-attn">
    <strong>Mandatory</strong> connection when the machine is powered: if absent, the machine goes into ERROR (red Ready/Fault LED).
    </div>

    <details class="ars-dropdown"><summary>M12 → RJ45 pinout</summary><div class="ars-dropdown-body">

    8-pole M12 → RJ45 adapter:

    | RJ45 pin | Signal | Function | Color |
    |---|---|---|---|
    | 1 | TD+ | Data transmission (+) | Yellow |
    | 2 | TD− | Data transmission (−) | Orange |
    | 3 | RD+ | Data reception (+) | White |
    | 4 | NC | Not assigned | — |
    | 5 | NC | Not assigned | — |
    | 6 | RD− | Data reception (−) | Blue |
    | 7 | NC | Not assigned | — |
    | 8 | NC | Not assigned | — |

    4-pole M12 D-code connector:

    | M12 pin | Signal | Function | Color |
    |---|---|---|---|
    | 1 | TD+ | Data transmission (+) | Yellow |
    | 2 | RD+ | Data reception (+) | White |
    | 3 | TD− | Data transmission (−) | Orange |
    | 4 | RD− | Data reception (−) | Blue |

    </div></details>
  -
    ```{image} ../../../../_shared/media/images/rack6.PNG
    :width: 110%
    :alt: Rack panel
    :class: ars-zoom-img
    ```

* - 3
  - **Connect the Hopper** on the rack.

    M12 A-code connector, **Modbus RTU** protocol.

    <details class="ars-dropdown"><summary>M12 A-code pinout</summary><div class="ars-dropdown-body">

    | M12 pin | Signal | Function | Color |
    |---|---|---|---|
    | 1 | A+ | RS485 data line (+) | Brown |
    | 2 | NC | Not assigned | White |
    | 3 | B− | RS485 data line (−) | Blue |
    | 4 | GND | Common reference | Black |
    | 5 | NC | Not assigned | Gray |

    </div></details>
  -
    ```{image} ../../../../_shared/media/images/rack7.PNG
    :width: 110%
    :alt: Rack panel
    :class: ars-zoom-img
    ```

* - 4
  - **Connect the power supply** on the rack — last.

    Power socket with switch; it also includes an IEC filter.

    <div class="ars-step-attn">
    Make sure the FlexiBowl® is <strong>switched off</strong> before connecting the power supply.
    </div>

    <div class="ars-step-warn">
    Permitted voltage: <strong>120–230 Vac, 50/60 Hz</strong>.
    </div>

    <div class="ars-step-note">
    On the rack too, the power connector has a housing for the <strong>2 protection fuses</strong>: check their condition at first start-up.
    </div>

    <details class="ars-dropdown"><summary>Power cable pinout diagram</summary><div class="ars-dropdown-body">

    | Color | Type | Label |
    |---|---|---|
    | Brown | Phase | L1 |
    | Blue | Neutral | N1 |
    | Yellow/Green | Earth | PE1 |

    </div></details>
  -
    ```{image} ../../../../_shared/media/images/rack1.PNG
    :width: 110%
    :alt: Rack panel
    :class: ars-zoom-img
    ```
```

(collegamento-rack)=
### Connection between Rack and FlexiBowl®

The rack communicates with the FlexiBowl® via 4 dedicated cables, each to be connected **exclusively** to the port with the corresponding label on the machine panel.

:::{attention}
Connect each cable to the port with the **matching label** (e.g. MOTOR ↔ MOTOR, C-A SIGNAL ↔ C-A SIGNAL). A crossed connection can damage the system.
:::

:::{tip}
The 3 m cables between rack and FlexiBowl® are included in the supply; the 5 and 10 m versions are available as an option: see {ref}`cavo-rack`.
:::

```{list-table}
:widths: 8 52 40
:header-rows: 1

* - #
  - Action
  - Image
* - 5
  - **Connect the Ethernet cable (C-ETH FB)** between Rack and FlexiBowl®.

    M12 D-code connector.
  -
    ```{image} ../../../../_shared/media/images/rack8.PNG
    :width: 110%
    :alt: Connect the C-ETH FB cable
    :class: ars-zoom-img
    ```
    ```{image} ../../../../_shared/media/images/smallpanel4.PNG
    :width: 110%
    :alt: Connect the C-ETH FB cable
    :class: ars-zoom-img
    ```
* - 6
  - **Connect the MOTOR cable.**

    <div class="ars-step-note">
    9-pin connector: it carries both the motor power and the <strong>STO</strong> signals to the FlexiBowl® (on the rack, STO and Motor are separate connectors; on the cable to the machine they are combined in a single 9-pin connector).
    </div>

    <details class="ars-dropdown"><summary>Motor connector pinout (9 pin)</summary><div class="ars-dropdown-body">

    | Pin | Description |
    |---|---|
    | 1 | +STO1 – Safe Torque Off |
    | 2 | +24 Vdc – Auxiliary power supply |
    | 3 | +STO2 – Safe Torque Off |
    | 4 | −24 Vdc – Auxiliary power supply |
    | 5 | NC |
    | 6 | +48 Vdc – Motor Power |
    | 7 | −STO1 – Safe Torque Off |
    | 8 | −48 Vdc – Motor Power |
    | 9 | −STO2 – Safe Torque Off |

    </div></details>
  -
    ```{image} ../../../../_shared/media/images/rack3.PNG
    :width: 110%
    :alt: Connect the Motor cable
    :class: ars-zoom-img
    ```
    ```{image} ../../../../_shared/media/images/smallpanel3.PNG
    :width: 110%
    :alt: Connect the C-ETH FB cable
    :class: ars-zoom-img
    ```
* - 7
  - **Connect the C-A SIGNAL cable.**

    12-pin connector for analog signals.

    <details class="ars-dropdown"><summary>C-A Signal pinout (12 pin)</summary><div class="ars-dropdown-body">

    | Pin | Description |
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
    :alt: Connect the C-A Signal cable
    :class: ars-zoom-img
    ```
    ```{image} ../../../../_shared/media/images/smallpanel1.PNG
    :width: 110%
    :alt: Connect the C-ETH FB cable
    :class: ars-zoom-img
    ```
* - 8
  - **Connect the C-B SIGNAL cable.**

    19-pin connector for digital signals, including the status LED activations.

    <details class="ars-dropdown"><summary>C-B Signal pinout (19 pin)</summary><div class="ars-dropdown-body">

    | Pin | Description |
    |---|---|
    | 1 | +24 Vdc – Green status LED activation |
    | 2 | −24 Vdc – Status LED common |
    | 3 | +24 Vdc – Red status LED activation |
    | 4 | +24 Vdc – Backlight status LED activation |
    | 5 | −24 Vdc – Backlight status LED activation |
    | 6 | +24 Vdc – Backlight activation |
    | 7 | −24 Vdc – Backlight activation |
    | 8 | +24 Vdc – Flip activation |
    | 9 | −24 Vdc – Flip activation |
    | 10 | +24 Vdc – Blow activation |
    | 11 | −24 Vdc – Blow activation |
    | 12–19 | NC |

    </div></details>
  -
    ```{image} ../../../../_shared/media/images/rack5.PNG
    :width: 110%
    :alt: Connect the C-B Signal cable
    :class: ars-zoom-img
    ```
    ```{image} ../../../../_shared/media/images/smallpanel2.PNG
    :width: 110%
    :alt: Connect the C-ETH FB cable
    :class: ars-zoom-img
    ```
```

:::{note}
After power-up, always check the state of the machine via the **status LEDs** on the front panel — see the {ref}`Status LEDs <led-stato>` section further down on this page.
:::

---

(led-stato)=
## Status LEDs

On the front panel of the FlexiBowl® there are two status LEDs, common to **all sizes** (500–1200 and 200/350):

| LED | Color | Meaning |
|---|---|---|
| **Light ON** | Green (only state) | Indicates whether the backlight on board the FlexiBowl® is ON or OFF. The backlight is used by the vision system to illuminate the components and make them recognizable. It can be activated via the vision software or via commands from an external system communicating over Ethernet. |
| **Ready / Fault** | Green | System operational and free of faults. Ethernet connection correct. |
| **Ready / Fault** | Red | Internal fault or fault in the Ethernet connection. Refer to the fault table. |

:::{note}
After power-up, wait for the **Ready/Fault** LED to light up: if Hopper and C-ETH are connected correctly, the LED will be **green**.
:::

---

(io-flexitrack)=
## Circular Tracking option — Interface Panel

The small panel supplied with the Circular Tracking option adds, in addition to the connections already described, the following dedicated connectors:

- **I/O connector**: exchange of digital signals, including the Latch function.
- **Encoder cable gland**: dedicated to the encoder internal to the FlexiBowl®.

```{list-table}
:widths: 8 52 40
:header-rows: 1

* - #
  - Action
  - Image
* - 10
  - **Connect the I/O connector** (19-pin).

    <details class="ars-dropdown"><summary>I/O connector pinout (19 pin)</summary><div class="ars-dropdown-body">

    | Pin | Signal |
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
    :alt: Circular Tracking I/O connector
    :class: ars-zoom-img
    ```
* - 11
  - **Connect the encoder cable gland**, dedicated to the encoder internal to the FlexiBowl®.
  -
    ```{image} ../../../../_shared/media/images/encpanel8.PNG
    :alt: Circular Tracking encoder cable gland
    :class: ars-zoom-img
    ```
```

---

## General Notes and Warnings

:::{attention}
All connection operations must be performed with the device switched off and disconnected from the power supply.
:::

:::{attention}
The earth connection is mandatory and must be verified before every power-up.
:::

:::{attention}
In case of an anomaly indicated by the red LED (Ready/Fault), refer to the model-specific fault table.
:::

:::{attention}
For further technical information or assistance, contact ARS s.r.l. – FlexiBowl® Division.
:::


