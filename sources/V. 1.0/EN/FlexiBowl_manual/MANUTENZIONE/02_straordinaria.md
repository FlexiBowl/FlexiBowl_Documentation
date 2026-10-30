# **Extraordinary Maintenance**

:::{warning}
Extraordinary maintenance and repair of the machine are reserved for qualified, trained and authorized technicians, employed by the Manufacturer or by the authorized service center. These interventions require in-depth, specialist knowledge of the machines, of the operations required, of the associated risks and of the correct procedures for working safely.
:::

If exceptional events occur that require extraordinary maintenance work, the user's routine maintenance personnel must follow these procedures:
- check the condition of the damaged or misaligned assemblies;
- carry out the operations described in this paragraph;
- if the operations to be carried out are not covered in this manual, send the Manufacturer a report of the events that occurred, the result of the inspection and any observations.

The Manufacturer or the authorized service center will assess the situation case by case. They will then agree with the routine maintenance personnel on the type of intervention to be carried out, choosing the most suitable solution from those listed below:
- the Manufacturer sends an authorized, trained and qualified technician to carry out the necessary interventions;
- or the Manufacturer authorizes the user's routine maintenance personnel to carry out the interventions, providing any additional instructions.

:::{warning}
The spare parts to be replaced must be ordered from ARS S.r.l.

If the customer does not use original spare parts or parts authorized in writing by the Manufacturer, the latter is released from any liability for the operation of the machine and the safety of the operators. Authorization and/or instructions must always be communicated in writing. In the absence of written authorization, it is forbidden to operate and the Manufacturer declines all liability.
:::

:::{warning}
Maintenance operations must be carried out only by qualified and authorized personnel.
:::

::::{warning}
<table style="width: 100%; border: none; background: transparent;">
  <tr style="background: transparent !important; border: none !important;">
    <td style="width: 10%; border: none; vertical-align: middle; text-align: center; background: transparent !important;">
      <img src="../../../../_shared/media/images/corrente.png" style="width: 50px; height: auto;">
    </td>
    <td style="width: 90%; border: none; vertical-align: middle; background: transparent !important; padding-left: 15px;">
      Disconnect the electrical power supply before removing the cover.
    </td>
  </tr>
</table>
::::

:::{warning}
Disconnect the electrical and pneumatic power supply before proceeding with maintenance operations.
:::

:::{note}
When fastening screws, always use LOCTITE 243 to ensure perfect tightening (except for the screws of the surface or rigid disc flange on the FlexiBowl®).
:::

## Potential intervention assemblies

The assemblies that make up the FlexiBowl® are the following:

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
        {n:1,  name:'Pneumatic unit',           desc:'They supply the flip unit and any blow-off nozzles.'},
        {n:2,  name:'Motor unit',               desc:'Allows the surface or rigid disc to rotate.'},
        {n:3,  name:'Containment ring',      desc:'Made up of several sectors, it prevents parts from escaping during operation. It also houses the diverters when no accessories are fitted.'},
        {n:4,  name:'Backlight',                   desc:'Backlights the vision area to highlight the outlines of the parts.'},
        {n:5,  name:'Flip screen',                desc:'Prevents parts from escaping during flipping.'},
        {n:6,  name:'Cover',                      desc:'Houses and protects the internal parts. Protects the user from exposure to electrical voltage and moving components.'},
        {n:7,  name:'Flip unit',                 desc:'Striker driven by a pneumatic mini-slide (350–1200) or a pneumatic cylinder (200). It generates an impulse that flips the objects before the vision window.'},
        {n:8,  name:'Frame',                      desc:'It is the load-bearing structure of the FlexiBowl®.'},
        {n:9, name:'Electronics unit',          desc:'Includes all the control electronics of the FlexiBowl®.'},
        {n:10, name:'Connector panel',         desc:'Includes all electrical and pneumatic connections.'},
        {n:11, name:'Surface / disc support', desc:'Holds the surface or rigid disc firmly attached to the motor unit.'},
        {n:12, name:'Cover plates',        desc:'Allow easy access to the internal components for maintenance.'}
      ]
    },
    fb350: {
      imgPath: '../../../../_shared/media/images/FB350-',
      imgDefault: '../../../../_shared/media/images/FB350-0.PNG',
      imgExt: '.PNG',
      comps: [
        {n:1,  name:'Cables and extensions',  desc:'They are the electronic connections between the various internal components of the FlexiBowl®.'},
        {n:2,  name:'Pneumatic unit', desc:'Supplies the flip unit and the blow-off nozzles.'},
        {n:3,  name:'Motor unit',     desc:'Allows the rigid disc to rotate.'},
        {n:4,  name:'Disc',             desc:'<a href="../ACCESSORI/02_DISCHI_RIGIDI.html">See the dedicated section</a>.'},
        {n:5,  name:'Backlight',         desc:'Backlights the vision area to highlight the outlines of the parts.'},
        {n:6,  name:'Flip screen',      desc:'Prevents parts from escaping during flipping. Also includes the <a href="../ACCESSORI/06-4_INTEGRATI.html">blow-off nozzles</a>.'},
        {n:7,  name:'Cover',            desc:'Houses and protects the internal parts. Protects the user from exposure to electrical voltage and moving components.'},
        {n:8,  name:'Flip unit',       desc:'Striker driven by a pneumatic cylinder (200). It generates an impulse that flips the objects before the vision window.'},
        {n:9,  name:'Frame',            desc:'It is the load-bearing structure of the FlexiBowl®.'},
        {n:10, name:'Disc support',    desc:'Holds the rigid disc firmly attached to the motor unit.'},
        {n:11, name:'Rack',              desc:'Houses all the electronics of the FlexiBowl®.'}
      ]
    },
    fb200: {
      imgPath: '../../../../_shared/media/images/FB200-',
      imgDefault: '../../../../_shared/media/images/FB200-0.PNG',
      imgExt: '.PNG',
      comps: [
        {n:1,  name:'Cables and extensions',  desc:'They are the electronic connections between the various internal components of the FlexiBowl®.'},
        {n:2,  name:'Pneumatic unit', desc:'Supplies the flip unit and the blow-off nozzles.'},
        {n:3,  name:'Motor unit',     desc:'Allows the rigid disc to rotate.'},
        {n:4,  name:'Disc',             desc:'<a href="../ACCESSORI/02_DISCHI_RIGIDI.html">See the dedicated section</a>.'},
        {n:5,  name:'Backlight',         desc:'Backlights the vision area to highlight the outlines of the parts.'},
        {n:6,  name:'Flip screen',      desc:'Prevents parts from escaping during flipping. Also includes the <a href="../ACCESSORI/06-4_INTEGRATI.html">blow-off nozzles</a>.'},
        {n:7,  name:'Cover',            desc:'Houses and protects the internal parts. Protects the user from exposure to electrical voltage and moving components.'},
        {n:8,  name:'Flip unit',       desc:'Striker driven by a pneumatic cylinder (200). It generates an impulse that flips the objects before the vision window.'},
        {n:9,  name:'Frame',            desc:'It is the load-bearing structure of the FlexiBowl®.'},
        {n:10, name:'Rack',              desc:'Houses all the electronics of the FlexiBowl®.'}
      ]
    }
  };

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
    newImg.src = m.imgPath + c.n + m.imgExt;
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

:::{toctree}
:hidden:
02-1_sost-backlight.md
02-2_sost-ev.md
02-3_sost-vp.md
02-4_sost-flip.md
02-11_sost-mot.md
02-12_sost-ele.md
:::