<style>
.compare-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  margin: 1rem 0 1.5rem;
}
@media (max-width: 680px) {
  .compare-grid { grid-template-columns: 1fr; }
}
.compare-card {
  border: 1px solid #5a9fd4;
  border-radius: 7px;
  overflow: hidden;
  font-size: 0.92rem;
}
.compare-card-header {
  padding: 0.5rem 1rem;
  font-weight: 700;
  font-size: 0.82rem;
  letter-spacing: 0.05em;
  color: #ffffff;
}
.v20 .compare-card-header { background: #1a4a7a; }
.v30 .compare-card-header { background: #1e6fbf; }
.compare-card-body {
  padding: 0.85rem 1rem;
}
.compare-card-body p, .compare-card-body li { margin: 0.25rem 0; }
.compare-card-body ul, .compare-card-body ol { padding-left: 1.2rem; margin: 0.4rem 0; }
.compare-card-body table {
  width: 100%;
  border-collapse: collapse;
  margin: 0.5rem 0;
  font-size: 0.88rem;
}
.compare-card-body table th {
  padding: 0.35rem 0.6rem;
  text-align: left;
  font-size: 0.78rem;
  font-weight: 700;
  border-bottom: 2px solid #5a9fd4;
  opacity: 0.75;
}
.compare-card-body table td {
  padding: 0.35rem 0.6rem;
  border-bottom: 1px solid rgba(90, 159, 212, 0.3);
}
.compare-card-body table tr:last-child td { border-bottom: none; }
.compare-card-body pre {
  border: 1px solid rgba(90, 159, 212, 0.4);
  border-radius: 5px;
  padding: 0.7rem 0.9rem;
  font-size: 0.8rem;
  overflow-x: auto;
  margin: 0.5rem 0 0;
}
</style>
 
# **Software-Vergleich**
 
Questa pagina confronta le principali differenze software tra **FlexiBowl® 2.0** e **FlexiBowl® 3.0**, con l'obiettivo di guidare l'utente nella comprensione delle nuove funzionalità e dei cambiamenti operativi introdotti dalla nuova generazione.
 
:::{important}
Prima di leggere i contenuti della pagina corrente, è buona pratica avere chiare le informazioni riportate nella pagina [Interfaccia Software](int_software)
:::
---
 
## 1. Protocolli di comunicazione disponibili
 
| Protocollo | FlexiBowl® 2.0 | FlexiBowl® 3.0 |
|---|---|---|
| TCP/IP – UDP | ✓ | ✓ (TCP Server) |
| EtherNet/IP | ✓ | ✓ |
| Profinet | ✗ | ✓ |
| Modbus | ✗ | ✓ |
| Digital I/O | ✓ | ✓ (opzionale) |
 
---
 
## 2. Interfaccia utente: com'è fatta e come si accede
 
<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0 — Software Parameters</div>
<div class="compare-card-body">
 
Interfaccia **desktop** chiamata **FlexiBowl® Parameters**, da installare sul PC di controllo.
 
**Installazione e accesso:**
 
1. Installare il programma **FlexiBowl® Parameters** sul PC (fornito da ARS).
2. Collegare il PC al FlexiBowl® tramite **cavo Ethernet** (LAN diretta o via switch).
3. Avviare il programma e inserire l'**indirizzo IP** del FlexiBowl® per connettersi.
 
Dalla schermata **Main Commands** sono accessibili i pannelli **Move**, **Shake** e **Option** tramite tab nella parte superiore.
 
</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0 — Interfaccia Web</div>
<div class="compare-card-body">
 
Interfaccia **completamente web-based**: non richiede alcuna installazione. È sufficiente un browser moderno.
 
**Accesso:**
 
1. Collegare il PC al FlexiBowl® tramite Ethernet.
2. Aprire il browser e digitare nella barra degli indirizzi l'**indirizzo IP** del FlexiBowl®.
3. Si apre la **Home page** dell'interfaccia.
 
**Struttura dell'interfaccia:**
 
Il menu laterale include pagine dedicate a ogni funzione operativa (Main Command, Jog Motor, Setup, Monitor, ecc.), accessibili direttamente dal browser.
 
</div>
</div>
</div>
 
:::{note}
Se il sistema in uso è **FlexiVision One**, la configurazione viene gestita dalla sua interfaccia dedicata. Non è necessario utilizzare l'interfaccia software FlexiBowl® descritta in questa sezione.
:::
 
---
 
## 3. Come cambiare l'indirizzo IP
 
<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0</div>
<div class="compare-card-body">
 
1. Utilizzare il programma fornito sulla USB.
2. Collegare il FlexiBowl® tramite cavo Ethernet.
3. Accendere il dispositivo.
4. Avviare il programma.
5. Nella casella **IP Address**, inserire l'indirizzo: `192.168.1.10`  
   *(Il PC collegato deve essere nella stessa subnet mask Classe B — 255.255.0.0)*
6. Premere **Ping** → pop-up **"FlexiBowl® found"**.
7. Premere **Ok** per abilitare **CONNECT** e avviare la connessione.
8. Dopo la connessione verrà visualizzata la home screen.
 
</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0</div>
<div class="compare-card-body">
 
1. Aprire il browser e accedere all'interfaccia tramite l'IP corrente.
2. Dal menu laterale, aprire la pagina **Setup**.
3. Cliccare su **Get IP** per leggere i parametri di rete correnti.
4. Inserire il nuovo indirizzo IP nei campi dedicati e cliccare **Set IP**.
5. Cliccare **Apply** per confermare, poi **Reboot** per rendere effettive le modifiche.
 
</div>
</div>
</div>
 
:::{note}
**FlexiBowl® 2.0** — Se è installata una versione precedente del programma, è necessario disinstallarla prima.
:::
 
:::{important}
**FlexiBowl® 3.0** — Dopo il reboot, riconnettersi al FlexiBowl® utilizzando il nuovo indirizzo IP impostato.
:::
 
---
 
## 4. Come gestire i movimenti
 
<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0</div>
<div class="compare-card-body">
 
I movimenti vengono configurati e testati da **Main Commands**, con tre pannelli:
 
- **Move**: imposta Acceleration, Deceleration, Speed e Angle tramite slider o campo numerico. **Test Move** esegue il movimento con i valori impostati.
- **Shake**: parametri CCW Angle, CW Angle, Count, Acceleration, Deceleration e Speed. **Test Shake** esegue lo shake.
- **Try Commands**: combina più comandi in una sequenza con loop configurabile, selezionando da **All Commands** e aggiungendo a **Selected Commands**.
 
Per la produzione via protocollo, si inviano comandi ASCII (es. `QX2` per Move, `QX6` per Shake) tramite il canale TCP/UDP configurato.
 
</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0</div>
<div class="compare-card-body">
 
I movimenti sono organizzati in **sequenze** (fino a 20), configurabili dalla pagina **Main Command**. Ogni sequenza contiene fino a 10 slot di comandi (Move, Shake, Flip, Blow).
 
Dalla pagina **Main Command** è possibile:
 
- Selezionare la sequenza tramite **Select the sequence**.
- Impostare tutti i parametri nei campi numerici.
- Aggiungere comandi con **Command Available** + **ADD**; riordinarli con **UP/DOWN**; eliminarli con **DELETE** o svuotare con **CLEAR**.
- Testare con **TEST SEQUENCE** o avviare in produzione con **RUN**.
 
La pagina **Jog Motor** consente rotazione continua (Speed positivo = orario, negativo = antiorario) con Flip e Blow integrati.
 
Per la produzione via protocollo: `10[0]%` per Sequenza 1 via TCP, oppure ControlWord `10` via EtherNet/IP o Profinet.
 
</div>
</div>
</div>
 
---
 
## 5. Come cambiare i parametri
 
<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0</div>
<div class="compare-card-body">
 
I parametri operativi vengono modificati in due modalità:
 
- **Interfaccia grafica**: slider o campi numerici nelle schermate Move e Shake di **Main Commands**.
- **Via protocollo (runtime)**: comandi `RW` (Write) e `RL` (Read) via TCP/UDP. I valori devono essere moltiplicati per il **fattore di riduzione** della macchina (ottenuto con il comando `RR114`), poiché i parametri sono espressi in unità interne del driver.
 
</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0</div>
<div class="compare-card-body">
 
I parametri vengono modificati in tre modalità:
 
- **Interfaccia web**: direttamente nei campi numerici della pagina **Main Command** per ogni sequenza.
- **Via protocollo WRITE**: ControlWord blocco WRITE con formula `N × 100 + offset_parametro`
- **Via protocollo READ**: ControlWord blocco READ con formula `10000 + N × 100 + offset_parametro`
 
</div>
</div>
</div>
 
---
 
### Esempio pratico: Move + Shake su FlexiBowl® 800
 
Lo scenario è il seguente: eseguire un **Move** a 360°, poi uno **Shake**, poi un wait di 200 ms.
 
<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0 — Sequenza comandi TCP</div>
<div class="compare-card-body">
 
I parametri devono essere scalati tramite il **fattore di riduzione** della macchina:
 
<pre>QX7                     → Accendi backlight
RR114                   → Leggi fattore di riduzione
variabile_riduzione = RX 1
 
RL1 (50 × variabile_riduzione), RW11   → Acceleration Move = 50%
RL1 (50 × variabile_riduzione), RW12   → Deceleration Move = 50%
RL1 (35 × variabile_riduzione), RW13   → Speed Move = 35%
RL1 (360 × variabile_riduzione), RW14  → Angle Move = 360°
QX2                     → Esegui Move
 
RL1 (50 × variabile_riduzione), RW15  → Acceleration Shake = 50%
RL1 (50 × variabile_riduzione), RW16  → Deceleration Shake = 50%
RL1 (50 × variabile_riduzione), RW110 → Speed Shake = 50%
RL1 (30 × variabile_riduzione), RW18  → Angle CW Shake = -30°
RL1 (30 × variabile_riduzione), RW19  → Angle CCW Shake = -45°
RL1 2, RW17                           → Count Shake = 2
QX6                     → Esegui Shake</pre>
 
Il wait di 200 ms è gestito dal sistema chiamante (robot o PLC).
 
</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0 — Configurazione interfaccia web</div>
<div class="compare-card-body">
 
Dalla pagina **Main Command**, selezionare **SEQUENCE 1** e impostare:
 
| Parametro | Valore |
|---|---|
| Acceleration Move | 50 % |
| Deceleration Move | 50 % |
| Speed Move | 35 % |
| Angle Move | 360° |
| Acceleration Shake | 50 % |
| Deceleration Shake | 50 % |
| Speed Shake | 50 % |
| Ccw Angle Shake | −45° |
| Cw Angle Shake | −30° |
| Count Shake | 2 |
 
Aggiungere alla lista: `FLB_MOVE` → `FLB_SHAKE`. Verificare Backlight dalla pagina **Option**. Il wait di 200 ms si gestisce aggiungendo `FLB_WAIT` alla lista o lato sistema chiamante.
 
Per eseguire la sequenza via TCP:
 
<pre>10[0]%    → Esegui Sequenza 1</pre>
 
Il sistema risponde con `10[0]` a conferma.
 
</div>
</div>
</div>
 
---
 
## 6. Come leggere gli allarmi
 
<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0</div>
<div class="compare-card-body">
 
Gli allarmi si consultano da **Monitor → Alarm Status** del programma **FlexiBowl® Parameters**. La schermata mostra gli stati del driver con indicatori LED (verde = OK, rosso = errore). La schermata **Driver Status** mostra in tempo reale tutte le variabili operative.
 
Reset allarme via protocollo:
 
<pre>Chr(0)Chr(7)QX12Chr(13)    → Reset allarme e riabilitazione motore</pre>
 
</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0</div>
<div class="compare-card-body">
 
Gli allarmi si consultano dalla pagina **Monitor** (tab: **I/O Status**, **Driver Status**, **Alarm Status**).
 
Via protocollo, il segnale di allarme è esposto da **In_Error** (BOOL) e il codice attivo da **ErrorCode** (UDINT):
 
<pre>InError%         → InError[1]% se c'è errore, InError[0]% se OK
ErrorCode%       → ErrorCode[N]% con il codice dell'errore attivo</pre>
 
Reset dell'allarme:
- Via protocollo TCP: `Reset%`
- Via variabile digitale: fronte di salita sul segnale di input **Reset** (BOOL)
 
</div>
</div>
</div>
 
:::{warning}
Prima di eseguire il reset, identificare e risolvere la causa dell'errore. Il sistema non eseguirà nuovi comandi di movimento finché è presente un errore attivo.
:::
 
:::{note}
Per la lista completa dei codici errore fare riferimento alla sezione [Codici Di Errore](sec-err)
:::
 
---
 
## 7. Modalità tracking (FlexiTrack)
 
<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0</div>
<div class="compare-card-body">
 
La modalità **FlexiTrack** è un'opzione acquistabile separatamente che consente di mantenere il FlexiBowl® in **rotazione continua** (jog) sincronizzando il segnale encoder con il robot di pick.
 
**Hardware richiesto:**
 
- Connessione all'**encoder interno** tramite il connettore del pannello di controllo (segnale quadratura TTL, 4000 conteggi/giro sul motore; per FlexiBowl® 500/650/800 con riduzione 1:3 → 12000 conteggi/giro sul disco).
- In alternativa, **encoder esterno** (incremental, TTL RS422, ≥ 12000 ppr) sul perno solidale alla puleggia condotta.
 
**Comandi principali FlexiTrack (via TCP/UDP):**
 
| Comando | Descrizione |
|---|---|
| `JA<valore>` | Accelerazione/decelerazione in giri/s² |
| `JL<valore>` | Decelerazione (se diversa da JA, inviare dopo JA) |
| `JS<valore>` | Velocità di rotazione in giri/s |
| `CC<valore>` | Corrente diretta al motore |
| `DI1` | Direzione oraria |
| `DI-1` | Direzione antioraria |
| `CJ` | Avvia jog (rotazione continua) |
| `SJ` | Ferma jog (con rampa JL) |
| `IL2` / `IH2` | Attiva / disattiva Flip |
| `IL3` / `IH3` | Attiva / disattiva Blow |
 
**Parametri consigliati:**
 
<pre>JA0.2    → accelerazione 0.2 giri/s²
JL0.2    → decelerazione 0.2 giri/s²
JS0.2    → velocità 0.2 giri/s
CC1.3    → corrente motore
DI1      → rotazione oraria</pre>
 
Flip e Blow vanno implementati tramite un **programma in background** con ciclo iterativo che commuta lo stato delle valvole.
 
</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0</div>
<div class="compare-card-body">
 
La modalità jog è **integrata nativamente** nella pagina **Jog Motor** — senza opzioni hardware aggiuntive.
 
**Parametri di movimento Jog:**
 
| Parametro | Unità | Descrizione |
|---|---|---|
| Acceleration | % | Rampa di accelerazione all'avvio |
| Deceleration | % | Rampa di decelerazione all'arresto |
| Speed | % | Velocità — positivo = orario; negativo = antiorario |
 
**Funzioni accessorie durante il Jog:**
 
- **Flip Enable**: flip automatico ciclico con Flip Duration, Flip Pression, Flip Pause.
- **Blow Enable**: soffio automatico ciclico con Blow Duration, Blow Pression, Blow Pause, Blow Type (BLOWc, BLOWe, BLOWc+BLOWe).
- **Backlight 1 / 2**: toggle retroilluminazione, indipendente dallo stato del jog.
 
**Avvio e arresto:**
 
- **START JOG**: avvia la rotazione continua.
- **STOP JOG**: interrompe con rampa di decelerazione.
 
Controllo via protocollo:
 
<pre>40[0]%    → Start Jog Seq (via TCP)
41[0]%    → Stop Jog Seq (via TCP)</pre>
 
</div>
</div>
</div>
 
:::{important}
Prima di avviare il jog, verificare che il motore sia abilitato (**ENABLE MOTOR** attivo) e che lo stato del sistema sia **READY**.
:::
 
:::{important}
Con FlexiTrack **(FlexiBowl® 2.0)**, il controllo del movimento è possibile **solo via protocollo Ethernet** (TCP/UDP). Il protocollo Digital I/O non è supportato.
:::


<br>

<!-- Versions and languages set-up -->
<style>
  .fixed-bar {
    position: fixed;
    bottom: 10px;
    right: 10px;
    background: rgba(240, 240, 240, 0.85);
    border: 1px solid rgba(100, 100, 100, 0.3);
    border-radius: 6px;
    box-shadow: 0 1px 6px rgba(0, 0, 0, 0.1);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 0.9rem;
    color: #222;
    display: flex;
    gap: 12px;
    padding: 6px 12px;
    align-items: center;
    z-index: 9999;
    backdrop-filter: saturate(180%) blur(10px);
  }

  @media print {
    .fixed-bar {
      display: none !important;
    }
  }

  .fixed-bar .dropdown {
    position: relative;
    user-select: none;
  }

  .fixed-bar .dropdown-toggle {
    background-color: rgba(200, 200, 200, 0.4);
    color: #222;
    padding: 6px 10px;
    border: 1px solid rgba(100, 100, 100, 0.3);
    border-radius: 4px;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 6px;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
    white-space: nowrap;
    transition: background-color 0.3s ease;
  }

  .fixed-bar .dropdown-toggle::after {
    content: none !important;
    display: none !important;
  }

  .fixed-bar .dropdown-toggle:hover {
    background-color: rgba(100, 150, 220, 0.2);
    color: #1a3e72;
    border-color: rgba(26, 62, 114, 0.6);
  }

  .fixed-bar .dropdown-toggle .fa {
    font-size: 0.9rem;
  }

  .fixed-bar .dropdown-menu {
    position: absolute;
    bottom: 100%;
    left: 0;
    background-color: rgba(250, 250, 250, 0.95);
    border: 1px solid rgba(150, 150, 150, 0.3);
    border-radius: 4px;
    box-shadow: 0 3px 8px rgba(0, 0, 0, 0.1);
    min-width: 140px;
    max-height: 200px;
    overflow-y: auto;
    display: none;
    flex-direction: column;
    z-index: 10000;
    backdrop-filter: saturate(180%) blur(8px);
  }

  .fixed-bar .dropdown-menu.show {
    display: flex;
  }

  .fixed-bar .dropdown-menu a {
    padding: 8px 12px;
    color: #1a3e72;
    text-decoration: none;
    border-bottom: 1px solid rgba(200, 200, 200, 0.5);
    white-space: nowrap;
    transition: background-color 0.25s ease;
  }

  .fixed-bar .dropdown-menu a:last-child {
    border-bottom: none;
  }

  .fixed-bar .dropdown-menu a:hover {
    background-color: rgba(100, 150, 220, 0.15);
  }

  .dropdown-download-buttons .btn__icon-container svg {
    width: 1em;
    height: 1em;
    stroke: currentColor;
    fill: none;
    stroke-width: 1.6;
    stroke-linecap: round;
    stroke-linejoin: round;
    vertical-align: middle;
  }

  a.headerlink.manual-heading-action {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    margin-left: 0.2em;
    text-decoration: none;
    color: #7b8493;
    transition: color 0.2s ease, opacity 0.2s ease;
  }

  a.headerlink.manual-heading-action svg {
    width: 0.8em;
    height: 0.8em;
    stroke: currentColor;
    fill: none;
    stroke-width: 1.6;
    stroke-linecap: round;
    stroke-linejoin: round;
    vertical-align: middle;
  }

  a.headerlink.manual-feedback-link:hover,
  a.headerlink.manual-feedback-link:focus-visible {
    color: #2563eb;
  }

  a.headerlink.manual-service-link:hover,
  a.headerlink.manual-service-link:focus-visible {
    color: #d97706;
  }
</style>

<div class="fixed-bar" role="region" aria-label="Version and language selector">
  <div class="dropdown" data-selector="version">
    <div class="dropdown-toggle" tabindex="0" aria-haspopup="listbox" aria-expanded="false">
      Version: <span class="current-value">V. 1.0</span>
      <span class="caret-icon" aria-hidden="true">&#9662;</span>
    </div>
    <div class="dropdown-menu" role="listbox">
      	<a href="#" role="option">V. 1.0</a>
    </div>
  </div>

  <div class="dropdown" data-selector="language">
    <div class="dropdown-toggle" tabindex="0" aria-haspopup="listbox" aria-expanded="false">
      Language: <span class="current-value">DE</span>
      <span class="caret-icon" aria-hidden="true">&#9662;</span>
    </div>
    <div class="dropdown-menu" role="listbox">
      	<a href="#" role="option">DE</a>
				<a href="#" role="option">EN</a>
				<a href="#" role="option">ES</a>
				<a href="#" role="option">FR</a>
				<a href="#" role="option">IT</a>
    </div>
  </div>
</div>

<script>
  (function () {
    const bar = document.querySelector('.fixed-bar');
    if (!bar) {
      return;
    }

    const inlineVersions = ["V. 1.0"];
    const inlineLanguages = ["DE", "EN", "ES", "FR", "IT"];
    const manifest = window.FV_VERSIONING || null;
    const versions = Array.isArray(manifest && manifest.versions) && manifest.versions.length
      ? manifest.versions
      : inlineVersions;
    const offlineZipEnabled = false;
    const offlineZipFileName = 'Offline manual.zip';
    const americanRegions = new Set([
      'AG', 'AR', 'AW', 'BB', 'BL', 'BM', 'BO', 'BQ', 'BR', 'BS', 'BZ', 'CA', 'CL', 'CO', 'CR',
      'CU', 'CW', 'DM', 'DO', 'EC', 'FK', 'GD', 'GF', 'GL', 'GP', 'GT', 'GY', 'HN', 'HT', 'JM',
      'KN', 'KY', 'LC', 'MF', 'MQ', 'MS', 'MX', 'NI', 'PA', 'PE', 'PM', 'PR', 'PY', 'SR', 'SV',
      'SX', 'TC', 'TT', 'US', 'UY', 'VC', 'VE', 'VG', 'VI', '419'
    ]);
    const additionalAmericanTimeZones = new Set([
      'Atlantic/Bermuda',
      'Pacific/Easter',
      'Pacific/Galapagos',
      'Pacific/Honolulu',
      'Pacific/Pitcairn'
    ]);

    function setCaret(toggle, isOpen) {
      const caret = toggle.querySelector('.caret-icon');
      if (caret) {
        caret.innerHTML = isOpen ? '&#9652;' : '&#9662;';
      }
    }

    function closeAllMenus() {
      bar.querySelectorAll('.dropdown').forEach(dropdown => {
        const menu = dropdown.querySelector('.dropdown-menu');
        const toggle = dropdown.querySelector('.dropdown-toggle');
        menu.classList.remove('show');
        toggle.setAttribute('aria-expanded', 'false');
        setCaret(toggle, false);
      });
    }

    function getLanguagesForVersion(version) {
      const manifestLanguages = manifest &&
        manifest.languagesByVersion &&
        Array.isArray(manifest.languagesByVersion[version]) &&
        manifest.languagesByVersion[version].length
          ? manifest.languagesByVersion[version]
          : null;

      if (manifestLanguages) {
        return manifestLanguages;
      }

      return inlineLanguages;
    }

    function getDefaultLanguageForVersion(version) {
      const manifestDefault = manifest &&
        manifest.defaultLanguageByVersion &&
        typeof manifest.defaultLanguageByVersion[version] === 'string'
          ? manifest.defaultLanguageByVersion[version]
          : '';

      if (manifestDefault) {
        return manifestDefault;
      }

      const availableLanguages = getLanguagesForVersion(version);
      return availableLanguages.length ? availableLanguages[0] : (inlineLanguages[0] || '');
    }

    function populateSelectorMenu(selector, values) {
      const menu = bar.querySelector(`[data-selector="${selector}"] .dropdown-menu`);
      if (!menu) {
        return;
      }

      menu.innerHTML = '';
      values.forEach(value => {
        const link = document.createElement('a');
        link.href = '#';
        link.setAttribute('role', 'option');
        link.textContent = value;
        menu.appendChild(link);
      });
    }

    function getNavigationContext() {
      const currentUrl = new URL(window.location.href);
      const rawSegments = currentUrl.pathname.split('/').filter(Boolean);
      const decodedSegments = rawSegments.map(segment => decodeURIComponent(segment));
      const currentVersionLabel = bar.querySelector('[data-selector="version"] .current-value');
      const currentLanguageLabel = bar.querySelector('[data-selector="language"] .current-value');
      const fallbackVersion = currentVersionLabel ? currentVersionLabel.textContent.trim() : '';
      const versionIndex = decodedSegments.findIndex(segment => versions.includes(segment));
      const currentVersion = versionIndex !== -1 ? decodedSegments[versionIndex] : fallbackVersion;
      const availableLanguages = getLanguagesForVersion(currentVersion);
      const fallbackLanguage = currentLanguageLabel ? currentLanguageLabel.textContent.trim() : '';
      const languageIndex = decodedSegments.findIndex(
        (segment, index) => index > versionIndex && availableLanguages.includes(segment)
      );

      return {
        currentUrl: currentUrl,
        rawSegments: rawSegments,
        versionIndex: versionIndex,
        currentVersion: currentVersion,
        currentLanguage: languageIndex !== -1 ? decodedSegments[languageIndex] : fallbackLanguage
      };
    }

    function refreshNavigationMenus() {
      const context = getNavigationContext();
      const resolvedVersion = versions.includes(context.currentVersion) ? context.currentVersion : (versions[0] || context.currentVersion);
      const availableLanguages = getLanguagesForVersion(resolvedVersion);
      const resolvedLanguage = availableLanguages.includes(context.currentLanguage)
        ? context.currentLanguage
        : (getDefaultLanguageForVersion(resolvedVersion) || context.currentLanguage);

      populateSelectorMenu('version', versions);
      populateSelectorMenu('language', availableLanguages);

      const versionLabel = bar.querySelector('[data-selector="version"] .current-value');
      const languageLabel = bar.querySelector('[data-selector="language"] .current-value');
      if (versionLabel) {
        versionLabel.textContent = resolvedVersion;
      }
      if (languageLabel) {
        languageLabel.textContent = resolvedLanguage;
      }
    }

    function buildScopedUrl(targetVersion, targetLanguage, pageName) {
      const context = getNavigationContext();
      const rootSegments = context.versionIndex !== -1 ? context.rawSegments.slice(0, context.versionIndex) : [];
      const targetPath = '/' + rootSegments.concat([
        encodeURIComponent(targetVersion),
        encodeURIComponent(targetLanguage),
        encodeURIComponent(pageName)
      ]).join('/');

      if (context.currentUrl.protocol === 'file:') {
        return 'file://' + targetPath;
      }

      return context.currentUrl.origin + targetPath;
    }

    function buildTargetUrl(targetVersion, targetLanguage) {
      return buildScopedUrl(targetVersion, targetLanguage, 'index.html');
    }

    function buildSiteRootAssetUrl(fileName) {
      const context = getNavigationContext();
      const rootSegments = context.versionIndex !== -1 ? context.rawSegments.slice(0, context.versionIndex) : [];
      const targetPath = '/' + rootSegments.concat([encodeURIComponent(fileName)]).join('/');

      if (context.currentUrl.protocol === 'file:') {
        return 'file://' + targetPath;
      }

      return context.currentUrl.origin + targetPath;
    }

    function buildClientSiteZipUrl() {
      return buildSiteRootAssetUrl(offlineZipFileName);
    }

    function getHeadingText(heading) {
      const clone = heading.cloneNode(true);
      clone.querySelectorAll('a.headerlink').forEach(link => link.remove());
      return clone.textContent.replace(/\s+/g, ' ').trim();
    }

    function normalizeMailText(text) {
      return String(text || '').replace(/\u00AE/g, '');
    }

    function getTimeZoneAmericaDecision() {
      try {
        const timeZone = String(Intl.DateTimeFormat().resolvedOptions().timeZone || '').trim();
        if (!timeZone) {
          return null;
        }
        return timeZone.startsWith('America/') || additionalAmericanTimeZones.has(timeZone);
      } catch (error) {
        return null;
      }
    }

    function isCoordinateInAmericas(latitude, longitude) {
      if (!Number.isFinite(latitude) || !Number.isFinite(longitude)) {
        return null;
      }

      return latitude >= -60 && latitude <= 85 && longitude >= -170 && longitude <= -25;
    }

    function getCurrentPosition(options) {
      return new Promise((resolve, reject) => {
        if (!navigator.geolocation || typeof navigator.geolocation.getCurrentPosition !== 'function') {
          reject(new Error('Geolocation unavailable'));
          return;
        }

        navigator.geolocation.getCurrentPosition(resolve, reject, options);
      });
    }

    async function resolveServiceAddress() {
      const timeZoneDecision = getTimeZoneAmericaDecision();
      if (timeZoneDecision === false) {
        return 'service@arsautomation.com';
      }

      const canTryGeolocation = Boolean(
        navigator.onLine &&
        window.isSecureContext &&
        navigator.geolocation &&
        typeof navigator.geolocation.getCurrentPosition === 'function'
      );

      if (canTryGeolocation) {
        try {
          const position = await getCurrentPosition({
            enableHighAccuracy: false,
            timeout: 4000,
            maximumAge: 300000
          });
          const inAmericas = isCoordinateInAmericas(position.coords.latitude, position.coords.longitude);
          if (inAmericas !== null) {
            return inAmericas ? 'us.service@arsautomation.com' : 'service@arsautomation.com';
          }
        } catch (error) {
        }
      }

      if (timeZoneDecision === true) {
        return 'us.service@arsautomation.com';
      }

      return 'service@arsautomation.com';
    }

    function buildMailtoUrl(address, subject, body) {
      return 'mailto:' + address +
        '?subject=' + encodeURIComponent(normalizeMailText(subject)) +
        '&body=' + encodeURIComponent(normalizeMailText(body));
    }

    function createHeadingActionLink(className, title, mailtoUrl, svgMarkup) {
      const link = document.createElement('a');
      link.className = 'headerlink manual-heading-action ' + className;
      link.href = mailtoUrl;
      link.title = title;
      link.setAttribute('aria-label', title);
      link.innerHTML = svgMarkup;
      return link;
    }

    function addHeadingActions() {
      const feedbackIcon = [
        '<svg viewBox="0 0 16 16" aria-hidden="true">',
        '<path d="M3 3.5h10v6.5H7.5L4.5 13v-3H3z"></path>',
        '<path d="M6 6.2h4"></path>',
        '<path d="M6 8.2h3"></path>',
        '</svg>'
      ].join('');

        const serviceIcon = [
          '<svg viewBox="0 0 16 16" aria-hidden="true">',
          '<circle cx="8" cy="8" r="5.2"></circle>',
          '<path d="M6.4 6.1A1.9 1.9 0 0 1 8 5.2c1.1 0 1.9.7 1.9 1.7 0 .8-.4 1.3-1.2 1.8-.6.4-.9.8-.9 1.5"></path>',
          '<circle cx="8" cy="11.7" r="0.45" style="fill:currentColor;stroke:none"></circle>',
          '</svg>'
        ].join('');

      document.querySelectorAll('h1 > a.headerlink, h2 > a.headerlink, h3 > a.headerlink, h4 > a.headerlink, h5 > a.headerlink, h6 > a.headerlink').forEach(link => {
        const heading = link.parentElement;
        if (!heading || heading.querySelector('.manual-feedback-link') || heading.querySelector('.manual-service-link')) {
          return;
        }

        const sectionTitle = getHeadingText(heading);
        const sectionUrl = new URL(link.getAttribute('href'), window.location.href).href;
        const pageUrl = window.location.href.split('#')[0];
        const feedbackBody = [
          'Hello Documentation Team,',
          '',
          'I would like to suggest an improvement for this section of the manual.',
          '',
          'Section: ' + sectionTitle,
          'Page: ' + pageUrl,
          'Section link: ' + sectionUrl,
          '',
          'Suggestion:',
          ''
        ].join('\n');
          const serviceBody = [
            'Hello Service Team,',
            '',
            'I need support related to this section of the manual.',
            '',
            'Section: ' + sectionTitle,
            'Page: ' + pageUrl,
            'Section link: ' + sectionUrl,
            '',
            'FlexiBowl serial number:',
            '',
            'Photos or videos of the issue attached:',
            '',
            'Issue description:',
            ''
          ].join('\n');

        const feedbackLink = createHeadingActionLink(
          'manual-feedback-link',
          'Suggest an improvement for this section',
          buildMailtoUrl('documentation@arsautomation.com', 'Documentation suggestion: ' + sectionTitle, feedbackBody),
          feedbackIcon
        );
          const serviceLink = createHeadingActionLink(
            'manual-service-link',
            'Contact service about this section',
            '#',
            serviceIcon
          );
          serviceLink.addEventListener('click', async event => {
            event.preventDefault();
            const serviceAddress = await resolveServiceAddress();
            window.location.href = buildMailtoUrl(serviceAddress, 'Service request: ' + sectionTitle, serviceBody);
          });

          heading.appendChild(feedbackLink);
          heading.appendChild(serviceLink);
        });
    }

    function enhancePrintMenu() {
      const dropdown = document.querySelector('.dropdown-download-buttons');
      if (!dropdown || dropdown.dataset.printMenuEnhanced === 'true') {
        return;
      }

      dropdown.dataset.printMenuEnhanced = 'true';

      const toggleButton = dropdown.querySelector('.dropdown-toggle');
      const hasReleaseDownloads = offlineZipEnabled;

      if (toggleButton) {
        const toggleLabel = hasReleaseDownloads ? 'Export options' : 'Print options';
        toggleButton.setAttribute('aria-label', toggleLabel);
        toggleButton.setAttribute('title', toggleLabel);
        toggleButton.setAttribute('data-bs-original-title', toggleLabel);
        const toggleIcon = toggleButton.querySelector('i');
        if (toggleIcon) {
          toggleIcon.className = hasReleaseDownloads ? 'fas fa-download' : 'fas fa-print';
        }
      }

      dropdown.querySelectorAll('.btn-download-source-button').forEach(sourceButton => {
        const sourceItem = sourceButton.closest('li');
        if (sourceItem) {
          sourceItem.remove();
        }
      });

      const pagePrintButton = dropdown.querySelector('.btn-download-pdf-button');
      if (pagePrintButton) {
        pagePrintButton.setAttribute('title', 'Print this page');
        pagePrintButton.setAttribute('aria-label', 'Print this page');
        pagePrintButton.setAttribute('data-bs-original-title', 'Print this page');
        const textContainer = pagePrintButton.querySelector('.btn__text-container');
        if (textContainer) {
          textContainer.textContent = 'Print this page';
        }
      }

      const menu = dropdown.querySelector('.dropdown-menu');
      if (!menu) {
        return;
      }

      menu.querySelectorAll('.btn-download-client-site-zip-button').forEach(button => {
        const item = button.closest('li');
        if (item) {
          item.remove();
        }
      });

      if (offlineZipEnabled) {
        const siteZipItem = document.createElement('li');
        const siteZipLink = document.createElement('a');
        siteZipLink.className = 'btn btn-sm dropdown-item btn-download-client-site-zip-button';
        siteZipLink.title = 'Download offline manual';
        siteZipLink.setAttribute('aria-label', 'Download offline manual');
        siteZipLink.setAttribute('download', offlineZipFileName);
        siteZipLink.href = buildClientSiteZipUrl();
        siteZipLink.innerHTML = [
          '<span class="btn__icon-container">',
          '<svg viewBox="0 0 16 16" aria-hidden="true">',
          '<path d="M4 3.5h8v2.5H4z"></path>',
          '<path d="M4 6h8v6.5H4z"></path>',
          '<path d="M8 3.5v9"></path>',
          '<path d="M6.3 9.2L8 10.9l1.7-1.7"></path>',
          '</svg>',
          '</span>',
          '<span class="btn__text-container">Download offline manual</span>'
        ].join('');
        siteZipItem.appendChild(siteZipLink);
        menu.appendChild(siteZipItem);
      }
    }

    refreshNavigationMenus();

    bar.querySelectorAll('.dropdown').forEach(dropdown => {
      const toggle = dropdown.querySelector('.dropdown-toggle');
      const menu = dropdown.querySelector('.dropdown-menu');
      const selector = dropdown.getAttribute('data-selector');

      toggle.addEventListener('click', event => {
        event.stopPropagation();
        const willOpen = toggle.getAttribute('aria-expanded') !== 'true';
        closeAllMenus();

        if (willOpen) {
          menu.classList.add('show');
          toggle.setAttribute('aria-expanded', 'true');
          setCaret(toggle, true);
        }
      });

      menu.addEventListener('click', event => {
        const link = event.target.closest('a');
        if (!link) {
          return;
        }

        event.preventDefault();
        const selectedValue = link.textContent.trim();
        const context = getNavigationContext();
        if (!selectedValue) {
          return;
        }

        if (selector === 'version') {
          const targetVersion = selectedValue;
          const availableLanguages = getLanguagesForVersion(targetVersion);
          const targetLanguage = availableLanguages.includes(context.currentLanguage)
            ? context.currentLanguage
            : getDefaultLanguageForVersion(targetVersion);
          if (targetLanguage) {
            window.location.href = buildTargetUrl(targetVersion, targetLanguage);
          }
          return;
        }

        window.location.href = buildTargetUrl(context.currentVersion, selectedValue);
      });
    });

    window.addEventListener('click', closeAllMenus);
    window.addEventListener('keydown', event => {
      if (event.key === 'Escape') {
        closeAllMenus();
      }
    });

    addHeadingActions();
    enhancePrintMenu();
  })();
</script>
