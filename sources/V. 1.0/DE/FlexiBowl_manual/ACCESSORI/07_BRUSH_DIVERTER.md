(brush)=
# **Brush Diverter**

## Komponenten der Baugruppe
Die Baugruppe **Brush Diverter** kann bis zu **4 Bürsten** umfassen:

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
  <button class="fb-tab on"    onclick="fbSwitchTab('Spazzole',this)">Bürsten</button>
</div>

<!-- ══════════ Spazzole ══════════ -->
<div class="fb-panel on" id="fb-panel-Spazzole">
  <div class="fb-wrap">
    <div class="fb-img-outer">
      <img class="fb-img-base" id="Spazzole-img-base" src="../../../../_shared/media/images/brush0.PNG" alt="Bürstenbaugruppe" />
      <img class="fb-img-hl"   id="Spazzole-img-hl"   src="" alt="" aria-hidden="true" />
      <div class="fb-badge" id="Spazzole-badge"></div>
      <div class="fb-hint"  id="Spazzole-hint">Eine Komponente aus der Liste auswählen</div>
    </div>
    <div class="fb-list-panel">
      <div class="fb-list-head"><span>Nr.</span><span>Komponente</span><span>Beschreibung</span></div>
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
        {n:1,  name:'Zentrale Bürste',                       desc:'Bewegt die Komponenten von der zentralen Kappe des FlexiBowl® weg.'},
        {n:2,  name:'Abweiserbürsten',           desc:'Sie bewegen die Komponenten vom Rand des FlexiBowl® weg.'},
        {n:3,  name:'Verstellbare Bürste',               desc:'Manuell höhenverstellbar, verhindert es, dass sich Teile überlappen.'},
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

## Empfohlene Anwendungen

Die Baugruppe **Brush Diverter** ist zu bevorzugen:

- gegenüber der Blasluft, wenn die Bauteile **zu schwer** sind, um vom Luftstrahl bewegt zu werden;
- gegenüber den Standard-Abweisern, wenn **Spike-Oberflächen** verwendet werden.

---

## Montageverfahren

:::{warning} Attenzione
Vor der Montage sicherstellen, dass der FlexiBowl® **ausgeschaltet ist und stillsteht**.
:::

| Schritt | Vorgang |
|:----:|-----------|
| 1 | Die gesamte Einheit aus **Flip-Schirm und Barriere** durch Lösen der **vier** Befestigungsschrauben entfernen |
| 2 | Den Schirm durch die Baugruppe **Brush Diverter** ersetzen |
| 3 | Die neue Einheit aus **Brush Diverter und Flip-Barriere** befestigen |

---

## Einstellverfahren

:::{warning} Attenzione
Vor der Einstellung sicherstellen, dass der FlexiBowl® **ausgeschaltet ist und stillsteht**.
:::

### Mittlere Bürsten und Abweiser

| Schritt | Vorgang |
|:----:|-----------|
| 1 | Die **beiden** Befestigungsschrauben lösen |
| 2 | Das **Langloch** nutzen, um die Bürste in die gewünschte Position zu bringen |
| 3 | Die **Befestigungsschrauben** wieder festziehen |

### Verstellbare Bürste

| Schritt | Vorgang |
|:----:|-----------|
| 1 | Die **Schrauben** an den Seiten der Halterung lösen |
| 2 | Die Bürste entlang der **Skalensäulen** in die gewünschte Position verschieben |
| 3 | Die **Schrauben** an den Seiten der Halterung festziehen |

---

## Überprüfung der korrekten Funktion

Einen Handhabungstest des FlexiBowl® durchführen, um die Wirksamkeit der Abweiser zu beurteilen.

---

:::{seealso}
Weitere Informationen zu Zubehör und alternativen Konfigurationen finden Sie in:
- Handbuch des Standard-Abweisers
- Leitfaden zu kompatiblen Spike-Oberflächen
- FlexiBowl®-Datenblatt
:::