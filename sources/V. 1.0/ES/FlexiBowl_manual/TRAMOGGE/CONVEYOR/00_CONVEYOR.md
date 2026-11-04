# **Conveyor Hopper**

## ¿Qué es la Conveyor Hopper?
La Conveyor Hopper CH60 es una tolva de 60 litros con cinta transportadora motorizada, diseñada para recibir componentes a granel de un sistema aguas arriba y transferirlos a un sistema aguas abajo. Es una **cuasi máquina**: debe incorporarse a una línea que gestione su lógica de funcionamiento y sus funciones de seguridad.

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
       Identificación de la máquina, declaración de incorporación, directivas, cualificación de los operadores, símbolos, EPI, garantía, dispositivos de seguridad, ruido, riesgos residuales y pictogramas.
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
       Describe la Conveyor Hopper CH60, el uso previsto y el uso incorrecto, las obligaciones y prohibiciones, los datos técnicos, las dimensiones de ocupación, los componentes principales y el ciclo de trabajo.
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
        <a class="qs-title-link" href="trasporto_installazione.html">Transporte e incorporación</a>
      </div>
      <p class="qs-card-desc">
       Embalaje, manipulación, condiciones ambientales permitidas, montaje, posicionamiento y conexión eléctrica.
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
       Controles preliminares e indicaciones para el uso de la máquina dentro de la línea.
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
       Plan de mantenimiento ordinario (controles, limpieza, lubricación) y procedimiento de sustitución del tejido de la cinta.
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
        <a class="qs-title-link" href="smaltimento_appendici.html">Puesta fuera de servicio, eliminación y anexos</a>
      </div>
      <p class="qs-card-desc">
       Procedimiento de puesta fuera de servicio y de eliminación por material, y lista de anexos.
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
