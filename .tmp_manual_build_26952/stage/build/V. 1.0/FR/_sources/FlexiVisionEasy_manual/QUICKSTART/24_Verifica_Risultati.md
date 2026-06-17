(dashboard)=
# **Monitoraggio Applicazione: Dashboard**

La **Dashboard** è l'interfaccia principale per il monitoraggio in tempo reale del sistema FlexiVision One. In questa pagina è possibile verificare l'efficienza del processo, analizzare i tempi di ciclo, validare il riconoscimento dei componenti e identificare eventuali colli di bottiglia nel sistema.


---

## Panoramica Interfaccia

L'interfaccia della Dashboard si divide in quattro sezioni principali:
![Pagina Hooper Setup](../../../../_shared/media/images/pagina_dashboard.png)
1. [**Controllo Operativo**](controllooperativo): Comandi e stato esecuzione
2. [**Analisi della Visione**](analisivisione): Visualizzazione pezzi rilevati e dettagli
3. [**Indicatori Performance**](indicatoriperformance): Connettività e tempi ciclo
4. [**Analisi Grafica**](analisigrafica): Grafici storici produttività e tempi

---
(controllooperativo)=
## Controllo Operativo - Comandi e stato esecuzione

```{list-table}
:header-rows: 1
:widths: 25 75

* - Elemento
  - Descrizione e Funzione
* - **In Run**
  - Indicatore di stato che segnala se il sistema è attualmente in funzione.  
    **Verde** 🟢: Sistema attivo e operativo.  
    **Rosso** 🔴: Sistema arrestato o in pausa.
* - **In Run Time**
  - Visualizza il tempo totale di attività del sistema dall'avvio dell'applicazione. 
* - **Selezione FlexiBowl**
  - Menu a tendina per selezionare il FlexiBowl specifico da monitorare. 
* - **Test Locator**
  - Scatta una foto dell'area di visione e avvia il riconoscimento dei componenti presenti. 
```

```{tip}
**Test Locator**
Utile per:
- Verificare che i componenti effettivamente vengano riconosciuti dalla visione 
- Nel caso in cui sia ha una collisione tra robot e comonente e voglio controllare l'affidabilità delle clearances
```

---
(analisivisione)=
## Analisi della Visione

Al centro della dashboard vengono riportati i dati relativi ai componenti identificati dal sistema di visione.

### Detected Vision Parts

**Detected Vision Parts** mostra:
- Immagine acquisita in tempo reale dalla camera
- Un **grafico storico** dei rilevamenti negli ultimi 30 secondi che mostra l'andamento del numero di pezzi riconosciuti per acquisizione.


### Tabella Modelli Rilevati

**Dettaglio componenti riconosciuti**

La tabella sotto l'immagine elenca tutti i componenti presenti nell'area di pick con i seguenti parametri:

```{list-table}
:header-rows: 1
:widths: 15 20 65

* - Campo
  - Tipo Dato
  - Descrizione
* - **Id**
  - Intero
  - Identificativo univoco progressivo del componente (0, 1, 2, ...).   
  Id 0 = componente con score più alto (migliore corrispondenza al modello se ordinati con Score Descending come consigliato).
* - **X**
  - Millimetri
  - Coordinata X del componente.
* - **Y**
  - Millimetri
  - Coordinata Y del componente.
* - **Rot (Rotation)**
  - Gradi
  - Angolo di rotazione del componente. 
* - **Score**
  - Percentuale
  - Valore percentuale (0.00-1.00 o 0%-100%) che esprime il grado di affidabilità del riconoscimento. Rappresenta la vicinanza/fedeltà rispetto al modello di riferimento. Score più alto = corrispondenza migliore.
```

```{list-table} **Interpretazione Score**

* - **Score > 0.90 (90%)**:
  - 
    - Eccellente corrispondenza al modello
    - Picking ad alta confidenza

* - **Score 0.80-0.90 (80-90%)**:
  - 
    - Buona corrispondenza
    - Picking sicuro se Accept Threshold configurato appropriatamente

* - **Score 0.70-0.80 (70-80%)**:
  - 
    - Corrispondenza accettabile
    - Verificare consistenza nel tempo

* - **Score < 0.70 (< 70%)**:
  - 
    - Corrispondenza scarsa
    - Se ricorrente, rivedere modello o Accept Threshold.
```

---
(indicatoriperformance)=
## Indicatori di Stato e Performance

### Connettività

Indicatori di stato delle comunicazioni con i dispositivi esterni:

```{list-table}
:header-rows: 1
:widths: 25 75

* - Indicatore
  - Descrizione
* - **FlexiBowl**
  - Stato della connessione hardware tra il VisionController (PC) e FlexiBowl.  
    **Verde**: Connesso e comunicante.  
    **Rosso**: Disconnesso o errore comunicazione.
* - **Robot**
  - Stato della comunicazione con il robot.   
    **Verde**: Connessione TCP/IP stabilita.  
    **Rosso**: Disconnesso o timeout comunicazione.
```

```{warning}
**Azioni in caso di disconnessione**

**FlexiBowl rosso**:
- Verificare cavo Ethernet FlexiBowl → VisionController
- Controllare alimentazione FlexiBowl
- Verificare IP FlexiBowl in FlexiBowl Setup
- Tentare reconnect o riavvio software

**Robot rosso**:
- Verificare cavo Ethernet Robot → VisionController
- Controllare che robot abbia aperto connessione TCP/IP
- Verificare porta TCP/IP in Robot Setup
- Controllare programma robot (Indirizzo IP del VisionController e Porta inserita correttamente nella sezione robot setup )

In produzione, entrambi gli indicatori devono essere sempre verdi.
```

### Analisi dei Tempi

Il sistema fornisce un breakdown dettagliato dei tempi di ciclo per individuare eventuali colli di bottiglia e ottimizzare il processo.

```{list-table}
:header-rows: 1
:widths: 35 65

* - Voce Temporale
  - Descrizione
* - **Camera Processing Time**
  - Tempo impiegato per l'acquisizione dell'immagine dal sensore camera. Include tempo di esposizione e trasferimento dati. 
* - **Locator Processing Time**
  - Tempo necessario all'algoritmo di visione per localizzare e riconoscere i componenti nell'immagine acquisita. Dipende da: numero modelli attivi, complessità modelli, numero clearances. 
* - **Total Vision Processing**
  - Somma dei tempi di Camera e Locator. Rappresenta il tempo totale che il sistema di visione impiega per elaborare un'immagine e inviare la/le coordinate.       
* - **Total FlexiBowl Time**
  - Tempo impiegato dal FlexiBowl per eseguire una sequenza di movimentazione completa. 
* - **Total Robot Time**
  - Tempo stimato o rilevato per l'operazione di Pick & Place completa del robot. Include: avvicinamento → presa → sollevamento → deposito → ritorno. 
* - **Total Processing Time**
  - Tempo totale del ciclo completo (Visione + FlexiBowl + Robot). Rappresenta il tempo dall'inizio di un ciclo all'inizio del successivo. Determina la produttività massima teorica (PPM).
```

```{tip}
**Interpretazione tempi per ottimizzazione**

Il grafico dei tempi permette di identificare il **collo di bottiglia** del sistema:

**Se Total Vision Processing è il maggiore**:
- Troppi modelli attivi → Disabilitare modelli non necessari
- Modelli troppo complessi → Semplificare con Score Threshold più alto
- Troppi Clearances → Ridurre numero o dimensione clearances
- Camera Processing alto → Ridurre tempo esposizione

**Se Total FlexiBowl Time è il maggiore**:
- Troppe pause → Ottimizzare sincronizzazione Flip/Move e ridurre la pausa di stabilizzazione (Pause X ms)
- Sequenza movimentazione troppo lenta → Aumentare velocità in Config FlexiBowl
- Angolo rotazione eccessivo → Ridurre Move Angle
- Shake troppo lungo → Aumentare velocità SHAKE e ridurre cicli SHAKE  

**Se Total Robot Time è il maggiore**:
- Traiettoria robot non ottimizzata → Ottimizzare path planning robot
- Velocità robot troppo bassa → Aumentare velocità movimento (se sicuro)
- Distanza deposito eccessiva → Riposizionare punto deposito più vicino
- Tempi di presa troppo lunghi → Ottimizzare apertura/chiusura gripper

**Obiettivo ottimizzazione**: Bilanciare i tre tempi per ridurre Total Processing Time complessivo.
```

---
(analisigrafica)=
## Analisi Grafica

I grafici nella parte inferiore della dashboard permettono un'analisi predittiva e diagnostica delle performance del sistema nel tempo.

### 1. Parts Per Minute (PPM)

```{list-table}
* - **Grafico produttività**
  - Mostra la produttività media del sistema espressa in **componenti prelevati al minuto** (Parts Per Minute).

* - **Caratteristiche**:
  - 
    - Asse X: Tempo 
    - Asse Y: PPM (pezzi/secondo)
    - Linea trend: Media mobile per identificare tendenze

* - **Utilizzo**:
  - 
    - Monitorare stabilità produttività nel tempo
    - Identificare degradazioni performance
    - Calcolare throughput effettivo vs teorico
```

```{tip}

  :::{list-table} **Interpretazione PPM**

    * - **PPM costante e stabile**:
      - 
        - ✓ Sistema ben configurato
        - ✓ Parametri ottimizzati
        - ✓ Nessun collo di bottiglia critico

    * - **PPM in diminuzione progressiva**:
      - 
        - ⚠️ Possibile usura componenti (superficie grip FlexiBowl)
        - ⚠️ Hopper che si svuota (se presente, meno pressione = scarico più lento)
        - ⚠️ Accumulo sporcizia su camera/illuminazione

    * - **PPM con fluttuazioni ampie**:
      - 
        - ⚠️ Instabilità nel processo
        - ⚠️ Problemi intermittenti di riconoscimento
        - ⚠️ Interferenze esterne (vibrazioni, luce variabile)

    * - **Azioni correttive**:
      - 
        - Analizzare correlazione con grafici tempi
        - Identificare quale componente (Vision/FlexiBowl/Robot) causa variazioni
        - Intervenire su parametri specifici
  :::
```

### 2. Fill Hopper

```{list-table}
* - **Grafico attivazioni tramoggia**
  - Rappresenta lo storico degli impulsi di scarico inviati alla tramoggia (Hopper), utile per monitorare l'autonomia del magazzino componenti.

* - **Caratteristiche**:
  - 
    - Asse X: Tempo
    - Asse Y: Attivazioni Hopper (eventi)
    - Picchi: Ogni picco rappresenta un'attivazione scarico

* - **Utilizzo**:
  - 
    - Prevedere quando ricaricare Hopper fisicamente
    - Verificare efficacia configurazione Hopper
    - Identificare anomalie nel comportamento scarico
```

```{tip}
  
  :::{list-table} **Analisi pattern Fill Hopper**

    * - **Attivazioni regolari e costanti**:
      - 
        - ✓ Configurazione Hopper ottimale
        - ✓ Flusso pezzi stabile e prevedibile
        - ✓ Autonomia calcolabile (es: attivazione ogni 10 min)

    * - **Attivazioni sempre più frequenti**:
      - 
        - ⚠️ Hopper si sta svuotando (meno pezzi = più attivazioni per mantenere livello)
        - ⚠️ Time scarico insufficiente per volume ridotto
        - **Azione**: Pianificare ricarica Hopper a breve

    * - **Nessuna attivazione per lungo periodo**:
      - 
        - ⚠️ Robot fermo o rallentato (pezzi non vengono consumati)
        - ⚠️ Possibile problema sistema che non richiede pezzi
        - **Azione**: Verificare stato produzione

    * - **Attivazioni molto ravvicinate (burst)**:
      - 
        - ⚠️ Soglia Hopper mal configurata (troppo alta)
        - ⚠️ Steps insufficienti (pezzi non arrivano in tempo)
        - **Azione**: Rivedere Config Hopper
  :::
```

### 3. Vision - FlexiBowl - Robot (Grafico Comparativo)

```{list-table} 
* - **Grafico tempi sovrapposti**
  - Un grafico comparativo a tre linee che sovrappone i tempi dei singoli processi nel tempo.

* - **Utilizzo**: 
  - Identificare istantaneamente quale processo influenza maggiormente il tempo di ciclo totale e come varia nel tempo.
```
---

## Monitoraggio Qualità - Indicatori critici da monitorare

```{list-table}
* - **Score dei componenti**
  - Assicurarsi che lo **Score** dei componenti rilevati sia costantemente sopra la soglia di tolleranza (Accept Threshold) impostata durante la configurazione modello.

* - **Monitoraggio Score**:
  - 
    - Controllare periodicamente tabella Modelli Rilevati
    - Verificare che score tipici siano 0.85-0.95
    - Investigare se score scendono sotto 0.80 regolarmente

* - **Score in diminuzione progressiva**:
  - 
    - ⚠️ Pezzi reali diversi da quello di training (variazioni produzione)
    - ⚠️ Illuminazione cambiata (backlight più debole, sporcizia)
    - ⚠️ Camera non più a fuoco (vibrazioni, urti)
    - ⚠️ Superficie FlexiBowl sporca (pattern interferente)

* - **Azioni correttive**:
  - 
    - Pulire camera, illuminazione, superficie FlexiBowl
    - Verificare messa a fuoco camera
    - Considerare re-training modello se pezzi sono cambiati
    - Ridurre Accept Threshold se score sono comunque affidabili ma più bassi
```
---

## Best Practices Monitoraggio Produttivo

### Check giornalieri

```{list-table}
* - **All'avvio produzione** (5 minuti):
  - 
    - Verificare indicatori connettività FlexiBowl e Robot (verdi)
    - Controllare che primi cicli mostrino score normali (>0.85)
    - Osservare che PPM si stabilizzi su valore atteso

* - **Durante produzione** (check ogni 1-2 ore):
  - 
    - Dare un'occhiata a PPM per verificare stabilità
    - Controllare Fill Hopper per prevedere ricarica necessaria
    - Verificare assenza errori o warning nel log

* - **A fine turno** (2 minuti):
  - 
    - Annotare PPM medio del turno
    - Controllare numero attivazioni Hopper
    - Verificare eventuali anomalie o eventi
    - Confrontare con dati giorno precedente
```
Questa routine minima garantisce identificazione rapida di problemi e mantiene tracciabilità performance.

### Report performance  

```{tip} **Metriche chiave da tracciare**
Per valutazione performance nel tempo, tracciare:

  :::{list-table} 

    * - **Giornalmente**:
      - 
        - PPM medio del turno
        - Numero pezzi totali prelevati
        - Numero attivazioni Hopper
        - Downtime totale (e cause)

    * - **Settimanalmente**:
      - 
        - Trend PPM (in aumento/diminuzione?)
        - Confronto PPM teorico vs reale
        - Score medio componenti rilevati
        - Eventuali modifiche configurazione e loro impatto

    * - **Mensilmente**:
      - 
        - Overall Equipment Effectiveness (OEE)
        - Analisi colli di bottiglia principali
        - Necessità di manutenzione predittiva
        - ROI del sistema
  :::

Questi dati permettono ottimizzazione continua e giustificano investimenti in miglioramenti.
```

---

```{tip}
**Sistema operativo completato!**

Congratulazioni! Il sistema FlexiVision One è ora completamente configurato, ottimizzato e validato per la produzione.

**Riepilogo percorso completato:**
- ✓ Setup hardware (FlexiBowl, Robot, Camera)
- ✓ Calibrazione completa (Camera, Robot)
- ✓ Modelli pezzo creati e ottimizzati
- ✓ FlexiBowl configurato per movimentazione ottimale
- ✓ Hopper configurato per alimentazione automatica (se presente)
- ✓ Sistema validato con monitoraggio Dashboard
- ✓ Performance verificate e stabili

Il sistema è pronto per operare in produzione con supervisione minima. Utilizzare la Dashboard per monitoraggio continuo e ottimizzazione nel tempo.

**Tempo totale investito**: 4-8 ore (primo sistema completo)

**Risultato**: Sistema di picking robotizzato completamente autonomo e ottimizzato!
```
---

Una volta validato il sistema tramite Dashboard:

**→ [Troubleshooting](../TROUBLESHOOTING/26_trb_shooting_guide.md)** - Guida risoluzione problemi comuni

**→ [Support](../27_Support.md)** - Contatti assistenza tecnica




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
      Language: <span class="current-value">FR</span>
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
