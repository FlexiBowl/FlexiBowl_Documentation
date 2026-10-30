# **Außerordentliche Wartung**

:::{warning}
Die außerordentliche Wartung und die Reparatur der Maschine sind qualifizierten, geschulten und autorisierten Technikern vorbehalten, die beim Hersteller oder beim autorisierten Servicezentrum beschäftigt sind. Diese Eingriffe erfordern fundierte Spezialkenntnisse über die Maschinen, die erforderlichen Arbeitsschritte, die damit verbundenen Risiken und die korrekten Verfahren für ein sicheres Arbeiten.
:::

Treten außergewöhnliche Ereignisse auf, die außerordentliche Wartungsarbeiten erfordern, muss das reguläre Wartungspersonal des Anwenders diese Verfahren befolgen:
- den Zustand der beschädigten oder verstellten Baugruppen prüfen;
- die in diesem Abschnitt beschriebenen Arbeiten ausführen;
- Sind die auszuführenden Arbeiten in diesem Handbuch nicht behandelt, dem Hersteller einen Bericht über die Vorfälle, das Ergebnis der Inspektion und eventuelle Anmerkungen übermitteln.

Der Hersteller oder das autorisierte Servicezentrum bewertet die Situation im Einzelfall. Anschließend stimmen sie sich mit dem regulären Wartungspersonal über die Art des Eingriffs ab und wählen die geeignetste der nachfolgend aufgeführten Lösungen:
- der Hersteller entsendet einen autorisierten, geschulten und qualifizierten Techniker, der die erforderlichen Eingriffe durchführt;
- oder der Hersteller ermächtigt das reguläre Wartungspersonal des Anwenders, die Eingriffe durchzuführen, und übermittelt gegebenenfalls zusätzliche Anweisungen.

:::{warning}
Die auszutauschenden Ersatzteile sind bei ARS S.r.l. zu bestellen.

Verwendet der Kunde keine Originalersatzteile oder vom Hersteller nicht schriftlich genehmigte Teile, gilt der Hersteller als von jeglicher Haftung für den Betrieb der Maschine und die Sicherheit der Bediener befreit. Genehmigungen und/oder Anweisungen müssen stets schriftlich mitgeteilt werden. Ohne schriftliche Genehmigung ist das Arbeiten untersagt, und der Hersteller lehnt jede Haftung ab.
:::

:::{warning}
Wartungsarbeiten dürfen nur von qualifiziertem und autorisiertem Personal durchgeführt werden.
:::

::::{warning}
<table style="width: 100%; border: none; background: transparent;">
  <tr style="background: transparent !important; border: none !important;">
    <td style="width: 10%; border: none; vertical-align: middle; text-align: center; background: transparent !important;">
      <img src="../../../../_shared/media/images/corrente.png" style="width: 50px; height: auto;">
    </td>
    <td style="width: 90%; border: none; vertical-align: middle; background: transparent !important; padding-left: 15px;">
      Vor dem Entfernen der Abdeckung die elektrische Stromversorgung trennen.
    </td>
  </tr>
</table>
::::

:::{warning}
Vor den Wartungsarbeiten die elektrische und pneumatische Versorgung trennen.
:::

:::{note}
Beim Befestigen von Schrauben stets LOCTITE 243 verwenden, um ein einwandfreies Festziehen zu gewährleisten (mit Ausnahme der Schrauben des Flansches der Oberfläche bzw. der starren Scheibe am FlexiBowl®).
:::

## Mögliche Eingriffsgruppen

Der FlexiBowl® setzt sich aus den folgenden Baugruppen zusammen:

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
      <img class="fb-img-base" id="fb650-img-base" src="../../../../_shared/media/images/component_default.PNG" alt="Ansicht FlexiBowl® 650" />
      <img class="fb-img-hl"   id="fb650-img-hl"   src="" alt="" aria-hidden="true" />
      <div class="fb-badge" id="fb650-badge"></div>
      <div class="fb-hint"  id="fb650-hint">Eine Komponente aus der Liste auswählen</div>
    </div>
    <div class="fb-list-panel">
      <div class="fb-list-head"><span>Nr.</span><span>Komponente</span><span>Beschreibung</span></div>
      <div id="fb650-list"></div>
    </div>
  </div>
</div>

<!-- ══════════ FB350 ══════════ -->
<div class="fb-panel" id="fb-panel-fb350">
  <div class="fb-wrap">
    <div class="fb-img-outer">
      <img class="fb-img-base" id="fb350-img-base" src="../../../../_shared/media/images/FB350-0.PNG" alt="Ansicht FlexiBowl® 350" />
      <img class="fb-img-hl"   id="fb350-img-hl"   src="" alt="" aria-hidden="true" />
      <div class="fb-badge" id="fb350-badge"></div>
      <div class="fb-hint"  id="fb350-hint">Eine Komponente aus der Liste auswählen</div>
    </div>
    <div class="fb-list-panel">
      <div class="fb-list-head"><span>Nr.</span><span>Komponente</span><span>Beschreibung</span></div>
      <div id="fb350-list"></div>
    </div>
  </div>
</div>

<!-- ══════════ FB200 ══════════ -->
<div class="fb-panel on" id="fb-panel-fb200">
  <div class="fb-wrap">
    <div class="fb-img-outer">
      <img class="fb-img-base" id="fb200-img-base" src="../../../../_shared/media/images/FB200-0.PNG" alt="Ansicht FlexiBowl® 200" />
      <img class="fb-img-hl"   id="fb200-img-hl"   src="" alt="" aria-hidden="true" />
      <div class="fb-badge" id="fb200-badge"></div>
      <div class="fb-hint"  id="fb200-hint">Eine Komponente aus der Liste auswählen</div>
    </div>
    <div class="fb-list-panel">
      <div class="fb-list-head"><span>Nr.</span><span>Komponente</span><span>Beschreibung</span></div>
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
        {n:1,  name:'Pneumatikeinheit',           desc:'Sie versorgen die Flip-Einheit und eventuelle Blasdüsen.'},
        {n:2,  name:'Motoreinheit',               desc:'Ermöglicht die Rotation der Oberfläche bzw. der starren Scheibe.'},
        {n:3,  name:'Haltering',      desc:'Besteht aus mehreren Segmenten und verhindert, dass Teile während des Betriebs herausfallen. Enthält auch die Abweiser, wenn kein Zubehör montiert ist.'},
        {n:4,  name:'Backlight',                   desc:'Beleuchtet den Sichtbereich von hinten, um die Konturen der Teile hervorzuheben.'},
        {n:5,  name:'Flip-Schirm',                desc:'Verhindert, dass Teile beim Wenden herausfallen.'},
        {n:6,  name:'Gehäuse',                      desc:'Umschließt und schützt die internen Elemente. Schützt den Benutzer vor elektrischer Spannung und beweglichen Teilen.'},
        {n:7,  name:'Flip-Einheit',                 desc:'Schlagelement, angetrieben von einem pneumatischen Mini-Schlitten (350–1200) oder einem Pneumatikzylinder (200). Erzeugt einen Impuls, der die Objekte vor dem Sichtfenster wendet.'},
        {n:8,  name:'Rahmen',                      desc:'Es ist die tragende Struktur des FlexiBowl®.'},
        {n:9, name:'Elektronikeinheit',          desc:'Enthält die gesamte Steuerelektronik des FlexiBowl®.'},
        {n:10, name:'Anschlussfeld',         desc:'Enthält alle elektrischen und pneumatischen Anschlüsse.'},
        {n:11, name:'Halterung Oberfläche / Scheibe', desc:'Hält die Oberfläche bzw. die starre Scheibe fest mit der Motoreinheit verbunden.'},
        {n:12, name:'Abdeckplatten',        desc:'Ermöglichen einen einfachen Zugang zu den internen Komponenten für Wartungsarbeiten.'}
      ]
    },
    fb350: {
      imgPath: '../../../../_shared/media/images/FB350-',
      imgDefault: '../../../../_shared/media/images/FB350-0.PNG',
      imgExt: '.PNG',
      comps: [
        {n:1,  name:'Kabel und Verlängerungen',  desc:'Sie sind die elektronischen Verbindungen zwischen den verschiedenen internen Komponenten des FlexiBowl®.'},
        {n:2,  name:'Pneumatikeinheit', desc:'Versorgt die Flip-Einheit und die Blasdüsen.'},
        {n:3,  name:'Motoreinheit',     desc:'Ermöglicht die Rotation der starren Scheibe.'},
        {n:4,  name:'Scheibe',             desc:'<a href="../ACCESSORI/02_DISCHI_RIGIDI.html">Siehe eigenen Abschnitt</a>.'},
        {n:5,  name:'Backlight',         desc:'Beleuchtet den Sichtbereich von hinten, um die Konturen der Teile hervorzuheben.'},
        {n:6,  name:'Flip-Schirm',      desc:'Verhindert, dass Teile beim Wenden herausfallen. Enthält auch die <a href="../ACCESSORI/06-4_INTEGRATI.html">Blasdüsen</a>.'},
        {n:7,  name:'Gehäuse',            desc:'Umschließt und schützt die internen Elemente. Schützt den Benutzer vor elektrischer Spannung und beweglichen Teilen.'},
        {n:8,  name:'Flip-Einheit',       desc:'Schlagelement, angetrieben von einem Pneumatikzylinder (200). Erzeugt einen Impuls, der die Objekte vor dem Sichtfenster wendet.'},
        {n:9,  name:'Rahmen',            desc:'Es ist die tragende Struktur des FlexiBowl®.'},
        {n:10, name:'Scheibenhalterung',    desc:'Hält die starre Scheibe fest mit der Motoreinheit verbunden.'},
        {n:11, name:'Rack',              desc:'Enthält die gesamte Elektronik des FlexiBowl®.'}
      ]
    },
    fb200: {
      imgPath: '../../../../_shared/media/images/FB200-',
      imgDefault: '../../../../_shared/media/images/FB200-0.PNG',
      imgExt: '.PNG',
      comps: [
        {n:1,  name:'Kabel und Verlängerungen',  desc:'Sie sind die elektronischen Verbindungen zwischen den verschiedenen internen Komponenten des FlexiBowl®.'},
        {n:2,  name:'Pneumatikeinheit', desc:'Versorgt die Flip-Einheit und die Blasdüsen.'},
        {n:3,  name:'Motoreinheit',     desc:'Ermöglicht die Rotation der starren Scheibe.'},
        {n:4,  name:'Scheibe',             desc:'<a href="../ACCESSORI/02_DISCHI_RIGIDI.html">Siehe eigenen Abschnitt</a>.'},
        {n:5,  name:'Backlight',         desc:'Beleuchtet den Sichtbereich von hinten, um die Konturen der Teile hervorzuheben.'},
        {n:6,  name:'Flip-Schirm',      desc:'Verhindert, dass Teile beim Wenden herausfallen. Enthält auch die <a href="../ACCESSORI/06-4_INTEGRATI.html">Blasdüsen</a>.'},
        {n:7,  name:'Gehäuse',            desc:'Umschließt und schützt die internen Elemente. Schützt den Benutzer vor elektrischer Spannung und beweglichen Teilen.'},
        {n:8,  name:'Flip-Einheit',       desc:'Schlagelement, angetrieben von einem Pneumatikzylinder (200). Erzeugt einen Impuls, der die Objekte vor dem Sichtfenster wendet.'},
        {n:9,  name:'Rahmen',            desc:'Es ist die tragende Struktur des FlexiBowl®.'},
        {n:10, name:'Rack',              desc:'Enthält die gesamte Elektronik des FlexiBowl®.'}
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