# **Motorized Hopper**

## ¿Qué es una Motorized Hopper?
La Motorized Hopper es un elevador de cinta de paletas, disponible en tamaños de 50, 100 y 150 litros, diseñado para elevar el material de abajo arriba y entregarlo en la salida. Es una **cuasi máquina**: debe incorporarse a una línea que gestione su lógica de funcionamiento y sus funciones de seguridad.

*Próximamente habrá más información sobre las Motorized Hoppers.*

<!--
Modelos: TRM/MOT 50/100/150 D/S (versión derecha / izquierda).

## Navegar por el manual
Este manual está estructurado como un flujo de trabajo secuencial pensado para acompañar a técnicos, instaladores y operadores a lo largo de todas las fases de vida de la maquinaria.

Estas son las páginas:

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
        <a class="qs-title-link" href="info_preliminari.html">Información preliminar y seguridad</a>
      </div>
      <p class="qs-card-desc">
       Introducción, glosario, símbolos, normas de seguridad, responsabilidad del Fabricante, garantía, certificación, condiciones ambientales, dispositivos de seguridad y placas aplicadas.
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
        <a class="qs-title-link" href="descrizione_macchina.html">Descripción de la máquina</a>
      </div>
      <p class="qs-card-desc">
       Layout, datos técnicos de los tamaños de 50, 100 y 150 litros, dimensiones de ocupación y descripción del funcionamiento.
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
        <a class="qs-title-link" href="trasporto_installazione.html">Embalaje, transporte e instalación</a>
      </div>
      <p class="qs-card-desc">
       Embalaje, manipulación y elevación, control de la integridad, instalación, conexiones, controles preliminares, pares de apriete y códigos de reciclaje.
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
        <a class="qs-title-link" href="uso.html">Uso</a>
      </div>
      <p class="qs-card-desc">
       Controles iniciales y ciclo de trabajo de la máquina.
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
        <a class="qs-title-link" href="manutenzione.html">Mantenimiento</a>
      </div>
      <p class="qs-card-desc">
       Precauciones de seguridad, plan de mantenimiento y lubricación, tensado de la cinta de paletas, procedimiento de sustitución de la cinta, diagnóstico de averías y mantenimiento extraordinario.
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
        <a class="qs-title-link" href="smaltimento_appendici.html">Eliminación y anexos</a>
      </div>
      <p class="qs-card-desc">
       Procedimientos de desmantelamiento, almacenamiento, reciclaje y lista de la documentación adjunta.
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