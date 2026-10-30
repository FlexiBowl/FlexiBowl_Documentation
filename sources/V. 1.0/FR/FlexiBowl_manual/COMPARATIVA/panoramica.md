# **Vue d'ensemble comparative**

## Qu'est-ce que FlexiBowl®

Le FlexiBowl® est un système flexible d'alimentation de composants dans des lignes automatisées utilisant des robots industriels et/ou collaboratifs. Grâce à la combinaison d'un mouvement rotatif et d'impulsions « flip », les pièces sont séparées et orientées pour être prélevées par le robot, quelles que soient leur géométrie, leur surface ou leur matière.

Ces caractéristiques fonctionnelles fondamentales restent inchangées entre la version 2.0 et la version 3.0.

---

## Approfondissements comparatifs

---

:::{raw} html

<script src="https://unpkg.com/@phosphor-icons/web"></script>

<div class="comp-workflow">
  <style>
    .comp-workflow {
      font-family: inherit;
      max-width: 680px;
      margin: 2.5rem auto;
      padding: 0 1rem;
    }
    .cw-step {
      display: flex;
      align-items: stretch;
      gap: 1.25rem;
      margin-bottom: 0;
    }
    .cw-step:hover .cw-card {
      border-color: #2980b9;
      background: #f0f7ff;
      transform: translateX(4px);
    }
    .cw-step:hover .cw-icon {
      background: #2980b9;
    }
    .cw-left {
      display: flex;
      flex-direction: column;
      align-items: center;
      flex-shrink: 0;
      width: 44px;
    }
    .cw-icon {
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: #3498db;
      color: #fff;
      font-size: 1.25rem;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      transition: background 0.2s;
    }
    .cw-connector {
      flex: 1;
      width: 3px;
      background: linear-gradient(to bottom, #3498db 0%, #bcd6ec 100%);
      margin: 6px auto 0;
      min-height: 32px;
    }
    .cw-last .cw-connector {
      display: none;
    }
    .cw-card {
      flex: 1;
      border: 1.5px solid #d0e4f0;
      border-radius: 10px;
      padding: 0.85rem 1.1rem;
      background: #fff;
      transition: border-color 0.2s, background 0.2s, transform 0.2s;
      margin-bottom: 0.65rem;
      text-decoration: none;
      display: block;
      color: inherit;
    }
    .cw-card-title {
      font-weight: 700;
      font-size: 1rem;
      color: #1a3a52;
      margin-bottom: 0.3rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }
    .cw-card-title i {
      font-size: 1.2rem;
      color: #1a3a52;
      flex-shrink: 0;
    }
    .cw-card-desc {
      font-size: 0.875rem;
      color: #556b7d;
      margin: 0;
      line-height: 1.45;
    }
    .cw-badge {
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
    .cw-badge:hover {
      background: #c6e0f5;
      color: #1a5f8a;
    }
  </style>

  <!-- Meccanica -->
  <div class="cw-step">
    <div class="cw-left">
      <div class="cw-icon"><i class="ph ph-wrench"></i></div>
      <div class="cw-connector"></div>
    </div>
    <a class="cw-card" href="comparativa_meccanica.html">
      <div class="cw-card-title">
        Comparatif mécanique
      </div>
      <p class="cw-card-desc">
        Comparaison des dimensions de construction (références A–K, zone backlight), des modèles disponibles et des capacités opérationnelles pour chaque taille.
      </p>
    </a>
  </div>

  <!-- Elettrica -->
  <div class="cw-step">
    <div class="cw-left">
      <div class="cw-icon"><i class="ph ph-plugs"></i></div>
      <div class="cw-connector"></div>
    </div>
    <a class="cw-card" href="comparativa_elettrica.html">
      <div class="cw-card-title">
        Comparatif électrique
      </div>
      <p class="cw-card-desc">
        Comparaison des composants électriques : alimentation, fusibles, carte d'interface, driver et moteur dans la version 2.0 ; automate intégré dans la version 3.0.
      </p>
    </a>
  </div>

  <!-- Pneumatica -->
  <div class="cw-step">
    <div class="cw-left">
      <div class="cw-icon"><i class="ph ph-wind"></i></div>
      <div class="cw-connector"></div>
    </div>
    <a class="cw-card" href="comparativa_pneumatica.html">
      <div class="cw-card-title">
        Comparatif pneumatique
      </div>
      <p class="cw-card-desc">
        Comparaison des schémas pneumatiques, des spécifications de l'air comprimé, des composants (flip, blow, vidage) et des variantes Clean Room.
      </p>
    </a>
  </div>

  <!-- Software -->
  <div class="cw-step cw-last">
    <div class="cw-left">
      <div class="cw-icon"><i class="ph ph-monitor"></i></div>
      <div class="cw-connector"></div>
    </div>
    <a class="cw-card" href="comparativa_software.html">
      <div class="cw-card-title">
        Comparatif logiciel
      </div>
      <p class="cw-card-desc">
        Comparaison de l'interface de configuration, de la gestion des paramètres de mouvement, de l'assistant de configuration et des modes de communication.
      </p>
    </a>
  </div>

</div>

:::