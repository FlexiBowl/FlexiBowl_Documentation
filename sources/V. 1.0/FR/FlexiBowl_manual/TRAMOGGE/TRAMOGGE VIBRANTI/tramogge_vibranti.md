# **Bulk Feeder**

## Qu'est-ce qu'un Bulk Feeder ?
Le Bulk Feeder vibrant est un dispositif industriel de stockage et d'alimentation conçu pour contenir des composants et les doser de manière continue et uniforme vers le FlexiBowl.

## Naviguer dans le manuel
Ce manuel est structuré comme un véritable workflow séquentiel conçu pour accompagner les techniciens, les installateurs et les opérateurs à travers toutes les phases de vie de la machine.

Voici chacune des pages :

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
        <a class="qs-title-link" href="info_preliminari.html">Informations préliminaires</a>
      </div>
      <p class="qs-card-desc">
        Contient des informations importantes telles que les avertissements généraux de sécurité et les critères de qualification de l'opérateur, ainsi que les données d'identification officielles du constructeur et du marquage CE. Définit de manière claire et contraignante les limites d'utilisation prévues du Bulk Feeder (but et domaine d'application) et la liste des usages non autorisés ou potentiellement dangereux.
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
        <a class="qs-title-link" href="descrizione_macchina.html">Description de la machine </a>
      </div>
      <p class="qs-card-desc">
       Elle décrit les ensembles principaux qui composent la structure, ainsi que les fiches de données techniques nominales (dimensions, poids, tensions et capacité de charge) utiles pour comprendre les limites de performance du système.
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
        <a class="qs-title-link" href="trasporto_installazione.html">Transport et installation </a>
      </div>
      <p class="qs-card-desc">
        Précise les lignes directrices pour la réception et le déballage de la machine, les procédures de levage et de manutention sécurisée des charges dans la zone de travail, et les exigences mécaniques pour la fixation et la mise à niveau correctes du Bulk Feeder sur la structure de support.
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
        <a class="qs-title-link" href="controller_cablaggio.html">Contrôleur et câblage</a>
      </div>
      <p class="qs-card-desc">
        Illustre les schémas électriques et les modalités d'interconnexion entre l'électroaimant du Bulk Feeder et l'unité de commande externe, en définissant la configuration des signaux logiques, l'étalonnage des fréquences de vibration et l'interface avec les API de ligne.
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
        <a class="qs-title-link" href="manutenzione.html">Maintenance et dépannage </a>
      </div>
      <p class="qs-card-desc">
       Présente le plan des contrôles périodiques (nettoyage, serrages structurels), les procédures d'étalonnage mécanique avancé — comme le réglage millimétrique de l'entrefer du stator — et les tableaux de diagnostic pour l'isolement et la résolution rapide des pannes.
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
        <a class="qs-title-link" href="smaltimento_appendici.html">Mise hors service et élimination </a>
      </div>
      <p class="qs-card-desc">
       Décrit les mesures de sécurité nécessaires à l'arrêt et au stockage du Bulk Feeder pendant les périodes d'inactivité prolongée, ainsi que les procédures de démontage et les exigences environnementales (Directive DEEE) pour le recyclage contrôlé des matériaux en fin de vie.
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
accessori_opzioni.md
:::