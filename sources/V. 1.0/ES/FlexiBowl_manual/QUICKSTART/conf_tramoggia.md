# **Configuración del Bulk Feeder**


Esta página le guía en la puesta en marcha del Bulk Feeder vibratorio, el accesorio opcional que alimenta el FlexiBowl® de forma continua y uniforme. Siga las cuatro fases en secuencia: posicionamiento y montaje mecánico, conexiones eléctricas, ajuste de la dirección de comunicación y configuración de los parámetros desde la interfaz de software.

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
  </style>

  <!-- Step 1 -->
  <div class="qs-step">
    <div class="qs-left">
      <div class="qs-number">1</div>
      <div class="qs-connector"></div>
    </div>
    <div class="qs-card">
      <div class="qs-card-title">
        <i class="ph ph-package"></i>
        <a class="qs-title-link" href="conf_tramoggia.html#posizionamento-e-installazione-meccanica">Posicionamiento e instalación mecánica</a>
      </div>
      <p class="qs-card-desc">
        Coloque el Bulk Feeder respetando la orientación correcta respecto al FlexiBowl® y fíjelo al soporte.
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
        <a class="qs-title-link" href="conf_tramoggia.html#collegamenti-elettrici">Conexiones eléctricas</a>
      </div>
      <p class="qs-card-desc">
        Conecte el controlador al Bulk Feeder, al FlexiBowl® (o al rack) y a la alimentación, respetando el orden de conexión.
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
        <i class="ph ph-hash"></i>
        <a class="qs-title-link" href="conf_tramoggia.html#indirizzo-di-comunicazione-rs485">Dirección de comunicación RS485</a>
      </div>
      <p class="qs-card-desc">
        Desde el panel del controlador, establezca una dirección única, necesaria para comunicarse con el FlexiBowl® y con otros posibles Bulk Feeder.
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
        <i class="ph ph-hash"></i>
        <a class="qs-title-link" href="conf_tramoggia.html#configurazione-da-interfaccia-software">Configuración desde la interfaz de software</a>
      </div>
      <p class="qs-card-desc">
        Active el Bulk Feeder desde la interfaz web del FlexiBowl® y ajuste la amplitud, la frecuencia y el tiempo de activación de la vibración.
      </p>
    </div>
  </div>
</div>

---

## 1. Posicionamiento e instalación mecánica

Los Bulk Feeder están disponibles en diferentes tamaños, cada uno con su propia carga máxima:

| Capacidad | Carga máxima |
|---|---|
| 1,5 l | 1 kg |
| 3 l | 1,5 kg |
| 5 l | 6 kg |
| 10 l | 6 kg |
| 20 l | 6 kg |
| 40 l | 15 kg |

El Bulk Feeder llega ya montado: no es necesario ensamblarlo, solo colocarlo y fijarlo.

::::{tab-set}
:::{tab-item} Posicionamiento correcto
![Posicionamiento correcto del Bulk Feeder respecto al FlexiBowl®](../../../../_shared/media/images/posizione_giustatramoggia.png)

La rampa del Bulk Feeder debe descargar los componentes directamente en la zona de trabajo del plato, con una inclinación que siga el perfil del FlexiBowl®.
:::
:::{tab-item} Posicionamiento incorrecto
![Ejemplo de posicionamiento incorrecto del Bulk Feeder](../../../../_shared/media/images/posizione_sbagliatatramoggia.png)

Una rampa demasiado alejada del área de trabajo genera una alimentación irregular y penaliza el rendimiento de la aplicación.
:::
::::

**Pasos:**

1. Coloque el Bulk Feeder sobre una superficie estable y horizontal, cerca del FlexiBowl®, respetando la orientación correcta indicada arriba.
2. Si el Bulk Feeder se instala sobre la superficie de una máquina sensible a las vibraciones, interponga un material aislante y antivibratorio entre ambas superficies para evitar que las vibraciones del Bulk Feeder se transmitan al FlexiBowl®.
3. Fije el Bulk Feeder al soporte mediante los orificios previstos, utilizando tornillos M8: el Bulk Feeder estándar tiene 4 orificios en la base, mientras que la versión más pequeña (1,5 l) tiene 2.

## 2. Conexiones eléctricas

:::{warning}
Antes de realizar o modificar cualquier conexión eléctrica, asegúrese de que el sistema esté apagado. Compruebe siempre que el conductor de tierra esté correctamente instalado e íntegro: la conexión eléctrica, incluida la puesta a tierra, debe estar siempre garantizada para el correcto funcionamiento de la máquina.
:::

![Esquema de los conectores del controlador del Bulk Feeder](../../../../_shared/media/images/controller_digitale_connettori.png)

El controlador del Bulk Feeder dispone de: entrada de alimentación de red (tierra, fase, neutro), conector RS485 para la comunicación (A+, B-, GND), salida de potencia hacia el motor del Bulk Feeder e interruptor general.

**Pasos:**

1. Conecte el controlador al Bulk Feeder mediante el cable dedicado.
2. Conecte el controlador al FlexiBowl® mediante el conector M12 con codificación A (comunicación Modbus RTU). En instalaciones multi-feeder con rack, conecte en su lugar el controlador al rack.
3. Tape cualquier conector no utilizado con el capuchón correspondiente, para protegerlo del polvo y los residuos. El capuchón debe garantizar una resistencia de 120 Ω entre los canales A+ y B- de la línea RS485.
4. Conecte el cable de alimentación al controlador: conecte siempre primero el lado del controlador del cable, antes de conectar el otro extremo.
5. Con el interruptor del controlador en posición OFF, conecte el cable de alimentación a la toma de red. La alimentación estándar es de 115 o 230 VAC ±5 % (la versión de 115 V solo está disponible bajo petición expresa).
6. Encienda el controlador con el interruptor general.

:::{tip}
El cable Modbus RTU entre el controlador y el FlexiBowl® está disponible en longitudes de 3, 5 y 10 m: véase {ref}`cavo-modbus`.
:::

:::{note}
Un único FlexiBowl® admite hasta **4 Bulk Feeder**. Para instalaciones multi-feeder, conecte cada Bulk Feeder a su propio controlador, conecte el primer controlador al FlexiBowl® (o al rack) y encadene los controladores siguientes a través del puerto del conector Bulk Feeder (daisy-chain). Tape el puerto no utilizado del último controlador de la cadena y conecte el cable de alimentación a cada controlador.
:::

## 3. Dirección de comunicación RS485

Cada controlador de Bulk Feeder debe tener una dirección de comunicación única en la red RS485 (parámetro **r**, rango 1–31). Si hay varios Bulk Feeder, asegúrese de que cada controlador de la misma red tenga una dirección distinta.

![Panel frontal del controlador: indicadores, pantalla y mandos](../../../../_shared/media/images/tramoggia-pannello-controller.jpg)


**Pasos desde el panel del controlador:**

1. Mantenga pulsado **FUNC** durante 2 segundos para entrar en el estado de ajuste de los parámetros básicos.
2. Pulse repetidamente **FUNC** para seleccionar el parámetro **r** (dirección de comunicación).
3. Pulse **▲** o **▼** para modificar el valor (1–31).
4. Mantenga pulsado de nuevo **FUNC** durante 2 segundos para salir y guardar.

## 4. Configuración desde la interfaz de software

Una vez completadas las conexiones y establecida la dirección, el Bulk Feeder puede configurarse y controlarse desde la página dedicada de la interfaz web del FlexiBowl®.

![Interfaz de software de configuración de los Bulk Feeder](../../../../_shared/media/images/tramoggia-interfaccia-software.png)

Para cada uno de los 4 Bulk Feeder disponibles se puede configurar:

| Campo | Descripción |
|---|---|
| **Enable** | Activa el Bulk Feeder correspondiente. |
| **ID** | Dirección RS485 del controlador conectado; use **Set New ID** para asignar una nueva por software. |
| **Status** | Estado actual del Bulk Feeder (p. ej., Disabled). |
| **Amplitude** | Amplitud de la vibración. |
| **Frequency** | Frecuencia de la vibración. |
| **Activation Time** | Duración, en milisegundos, de cada impulso de vibración. |

**Pasos:**

1. Acceda a la interfaz web del FlexiBowl® y abra la página de los Bulk Feeder.
2. Seleccione **Enable** en el Bulk Feeder que desea activar.
3. Compruebe que el campo **ID** coincida con la dirección establecida en el controlador (paso 3); de lo contrario, use **Set New ID**.
4. Establezca los valores iniciales de **Amplitude**, **Frequency** y **Activation Time** según el componente que se vaya a alimentar.
5. Pulse **Start Hopper** para arrancar el Bulk Feeder y comprobar su funcionamiento; ajuste los parámetros hasta que la alimentación de los componentes sea continua y uniforme.

:::{note}
Los valores óptimos de amplitud, frecuencia y tiempo de activación dependen del componente y de la geometría del Bulk Feeder: ajústelos progresivamente observando el flujo de alimentación, partiendo de valores bajos y aumentando hasta obtener una alimentación constante sin atascos.
:::

## Parámetros avanzados del controlador 

### **Parámetros comunes** 
Los parámetros comunes se pueden ajustar en cualquier momento con las teclas **Vol+** / **Vol-**, incluso mientras se muestra otro parámetro:

![Parámetros comunes del controlador](../../../../_shared/media/images/tramoggia-parametri-comuni.png)

| Definición | Símbolo | Rango | Predeterminado |
|---|---|---|---|
| Tensión de salida | U | 0–260 V | 50 |

### **Parámetros básicos**
Para acceder a los parámetros básicos, mantenga pulsado **FUNC** durante 2 segundos; pulse **FUNC** para desplazarse por los parámetros, **▲/▼** para modificarlos y mantenga pulsado **FUNC** durante 2 segundos para salir:

![Parámetros básicos del controlador](../../../../_shared/media/images/tramoggia-parametri-base.png)

| Definición | Símbolo | Rango | Predeterminado |
|---|---|---|---|
| Frecuencia de salida | E | 40,0–200,0 Hz | 100,0 |
| Tensión de salida máxima ajustable | h | 0–260 V | 260 |
| Dirección de comunicación | r | 1–31 | 1 |
| Velocidad de transmisión (baud rate) de la comunicación | c | 0,3–115,2 kbps | 115,2 |
| Reinicio del controlador | — | — | — |

### **Reinicio del controlador**

![Procedimiento de reinicio del controlador](../../../../_shared/media/images/tramoggia-reset-controller.png)

1. Mantenga pulsado **FUNC** durante 2 segundos para entrar en el estado de ajuste de los parámetros básicos.
2. Pulse **FUNC** hasta que el parámetro de reinicio (`88888`) parpadee en la pantalla.
3. Mantenga pulsado **▲** hasta que aparezca `-----` en la pantalla.
4. Suelte **▲** para completar el reinicio: la pantalla mostrará `U 50`, confirmando que la operación se ha realizado con éxito.


