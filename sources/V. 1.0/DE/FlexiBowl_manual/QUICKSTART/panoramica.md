# **Übersicht der Arbeitsschritte**
Diese Seite bietet einen Überblick über den Konfigurations- und Inbetriebnahmeprozess des FlexiBowl®. Der folgende Workflow zeigt die wichtigsten Schritte in der richtigen Reihenfolge: Klicken Sie auf einen Schritt, um die zugehörige Seite zu öffnen.

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
        <a class="qs-title-link" href="installazione_meccanica.html">Installation des FlexiBowl®</a>
        <a class="qs-badge" href="../DATI TECNICI/02_dati-tecnici-meccanici.html">Mechanik</a>
      </div>
      <p class="qs-card-desc">
        Positionieren und befestigen Sie den FlexiBowl® auf einer stabilen, waagerechten Fläche und beachten Sie dabei die Ebenheitstoleranzen und die Maßvorgaben für die Auflage.
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
        <a class="qs-title-link" href="cablaggio_FB.html">Verdrahtung des FlexiBowl®</a>
        <a class="qs-badge" href="../DATI TECNICI/03_dati-tecnici-elettrici.html">Elektrik</a>
      </div>
      <p class="qs-card-desc">
        Stellen Sie die elektrischen Anschlüsse gemäß den Anweisungen für das verwendete Modell her (200/350 über externe Box; 500–1200 am integrierten Schaltfeld).
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
        <a class="qs-title-link" href="conf_interfaccia.html">Konfiguration der Benutzeroberfläche</a>
        <a class="qs-badge" href="../INSTALLAZIONE/04_interfaccia-software.html">Software</a>
      </div>
      <p class="qs-card-desc">
        Rufen Sie die FlexiBowl®-Weboberfläche auf, konfigurieren Sie die IP-Adresse und die Kommunikationsart und aktivieren Sie bei Bedarf das Backlight zur Kalibrierung des Bildverarbeitungssystems.
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
        Nutzen Sie die geführte Konfiguration, um das zuzuführende Bauteil zu charakterisieren (Geometrie, Überlappung), die Zubehörteile (Air-Blow, Flip) zu testen und die optimalen Bewegungs- und Schüttelparameter automatisch zu erzeugen.
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
        <a class="qs-title-link" href="conf_tramoggia.html">Konfiguration des Bulk Feeders</a>
      </div>
      <p class="qs-card-desc">
        Nutzen Sie die geführte Konfiguration, um das Verhalten des Bulk Feeders zu charakterisieren.
      </p>
    </div>
  </div>
</div>

:::{note}
Wenn das verwendete System **FlexiVision One** ist, wird die Phase der Konfiguration der Benutzeroberfläche direkt über die zugehörige Oberfläche abgewickelt. Siehe FlexiVision One Handbuch.
:::
