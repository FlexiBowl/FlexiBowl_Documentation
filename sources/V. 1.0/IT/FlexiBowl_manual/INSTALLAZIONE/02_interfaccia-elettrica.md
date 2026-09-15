(intele)=
# [ELE] **Interfaccia Elettrica**

Il pannello connettori del FlexiBowl® varia in base alla versione della macchina:

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
  <button class="ie-tab on" onclick="ieSwitchTab('smallpanel',this)">Pannello FlexiBowl® 200-350</button>
  <button class="ie-tab"    onclick="ieSwitchTab('rack',this)">Rack</button>
  <button class="ie-tab"    onclick="ieSwitchTab('stpanel',this)">Pannello Standard</button>
  <button class="ie-tab"    onclick="ieSwitchTab('encpanel',this)">Pannello Flexitracking</button>
</div>
<!-- ══════════ PANNELLO FB200-350 ══════════ -->
<div class="ie-panel on" id="ie-panel-smallpanel">
  <div class="ie-wrap">
    <div class="ie-img-outer">
      <img class="ie-img-base" id="smallpanel-img-base" src="../../../../_shared/media/images/smallpanel0.PNG" alt="Pannello FlexiBowl® 200-350" />
      <img class="ie-img-hl"   id="smallpanel-img-hl"   src="" alt="" aria-hidden="true" />
      <div class="ie-badge" id="smallpanel-badge"></div>
      <div class="ie-hint"  id="smallpanel-hint">Seleziona un connettore dalla lista</div>
    </div>
    <div class="ie-list-panel">
      <div class="ie-list-head"><span>N.</span><span>Connettore</span><span>Descrizione</span></div>
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
      <div class="ie-hint"  id="rack-hint">Seleziona un connettore dalla lista</div>
    </div>
    <div class="ie-list-panel">
      <div class="ie-list-head"><span>N.</span><span>Connettore</span><span>Descrizione</span></div>
      <div id="rack-list"></div>
    </div>
  </div>
</div>
<!-- ══════════ PANNELLO STANDARD ══════════ -->
<div class="ie-panel" id="ie-panel-stpanel">
  <div class="ie-wrap">
    <div class="ie-img-outer">
      <img class="ie-img-base" id="stpanel-img-base" src="../../../../_shared/media/images/stpanel0.PNG" alt="Pannello Standard FlexiBowl®" />
      <img class="ie-img-hl"   id="stpanel-img-hl"   src="" alt="" aria-hidden="true" />
      <div class="ie-badge" id="stpanel-badge"></div>
      <div class="ie-hint"  id="stpanel-hint">Seleziona un connettore dalla lista</div>
    </div>
    <div class="ie-list-panel">
      <div class="ie-list-head"><span>N.</span><span>Connettore</span><span>Descrizione</span></div>
      <div id="stpanel-list"></div>
    </div>
  </div>
</div>
<!-- ══════════ PANNELLO FLEXITRACKING ══════════ -->
<div class="ie-panel" id="ie-panel-encpanel">
  <div class="ie-wrap">
    <div class="ie-img-outer">
      <img class="ie-img-base" id="encpanel-img-base" src="../../../../_shared/media/images/encpanel0.PNG" alt="Pannello Flexitracking FlexiBowl®" />
      <img class="ie-img-hl"   id="encpanel-img-hl"   src="" alt="" aria-hidden="true" />
      <div class="ie-badge" id="encpanel-badge"></div>
      <div class="ie-hint"  id="encpanel-hint">Seleziona un connettore dalla lista</div>
    </div>
    <div class="ie-list-panel">
      <div class="ie-list-head"><span>N.</span><span>Connettore</span><span>Descrizione</span></div>
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
        {n:1, name:'C-A SIGNAL', desc:'Connettore C-A signal'},
        {n:2, name:'C-B SIGNAL', desc:'Connettore C-B Signal'},
        {n:3, name:'MOTOR',      desc:'Connettore cavo motore'},
        {n:4, name:'C-ETH FB',   desc:'Collegamento ethernet al rack'},
        {n:5, name:'AIR SUPPLY', desc:'Ingresso aria'}
      ]
    },
    rack: {
      imgPath: '../../../../_shared/media/images/rack',
      imgExt: '.PNG',
      comps: [
        {n:1, name:'POWER SUPPLY', desc:'Presa di corrente e interruttore; comprende anche un filtro IEC'},
        {n:2, name:'STO',          desc:'Connettore STO'},
        {n:3, name:'MOTOR',        desc:'Connettore cavo motore'},
        {n:4, name:'C-A SIGNAL',   desc:'Connettore C-A signal'},
        {n:5, name:'C-B SIGNAL',   desc:'Connettore C-B Signal'},
        {n:6, name:'C-ETH IN',     desc:'Connettore Ethernet'},
        {n:7, name:'HOPPER',       desc:'Connettore tramoggia'},
        {n:8, name:'C-ETH FB',     desc:'Collegamento Ethernet al FlexiBowl\u00ae'}
      ]
    },
    stpanel: {
      imgPath: '../../../../_shared/media/images/stpanel',
      imgExt: '.PNG',
      comps: [
        {n:1, name:'POWER SUPPLY', desc:'Presa di corrente e interruttore; comprende anche un filtro IEC'},
        {n:2, name:'AIR SUPPLY',   desc:'Ingresso aria'},
        {n:3, name:'LIGHT ON',     desc:'LED di stato backlight'},
        {n:4, name:'READY/FAULT',  desc:'LED di stato Ready/Fault'},
        {n:5, name:'HOPPER',       desc:'Connettore tramoggia'},
        {n:6, name:'C-ETH',        desc:'Connettore Ethernet'},
        {n:7, name:'STO',          desc:'Connettore STO'}
      ]
    },
    encpanel: {
      imgPath: '../../../../_shared/media/images/encpanel',
      imgExt: '.PNG',
      comps: [
        {n:1, name:'POWER SUPPLY', desc:'Presa di corrente e interruttore; comprende anche un filtro IEC'},
        {n:2, name:'LIGHT ON',     desc:'LED di stato backlight'},
        {n:3, name:'READY/FAULT',  desc:'LED di stato Ready/Fault'},
        {n:4, name:'HOPPER',       desc:'Connettore tramoggia'},
        {n:5, name:'C-ETH',        desc:'Connettore Ethernet'},
        {n:6, name:'ENCODER',      desc:'Passaggio cavo encoder'},
        {n:7, name:'AIR SUPPLY',   desc:'Ingresso aria'},
        {n:8, name:'I/O',          desc:'Connettore I/O'},
        {n:9, name:'STO',          desc:'Connettore STO'}
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
Prima di effettuare qualsiasi connessione elettrica, assicurarsi che l'alimentazione sia disinserita e che il sistema sia in stato di sicurezza. 
:::

:::{important}
Lasciare circa {ref}`100mm di spazio libero <dim800>` attorno ai connettori di alimentazione per agevolare le operazioni di cablaggio e manutenzione.
:::

L'interfaccia elettrica del FlexiBowl® cambia in base alla taglia della macchina:

- **FlexiBowl® 500 – 1200**: tutti i connettori (STO, Ethernet, Hopper, alimentazione, aria) si trovano su un unico **pannello elettrico standard**, montato direttamente sulla macchina.
- **FlexiBowl® 200 / 350**: i connettori principali si trovano su un **rack** esterno; il rack viene poi collegato alla macchina tramite 4 cavi dedicati (Ethernet, Motore+STO, segnale A, segnale B). Sulla macchina resta da collegare solo l'aria compressa.

---

## FlexiBowl® 500 – 1200 — Pannello Elettrico Standard

```{list-table}
:widths: 8 52 40
:header-rows: 1

* - #
  - Azione
  - Immagine
* - 1
  - **Collegare lo STO.**

    Connettore a 10 pin. Necessario per attivare il motore.

    <div class="ars-step-note">
    Gli ingressi <strong>+STO1</strong> e <strong>+STO2</strong> devono ricevere <strong>+24 Vdc</strong> dal circuito di sicurezza; <strong>−STO1</strong> e <strong>−STO2</strong> vanno collegati al riferimento −24 Vdc.
    </div>

    <details class="ars-dropdown"><summary>Pinout connettore STO (10 pin)</summary><div class="ars-dropdown-body">

    | Pin | Descrizione |
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
    :alt: Collegare lo STO
    :class: ars-zoom-img
    ```

* - 2
  - **Collegare l'Ethernet (C-ETH).**

    Connettore M12, codifica D-Code. Consente la comunicazione con il FlexiBowl®, accessibile anche tramite web browser.

    <div class="ars-step-attn">
    Quando il FlexiBowl® è alimentato, il collegamento Ethernet è <strong>obbligatorio</strong>: se assente, la macchina entra in stato di <strong>ERROR</strong> (LED Ready/Fault rosso).
    </div>

    <details class="ars-dropdown"><summary>Pinout M12 → RJ45</summary><div class="ars-dropdown-body">

    Adattatore M12 8 poli → RJ45:

    | Pin | Colore |
    |---|---|
    | 1 | Giallo |
    | 2 | Arancione |
    | 3 | Bianco |
    | 4 | Non assegnato |
    | 5 | Non assegnato |
    | 6 | Blu |
    | 7 | Non assegnato |
    | 8 | Non assegnato |

    Connettore M12 D-code 4 poli:

    | Pin | Colore |
    |---|---|
    | 1 | Giallo |
    | 2 | Bianco |
    | 3 | Arancione |
    | 4 | Blu |

    </div></details>
  -
    ```{image} ../../../../_shared/media/images/stpanel6.PNG
    :alt: Collegare l'Ethernet
    :class: ars-zoom-img
    ```

* - 3
  - **Collegare l'Hopper.**

    Connettore M12 A-code, utilizzato per comunicare con i controller hopper ARS tramite protocollo **Modbus RTU**.

    <details class="ars-dropdown"><summary>Pinout M12 A-code</summary><div class="ars-dropdown-body">

    | Pin | Colore |
    |---|---|
    | 1 | Marrone |
    | 2 | Bianco |
    | 3 | Blu |
    | 4 | Nero |
    | 5 | Grigio |

    </div></details>
  -
    ```{image} ../../../../_shared/media/images/stpanel5.PNG
    :alt: Collegare l'Hopper
    :class: ars-zoom-img
    ```

* - 4
  - **Collegare l'alimentazione (Power Supply) — per ultima.**

    Connettore fornito in dotazione, identificato con la sigla **POWER SUPPLY**. Il pulsante di alimentazione consente di accendere/spegnere il dispositivo.

    <div class="ars-step-attn">
    Assicurarsi che il FlexiBowl® sia <strong>spento</strong> prima di collegare l'alimentazione, e che il dispositivo sia collegato a terra.
    </div>

    <div class="ars-step-warn">
    Tensione ammessa: <strong>120–230 Vac, 50/60 Hz</strong>.
    </div>

    <div class="ars-step-note">
    Il connettore di alimentazione è provvisto di un supporto per l'alloggiamento di <strong>n. 2 fusibili</strong>, con funzione di protezione da eventuali anomalie elettriche. Al primo avvio, verificarne sempre lo stato prima di accendere il dispositivo.
    </div>

    <details class="ars-dropdown"><summary>Schema pinout cavo alimentazione</summary><div class="ars-dropdown-body">

    | Colore | Tipo | Etichetta |
    |---|---|---|
    | Marrone | Fase | L1 |
    | Blu | Neutro | N1 |
    | Giallo/Verde | Terra | PE1 |

    </div></details>
  -
    ```{image} ../../../../_shared/media/images/stpanel1.PNG
    :alt: Collegare l'alimentazione
    :class: ars-zoom-img
    ```

```

:::{note}
Dopo l'accensione, verificare sempre lo stato della macchina tramite i **LED di stato** sul pannello frontale — vedi sezione {ref}`LED di Stato <led-stato>` più in basso in questa pagina.
:::

---

## FlexiBowl® 200 / 350 — Rack Esterno

I modelli FlexiBowl® FB 200 e FB 350 sono dotati di un **Rack** esterno, contenente tutti i dispositivi elettronici necessari al funzionamento. I connettori verso gli impianti del cliente si trovano sul rack (non sulla macchina) e hanno la **stessa piedinatura** dei corrispondenti connettori del pannello standard, semplicemente posizionati su un box esterno.

### Collegamenti sul Rack

```{list-table}
:widths: 8 52 40
:header-rows: 1

* - #
  - Azione
  - Immagine
* - 1
  - **Collegare lo STO** sul rack.

    Connettore a 10 pin, stessa funzione e piedinatura del pannello standard.

    <div class="ars-step-note">
    Gli ingressi <strong>+STO1</strong> e <strong>+STO2</strong> devono ricevere <strong>+24 Vdc</strong> dal circuito di sicurezza; <strong>−STO1</strong> e <strong>−STO2</strong> vanno collegati al riferimento −24 Vdc.
    </div>

    <details class="ars-dropdown"><summary>Pinout connettore STO (10 pin)</summary><div class="ars-dropdown-body">

    | Pin | Descrizione |
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
    :alt: Collegare lo STO
    :class: ars-zoom-img
    ```

* - 2
  - **Collegare il C-ETH IN** sul rack.

    Connettore M12, codifica D-Code.

    <div class="ars-step-attn">
    Collegamento <strong>obbligatorio</strong> a macchina alimentata: se assente, la macchina va in ERROR (LED Ready/Fault rosso).
    </div>

    <details class="ars-dropdown"><summary>Pinout M12 → RJ45</summary><div class="ars-dropdown-body">

    Adattatore M12 8 poli → RJ45:

    | Pin | Colore |
    |---|---|
    | 1 | Giallo |
    | 2 | Arancione |
    | 3 | Bianco |
    | 4 | Non assegnato |
    | 5 | Non assegnato |
    | 6 | Blu |
    | 7 | Non assegnato |
    | 8 | Non assegnato |

    Connettore M12 D-code 4 poli:

    | Pin | Colore |
    |---|---|
    | 1 | Giallo |
    | 2 | Bianco |
    | 3 | Arancione |
    | 4 | Blu |

    </div></details>
  -
    ```{image} ../../../../_shared/media/images/rack6.PNG
    :width: 110%
    :alt: Pannello rack
    :class: ars-zoom-img
    ```

* - 3
  - **Collegare l'Hopper** sul rack.

    Connettore M12 A-code, protocollo **Modbus RTU**.

    <details class="ars-dropdown"><summary>Pinout M12 A-code</summary><div class="ars-dropdown-body">

    | Pin | Colore |
    |---|---|
    | 1 | Marrone |
    | 2 | Bianco |
    | 3 | Blu |
    | 4 | Nero |
    | 5 | Grigio |

    </div></details>
  -
    ```{image} ../../../../_shared/media/images/rack7.PNG
    :width: 110%
    :alt: Pannello rack
    :class: ars-zoom-img
    ```

* - 4
  - **Collegare l'alimentazione** sul rack — per ultima.

    Presa di corrente con interruttore; comprende anche un filtro IEC.

    <div class="ars-step-attn">
    Assicurarsi che il FlexiBowl® sia <strong>spento</strong> prima di collegare l'alimentazione.
    </div>

    <div class="ars-step-warn">
    Tensione ammessa: <strong>120–230 Vac, 50/60 Hz</strong>.
    </div>

    <div class="ars-step-note">
    Anche sul rack, il connettore di alimentazione dispone dell'alloggiamento per i <strong>2 fusibili</strong> di protezione: verificarne lo stato al primo avvio.
    </div>

    <details class="ars-dropdown"><summary>Schema pinout cavo alimentazione</summary><div class="ars-dropdown-body">

    | Colore | Tipo | Etichetta |
    |---|---|---|
    | Marrone | Fase | L1 |
    | Blu | Neutro | N1 |
    | Giallo/Verde | Terra | PE1 |

    </div></details>
  -
    ```{image} ../../../../_shared/media/images/rack1.PNG
    :width: 110%
    :alt: Pannello rack
    :class: ars-zoom-img
    ```
```

### Collegamento tra Rack e FlexiBowl®

Il rack comunica con il FlexiBowl® tramite 4 cavi dedicati, ciascuno da collegare **esclusivamente** alla porta con l'etichetta corrispondente sul pannello macchina.

:::{attention}
Collegare ogni cavo alla porta con l'**etichetta corrispondente** (es. MOTOR ↔ MOTOR, C-A SIGNAL ↔ C-A SIGNAL). Un collegamento incrociato può danneggiare il sistema.
:::

```{list-table}
:widths: 8 52 40
:header-rows: 1

* - #
  - Azione
  - Immagine
* - 5
  - **Collegare il cavo Ethernet (C-ETH FB)** tra Rack e FlexiBowl®.

    Connettore M12 D-code.
  -
    ```{image} ../../../../_shared/media/images/rack8.PNG
    :width: 110%
    :alt: Collegare il cavo C-ETH FB
    :class: ars-zoom-img
    ```
    ```{image} ../../../../_shared/media/images/smallpanel4.PNG
    :width: 110%
    :alt: Collegare il cavo C-ETH FB
    :class: ars-zoom-img
    ```
* - 6
  - **Collegare il cavo MOTOR.**

    <div class="ars-step-note">
    Connettore a 9 pin: veicola sia l'alimentazione del motore sia i segnali <strong>STO</strong> verso il FlexiBowl® (sul rack, STO e Motore sono connettori separati; sul cavo verso la macchina sono combinati in un unico connettore a 9 pin).
    </div>

    <details class="ars-dropdown"><summary>Pinout connettore Motor (9 pin)</summary><div class="ars-dropdown-body">

    | Pin | Descrizione |
    |---|---|
    | 1 | +STO1 – Safety Torque Off |
    | 2 | +24 Vdc – Alimentazione ausiliaria |
    | 3 | +STO2 – Safety Torque Off |
    | 4 | −24 Vdc – Alimentazione ausiliaria |
    | 5 | NC |
    | 6 | +48 Vdc – Motor Power |
    | 7 | −STO1 – Safety Torque Off |
    | 8 | −48 Vdc – Motor Power |
    | 9 | −STO2 – Safety Torque Off |

    </div></details>
  -
    ```{image} ../../../../_shared/media/images/rack3.PNG
    :width: 110%
    :alt: Collegare il cavo Motor
    :class: ars-zoom-img
    ```
    ```{image} ../../../../_shared/media/images/smallpanel3.PNG
    :width: 110%
    :alt: Collegare il cavo C-ETH FB
    :class: ars-zoom-img
    ```
* - 7
  - **Collegare il cavo C-A SIGNAL.**

    Connettore a 12 pin per i segnali analogici.

    <details class="ars-dropdown"><summary>Pinout C-A Signal (12 pin)</summary><div class="ars-dropdown-body">

    | Pin | Descrizione |
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
    :alt: Collegare il cavo C-A Signal
    :class: ars-zoom-img
    ```
    ```{image} ../../../../_shared/media/images/smallpanel1.PNG
    :width: 110%
    :alt: Collegare il cavo C-ETH FB
    :class: ars-zoom-img
    ```
* - 8
  - **Collegare il cavo C-B SIGNAL.**

    Connettore a 19 pin per i segnali digitali, incluse le attivazioni dei LED di stato.

    <details class="ars-dropdown"><summary>Pinout C-B Signal (19 pin)</summary><div class="ars-dropdown-body">

    | Pin | Descrizione |
    |---|---|
    | 1 | +24 Vdc – Attivazione Led Verde Stato |
    | 2 | −24 Vdc – Comune Led Stato |
    | 3 | +24 Vdc – Attivazione Led Rosso Stato |
    | 4 | +24 Vdc – Attivazione Led Stato Back light |
    | 5 | −24 Vdc – Attivazione Led Stato Back light |
    | 6 | +24 Vdc – Attivazione Back light |
    | 7 | −24 Vdc – Attivazione Back light |
    | 8 | +24 Vdc – Attivazione Flip |
    | 9 | −24 Vdc – Attivazione Flip |
    | 10 | +24 Vdc – Attivazione Blow |
    | 11 | −24 Vdc – Attivazione Blow |
    | 12–19 | NC |

    </div></details>
  -
    ```{image} ../../../../_shared/media/images/rack5.PNG
    :width: 110%
    :alt: Collegare il cavo C-B Signal
    :class: ars-zoom-img
    ```
    ```{image} ../../../../_shared/media/images/smallpanel2.PNG
    :width: 110%
    :alt: Collegare il cavo C-ETH FB
    :class: ars-zoom-img
    ```
```

:::{note}
Dopo l'accensione, verificare sempre lo stato della macchina tramite i **LED di stato** sul pannello frontale — vedi sezione {ref}`LED di Stato <led-stato>` più in basso in questa pagina.
:::

---

(led-stato)=
## LED di Stato

Sul pannello frontale del FlexiBowl® sono presenti due LED di stato, comuni a **tutte le taglie** (500–1200 e 200/350):

| LED | Colore | Significato |
|---|---|---|
| **Light ON** | Verde (unico stato) | Indica se il backlight a bordo del FlexiBowl® è ON o OFF. Il backlight viene utilizzato dal sistema di visione per illuminare i componenti e renderli riconoscibili. Attivabile tramite il software di visione oppure mediante comandi provenienti da un sistema esterno in comunicazione Ethernet. |
| **Ready / Fault** | Verde | Sistema operativo e privo di anomalie. Collegamento Ethernet corretto. |
| **Ready / Fault** | Rosso | Anomalia interna oppure anomalia nel collegamento Ethernet. Fare riferimento alla tabella delle anomalie. |

:::{note}
Dopo l'accensione, attendere che il LED **Ready/Fault** si accenda: se Hopper e C-ETH sono collegati correttamente, il LED sarà **verde**.
:::

---

## Opzione FlexiTrack — Pannellino di Interfaccia

Il pannellino in dotazione con l'opzione FlexiTrack aggiunge, oltre ai collegamenti già descritti, i seguenti connettori dedicati:

- **Connettore I/O**: scambio segnali digitali, inclusa la funzione Latch.
- **Passacavo encoder**: dedicato all'encoder interno al FlexiBowl®.

```{list-table}
:widths: 8 52 40
:header-rows: 1

* - #
  - Azione
  - Immagine
* - 10
  - **Collegare il connettore I/O** a 19 pin.

    <details class="ars-dropdown"><summary>Pinout connettore I/O (19 pin)</summary><div class="ars-dropdown-body">

    | Pin | Segnale |
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
    :alt: Connettore I/O FlexiTrack
    :class: ars-zoom-img
    ```
* - 11
  - **Collegare il passacavo encoder**, dedicato all'encoder interno al FlexiBowl®.
  -
    ```{image} ../../../../_shared/media/images/encpanel8.PNG
    :alt: Passacavo encoder FlexiTrack
    :class: ars-zoom-img
    ```
```

---

## Note e Avvertenze Generali

:::{attention}
Tutte le operazioni di connessione devono essere eseguite a dispositivo spento e scollegato dall'alimentazione.
:::

:::{attention}
Il collegamento di terra è obbligatorio e deve essere verificato prima di ogni accensione.
:::

:::{attention}
In caso di anomalia indicata dal LED rosso (Ready/Fault), fare riferimento alla tabella delle anomalie specifica del modello.
:::

:::{attention}
Per ulteriori informazioni tecniche o assistenza, contattare ARS s.r.l. – FlexiBowl® Division.
:::





