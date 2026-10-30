# **Remplacement des composants électroniques**

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
* - {ref}`Qualification de l'opérateur <operatori>`
  - {ref}`EPI nécessaires <dpi>`

* - **Mainteneur électricien**
  - :::{raw} html
       <div class="ars-img-row">
         <img src="../../../../_shared/media/images/guanti.png" alt="gants">
         <img src="../../../../_shared/media/images/scarpe.png" alt="chaussures">
         <img src="../../../../_shared/media/images/tuta.png" alt="combinaison">
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
      Débrancher l'alimentation électrique avant d'effectuer toute opération à l'intérieur du FlexiBowl®.
    </td>
  </tr>
</table>
::::

## Remplacement des principaux composants électroniques

Dans les tailles plus petites, toute l'électronique est contenue dans le rack, il suffit donc de démonter le panneau supérieur pour accéder à tous les composants. Dans les FlexiBowl® de taille 500 ou supérieure, en revanche, toutes les parties sont contenues dans la machine.

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
  <button class="fb-tab on"    onclick="fbSwitchTab('rack',this)">Électronique dans le rack</button>
  <button class="fb-tab"    onclick="fbSwitchTab('fb',this)">Électronique dans le FlexiBowl®</button>
</div>

<!-- ══════════ rack ══════════ -->
<div class="fb-panel on" id="fb-panel-rack">
  <div class="fb-wrap">
    <div class="fb-img-outer">
      <img class="fb-img-base" id="rack-img-base" src="../../../../_shared/media/images/inrack0.PNG" alt="Électronique dans le rack" />
      <img class="fb-img-hl"   id="rack-img-hl"   src="" alt="" aria-hidden="true" />
      <div class="fb-badge" id="rack-badge"></div>
      <div class="fb-hint"  id="rack-hint">Sélectionner un composant dans la liste</div>
    </div>
    <div class="fb-list-panel">
      <div class="fb-list-head"><span>N°</span><span>Composant</span><span>Description</span></div>
      <div id="rack-list"></div>
    </div>
  </div>
</div>

<!-- ══════════ fb ══════════ -->
<div class="fb-panel" id="fb-panel-fb">
  <div class="fb-wrap">
    <div class="fb-img-outer">
      <img class="fb-img-base" id="fb-img-base" src="../../../../_shared/media/images/fbele0.PNG" alt="Électronique dans le FlexiBowl®" />
      <img class="fb-img-hl"   id="fb-img-hl"   src="" alt="" aria-hidden="true" />
      <div class="fb-badge" id="fb-badge"></div>
      <div class="fb-hint"  id="fb-hint">Sélectionner un composant dans la liste</div>
    </div>
    <div class="fb-list-panel">
      <div class="fb-list-head"><span>N°</span><span>Composant</span><span>Description</span></div>
      <div id="fb-list"></div>
    </div>
  </div>
</div>

<script>
(function(){

  /* ── dati componenti ── */
  var models = {
    rack: {
      imgPath: '../../../../_shared/media/images/inrack',
      imgDefault: '../../../../_shared/media/images/inrack0.PNG',
      imgExt: '.PNG',
      comps: [
        {n:1,  name:'Groupe API et alimentation 24V',     desc:'Ils sont fixés sur un rail DIN ; les modules de l’API sont amovibles individuellement'},
        {n:2,  name:'Alimentation 48V',                  desc:'Fixé sur rail DIN'},
        {n:3,  name:'Carte',                            desc:'Son support est fixé sur le plateau inférieur par deux entretoises ; il contient également les fusibles'},
        {n:4,  name:'Résistance de freinage',           desc:'Fixée sur le plateau inférieur par deux vis M4'},
      ]
    },
    fb: {
      imgPath: '../../../../_shared/media/images/fbele',
      imgDefault: '../../../../_shared/media/images/fbele0.PNG',
      imgExt: '.PNG',
      comps: [
        {n:1,  name:'Groupe API et alimentation 24V',     desc:'Ils sont fixés sur un rail DIN ; les modules de l’API sont amovibles individuellement'},
        {n:2,  name:'Alimentation 48V',                  desc:'Fixé sur rail DIN'},
        {n:3,  name:'Résistance de freinage',           desc:'Fixée sur le plateau inférieur par deux vis M4 sur le FlexiBowl® 500 et par quatre vis M4 sur les autres tailles'},
      ]
    },
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

Dans les FlexiBowl® de taille 500 ou supérieure, la carte est ancrée à un support fixé sur la colonne à côté du backlight, du côté flip.

::: {figure} ../../../../_shared/media/images/schedapos.png
:align: center
:width: 90%
:::

:::{note}
Dans les FlexiBowl® de taille 650 ou supérieure, toute l'électronique est accessible par le haut en retirant l'illuminateur du backlight et le couvercle central du plateau supérieur. Sur le FlexiBowl® 500, il peut être plus pratique de démonter les carters pour accéder latéralement au groupe automate/alimentation 24 V et à la résistance de freinage.
:::


(scheda-interfaccia)=
## Maintenance de la carte d'interface

Cette section décrit le fonctionnement et la procédure de remplacement des **relais d'interface** et des **fusibles de protection** présents sur la carte d'interface.

La figure suivante montre la carte avec l'indication de la position des relais et des fusibles.

::: {figure} ../../../../_shared/media/images/schedafronte.png
:align: center
:width: 80%

Vue de face de la carte d'interface
:::

À l'arrière de la carte sont indiqués l'ampérage de chaque fusible et la référence de chaque relais d'interface.

(scheda-interfaccia-retro)=
::: {figure} ../../../../_shared/media/images/schedaretro.png
:align: center
:width: 80%

Vue arrière : références des relais et calibres des fusibles
:::

### Avertissements de sécurité

:::{danger}
**Risque électrique.** Avant d'intervenir sur la carte d'interface, mettre la machine hors tension au moyen de l'interrupteur général et attendre la décharge des condensateurs. Vérifier l'absence de tension avec un instrument de mesure approprié avant de toucher tout composant.
:::

Pendant les opérations de maintenance, respecter scrupuleusement les indications suivantes :

- l'intervention doit être effectuée exclusivement par du personnel technique qualifié et formé ;
- utiliser des équipements de protection individuelle (EPI) appropriés, y compris des gants antistatiques ;
- éviter de laisser tomber des outils ou des corps étrangers sur la carte pendant l'intervention ;
- ne pas remplacer un fusible par un fusible d'ampérage différent de celui d'origine ;
- ne pas forcer sur les relais lors de l'extraction : si un composant est bloqué, vérifier son bon accrochage avant de poursuivre ;
- à la fin de l'intervention, refermer correctement la porte/fente d'accès avant de rétablir l'alimentation.

### Description de la carte

(scheda-relè)=
#### Relais d'interface

La carte est dotée de cinq relais d'interface, identifiés par les sigles K1–K5. Le relais K1 est un relais électromécanique à double inverseur ; tous les autres relais (K2–K5) sont des relais statiques.

:::{list-table}
:widths: 10 55 35
:header-rows: 1

* - Réf.
  - Fonction
  - Type
* - K1
  - Relais d'interface pour backlight
  - Électromécanique à double inverseur
* - K2
  - Relais d'interface pour électrovanne du flip
  - Statique
* - K3
  - Relais d'interface pour électrovanne de soufflage central
  - Statique
* - K4
  - Relais d'interface pour électrovanne de soufflage radial
  - Statique
* - K5
  - Relais d'interface pour électrovanne de vidage (optionnel)
  - Statique
:::

(scheda-fusibili)=
#### Fusibles de protection

La carte est dotée de neuf fusibles de protection de type *automotive mini*. Le kit de fusibles de rechange est fourni avec le FlexiBowl®.

:::{list-table}
:widths: 10 70 20
:header-rows: 1

* - Réf.
  - Fonction
  - Calibre
* - F1
  - Alimentation principale
  - 10 A
* - F2
  - Alimentation 24 V — électrovannes flip, soufflage central/radial, vidage
  - 7.5 A
* - F3
  - Alimentation du connecteur STO
  - 2 A
* - F4
  - Alimentation vers le client
  - 5 A
* - F5
  - Capteur de vidage
  - 2 A
* - F6
  - Alimentation du backlight
  - 7.5 A
* - F7
  - Alimentation du backlight
  - 7.5 A
* - F8
  - Alimentation du moteur et du driver
  - 5 A
* - F9
  - Alimentation de l'automate
  - 7.5 A
:::

### Équipement nécessaire

- Extracteur pour fusibles *automotive mini* (ou pince à becs plats)
- Kit de fusibles de rechange fourni avec le FlexiBowl®
- Relais de rechange conformes à la référence d'origine (K1–K5)

### Remplacement des relais d'interface

La procédure s'applique au remplacement d'un ou de plusieurs relais d'interface (K1–K5).

1. Mettre la machine hors tension et vérifier l'absence de tension avec le multimètre, comme indiqué dans les avertissements de sécurité.
2. Accéder à la carte d'interface par l'ouverture prévue à cet effet.
3. Repérer le relais à remplacer en se référant à la {ref}`vue arrière <scheda-interfaccia-retro>` et au {ref}`tableau des relais <scheda-relè>`.
4. Si le relais à remplacer est **K1** (électromécanique), l'extraire délicatement de son support en tirant vers le haut sans forcer sur les bornes.
5. Si le relais à remplacer est **K2, K3, K4 ou K5** (statique), l'extraire avec la même précaution, en évitant de plier les broches de contact.
6. Insérer le relais de rechange dans le support en vérifiant que la référence et l'orientation correspondent exactement à celles du composant retiré.
7. Vérifier que le relais est correctement inséré et stable dans le support.
8. Refermer l'ouverture d'accès à la carte.
9. Rétablir l'alimentation et vérifier le bon fonctionnement de la fonction associée au relais remplacé.

### Remplacement des fusibles de protection

La procédure s'applique au remplacement d'un ou de plusieurs fusibles de protection (F1–F9).

1. Mettre la machine hors tension et vérifier l'absence de tension avec le multimètre, comme indiqué dans les avertissements de sécurité.
2. Ouvrir la fente d'accès aux fusibles de protection prévue à cet effet.
3. Repérer le fusible à remplacer en se référant à la {ref}`vue arrière <scheda-interfaccia-retro>` et au {ref}`tableau des fusibles <scheda-fusibili>`.
4. Extraire le fusible à l'aide de l'extracteur dédié (ou d'une pince), en le saisissant sans toucher les parties métalliques.
5. Si possible, vérifier la cause du déclenchement du fusible avant de procéder au remplacement.
6. Prélever dans le kit de rechange un fusible *automotive mini* de même calibre (ampérage) que celui indiqué dans le tableau.
7. Insérer le nouveau fusible dans son logement en vérifiant qu'il est correctement positionné.
8. Refermer la fente d'accès.
9. Rétablir l'alimentation et vérifier le bon fonctionnement du circuit protégé par le fusible remplacé.

:::{caution}
Ne jamais utiliser un fusible de calibre différent de celui d'origine.
:::

### Contrôles périodiques et maintenance préventive

- Vérifier périodiquement l'absence de signes de surchauffe ou de noircissement sur les relais, les fusibles et les supports.
- Vérifier que les connecteurs présents sur la carte sont correctement enfichés.
- Toujours disposer d'un stock du kit de fusibles de rechange.
- Consigner chaque remplacement effectué (date, référence du composant, cause) dans un registre de maintenance.
