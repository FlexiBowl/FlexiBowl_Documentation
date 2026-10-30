(tracking)=
# **Modo Circular Tracking**

## Funcionamiento en Tracking

La opción **Circular Tracking** permite maximizar la productividad del FlexiBowl® haciéndolo girar de forma continua y sin interrupciones.
 En lugar de detenerse en cada ciclo para tomar la foto y dar al robot tiempo para recoger las piezas presentes en el área de visión, un encoder realiza el seguimiento del ángulo de rotación recorrido por la superficie del disco rígido desde el momento de la captura de la foto hasta el momento en que el robot toma la pieza.

:::{figure} ../../../../_shared/media/images/Tracking.png
:width: 50%
:align: center
:::

:::{image} ../../../../_shared/media/videos/TRACKING_MODE.GIF
:width: 100%
:align: center
:::

::::{tip}
El funcionamiento en circular tracking desplaza el área de toma que, si normalmente coincide con la de visión, en este caso quedará desplazada aguas abajo.
 Consulte el capítulo {ref}`Layout Best Practice <layoutbp>` para más información sobre la colocación recomendada del robot y de los demás accesorios en funcionamiento estándar y Circular Tracking.

:::{figure} ../../../../_shared/media/images/TrackingLayout.PNG
:width: 80%
:align: center
:::

::::
---

## Características principales

<div class="tracking-features">

| Característica | Descripción |
|---|---|
| **Rendimiento** | Ideal para maximizar el rendimiento (hasta el 100 %) |
| **Área de visión** | Un sector por delante del área de toma |
| **Paralelismo** | Descarga del hopper, movimiento/impulso del FlexiBowl®, visión y recogida ejecutándose simultáneamente |
| **Estabilidad** | Mayor estabilidad del tiempo de ciclo instantáneo |
| **Precisión** | Menor precisión que en el modo estándar |

</div>

---

## Ciclo operativo

El funcionamiento en circular tracking se basa en un ciclo continuo dividido en cuatro fases que se desarrollan en paralelo:

```{list-table}
:header-rows: 1
:widths: 20 80

* - Fase
  - Descripción
* - **Detect**
  - La cámara captura la imagen de un sector del FlexiBowl®, anticipándose al área de toma.
* - **Move**
  - El bowl gira de forma continua, sin detenerse; el encoder registra el desplazamiento angular en tiempo real.
* - **Flip / Drop**
  - Las piezas que no están correctamente orientadas se voltean o se descargan en la posición correcta.
* - **Pick**
  - El robot toma las piezas compensando el movimiento del FlexiBowl® gracias a los datos del encoder.
```

---

## Hardware y software necesarios

Para habilitar el Circular Tracking se necesitan los siguientes componentes:

- Opción **Circular Tracking** en el FlexiBowl®, disponible en la lista de precios para:

  | Tamaño | Código de la lista de precios |
  |---|---|
  | FlexiBowl® 500 | Circular Tracking 500C · Circular Tracking 500CC |
  | FlexiBowl® 650 | Circular Tracking 650CC |
  | FlexiBowl® 800 | Circular Tracking 800C · Circular Tracking 800CC |
  | FlexiBowl® 1200 | Circular Tracking 1200C · Circular Tracking 1200CC |

- Opción **conveyor tracking** en el controlador del robot

(schema-di-collegamento)=
### Datos técnicos del encoder

La opción Circular Tracking incluye un encoder conectado a la rotación del disco. La señal del encoder se divide dentro del FlexiBowl® y se envía tanto al driver del motor como al controlador del robot.

:::{list-table}
:widths: 35 65
:stub-columns: 1

* - Modelo
  - 
* - Número máx. de impulsos
  - 49152 / 65536 impulsos/vuelta, según la velocidad del FlexiBowl®
* - Interfaz de comunicación
  - Incremental, TTL / HTL (ajuste de fábrica: TTL)
* - Certificaciones
  - Declaración de conformidad UE · Declaración de conformidad UK · Declaración de conformidad ACMA · Declaración de conformidad Marruecos · China RoHS · cULus
* - Conexión en el FlexiBowl®
  - {ref}`Prensaestopas del encoder <io-flexitrack>`
:::

---
## Página JOG 

La página **Jog Motor** permite accionar el FlexiBowl® en modo circular tracking, sin utilizar secuencias programadas. Se utiliza principalmente durante las fases de configuración, puesta en servicio y prueba del sistema, permitiendo al operador controlar directamente la rotación del FlexiBowl® y las funciones accesorias.
![página jog motor](../../../../_shared/media/images/jog_motor.png)

Para más información, consulte la [página JOG](jog)

#### Comandi EXE JOG

| Comando | ControlWord | Busy durante la ejecución | ReturnData_1 | Explicación | 
|---|---|---|---|---|
| Start Jog Seq | 40 | SÍ | 40 | Iniciar Jog |
| Stop Jog Seq | 41 | SÍ | 41 | Detener Jog |

#### Comandi WRITE JOG

Los comandos de Jog (funcionamiento manual continuo) se pueden configurar por separado mediante ControlWord en el bloque 20000.

| Comando | ControlWord | Range Data_1 | Notas |
|---|---|---|---|
| AccelerationJog | 20001 | 0–100 | Rampa de aceleración del jog (%) |
| DecelerationJog | 20002 | 0–100 | Rampa de deceleración del jog (%) |
| SpeedJog | 20003 | 0–100 | Velocidad del jog (%). Valores 1000–1100 = velocidad negativa (rotación inversa) |
| FlipJog_Enable | 20004 | 0–1 | 0 = flip deshabilitado, 1 = flip habilitado durante el jog |
| FlipJog_Duration | 20005 | 0–1000 | Duración del impulso de flip (ms) |
| FlipJog_Pressure | 20006 | 0–600 | Presión de flip (/100 = Bar) |
| FlipJog_Pause | 20007 | 0–1000 | Pausa entre flips consecutivos (ms) |
| BlowJog_Enable | 20008 | 0–1 | 0 = blow deshabilitado, 1 = blow habilitado durante el jog |
| BlowJog_Duration | 20009 | 0–1000 | Duración del impulso de blow (ms) |
| BlowJog_Pressure | 20010 | 0–600 | Presión de blow (/100 = Bar) |
| BlowJog_Pause | 20011 | 0–1000 | Pausa entre blows consecutivos (ms) |
| BlowJog_Type | 20012 | 0–2 | Tipo de blow: 0 = BLOWc, 1 = BLOWe, 2 = BLOWc+BLOWe |
| Backlight_1 | 20013 | 0–1 | 0 = apagado, 1 = encendido |
| Backlight_2 | 20014 | 0–1 | 0 = apagado, 1 = encendido |

#### Comandi READ JOG

Los mismos comandos JOG escribibles (bloque 20000) se pueden leer en el bloque 20100:

| Comando | ControlWord READ | Rango ReturnData_2 |
|---|---|---|
| AccelerationJog | 20101 | 0–100 |
| DecelerationJog | 20102 | 0–100 |
| SpeedJog | 20103 | 0–100 (1000–1100 = negativo) |
| FlipJog_Enable | 20104 | 0–1 |
| FlipJog_Duration | 20105 | 0–1000 |
| FlipJog_Pressure | 20106 | 0–600 (/100) |
| FlipJog_Pause | 20107 | 0–1000 |
| BlowJog_Enable | 20108 | 0–1 |
| BlowJog_Duration | 20109 | 0–1000 |
| BlowJog_Pressure | 20110 | 0–600 (/100) |
| BlowJog_Pause | 20111 | 0–1000 |
| BlowJog_Type | 20112 | 0–2 |
| Backlight_1 | 20113 | 0–1 |
| Backlight_2 | 20114 | 0–1 |

::::{tip}
Para los Códigos de error, consulte la página específica.
:::{card} IR A LA PÁGINA CORRESPONDIENTE
:link: sec-err
:link-type: ref
:class-card: isw-card-field
:class-body: isw-card-body
:::
::::

---
## Ventajas 


:::{grid-item-card} Ventajas
- **Velocidad**: .
- **Estabilidad del tiempo de ciclo**: .
- **Menor huella de espacio**: .
:::

---
## Notas operativas

:::{warning}
El modo Circular Tracking ofrece el máximo rendimiento pero con una **precisión ligeramente inferior** a la del modo estándar. Evalúe su idoneidad en función de los requisitos de tolerancia del componente que se va a manipular.
:::

:::{note}
Para la configuración del parámetro de desfase entre el área de visión y el área de toma, consulte la sección de configuración de software del sistema.
:::

