# **Motorized Hopper**

## Qu'est-ce qu'une Motorized Hopper ?
La Motorized Hopper est un élévateur à tapis à palettes, disponible en tailles de 50, 100 et 150 litres, conçu pour élever le matériau de bas en haut et le livrer à la sortie. C'est une **machine incomplète** : elle doit être incorporée dans une ligne qui en gère la logique de fonctionnement et les fonctions de sécurité.

*Plus d'informations sur les Motorized Hoppers seront bientôt disponibles.*

<!--
Modèles : TRM/MOT 50/100/150 D/S (version droite / gauche).

## Naviguer dans le manuel
Ce manuel est structuré comme un workflow séquentiel destiné à accompagner les techniciens, les installateurs et les opérateurs à travers toutes les phases de vie de la machine.

Voici chacune des pages :

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

  <div class="qs-step">
    <div class="qs-left">
      <div class="qs-number">1</div>
      <div class="qs-connector"></div>
    </div>
    <div class="qs-card">
      <div class="qs-card-title">
        <a class="qs-title-link" href="info_preliminari.html">Informations préliminaires et sécurité</a>
      </div>
      <p class="qs-card-desc">
       Introduction, glossaire, symboles, règles de sécurité, responsabilité du Constructeur, garantie, certification, conditions environnementales, dispositifs de sécurité et plaques apposées.
      </p>
    </div>
  </div>

  <div class="qs-step">
    <div class="qs-left">
      <div class="qs-number">2</div>
      <div class="qs-connector"></div>
    </div>
    <div class="qs-card">
      <div class="qs-card-title">
        <a class="qs-title-link" href="descrizione_macchina.html">Description de la machine</a>
      </div>
      <p class="qs-card-desc">
       Layout, données techniques des tailles de 50, 100 et 150 litres, dimensions d'encombrement et description du fonctionnement.
      </p>
    </div>
  </div>

  <div class="qs-step">
    <div class="qs-left">
      <div class="qs-number">3</div>
      <div class="qs-connector"></div>
    </div>
    <div class="qs-card">
      <div class="qs-card-title">
        <a class="qs-title-link" href="trasporto_installazione.html">Emballage, transport et installation</a>
      </div>
      <p class="qs-card-desc">
       Emballage, manutention et levage, contrôle de l'intégrité, installation, raccordements, contrôles préliminaires, couples de serrage et codes de recyclage.
      </p>
    </div>
  </div>

  <div class="qs-step">
    <div class="qs-left">
      <div class="qs-number">4</div>
      <div class="qs-connector"></div>
    </div>
    <div class="qs-card">
      <div class="qs-card-title">
        <a class="qs-title-link" href="uso.html">Utilisation</a>
      </div>
      <p class="qs-card-desc">
       Contrôles initiaux et cycle de travail de la machine.
      </p>
    </div>
  </div>

  <div class="qs-step">
    <div class="qs-left">
      <div class="qs-number">5</div>
      <div class="qs-connector"></div>
    </div>
    <div class="qs-card">
      <div class="qs-card-title">
        <a class="qs-title-link" href="manutenzione.html">Maintenance</a>
      </div>
      <p class="qs-card-desc">
       Précautions de sécurité, plan de maintenance et de lubrification, tension du tapis à palettes, procédure de remplacement du tapis, diagnostic des pannes et maintenance extraordinaire.
      </p>
    </div>
  </div>

  <div class="qs-step">
    <div class="qs-left">
      <div class="qs-number">6</div>
      <div class="qs-connector"></div>
    </div>
    <div class="qs-card">
      <div class="qs-card-title">
        <a class="qs-title-link" href="smaltimento_appendici.html">Élimination et annexes</a>
      </div>
      <p class="qs-card-desc">
       Procédures de démantèlement, stockage, recyclage et liste de la documentation annexée.
      </p>
    </div>
  </div>
</div>

:::{toctree}
:hidden:
info_preliminari.md
descrizione_macchina.md
trasporto_installazione.md
uso.md
manutenzione.md
smaltimento_appendici.md
:::
-->