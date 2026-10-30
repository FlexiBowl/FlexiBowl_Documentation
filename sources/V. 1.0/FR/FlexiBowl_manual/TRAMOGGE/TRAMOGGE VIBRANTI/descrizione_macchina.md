# **Description de la machine**

<p style="line-height: 1.6; border-left: 4px solid #34495e; padding-left: 15px; margin-bottom: 25px;">
  Les Bulk Feeder sont particulièrement adaptés pour alimenter et pré-doser des pièces de petites, moyennes et grandes dimensions. Ils sont actionnés par une base linéaire vibrante dont le modèle varie selon la taille du Bulk Feeder lui-même.
</p>

La machine standard se compose des parties fondamentales suivantes :

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
  <button class="tr-tab on"    onclick="trSwitchTab('Bulk Feeder',this)">Bulk Feeder vibrant</button>
</div>

<!-- ══════════ TRAMOGGIA ══════════ -->
<div class="tr-panel on" id="tr-panel-tramoggia">
  <div class="tr-wrap">
    <div class="tr-img-outer">
      <img class="tr-img-base" id="tramoggia-img-base" src="../../../../../_shared/media/images/tramoggia0.PNG" alt="Vue du Bulk Feeder" />
      <img class="tr-img-hl"   id="tramoggia-img-hl"   src="" alt="" aria-hidden="true" />
      <div class="tr-badge" id="tramoggia-badge"></div>
      <div class="tr-hint"  id="tramoggia-hint">Sélectionner un composant dans la liste</div>
    </div>
    <div class="tr-list-panel">
      <div class="tr-list-head"><span>N°</span><span>Composant</span><span>Description</span></div>
      <div id="tramoggia-list"></div>
    </div>
  </div>
</div>

<script>
(function(){

  /* ── dati componenti ── */
  var models = {
    tramoggia: {
      imgPath: '../../../../../_shared/media/images/tramoggia',
      imgExt: '.PNG',
      comps: [
        {n:1,  name:'Support',        desc:'C’est le composant qui est fixé sur la machine et sur lequel est positionné le Bulk Feeder.'},
        {n:2,  name:'Base vibrante',    desc:'C’est le composant principal du Bulk Feeder ; au moyen d’un électroaimant, il produit la vibration qui permet l’avancement des pièces sur la cuve.'},
        {n:3,  name:'Cuve',            desc:'Elle peut être de 1,5 l, 5 l, 10 l, 20 l ou 40 l selon le composant à traiter. Des dimensions sur mesure sont également réalisables sur demande. La cuve de 1,5 l est en matière plastique, tandis que les autres sont en acier INOX.'},
        {n:4,  name:'Controller',       desc:'Il sert à régler la vibration du Bulk Feeder.'},
        {n:5,  name:'Carter',           desc:'Composants de protection de la base vibrante contre les chocs, la saleté et la poussière.'},
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
      row.className = 'tr-row';
      row.innerHTML = '<div class="tr-bubble">'+c.n+'</div>'
                    + '<div class="tr-name">'+c.name+'</div>'
                    + '<div class="tr-desc">'+c.desc+'</div>';
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
Dans le cas de modèles personnalisés, les composants peuvent différer, en partie ou en totalité, de ceux indiqués. Pour ces modèles, il faut se référer au dossier technique du projet.
:::

## Composants et fonctionnement

* **Structure de la base :** La base linéaire vibrante se compose de deux corps reliés entre eux par des ressorts à lames.
* **Mécanisme de vibration :** Le fonctionnement repose sur un électroaimant solidaire du corps fixe, qui attire et relâche le corps mobile. Cette action génère la vibration qui fait avancer les pièces contenues dans la cuve (positionnée sur le corps mobile et bloquée à l'aide de mâchoires).
* **Commande électrique :** Pour ce faire, les vibrateurs ont besoin d'un contrôleur qui convertit le courant alternatif en courant d'impulsion, et qui règle également la vitesse du système lui-même.

---

## Utilisation prévue 

Le Bulk Feeder est disponible en six modèles de base. Des modèles personnalisés, dérivés de ceux de base mais différents en termes de dimensions et de performances, peuvent être réalisés après concertation avec les demandes de l'utilisateur.

:::{note} 
**Note de validité :** Les informations contenues dans le présent manuel sont à considérer comme valables également pour les modèles personnalisés.
:::

**Capacité des modèles standard disponibles :**

| Modèle de base | Capacité de la cuve | Capacité de charge |
|:--- |:--- | :--- | 
| **Modèle 1** | 1,5 litre | 1 kg | 
| **Modèle 2** | 3 litres | 1,5 kg | 
| **Modèle 3** | 5 litres | 6 kg |
| **Modèle 4** | 10 litres | 6 kg |
| **Modèle 5** | 20 litres | 6 kg |
| **Modèle 6** | 40 litres | 15 kg |


La machine en question est destinée à un usage industriel pour :

::::{list-table}
:widths: 25 25 25 25
:header-rows: 1
:class: custom-safety-table

* - <span style="font-weight: bold; color: #2c3e50;">Opération</span>
  - <span style="font-weight: bold; color: #27ae60;">Autorisé</span>
  - <span style="font-weight: bold; color: #c0392b;">Non autorisée</span>
  - <span style="font-weight: bold; color: #2c3e50;">Environnement de travail</span>

* - <div style="padding: 8px 0;"><span style="font-weight: 600; text-transform: uppercase; font-size: 0.9em; ">Manutention destinée à l'alimentation de :</span></div>
  - <div style="background-color: #e8f8f5; border-left: 4px solid #2ecc71; padding: 10px; margin: 5px 0; border-radius: 4px; font-size: 0.95em; color: #117a65;">
      Composants dont le poids et les dimensions maximaux varient selon le modèle de machine.
    </div>
  - <div style="background-color: #fdf2f2; border-left: 4px solid #e74c3c; padding: 10px; margin: 5px 0; border-radius: 4px; font-size: 0.95em; color: #78281f;">
      Tout autre composant ne rentrant pas dans la plage de poids et de dimensions maximaux autorisés.
    </div>
  - <div style="background-color: #f4f6f7; padding: 10px; margin: 5px 0; border-radius: 4px; font-size: 0.95em; text-align: center; font-weight: 500; color: #566573;">
      Industriel
    </div>
::::

:::{IMPORTANT}
Pour plus d'informations sur le type de composants autorisés, consulter le paragraphe « Caractéristiques techniques » du présent manuel.
:::

<div style="display: flex; flex-direction: column; gap: 20px; margin: 20px 0;">

  <!-- Card 1: Destinazione d'Uso -->
  <div style="border-left: 5px solid #2980b9; background-color: #ebf5fb; padding: 20px; border-radius: 4px 8px 8px 4px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
    <h3 style="color: #2980b9; margin-top: 0; font-size: 1.2em; border-bottom: none;"> Destination d'usage</h3>
    <p style="margin-bottom: 10px; color: #2c3e50;">La machine a été conçue pour :</p>
    <ul style="color: #34495e; margin-bottom: 0; padding-left: 20px;">
      <li style="margin-bottom: 5px;">répondre aux <strong>exigences spécifiques</strong> mentionnées dans le contrat de vente ;</li>
      <li>être utilisée conformément aux <strong>instructions et aux limites d'emploi</strong> indiqués dans le présent manuel.</li>
    </ul>
  </div>

  <!-- Card 2: Condizioni per la Sicurezza -->
  <div style="border-left: 5px solid #27ae60; background-color: #eafaf1; padding: 20px; border-radius: 4px 8px 8px 4px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
    <h3 style="color: #27ae60; margin-top: 0; font-size: 1.2em; border-bottom: none;"> Conditions de sécurité</h3>
    <p style="margin-bottom: 10px; color: #2c3e50;">La machine est conçue et construite pour fonctionner en toute sécurité <strong>uniquement si</strong>:</p>
    <ul style="color: #34495e; margin-bottom: 0; padding-left: 20px;">
      <li style="margin-bottom: 5px;">elle est utilisée dans les limites déclarées dans le contrat et dans le présent manuel ;</li>
      <li style="margin-bottom: 5px;">les procédures du manuel d'utilisation sont scrupuleusement respectées ;</li>
      <li style="margin-bottom: 5px;">la maintenance courante est effectuée dans les délais et selon les modalités indiquées ;</li>
      <li style="margin-bottom: 5px;">la maintenance extraordinaire est effectuée rapidement en cas de besoin ;</li>
      <li><strong style="color: #c0392b;">les dispositifs de sécurité ne sont JAMAIS retirés et/ou contournés.</strong></li>
    </ul>
  </div>

</div>

## Mauvais usage (raisonnablement prévisible)

<div style="border-left: 5px solid #c0392b; background-color: #fdf2f2; padding: 20px; border-radius: 4px; margin: 15px 0; box-shadow: 0 2px 5px rgba(0,0,0,0.03);">
  <ul style="color: #2c3e50; margin: 0; padding-left: 20px; line-height: 1.6;">
    <li style="margin-bottom: 8px;">Traitement de composants liquides et de grenaille fine ;</li>
    <li style="margin-bottom: 8px;">Modification des paramètres de travail compromettant la sécurité ;</li>
    <li style="margin-bottom: 8px;">Transport de personnes ;</li>
    <li style="margin-bottom: 8px;">Utilisation de la machine comme point d'appui ;</li>
    <li style="margin-bottom: 8px;">Utilisation de la machine pour obtenir des valeurs de production supérieures aux limites prescrites ;</li>
    <li style="margin-bottom: 8px;">Modification / manipulation des connexions électriques et pneumatiques de la machine ou de tout autre de ses composants ;</li>
    <li style="margin-bottom: 8px;">Utilisation de la machine avec un produit autre que celui indiqué dans « Utilisation prévue (correcte) » ;</li>
    <li style="margin-bottom: 0;">Utilisation de la machine d'une manière différente de celle prévue au paragraphe « Utilisation prévue (correcte) ».</li>
  </ul>
</div>

:::{warning}
Toute utilisation de la machine autre que celle prévue doit être préalablement autorisée par écrit par le Constructeur. En l'absence de cette autorisation écrite, l'utilisation est à considérer comme « usage inapproprié » ; le Constructeur décline par conséquent toute responsabilité pour les dommages éventuellement causés aux biens ou aux personnes et considère comme déchue toute garantie sur la machine.
:::

:::{important}
Un usage inapproprié de la machine exclut toute responsabilité du Constructeur.
:::

## Obligations et interdictions 

### Obligations des utilisateurs 

L'utilisateur (entrepreneur ou employeur) doit :

<div style="border-left: 5px solid #2980b9; background-color: #ebf5fb; padding: 20px; border-radius: 4px; margin: 15px 0; box-shadow: 0 2px 5px rgba(0,0,0,0.03);">
  <ul style="color: #2c3e50; margin: 0; padding-left: 20px; line-height: 1.6;">
    <li style="margin-bottom: 8px;">Tenir compte des capacités et des conditions des opérateurs au regard de leur santé et de leur sécurité ;</li>
    <li style="margin-bottom: 8px;">Fournir les équipements de protection individuelle (EPI) adaptés aux différentes procédures ;</li>
    <li style="margin-bottom: 8px;">Fournir des moyens et des procédures de levage conformes aux normes ;</li>
    <li style="margin-bottom: 8px;">Exiger de chaque travailleur le respect des règles et des dispositions de l'entreprise en matière de sécurité et d'utilisation des moyens de protection collective et individuelle mis à sa disposition ;</li>
    <li style="margin-bottom: 8px;">Instruire le personnel sur les procédures à suivre en cas d'accident ;</li>
    <li style="margin-bottom: 8px;">Instruire le personnel sur les risques résiduels présents ;</li>
    <li style="margin-bottom: 8px;">Instruire le personnel sur les dispositifs prévus pour la sécurité des opérateurs ;</li>
    <li style="margin-bottom: 8px;">Instruire le personnel sur les risques d'émission de bruit dans l'environnement de travail ;</li>
    <li style="margin-bottom: 0;">Instruire le personnel sur les règles générales de prévention des accidents prévues par les directives européennes et par la législation du pays de destination de la machine.</li>
  </ul>
</div>

:::{note} 
Ne faire travailler sur la machine que du personnel ayant pris connaissance du présent manuel et ayant reçu une formation appropriée.
:::

### Obligations du personnel affecté (opérateurs/mainteneurs/techniciens)

Le personnel doit :

<div style="border-left: 5px solid #27ae60; background-color: #eafaf1; padding: 20px; border-radius: 4px; margin: 15px 0; box-shadow: 0 2px 5px rgba(0,0,0,0.03);">
  <ul style="color: #2c3e50; margin: 0; padding-left: 20px; line-height: 1.6;">
    <li style="margin-bottom: 8px;"><strong>Effectuer les interventions de maintenance toujours machine arrêtée.</strong> Ne jamais lubrifier des organes en mouvement ;</li>
    <li style="margin-bottom: 8px;">Lorsque la machine est en fonctionnement, éviter d'opérer à proximité avec des chaînes, des bracelets, des cravates ou d'autres vêtements susceptibles de s'accrocher dans les mécanismes ;</li>
    <li style="margin-bottom: 8px;">Attacher obligatoirement les cheveux longs afin d'éviter le risque d'entraînement ;</li>
    <li style="margin-bottom: 8px;">Effectuer des interventions sur le tableau électrique, les boîtes de dérivation, les câbles et les composants électriques <strong>exclusivement avec l'interrupteur général éteint</strong>;</li>
    <li style="margin-bottom: 8px;">S'assurer qu'aucune personne ne se trouve à l'intérieur des zones dangereuses avant de démarrer la machine ;</li>
    <li style="margin-bottom: 8px;">Faire preuve de la plus grande attention pendant le fonctionnement afin que personne ne puisse accéder directement aux parties en mouvement ;</li>
    <li style="margin-bottom: 8px;">Utiliser de manière appropriée les dispositifs de protection mis à disposition par l'employeur ;</li>
    <li style="margin-bottom: 0;">Signaler immédiatement à l'employeur, au dirigeant ou au préposé toute défaillance ou anomalie des dispositifs de sécurité.</li>
  </ul>
</div>

### Interdictions pour le personnel préposé 

En particulier, le personnel ne doit pas :

<div style="border-left: 5px solid #c0392b; background-color: #fdf2f2; padding: 20px; border-radius: 4px; margin: 15px 0; box-shadow: 0 2px 5px rgba(0,0,0,0.03);">
  <ul style="color: #2c3e50; margin: 0; padding-left: 20px; line-height: 1.6;">
    <li style="margin-bottom: 8px;">Utiliser la machine de manière inappropriée (c'est-à-dire pour des usages autres que ceux indiqués au paragraphe « Utilisation prévue ») ;</li>
    <li style="margin-bottom: 8px;">Retirer ou modifier sans autorisation préalable les dispositifs de sécurité ou de signalisation ;</li>
    <li style="margin-bottom: 8px;">Effectuer de leur propre initiative des opérations ou des manœuvres hors de leur compétence ou pouvant compromettre leur sécurité ou celle d'autres travailleurs ;</li>
    <li style="margin-bottom: 8px;">Porter des bracelets, des bagues ou des chaînettes pouvant pendre et être entraînés par des organes en mouvement ;</li>
    <li style="margin-bottom: 8px;">Remplacer ou modifier les vitesses des composants de la machine sans le consentement explicite d'un responsable ;</li>
    <li style="margin-bottom: 8px;">Modifier de quelque manière que ce soit le cycle programmé de la machine ;</li>
    <li style="margin-bottom: 8px;">Modifier les raccordements électriques dans le but d'exclure ou de contourner les sécurités internes ;</li>
    <li style="margin-bottom: 8px;">Utiliser la machine si elle n'a pas été installée en totale conformité avec la réglementation en vigueur ;</li>
    <li style="margin-bottom: 8px;">Utiliser la machine comme point d'appui, même si elle ne fonctionne pas (au risque de chute de l'opérateur et/ou de détérioration de la structure) ;</li>
    <li style="margin-bottom: 0;">Utiliser la machine en dehors des conditions ambiantes autorisées (consulter le « Chapitre 5 »).</li>
  </ul>
</div>

:::{attention}
ARS S.r.l. ne répond pas des dommages causés aux biens ou aux personnes dans le cas où :
•	il est constaté que la machine a été utilisée dans l'un des environnements non autorisés ;
•	les obligations et interdictions décrites ici n'ont pas été respectées.
:::

## Données techniques 

```{list-table}
:header-rows: 1
:widths: 20 30 25 25

* - Taille du Bulk Feeder
  - Alimentation électrique
  - Fréquence / Phase
  - Intensité absorbée (A)
* - 1,5 l
  - 230 Vac ±5 % ({ref}`115 Vac sur demande <tramoggia-110v>`)
  - 50-60 Hz / monophasé
  - 0,1
* - 3 l
  - 230 Vac ±5 % ({ref}`115 Vac sur demande <tramoggia-110v>`)
  - 50-60 Hz / monophasé
  - 0,1
* - 5 l
  - 230 Vac ±5 % ({ref}`115 Vac sur demande <tramoggia-110v>`)
  - 50-60 Hz / monophasé
  - 0,25
* - 10 l
  - 230 Vac ±5 % ({ref}`115 Vac sur demande <tramoggia-110v>`)
  - 50-60 Hz / monophasé
  - 0,25
* - 20 l
  - 230 Vac ±5 % ({ref}`115 Vac sur demande <tramoggia-110v>`)
  - 50-60 Hz / monophasé
  - 0,25
* - 40 l
  - 230 Vac ±5 % ({ref}`115 Vac sur demande <tramoggia-110v>`)
  - 50-60 Hz / monophasé
  - 0,45
```

| Taille du Bulk Feeder | 1,5 l | 3 l | 5 l | 10 l | 20 l | 40 l |
|------------------------------|--------|------|------|-------|-------|-------|
| Poids net correspondant | 2 kg | 11 kg | 24 kg | 26 kg | 28 kg | 38 kg |

:::{attention}
Dans le cas de modèles personnalisés, les valeurs indiquées peuvent différer de celles du tableau. Pour ces modèles, il faut se référer au dossier technique du projet.
:::

## Implantation 

![Dimensions du Bulk Feeder](../../../../../_shared/media/images/dim_tramoggia.jpg)

| Dimensions | 1,5 l | 3 l | 5 l | 10 l | 20 l | 40 l |
|------------|--------|------|------|-------|-------|-------|
| A | 350 mm | 450 mm | 480 mm | 670 mm | 780 mm | 780 mm |
| B | 65 mm | 100 mm | 130 mm | 155 mm | 183 mm | 208 mm |
| C | 90 mm | 120 mm | 150 mm | 160 mm | 215 mm | 315 mm |
| D | 211 mm | 215 mm | 247 mm | 247 mm | 247 mm | 290 mm |
| E | 350 mm | 515 mm | 515 mm | 690 mm | 780 mm | 780 mm |

:::{attention}
Dans le cas de modèles personnalisés, les valeurs indiquées peuvent différer de celles du tableau. Pour ces modèles, il faut se référer au dossier technique du projet.
:::


## Composants standard et optionnels 

```{list-table} Accessoires et équipements des Bulk Feeder
:widths: 20 40 25 15
:header-rows: 1

* - **Élément**
  - **Description**
  - **Photo**
  - **Standard / Optionnel**

* - Barrière doseuse
  - Doseur à barrière pour la régulation du flux (réglable). Voir {ref}`barriera`.
  - 
    :::{image} ../../../../../_shared/media/images/barriera_dosatrice.jpg
    :alt: Barrière doseuse
    :width: 120px
    :align: center
    :::
  - OPTIONNEL (hors Bulk Feeder 1,5 l)

* - Protection de sécurité
  - Protection de sécurité pour les mains. Voir {ref}`hand-guard`.
  - 
    :::{image} ../../../../../_shared/media/images/protezione_sicurezza.jpg
    :alt: Protection de sécurité
    :width: 120px
    :align: center
    :::
  - OPTIONNEL (hors Bulk Feeder 1,5 l)

* - Revêtement
  - Revêtement de la cuve en polyuréthane. Voir {ref}`tramoggia-pu`.
  - 
    :::{image} ../../../../../_shared/media/images/rivestimento.png
        :alt: Revêtement
        :width: 120px
        :align: center
    :::
  - OPTIONNEL (hors Bulk Feeder 1,5 l)

* - Cellule photoélectrique frontale
  - Elle a pour fonction de vérifier la présence de composants dans la zone frontale de la cuve vibrante pendant le processus d'alimentation. Voir {ref}`fotocellula-frontale`.
  - 
    :::{image} ../../../../../_shared/media/images/fotocellula_frontale.png
        :alt: Cellule photoélectrique frontale
        :width: 120px
        :align: center
    :::
  - OPTIONNEL (hors Bulk Feeder 1,5 l)

* - Cellule photoélectrique arrière
  - Elle a pour fonction de surveiller le niveau des pièces présentes dans la cuve. Voir {ref}`fotocellula-posteriore`.
  - 
    :::{image} ../../../../../_shared/media/images/fotocellula_posteriore.png
        :alt: Cellule photoélectrique arrière
        :width: 120px
        :align: center
    :::
  - OPTIONNEL (hors Bulk Feeder 1,5 l)

```

:::{note}
La liste complète des variantes, accessoires et options disponibles au tarif (y compris les versions 110 V, les kits antivibratoires et les câbles du contrôleur) figure dans la page {ref}`Accessoires et options <tramoggia-accessori>`.
:::

### Cycle de travail 

Le cycle de travail est décrit ci-dessous de manière simplifiée, divisé en phases opérationnelles suivantes :

<div style="display: flex; flex-direction: column; gap: 15px; margin: 20px 0; position: relative;">

  <!-- Fase 1 -->
  <div style="display: flex; background-color: #f8f9fa; border-radius: 8px; border: 1px solid #e9ecef; overflow: hidden; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
    <div style="background-color: #2c3e50; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 60px; font-size: 1.4em; font-weight: bold; flex-shrink: 0;">
      1
    </div>
    <div style="padding: 15px 20px; display: flex; align-items: center; color: #2c3e50; line-height: 1.5;">
      <span>L'opérateur place le produit à traiter à l'intérieur de la cuve, manuellement ou avec un système de chargement automatique.</span>
    </div>
  </div>

  <!-- Fase 2 -->
  <div style="display: flex; background-color: #f8f9fa; border-radius: 8px; border: 1px solid #e9ecef; overflow: hidden; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
    <div style="background-color: #34495e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 60px; font-size: 1.4em; font-weight: bold; flex-shrink: 0;">
      2
    </div>
    <div style="padding: 15px 20px; display: flex; align-items: center; color: #2c3e50; line-height: 1.5;">
      <span>Le Bulk Feeder effectue cycliquement des vibrations (réglées par l'opérateur) pour permettre l'avancement des pièces, de manière à garantir en permanence leur présence sur l'alimentateur.</span>
    </div>
  </div>

</div>