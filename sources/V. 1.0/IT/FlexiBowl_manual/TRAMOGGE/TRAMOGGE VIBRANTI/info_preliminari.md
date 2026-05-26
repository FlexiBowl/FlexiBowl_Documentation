
# **Informazioni Preliminari Generali**

```{important}
Prima di installare, utilizzare o effettuare manutenzione sulla macchina, leggere attentamente l'intero manuale e tutta la documentazione allegata.

Il mancato rispetto delle istruzioni riportate può causare:
- danni alla macchina;
- perdita delle condizioni di sicurezza;
- rischi per operatori e manutentori;
- decadenza della garanzia.
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

## Identificazione

<div class="isw-meta-grid">
  <div class="isw-meta-card">
    <div class="isw-meta-title"><i class="ph ph-factory"></i> Costruttore</div>
    <div class="isw-meta-content">
      <strong>ARS S.r.l.</strong><br>
      Via Aretina Nord, 157<br>
      52041 – Pieve al Toppo (AR), Italia<br>
      Tel. +39 0575 398611 &nbsp;·&nbsp; Fax +39 0575 398620<br>
      <a href="mailto:info@arsautomation.com">info@arsautomation.com</a><br>
      <a href="https://www.arsautomation.com" target="_blank">www.arsautomation.com</a>
    </div>
  </div>
  <div class="isw-meta-card">
    <div class="isw-meta-title"><i class="ph ph-cpu"></i> Identificazione Macchina</div>
    <div class="isw-meta-content">
      <strong>Macchina:</strong> Tramoggia<br>
      <strong>Modelli base:</strong>
      <div class="isw-model-badges">
        <span class="isw-badge">1,5 lt</span>
        <span class="isw-badge">3 lt</span>
        <span class="isw-badge">5 lt</span>
        <span class="isw-badge">10 lt</span>
        <span class="isw-badge">20 lt</span>
        <span class="isw-badge">40 lt</span>
      </div>
      <small>In alcune applicazioni possono esistere modelli personalizzati. L'identificazione è definita dal progetto di riferimento.</small>
    </div>
  </div>
</div>

### Targa di Identificazione

La macchina è dotata di una targa di identificazione posizionata sulla **base vibrante**. Gli estremi riportati sulla targhetta devono essere citati in ogni comunicazione con ARS S.r.l.

![Etichetta Tramoggia](../../../../../_shared/media/images/etichetta_tramoggia.jpg)

<table class="isw-table">
  <thead>
    <tr>
      <th>Pos.</th>
      <th>Elemento sulla targa</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>1</td><td>Logo Costruttore</td></tr>
    <tr><td>2</td><td>N° parte</td></tr>
    <tr><td>3</td><td>Modello Macchina</td></tr>
    <tr><td>4</td><td>Potenza</td></tr>
    <tr><td>5</td><td>Tensione di Alimentazione</td></tr>
    <tr><td>6</td><td>Anno di Costruzione</td></tr>
    <tr><td>7</td><td>Grado di protezione IP</td></tr>
    <tr><td>8</td><td>N° matricola</td></tr>
  </tbody>
</table>

```{warning}
**ATTENZIONE — Targa identificativa CE**

È assolutamente vietato:
- asportare la targa identificativa CE;
- sostituirla con targhe non autorizzate.

Se la targa venisse danneggiata o rimossa per cause accidentali, il cliente è **obbligato** a informare immediatamente il Costruttore.
```

---

## Dichiarazione di Conformità CE (Copia)

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
    <div><strong>Luogo:</strong> Arezzo</div>
    <div><strong>Firma:</strong> [Firmato]</div>
    <div><strong>Data:</strong> 01-FEB-2019</div>
    <div><strong>Nome:</strong> Marco Mazzini</div>
  </div>
</div>

---

## Direttive di Riferimento

La macchina fornita da ARS S.r.l. non rientra nelle categorie elencate nell'**Allegato IV** della Direttiva Macchine; si applica pertanto la procedura di valutazione della conformità con **controllo interno sulla fabbricazione** (Allegato VIII).

Il fascicolo tecnico di costruzione è redatto secondo l'**Allegato VII** della Direttiva 2006/42/CE ed è disponibile agli organi di vigilanza su richiesta motivata.

La macchina è immessa sul mercato corredata di:
- Marcatura CE
- Dichiarazione CE di Conformità
- Manuale di istruzioni e avvertenze *(punto 1.7.4 della Direttiva Macchine 2006/42/CE)*

<table class="isw-table">
  <thead>
    <tr>
      <th>Direttiva</th>
      <th>Descrizione / Ambito</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="font-family:inherit; font-weight:700; color:#1a3a52; width:auto;">2006/42/CE</td>
      <td>Direttiva Macchine</td>
    </tr>
    <tr>
      <td style="font-family:inherit; font-weight:700; color:#1a3a52;">2014/30/UE</td>
      <td>Direttiva per la Compatibilità Elettromagnetica</td>
    </tr>
  </tbody>
</table>

---

## Destinatari, Fornitura e Conservazione

Il manuale è destinato agli operatori incaricati di utilizzare e gestire la macchina in **tutte le fasi della sua vita tecnica**. Il manuale, unitamente al certificato CE, è **parte integrante della macchina** e deve accompagnarla in ogni spostamento o rivendita.

| Aspetto | Prescrizione |
|---|---|
| **Integrità** | Conservare integro. In caso di smarrimento, richiedere copia immediata al Costruttore. |
| **Passaggi di proprietà** | Deve seguire la macchina fino alla demolizione (spostamenti, vendita, noleggio, affitto). |
| **Formato** | Fornito in formato elettronico, con allegati (schemi elettrici, manuali sub-fornitori). |
| **Allegati** | I manuali allegati sono parte costitutiva; si applicano le medesime prescrizioni. |
| **Lingua originale** | Italiano. In caso di incongruenze con le traduzioni, fa fede il testo originale. |
| **Aggiornamenti** | A cura del Costruttore. L'utilizzatore garantisce che solo le versioni aggiornate siano in uso. |

```{attention}
La Ditta Costruttrice declina ogni responsabilità per uso improprio della macchina e/o per danni causati da operazioni non contemplate nella documentazione tecnica.
```

---

## Profili degli Operatori e Qualifiche

<div class="isw-profiles">

  <div class="isw-profile">
    <div class="isw-profile-header">
      <i class="ph ph-user" style="color:#2980b9;font-size:1.1rem;"></i>
      <span class="isw-profile-role">Operatore</span>
    </div>
    <div class="isw-profile-body">
      Personale dell'utilizzatore addestrato e abilitato alla conduzione della macchina ai fini produttivi. Esegue le operazioni necessarie al buon funzionamento e alla propria incolumità. Ha comprovata esperienza e formazione specifica. In caso di dubbi, segnala le anomalie al superiore.
      <div class="isw-profile-note">⚠ Non è autorizzato ad effettuare alcuna attività di manutenzione.</div>
    </div>
  </div>

  <div class="isw-profile">
    <div class="isw-profile-header">
      <i class="ph ph-wrench" style="color:#2980b9;font-size:1.1rem;"></i>
      <span class="isw-profile-role">Manutentore Meccanico</span>
    </div>
    <div class="isw-profile-body">
      Tecnico qualificato per attività preventiva/correttiva su parti meccaniche. Accede a tutte le parti della macchina per analisi visiva, regolazione e taratura. Legge schemi pneumatici/oleodinamici, disegni tecnici e liste ricambi. In casi straordinari può operare con sicurezze ridotte.
      <div class="isw-profile-note">⚠ Non è abilitato ad intervenire su impianti elettrici sotto tensione.</div>
    </div>
  </div>

  <div class="isw-profile">
    <div class="isw-profile-header">
      <i class="ph ph-lightning" style="color:#2980b9;font-size:1.1rem;"></i>
      <span class="isw-profile-role">Manutentore Elettrico</span>
    </div>
    <div class="isw-profile-body">
      Tecnico qualificato per manutenzione preventiva/correttiva sull'impianto elettrico. Legge gli schemi elettrici e verifica i cicli funzionali. Può operare sotto tensione nei quadri elettrici <strong>solo se in possesso di idoneità PEI (Normativa EN 50110-1)</strong>.
      <div class="isw-profile-note">⚠ Non esegue programmazione software (PLC o logiche di sicurezza) e non modifica le password.</div>
    </div>
  </div>

  <div class="isw-profile">
    <div class="isw-profile-header">
      <i class="ph ph-code" style="color:#2980b9;font-size:1.1rem;"></i>
      <span class="isw-profile-role">Tecnico Esperto Software</span>
    </div>
    <div class="isw-profile-body">
      Tecnico del Costruttore con comprovata esperienza su sistemi PLC/PC e azionamenti. Esegue modifiche ai dati macchina, creazione di programmi di lavoro e regolazione dei parametri drive. Può operare nei quadri elettrici sotto tensione solo se <strong>soggetto idoneo PEI (EN 50110-1)</strong>.
    </div>
  </div>

  <div class="isw-profile">
    <div class="isw-profile-header">
      <i class="ph ph-star" style="color:#2980b9;font-size:1.1rem;"></i>
      <span class="isw-profile-role">Tecnico del Costruttore</span>
    </div>
    <div class="isw-profile-body">
      Tecnico specializzato e qualificato direttamente da ARS S.r.l. (o dal distributore) per operazioni ad elevata complessità. Conosce nel dettaglio il ciclo costruttivo della macchina e interviene su richiesta specifica dell'utilizzatore.
    </div>
  </div>

</div>

Tutte le qualifiche sopra rientrano obbligatoriamente nella categoria di **"Persona Addestrata"**:

<div class="isw-trained-person">
  <div>
    <div class="isw-trained-person-title">Persona Addestrata</div>
    Soggetto informato, istruito ed addestrato sul lavoro e sui pericoli derivanti da un uso improprio. Conosce l'importanza dei dispositivi di sicurezza, le norme antinfortunistiche e le condizioni operative per il lavoro in sicurezza.
  </div>
</div>

---

## Simbologia di Sicurezza

<div class="isw-symbol-grid">

  <div class="isw-symbol-item">
    <img src="../../../../../_shared/media/images/simbolo_avvertenza.png" alt="Avvertenza">
    <div>
      <div class="isw-symbol-label">Avvertenza generale</div>
      <div class="isw-symbol-desc">Avvertenze cruciali per la sicurezza dell'operatore e/o per l'integrità della macchina.</div>
    </div>
  </div>

  <div class="isw-symbol-item">
    <img src="../../../../../_shared/media/images/simbolo_elettrico.png" alt="Pericolo elettrico">
    <div>
      <div class="isw-symbol-label">Pericolo elettrico</div>
      <div class="isw-symbol-desc">Segnala pericoli e rischi di natura elettrica (presenza di tensione).</div>
    </div>
  </div>

  <div class="isw-symbol-item">
    <img src="../../../../../_shared/media/images/obbligo_info.png" alt="Informazione importante">
    <div>
      <div class="isw-symbol-label">Informazione importante</div>
      <div class="isw-symbol-desc">Informazioni di particolare importanza relative alla gestione operativa del sistema.</div>
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

## Glossario Tecnico

<table class="isw-table">
  <thead>
    <tr>
      <th style="width:200px;">Termine</th>
      <th>Definizione Tecnica</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Accessori di sollevamento</td><td>Componenti non collegati alle macchine che consentono la presa del carico, disposti tra la macchina e il carico (incluse imbracature e loro componenti).</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Avaria</td><td>Guasto che impedisce il normale funzionamento di un macchinario o di un impianto.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Catene, funi o cinghie</td><td>Elementi progettati per il sollevamento come parte integrante di macchine o accessori di sollevamento.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Danno</td><td>Qualunque conseguenza negativa derivante dal verificarsi di un evento pericoloso.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">D.P.I.</td><td>Dispositivo di Protezione Individuale: prodotti atti a salvaguardare la salute e la sicurezza dei lavoratori che li indossano.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Macchina</td><td>Insieme equipaggiato di un sistema di azionamento composto di parti (di cui almeno una mobile), collegate per un'applicazione determinata.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Malfunzionamento</td><td>Funzionamento difettoso o inadeguato di una macchina o di un suo elemento.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Pericolo</td><td>Potenziale sorgente di danno che, se non evitato, comporta un rischio per la sicurezza e la salute.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Protezione</td><td>Difesa contro ciò che può causare danno. Può essere <strong>Attiva</strong> (azionata dall'operatore) o <strong>Passiva</strong> (interviene senza comando umano).</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Riparo</td><td>Barriera fisica, progettata come parte strutturale della macchina, per fornire protezione.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Rischio</td><td>Combinazione della probabilità e della gravità di una lesione o di un danno in una situazione pericolosa.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Rischio residuo</td><td>Rischio che permane dopo l'adozione delle misure di protezione e prevenzione in fase di progetto.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Uso previsto</td><td>Uso della macchina in conformità alle informazioni fornite nelle istruzioni d'uso.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Uso scorretto prevedibile</td><td>Uso non previsto dal progettista, derivante da un comportamento umano facilmente prevedibile.</td></tr>
  </tbody>
</table>

---

## Dispositivi di Protezione Individuale (D.P.I.) Obbligatori

Nelle fasi di prossimità alla macchina (montaggio, manutenzione, regolazione) è obbligatorio impiegare i seguenti DPI:

<div class="isw-symbol-grid">
  <div class="isw-symbol-item">
    <img src="../../../../../_shared/media/images/obbligo_guanti.png" alt="Guanti protettivi">
    <div>
      <div class="isw-symbol-label">Guanti protettivi</div>
      <div class="isw-symbol-desc">Obbligo di indossare guanti protettivi o isolanti a protezione delle mani.</div>
    </div>
  </div>
  <div class="isw-symbol-item">
    <img src="../../../../../_shared/media/images/obbligo_occhiali.png" alt="Occhiali di protezione">
    <div>
      <div class="isw-symbol-label">Occhiali di protezione</div>
      <div class="isw-symbol-desc">Obbligo di indossare occhiali protettivi per la salvaguardia degli occhi.</div>
    </div>
  </div>
  <div class="isw-symbol-item">
    <img src="../../../../../_shared/media/images/obbligo_antiinf.png" alt="Scarpe antinfortunistiche">
    <div>
      <div class="isw-symbol-label">Scarpe antinfortunistiche</div>
      <div class="isw-symbol-desc">Obbligo di calzare scarpe antinfortunistiche per la protezione dei piedi.</div>
    </div>
  </div>
  <div class="isw-symbol-item">
    <img src="../../../../../_shared/media/images/obbligo_rumore.png" alt="Protezione dal rumore">
    <div>
      <div class="isw-symbol-label">Protezione dal rumore</div>
      <div class="isw-symbol-desc">Obbligo di indossare cuffie o tappi auricolari per la protezione dell'udito.</div>
    </div>
  </div>
  <div class="isw-symbol-item">
    <img src="../../../../../_shared/media/images/obbligo_indumenti.png" alt="Indumenti protettivi">
    <div>
      <div class="isw-symbol-label">Indumenti protettivi</div>
      <div class="isw-symbol-desc">Obbligo di indossare gli specifici indumenti di lavoro protettivi.</div>
    </div>
  </div>
  <div class="isw-symbol-item">
    <img src="../../../../../_shared/media/images/obbligo_manuale.png" alt="Consultazione manuale">
    <div>
      <div class="isw-symbol-label">Consultazione Manuale</div>
      <div class="isw-symbol-desc">Obbligo di leggere e comprendere le istruzioni d'uso prima di qualsiasi attività.</div>
    </div>
  </div>
  <div class="isw-symbol-item">
    <img src="../../../../../_shared/media/images/obbligo_casco.png" alt="Casco di protezione">
    <div>
      <div class="isw-symbol-label">Casco di protezione</div>
      <div class="isw-symbol-desc">Obbligo di indossare il casco a protezione del capo.</div>
    </div>
  </div>
</div>

```{warning}
**ABBIGLIAMENTO DI SICUREZZA**

L'abbigliamento del personale deve essere conforme ai requisiti essenziali previsti dal **Regolamento UE 2016/425** e alle leggi vigenti nel Paese di installazione. Il mancato rispetto può compromettere la sicurezza dell'operatore e delle persone esposte.
```

---

## Mappatura delle Aree di Sicurezza

<div class="isw-zones">
  <div class="isw-zone">
    <div class="isw-zone-label">Zone di comando</div>
    <div class="isw-zone-desc">Aree in cui l'operatore esegue il controllo delle funzioni cicliche (in modalità automatica o semiautomatica), tramite i pannelli dedicati.</div>
  </div>
  <div class="isw-zone">
    <div class="isw-zone-label">Zone di manutenzione / regolazione</div>
    <div class="isw-zone-desc">Accessibili solo a manutentori meccanici ed elettrici qualificati per operazioni di settaggio. Rimangono interdette durante il ciclo produttivo standard.</div>
  </div>
  <div class="isw-zone">
    <div class="isw-zone-label">Zone pericolose</div>
    <div class="isw-zone-desc">Aree interne o perimetrali alla macchina con rischi residui. <strong>È categoricamente vietato l'accesso a chiunque quando la macchina è in funzione.</strong></div>
  </div>
</div>

```{warning}
**ACCESSO A ZONE PERICOLOSE**

I rischi nelle zone della macchina sono protetti tramite ripari fisici (carter, portelli) e dispositivi elettrici interbloccati (sensori, microinterruttori).

Quando il sistema è attivo è severamente vietato:
- scavalcare le protezioni;
- bypassare i dispositivi di sicurezza;
- intervenire all'interno delle aree protette.

La rimozione o l'elusione dei sistemi di sicurezza può causare gravi lesioni alle persone e danni alla macchina.
```

---

## Condizioni e Limiti della Garanzia

Le clausole complete sono stabilite nel contratto di vendita, le cui condizioni hanno sempre la priorità rispetto a questo manuale.

<div class="isw-warranty-grid">
  <div class="isw-warranty-col valid">
    <div class="isw-warranty-col-header">✔ Condizioni di validità</div>
    <ul>
      <li>Apertura imballi eseguita con mezzi idonei senza danni ai sistemi.</li>
      <li>Installazione e avviamento eseguiti alla presenza di tecnici abilitati.</li>
      <li>Utilizzo entro i limiti nominali dichiarati nel contratto.</li>
      <li>Manutenzione nei tempi prestabiliti con <strong>ricambi originali ARS S.r.l.</strong> affidati a personale qualificato.</li>
    </ul>
  </div>
  <div class="isw-warranty-col invalid">
    <div class="isw-warranty-col-header">✘ Cause di decadenza immediata</div>
    <ul>
      <li>Mancato rispetto delle norme di sicurezza o delle istruzioni.</li>
      <li>Installazione o impiego in ambienti non idonei.</li>
      <li>Rimozione o manomissione di dispositivi di controllo e sicurezza.</li>
      <li>Rimozione o alterazione della targa CE o dei pittogrammi.</li>
      <li>Modifiche non autorizzate al software (PLC, logiche, password).</li>
      <li>Uso improprio o affidamento a personale non autorizzato.</li>
      <li>Modifiche meccaniche/elettriche/pneumatiche senza autorizzazione scritta del Costruttore.</li>
      <li>Anomalie nell'erogazione dell'energia di alimentazione.</li>
      <li>Mancata attuazione del piano di manutenzione programmata.</li>
      <li>Smaltimento finale in violazione delle norme ambientali vigenti.</li>
    </ul>
  </div>
</div>

---

## Sicurezze

<div class="isw-safety-cards">

  <div class="isw-safety-card">
    <div class="isw-safety-card-title"><i class="ph ph-speaker-high"></i> Rumore</div>
    <p>Misurazioni eseguite secondo UNI EN 11200 e UNI EN ISO 3746. L'esposizione al rumore durante il funzionamento è pari a <strong>90 dB</strong>. Il livello effettivo in sito può variare in funzione del tipo di installazione, delle macchine adiacenti e delle caratteristiche dell'ambiente.</p>
  </div>

  <div class="isw-safety-card">
    <div class="isw-safety-card-title"><i class="ph ph-wave-sine"></i> Vibrazioni</div>
    <p>Le vibrazioni prodotte dalla macchina in normali condizioni di esercizio non sono pericolose per la salute degli operatori. Una vibrazione eccessiva è sintomo di guasto meccanico e deve essere segnalata ed eliminata immediatamente.</p>
  </div>

  <div class="isw-safety-card">
    <div class="isw-safety-card-title"><i class="ph ph-broadcast"></i> Compatibilità Elettromagnetica</div>
    <p>La macchina è conforme alla Direttiva EMC. I valori di emissione rientrano nei limiti normativi grazie all'impiego di componenti certificati, collegamenti idonei e filtri dove necessario. Interventi manutentivi non conformi o sostituzioni errate di componenti possono compromettere tale conformità.</p>
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
**OBBLIGO** — È obbligatorio utilizzare i dispositivi di protezione individuale durante il funzionamento della macchina.
```

### Rischi Residui

La progettazione della macchina è stata eseguita per garantire i requisiti essenziali di sicurezza; tuttavia, permangono rischi residui nelle fasi di:
- trasporto e installazione
- funzionamento normale
- regolazione e messa a punto
- manutenzione e pulizia
- smontaggio e smantellamento

<div class="isw-risks">

  <div class="isw-risk">
    <div class="isw-risk-icons">
      <img src="../../../../../_shared/media/images/simbolo_avvertenza.png" alt="">
      <img src="../../../../../_shared/media/images/pericolo_movimento.png" alt="">
      <img src="../../../../../_shared/media/images/pericolo_spazi.png" alt="">
    </div>
    <div class="isw-risk-body">
      <div class="isw-risk-title">Pericoli dovuti alla movimentazione</div>
      <div class="isw-risk-desc">
        Le operazioni di scarico, apertura degli imballi e movimentazione della macchina espongono agli operatori al rischio di <strong>carichi sospesi e schiacciamento</strong>. Devono essere svolte esclusivamente da personale specializzato nella conduzione di mezzi di sollevamento e appositamente addestrato.
        <br><br>Le procedure dettagliate sono descritte nel capitolo <em>"Trasporto e installazione"</em>.
      </div>
    </div>
  </div>

  <div class="isw-risk">
    <div class="isw-risk-icons">
      <img src="../../../../../_shared/media/images/simbolo_avvertenza.png" alt="">
      <img src="../../../../../_shared/media/images/simbolo_elettrico.png" alt="">
    </div>
    <div class="isw-risk-body">
      <div class="isw-risk-title">Pericolo elettrico</div>
      <div class="isw-risk-desc">
        Le operazioni di accesso e manutenzione espongono al rischio elettrico. Gli interventi sotto tensione devono essere effettuati esclusivamente da personale esperto e qualificato. Misure di sicurezza:
        <ul>
          <li>Rispettare i pittogrammi di sicurezza relativi al rischio elettrico.</li>
          <li>Non effettuare manutenzione senza aver preventivamente sezionato l'alimentazione.</li>
          <li>Consultare i manuali delle attrezzature commerciali per raccomandazioni specifiche.</li>
          <li>Ispezionare periodicamente il circuito di protezione equipotenziale.</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="isw-risk">
    <div class="isw-risk-icons">
      <img src="../../../../../_shared/media/images/simbolo_avvertenza.png" alt="">
    </div>
    <div class="isw-risk-body">
      <div class="isw-risk-title">Pericolo derivante da polveri e schegge</div>
      <div class="isw-risk-desc">
        Al termine del ciclo di lavoro possono restare sulla superficie della macchina residui delle parti alimentate o accumuli di polveri. Procedere a un'accurata pulizia della superficie vibrante dopo ogni utilizzo (vedere cap. 7).
      </div>
    </div>
  </div>

</div>

```{attention}
Non effettuare attività di manutenzione e pulizia senza aver prima de-energizzato tutte le fonti di energia presenti.
```

```{attention}
È assolutamente vietato rimuovere le protezioni di sicurezza o aprire i ripari fissi senza aver prima sezionato l'alimentazione elettrica e pneumatica della macchina.
```

L'utilizzatore è tenuto a:
- analizzare i rischi di movimentazione e installazione all'interno della propria sede;
- sensibilizzare e istruire il personale addetto alle operazioni;
- applicare le segnalazioni visive di sicurezza nell'ambiente di lavoro.

</div>