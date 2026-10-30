
# **Allgemeine Vorabinformationen**

```{important}
Lesen Sie vor Installation, Verwendung oder Wartung der Maschine das gesamte Handbuch und die gesamte beigefügte Dokumentation sorgfältig durch.

Die Nichtbeachtung der angegebenen Anweisungen kann Folgendes verursachen:
- Schäden an der Maschine;
- Verlust der Sicherheitsbedingungen;
- Gefahren für Bediener und Wartungspersonal;
- Erlöschen der Garantie.
```

<script src="https://unpkg.com/@phosphor-icons/web"></script>

<style>
/* ── Variabili e Reset ── */
.isw-page {
  --c-primary:    #1a3a52;
  --c-accent:     #2980b9;
  --c-accent-lt:  #d0e4f0;
  --c-bg:         #ffffff;
  --c-bg-alt:     #f7fbfe;
  --c-bg-hover:   #e8f4fc;
  --c-border:     #d0e4f0;
  --c-text:       #334e5e;
  --c-muted:      #7a9ab0;
  --radius:       10px;
  --shadow-sm:    0 1px 4px rgba(41,128,185,.08);
  --shadow-md:    0 3px 10px rgba(41,128,185,.12);
  max-width: 860px;
  margin: 0 auto;
  padding: 0 0 3rem;
}

/* ── Headings ── */
.isw-page h2 {
  color: var(--c-primary);
  font-weight: 700;
  border-bottom: 2px solid var(--c-accent-lt);
  padding-bottom: .4rem;
  margin-top: 2.5rem;
}
.isw-page h3 {
  color: var(--c-primary);
  font-weight: 600;
  margin-top: 1.6rem;
}

/* ── Meta Grid (Identificazione) ── */
.isw-meta-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1rem;
  margin: 1rem 0 2rem;
}
.isw-meta-card {
  padding: 1.2rem 1.4rem;
  border: 1.5px solid var(--c-border);
  border-radius: var(--radius);
  background: var(--c-bg);
  box-shadow: var(--shadow-sm);
  transition: box-shadow .2s;
}
.isw-meta-card:hover { box-shadow: var(--shadow-md); }

.isw-meta-title {
  font-size: .75rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: .06em;
  color: var(--c-accent);
  margin-bottom: .6rem;
  display: flex;
  align-items: center;
  gap: .4rem;
}
.isw-meta-content {
  font-size: .9rem;
  line-height: 1.6;
  color: var(--c-primary);
}
.isw-meta-content small { color: var(--c-muted); display: block; margin-top: .4rem; line-height: 1.3; }

/* ── Badge modelli ── */
.isw-model-badges {
  display: flex;
  flex-wrap: wrap;
  gap: .4rem;
  margin-top: .5rem;
}
.isw-badge {
  background: var(--c-bg-alt);
  border: 1px solid var(--c-border);
  border-radius: 4px;
  padding: .15rem .55rem;
  font-size: .78rem;
  font-weight: 700;
  color: var(--c-accent);
  font-family: monospace;
}

/* ── Tabelle standard ── */
.isw-table {
  width: 100%;
  border-collapse: collapse;
  font-size: .9rem;
  margin: .75rem 0 1.5rem;
  border-radius: var(--radius);
  overflow: hidden;
  box-shadow: var(--shadow-sm);
}
.isw-table thead th {
  background: var(--c-bg-alt);
  color: var(--c-primary);
  border-bottom: 2px solid var(--c-accent);
  padding: .65rem 1rem;
  text-align: left;
  font-weight: 700;
  font-size: .8rem;
  text-transform: uppercase;
  letter-spacing: .05em;
}
.isw-table tbody tr { transition: background .15s; }
.isw-table tbody tr:nth-child(odd)  { background: var(--c-bg); }
.isw-table tbody tr:nth-child(even) { background: var(--c-bg-alt); }
.isw-table tbody tr:hover { background: var(--c-bg-hover); }
.isw-table td {
  padding: .55rem 1rem;
  border-bottom: 1px solid var(--c-border);
  color: var(--c-text);
  vertical-align: top;
}
.isw-table td:first-child {
  font-family: monospace;
  font-weight: 700;
  color: var(--c-accent);
  white-space: nowrap;
  width: 80px;
}

/* ── Dichiarazione CE ── */
.isw-ce-box {
  background: var(--c-bg-alt);
  border: 1px dashed var(--c-accent-lt);
  border-left: 4px solid var(--c-accent);
  border-radius: var(--radius);
  padding: 1.6rem;
  margin: 1.5rem 0;
}
.isw-ce-header {
  text-align: center;
  font-weight: 700;
  font-size: 1.05rem;
  color: var(--c-primary);
  margin-bottom: 1.2rem;
  letter-spacing: .08em;
  text-transform: uppercase;
}
.isw-ce-box ul { margin: .4rem 0 .8rem 1.2rem; }
.isw-ce-box li { margin-bottom: .2rem; font-size: .88rem; }

.isw-ce-footer {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: .4rem 2rem;
  margin-top: 1.2rem;
  padding-top: 1rem;
  border-top: 1px solid var(--c-border);
  font-size: .85rem;
}

/* ── Tabella Operatori / Profili ── */
.isw-profiles { margin: 1rem 0 1.5rem; display: flex; flex-direction: column; gap: .75rem; }
.isw-profile {
  border: 1.5px solid var(--c-border);
  border-radius: var(--radius);
  overflow: hidden;
  box-shadow: var(--shadow-sm);
}
.isw-profile-header {
  display: flex;
  align-items: center;
  gap: .6rem;
  background: var(--c-bg-alt);
  padding: .6rem 1rem;
  border-bottom: 1px solid var(--c-border);
}
.isw-profile-role {
  font-weight: 700;
  font-size: .85rem;
  color: var(--c-primary);
}
.isw-profile-body {
  padding: .8rem 1rem;
  font-size: .88rem;
  line-height: 1.6;
  color: var(--c-text);
}
.isw-profile-note {
  margin-top: .5rem;
  padding: .4rem .7rem;
  background: #fff8e1;
  border-left: 3px solid #f0b429;
  border-radius: 4px;
  font-size: .82rem;
  color: #7a5c00;
}

/* ── Persona Addestrata callout ── */
.isw-trained-person {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  padding: 1rem 1.2rem;
  border: 1.5px solid var(--c-border);
  border-radius: var(--radius);
  background: var(--c-bg);
  margin: 1rem 0 1.5rem;
  box-shadow: var(--shadow-sm);
}
.isw-trained-person-icon { font-size: 2rem; line-height: 1; flex-shrink: 0; }
.isw-trained-person-title { font-weight: 700; color: var(--c-accent); font-size: .8rem; text-transform: uppercase; letter-spacing: .05em; margin-bottom: .3rem; }

/* ── DPI / Simbologia Grid ── */
.isw-symbol-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
  gap: .75rem;
  margin: 1rem 0 1.5rem;
}
.isw-symbol-item {
  display: flex;
  align-items: flex-start;
  gap: .9rem;
  padding: .8rem 1rem;
  border: 1px solid var(--c-border);
  border-radius: var(--radius);
  background: var(--c-bg);
  transition: box-shadow .2s, background .15s;
}
.isw-symbol-item:hover { background: var(--c-bg-hover); box-shadow: var(--shadow-sm); }
.isw-symbol-item img { width: 52px; height: 52px; object-fit: contain; flex-shrink: 0; }
.isw-symbol-label { font-weight: 700; font-size: .88rem; color: var(--c-primary); margin-bottom: .25rem; }
.isw-symbol-desc  { font-size: .82rem; color: var(--c-text); line-height: 1.4; }

/* ── Rischi residui ── */
.isw-risks { display: flex; flex-direction: column; gap: .75rem; margin: 1rem 0 1.5rem; }
.isw-risk {
  display: grid;
  grid-template-columns: 100px 1fr;
  gap: 0;
  border: 1.5px solid var(--c-border);
  border-radius: var(--radius);
  overflow: hidden;
  box-shadow: var(--shadow-sm);
}
.isw-risk-icons {
  background: var(--c-bg-alt);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: .5rem;
  padding: .8rem;
  border-right: 1px solid var(--c-border);
}
.isw-risk-icons img { width: 44px; height: 44px; object-fit: contain; }
.isw-risk-body { padding: .9rem 1.1rem; }
.isw-risk-title { font-weight: 700; color: var(--c-primary); font-size: .9rem; margin-bottom: .4rem; }
.isw-risk-desc { font-size: .87rem; color: var(--c-text); line-height: 1.55; }
.isw-risk-desc ul { margin: .3rem 0 0 1.1rem; }
.isw-risk-desc li { margin-bottom: .15rem; }

/* ── Zone di sicurezza ── */
.isw-zones { display: flex; flex-direction: column; gap: .6rem; margin: 1rem 0 1.5rem; }
.isw-zone {
  display: grid;
  grid-template-columns: 160px 1fr;
  border: 1.5px solid var(--c-border);
  border-radius: var(--radius);
  overflow: hidden;
}
.isw-zone-label {
  background: var(--c-accent);
  color: #fff;
  font-weight: 700;
  font-size: .8rem;
  padding: .7rem .9rem;
  display: flex;
  align-items: center;
}
.isw-zone:nth-child(2) .isw-zone-label { background: #e67e22; }
.isw-zone:nth-child(3) .isw-zone-label { background: #c0392b; }
.isw-zone-desc { padding: .65rem .9rem; font-size: .87rem; color: var(--c-text); line-height: 1.5; background: var(--c-bg); }

/* ── Garanzia: due colonne ── */
.isw-warranty-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  margin: 1rem 0 1.5rem;
}
@media (max-width: 640px) {
  .isw-warranty-grid { grid-template-columns: 1fr; }
  .isw-risk { grid-template-columns: 1fr; }
  .isw-risk-icons { flex-direction: row; border-right: none; border-bottom: 1px solid var(--c-border); }
  .isw-zone { grid-template-columns: 1fr; }
}
.isw-warranty-col {
  border: 1.5px solid var(--c-border);
  border-radius: var(--radius);
  overflow: hidden;
}
.isw-warranty-col-header {
  padding: .55rem 1rem;
  font-weight: 700;
  font-size: .8rem;
  text-transform: uppercase;
  letter-spacing: .05em;
}
.isw-warranty-col.valid   .isw-warranty-col-header { background: #e8f8f0; color: #1a6b3a; border-bottom: 2px solid #27ae60; }
.isw-warranty-col.invalid .isw-warranty-col-header { background: #fdecea; color: #7b1c1c; border-bottom: 2px solid #c0392b; }
.isw-warranty-col ul { margin: .5rem .5rem .7rem 1.4rem; padding: 0; }
.isw-warranty-col li { font-size: .84rem; color: var(--c-text); margin-bottom: .3rem; line-height: 1.4; }

/* ── Sicurezze inline ── */
.isw-safety-cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: .85rem;
  margin: 1rem 0 1.5rem;
}
.isw-safety-card {
  border: 1.5px solid var(--c-border);
  border-radius: var(--radius);
  padding: 1rem 1.1rem;
  background: var(--c-bg);
}
.isw-safety-card-title {
  font-weight: 700;
  color: var(--c-primary);
  font-size: .88rem;
  margin-bottom: .35rem;
  display: flex;
  align-items: center;
  gap: .4rem;
}
.isw-safety-card p { font-size: .85rem; color: var(--c-text); line-height: 1.5; margin: 0; }
</style>

<div class="isw-page">

## Identifikation

<div class="isw-meta-grid">
  <div class="isw-meta-card">
    <div class="isw-meta-title"><i class="ph ph-factory"></i> Hersteller</div>
    <div class="isw-meta-content">
      <strong>ARS S.r.l.</strong><br>
      Via Aretina Nord, 157<br> 52041 – Pieve al Toppo (AR), Italien<br> Tel. +39 0575 398611 &nbsp;·&nbsp; Fax +39 0575 398620<br>
      <a href="mailto:info@arsautomation.com">info@arsautomation.com</a><br>
      <a href="https://www.arsautomation.com" target="_blank">www.arsautomation.com</a>
    </div>
  </div>
  <div class="isw-meta-card">
    <div class="isw-meta-title"><i class="ph ph-cpu"></i> Maschinenidentifikation</div>
    <div class="isw-meta-content">
      <strong>Maschine:</strong> Bulk Feeder<br>
      <strong>Basismodelle:</strong>
      <div class="isw-model-badges">
        <span class="isw-badge">1,5 l</span>
        <span class="isw-badge">3 l</span>
        <span class="isw-badge">5 l</span>
        <span class="isw-badge">10 l</span>
        <span class="isw-badge">20 l</span>
        <span class="isw-badge">40 l</span>
      </div>
      <small>Bei einigen Anwendungen können kundenspezifische Modelle vorhanden sein. Die Identifikation wird durch das Referenzprojekt festgelegt.</small>
    </div>
  </div>
</div>

### Typenschild

Die Maschine ist mit einem Typenschild an der **Vibrationsbasis** versehen. Die auf dem Schild angegebenen Daten müssen bei jeder Kommunikation mit ARS S.r.l. genannt werden.

![Etikett des Bulk Feeders](../../../../../_shared/media/images/etichetta_tramoggia.jpg)

<table class="isw-table">
  <thead>
    <tr>
      <th>Pos.</th>
      <th>Angabe auf dem Typenschild</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>1</td><td>Logo des Herstellers</td></tr>
    <tr><td>2</td><td>Teilenummer</td></tr>
    <tr><td>3</td><td>Maschinenmodell</td></tr>
    <tr><td>4</td><td>Leistung</td></tr>
    <tr><td>5</td><td>Versorgungsspannung</td></tr>
    <tr><td>6</td><td>Baujahr</td></tr>
    <tr><td>7</td><td>IP-Schutzart</td></tr>
    <tr><td>8</td><td>Seriennummer</td></tr>
  </tbody>
</table>

```{warning}
**ACHTUNG — CE-Typenschild**

Es ist strengstens verboten:
- das CE-Typenschild zu entfernen;
- es durch nicht autorisierte Schilder zu ersetzen.

Wird das Typenschild versehentlich beschädigt oder entfernt, ist der Kunde **verpflichtet**, den Hersteller unverzüglich zu informieren.
```

---

## EG-Konformitätserklärung (Kopie)

<div class="isw-ce-box">
  <div class="isw-ce-header">"CE" Declaration of Conformity</div>
  <p style="font-size:.88rem; margin:0 0 .6rem;"><strong>We:</strong> ARS S.r.l. – Via Aretina Nord, 157 – 52041 Pieve al Toppo (AR), Italia</p>
  <p style="font-size:.88rem; margin:0 0 .4rem;">Declare under our exclusive responsibility that the product:</p>
  <p style="font-size:.95rem; font-weight:700; color:#1a3a52; margin:0 0 .8rem;">BULK FEEDER &nbsp;1,5 lt / 3 lt / 5 lt / 10 lt / 20 lt / 40 lt</p>
  <p style="font-size:.88rem; margin:0 0 .4rem;">is compliant with the following standards and regulations:</p>
  <ul>
    <li>DLGS 17/2010</li>
    <li>2006/42/EC – <em>"Partly completed machinery"</em></li>
  </ul>
  <p style="font-size:.85rem; margin:0;">The machinery described above is intended to be incorporated into other machinery and must not be put into service until the relevant machinery into which it is to be incorporated has been declared in conformity with the essential health and safety requirements of Directive 2006/42/EC.</p>
  <div class="isw-ce-footer">
    <div><strong>Ort:</strong> Arezzo</div>
    <div><strong>Unterschrift:</strong> [Unterzeichnet]</div>
    <div><strong>Datum:</strong> 01-FEB-2019</div>
    <div><strong>Name:</strong> Marco Mazzini</div>
  </div>
</div>

---

## Bezugsrichtlinien

Die von ARS S.r.l. gelieferte Maschine fällt nicht unter die in **Anhang IV** der Maschinenrichtlinie aufgeführten Kategorien; es gilt daher das Konformitätsbewertungsverfahren mit **interner Fertigungskontrolle** (Anhang VIII).

Die technischen Unterlagen sind gemäß **Anhang VII** der Richtlinie 2006/42/EG erstellt und stehen den Aufsichtsbehörden auf begründetes Verlangen zur Verfügung.

Die Maschine wird in Verkehr gebracht mit:
- CE-Kennzeichnung
- EG-Konformitätserklärung
- Betriebsanleitung und Warnhinweise *(Punkt 1.7.4 der Maschinenrichtlinie 2006/42/EG)*

<table class="isw-table">
  <thead>
    <tr>
      <th>Richtlinie</th>
      <th>Beschreibung / Geltungsbereich</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="font-family:inherit; font-weight:700; color:#1a3a52; width:auto;">2006/42/EG</td>
      <td>Maschinenrichtlinie</td>
    </tr>
    <tr>
      <td style="font-family:inherit; font-weight:700; color:#1a3a52;">2014/30/EU</td>
      <td>EMV-Richtlinie (Elektromagnetische Verträglichkeit)</td>
    </tr>
  </tbody>
</table>

---

## Adressaten, Lieferung und Aufbewahrung

Das Handbuch richtet sich an die Bediener, die mit der Verwendung und Handhabung der Maschine in **allen Phasen ihrer technischen Lebensdauer** betraut sind. Das Handbuch ist zusammen mit der CE-Bescheinigung **fester Bestandteil der Maschine** und muss sie bei jedem Standortwechsel oder Weiterverkauf begleiten.

| Aspekt | Vorgabe |
|---|---|
| **Unversehrtheit** | Unversehrt aufbewahren. Bei Verlust unverzüglich eine Kopie beim Hersteller anfordern. |
| **Eigentümerwechsel** | Muss der Maschine bis zur Verschrottung folgen (Standortwechsel, Verkauf, Vermietung, Verpachtung). |
| **Format** | In elektronischem Format geliefert, mit Anlagen (Schaltpläne, Unterlieferanten-Handbücher). |
| **Anlagen** | Die beigefügten Handbücher sind fester Bestandteil; es gelten dieselben Vorgaben. |
| **Originalsprache** | Italienisch. Bei Abweichungen von den Übersetzungen ist der Originaltext maßgebend. |
| **Aktualisierungen** | Erfolgen durch den Hersteller. Der Anwender stellt sicher, dass nur aktualisierte Versionen verwendet werden. |

```{attention}
Die herstellende Firma lehnt jede Haftung für eine unsachgemäße Verwendung der Maschine und/oder für Schäden ab, die durch in der technischen Dokumentation nicht vorgesehene Arbeiten verursacht werden.
```

---

## Bedienerprofile und Qualifikationen

<div class="isw-profiles">

  <div class="isw-profile">
    <div class="isw-profile-header">
      <i class="ph ph-user" style="color:#2980b9;font-size:1.1rem;"></i>
      <span class="isw-profile-role">Bediener</span>
    </div>
    <div class="isw-profile-body">
      Personal des Anwenders, das geschult und befugt ist, die Maschine zu Produktionszwecken zu bedienen. Führt die für den ordnungsgemäßen Betrieb und die eigene Unversehrtheit erforderlichen Arbeiten aus. Verfügt über nachgewiesene Erfahrung und spezifische Ausbildung. Meldet bei Zweifeln Auffälligkeiten an den Vorgesetzten.
      <div class="isw-profile-note">⚠ Ist nicht befugt, Wartungsarbeiten jeglicher Art durchzuführen.</div>
    </div>
  </div>

  <div class="isw-profile">
    <div class="isw-profile-header">
      <i class="ph ph-wrench" style="color:#2980b9;font-size:1.1rem;"></i>
      <span class="isw-profile-role">Mechanischer Instandhalter</span>
    </div>
    <div class="isw-profile-body">
      Qualifizierter Techniker für vorbeugende/korrektive Arbeiten an mechanischen Teilen. Hat Zugang zu allen Teilen der Maschine für Sichtprüfung, Einstellung und Kalibrierung. Liest pneumatische/hydraulische Schaltpläne, technische Zeichnungen und Ersatzteillisten. In Ausnahmefällen kann er mit reduzierten Sicherheitseinrichtungen arbeiten.
      <div class="isw-profile-note">⚠ Ist nicht befähigt, an unter Spannung stehenden elektrischen Anlagen zu arbeiten.</div>
    </div>
  </div>

  <div class="isw-profile">
    <div class="isw-profile-header">
      <i class="ph ph-lightning" style="color:#2980b9;font-size:1.1rem;"></i>
      <span class="isw-profile-role">Elektrischer Instandhalter</span>
    </div>
    <div class="isw-profile-body">
      Qualifizierter Techniker für vorbeugende/korrektive Wartung der elektrischen Anlage. Liest die Schaltpläne und prüft die Funktionszyklen. Darf in den Schaltschränken unter Spannung arbeiten, <strong>nur wenn er über die PEI-Eignung (Norm EN 50110-1) verfügt</strong>.
      <div class="isw-profile-note">⚠ Führt keine Software-Programmierung (SPS oder Sicherheitslogik) durch und ändert keine Passwörter.</div>
    </div>
  </div>

  <div class="isw-profile">
    <div class="isw-profile-header">
      <i class="ph ph-code" style="color:#2980b9;font-size:1.1rem;"></i>
      <span class="isw-profile-role">Software-Fachtechniker</span>
    </div>
    <div class="isw-profile-body">
      Techniker des Herstellers mit nachgewiesener Erfahrung mit SPS-/PC-Systemen und Antrieben. Nimmt Änderungen an Maschinendaten vor, erstellt Arbeitsprogramme und stellt Antriebsparameter ein. Darf in den Schaltschränken nur unter Spannung arbeiten, wenn er <strong>PEI-geeignet ist (EN 50110-1)</strong>.
    </div>
  </div>

  <div class="isw-profile">
    <div class="isw-profile-header">
      <i class="ph ph-star" style="color:#2980b9;font-size:1.1rem;"></i>
      <span class="isw-profile-role">Techniker des Herstellers</span>
    </div>
    <div class="isw-profile-body">
      Spezialisierter und direkt von ARS S.r.l. (oder vom Händler) qualifizierter Techniker für hochkomplexe Arbeiten. Kennt den Bauablauf der Maschine im Detail und greift auf ausdrückliche Anforderung des Anwenders ein.
    </div>
  </div>

</div>

Alle oben genannten Qualifikationen fallen zwingend in die Kategorie **„Unterwiesene Person“**:

<div class="isw-trained-person">
  <div>
    <div class="isw-trained-person-title">Unterwiesene Person</div>
    Eine über die Arbeit und die Gefahren einer unsachgemäßen Verwendung informierte, unterwiesene und geschulte Person. Kennt die Bedeutung der Sicherheitseinrichtungen, die Unfallverhütungsvorschriften und die Betriebsbedingungen für sicheres Arbeiten.
  </div>
</div>

---

## Sicherheitssymbole

<div class="isw-symbol-grid">

  <div class="isw-symbol-item">
    <img src="../../../../../_shared/media/images/simbolo_avvertenza.png" alt="Warnhinweis">
    <div>
      <div class="isw-symbol-label">Allgemeiner Warnhinweis</div>
      <div class="isw-symbol-desc">Wesentliche Warnhinweise für die Sicherheit des Bedieners und/oder die Unversehrtheit der Maschine.</div>
    </div>
  </div>

  <div class="isw-symbol-item">
    <img src="../../../../../_shared/media/images/simbolo_elettrico.png" alt="Elektrische Gefahr">
    <div>
      <div class="isw-symbol-label">Elektrische Gefahr</div>
      <div class="isw-symbol-desc">Weist auf Gefahren und Risiken elektrischer Art hin (Vorhandensein von Spannung).</div>
    </div>
  </div>

  <div class="isw-symbol-item">
    <img src="../../../../../_shared/media/images/obbligo_info.png" alt="Wichtige Information">
    <div>
      <div class="isw-symbol-label">Wichtige Information</div>
      <div class="isw-symbol-desc">Informationen von besonderer Bedeutung für die Betriebsführung des Systems.</div>
    </div>
  </div>

</div>

<style>
.isw-symbol-grid {
  display: flex;
  flex-direction: column; /* Mette i tre blocchi uno sotto l'altro */
  gap: 24px;              /* Crea lo spazio vuoto tra un blocco e l'altro */
}

.isw-symbol-item {
  display: flex;          /* Allinea l'immagine e i testi affiancati dentro la riga */
  align-items: center;    /* Centra verticalmente l'immagine rispetto al testo (opzionale) */
  gap: 15px;              /* Crea spazio tra l'immagine e il testo */
}
</style>

---

## Technisches Glossar

<table class="isw-table">
  <thead>
    <tr>
      <th style="width:200px;">Begriff</th>
      <th>Technische Definition</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Lastaufnahmemittel</td><td>Nicht mit den Maschinen verbundene Bauteile, die das Aufnehmen der Last ermöglichen und zwischen der Maschine und der Last angeordnet sind (einschließlich Anschlagmittel und deren Bauteile).</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Ausfall</td><td>Störung, die den normalen Betrieb einer Maschine oder Anlage verhindert.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Ketten, Seile oder Gurte</td><td>Für das Heben konstruierte Elemente als fester Bestandteil von Maschinen oder Lastaufnahmemitteln.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Schaden</td><td>Jede negative Folge, die sich aus dem Eintreten eines gefährlichen Ereignisses ergibt.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">PSA</td><td>Persönliche Schutzausrüstung: Produkte, die dazu bestimmt sind, die Gesundheit und Sicherheit der Arbeitnehmer zu schützen, die sie tragen.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Maschine</td><td>Gesamtheit, ausgestattet mit einem Antriebssystem, bestehend aus Teilen (von denen mindestens eines beweglich ist), die für eine bestimmte Anwendung verbunden sind.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Fehlfunktion</td><td>Fehlerhaftes oder unzureichendes Funktionieren einer Maschine oder eines ihrer Elemente.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Gefährdung</td><td>Potenzielle Schadensquelle, die, wenn sie nicht vermieden wird, ein Risiko für Sicherheit und Gesundheit darstellt.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Schutz</td><td>Abwehr dessen, was Schaden verursachen kann. Möglich ist ein <strong>Aktiver Schutz</strong> (vom Bediener betätigt) oder ein <strong>Passiver Schutz</strong> (greift ohne menschliches Zutun ein).</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Schutzeinrichtung</td><td>Physische Barriere, die als struktureller Teil der Maschine konstruiert ist, um Schutz zu bieten.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Risiko</td><td>Kombination aus der Wahrscheinlichkeit und dem Schweregrad einer Verletzung oder Gesundheitsschädigung in einer Gefahrensituation.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Restrisiko</td><td>Risiko, das nach den in der Konstruktionsphase getroffenen Schutz- und Vorbeugemaßnahmen verbleibt.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Bestimmungsgemäße Verwendung</td><td>Verwendung der Maschine in Übereinstimmung mit den in der Betriebsanleitung enthaltenen Informationen.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Vorhersehbare Fehlanwendung</td><td>Vom Konstrukteur nicht vorgesehene Verwendung, die sich aus leicht vorhersehbarem menschlichem Verhalten ergibt.</td></tr>
  </tbody>
</table>

---

## Vorgeschriebene persönliche Schutzausrüstung (PSA)

In der Nähe der Maschine (Montage, Wartung, Einstellung) ist die folgende PSA zu verwenden:

<div class="isw-symbol-grid">
  <div class="isw-symbol-item">
    <img src="../../../../../_shared/media/images/obbligo_guanti.png" alt="Schutzhandschuhe">
    <div>
      <div class="isw-symbol-label">Schutzhandschuhe</div>
      <div class="isw-symbol-desc">Zum Schutz der Hände sind Schutz- oder Isolierhandschuhe zu tragen.</div>
    </div>
  </div>
  <div class="isw-symbol-item">
    <img src="../../../../../_shared/media/images/obbligo_occhiali.png" alt="Schutzbrille">
    <div>
      <div class="isw-symbol-label">Schutzbrille</div>
      <div class="isw-symbol-desc">Zum Schutz der Augen ist eine Schutzbrille zu tragen.</div>
    </div>
  </div>
  <div class="isw-symbol-item">
    <img src="../../../../../_shared/media/images/obbligo_antiinf.png" alt="Sicherheitsschuhe">
    <div>
      <div class="isw-symbol-label">Sicherheitsschuhe</div>
      <div class="isw-symbol-desc">Zum Schutz der Füße sind Sicherheitsschuhe zu tragen.</div>
    </div>
  </div>
  <div class="isw-symbol-item">
    <img src="../../../../../_shared/media/images/obbligo_rumore.png" alt="Gehörschutz">
    <div>
      <div class="isw-symbol-label">Gehörschutz</div>
      <div class="isw-symbol-desc">Zum Schutz des Gehörs sind Kapselgehörschützer oder Ohrstöpsel zu tragen.</div>
    </div>
  </div>
  <div class="isw-symbol-item">
    <img src="../../../../../_shared/media/images/obbligo_indumenti.png" alt="Schutzkleidung">
    <div>
      <div class="isw-symbol-label">Schutzkleidung</div>
      <div class="isw-symbol-desc">Die vorgeschriebene Arbeitsschutzkleidung ist zu tragen.</div>
    </div>
  </div>
  <div class="isw-symbol-item">
    <img src="../../../../../_shared/media/images/obbligo_manuale.png" alt="Handbuch beachten">
    <div>
      <div class="isw-symbol-label">Handbuch beachten</div>
      <div class="isw-symbol-desc">Die Betriebsanleitung ist vor jeder Tätigkeit zu lesen und zu verstehen.</div>
    </div>
  </div>
  <div class="isw-symbol-item">
    <img src="../../../../../_shared/media/images/obbligo_casco.png" alt="Schutzhelm">
    <div>
      <div class="isw-symbol-label">Schutzhelm</div>
      <div class="isw-symbol-desc">Zum Schutz des Kopfes ist ein Helm zu tragen.</div>
    </div>
  </div>
</div>

```{warning}
**SICHERHEITSKLEIDUNG**

Die Kleidung des Personals muss den grundlegenden Anforderungen der **EU-Verordnung 2016/425** und den im Installationsland geltenden Gesetzen entsprechen. Die Nichteinhaltung kann die Sicherheit des Bedieners und der exponierten Personen gefährden.
```

---

## Kartierung der Sicherheitsbereiche

<div class="isw-zones">
  <div class="isw-zone">
    <div class="isw-zone-label">Bedienbereiche</div>
    <div class="isw-zone-desc">Bereiche, in denen der Bediener die zyklischen Funktionen (im Automatik- oder Halbautomatikbetrieb) über die dafür vorgesehenen Bedienfelder überwacht.</div>
  </div>
  <div class="isw-zone">
    <div class="isw-zone-label">Wartungs-/Einstellbereiche</div>
    <div class="isw-zone-desc">Nur für qualifizierte mechanische und elektrische Instandhalter für Einrichtarbeiten zugänglich. Während des normalen Produktionszyklus bleiben sie gesperrt.</div>
  </div>
  <div class="isw-zone">
    <div class="isw-zone-label">Gefahrenbereiche</div>
    <div class="isw-zone-desc">Bereiche im Inneren oder am Umfang der Maschine mit Restrisiken. <strong>Der Zutritt ist für jedermann strengstens verboten, solange die Maschine in Betrieb ist.</strong></div>
  </div>
</div>

```{warning}
**ZUGANG ZU GEFAHRENBEREICHEN**

Die Risiken in den Maschinenbereichen werden durch physische Schutzeinrichtungen (Verkleidungen, Türen) und verriegelte elektrische Einrichtungen (Sensoren, Mikroschalter) abgesichert.

Bei aktivem System ist es strengstens verboten:
- die Schutzeinrichtungen zu übersteigen;
- die Sicherheitseinrichtungen zu überbrücken;
- im Inneren der geschützten Bereiche einzugreifen.

Das Entfernen oder Umgehen der Sicherheitssysteme kann zu schweren Verletzungen von Personen und zu Schäden an der Maschine führen.
```

---

## Garantiebedingungen und -grenzen

Die vollständigen Klauseln sind im Kaufvertrag festgelegt, dessen Bedingungen stets Vorrang vor diesem Handbuch haben.

<div class="isw-warranty-grid">
  <div class="isw-warranty-col valid">
    <div class="isw-warranty-col-header">✔ Gültigkeitsbedingungen</div>
    <ul>
      <li>Verpackungen mit geeigneten Mitteln und ohne Schäden an den Systemen geöffnet.</li>
      <li>Installation und Inbetriebnahme in Anwesenheit befugter Techniker durchgeführt.</li>
      <li>Einsatz innerhalb der im Vertrag angegebenen Nennwerte.</li>
      <li>Wartung innerhalb der festgelegten Fristen mit <strong>Original-Ersatzteilen von ARS S.r.l.</strong> durch qualifiziertes Personal.</li>
    </ul>
  </div>
  <div class="isw-warranty-col invalid">
    <div class="isw-warranty-col-header">✘ Gründe für das sofortige Erlöschen</div>
    <ul>
      <li>Nichtbeachtung der Sicherheitsvorschriften oder Anweisungen.</li>
      <li>Installation oder Einsatz in ungeeigneten Umgebungen.</li>
      <li>Entfernen oder Manipulieren von Kontroll- und Sicherheitseinrichtungen.</li>
      <li>Entfernen oder Verändern des CE-Schilds oder der Piktogramme.</li>
      <li>Nicht autorisierte Änderungen an der Software (SPS, Logiken, Passwörter).</li>
      <li>Unsachgemäße Verwendung oder Überlassen an nicht autorisiertes Personal.</li>
      <li>Mechanische/elektrische/pneumatische Änderungen ohne schriftliche Genehmigung des Herstellers.</li>
      <li>Unregelmäßigkeiten bei der Energieversorgung.</li>
      <li>Nichtdurchführung des planmäßigen Wartungsplans.</li>
      <li>Endgültige Entsorgung unter Verstoß gegen die geltenden Umweltvorschriften.</li>
    </ul>
  </div>
</div>

---

## Sicherheitsmerkmale

<div class="isw-safety-cards">

  <div class="isw-safety-card">
    <div class="isw-safety-card-title"><i class="ph ph-speaker-high"></i> Lärm</div>
    <p>Messungen gemäß UNI EN 11200 und UNI EN ISO 3746 durchgeführt. Die Lärmbelastung im Betrieb beträgt <strong>90 dB</strong>. Der tatsächliche Pegel vor Ort kann je nach Art der Installation, benachbarten Maschinen und den Eigenschaften der Umgebung abweichen.</p>
  </div>

  <div class="isw-safety-card">
    <div class="isw-safety-card-title"><i class="ph ph-wave-sine"></i> Vibrationen</div>
    <p>Die von der Maschine unter normalen Betriebsbedingungen erzeugten Vibrationen sind für die Gesundheit der Bediener nicht gefährlich. Übermäßige Vibrationen sind ein Anzeichen für einen mechanischen Defekt und müssen unverzüglich gemeldet und beseitigt werden.</p>
  </div>

  <div class="isw-safety-card">
    <div class="isw-safety-card-title"><i class="ph ph-broadcast"></i> Elektromagnetische Verträglichkeit</div>
    <p>Die Maschine entspricht der EMV-Richtlinie. Die Emissionswerte liegen dank des Einsatzes zertifizierter Bauteile, geeigneter Anschlüsse und, wo nötig, Filter innerhalb der normativen Grenzwerte. Nicht konforme Wartungsarbeiten oder der fehlerhafte Austausch von Bauteilen können diese Konformität beeinträchtigen.</p>
  </div>

</div>

<style>
.isw-safety-cards {
  display: flex;
  flex-direction: column; 
  gap: 20px;              
}
</style>

```{attention}
**PFLICHT** — Während des Betriebs der Maschine ist persönliche Schutzausrüstung zu verwenden.
```

### Restrisiken

Die Maschine wurde so konstruiert, dass die grundlegenden Sicherheitsanforderungen erfüllt sind; dennoch verbleiben Restrisiken in den Phasen:
- Transport und Installation
- Normalbetrieb
- Einstellung und Feinabstimmung
- Wartung und Reinigung
- Demontage und Außerbetriebnahme

<div class="isw-risks">

  <div class="isw-risk">
    <div class="isw-risk-icons">
      <img src="../../../../../_shared/media/images/simbolo_avvertenza.png" alt="">
      <img src="../../../../../_shared/media/images/pericolo_movimento.png" alt="">
      <img src="../../../../../_shared/media/images/pericolo_spazi.png" alt="">
    </div>
    <div class="isw-risk-body">
      <div class="isw-risk-title">Gefahren durch Handhabung</div>
      <div class="isw-risk-desc">
        Das Abladen, das Öffnen der Verpackungen und die Handhabung der Maschine setzen die Bediener dem Risiko von <strong>schwebenden Lasten und Quetschungen</strong> aus. Sie dürfen ausschließlich von Personal durchgeführt werden, das auf die Bedienung von Hebemitteln spezialisiert und eigens geschult ist.
        <br><br>Die detaillierten Verfahren sind im Kapitel <em>„Transport und Installation“</em>.
      </div>
    </div>
  </div>

  <div class="isw-risk">
    <div class="isw-risk-icons">
      <img src="../../../../../_shared/media/images/simbolo_avvertenza.png" alt="">
      <img src="../../../../../_shared/media/images/simbolo_elettrico.png" alt="">
    </div>
    <div class="isw-risk-body">
      <div class="isw-risk-title">Elektrische Gefahr</div>
      <div class="isw-risk-desc">
        Zugangs- und Wartungsarbeiten setzen das Personal elektrischen Risiken aus. Arbeiten unter Spannung dürfen ausschließlich von erfahrenem und qualifiziertem Personal durchgeführt werden. Sicherheitsmaßnahmen:
        <ul>
          <li>Beachten Sie die Sicherheitspiktogramme zum elektrischen Risiko.</li>
          <li>Führen Sie keine Wartung durch, ohne zuvor die Energieversorgung getrennt zu haben.</li>
          <li>Konsultieren Sie die Handbücher der Handelsgeräte für spezifische Empfehlungen.</li>
          <li>Prüfen Sie den Potentialausgleichskreis regelmäßig.</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="isw-risk">
    <div class="isw-risk-icons">
      <img src="../../../../../_shared/media/images/simbolo_avvertenza.png" alt="">
    </div>
    <div class="isw-risk-body">
      <div class="isw-risk-title">Gefahr durch Staub und Splitter</div>
      <div class="isw-risk-desc">
        Am Ende des Arbeitszyklus können Rückstände der zugeführten Teile oder Staubansammlungen auf der Oberfläche der Maschine verbleiben. Reinigen Sie die Vibrationsfläche nach jeder Verwendung gründlich (siehe Kap. 7).
      </div>
    </div>
  </div>

</div>

```{attention}
Führen Sie keine Wartungs- und Reinigungsarbeiten durch, ohne zuvor alle vorhandenen Energiequellen spannungsfrei geschaltet zu haben.
```

```{attention}
Es ist strengstens verboten, die Schutzeinrichtungen zu entfernen oder die feststehenden Schutzeinrichtungen zu öffnen, ohne zuvor die elektrische und pneumatische Energieversorgung der Maschine getrennt zu haben.
```

Der Anwender ist verpflichtet:
- die Handhabungs- und Installationsrisiken in den eigenen Räumlichkeiten zu analysieren;
- das mit den Arbeiten betraute Personal zu sensibilisieren und zu unterweisen;
- visuelle Sicherheitskennzeichnungen im Arbeitsbereich anzubringen.

</div>