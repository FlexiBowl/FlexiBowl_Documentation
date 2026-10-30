# **Bulk Feeder**

## ¿Qué es un Bulk Feeder?
El Bulk Feeder vibratorio es un dispositivo industrial de almacenamiento y alimentación diseñado para contener componentes y dosificarlos de forma continua y uniforme hacia el FlexiBowl.

## Navegar por el manual
Este manual está estructurado como un verdadero flujo de trabajo secuencial pensado para acompañar a técnicos, instaladores y operadores a lo largo de todas las fases de vida de la máquina.

Estas son las páginas:

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
        <a class="qs-title-link" href="info_preliminari.html">Información preliminar</a>
      </div>
      <p class="qs-card-desc">
        Contiene información importante como las advertencias generales de seguridad y los criterios de cualificación del operador, junto con los datos oficiales de identificación del fabricante y del marcado CE. Define de forma clara y vinculante los límites de uso previstos del Bulk Feeder (finalidad y ámbito de aplicación) y la lista de usos no permitidos o potencialmente peligrosos.
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
        <a class="qs-title-link" href="descrizione_macchina.html">Descripción de la máquina </a>
      </div>
      <p class="qs-card-desc">
       En ella se describen los grupos principales que componen la estructura, junto con las fichas de datos técnicos nominales (dimensiones, pesos, tensiones y capacidad de carga) útiles para comprender los límites de prestaciones del sistema.
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
        <a class="qs-title-link" href="trasporto_installazione.html">Transporte e instalación </a>
      </div>
      <p class="qs-card-desc">
        Especifica las directrices para la recepción y el desembalaje de la maquinaria, los procedimientos para la elevación y manipulación seguras de cargas en el área de trabajo y los requisitos mecánicos para la correcta fijación y nivelación del Bulk Feeder sobre la estructura de soporte.
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
        <a class="qs-title-link" href="controller_cablaggio.html">Controlador y cableado</a>
      </div>
      <p class="qs-card-desc">
        Ilustra los esquemas eléctricos y las modalidades de interconexión entre el electroimán del Bulk Feeder y la unidad de control externa, definiendo la configuración de las señales lógicas, el calibrado de las frecuencias de vibración y la interfaz con los PLC de línea.
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
        <a class="qs-title-link" href="manutenzione.html">Mantenimiento y resolución de problemas </a>
      </div>
      <p class="qs-card-desc">
       Recoge el plan de controles periódicos (limpieza, apriete de elementos estructurales), los procedimientos de calibrado mecánico avanzado — como el ajuste milimétrico del entrehierro del estátor — y las tablas de diagnóstico para el aislamiento y la resolución rápida de averías.
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
        <a class="qs-title-link" href="smaltimento_appendici.html">Puesta fuera de servicio y eliminación </a>
      </div>
      <p class="qs-card-desc">
       Describe las medidas de seguridad necesarias para la parada y el almacenamiento del Bulk Feeder durante periodos de inactividad prolongada, junto con los procedimientos de desmontaje y los requisitos medioambientales (Directiva RAEE) para el reciclaje controlado de los materiales al final de su vida útil.
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