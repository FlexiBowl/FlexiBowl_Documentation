(panoramica)=
# **Übersicht und Auspacken**

## Hauptkomponenten des FlexiBowl®

Der FlexiBowl® besteht aus den folgenden Hauptteilen:

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
//        {n:1,  name:'Pneumatikeinheit',           desc:'Sie versorgen die Flip-Einheit und eventuelle Blasdüsen.'},
//        {n:2,  name:'Motoreinheit',               desc:'Ermöglicht die Rotation der Oberfläche bzw. der starren Scheibe.'},
        {img:3,  name:'Haltering',      desc:'Besteht aus mehreren Segmenten und verhindert, dass Teile während des Betriebs herausfallen. Enthält auch die Abweiser, wenn kein Zubehör montiert ist.'},
//        {img:4,  name:'Backlight',                   desc:'Beleuchtet den Sichtbereich von hinten, um die Konturen der Teile hervorzuheben.'},
        {img:5,  name:'Flip-Schirm',                desc:'Verhindert, dass Teile beim Wenden herausfallen.'},
        {img:6,  name:'Gehäuse',                      desc:'Umschließt und schützt die internen Elemente. Schützt den Benutzer vor elektrischer Spannung und beweglichen Teilen.'},
//        {img:7,  name:'Flip-Einheit',                 desc:'Schlagelement, angetrieben von einem pneumatischen Mini-Schlitten (350–1200) oder einem Pneumatikzylinder (200). Erzeugt einen Impuls, der die Objekte vor dem Sichtfenster wendet.'},
//        {n:8,  name:'Rahmen',                      desc:'Es ist die tragende Struktur des FlexiBowl®.'},
//        {n:9, name:'Elektronikeinheit',          desc:'Enthält die gesamte Steuerelektronik des FlexiBowl®.'},
//        {n:10, name:'Anschlussfeld',         desc:'Enthält alle elektrischen und pneumatischen Anschlüsse.'},
        {img:11, name:'Halterung Oberfläche / Scheibe', desc:'Hält die Oberfläche bzw. die starre Scheibe fest mit der Motoreinheit verbunden.'},
//        {n:12, name:'Abdeckplatten',        desc:'Ermöglichen einen einfachen Zugang zu den internen Komponenten für Wartungsarbeiten.'}
      ]
    },
    fb350: {
      imgPath: '../../../../_shared/media/images/FB350-',
      imgDefault: '../../../../_shared/media/images/FB350-0.PNG',
      imgExt: '.PNG',
      comps: [
        {img:1,  name:'Kabel und Verlängerungen',  desc:'Sie sind die elektronischen Verbindungen zwischen den verschiedenen internen Komponenten des FlexiBowl®.'},
//        {n:2,  name:'Pneumatikeinheit', desc:'Versorgt die Flip-Einheit und die Blasdüsen.'},
//        {n:3,  name:'Motoreinheit',     desc:'Ermöglicht die Rotation der starren Scheibe.'},
        {img:4,  name:'Scheibe',             desc:'<a href="../ACCESSORI/02_DISCHI_RIGIDI.html">Siehe eigenen Abschnitt</a>.'},
//        {n:5,  name:'Backlight',         desc:'Beleuchtet den Sichtbereich von hinten, um die Konturen der Teile hervorzuheben.'},
        {img:6,  name:'Flip-Schirm',      desc:'Verhindert, dass Teile beim Wenden herausfallen. Enthält auch die <a href="../ACCESSORI/06-4_INTEGRATI.html">Blasdüsen</a>.'},
        {img:7,  name:'Gehäuse',            desc:'Umschließt und schützt die internen Elemente. Schützt den Benutzer vor elektrischer Spannung und beweglichen Teilen.'},
//        {n:8,  name:'Flip-Einheit',       desc:'Schlagelement, angetrieben von einem Pneumatikzylinder (200). Erzeugt einen Impuls, der die Objekte vor dem Sichtfenster wendet.'},
//        {n:9,  name:'Rahmen',            desc:'Es ist die tragende Struktur des FlexiBowl®.'},
        {img:10, name:'Scheibenhalterung',    desc:'Hält die starre Scheibe fest mit der Motoreinheit verbunden.'},
        {img:11, name:'Rack',              desc:'Enthält die gesamte Elektronik des FlexiBowl®.'}
      ]
    },
    fb200: {
      imgPath: '../../../../_shared/media/images/FB200-',
      imgDefault: '../../../../_shared/media/images/FB200-0.PNG',
      imgExt: '.PNG',
      comps: [
        {img:1,  name:'Kabel und Verlängerungen',  desc:'Sie sind die elektronischen Verbindungen zwischen den verschiedenen internen Komponenten des FlexiBowl®.'},
//        {n:2,  name:'Pneumatikeinheit', desc:'Versorgt die Flip-Einheit und die Blasdüsen.'},
//        {n:3,  name:'Motoreinheit',     desc:'Ermöglicht die Rotation der starren Scheibe.'},
        {img:4,  name:'Scheibe',             desc:'<a href="../ACCESSORI/02_DISCHI_RIGIDI.html">Siehe eigenen Abschnitt</a>.'},
//        {n:5,  name:'Backlight',         desc:'Beleuchtet den Sichtbereich von hinten, um die Konturen der Teile hervorzuheben.'},
        {img:6,  name:'Flip-Schirm',      desc:'Verhindert, dass Teile beim Wenden herausfallen. Enthält auch die <a href="../ACCESSORI/06-4_INTEGRATI.html">Blasdüsen</a>.'},
        {img:7,  name:'Gehäuse',            desc:'Umschließt und schützt die internen Elemente. Schützt den Benutzer vor elektrischer Spannung und beweglichen Teilen.'},
//        {n:8,  name:'Flip-Einheit',       desc:'Schlagelement, angetrieben von einem Pneumatikzylinder (200). Erzeugt einen Impuls, der die Objekte vor dem Sichtfenster wendet.'},
//        {n:9,  name:'Rahmen',            desc:'Es ist die tragende Struktur des FlexiBowl®.'},
        {img:10, name:'Rack',              desc:'Enthält die gesamte Elektronik des FlexiBowl®.'}
      ]
    }
  };

  Object.keys(models).forEach(function(id){
  models[id].comps.forEach(function(c, i){
    if (c.img === undefined) c.img = c.n;
    c.n = i + 1;
  });
});

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
    newImg.src = m.imgPath + c.img + m.imgExt;   // <-- c.img, non c.n
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

## Was ist im Lieferumfang enthalten?


Dieser Abschnitt beschreibt den Inhalt der Verpackung des **FlexiBowl® 3.0** und die mit der Einheit gelieferten Standardkomponenten.

:::{important}
Vor der Installation prüfen, ob alle in diesem Abschnitt aufgeführten Komponenten in der Verpackung vorhanden sind. Bei fehlenden oder beschädigten Komponenten den [Technischen Support](support) kontaktieren, bevor das Gerät in Betrieb genommen wird.
:::

---

### 1. Verpackungsinhalt

In der Verpackung befinden sich der **FlexiBowl®** und alle Standard-Anschlussadapter:

```{list-table}
:header-rows: 1
:widths: 22 58 20

* - Komponente
  - Beschreibung
  - Bild
* - **Stromversorgungsstecker**
  - Mit Verriegelungsclip ausgestattet, der ein versehentliches Lösen verhindert
  - :::{image} ../../../../_shared/media/images/connettore_power.png
    :width: 100%
    :::
* - **10-poliges Steckerkabel**
  - Führt die 24-Vdc-Versorgung und die beiden Safe-Torque-Off-Kanäle (STO)
  - :::{image} ../../../../_shared/media/images/connettore_STO.png
    :width: 100%
    :::
* - **M12-D-kodierter Stecker**
  - Dient der Ethernet-Kommunikation zwischen dem FlexiBowl® und dem System
  - :::{image} ../../../../_shared/media/images/connettore_ethernet.png
    :width: 100%
    :::
* - **M12-A-kodierter Stecker**
  - Dient der Modbus-RTU-Kommunikation mit der Steuerung des Bulk Feeders
  - :::{image} ../../../../_shared/media/images/connettore_hopper.png
    :width: 100%
    :::
* - **USB-Stick**
  - Enthält die Handbücher der Einheit und den zugehörigen individuellen Prüfbericht (Test Report)
  - —
```
:::{note}
Die Verbindungskabel sind separat als Option in 3, 5 oder 10 Metern erhältlich: siehe {ref}`Verbindungskabel <cavi>`.
:::

---

### 2. Zusätzliche Komponenten je Baugröße


```{list-table}
:header-rows: 1
:widths: 20 20 60

* - Modell
  - Bild
  - Zusätzliche Ausstattung
* - **FlexiBowl® 200 / 350**
  - :::{image} ../../../../_shared/media/images/FB350.png
    :width: 100%
    :::
  - Enthält außerdem das **Rack** und die zugehörigen **Verbindungskabel**, die für die externe Elektronik erforderlich sind. Die mitgelieferten 3 m langen Kabel ermöglichen alle Verbindungen zwischen Rack und FlexiBowl®. Optional sind sie in 5/10 Metern erhältlich ({ref}`siehe Rack-Kabel <cavo-rack>`).
    :::{image} ../../../../_shared/media/images/rack.png
    :width: 100%
    :::
* - **FlexiBowl® 500 und größer**
  - :::{image} ../../../../_shared/media/images/FB650.png
    :width: 100%
    :::
  - Benötigen kein externes Anschluss-Rack: Die Elektronik ist direkt in die Einheit integriert
```


#### Anschlussfeld des Racks (FlexiBowl® 200 / 350)

```{image} ../../../../_shared/media/images/rack.png
:alt: Anschlussfeld des Racks
:width: 80%
:align: center
```

Das rückseitige Feld des Racks fasst alle im vorherigen Absatz beschriebenen Anschlusspunkte zusammen: Spannungsversorgung (**POWER SUPPLY**), Safe Torque Off (**STO**), Motor (**MOTOR**), Ethernet zum System (**C-ETH IN**) und zum FlexiBowl® (**C-ETH FB**), Bulk Feeder (**HOPPER**) und Encodersignale (**C-A SIGNAL**, **C-B SIGNAL**).

:::{note}
Einzelheiten zur Positionierung und zum Anschluss des Racks finden Sie im Abschnitt [Mechanische Installation](mech_install).
:::


---

### 3. Mitgelieferte Dokumentation

Der mitgelieferte USB-Stick enthält:

- Die **Handbücher** der Einheit (Offline-Version der Dokumentation)
- Der individuelle **Prüfbericht** (Test Report) des erworbenen FlexiBowl®



