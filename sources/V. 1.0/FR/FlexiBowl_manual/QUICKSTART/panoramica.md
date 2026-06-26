# **Aperçu des opérations**
Questa pagina fornisce una visione d'insieme del processo di configurazione e messa in funzione del FlexiBowl®. Il workflow seguente illustra i passaggi principali in sequenza: clicca su ciascuno step per accedere alla pagina dedicata.

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
        <i class="ph ph-wrench"></i>
        <a class="qs-title-link" href="installazione_meccanica.html">Installazione del FlexiBowl®</a>
        <a class="qs-badge" href="../DATI TECNICI/02_dati-tecnici-meccanici.html">Meccanica</a>
      </div>
      <p class="qs-card-desc">
        Posizionare e fissare il FlexiBowl® su un piano stabile e orizzontale, rispettando le tolleranze di planarità e i requisiti dimensionali del supporto.
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
        <i class="ph ph-plugs"></i>
        <a class="qs-title-link" href="cablaggio_FB.html">Cablaggio del FlexiBowl®</a>
        <a class="qs-badge" href="../DATI TECNICI/03_dati-tecnici-elettrici.html">Elettrica</a>
      </div>
      <p class="qs-card-desc">
        Eseguire i collegamenti elettrici seguendo le istruzioni specifiche per il modello in uso (200/350 tramite box esterno; 500–1200 sul pannello integrato).
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
        <i class="ph ph-monitor"></i>
        <a class="qs-title-link" href="conf_interfaccia.html">Configurazione Interfaccia</a>
        <a class="qs-badge" href="../INSTALLAZIONE/04_interfaccia-software.html">Software</a>
      </div>
      <p class="qs-card-desc">
        Accedere all'interfaccia web del FlexiBowl®, configurare l'indirizzo IP, il tipo di comunicazione e, se necessario, abilitare il backlight per la calibrazione del sistema di visione.
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
        <i class="ph ph-sliders"></i>
        <a class="qs-title-link" href="FB_wizard.html">FlexiBowl® Wizard</a>
      </div>
      <p class="qs-card-desc">
        Utilizzare la configurazione guidata per caratterizzare il componente da alimentare (geometria, sovrapposizione), testare gli accessori (air-blow, flip) e generare automaticamente i parametri ottimali di movimento e scuotimento.
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
        <i class="ph ph-sliders"></i>
        <a class="qs-title-link" href="conf_tramoggia.html">Configurazione Tramoggia</a>
      </div>
      <p class="qs-card-desc">
        Utilizzare la configurazione guidata per caratterizzare il comportamento della tramoggia.
      </p>
    </div>
  </div>
</div>

:::{note}
Se il sistema in uso è **FlexiVision One**, la fase di Configurazione Interfaccia viene gestita direttamente dalla sua interfaccia dedicata. Fare riferimento al Manuale FlexiVision One.
:::
