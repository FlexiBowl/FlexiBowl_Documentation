(intele)=
# **Interface électrique**

Le panneau de connecteurs du FlexiBowl® varie en fonction de la version de la machine :

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
  <button class="ie-tab on" onclick="ieSwitchTab('smallpanel',this)">Panneau FlexiBowl® 200-350</button>
  <button class="ie-tab"    onclick="ieSwitchTab('rack',this)">Rack</button>
  <button class="ie-tab"    onclick="ieSwitchTab('stpanel',this)">Panneau Standard</button>
  <button class="ie-tab"    onclick="ieSwitchTab('encpanel',this)">Panneau Circular Tracking</button>
</div>
<!-- ══════════ PANNELLO FB200-350 ══════════ -->
<div class="ie-panel on" id="ie-panel-smallpanel">
  <div class="ie-wrap">
    <div class="ie-img-outer">
      <img class="ie-img-base" id="smallpanel-img-base" src="../../../../_shared/media/images/smallpanel0.PNG" alt="Panneau FlexiBowl® 200-350" />
      <img class="ie-img-hl"   id="smallpanel-img-hl"   src="" alt="" aria-hidden="true" />
      <div class="ie-badge" id="smallpanel-badge"></div>
      <div class="ie-hint"  id="smallpanel-hint">Sélectionner un connecteur dans la liste</div>
    </div>
    <div class="ie-list-panel">
      <div class="ie-list-head"><span>N°</span><span>Connecteur</span><span>Description</span></div>
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
      <div class="ie-hint"  id="rack-hint">Sélectionner un connecteur dans la liste</div>
    </div>
    <div class="ie-list-panel">
      <div class="ie-list-head"><span>N°</span><span>Connecteur</span><span>Description</span></div>
      <div id="rack-list"></div>
    </div>
  </div>
</div>
<!-- ══════════ PANNELLO STANDARD ══════════ -->
<div class="ie-panel" id="ie-panel-stpanel">
  <div class="ie-wrap">
    <div class="ie-img-outer">
      <img class="ie-img-base" id="stpanel-img-base" src="../../../../_shared/media/images/stpanel0.PNG" alt="Panneau Standard FlexiBowl®" />
      <img class="ie-img-hl"   id="stpanel-img-hl"   src="" alt="" aria-hidden="true" />
      <div class="ie-badge" id="stpanel-badge"></div>
      <div class="ie-hint"  id="stpanel-hint">Sélectionner un connecteur dans la liste</div>
    </div>
    <div class="ie-list-panel">
      <div class="ie-list-head"><span>N°</span><span>Connecteur</span><span>Description</span></div>
      <div id="stpanel-list"></div>
    </div>
  </div>
</div>
<!-- ══════════ PANNELLO FLEXITRACKING ══════════ -->
<div class="ie-panel" id="ie-panel-encpanel">
  <div class="ie-wrap">
    <div class="ie-img-outer">
      <img class="ie-img-base" id="encpanel-img-base" src="../../../../_shared/media/images/encpanel0.PNG" alt="Panneau Circular Tracking FlexiBowl®" />
      <img class="ie-img-hl"   id="encpanel-img-hl"   src="" alt="" aria-hidden="true" />
      <div class="ie-badge" id="encpanel-badge"></div>
      <div class="ie-hint"  id="encpanel-hint">Sélectionner un connecteur dans la liste</div>
    </div>
    <div class="ie-list-panel">
      <div class="ie-list-head"><span>N°</span><span>Connecteur</span><span>Description</span></div>
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
        {n:1, name:'C-A SIGNAL', desc:'Connecteur C-A signal'},
        {n:2, name:'C-B SIGNAL', desc:'Connecteur C-B signal'},
        {n:3, name:'MOTOR',      desc:'Connecteur du câble moteur'},
        {n:4, name:'C-ETH FB',   desc:'Connexion Ethernet vers le rack'},
        {n:5, name:'AIR SUPPLY', desc:'Entrée d’air'}
      ]
    },
    rack: {
      imgPath: '../../../../_shared/media/images/rack',
      imgExt: '.PNG',
      comps: [
        {n:1, name:'POWER SUPPLY', desc:'Prise d’alimentation et interrupteur ; comprend également un filtre CEI'},
        {n:2, name:'STO',          desc:'Connecteur STO'},
        {n:3, name:'MOTOR',        desc:'Connecteur du câble moteur'},
        {n:4, name:'C-A SIGNAL',   desc:'Connecteur C-A signal'},
        {n:5, name:'C-B SIGNAL',   desc:'Connecteur C-B signal'},
        {n:6, name:'C-ETH IN',     desc:'Connecteur Ethernet'},
        {n:7, name:'HOPPER',       desc:'Connecteur Bulk Feeder'},
        {n:8, name:'C-ETH FB',     desc:'Connexion Ethernet au FlexiBowl®'}
      ]
    },
    stpanel: {
      imgPath: '../../../../_shared/media/images/stpanel',
      imgExt: '.PNG',
      comps: [
        {n:1, name:'POWER SUPPLY', desc:'Prise d’alimentation et interrupteur ; comprend également un filtre CEI'},
        {n:2, name:'AIR SUPPLY',   desc:'Entrée d’air'},
        {n:3, name:'LIGHT ON',     desc:'LED d’état du rétroéclairage'},
        {n:4, name:'READY/FAULT',  desc:'LED d’état Ready/Fault'},
        {n:5, name:'HOPPER',       desc:'Connecteur Bulk Feeder'},
        {n:6, name:'C-ETH',        desc:'Connecteur Ethernet'},
        {n:7, name:'STO',          desc:'Connecteur STO'}
      ]
    },
    encpanel: {
      imgPath: '../../../../_shared/media/images/encpanel',
      imgExt: '.PNG',
      comps: [
        {n:1, name:'POWER SUPPLY', desc:'Prise d’alimentation et interrupteur ; comprend également un filtre CEI'},
        {n:2, name:'LIGHT ON',     desc:'LED d’état du rétroéclairage'},
        {n:3, name:'READY/FAULT',  desc:'LED d’état Ready/Fault'},
        {n:4, name:'HOPPER',       desc:'Connecteur Bulk Feeder'},
        {n:5, name:'C-ETH',        desc:'Connecteur Ethernet'},
        {n:6, name:'ENCODER',      desc:'Passage du câble de l’encodeur'},
        {n:7, name:'AIR SUPPLY',   desc:'Entrée d’air'},
        {n:8, name:'I/O',          desc:'Connecteur E/S'},
        {n:9, name:'STO',          desc:'Connecteur STO'}
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
Avant d'effectuer toute connexion électrique, s'assurer que l'alimentation est coupée et que le système est en état de sécurité.
:::

:::{important}
Laisser environ {ref}`100 mm d'espace libre <dim800>` autour des connecteurs d'alimentation pour faciliter les opérations de câblage et de maintenance.
:::

L'interface électrique du FlexiBowl® change en fonction de la taille de la machine :

- **FlexiBowl® 500 – 1200** : tous les connecteurs (STO, Ethernet, Hopper, alimentation, air) se trouvent sur un unique **panneau électrique standard**, monté directement sur la machine.
- **FlexiBowl® 200 / 350** : les connecteurs principaux se trouvent sur un **rack** externe ; le rack est ensuite raccordé à la machine au moyen de 4 câbles dédiés (Ethernet, Moteur+STO, signal A, signal B). Il ne reste à raccorder sur la machine que l'air comprimé.

---

(pannello-standard)=
## FlexiBowl® 500 – 1200 — Panneau électrique standard

```{list-table}
:widths: 8 52 40
:header-rows: 1

* - #
  - Action
  - Image
* - 1
  - **Raccorder le STO.**

    Connecteur 10 broches. Nécessaire pour activer le moteur.

    <div class="ars-step-note">
    Les entrées <strong>+STO1</strong> et <strong>+STO2</strong> doivent recevoir <strong>+24 Vdc</strong> du circuit de sécurité ; <strong>−STO1</strong> et <strong>−STO2</strong> doivent être raccordées à la référence −24 Vdc.
    </div>

    <details class="ars-dropdown"><summary>Brochage du connecteur STO (10 broches)</summary><div class="ars-dropdown-body">

    | Broche | Description |
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
    :alt: Raccorder le STO
    :class: ars-zoom-img
    ```

* - 2
  - **Raccorder l'Ethernet (C-ETH).**

    Connecteur M12, codage D. Il permet la communication avec le FlexiBowl®, également accessible via navigateur web.

    <div class="ars-step-attn">
    Lorsque le FlexiBowl® est alimenté, la connexion Ethernet est <strong>obligatoire</strong> : si elle est absente, la machine passe à l'état <strong>ERROR</strong> (LED Ready/Fault rouge).
    </div>

    <details class="ars-dropdown"><summary>Brochage M12 → RJ45</summary><div class="ars-dropdown-body">

    Adaptateur M12 8 pôles → RJ45 :

    | Broche RJ45 | Signal | Fonction | Couleur |
    |---|---|---|---|
    | 1 | TD+ | Transmission de données (+) | Jaune |
    | 2 | TD− | Transmission de données (−) | Orange |
    | 3 | RD+ | Réception de données (+) | Blanc |
    | 4 | NC | Non affecté | — |
    | 5 | NC | Non affecté | — |
    | 6 | RD− | Réception de données (−) | Bleu |
    | 7 | NC | Non affecté | — |
    | 8 | NC | Non affecté | — |

    Connecteur M12 codage D 4 pôles :

    | Broche M12 | Signal | Fonction | Couleur |
    |---|---|---|---|
    | 1 | TD+ | Transmission de données (+) | Jaune |
    | 2 | RD+ | Réception de données (+) | Blanc |
    | 3 | TD− | Transmission de données (−) | Orange |
    | 4 | RD− | Réception de données (−) | Bleu |

    </div></details>
  -
    ```{image} ../../../../_shared/media/images/stpanel6.PNG
    :alt: Raccorder l'Ethernet
    :class: ars-zoom-img
    ```

* - 3
  - **Raccorder le Hopper.**

    Connecteur M12 codage A, utilisé pour communiquer avec les contrôleurs hopper ARS via le protocole **Modbus RTU**.

    <details class="ars-dropdown"><summary>Brochage M12 codage A</summary><div class="ars-dropdown-body">

    | Broche M12 | Signal | Fonction | Couleur |
    |---|---|---|---|
    | 1 | A+ | Ligne de données RS485 (+) | Marron |
    | 2 | NC | Non affecté | Blanc |
    | 3 | B− | Ligne de données RS485 (−) | Bleu |
    | 4 | GND | Référence commune | Noir |
    | 5 | NC | Non affecté | Gris |

    </div></details>
  -
    ```{image} ../../../../_shared/media/images/stpanel5.PNG
    :alt: Raccorder le Hopper
    :class: ars-zoom-img
    ```

* - 4
  - **Raccorder l'alimentation (Power Supply) — en dernier.**

    Connecteur fourni en dotation, identifié par l'inscription **POWER SUPPLY**. Le bouton d'alimentation permet d'allumer/éteindre l'appareil.

    <div class="ars-step-attn">
    S'assurer que le FlexiBowl® est <strong>éteint</strong> avant de raccorder l'alimentation, et que l'appareil est relié à la terre.
    </div>

    <div class="ars-step-warn">
    Tension admise : <strong>120–230 Vac, 50/60 Hz</strong>.
    </div>

    <div class="ars-step-note">
    Le connecteur d'alimentation est équipé d'un support pour <strong>2 fusibles</strong>, destinés à la protection contre d'éventuelles anomalies électriques. Au premier démarrage, toujours en vérifier l'état avant d'allumer l'appareil.
    </div>

    <details class="ars-dropdown"><summary>Schéma de brochage du câble d'alimentation</summary><div class="ars-dropdown-body">

    | Couleur | Type | Étiquette |
    |---|---|---|
    | Marron | Phase | L1 |
    | Bleu | Neutre | N1 |
    | Jaune/Vert | Terre | PE1 |

    </div></details>
  -
    ```{image} ../../../../_shared/media/images/stpanel1.PNG
    :alt: Raccorder l'alimentation
    :class: ars-zoom-img
    ```

```

:::{note}
Après la mise sous tension, toujours vérifier l'état de la machine au moyen des **LED d'état** situées sur le panneau frontal — voir la section {ref}`LED d'état <led-stato>` plus bas dans cette page.
:::

:::{tip}
Les câbles d'alimentation et Ethernet sont disponibles en option dans les longueurs de 3, 5 et 10 m : voir {ref}`cavo-alim` et {ref}`cavo-eth`.
:::

---

(rack-esterno)=
## FlexiBowl® 200 / 350 — Rack externe

Les modèles FlexiBowl® FB 200 et FB 350 sont dotés d'un **Rack** externe, contenant tous les dispositifs électroniques nécessaires au fonctionnement. Les connecteurs vers les installations du client se trouvent sur le rack (et non sur la machine) et ont le **même brochage** que les connecteurs correspondants du panneau standard, simplement positionnés sur un boîtier externe.

### Raccordements sur le rack

```{list-table}
:widths: 8 52 40
:header-rows: 1

* - #
  - Action
  - Image
* - 1
  - **Raccorder le STO** sur le rack.

    Connecteur 10 broches, même fonction et même brochage que le panneau standard.

    <div class="ars-step-note">
    Les entrées <strong>+STO1</strong> et <strong>+STO2</strong> doivent recevoir <strong>+24 Vdc</strong> du circuit de sécurité ; <strong>−STO1</strong> et <strong>−STO2</strong> doivent être raccordées à la référence −24 Vdc.
    </div>

    <details class="ars-dropdown"><summary>Brochage du connecteur STO (10 broches)</summary><div class="ars-dropdown-body">

    | Broche | Description |
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
    :alt: Raccorder le STO
    :class: ars-zoom-img
    ```

* - 2
  - **Raccorder le C-ETH IN** sur le rack.

    Connecteur M12, codage D.

    <div class="ars-step-attn">
    Connexion <strong>obligatoire</strong> lorsque la machine est alimentée : si elle est absente, la machine passe en ERROR (LED Ready/Fault rouge).
    </div>

    <details class="ars-dropdown"><summary>Brochage M12 → RJ45</summary><div class="ars-dropdown-body">

    Adaptateur M12 8 pôles → RJ45 :

    | Broche RJ45 | Signal | Fonction | Couleur |
    |---|---|---|---|
    | 1 | TD+ | Transmission de données (+) | Jaune |
    | 2 | TD− | Transmission de données (−) | Orange |
    | 3 | RD+ | Réception de données (+) | Blanc |
    | 4 | NC | Non affecté | — |
    | 5 | NC | Non affecté | — |
    | 6 | RD− | Réception de données (−) | Bleu |
    | 7 | NC | Non affecté | — |
    | 8 | NC | Non affecté | — |

    Connecteur M12 codage D 4 pôles :

    | Broche M12 | Signal | Fonction | Couleur |
    |---|---|---|---|
    | 1 | TD+ | Transmission de données (+) | Jaune |
    | 2 | RD+ | Réception de données (+) | Blanc |
    | 3 | TD− | Transmission de données (−) | Orange |
    | 4 | RD− | Réception de données (−) | Bleu |

    </div></details>
  -
    ```{image} ../../../../_shared/media/images/rack6.PNG
    :width: 110%
    :alt: Panneau du rack
    :class: ars-zoom-img
    ```

* - 3
  - **Raccorder le Hopper** sur le rack.

    Connecteur M12 codage A, protocole **Modbus RTU**.

    <details class="ars-dropdown"><summary>Brochage M12 codage A</summary><div class="ars-dropdown-body">

    | Broche M12 | Signal | Fonction | Couleur |
    |---|---|---|---|
    | 1 | A+ | Ligne de données RS485 (+) | Marron |
    | 2 | NC | Non affecté | Blanc |
    | 3 | B− | Ligne de données RS485 (−) | Bleu |
    | 4 | GND | Référence commune | Noir |
    | 5 | NC | Non affecté | Gris |

    </div></details>
  -
    ```{image} ../../../../_shared/media/images/rack7.PNG
    :width: 110%
    :alt: Panneau du rack
    :class: ars-zoom-img
    ```

* - 4
  - **Raccorder l'alimentation** sur le rack — en dernier.

    Prise de courant avec interrupteur ; elle comprend également un filtre IEC.

    <div class="ars-step-attn">
    S'assurer que le FlexiBowl® est <strong>éteint</strong> avant de raccorder l'alimentation.
    </div>

    <div class="ars-step-warn">
    Tension admise : <strong>120–230 Vac, 50/60 Hz</strong>.
    </div>

    <div class="ars-step-note">
    Sur le rack également, le connecteur d'alimentation dispose du logement pour les <strong>2 fusibles</strong> de protection : en vérifier l'état au premier démarrage.
    </div>

    <details class="ars-dropdown"><summary>Schéma de brochage du câble d'alimentation</summary><div class="ars-dropdown-body">

    | Couleur | Type | Étiquette |
    |---|---|---|
    | Marron | Phase | L1 |
    | Bleu | Neutre | N1 |
    | Jaune/Vert | Terre | PE1 |

    </div></details>
  -
    ```{image} ../../../../_shared/media/images/rack1.PNG
    :width: 110%
    :alt: Panneau du rack
    :class: ars-zoom-img
    ```
```

(collegamento-rack)=
### Raccordement entre le rack et le FlexiBowl®

Le rack communique avec le FlexiBowl® au moyen de 4 câbles dédiés, chacun devant être raccordé **exclusivement** au port portant l'étiquette correspondante sur le panneau de la machine.

:::{attention}
Raccorder chaque câble au port portant l'**étiquette correspondante** (par ex. MOTOR ↔ MOTOR, C-A SIGNAL ↔ C-A SIGNAL). Un raccordement croisé peut endommager le système.
:::

:::{tip}
Les câbles de 3 m entre le rack et le FlexiBowl® sont inclus dans la fourniture ; les versions de 5 et 10 m sont disponibles en option : voir {ref}`cavo-rack`.
:::

```{list-table}
:widths: 8 52 40
:header-rows: 1

* - #
  - Action
  - Image
* - 5
  - **Raccorder le câble Ethernet (C-ETH FB)** entre le rack et le FlexiBowl®.

    Connecteur M12 codage D.
  -
    ```{image} ../../../../_shared/media/images/rack8.PNG
    :width: 110%
    :alt: Raccorder le câble C-ETH FB
    :class: ars-zoom-img
    ```
    ```{image} ../../../../_shared/media/images/smallpanel4.PNG
    :width: 110%
    :alt: Raccorder le câble C-ETH FB
    :class: ars-zoom-img
    ```
* - 6
  - **Raccorder le câble MOTOR.**

    <div class="ars-step-note">
    Connecteur 9 broches : il véhicule à la fois l'alimentation du moteur et les signaux <strong>STO</strong> vers le FlexiBowl® (sur le rack, STO et Moteur sont des connecteurs séparés ; sur le câble vers la machine, ils sont regroupés en un seul connecteur 9 broches).
    </div>

    <details class="ars-dropdown"><summary>Brochage du connecteur Motor (9 broches)</summary><div class="ars-dropdown-body">

    | Broche | Description |
    |---|---|
    | 1 | +STO1 – Safe Torque Off |
    | 2 | +24 Vdc – Alimentation auxiliaire |
    | 3 | +STO2 – Safe Torque Off |
    | 4 | −24 Vdc – Alimentation auxiliaire |
    | 5 | NC |
    | 6 | +48 Vdc – Motor Power |
    | 7 | −STO1 – Safe Torque Off |
    | 8 | −48 Vdc – Motor Power |
    | 9 | −STO2 – Safe Torque Off |

    </div></details>
  -
    ```{image} ../../../../_shared/media/images/rack3.PNG
    :width: 110%
    :alt: Raccorder le câble Motor
    :class: ars-zoom-img
    ```
    ```{image} ../../../../_shared/media/images/smallpanel3.PNG
    :width: 110%
    :alt: Raccorder le câble C-ETH FB
    :class: ars-zoom-img
    ```
* - 7
  - **Raccorder le câble C-A SIGNAL.**

    Connecteur 12 broches pour les signaux analogiques.

    <details class="ars-dropdown"><summary>Brochage C-A Signal (12 broches)</summary><div class="ars-dropdown-body">

    | Broche | Description |
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
    :alt: Raccorder le câble C-A Signal
    :class: ars-zoom-img
    ```
    ```{image} ../../../../_shared/media/images/smallpanel1.PNG
    :width: 110%
    :alt: Raccorder le câble C-ETH FB
    :class: ars-zoom-img
    ```
* - 8
  - **Raccorder le câble C-B SIGNAL.**

    Connecteur 19 broches pour les signaux numériques, y compris les activations des LED d'état.

    <details class="ars-dropdown"><summary>Brochage C-B Signal (19 broches)</summary><div class="ars-dropdown-body">

    | Broche | Description |
    |---|---|
    | 1 | +24 Vdc – Activation de la LED d'état verte |
    | 2 | −24 Vdc – Commun des LED d'état |
    | 3 | +24 Vdc – Activation de la LED d'état rouge |
    | 4 | +24 Vdc – Activation de la LED d'état du Backlight |
    | 5 | −24 Vdc – Activation de la LED d'état du Backlight |
    | 6 | +24 Vdc – Activation du Backlight |
    | 7 | −24 Vdc – Activation du Backlight |
    | 8 | +24 Vdc – Activation du Flip |
    | 9 | −24 Vdc – Activation du Flip |
    | 10 | +24 Vdc – Activation du Blow |
    | 11 | −24 Vdc – Activation du Blow |
    | 12–19 | NC |

    </div></details>
  -
    ```{image} ../../../../_shared/media/images/rack5.PNG
    :width: 110%
    :alt: Raccorder le câble C-B Signal
    :class: ars-zoom-img
    ```
    ```{image} ../../../../_shared/media/images/smallpanel2.PNG
    :width: 110%
    :alt: Raccorder le câble C-ETH FB
    :class: ars-zoom-img
    ```
```

:::{note}
Après la mise sous tension, toujours vérifier l'état de la machine au moyen des **LED d'état** situées sur le panneau frontal — voir la section {ref}`LED d'état <led-stato>` plus bas dans cette page.
:::

---

(led-stato)=
## LED d'état

Sur le panneau frontal du FlexiBowl® se trouvent deux LED d'état, communes à **toutes les tailles** (500–1200 et 200/350) :

| LED | Couleur | Signification |
|---|---|---|
| **Light ON** | Vert (état unique) | Indique si le backlight embarqué sur le FlexiBowl® est ON ou OFF. Le backlight est utilisé par le système de vision pour éclairer les composants et les rendre reconnaissables. Il peut être activé via le logiciel de vision ou au moyen de commandes provenant d'un système externe communiquant par Ethernet. |
| **Ready / Fault** | Vert | Système opérationnel et exempt d'anomalies. Connexion Ethernet correcte. |
| **Ready / Fault** | Rouge | Anomalie interne ou anomalie de la connexion Ethernet. Se reporter au tableau des anomalies. |

:::{note}
Après la mise sous tension, attendre que la LED **Ready/Fault** s'allume : si le Hopper et le C-ETH sont correctement raccordés, la LED sera **verte**.
:::

---

(io-flexitrack)=
## Option Circular Tracking — Petit panneau d'interface

Le petit panneau fourni avec l'option Circular Tracking ajoute, en plus des connexions déjà décrites, les connecteurs dédiés suivants :

- **Connecteur E/S** : échange de signaux numériques, y compris la fonction Latch.
- **Passe-câble encodeur** : dédié à l'encodeur interne au FlexiBowl®.

```{list-table}
:widths: 8 52 40
:header-rows: 1

* - #
  - Action
  - Image
* - 10
  - **Raccorder le connecteur E/S** à 19 broches.

    <details class="ars-dropdown"><summary>Brochage du connecteur E/S (19 broches)</summary><div class="ars-dropdown-body">

    | Broche | Signal |
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
    :alt: Connecteur E/S Circular Tracking
    :class: ars-zoom-img
    ```
* - 11
  - **Raccorder le passe-câble encodeur**, dédié à l'encodeur interne au FlexiBowl®.
  -
    ```{image} ../../../../_shared/media/images/encpanel8.PNG
    :alt: Passe-câble encodeur Circular Tracking
    :class: ars-zoom-img
    ```
```

---

## Notes et avertissements généraux

:::{attention}
Toutes les opérations de raccordement doivent être effectuées appareil éteint et débranché de l'alimentation.
:::

:::{attention}
Le raccordement à la terre est obligatoire et doit être vérifié avant chaque mise sous tension.
:::

:::{attention}
En cas d'anomalie signalée par la LED rouge (Ready/Fault), se reporter au tableau des anomalies propre au modèle.
:::

:::{attention}
Pour toute information technique complémentaire ou assistance, contacter ARS s.r.l. – FlexiBowl® Division.
:::


