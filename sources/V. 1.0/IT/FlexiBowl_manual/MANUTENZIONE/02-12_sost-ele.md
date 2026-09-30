# [ELE] **Sostituzione componentistica elettronica**

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
* - {ref}`Qualifica operatore <operatori>`
  - {ref}`D.P.I. Necessari <dpi>`

* - **Manutentore elettrico**
  - :::{raw} html
       <div class="ars-img-row">
         <img src="../../../../_shared/media/images/guanti.png" alt="guanti">
         <img src="../../../../_shared/media/images/scarpe.png" alt="scarpe">
         <img src="../../../../_shared/media/images/tuta.png" alt="tuta">
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
      Disconnettere l’alimentazione elettrica prima di effettuare qualsiasi operazione all'interno del FlexiBowl®.
    </td>
  </tr>
</table>
::::

## Sostituzione delle parti elettroniche principali

Nelle taglie più piccole l'elettronica è tutta compresa nel rack, per cui è sufficiente smontare il pannello superiore per accedere a tutta la componentistica. Nei FlexiBowl® di taglia 500 o superiore invece tutte le parti sono contenute nella macchina.

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
  <button class="fb-tab on"    onclick="fbSwitchTab('rack',this)">Elettronica nel rack</button>
  <button class="fb-tab"    onclick="fbSwitchTab('fb',this)">Elettronica nel FlexiBowl®</button>
</div>

<!-- ══════════ rack ══════════ -->
<div class="fb-panel on" id="fb-panel-rack">
  <div class="fb-wrap">
    <div class="fb-img-outer">
      <img class="fb-img-base" id="rack-img-base" src="../../../../_shared/media/images/inrack0.PNG" alt="Elettronica nel rack" />
      <img class="fb-img-hl"   id="rack-img-hl"   src="" alt="" aria-hidden="true" />
      <div class="fb-badge" id="rack-badge"></div>
      <div class="fb-hint"  id="rack-hint">Seleziona un componente dalla lista</div>
    </div>
    <div class="fb-list-panel">
      <div class="fb-list-head"><span>N.</span><span>Componente</span><span>Descrizione</span></div>
      <div id="rack-list"></div>
    </div>
  </div>
</div>

<!-- ══════════ fb ══════════ -->
<div class="fb-panel" id="fb-panel-fb">
  <div class="fb-wrap">
    <div class="fb-img-outer">
      <img class="fb-img-base" id="fb-img-base" src="../../../../_shared/media/images/fbele0.PNG" alt="Elettronica nel FlexiBowl®" />
      <img class="fb-img-hl"   id="fb-img-hl"   src="" alt="" aria-hidden="true" />
      <div class="fb-badge" id="fb-badge"></div>
      <div class="fb-hint"  id="fb-hint">Seleziona un componente dalla lista</div>
    </div>
    <div class="fb-list-panel">
      <div class="fb-list-head"><span>N.</span><span>Componente</span><span>Descrizione</span></div>
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
        {n:1,  name:'Gruppo PLC e alimentatore 24V',     desc:'Sono fissati su una barra DIN; i moduli del PLC sono rimuovobili singolarmente'},
        {n:2,  name:'Alimentatore 48V',                  desc:'Fissato su barra DIN'},
        {n:3,  name:'Scheda',                            desc:'Il suo supporto è fissato sul pianale inferiore attraverso due distanziali; contiene anche i fusibili'},
        {n:4,  name:'Resistenza di frenatura',           desc:'Fissata sul pianale inferiore tramite due viti M4'},
      ]
    },
    fb: {
      imgPath: '../../../../_shared/media/images/fbele',
      imgDefault: '../../../../_shared/media/images/fbele0.PNG',
      imgExt: '.PNG',
      comps: [
        {n:1,  name:'Gruppo PLC e alimentatore 24V',     desc:'Sono fissati su una barra DIN; i moduli del PLC sono rimuovobili singolarmente'},
        {n:2,  name:'Alimentatore 48V',                  desc:'Fissato su barra DIN'},
        {n:3,  name:'Resistenza di frenatura',           desc:'Fissata sul pianale inferiore tramite due viti M4 sul FlexiBowl® 500 e tramite quattro viti M4 sulle altre taglie'},
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

La scheda nei FlexiBowl® di taglia 500 o superiore è ancorata a un supporto fissato sulla colonna accanto al backlihgt dal lato flip.

::: {figure} ../../../../_shared/media/images/schedapos.png
:align: center
:width: 90%
:::

:::{note}
Nei FlexiBowl® di taglia 650 o superiore tutta l'elettronica è accessibile dall'alto rimuovendo l'illuminatore del backlight e il coperchio centrale del pianale superiore. Nel FlexiBowl® 500 può essere più conveniente smontare i carter per accedere lateralmente al gruppo PLC/alimentatore 24V e alla resistenza di frenatura.
:::


(scheda-interfaccia)=
## Manutenzione della scheda di interfaccia

Questa sezione descrive il funzionamento e la procedura di sostituzione dei **relè di interfaccia** e dei **fusibili di protezione** presenti a bordo della scheda di interfaccia.

La figura seguente mostra la scheda con l'indicazione della posizione dei relè e dei fusibili.

::: {figure} ../../../../_shared/media/images/schedafronte.png
:align: center
:width: 80%

Vista frontale della scheda di interfaccia
:::

Sulla parte posteriore della scheda sono riportati l'amperaggio di ciascun fusibile e il riferimento di ciascun relè di interfaccia.

(scheda-interfaccia-retro)=
::: {figure} ../../../../_shared/media/images/schedaretro.png
:align: center
:width: 80%

Vista posteriore: riferimenti dei relè e taglio dei fusibili
:::

### Avvertenze di sicurezza

:::{danger}
**Rischio elettrico.** Prima di intervenire sulla scheda di interfaccia, togliere tensione alla macchina agendo sull'interruttore generale e attendere lo scaricamento dei condensatori. Verificare l'assenza di tensione con un idoneo strumento di misura prima di toccare qualsiasi componente.
:::

Durante le operazioni di manutenzione attenersi scrupolosamente alle seguenti indicazioni:

- l'intervento deve essere eseguito esclusivamente da personale tecnico qualificato e formato;
- utilizzare dispositivi di protezione individuale (D.P.I.) idonei, inclusi guanti antistatici;
- evitare di lasciare cadere utensili o corpi estranei sulla scheda durante l'intervento;
- non sostituire un fusibile con uno di amperaggio diverso da quello originale;
- non forzare i relè durante l'estrazione: se un componente risulta bloccato, verificarne il corretto aggancio prima di proseguire;
- al termine dell'intervento, richiudere correttamente lo sportello/fessura di accesso prima di ripristinare l'alimentazione.

### Descrizione della scheda

(scheda-relè)=
#### Relè di interfaccia

La scheda è dotata di cinque relè di interfaccia, identificati dalle sigle K1–K5. Il relè K1 è un relè elettromeccanico a doppio scambio; tutti gli altri relè (K2–K5) sono relè a stato solido.

:::{list-table}
:widths: 10 55 35
:header-rows: 1

* - Rif.
  - Funzione
  - Tipologia
* - K1
  - Relè di interfaccia per back light
  - Elettromeccanico a doppio scambio
* - K2
  - Relè di interfaccia per elettrovalvola del flip
  - Stato solido
* - K3
  - Relè di interfaccia per elettrovalvola soffio centrale
  - Stato solido
* - K4
  - Relè di interfaccia per elettrovalvola soffio radiale
  - Stato solido
* - K5
  - Relè di interfaccia per elettrovalvola svuotamento (opzionale)
  - Stato solido
:::

(scheda-fusibili)=
#### Fusibili di protezione

La scheda è dotata di nove fusibili di protezione di tipo *automotive mini*. Il kit di ricambio dei fusibili è fornito a corredo del FlexiBowl®.

:::{list-table}
:widths: 10 70 20
:header-rows: 1

* - Rif.
  - Funzione
  - Taglio
* - F1
  - Alimentazione principale
  - 10 A
* - F2
  - Alimentazione 24 V — elettrovalvola flip, soffio centrale/radiale, svuotamento
  - 7.5 A
* - F3
  - Alimentazione connettore STO
  - 2 A
* - F4
  - Alimentazione verso cliente
  - 5 A
* - F5
  - Sensore di svuotamento
  - 2 A
* - F6
  - Alimentazione back light
  - 7.5 A
* - F7
  - Alimentazione back light
  - 7.5 A
* - F8
  - Alimentazione motore e driver
  - 5 A
* - F9
  - Alimentazione PLC
  - 7.5 A
:::

### Attrezzatura necessaria

- Estrattore per fusibili *automotive mini* (o pinzetta a becchi piatti)
- Kit di ricambio fusibili in dotazione al FlexiBowl®
- Relè di ricambio conformi al riferimento originale (K1–K5)

### Sostituzione dei relè di interfaccia

La procedura si applica alla sostituzione di uno o più relè di interfaccia (K1–K5).

1. Togliere tensione alla macchina e verificarne l'assenza con il multimetro, come indicato nelle avvertenze di sicurezza.
2. Accedere alla scheda di interfaccia attraverso l'apposita apertura.
3. Individuare la posizione del relè da sostituire facendo riferimento alla {ref}`vista posteriore <scheda-interfaccia-retro>` e alla {ref}`tabella dei relè <scheda-relè>`.
4. Se il relè da sostituire è **K1** (elettromeccanico), estrarlo delicatamente dal proprio zoccolo tirandolo verso l'alto senza forzare i terminali.
5. Se il relè da sostituire è **K2, K3, K4 o K5** (stato solido), estrarlo con la stessa attenzione, evitando di piegare i pin di contatto.
6. Inserire il relè di ricambio nello zoccolo, verificando che il riferimento e l'orientamento corrispondano esattamente a quelli del componente rimosso.
7. Verificare che il relè sia correttamente inserito e stabile nello zoccolo.
8. Richiudere l'apertura di accesso alla scheda.
9. Ripristinare l'alimentazione e verificare il corretto funzionamento della funzione associata al relè sostituito.

### Sostituzione dei fusibili di protezione

La procedura si applica alla sostituzione di uno o più fusibili di protezione (F1–F9).

1. Togliere tensione alla macchina e verificarne l'assenza con il multimetro, come indicato nelle avvertenze di sicurezza.
2. Aprire l'apposita fessura di accesso ai fusibili di protezione.
3. Individuare il fusibile da sostituire facendo riferimento alla {ref}`vista posteriore <scheda-interfaccia-retro>` e alla {ref}`tabella dei fusibili <scheda-fusibili>`.
4. Estrarre il fusibile utilizzando l'estrattore dedicato (o una pinzetta), afferrandolo senza toccare le parti metalliche.
5. Verificare, se possibile, la causa dell'intervento del fusibile prima di procedere alla sostituzione.
6. Prelevare dal kit di ricambio un fusibile *automotive mini* dello stesso taglio (amperaggio) indicato in tabella.
7. Inserire il nuovo fusibile nella propria sede, verificando che risulti correttamente alloggiato.
8. Richiudere la fessura di accesso.
9. Ripristinare l'alimentazione e verificare il corretto funzionamento del circuito protetto dal fusibile sostituito.

:::{caution}
Non utilizzare mai un fusibile di taglio diverso da quello originale.
:::

### Controlli periodici e manutenzione preventiva

- Verificare periodicamente l'assenza di segni di surriscaldamento o annerimento su relè, fusibili e zoccoli.
- Controllare che i connettori presenti sulla scheda siano correttamente innestati.
- Tenere sempre disponibile una scorta del kit di ricambio fusibili.
- Annotare ogni sostituzione effettuata (data, riferimento componente, causa) in un registro di manutenzione.
