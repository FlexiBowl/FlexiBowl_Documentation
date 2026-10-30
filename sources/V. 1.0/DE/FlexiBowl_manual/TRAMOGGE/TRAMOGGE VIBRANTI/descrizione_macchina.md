# **Maschinenbeschreibung**

<p style="line-height: 1.6; border-left: 4px solid #34495e; padding-left: 15px; margin-bottom: 25px;">
  Bulk Feeder eignen sich besonders zum Zuführen und Vordosieren von kleinen, mittleren und großen Teilen. Sie werden von einem linearen Vibrationssockel angetrieben, dessen Modell sich nach der Größe des Bulk Feeders richtet.
</p>

Die Standardmaschine besteht aus den folgenden Hauptteilen:

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
  <button class="tr-tab on"    onclick="trSwitchTab('Bulk Feeder',this)">Vibrations-Bulk-Feeder</button>
</div>

<!-- ══════════ TRAMOGGIA ══════════ -->
<div class="tr-panel on" id="tr-panel-tramoggia">
  <div class="tr-wrap">
    <div class="tr-img-outer">
      <img class="tr-img-base" id="tramoggia-img-base" src="../../../../../_shared/media/images/tramoggia0.PNG" alt="Ansicht des Bulk Feeders" />
      <img class="tr-img-hl"   id="tramoggia-img-hl"   src="" alt="" aria-hidden="true" />
      <div class="tr-badge" id="tramoggia-badge"></div>
      <div class="tr-hint"  id="tramoggia-hint">Eine Komponente aus der Liste auswählen</div>
    </div>
    <div class="tr-list-panel">
      <div class="tr-list-head"><span>Nr.</span><span>Komponente</span><span>Beschreibung</span></div>
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
        {n:1,  name:'Halterung',        desc:'Dies ist die Komponente, die an der Maschine befestigt wird und auf der der Bulk Feeder positioniert wird.'},
        {n:2,  name:'Vibrationsbasis',    desc:'Dies ist die Hauptkomponente des Bulk Feeders; mithilfe eines Elektromagneten erzeugt sie die Vibration, die die Teile auf der Wanne vorantreibt.'},
        {n:3,  name:'Wanne',            desc:'Sie ist in 1,5 l, 5 l, 10 l, 20 l oder 40 l erhältlich, je nach zu verarbeitendem Bauteil. Auf Anfrage sind auch kundenspezifische Größen möglich. Die 1,5-l-Wanne besteht aus Kunststoff, die anderen aus Edelstahl.'},
        {n:4,  name:'Controller',       desc:'Er dient zur Einstellung der Vibration des Bulk Feeders.'},
        {n:5,  name:'Gehäuse',           desc:'Komponenten zum Schutz der Vibrationsbasis vor Stößen, Schmutz und Staub.'},
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
Bei kundenspezifischen Modellen können die Komponenten ganz oder teilweise von den angegebenen abweichen. Für solche Modelle ist die technische Projektakte heranzuziehen.
:::

## Komponenten und Funktionsweise

* **Aufbau des Sockels:** Der lineare Vibrationssockel besteht aus zwei Körpern, die durch Blattfedern miteinander verbunden sind.
* **Vibrationsmechanismus:** Der Betrieb beruht auf einem am feststehenden Körper befestigten Elektromagneten, der den beweglichen Körper anzieht und freigibt. Diese Bewegung erzeugt die Vibration, durch die sich die in der Wanne befindlichen Teile vorwärtsbewegen (die Wanne ist auf dem beweglichen Körper positioniert und mit Klemmbacken befestigt).
* **Elektrische Steuerung:** Hierfür benötigen die Vibratoren eine Steuerung, die Wechselstrom in Impulsstrom umwandelt und außerdem die Geschwindigkeit des Systems regelt.

---

## Bestimmungsgemäße Verwendung 

Der Bulk Feeder ist in sechs Basismodellen erhältlich. Kundenspezifische Modelle, die von den Basismodellen abgeleitet sind, sich aber in Abmessungen und Leistung unterscheiden, sind nach Abstimmung mit den Anforderungen des Anwenders realisierbar.

:::{note} 
**Hinweis zur Gültigkeit:** Die in diesem Handbuch enthaltenen Informationen gelten auch für kundenspezifische Modelle.
:::

**Fassungsvermögen der verfügbaren Standardmodelle:**

| Basismodell | Fassungsvermögen der Wanne | Tragfähigkeit |
|:--- |:--- | :--- | 
| **Modell 1** | 1,5 Liter | 1 kg | 
| **Modell 2** | 3 Liter | 1,5 kg | 
| **Modell 3** | 5 Liter | 6 kg |
| **Modell 4** | 10 Liter | 6 kg |
| **Modell 5** | 20 Liter | 6 kg |
| **Modell 6** | 40 Liter | 15 kg |


Die vorliegende Maschine ist für den industriellen Einsatz bestimmt zur:

::::{list-table}
:widths: 25 25 25 25
:header-rows: 1
:class: custom-safety-table

* - <span style="font-weight: bold; color: #2c3e50;">Vorgang</span>
  - <span style="font-weight: bold; color: #27ae60;">Zulässig</span>
  - <span style="font-weight: bold; color: #c0392b;">Nicht zulässig</span>
  - <span style="font-weight: bold; color: #2c3e50;">Arbeitsumgebung</span>

* - <div style="padding: 8px 0;"><span style="font-weight: 600; text-transform: uppercase; font-size: 0.9em; ">Handhabung zum Zweck der Zuführung von:</span></div>
  - <div style="background-color: #e8f8f5; border-left: 4px solid #2ecc71; padding: 10px; margin: 5px 0; border-radius: 4px; font-size: 0.95em; color: #117a65;">
      Bauteile, deren maximales Gewicht und maximale Abmessungen je nach Maschinenmodell variieren.
    </div>
  - <div style="background-color: #fdf2f2; border-left: 4px solid #e74c3c; padding: 10px; margin: 5px 0; border-radius: 4px; font-size: 0.95em; color: #78281f;">
      Alle anderen Bauteile, die nicht im zulässigen Bereich für maximales Gewicht und maximale Abmessungen liegen.
    </div>
  - <div style="background-color: #f4f6f7; padding: 10px; margin: 5px 0; border-radius: 4px; font-size: 0.95em; text-align: center; font-weight: 500; color: #566573;">
      Industriell
    </div>
::::

:::{IMPORTANT}
Weitere Informationen zur Art der zulässigen Bauteile finden sich im Abschnitt „Technische Daten“ dieses Handbuchs.
:::

<div style="display: flex; flex-direction: column; gap: 20px; margin: 20px 0;">

  <!-- Card 1: Destinazione d'Uso -->
  <div style="border-left: 5px solid #2980b9; background-color: #ebf5fb; padding: 20px; border-radius: 4px 8px 8px 4px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
    <h3 style="color: #2980b9; margin-top: 0; font-size: 1.2em; border-bottom: none;"> Verwendungszweck</h3>
    <p style="margin-bottom: 10px; color: #2c3e50;">Die Maschine wurde geschaffen, um:</p>
    <ul style="color: #34495e; margin-bottom: 0; padding-left: 20px;">
      <li style="margin-bottom: 5px;">die <strong>spezifischen Anforderungen</strong> zu erfüllen, die im Kaufvertrag genannt sind;</li>
      <li>entsprechend den <strong>Anweisungen und Einsatzgrenzen</strong> verwendet zu werden, die in diesem Handbuch angegeben sind.</li>
    </ul>
  </div>

  <!-- Card 2: Condizioni per la Sicurezza -->
  <div style="border-left: 5px solid #27ae60; background-color: #eafaf1; padding: 20px; border-radius: 4px 8px 8px 4px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
    <h3 style="color: #27ae60; margin-top: 0; font-size: 1.2em; border-bottom: none;"> Sicherheitsbedingungen</h3>
    <p style="margin-bottom: 10px; color: #2c3e50;">Die Maschine ist so konstruiert und gebaut, dass sie sicher arbeitet, <strong>jedoch ausschließlich, wenn</strong>:</p>
    <ul style="color: #34495e; margin-bottom: 0; padding-left: 20px;">
      <li style="margin-bottom: 5px;">sie innerhalb der im Vertrag und in diesem Handbuch angegebenen Grenzen eingesetzt wird;</li>
      <li style="margin-bottom: 5px;">die Verfahren des Betriebshandbuchs gewissenhaft befolgt werden;</li>
      <li style="margin-bottom: 5px;">die regelmäßige Wartung zu den angegebenen Zeitpunkten und auf die angegebene Weise durchgeführt wird;</li>
      <li style="margin-bottom: 5px;">bei Bedarf rechtzeitig die außerordentliche Wartung durchgeführt wird;</li>
      <li><strong style="color: #c0392b;">die Sicherheitseinrichtungen NIEMALS entfernt und/oder überbrückt werden.</strong></li>
    </ul>
  </div>

</div>

## Fehlanwendung (vernünftigerweise vorhersehbar)

<div style="border-left: 5px solid #c0392b; background-color: #fdf2f2; padding: 20px; border-radius: 4px; margin: 15px 0; box-shadow: 0 2px 5px rgba(0,0,0,0.03);">
  <ul style="color: #2c3e50; margin: 0; padding-left: 20px; line-height: 1.6;">
    <li style="margin-bottom: 8px;">Verarbeiten flüssiger Bauteile und feinen Strahlguts;</li>
    <li style="margin-bottom: 8px;">Ändern von Arbeitsparametern in einer Weise, die die Sicherheit beeinträchtigt;</li>
    <li style="margin-bottom: 8px;">Transport von Personen;</li>
    <li style="margin-bottom: 8px;">Verwendung der Maschine als Abstützpunkt;</li>
    <li style="margin-bottom: 8px;">Verwendung der Maschine, um Produktionswerte über den vorgeschriebenen Grenzen zu erzielen;</li>
    <li style="margin-bottom: 8px;">Ändern / Manipulieren der elektrischen und pneumatischen Anschlüsse der Maschine oder anderer ihrer Bauteile;</li>
    <li style="margin-bottom: 8px;">Verwendung der Maschine mit einem anderen als dem unter „Bestimmungsgemäße Verwendung (korrekt)“ aufgeführten Produkt;</li>
    <li style="margin-bottom: 0;">Verwendung der Maschine auf andere Weise als im Absatz „Bestimmungsgemäße Verwendung (korrekt)“ vorgesehen.</li>
  </ul>
</div>

:::{warning}
Jede von der vorgesehenen abweichende Verwendung der Maschine muss vorab schriftlich vom Hersteller genehmigt werden. Fehlt diese schriftliche Genehmigung, gilt die Verwendung als „unsachgemäß“; der Hersteller lehnt daher jede Haftung für eventuell verursachte Sach- oder Personenschäden ab und betrachtet jegliche Garantie auf die Maschine als erloschen.
:::

:::{important}
Eine unsachgemäße Verwendung der Maschine schließt jegliche Haftung des Herstellers aus.
:::

## Pflichten und Verbote 

### Pflichten der Anwender 

Der Anwender (Unternehmer oder Arbeitgeber) muss:

<div style="border-left: 5px solid #2980b9; background-color: #ebf5fb; padding: 20px; border-radius: 4px; margin: 15px 0; box-shadow: 0 2px 5px rgba(0,0,0,0.03);">
  <ul style="color: #2c3e50; margin: 0; padding-left: 20px; line-height: 1.6;">
    <li style="margin-bottom: 8px;">die Fähigkeiten und Bedingungen der Bediener im Hinblick auf deren Gesundheit und Sicherheit berücksichtigen;</li>
    <li style="margin-bottom: 8px;">die für die einzelnen Verfahren geeignete persönliche Schutzausrüstung (PSA) bereitstellen;</li>
    <li style="margin-bottom: 8px;">normgerechte Hebemittel und Hebeverfahren bereitstellen;</li>
    <li style="margin-bottom: 8px;">von den einzelnen Arbeitnehmern die Einhaltung der betrieblichen Regeln und Vorschriften zur Sicherheit und zur Verwendung der ihnen zur Verfügung gestellten kollektiven und individuellen Schutzmittel verlangen;</li>
    <li style="margin-bottom: 8px;">das Personal über die im Unfallfall zu befolgenden Verfahren unterweisen;</li>
    <li style="margin-bottom: 8px;">das Personal über die vorhandenen Restrisiken unterweisen;</li>
    <li style="margin-bottom: 8px;">das Personal über die zur Sicherheit der Bediener vorgesehenen Einrichtungen unterweisen;</li>
    <li style="margin-bottom: 8px;">das Personal über die Risiken der Lärmemission am Arbeitsplatz unterweisen;</li>
    <li style="margin-bottom: 0;">das Personal über die allgemeinen Unfallverhütungsvorschriften unterweisen, die in europäischen Richtlinien und in der Gesetzgebung des Bestimmungslandes der Maschine vorgesehen sind.</li>
  </ul>
</div>

:::{note} 
nur Personal an der Maschine arbeiten lassen, das dieses Handbuch gelesen hat und entsprechend geschult wurde.
:::

### Pflichten des eingesetzten Personals (Bediener/Wartungspersonal/Techniker)

Das Personal muss:

<div style="border-left: 5px solid #27ae60; background-color: #eafaf1; padding: 20px; border-radius: 4px; margin: 15px 0; box-shadow: 0 2px 5px rgba(0,0,0,0.03);">
  <ul style="color: #2c3e50; margin: 0; padding-left: 20px; line-height: 1.6;">
    <li style="margin-bottom: 8px;"><strong>Wartungsarbeiten immer bei ausgeschalteter Maschine durchführen.</strong> nie bewegte Teile schmieren;</li>
    <li style="margin-bottom: 8px;">bei laufender Maschine nicht in ihrer Nähe mit Ketten, Armbändern, Krawatten oder anderer Kleidung arbeiten, die sich in den Mechanismen verfangen kann;</li>
    <li style="margin-bottom: 8px;">lange Haare unbedingt zusammenbinden, um die Gefahr des Einzugs zu vermeiden;</li>
    <li style="margin-bottom: 8px;">Arbeiten am Schaltschrank, an Abzweigdosen, Kabeln und elektrischen Bauteilen <strong>ausschließlich bei ausgeschaltetem Hauptschalter durchführen</strong>;</li>
    <li style="margin-bottom: 8px;">sich vor dem Start der Maschine vergewissern, dass sich niemand in den Gefahrenbereichen befindet;</li>
    <li style="margin-bottom: 8px;">während des Betriebs höchste Aufmerksamkeit walten lassen, damit niemand direkt an die beweglichen Teile gelangen kann;</li>
    <li style="margin-bottom: 8px;">die vom Arbeitgeber zur Verfügung gestellten Schutzeinrichtungen sachgemäß verwenden;</li>
    <li style="margin-bottom: 0;">dem Arbeitgeber, der Führungskraft oder dem Vorgesetzten unverzüglich jeden Mangel oder jede Auffälligkeit an den Sicherheitseinrichtungen melden.</li>
  </ul>
</div>

### Verbote für das Bedienpersonal 

Insbesondere darf das Personal nicht:

<div style="border-left: 5px solid #c0392b; background-color: #fdf2f2; padding: 20px; border-radius: 4px; margin: 15px 0; box-shadow: 0 2px 5px rgba(0,0,0,0.03);">
  <ul style="color: #2c3e50; margin: 0; padding-left: 20px; line-height: 1.6;">
    <li style="margin-bottom: 8px;">die Maschine unsachgemäß verwenden (d. h. für andere als die im Absatz „Bestimmungsgemäße Verwendung“ angegebenen Zwecke);</li>
    <li style="margin-bottom: 8px;">ohne vorherige Genehmigung Sicherheits- oder Signaleinrichtungen entfernen oder verändern;</li>
    <li style="margin-bottom: 8px;">aus eigener Initiative Arbeiten oder Handgriffe ausführen, die außerhalb ihrer Zuständigkeit liegen oder die die eigene Sicherheit oder die anderer Arbeitnehmer gefährden können;</li>
    <li style="margin-bottom: 8px;">Armbänder, Ringe oder Halsketten tragen, die baumeln und von beweglichen Teilen erfasst werden können;</li>
    <li style="margin-bottom: 8px;">die Geschwindigkeiten der Maschinenkomponenten ohne ausdrückliche Zustimmung eines Verantwortlichen ersetzen oder ändern;</li>
    <li style="margin-bottom: 8px;">den programmierten Zyklus der Maschine in irgendeiner Weise verändern;</li>
    <li style="margin-bottom: 8px;">die elektrischen Anschlüsse mit dem Ziel verändern, die internen Sicherheitseinrichtungen auszuschalten oder zu überbrücken;</li>
    <li style="margin-bottom: 8px;">die Maschine verwenden, wenn sie nicht in vollständiger Übereinstimmung mit den geltenden Vorschriften installiert wurde;</li>
    <li style="margin-bottom: 8px;">die Maschine als Abstützpunkt verwenden, auch wenn sie nicht in Betrieb ist (bei Gefahr eines Sturzes des Bedieners und/oder einer Beschädigung der Struktur);</li>
    <li style="margin-bottom: 0;">die Maschine außerhalb der zulässigen Umgebungsbedingungen verwenden (siehe „Kapitel 5“).</li>
  </ul>
</div>

:::{attention}
ARS S.r.l. haftet nicht für Sach- oder Personenschäden, wenn:
•	festgestellt wird, dass die Maschine in einer der unzulässigen Umgebungen verwendet wurde;
•	die hier beschriebenen Pflichten und Verbote nicht eingehalten wurden.
:::

## Technische Daten 

```{list-table}
:header-rows: 1
:widths: 20 30 25 25

* - Größe des Bulk Feeders
  - Elektrische Versorgung
  - Frequenz / Phase
  - Stromaufnahme (A)
* - 1,5 l
  - 230 V AC ±5 % ({ref}`115 V AC auf Anfrage <tramoggia-110v>`)
  - 50-60 Hz / einphasig
  - 0,1
* - 3 l
  - 230 V AC ±5 % ({ref}`115 V AC auf Anfrage <tramoggia-110v>`)
  - 50-60 Hz / einphasig
  - 0,1
* - 5 l
  - 230 V AC ±5 % ({ref}`115 V AC auf Anfrage <tramoggia-110v>`)
  - 50-60 Hz / einphasig
  - 0,25
* - 10 l
  - 230 V AC ±5 % ({ref}`115 V AC auf Anfrage <tramoggia-110v>`)
  - 50-60 Hz / einphasig
  - 0,25
* - 20 l
  - 230 V AC ±5 % ({ref}`115 V AC auf Anfrage <tramoggia-110v>`)
  - 50-60 Hz / einphasig
  - 0,25
* - 40 l
  - 230 V AC ±5 % ({ref}`115 V AC auf Anfrage <tramoggia-110v>`)
  - 50-60 Hz / einphasig
  - 0,45
```

| Größe des Bulk Feeders | 1,5 l | 3 l | 5 l | 10 l | 20 l | 40 l |
|------------------------------|--------|------|------|-------|-------|-------|
| Entsprechendes Nettogewicht | 2 kg | 11 kg | 24 kg | 26 kg | 28 kg | 38 kg |

:::{attention}
Bei kundenspezifischen Modellen können die angegebenen Werte von denen in der Tabelle abweichen. Für solche Modelle ist die technische Projektakte heranzuziehen.
:::

## Layout 

![Abmessungen des Bulk Feeders](../../../../../_shared/media/images/dim_tramoggia.jpg)

| Abmessungen | 1,5 l | 3 l | 5 l | 10 l | 20 l | 40 l |
|------------|--------|------|------|-------|-------|-------|
| A | 350 mm | 450 mm | 480 mm | 670 mm | 780 mm | 780 mm |
| B | 65 mm | 100 mm | 130 mm | 155 mm | 183 mm | 208 mm |
| C | 90 mm | 120 mm | 150 mm | 160 mm | 215 mm | 315 mm |
| D | 211 mm | 215 mm | 247 mm | 247 mm | 247 mm | 290 mm |
| E | 350 mm | 515 mm | 515 mm | 690 mm | 780 mm | 780 mm |

:::{attention}
Bei kundenspezifischen Modellen können die angegebenen Werte von denen in der Tabelle abweichen. Für solche Modelle ist die technische Projektakte heranzuziehen.
:::


## Standard- und optionale Komponenten 

```{list-table} Zubehör und Ausstattung der Bulk Feeder
:widths: 20 40 25 15
:header-rows: 1

* - **Element**
  - **Beschreibung**
  - **Foto**
  - **Standard / Optional**

* - Dosierbarriere
  - Barrieredosierer zur Flussregulierung (einstellbar). Siehe {ref}`barriera`.
  - 
    :::{image} ../../../../../_shared/media/images/barriera_dosatrice.jpg
    :alt: Dosierbarriere
    :width: 120px
    :align: center
    :::
  - OPTIONAL (ausgenommen Bulk Feeder 1,5 l)

* - Sicherheitsschutz
  - Sicherheits-Handschutz. Siehe {ref}`hand-guard`.
  - 
    :::{image} ../../../../../_shared/media/images/protezione_sicurezza.jpg
    :alt: Sicherheitsschutz
    :width: 120px
    :align: center
    :::
  - OPTIONAL (ausgenommen Bulk Feeder 1,5 l)

* - Beschichtung
  - Polyurethan-Beschichtung der Wanne. Siehe {ref}`tramoggia-pu`.
  - 
    :::{image} ../../../../../_shared/media/images/rivestimento.png
        :alt: Beschichtung
        :width: 120px
        :align: center
    :::
  - OPTIONAL (ausgenommen Bulk Feeder 1,5 l)

* - Frontlichtschranke
  - Seine Funktion ist es, während des Zuführprozesses das Vorhandensein von Bauteilen im vorderen Bereich der Vibrationswanne zu prüfen. Siehe {ref}`fotocellula-frontale`.
  - 
    :::{image} ../../../../../_shared/media/images/fotocellula_frontale.png
        :alt: Frontlichtschranke
        :width: 120px
        :align: center
    :::
  - OPTIONAL (ausgenommen Bulk Feeder 1,5 l)

* - Rücklichtschranke
  - Seine Funktion ist es, den Füllstand der Teile in der Wanne zu überwachen. Siehe {ref}`fotocellula-posteriore`.
  - 
    :::{image} ../../../../../_shared/media/images/fotocellula_posteriore.png
        :alt: Rücklichtschranke
        :width: 120px
        :align: center
    :::
  - OPTIONAL (ausgenommen Bulk Feeder 1,5 l)

```

:::{note}
Die vollständige Liste der in der Preisliste verfügbaren Varianten, Zubehörteile und Optionen (einschließlich der 110-V-Versionen, der Schwingungsdämpfungs-Kits und der Steuerungskabel) finden Sie auf der Seite {ref}`Zubehör und Optionen <tramoggia-accessori>`.
:::

### Arbeitszyklus 

Nachfolgend wird der Arbeitszyklus vereinfacht beschrieben, gegliedert in die folgenden Betriebsphasen:

<div style="display: flex; flex-direction: column; gap: 15px; margin: 20px 0; position: relative;">

  <!-- Fase 1 -->
  <div style="display: flex; background-color: #f8f9fa; border-radius: 8px; border: 1px solid #e9ecef; overflow: hidden; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
    <div style="background-color: #2c3e50; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 60px; font-size: 1.4em; font-weight: bold; flex-shrink: 0;">
      1
    </div>
    <div style="padding: 15px 20px; display: flex; align-items: center; color: #2c3e50; line-height: 1.5;">
      <span>Der Bediener legt das zu verarbeitende Produkt manuell oder mit einem automatischen Beladesystem in die Wanne.</span>
    </div>
  </div>

  <!-- Fase 2 -->
  <div style="display: flex; background-color: #f8f9fa; border-radius: 8px; border: 1px solid #e9ecef; overflow: hidden; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
    <div style="background-color: #34495e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 60px; font-size: 1.4em; font-weight: bold; flex-shrink: 0;">
      2
    </div>
    <div style="padding: 15px 20px; display: flex; align-items: center; color: #2c3e50; line-height: 1.5;">
      <span>Der Bulk Feeder führt zyklisch Vibrationen aus (vom Bediener eingestellt), damit die Teile vorrücken können, sodass sie stets auf dem Zuführer vorhanden sind.</span>
    </div>
  </div>

</div>