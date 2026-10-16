# [MEC] **Machine Description** 

<p style="line-height: 1.6; border-left: 4px solid #34495e; padding-left: 15px; margin-bottom: 25px;">
  The hoppers are particularly suitable for feeding and pre-dosing small, medium and large parts. They are driven by a linear vibrating base, whose model varies according to the size of the hopper itself.
</p>

The standard machine is made up of the following main parts:

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
.tr-tabs{display:flex;gap:6px;margin-bottom:12px}
.tr-tab{padding:5px 14px;border-radius:6px;border:1.5px solid var(--bd);background:#fff;font-size:13px;font-weight:600;color:var(--tx2);cursor:pointer;transition:background var(--tr),color var(--tr),border-color var(--tr)}
.tr-tab:hover{background:var(--bg-h)}
.tr-tab.on{background:var(--acc-bg);color:var(--acc-dk);border-color:var(--acc)}

/* ── Panel ── */
.tr-panel{display:none}
.tr-panel.on{display:block}
.tr-wrap{border:1px solid var(--bd);border-radius:var(--r);overflow:hidden;background:var(--bg-p);box-shadow:0 2px 12px rgba(0,0,0,0.07)}
.tr-img-outer{position:relative;width:100%;padding-top:70.71%}
.tr-img-outer img{position:absolute;inset:0;width:100%;height:100%;object-fit:contain;padding:0;transition:opacity var(--tr)}
.tr-img-base{opacity:1;z-index:1}
.tr-img-hl{opacity:0;z-index:2}
.tr-badge{position:absolute;top:12px;left:14px;z-index:3;background:var(--acc);color:#fff;font-size:12px;font-weight:600;padding:4px 10px;border-radius:20px;opacity:0;transform:translateY(-4px);transition:opacity var(--tr),transform var(--tr);pointer-events:none;white-space:nowrap}
.tr-badge.on{opacity:1;transform:translateY(0)}
.tr-hint{position:absolute;bottom:14px;left:50%;z-index:3;transform:translateX(-50%);font-size:13px;color:#fff;background:rgba(0,0,0,0.38);padding:6px 16px;border-radius:20px;pointer-events:none;transition:opacity var(--tr);white-space:nowrap}
.tr-list-panel{border-top:1px solid var(--bd);background:var(--bg-p)}
.tr-list-head{display:grid;grid-template-columns:40px 160px 1fr;gap:8px;padding:8px 14px;background:var(--bg-s);border-bottom:1px solid var(--bd);font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:.05em;color:var(--tx3)}
.tr-row{display:grid;grid-template-columns:40px 160px 1fr;gap:8px;align-items:center;padding:9px 14px;border-bottom:1px solid var(--bd);cursor:pointer;transition:background var(--tr);user-select:none}
.tr-row:last-child{border-bottom:none}
.tr-row:hover{background:var(--bg-h)}
.tr-row.on{background:var(--acc-bg)}
.tr-bubble{width:26px;height:26px;border-radius:50%;border:1.5px solid var(--bd);background:#fff;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:600;color:var(--tx2);flex-shrink:0;transition:background var(--tr),color var(--tr),border-color var(--tr)}
.tr-row.on .tr-bubble{background:var(--acc);color:#fff;border-color:var(--acc)}
.tr-name{font-size:13px;font-weight:500;color:var(--tx1);transition:color var(--tr)}
.tr-row.on .tr-name{color:var(--acc-dk)}
.tr-desc{font-size:12px;color:var(--tx2);line-height:1.55}
.tr-desc a{color:var(--acc);text-decoration:underline}
</style>

<!-- Tab bar -->
<div class="tr-tabs">
  <button class="tr-tab on"    onclick="trSwitchTab('tramoggia',this)">Vibrating hopper</button>
</div>

<!-- ══════════ TRAMOGGIA ══════════ -->
<div class="tr-panel on" id="tr-panel-tramoggia">
  <div class="tr-wrap">
    <div class="tr-img-outer">
      <img class="tr-img-base" id="tramoggia-img-base" src="../../../../../_shared/media/images/tramoggia0.PNG" alt="Hopper view" />
      <img class="tr-img-hl"   id="tramoggia-img-hl"   src="" alt="" aria-hidden="true" />
      <div class="tr-badge" id="tramoggia-badge"></div>
      <div class="tr-hint"  id="tramoggia-hint">Select a component from the list</div>
    </div>
    <div class="tr-list-panel">
      <div class="tr-list-head"><span>No.</span><span>Component</span><span>Description</span></div>
      <div id="tramoggia-list"></div>
    </div>
  </div>
</div>

<script>
(function(){

  /* ── component data ── */
  var models = {
    tramoggia: {
      imgPath: '../../../../../_shared/media/images/tramoggia',
      imgExt: '.PNG',
      comps: [
        {n:1,  name:'Support',        desc:'This is the component that is bracketed to the machine and on which the hopper is positioned.'},
        {n:2,  name:'Vibrating base',    desc:'This is the main component of the hopper; by means of an electromagnet it produces the vibration that allows the parts to advance on the bowl.'},
        {n:3,  name:'Bowl',            desc:'It can be 1.5 l, 5 l, 10 l, 20 l or 40 l depending on the component to be processed. Custom sizes can also be made on request. The 1.5 l bowl is made of plastic material while the others are made of stainless steel.'},
        {n:4,  name:'Controller',       desc:'It is used to adjust the vibration of the hopper.'},
        {n:5,  name:'Cover',           desc:'Protection components for the vibrating base against impacts, dirt and dust.'},
      ]
    },
  };

  /* ── state per model ── */
  var state = {};
  Object.keys(models).forEach(function(id){ state[id]={activeN:null,activeRow:null}; });

  /* ── builds the lists ── */
  Object.keys(models).forEach(function(id){
    var m   = models[id];
    var el  = document.getElementById(id+'-list');
    m.comps.forEach(function(c){
      var row = document.createElement('div');
      row.className = 'tr-row';
      row.innerHTML = '<div class="tr-bubble">'+c.n+'</div>'
                    + '<div class="tr-name">'+c.name+'</div>'
                    + '<div class="tr-desc">'+c.desc+'</div>';
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
  window.trSwitchTab = function(id, btn){
    document.querySelectorAll('.tr-panel.on').forEach(function(p){
      var oldId = p.id.replace('tr-panel-','');
      reset(oldId);
    });
    document.querySelectorAll('.tr-tab').forEach(function(b){ b.classList.remove('on'); });
    document.querySelectorAll('.tr-panel').forEach(function(p){ p.classList.remove('on'); });
    btn.classList.add('on');
    document.getElementById('tr-panel-'+id).classList.add('on');
  };

})();
</script>
:::

:::{attention}
In the case of custom models, the components may differ, partially or totally, from those indicated. For models of this kind, refer to the technical project file. 
:::

## Components and Operation

* **Base structure:** The linear vibrating base is made up of two bodies joined together by leaf springs.
* **Vibration mechanism:** Operation relies on an electromagnet integral with the fixed body that attracts and releases the moving body. This action generates the vibration that allows the parts contained inside the bowl (positioned on the moving body and locked by means of clamps) to advance.
* **Electrical control:** To fulfil this purpose the vibrators require a controller that converts alternating current into pulse current, as well as adjusting the speed of the system itself.

---

## Intended Use 

The hopper is available in six base models. Custom models, derived from the base ones but different in terms of size and performance, can be made after discussion of the user's requirements. 

:::{note} 
**Validity note:** The information contained in this manual is also to be considered valid for custom models.
:::

**Capacity of the available standard models:**

| Base Model | Bowl Capacity | Load Capacity |
|:--- |:--- | :--- | 
| **Model 1** | 1.5 liters | 1 kg | 
| **Model 2** | 3 liters | 1.5 kg | 
| **Model 3** | 5 liters | 6 kg |
| **Model 4** | 10 liters | 6 kg |
| **Model 5** | 20 liters | 6 kg |
| **Model 6** | 40 liters | 15 kg |


The machine in question is intended for industrial use for: 

::::{list-table}
:widths: 25 25 25 25
:header-rows: 1
:class: custom-safety-table

* - <span style="font-weight: bold; color: #2c3e50;">Operation</span>
  - <span style="font-weight: bold; color: #27ae60;">Allowed</span>
  - <span style="font-weight: bold; color: #c0392b;">Not Allowed</span>
  - <span style="font-weight: bold; color: #2c3e50;">Working environment</span>

* - <div style="padding: 8px 0;"><span style="font-weight: 600; text-transform: uppercase; font-size: 0.9em; ">Handling for the purpose of feeding:</span></div>
  - <div style="background-color: #e8f8f5; border-left: 4px solid #2ecc71; padding: 10px; margin: 5px 0; border-radius: 4px; font-size: 0.95em; color: #117a65;">
      Components whose maximum weight and dimensions vary according to the machine model.
    </div>
  - <div style="background-color: #fdf2f2; border-left: 4px solid #e74c3c; padding: 10px; margin: 5px 0; border-radius: 4px; font-size: 0.95em; color: #78281f;">
      Any other component not included within the allowed maximum weight and dimension range.
    </div>
  - <div style="background-color: #f4f6f7; padding: 10px; margin: 5px 0; border-radius: 4px; font-size: 0.95em; text-align: center; font-weight: 500; color: #566573;">
      Industrial
    </div>
::::

:::{IMPORTANT}
For more information on the type of components allowed, see the “Technical data” paragraph of this manual.
:::

<div style="display: flex; flex-direction: column; gap: 20px; margin: 20px 0;">

  <!-- Card 1: Intended Purpose -->
  <div style="border-left: 5px solid #2980b9; background-color: #ebf5fb; padding: 20px; border-radius: 4px 8px 8px 4px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
    <h3 style="color: #2980b9; margin-top: 0; font-size: 1.2em; border-bottom: none;"> Intended Purpose</h3>
    <p style="margin-bottom: 10px; color: #2c3e50;">The machine was created to:</p>
    <ul style="color: #34495e; margin-bottom: 0; padding-left: 20px;">
      <li style="margin-bottom: 5px;">meet the <strong>specific requirements</strong> mentioned in the sales contract;</li>
      <li>be used according to the <strong>instructions and limits of use</strong> given in this manual.</li>
    </ul>
  </div>

  <!-- Card 2: Safety Conditions -->
  <div style="border-left: 5px solid #27ae60; background-color: #eafaf1; padding: 20px; border-radius: 4px 8px 8px 4px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
    <h3 style="color: #27ae60; margin-top: 0; font-size: 1.2em; border-bottom: none;"> Safety Conditions</h3>
    <p style="margin-bottom: 10px; color: #2c3e50;">The machine is designed and built to work safely <strong>only if</strong>:</p>
    <ul style="color: #34495e; margin-bottom: 0; padding-left: 20px;">
      <li style="margin-bottom: 5px;">it is used within the limits declared in the contract and in this manual;</li>
      <li style="margin-bottom: 5px;">the procedures of the user manual are scrupulously followed;</li>
      <li style="margin-bottom: 5px;">routine maintenance is carried out at the times and in the ways indicated;</li>
      <li style="margin-bottom: 5px;">extraordinary maintenance is promptly carried out when necessary;</li>
      <li><strong style="color: #c0392b;">the safety devices are NEVER removed and/or bypassed.</strong></li>
    </ul>
  </div>

</div>

## Misuse (Reasonably Foreseeable)

<div style="border-left: 5px solid #c0392b; background-color: #fdf2f2; padding: 20px; border-radius: 4px; margin: 15px 0; box-shadow: 0 2px 5px rgba(0,0,0,0.03);">
  <ul style="color: #2c3e50; margin: 0; padding-left: 20px; line-height: 1.6;">
    <li style="margin-bottom: 8px;">Processing liquid components and fine grit;</li>
    <li style="margin-bottom: 8px;">Changing working parameters that compromise safety;</li>
    <li style="margin-bottom: 8px;">Transporting people;</li>
    <li style="margin-bottom: 8px;">Using the machine as a support point;</li>
    <li style="margin-bottom: 8px;">Using the machine so as to obtain production values higher than the prescribed limits;</li>
    <li style="margin-bottom: 8px;">Modifying / tampering with the electrical and pneumatic connections of the machine or any other of its components;</li>
    <li style="margin-bottom: 8px;">Using the machine with a product other than the one listed in the “Intended use (correct)”;</li>
    <li style="margin-bottom: 0;">Using the machine differently from what is provided for in the “Intended use (correct)” paragraph.</li>
  </ul>
</div>

:::{warning}
Any use of the machine other than that intended must be authorized in writing in advance by the Manufacturer. In the absence of such written authorization, the use is to be considered “improper use”; therefore the Manufacturer declines all liability for any damage caused to property or persons and considers any type of warranty on the machine void.  
:::

:::{important}
Improper use of the machine excludes any liability of the Manufacturer.
:::

## Obligations and Prohibitions 

### Obligations of the users 

The user (entrepreneur or employer) must:

<div style="border-left: 5px solid #2980b9; background-color: #ebf5fb; padding: 20px; border-radius: 4px; margin: 15px 0; box-shadow: 0 2px 5px rgba(0,0,0,0.03);">
  <ul style="color: #2c3e50; margin: 0; padding-left: 20px; line-height: 1.6;">
    <li style="margin-bottom: 8px;">Take into account the capabilities and conditions of the operators in relation to their health and safety;</li>
    <li style="margin-bottom: 8px;">Provide personal protective equipment (PPE) suitable for the individual procedures;</li>
    <li style="margin-bottom: 8px;">Provide lifting equipment and procedures that comply with the standards;</li>
    <li style="margin-bottom: 8px;">Require each worker to comply with the company rules and provisions on safety and on the use of the collective and personal protective equipment made available to them;</li>
    <li style="margin-bottom: 8px;">Instruct the personnel on the procedures to follow in the event of an accident;</li>
    <li style="margin-bottom: 8px;">Instruct the personnel on the residual risks present;</li>
    <li style="margin-bottom: 8px;">Instruct the personnel on the devices provided for operator safety;</li>
    <li style="margin-bottom: 8px;">Instruct the personnel on the risks of noise emission in the working environment;</li>
    <li style="margin-bottom: 0;">Instruct the personnel on the general accident-prevention rules laid down by European directives and by the legislation of the country of destination of the machine.</li>
  </ul>
</div>

:::{note} 
Allow only personnel who have read this manual and have been properly trained to operate the machine.
:::

### Obligations of the assigned personnel (operators/maintenance technicians/technicians)

The personnel must:

<div style="border-left: 5px solid #27ae60; background-color: #eafaf1; padding: 20px; border-radius: 4px; margin: 15px 0; box-shadow: 0 2px 5px rgba(0,0,0,0.03);">
  <ul style="color: #2c3e50; margin: 0; padding-left: 20px; line-height: 1.6;">
    <li style="margin-bottom: 8px;"><strong>Always carry out maintenance work with the machine switched off.</strong> Never lubricate moving parts;</li>
    <li style="margin-bottom: 8px;">When the machine is running, avoid working nearby wearing chains, bracelets, ties or other garments that may get caught in the mechanisms;</li>
    <li style="margin-bottom: 8px;">Long hair must be tied back to avoid the risk of entanglement;</li>
    <li style="margin-bottom: 8px;">Carry out work on the electrical panel, junction boxes, cables and electrical components <strong>only with the main switch off</strong>;</li>
    <li style="margin-bottom: 8px;">Make sure that no one is inside the danger zones before starting the machine;</li>
    <li style="margin-bottom: 8px;">Pay the utmost attention during operation so that no one can directly access the moving parts;</li>
    <li style="margin-bottom: 8px;">Use the protective devices provided by the employer appropriately;</li>
    <li style="margin-bottom: 0;">Immediately report to the employer, manager or supervisor any deficiency or anomaly in the safety devices.</li>
  </ul>
</div>

### Prohibitions for the assigned personnel 

In particular, the personnel must not:

<div style="border-left: 5px solid #c0392b; background-color: #fdf2f2; padding: 20px; border-radius: 4px; margin: 15px 0; box-shadow: 0 2px 5px rgba(0,0,0,0.03);">
  <ul style="color: #2c3e50; margin: 0; padding-left: 20px; line-height: 1.6;">
    <li style="margin-bottom: 8px;">Use the machine improperly (i.e. for uses other than those indicated in the “Intended Use” paragraph);</li>
    <li style="margin-bottom: 8px;">Remove or modify the safety or signalling devices without prior authorization;</li>
    <li style="margin-bottom: 8px;">Carry out on their own initiative operations or maneuvers outside their competence or that may compromise their own safety or that of other workers;</li>
    <li style="margin-bottom: 8px;">Wear bracelets, rings or chains that may dangle and be dragged by moving parts;</li>
    <li style="margin-bottom: 8px;">Replace or modify the speeds of the machine components without the explicit consent of a supervisor;</li>
    <li style="margin-bottom: 8px;">Modify the programmed cycle of the machine in any way;</li>
    <li style="margin-bottom: 8px;">Modify the electrical connections with the aim of excluding or bypassing the internal safety devices;</li>
    <li style="margin-bottom: 8px;">Use the machine if it has not been installed in full compliance with the regulations in force;</li>
    <li style="margin-bottom: 8px;">Use the machine as a support point, even if not operating (risk of the operator falling and/or damage to the structure);</li>
    <li style="margin-bottom: 0;">Use the machine outside the permitted environmental conditions (see “Chapter 5”).</li>
  </ul>
</div>

:::{attention}
ARS S.r.l. is not liable for damage caused to property or persons in the event that:  
•	it is found that the machine has been used in one of the non-permitted environments;  
•	the obligations and prohibitions described here have not been complied with.  
:::

## Technical Data 

```{list-table}
:header-rows: 1
:widths: 20 30 25 25

* - Hopper Size
  - Power supply
  - Frequency / Phase
  - Current draw (A)
* - 1.5 l
  - 230Vac ±5% (115Vac on request)
  - 50-60 Hz / single-phase
  - 0.1
* - 3 l
  - 230Vac ±5% (115Vac on request)
  - 50-60 Hz / single-phase
  - 0.1
* - 5 l
  - 230Vac ±5% (115Vac on request)
  - 50-60 Hz / single-phase
  - 0.25
* - 10 l
  - 230Vac ±5% (115Vac on request)
  - 50-60 Hz / single-phase
  - 0.25
* - 20 l
  - 230Vac ±5% (115Vac on request)
  - 50-60 Hz / single-phase
  - 0.25
* - 40 l
  - 230Vac ±5% (115Vac on request)
  - 50-60 Hz / single-phase
  - 0.45
```

| Hopper Size | 1.5 l | 3 l | 5 l | 10 l | 20 l | 40 l |
|------------------------------|--------|------|------|-------|-------|-------|
| Corresponding net weight | 11 Kg | 18 Kg | 22 Kg | 24 Kg | 27 Kg | 38 Kg |

:::{attention}
In the case of custom models, the values indicated may differ from those in the table. For models of this kind, refer to the technical project file. 
:::

## Layout 

![Hopper dimensions](../../../../../_shared/media/images/dim_tramoggia.jpg)

| Dimensions | 1.5 l | 3 l | 5 l | 10 l | 20 l | 40 l |
|------------|--------|------|------|-------|-------|-------|
| A | 350 mm | 525 mm | 435 mm | 630 mm | 760 mm | 780 mm |
| B | 65 mm | 98 mm | 135 mm | 135 mm | 180 mm | 260 mm |
| C | 90 mm | 97 mm | 140 mm | 140 mm | 220 mm | 280 mm |
| D | 211 mm | 218 mm | 247 mm | 247 mm | 262 mm | 290 mm |

:::{attention}
In the case of custom models, the values indicated may differ from those in the table. For models of this kind, refer to the technical project file. 
:::


## Standard and Optional Components 

```{list-table} Hopper Accessories and Equipment
:widths: 20 40 25 15
:header-rows: 1

* - **Item**
  - **Description**
  - **Photo**
  - **Standard / Optional**

* - Emptying door
  - Rear discharge door for quick emptying
  - 
    :::{image} ../../../../../_shared/media/images/sportello_svuotamento.jpg
    :alt: Emptying door
    :width: 120px
    :align: center
    :::
  - STANDARD (1.5 l hopper excluded)

* - Dosing barrier
  - Barrier dosing device for flow regulation (adjustable)
  - 
    :::{image} ../../../../../_shared/media/images/barriera_dosatrice.jpg
    :alt: Dosing barrier
    :width: 120px
    :align: center
    :::
  - OPTIONAL (1.5 l hopper excluded)

* - Safety guard
  - Safety guard for hands
  - 
    :::{image} ../../../../../_shared/media/images/protezione_sicurezza.jpg
    :alt: Safety guard
    :width: 120px
    :align: center
    :::
  - OPTIONAL (1.5 l hopper excluded)

* - Coating
  - Polyurethane bowl coating
  - 
    :::{image} ../../../../../_shared/media/images/rivestimento.png
        :alt: Coating
        :width: 120px
        :align: center
    :::
  - OPTIONAL (1.5 l hopper excluded)

* - Front photocell
  - Its function is to check the presence of components in the front area of the vibrating bowl during the feeding process. For more information refer to Appendix A: “Frontal and Rear Photocells”.
  - 
    :::{image} ../../../../../_shared/media/images/fotocellula_frontale.png
        :alt: Front photocell
        :width: 120px
        :align: center
    :::
  - OPTIONAL (1.5 l hopper excluded)

* - Rear photocell
  - Its function is to monitor the level of the parts inside the bowl. For more information refer to Appendix A: “Frontal and Rear Photocells”.
  - 
    :::{image} ../../../../../_shared/media/images/fotocellula_posteriore.png
        :alt: Rear photocell
        :width: 120px
        :align: center
    :::
  - OPTIONAL (1.5 l hopper excluded)

```

### Processing cycle 

The processing cycle, divided into the following operating phases, is described below in a simplified manner:

<div style="display: flex; flex-direction: column; gap: 15px; margin: 20px 0; position: relative;">

  <!-- Phase 1 -->
  <div style="display: flex; background-color: #f8f9fa; border-radius: 8px; border: 1px solid #e9ecef; overflow: hidden; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
    <div style="background-color: #2c3e50; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 60px; font-size: 1.4em; font-weight: bold; flex-shrink: 0;">
      1
    </div>
    <div style="padding: 15px 20px; display: flex; align-items: center; color: #2c3e50; line-height: 1.5;">
      <span>The operator places the product to be processed inside the bowl, manually or with an automatic loading system.</span>
    </div>
  </div>

  <!-- Phase 2 -->
  <div style="display: flex; background-color: #f8f9fa; border-radius: 8px; border: 1px solid #e9ecef; overflow: hidden; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
    <div style="background-color: #34495e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 60px; font-size: 1.4em; font-weight: bold; flex-shrink: 0;">
      2
    </div>
    <div style="padding: 15px 20px; display: flex; align-items: center; color: #2c3e50; line-height: 1.5;">
      <span>The hopper cyclically performs vibrations (set by the operator) to allow the parts to advance, so as to constantly ensure their presence on the feeder.</span>
    </div>
  </div>

</div>