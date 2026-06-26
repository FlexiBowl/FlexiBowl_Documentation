# **Vibrant Hoppers**

## Cosa è una tramoggia vibrante?
La tramoggia vibrante è un dispositivo industriale di stoccaggio e alimentazione progettato per contenere componenti e dosarli in modo continuo e uniforme verso il FlexiBowl.

## Navigare il Manuale
Questo manuale è strutturato come un vero e proprio workflow sequenziale pensato per accompagnare i tecnici, gli installatori e gli operatori attraverso tutte le fasi di vita del macchinario.

Ecco ciascuna delle pagine: 

<script src="https://unpkg.com/@phosphor-icons/web"></script>

<div class="quickstart-workflow">
  <style>
    .quickstart-workflow {
      font-family: inherit;
      max-width: 680px;
      margin: 2.5rem auto;
      padding: 0 1rem;
    }

    .qs-step {
      display: flex;
      align-items: stretch;
      gap: 1.25rem;
      margin-bottom: 0;
    }

    .qs-step:hover .qs-card {
      border-color: #2980b9;
      background: #f0f7ff;
      transform: translateX(4px);
    }

    .qs-step:hover .qs-number {
      background: #2980b9;
    }

    .qs-left {
      display: flex;
      flex-direction: column;
      align-items: center;
      flex-shrink: 0;
      width: 44px;
    }

    .qs-number {
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: #3498db;
      color: #fff;
      font-weight: 700;
      font-size: 1rem;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      transition: background 0.2s;
    }

    .qs-connector {
      flex: 1;
      width: 3px;
      background: linear-gradient(to bottom, #3498db 0%, #bcd6ec 100%);
      margin: 6px auto 0;
      min-height: 32px;
    }

    .qs-last .qs-connector {
      display: none;
    }

    .qs-card {
      flex: 1;
      border: 1.5px solid #d0e4f0;
      border-radius: 10px;
      padding: 0.85rem 1.1rem;
      background: #fff;
      transition: border-color 0.2s, background 0.2s, transform 0.2s;
      margin-bottom: 0.65rem;
    }

    .qs-card-title {
      font-weight: 700;
      font-size: 1rem;
      color: #1a3a52;
      margin-bottom: 0.3rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .qs-card-title i {
      font-size: 1.2rem;
      color: #1a3a52;
      flex-shrink: 0;
    }

    .qs-title-link {
      color: inherit;
      text-decoration: none;
    }

    .qs-title-link:hover {
      color: #2980b9;
      text-decoration: none;
    }

    .qs-card-desc {
      font-size: 0.875rem;
      color: #556b7d;
      margin: 0;
      line-height: 1.45;
    }

    .qs-badge {
      display: inline-block;
      font-size: 0.7rem;
      font-weight: 600;
      color: #2980b9;
      background: #e3f1fb;
      border-radius: 4px;
      padding: 1px 7px;
      margin-left: auto;
      white-space: nowrap;
      text-decoration: underline;
      cursor: pointer;
    }

    .qs-badge:hover {
      background: #c6e0f5;
      color: #1a5f8a;
    }
  </style>

  <!-- Step 1 -->
  <div class="qs-step">
    <div class="qs-left">
      <div class="qs-number">1</div>
    <div class="qs-connector"></div>
    </div>
    <div class="qs-card">
      <div class="qs-card-title">
        <a class="qs-title-link" href="info_preliminari.html">Informazioni Preliminari</a>
      </div>
      <p class="qs-card-desc">
        Contiene informazioni importanti come le avvertenze generali sulla sicurezza e i criteri di qualificazione dell'operatore, insieme ai dati di identificazione ufficiale del costruttore e della marcatura CE. Definisce in modo chiaro e vincolante i limiti d'uso previsti della tramoggia (scopo e campo di applicazione) e l'elenco degli usi non consentiti o potenzialmente pericolosi.
      </p>
    </div>
  </div>

  <!-- Step 2 -->
  <div class="qs-step">
    <div class="qs-left">
      <div class="qs-number">2</div>
      <div class="qs-connector"></div>
    </div>
    <div class="qs-card">
      <div class="qs-card-title">
        <a class="qs-title-link" href="descrizione_macchina.html">Descrizione Macchina </a>
      </div>
      <p class="qs-card-desc">
       Al suo interno sono descritti i gruppi principali che compongono la struttura, insieme alle schede dei dati tecnici nominali (dimensioni, pesi, tensioni e capacità di carico) utili per comprendere i limiti prestazionali del sistema.
      </p>
    </div>
  </div>

  <!-- Step 3 -->
  <div class="qs-step">
    <div class="qs-left">
      <div class="qs-number">3</div>
      <div class="qs-connector"></div>
    </div>
    <div class="qs-card">
      <div class="qs-card-title">
        <a class="qs-title-link" href="trasporto_installazione.html">Trasporto e Installazione </a>
      </div>
      <p class="qs-card-desc">
        Specifica le linee guida per la ricezione e il disimballo del macchinario, le procedure per il sollevamento e la movimentazione sicura dei pesi nell'area di lavoro, e i requisiti meccanici per il corretto fissaggio e livellamento della tramoggia sulla struttura di supporto.
      </p>
    </div>
  </div>

  <!-- Step 4 -->
  <div class="qs-step">
    <div class="qs-left">
      <div class="qs-number">4</div>
      <div class="qs-connector"></div>
    </div>
    <div class="qs-card">
      <div class="qs-card-title">
        <a class="qs-title-link" href="controller_cablaggio.html">Controller e Cablaggio</a>
      </div>
      <p class="qs-card-desc">
        Illustra gli schemi elettrici e le modalità di interconnessione tra l'elettromagnete della tramoggia e l'unità di controllo esterna, definendo la configurazione dei segnali logici, la taratura delle frequenze di vibrazione e l'interfaccia con i PLC di linea.
      </p>
    </div>
  </div>

  <!-- Step 5 -->
  <div class="qs-step">
    <div class="qs-left">
      <div class="qs-number">5</div>
      <div class="qs-connector"></div>
    </div>
    <div class="qs-card">
      <div class="qs-card-title">
        <a class="qs-title-link" href="manutenzione.html">Manutenzione e Risoluzione Problemi </a>
      </div>
      <p class="qs-card-desc">
       Riporta il piano dei controlli periodici (pulizia, serraggi strutturali), le procedure di taratura meccanica avanzata — come la regolazione millimetrica del traferro dello statore — e le tabelle diagnostiche per l'isolamento e la risoluzione rapida dei guasti.
      </p>
    </div>
  </div>
      <!-- Step 6 -->
  <div class="qs-step">
    <div class="qs-left">
      <div class="qs-number">6</div>
      <div class="qs-connector"></div>
    </div>
    <div class="qs-card">
      <div class="qs-card-title">
        <a class="qs-title-link" href="smaltimento_appendici.html">Messa fuori servizio e Smaltimento </a>
      </div>
      <p class="qs-card-desc">
       Descrive le misure di sicurezza necessarie per l'arresto e l'immagazzinamento della tramoggia nei periodi di inattività prolungata, insieme alle procedure di smontaggio e ai requisiti ambientali (Direttiva RAEE) per il riciclo controllato dei materiali a fine vita.
      </p>
    </div>
  </div>
</div>

:::{toctree}
:hidden:
info_preliminari.md
descrizione_macchina.md
trasporto_installazione.md
controller_cablaggio.md
manutenzione.md
smaltimento_appendici.md
:::