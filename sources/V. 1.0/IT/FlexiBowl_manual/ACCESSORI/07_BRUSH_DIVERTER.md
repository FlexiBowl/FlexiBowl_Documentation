(brush)=
# [MEC] **Brush Diverter**

## Componenti del gruppo
Il gruppo **brush diverter** può comprendere fino a **4 spazzole**:

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
  <button class="fb-tab on"    onclick="fbSwitchTab('Spazzole',this)">Spazzole</button>
</div>

<!-- ══════════ Spazzole ══════════ -->
<div class="fb-panel on" id="fb-panel-Spazzole">
  <div class="fb-wrap">
    <div class="fb-img-outer">
      <img class="fb-img-base" id="Spazzole-img-base" src="../../../../_shared/media/images/brush0.PNG" alt="Gruppo spazzole" />
      <img class="fb-img-hl"   id="Spazzole-img-hl"   src="" alt="" aria-hidden="true" />
      <div class="fb-badge" id="Spazzole-badge"></div>
      <div class="fb-hint"  id="Spazzole-hint">Seleziona un componente dalla lista</div>
    </div>
    <div class="fb-list-panel">
      <div class="fb-list-head"><span>N.</span><span>Componente</span><span>Descrizione</span></div>
      <div id="Spazzole-list"></div>
    </div>
  </div>
</div>

<script>
(function(){

  /* ── dati componenti ── */
  var models = {
    Spazzole: {
      imgPath: '../../../../_shared/media/images/brush',
      imgDefault: '../../../../_shared/media/images/brush0.PNG',
      imgExt: '.PNG',
      comps: [
        {n:1,  name:'Spazzola centrale',                       desc:'Allontana i componenti dalla calotta centrale del FlexiBowl®.'},
        {n:2,  name:'Spazzole deviatore',           desc:'Allontanano i componenti dal bordo del FlexiBowl®.'},
        {n:3,  name:'Spazzola regolabile',               desc:'Di altezza variabile manualmente, serve a evitare che i pezzi si sovrappongano.'},
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

---

## Applicazioni consigliate

Preferire il gruppo **brush diverter**:

- Rispetto ai soffi quando i componenti sono **troppo pesanti** per essere spostati dal getto d'aria;
- Rispetto ai deviatori standard quando si utilizzano **superfici spike**.

---

## Procedura di montaggio

:::{warning} Attenzione
Assicurarsi che il FlexiBowl® sia **spento e fermo** prima di procedere con il montaggio.
:::

| Step | Operazione |
|:----:|-----------|
| 1 | Rimuovere tutto il gruppo **schermo-barriera flip** svitando le **quattro viti** di fissaggio |
| 2 | Sostituire lo schermo con il gruppo **brush diverter** |
| 3 | Fissare il nuovo gruppo **brush diverter-barriera flip** |

---

## Procedura di regolazione

:::{warning} Attenzione
Assicurarsi che il FlexiBowl® sia **spento e fermo** prima di procedere con la regolazione.
:::

### Spazzole centrale e deviatori

| Step | Operazione |
|:----:|-----------|
| 1 | Allentare le **due viti** di fissaggio |
| 2 | Sfruttare l'**asola** per portare la spazzola nella posizione desiderata |
| 3 | Stringere di nuovo le **viti di fissaggio** |

### Spazzola regolabile

| Step | Operazione |
|:----:|-----------|
| 1 | Allentare le **viti** ai lati del supporto |
| 2 | Far scorrere la spazzola sulle **colonne graduate** fino alla posizione desiderata |
| 3 | Stringere le **viti** ai lati del supporto |

---

## Valutazione del corretto funzionamento

Effetuare una prova di movimentazione del FlexiBowl® per valutare l'efficacia dei deviatori.

---

:::{seealso}
Per ulteriori informazioni su accessori e configurazioni alternative, consultare:
- Manuale del deviatore standard
- Guida alle superfici spike compatibili
- Scheda tecnica FlexiBowl®
:::