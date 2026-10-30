(panoramica)=
# **Overview and Unboxing**

## Main components of the FlexiBowl®

The FlexiBowl® consists of the following main parts:

:::{raw} html
<style>
*{box-sizing:border-box;margin:0;padding:0}
:root{
  --acc:#1a6fc4;--acc-dk:#0d4a8a;--acc-bg:#e8f1fb;
  --bd:#e0e0e0;--bg-p:#ffffff;--bg-s:#f7f8f9;--bg-h:#f0f4fa;
  --tx1:#1a1a1a;--tx2:#555;--tx3:#888;
  --r:10px;--tr:0.35s cubic-bezier(.4,0,.2,1);
}

/* ── Tab bar ── */
.fb-tabs{display:flex;gap:6px;margin-bottom:12px}
.fb-tab{padding:5px 14px;border-radius:6px;border:1.5px solid var(--bd);background:#fff;font-size:13px;font-weight:600;color:var(--tx2);cursor:pointer;transition:background var(--tr),color var(--tr),border-color var(--tr)}
.fb-tab:hover{background:var(--bg-h)}
.fb-tab.on{background:var(--acc-bg);color:var(--acc-dk);border-color:var(--acc)}

/* ── Panel ── */
.fb-panel{display:none}
.fb-panel.on{display:block}
.fb-wrap{border:1px solid var(--bd);border-radius:var(--r);overflow:hidden;background:var(--bg-p);box-shadow:0 2px 12px rgba(0,0,0,0.07)}
.fb-img-outer{position:relative;width:100%;padding-top:70.71%}
.fb-img-outer img{position:absolute;inset:0;width:100%;height:100%;object-fit:contain;padding:0;transition:opacity var(--tr)}
.fb-img-base{opacity:1;z-index:1}
.fb-img-hl{opacity:0;z-index:2}
.fb-badge{position:absolute;top:12px;left:14px;z-index:3;background:var(--acc);color:#fff;font-size:12px;font-weight:600;padding:4px 10px;border-radius:20px;opacity:0;transform:translateY(-4px);transition:opacity var(--tr),transform var(--tr);pointer-events:none;white-space:nowrap}
.fb-badge.on{opacity:1;transform:translateY(0)}
.fb-hint{position:absolute;bottom:14px;left:50%;z-index:3;transform:translateX(-50%);font-size:13px;color:#fff;background:rgba(0,0,0,0.38);padding:6px 16px;border-radius:20px;pointer-events:none;transition:opacity var(--tr);white-space:nowrap}
.fb-list-panel{border-top:1px solid var(--bd);background:var(--bg-p)}
.fb-list-head{display:grid;grid-template-columns:40px 160px 1fr;gap:8px;padding:8px 14px;background:var(--bg-s);border-bottom:1px solid var(--bd);font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:.05em;color:var(--tx3)}
.fb-row{display:grid;grid-template-columns:40px 160px 1fr;gap:8px;align-items:center;padding:9px 14px;border-bottom:1px solid var(--bd);cursor:pointer;transition:background var(--tr);user-select:none}
.fb-row:last-child{border-bottom:none}
.fb-row:hover{background:var(--bg-h)}
.fb-row.on{background:var(--acc-bg)}
.fb-bubble{width:26px;height:26px;border-radius:50%;border:1.5px solid var(--bd);background:#fff;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:600;color:var(--tx2);flex-shrink:0;transition:background var(--tr),color var(--tr),border-color var(--tr)}
.fb-row.on .fb-bubble{background:var(--acc);color:#fff;border-color:var(--acc)}
.fb-name{font-size:13px;font-weight:500;color:var(--tx1);transition:color var(--tr)}
.fb-row.on .fb-name{color:var(--acc-dk)}
.fb-desc{font-size:12px;color:var(--tx2);line-height:1.55}
.fb-desc a{color:var(--acc);text-decoration:underline}
</style>

<!-- Tab bar -->
<div class="fb-tabs">
  <button class="fb-tab on"    onclick="fbSwitchTab('fb200',this)">FB200</button>
  <button class="fb-tab"    onclick="fbSwitchTab('fb350',this)">FB350</button>
  <button class="fb-tab" onclick="fbSwitchTab('fb650',this)">FB500-650-800-1200</button>
</div>

<!-- ══════════ FB650 ══════════ -->
<div class="fb-panel" id="fb-panel-fb650">
  <div class="fb-wrap">
    <div class="fb-img-outer">
      <img class="fb-img-base" id="fb650-img-base" src="../../../../_shared/media/images/component_default.PNG" alt="FlexiBowl® 650 view" />
      <img class="fb-img-hl"   id="fb650-img-hl"   src="" alt="" aria-hidden="true" />
      <div class="fb-badge" id="fb650-badge"></div>
      <div class="fb-hint"  id="fb650-hint">Select a component from the list</div>
    </div>
    <div class="fb-list-panel">
      <div class="fb-list-head"><span>No.</span><span>Component</span><span>Description</span></div>
      <div id="fb650-list"></div>
    </div>
  </div>
</div>

<!-- ══════════ FB350 ══════════ -->
<div class="fb-panel" id="fb-panel-fb350">
  <div class="fb-wrap">
    <div class="fb-img-outer">
      <img class="fb-img-base" id="fb350-img-base" src="../../../../_shared/media/images/FB350-0.PNG" alt="FlexiBowl® 350 view" />
      <img class="fb-img-hl"   id="fb350-img-hl"   src="" alt="" aria-hidden="true" />
      <div class="fb-badge" id="fb350-badge"></div>
      <div class="fb-hint"  id="fb350-hint">Select a component from the list</div>
    </div>
    <div class="fb-list-panel">
      <div class="fb-list-head"><span>No.</span><span>Component</span><span>Description</span></div>
      <div id="fb350-list"></div>
    </div>
  </div>
</div>

<!-- ══════════ FB200 ══════════ -->
<div class="fb-panel on" id="fb-panel-fb200">
  <div class="fb-wrap">
    <div class="fb-img-outer">
      <img class="fb-img-base" id="fb200-img-base" src="../../../../_shared/media/images/FB200-0.PNG" alt="FlexiBowl® 200 view" />
      <img class="fb-img-hl"   id="fb200-img-hl"   src="" alt="" aria-hidden="true" />
      <div class="fb-badge" id="fb200-badge"></div>
      <div class="fb-hint"  id="fb200-hint">Select a component from the list</div>
    </div>
    <div class="fb-list-panel">
      <div class="fb-list-head"><span>No.</span><span>Component</span><span>Description</span></div>
      <div id="fb200-list"></div>
    </div>
  </div>
</div>

<script>
(function(){

  /* ── dati componenti ── */
  var models = {
    fb650: {
      imgPath: '../../../../_shared/media/images/component_',
      imgDefault: '../../../../_shared/media/images/component_default.PNG',
      imgExt: '.PNG',
      comps: [
//        {n:1,  name:'Pneumatic unit',           desc:'They supply the flip unit and any blow-off nozzles.'},
//        {n:2,  name:'Motor unit',               desc:'Allows the surface or rigid disc to rotate.'},
        {img:3,  name:'Containment ring',      desc:'Made up of several sectors, it prevents parts from escaping during operation. It also houses the diverters when no accessories are fitted.'},
//        {img:4,  name:'Backlight',                   desc:'Backlights the vision area to highlight the outlines of the parts.'},
        {img:5,  name:'Flip screen',                desc:'Prevents parts from escaping during flipping.'},
        {img:6,  name:'Cover',                      desc:'Houses and protects the internal parts. Protects the user from exposure to electrical voltage and moving components.'},
//        {img:7,  name:'Flip unit',                 desc:'Striker driven by a pneumatic mini-slide (350–1200) or a pneumatic cylinder (200). It generates an impulse that flips the objects before the vision window.'},
//        {n:8,  name:'Frame',                      desc:'It is the load-bearing structure of the FlexiBowl®.'},
//        {n:9, name:'Electronics unit',          desc:'Includes all the control electronics of the FlexiBowl®.'},
//        {n:10, name:'Connector panel',         desc:'Includes all electrical and pneumatic connections.'},
        {img:11, name:'Surface / disc support', desc:'Holds the surface or rigid disc firmly attached to the motor unit.'},
//        {n:12, name:'Cover plates',        desc:'Allow easy access to the internal components for maintenance.'}
      ]
    },
    fb350: {
      imgPath: '../../../../_shared/media/images/FB350-',
      imgDefault: '../../../../_shared/media/images/FB350-0.PNG',
      imgExt: '.PNG',
      comps: [
        {img:1,  name:'Cables and extensions',  desc:'They are the electronic connections between the various internal components of the FlexiBowl®.'},
//        {n:2,  name:'Pneumatic unit', desc:'Supplies the flip unit and the blow-off nozzles.'},
//        {n:3,  name:'Motor unit',     desc:'Allows the rigid disc to rotate.'},
        {img:4,  name:'Disc',             desc:'<a href="../ACCESSORI/02_DISCHI_RIGIDI.html">See the dedicated section</a>.'},
//        {n:5,  name:'Backlight',         desc:'Backlights the vision area to highlight the outlines of the parts.'},
        {img:6,  name:'Flip screen',      desc:'Prevents parts from escaping during flipping. Also includes the <a href="../ACCESSORI/06-4_INTEGRATI.html">blow-off nozzles</a>.'},
        {img:7,  name:'Cover',            desc:'Houses and protects the internal parts. Protects the user from exposure to electrical voltage and moving components.'},
//        {n:8,  name:'Flip unit',       desc:'Striker driven by a pneumatic cylinder (200). It generates an impulse that flips the objects before the vision window.'},
//        {n:9,  name:'Frame',            desc:'It is the load-bearing structure of the FlexiBowl®.'},
        {img:10, name:'Disc support',    desc:'Holds the rigid disc firmly attached to the motor unit.'},
        {img:11, name:'Rack',              desc:'Houses all the electronics of the FlexiBowl®.'}
      ]
    },
    fb200: {
      imgPath: '../../../../_shared/media/images/FB200-',
      imgDefault: '../../../../_shared/media/images/FB200-0.PNG',
      imgExt: '.PNG',
      comps: [
        {img:1,  name:'Cables and extensions',  desc:'They are the electronic connections between the various internal components of the FlexiBowl®.'},
//        {n:2,  name:'Pneumatic unit', desc:'Supplies the flip unit and the blow-off nozzles.'},
//        {n:3,  name:'Motor unit',     desc:'Allows the rigid disc to rotate.'},
        {img:4,  name:'Disc',             desc:'<a href="../ACCESSORI/02_DISCHI_RIGIDI.html">See the dedicated section</a>.'},
//        {n:5,  name:'Backlight',         desc:'Backlights the vision area to highlight the outlines of the parts.'},
        {img:6,  name:'Flip screen',      desc:'Prevents parts from escaping during flipping. Also includes the <a href="../ACCESSORI/06-4_INTEGRATI.html">blow-off nozzles</a>.'},
        {img:7,  name:'Cover',            desc:'Houses and protects the internal parts. Protects the user from exposure to electrical voltage and moving components.'},
//        {n:8,  name:'Flip unit',       desc:'Striker driven by a pneumatic cylinder (200). It generates an impulse that flips the objects before the vision window.'},
//        {n:9,  name:'Frame',            desc:'It is the load-bearing structure of the FlexiBowl®.'},
        {img:10, name:'Rack',              desc:'Houses all the electronics of the FlexiBowl®.'}
      ]
    }
  };

  Object.keys(models).forEach(function(id){
  models[id].comps.forEach(function(c, i){
    if (c.img === undefined) c.img = c.n;
    c.n = i + 1;
  });
});

  /* ── stato per modello ── */
  var state = {};
  Object.keys(models).forEach(function(id){ state[id]={activeN:null,activeRow:null}; });

  /* ── costruisce le liste ── */
  Object.keys(models).forEach(function(id){
    var m   = models[id];
    var el  = document.getElementById(id+'-list');
    m.comps.forEach(function(c){
      var row = document.createElement('div');
      row.className = 'fb-row';
      row.innerHTML = '<div class="fb-bubble">'+c.n+'</div>'
                    + '<div class="fb-name">'+c.name+'</div>'
                    + '<div class="fb-desc">'+c.desc+'</div>';
      row.addEventListener('click', function(){ toggle(id, c, row); });
      el.appendChild(row);
    });
  });

  /* ── toggle componente ── */
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

    badge.textContent = c.n + ' \u2014 ' + c.name;
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
    newImg.src = m.imgPath + c.img + m.imgExt;   // <-- c.img, non c.n
  }

  /* ── reset ── */
  function reset(id){
    var s       = state[id];
    var m       = models[id];
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

  /* ── switch tab ── */
  window.fbSwitchTab = function(id, btn){
    /* resetta il pannello attualmente attivo prima di cambiare */
    document.querySelectorAll('.fb-panel.on').forEach(function(p){
      var oldId = p.id.replace('fb-panel-','');
      reset(oldId);
    });
    document.querySelectorAll('.fb-tab').forEach(function(b){ b.classList.remove('on'); });
    document.querySelectorAll('.fb-panel').forEach(function(p){ p.classList.remove('on'); });
    btn.classList.add('on');
    document.getElementById('fb-panel-'+id).classList.add('on');
  };

})();
</script>
:::

## What is in the box?


This section describes the contents of the **FlexiBowl® 3.0** package and the standard components supplied with the unit.

:::{important}
Before proceeding with the installation, verify that all components listed in this section are present in the package. In case of missing or damaged components, contact [Technical Support](support) before putting the device into operation.
:::

---

### 1. Package contents

Inside the package are the **FlexiBowl®** and all standard connection adapters:

```{list-table}
:header-rows: 1
:widths: 22 58 20

* - Component
  - Description
  - Image
* - **Power connector**
  - Equipped with a locking clip that prevents accidental disconnection
  - :::{image} ../../../../_shared/media/images/connettore_power.png
    :width: 100%
    :::
* - **10-pin connector cable**
  - Carries the 24 Vdc power supply and the two Safe Torque Off (STO) channels
  - :::{image} ../../../../_shared/media/images/connettore_STO.png
    :width: 100%
    :::
* - **M12 D-code connector**
  - Used for Ethernet communication between the FlexiBowl® and the system
  - :::{image} ../../../../_shared/media/images/connettore_ethernet.png
    :width: 100%
    :::
* - **M12 A-code connector**
  - Used for Modbus RTU communication with the Bulk Feeder controller
  - :::{image} ../../../../_shared/media/images/connettore_hopper.png
    :width: 100%
    :::
* - **USB flash drive**
  - Contains the unit manuals and its individual test report
  - —
```
:::{note}
Connection cables can be purchased separately as an option in 3, 5 or 10 meters: see {ref}`Connection cables <cavi>`.
:::

---

### 2. Additional components by size


```{list-table}
:header-rows: 1
:widths: 20 20 60

* - Model
  - Image
  - Additional equipment
* - **FlexiBowl® 200 / 350**
  - :::{image} ../../../../_shared/media/images/FB350.png
    :width: 100%
    :::
  - Also includes the **rack** and the related **connection cables**, required for the external electronics. The included cables, 3 m long, allow all connections between rack and FlexiBowl® to be made. 5/10 meter versions are available as an option ({ref}`see rack cables <cavo-rack>`).
    :::{image} ../../../../_shared/media/images/rack.png
    :width: 100%
    :::
* - **FlexiBowl® 500 and above**
  - :::{image} ../../../../_shared/media/images/FB650.png
    :width: 100%
    :::
  - Do not require the external connection rack: the electronics are integrated directly into the unit
```


#### Rack connection panel (FlexiBowl® 200 / 350)

```{image} ../../../../_shared/media/images/rack.png
:alt: Rack connection panel
:width: 80%
:align: center
```

The rear panel of the rack groups all the connection points described in the previous paragraph: power supply (**POWER SUPPLY**), Safe Torque Off (**STO**), motor (**MOTOR**), Ethernet to the system (**C-ETH IN**) and to the FlexiBowl® (**C-ETH FB**), Bulk Feeder (**HOPPER**) and encoder signals (**C-A SIGNAL**, **C-B SIGNAL**).

:::{note}
For details on the positioning and connection of the rack, refer to the [Mechanical Installation](mech_install) section.
:::


---

### 3. Accompanying documentation

The USB flash drive supplied contains:

- The unit **manuals** (offline version of the documentation)
- The individual **test report** of the purchased FlexiBowl®



