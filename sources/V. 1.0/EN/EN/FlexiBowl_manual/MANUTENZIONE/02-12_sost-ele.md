# [ELE] **Replacement of Electronic Components**

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

* - **Electrical maintenance technician**
  - :::{raw} html
       <div class="ars-img-row">
         <img src="../../../../_shared/media/images/guanti.png" alt="gloves">
         <img src="../../../../_shared/media/images/scarpe.png" alt="shoes">
         <img src="../../../../_shared/media/images/tuta.png" alt="overalls">
       </div>
    :::
::::
:::::

::::{warning}
<table style="width: 100%; border: none; background: transparent;">
  <tr style="background: transparent !important; border: none !important;">
    <td style="width: 10%; border: none; vertical-align: middle; text-align: center; background: transparent !important;">
      <img src="../../../../_shared/media/images/corrente.png" style="width: 50px; height: auto;">
    </td>
    <td style="width: 90%; border: none; vertical-align: middle; background: transparent !important; padding-left: 15px;">
      Disconnect the electrical power supply before carrying out any operation inside the FlexiBowl®.
    </td>
  </tr>
</table>
::::

## Replacement of the main electronic parts

In the smaller sizes the electronics are all contained in the rack, so it is sufficient to remove the top panel to access all the components. In FlexiBowl® units of size 500 or larger, instead, all the parts are contained in the machine.

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
  <button class="fb-tab on"    onclick="fbSwitchTab('rack',this)">Electronics in the rack</button>
  <button class="fb-tab"    onclick="fbSwitchTab('fb',this)">Electronics in the FlexiBowl®</button>
</div>

<!-- ══════════ rack ══════════ -->
<div class="fb-panel on" id="fb-panel-rack">
  <div class="fb-wrap">
    <div class="fb-img-outer">
      <img class="fb-img-base" id="rack-img-base" src="../../../../_shared/media/images/inrack0.PNG" alt="Electronics in the rack" />
      <img class="fb-img-hl"   id="rack-img-hl"   src="" alt="" aria-hidden="true" />
      <div class="fb-badge" id="rack-badge"></div>
      <div class="fb-hint"  id="rack-hint">Select a component from the list</div>
    </div>
    <div class="fb-list-panel">
      <div class="fb-list-head"><span>No.</span><span>Component</span><span>Description</span></div>
      <div id="rack-list"></div>
    </div>
  </div>
</div>

<!-- ══════════ fb ══════════ -->
<div class="fb-panel" id="fb-panel-fb">
  <div class="fb-wrap">
    <div class="fb-img-outer">
      <img class="fb-img-base" id="fb-img-base" src="../../../../_shared/media/images/fbele0.PNG" alt="Electronics in the FlexiBowl®" />
      <img class="fb-img-hl"   id="fb-img-hl"   src="" alt="" aria-hidden="true" />
      <div class="fb-badge" id="fb-badge"></div>
      <div class="fb-hint"  id="fb-hint">Select a component from the list</div>
    </div>
    <div class="fb-list-panel">
      <div class="fb-list-head"><span>No.</span><span>Component</span><span>Description</span></div>
      <div id="fb-list"></div>
    </div>
  </div>
</div>

<script>
(function(){

  /* ── component data ── */
  var models = {
    rack: {
      imgPath: '../../../../_shared/media/images/inrack',
      imgDefault: '../../../../_shared/media/images/inrack0.PNG',
      imgExt: '.PNG',
      comps: [
        {n:1,  name:'PLC assembly and 24V power supply',     desc:'They are fixed on a DIN rail; the PLC modules can be removed individually'},
        {n:2,  name:'48V power supply',                  desc:'Fixed on a DIN rail'},
        {n:3,  name:'Board',                            desc:'Its support is fixed to the lower platform by means of two spacers; it also contains the fuses'},
        {n:4,  name:'Braking resistor',           desc:'Fixed to the lower platform by means of two M4 screws'},
      ]
    },
    fb: {
      imgPath: '../../../../_shared/media/images/fbele',
      imgDefault: '../../../../_shared/media/images/fbele0.PNG',
      imgExt: '.PNG',
      comps: [
        {n:1,  name:'PLC assembly and 24V power supply',     desc:'They are fixed on a DIN rail; the PLC modules can be removed individually'},
        {n:2,  name:'48V power supply',                  desc:'Fixed on a DIN rail'},
        {n:3,  name:'Braking resistor',           desc:'Fixed to the lower platform by means of two M4 screws on the FlexiBowl® 500 and by means of four M4 screws on the other sizes'},
      ]
    },
  };

  /* ── state per model ── */
  var state = {};
  Object.keys(models).forEach(function(id){ state[id]={activeN:null,activeRow:null}; });

  /* ── build the lists ── */
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

  /* ── toggle component ── */
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
    /* reset the currently active panel before switching */
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

In FlexiBowl® units of size 500 or larger, the board is anchored to a support fixed on the column next to the backlight on the flip side.

::: {figure} ../../../../_shared/media/images/schedapos.png
:align: center
:width: 90%
:::

:::{note}
In FlexiBowl® units of size 650 or larger, all the electronics can be accessed from above by removing the backlight illuminator and the central cover of the upper platform. On the FlexiBowl® 500 it may be more convenient to remove the covers in order to access the PLC/24V power supply assembly and the braking resistor from the side.
:::


(scheda-interfaccia)=
## Interface board maintenance

This section describes the operation and replacement procedure of the **interface relays** and the **protection fuses** present on the interface board.

The following figure shows the board with the position of the relays and fuses indicated.

::: {figure} ../../../../_shared/media/images/schedafronte.png
:align: center
:width: 80%

Front view of the interface board
:::

The rating of each fuse and the reference of each interface relay are printed on the back of the board.

(scheda-interfaccia-retro)=
::: {figure} ../../../../_shared/media/images/schedaretro.png
:align: center
:width: 80%

Rear view: relay references and fuse ratings
:::

### Safety warnings

:::{danger}
**Electrical hazard.** Before working on the interface board, remove power from the machine using the main switch and wait for the capacitors to discharge. Check that no voltage is present with a suitable measuring instrument before touching any component.
:::

During maintenance operations, strictly observe the following instructions:

- the intervention must be carried out exclusively by qualified and trained technical personnel;
- use suitable personal protective equipment (PPE), including antistatic gloves;
- avoid dropping tools or foreign objects onto the board during the intervention;
- do not replace a fuse with one of a different rating from the original;
- do not force the relays during extraction: if a component is stuck, check that it is correctly latched before proceeding;
- at the end of the intervention, correctly close the access door/slot before restoring power.

### Board description

(scheda-relè)=
#### Interface relays

The board is equipped with five interface relays, identified as K1–K5. Relay K1 is a double-changeover electromechanical relay; all the other relays (K2–K5) are solid-state relays.

:::{list-table}
:widths: 10 55 35
:header-rows: 1

* - Ref.
  - Function
  - Type
* - K1
  - Interface relay for back light
  - Double-changeover electromechanical
* - K2
  - Interface relay for flip solenoid valve
  - Solid state
* - K3
  - Interface relay for central blow solenoid valve
  - Solid state
* - K4
  - Interface relay for radial blow solenoid valve
  - Solid state
* - K5
  - Interface relay for emptying solenoid valve (optional)
  - Solid state
:::

(scheda-fusibili)=
#### Protection fuses

The board is equipped with nine protection fuses of the *automotive mini* type. The spare fuse kit is supplied with the FlexiBowl®.

:::{list-table}
:widths: 10 70 20
:header-rows: 1

* - Ref.
  - Function
  - Rating
* - F1
  - Main power supply
  - 10 A
* - F2
  - 24 V power supply — flip solenoid valve, central/radial blow, emptying
  - 7.5 A
* - F3
  - STO connector power supply
  - 2 A
* - F4
  - Power supply to customer
  - 5 A
* - F5
  - Emptying sensor
  - 2 A
* - F6
  - Back light power supply
  - 7.5 A
* - F7
  - Back light power supply
  - 7.5 A
* - F8
  - Motor and driver power supply
  - 5 A
* - F9
  - PLC power supply
  - 7.5 A
:::

### Required equipment

- Fuse puller for *automotive mini* fuses (or flat-nose tweezers)
- Spare fuse kit supplied with the FlexiBowl®
- Spare relays matching the original reference (K1–K5)

### Replacing the interface relays

The procedure applies to the replacement of one or more interface relays (K1–K5).

1. Remove power from the machine and check that no voltage is present with the multimeter, as indicated in the safety warnings.
2. Access the interface board through the dedicated opening.
3. Locate the position of the relay to be replaced by referring to the {ref}`rear view <scheda-interfaccia-retro>` and the {ref}`relay table <scheda-relè>`.
4. If the relay to be replaced is **K1** (electromechanical), gently extract it from its socket by pulling it upwards without forcing the terminals.
5. If the relay to be replaced is **K2, K3, K4 or K5** (solid state), extract it with the same care, avoiding bending the contact pins.
6. Insert the spare relay into the socket, checking that the reference and the orientation exactly match those of the removed component.
7. Check that the relay is correctly inserted and stable in the socket.
8. Close the board access opening.
9. Restore power and check the correct operation of the function associated with the replaced relay.

### Replacing the protection fuses

The procedure applies to the replacement of one or more protection fuses (F1–F9).

1. Remove power from the machine and check that no voltage is present with the multimeter, as indicated in the safety warnings.
2. Open the dedicated access slot to the protection fuses.
3. Locate the fuse to be replaced by referring to the {ref}`rear view <scheda-interfaccia-retro>` and the {ref}`fuse table <scheda-fusibili>`.
4. Extract the fuse using the dedicated puller (or tweezers), gripping it without touching the metal parts.
5. If possible, check the cause of the fuse blowing before proceeding with the replacement.
6. Take from the spare kit an *automotive mini* fuse of the same rating (amperage) indicated in the table.
7. Insert the new fuse into its seat, checking that it is correctly seated.
8. Close the access slot.
9. Restore power and check the correct operation of the circuit protected by the replaced fuse.

:::{caution}
Never use a fuse with a rating different from the original.
:::

### Periodic checks and preventive maintenance

- Periodically check for the absence of signs of overheating or blackening on relays, fuses and sockets.
- Check that the connectors on the board are correctly engaged.
- Always keep a stock of the spare fuse kit available.
- Record every replacement carried out (date, component reference, cause) in a maintenance log.
