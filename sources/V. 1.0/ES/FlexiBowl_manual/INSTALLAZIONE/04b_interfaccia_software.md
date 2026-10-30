(tcp)=
# **TCP Server**

Cuando se utiliza la comunicación **TCP Server**, los comandos no se envían como variables binarias sino como **cadenas de texto** a través de una conexión socket en el puerto configurado (por defecto: 8123).


Cada mensaje tiene la forma:

```
NomeVariabile[Valore]%
```

El carácter `%` es el **terminador de mensaje** y debe estar siempre presente al final. El campo `[Valore]` contiene el dato numérico asociado (ControlWord, estado, etc.).

## Tabla de sintaxis TCP

| Operación | Mensaje que se debe enviar | Respuesta si OK | Respuesta si hay error |
|---|---|---|---|
| Todos los comandos EXE | `10[0]%` | `10[0]%` | `1[0]%` |
| Todos los comandos WRITE | `100[56]%` | `100[0]%` | `2[0]%` |
| Todos los comandos READ | `10100[0]%` | `10100[valore]%` | `2[0]%` |
| Reinicio de errores | `Reset%` | `Reset%` | — |
| Leer el estado Busy | `Busy%` | `Busy[1]%` | `Busy[0]%` |
| Leer el estado Ready | `Ready%` | `Ready[1]%` | `Ready[0]%` |
| Leer el estado InError | `InError%` | `InError[1]%` | `InError[0]%` |
| Leer el estado InPowerOn | `InPowerOn%` | `InPowerOn[1]%` | `InPowerOn[0]%` |
| Leer ErrorCode | `ErrorCode%` | `ErrorCode[56]%` | `ErrorCode[0]%` |

:::{note}
En las respuestas de tipo READ, el texto `[valore]` se sustituye por el valor numérico efectivo leído por el sistema. Por ejemplo, para leer la velocidad de la SEQ 1 (ControlWord 10102), se envía `10102[0]%` y se recibe `10102[35]%` si la velocidad está ajustada al 35 %.
:::

:::{warning}
Los comandos Hopper vía TCP (`Hopper1Start%`, etc.) funcionan **solo cuando la comunicación está activa y el FlexiBowl® no está en movimiento**. No se garantiza el correcto funcionamiento si el FlexiBowl® está ejecutando una secuencia o está en modo jog.
:::

## Significado de ReturnData_1 (o respuesta TCP)

| Valor | Significado |
|---|---|
| `0` | NULL — ningún comando en curso (estado inicial) |
| `1` | Comando no interpretable (ControlWord desconocida) |
| `2` | Data_1 fuera de rango, pero el comando ha sido reconocido |
| `3` | Sistema ocupado (Busy) — volver a intentarlo cuando Busy vuelva a 0 |
| Valor = ControlWord | Comando ejecutado correctamente |

---

## Protocolo de comandos

El protocolo de comandos define todas las acciones disponibles mediante la ControlWord. Las ControlWords son **las mismas para todos los protocolos**; solo cambia el transporte (véanse [Transporte Fieldbus](#sec-fieldbus) y [Sintaxis TCP](#sec-tcp)). Los comandos se agrupan en categorías:

<div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:1rem; margin:1.5rem 0 2.5rem;">

  <a href="#sec-exe" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-play-circle" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Comandos EXE</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Comandos de ejecución (inicio de secuencias, jog, reinicio)</span>
  </a>

  <a href="#sec-write" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-pencil-simple" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Comandos WRITE</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Escritura de parámetros (velocidad, ángulos, tiempos, etc.)</span>
  </a>

  <a href="#sec-read" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-eye" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Comandos READ</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Lectura de los parámetros configurados actualmente</span>
  </a>

</div>

(sec-exe)=
### Comandos <span class="isw-section-badge isw-badge-exe"><i class="ph ph-play-circle"></i> EXE</span>

Los comandos EXE inician una acción inmediata en el FlexiBowl®. Durante la ejecución **Busy** permanece a `1`.

| Comando | ControlWord | Busy durante la ejecución | ReturnData_1 | Explicación | 
|---|---|---|---|---|
| Exe Seq 1 | 10 | SÍ | 10 | Ejecutar la Secuencia 1 |
| Exe Seq 2 | 11 | SÍ | 11 | Ejecutar la Secuencia 2 |
| Exe Seq 3 | 12 | SÍ | 12 | Ejecutar la Secuencia 3 |
| Exe Seq 4 | 13 | SÍ | 13 | Ejecutar la Secuencia 4 |
| Exe Seq 5 | 14 | SÍ | 14 | Ejecutar la Secuencia 5 |
| Exe Seq 6 | 15 | SÍ | 15 | Ejecutar la Secuencia 6 |
| Exe Seq 7 | 16 | SÍ | 16 | Ejecutar la Secuencia 7 |
| Exe Seq 8 | 17 | SÍ | 17 | Ejecutar la Secuencia 8 |
| Exe Seq 9 | 18 | SÍ | 18 | Ejecutar la Secuencia 9 |
| Exe Seq 10 | 19 | SÍ | 19 | Ejecutar la Secuencia 10 |
| Exe Seq 11 | 20 | SÍ | 20 | Ejecutar la Secuencia 11 |
| Exe Seq 12 | 21 | SÍ | 21 | Ejecutar la Secuencia 12 |
| Exe Seq 13 | 22 | SÍ | 22 | Ejecutar la Secuencia 13 |
| Exe Seq 14 | 23 | SÍ | 23 | Ejecutar la Secuencia 14 |
| Exe Seq 15 | 24 | SÍ | 24 | Ejecutar la Secuencia 15 |
| Exe Seq 16 | 25 | SÍ | 25 | Ejecutar la Secuencia 16 |
| Exe Seq 17 | 26 | SÍ | 26 | Ejecutar la Secuencia 17 |
| Exe Seq 18 | 27 | SÍ | 27 | Ejecutar la Secuencia 18 |
| Exe Seq 19 | 28 | SÍ | 28 | Ejecutar la Secuencia 19 |
| Exe Seq 20 | 29 | SÍ | 29 | Ejecutar la Secuencia 20 |
| Start Jog Seq | 40 | SÍ | 40 | Iniciar Jog |
| Stop Jog Seq | 41 | SÍ | 41 | Detener Jog |
| Reset Return Data | 50 | NO | 0 | Pone a cero el valor de ReturnData_1 y ReturnData_2, devolviéndolos al estado inicial `0` |

:::{note}
El comando **Reset Return Data** (ControlWord 50) pone a cero el valor de ReturnData_1 y ReturnData_2, devolviéndolos al estado inicial `0`. Resulta útil para verificar que un nuevo comando se recibe y se procesa realmente.
:::

(TCP_EXE)=
#### Ejemplo práctico — «Ejecutar la Secuencia 3»

<div class="isw-example">
<div class="isw-example-title">Ejecutar la Secuencia 3 → ControlWord 12</div>
<div class="isw-example-body">
<div>

<div>
<div class="isw-example-col-title">TCP Server</div>

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>12[0]%</code><br> RETURN SI OK:&nbsp;&nbsp;&nbsp;<span class="ok">12[0]</span>
</div>

Ejemplo de comando **no válido** (p. ej. la secuencia 9 no existe en el dispositivo):

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>9[0]%</code><br> RETURN SI NO OK:&nbsp;&nbsp;&nbsp;<span class="ko">1[0]</span>
</div>

</div>
</div>
</div>

(sec-write)=
### Comandos <span class="isw-section-badge isw-badge-write"><i class="ph ph-pencil-simple"></i> WRITE</span>

Los comandos WRITE permiten modificar los parámetros operativos del FlexiBowl® (velocidad, ángulos, tiempos, etc.) directamente desde el sistema externo, sin necesidad de acceder a la interfaz gráfica.

#### Lógica de direccionamiento de las secuencias

Cada secuencia (de 1 a 20) tiene su propio bloque de parámetros. La ControlWord se calcula con la fórmula:

> **ControlWord = N × 100 + parameter_offset**

donde `N` es el número de la secuencia (1–20) y `offset_parametro` identifica el parámetro específico.

#### Parámetros escribibles para cada secuencia

| Parámetro | Offset | Range Data_1 | Notas |
|---|---|---|---|
| AccelerationMove | 00 | 1–100 | Rampa de aceleración del movimiento rotatorio (%) |
| DecelerationMove | 01 | 1–100 | Rampa de deceleración del movimiento rotatorio (%) |
| SpeedMove | 02 | 1–100 | Velocidad del movimiento rotatorio (%) |
| AngleMove | 03 | 0–720 | Ángulo de rotación en grados. Valores 1000–1720 = ángulo negativo (dirección opuesta) |
| AccelerationShake | 04 | 1–100 | Rampa de aceleración del shake (%) |
| DecelerationShake | 05 | 1–100 | Rampa de deceleración del shake (%) |
| CountShake | 06 | 2–20 | Número de oscilaciones por ciclo de shake |
| CwAngleShake | 07 | 0–360 | Ángulo de rotación en sentido horario durante el shake. Valores 1000–1360 = ángulo negativo |
| CcwAngleShake | 08 | 0–360 | Ángulo de rotación en sentido antihorario durante el shake. Valores 1000–1360 = ángulo negativo |
| SpeedShake | 09 | 1–100 | Velocidad del shake (%) |
| FlipCount | 10 | 0–20 | Número de flips por ciclo |
| FlipDelay | 11 | 0–500 | Pausa entre un flip y el siguiente (ms) |
| BlowDelay | 12 | 0–500 | Pausa entre un impulso de blow y el siguiente (ms) |
| ProportionalValve_Flip | 13 | 0–600 | Presión de la válvula proporcional Flip (valor /100 = Bar) |
| ProportionalValve_Blow | 14 | 0–600 | Presión de la válvula proporcional Blow (valor /100 = Bar) |
| Delete all sequence | 30 | — | Elimina todos los comandos de la lista de la secuencia |
| Emptying Sequence | 40 | 0–1 | 0 = modo normal, 1 = modo Quick Emptying |
| Seq Add Cmd | 50 | COMANDO FLB | Añade un comando a la lista de la secuencia |

#### Ejemplos de ControlWord WRITE

| Secuencia | Parámetro | Offset asociado al parámetro | Fórmula (N x 100 + Offset) | ControlWord |
|---|---|---|---|---|
| SEQ 1 (N=1) | AccelerationMove | 00 | 1 x 100 + 00 | 100 |
| SEQ 1 (N=1) | SpeedMove | 02 | 1 x 100 + 02 | 102 |
| SEQ 1 (N=1) | FlipCount | 10 | 1 x 100 + 10 | 110 |
| SEQ 1 (N=1) | Emptying Sequence | 40 | 1 x 100 + 40 | 140 |
| SEQ 1 (N=1) | Seq Add Cmd | 50 | 1 x 100 + 50 | 150 |
| SEQ 2 (N=2) | AccelerationMove | 00 | 2 x 100 + 00 | 200 |
| SEQ 2 (N=2) | SpeedMove | 02 | 2 x 100 + 02 | 202 |
| SEQ 5 (N=5) | AngleMove | 03 | 5 x 100 + 03 | 503 |
| SEQ 10 (N=10) | FlipDelay | 11 | 10 x 100 + 11 |1011 |
| SEQ 20 (N=20) | SpeedMove | 02 | 20 x 100 + 02 | 2002 |

:::{tip}
La fórmula es sencilla:
- Para escribir la velocidad (offset 02) de la secuencia 7, la ControlWord es `7 × 100 + 2 = 702`.
- Para escribir el FlipCount (offset 10) de la secuencia 15, la ControlWord es `15 × 100 + 10 = 1510`.
:::

(TCP_write)=
#### Ejemplo práctico — «Establecer la aceleración del Move a 80 en la Secuencia 7»

<div class="isw-example">
<div class="isw-example-title">SpeedMove Seq 7 → ControlWord 700, Data_1 = 80</div>
<div class="isw-example-body">
<div>

<div>
<div class="isw-example-col-title">TCP Server</div>

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>700[80]%</code><br> RETURN SI OK:&nbsp;&nbsp;&nbsp;<span class="ok">700[0]</span>
</div>

Ejemplo de **valor fuera de rango** (aceleración 1000 no admitida, rango 1–100):

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>700[1000]%</code><br> RETURN SI NO OK:&nbsp;&nbsp;&nbsp;<span class="ko">2[0]</span>
</div>

</div>
</div>
</div>

#### Parámetros WRITE JOG

Los parámetros del Jog (funcionamiento manual continuo) se pueden configurar por separado mediante ControlWord en el bloque 20000.

| Parámetro | ControlWord | Range Data_1 | Notas |
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

---

(sec-read)=
### Comandos <span class="isw-section-badge isw-badge-read"><i class="ph ph-eye"></i> READ</span>

Los comandos READ permiten leer los parámetros configurados actualmente en el FlexiBowl®. El valor leído se devuelve en **ReturnData_2**.

#### Lógica de direccionamiento READ de las secuencias

La ControlWord para la lectura se calcula con la fórmula:

> **ControlWord = 10000 + N × 100 + parameter_offset**

donde `N` es el número de la secuencia (1–20) y `offset_parametro` es el mismo que se usa en los comandos WRITE.

Los parámetros legibles son los mismos que los del bloque WRITE, con la adición de las 10 ranuras de la lista de comandos:

| Parámetro adicional | Offset | Descripción |
|---|---|---|
| Seq Slot 1 Cmd | 50 | Comando en la posición 1 de la lista de la secuencia |
| Seq Slot 2 Cmd | 51 | Comando en la posición 2 |
| … | … | … |
| Seq Slot 10 Cmd | 59 | Comando en la posición 10 |

#### Ejemplos de ControlWord READ

| Secuencia | Parámetro | ControlWord |
|---|---|---|
| SEQ 1 | AccelerationMove | 10100 |
| SEQ 1 | SpeedMove | 10102 |
| SEQ 1 | FlipCount | 10110 |
| SEQ 1 | Emptying Sequence | 10140 |
| SEQ 1 | Slot 1 Cmd | 10150 |
| SEQ 1 | Slot 10 Cmd | 10159 |
| SEQ 5 | AngleMove | 10503 |
| SEQ 10 | SpeedMove | 11002 |
| SEQ 20 | Emptying Sequence | 12040 |

:::{tip}
Fórmula rápida:
 Para leer la velocidad (offset 02) de la secuencia 12, la ControlWord es `10000 + 12 × 100 + 2 = 11202`.
:::

(TCP_read)=
#### Ejemplo práctico — «Leer el ángulo de la Secuencia 16»

<div class="isw-example">
<div class="isw-example-title">AngleMove Seq 16 → ControlWord 11603</div>
<div class="isw-example-body">
<div>

<div>
<div class="isw-example-col-title">TCP Server</div>

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>11603[0]%</code><br> RETURN SI OK:&nbsp;&nbsp;&nbsp;<span class="ok">11603[45]</span>
</div>

Ejemplo de **valor fuera de rango** al escribir en el mismo parámetro (ángulo máximo 720°):

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>11603[6799]%</code><br> RETURN SI NO OK:&nbsp;&nbsp;&nbsp;<span class="ko">1[0]</span>
</div>

</div>
</div>
</div>

#### Parámetros READ JOG

Los mismos parámetros JOG escribibles (bloque 20000) se pueden leer en el bloque 20100:

| Parámetro | ControlWord READ | Rango ReturnData_2 |
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

---

(sec-hopper)=
## Comandos <span class="isw-section-badge isw-badge-hop"><i class="ph ph-funnel"></i> HOPPER</span>

Los comandos Hopper controlan los Bulk Feeders conectados al sistema (hasta 4). Siguen la misma lógica ControlWord/WRITE/READ descrita anteriormente, válida para todos los protocolos, además de una sintaxis TCP específica para el arranque rápido.

### Arranque rápido vía TCP

Además de la sintaxis general de ControlWord, el protocolo **TCP Server** ofrece mensajes específicos para iniciar directamente un hopper:

| Operación | Mensaje que se debe enviar | Respuesta |
|---|---|---|
| Iniciar el Hopper 1 | `Hopper1Start%` | `Hopper1Start *` |
| Iniciar el Hopper 2 | `Hopper2Start%` | `Hopper2Start *` |
| Iniciar el Hopper 3 | `Hopper3Start%` | `Hopper3Start *` |
| Iniciar el Hopper 4 | `Hopper4Start%` | `Hopper4Start *` |

En los protocolos fieldbus (EtherNet/IP, Profinet, Modbus), el mismo arranque inmediato se obtiene poniendo directamente a `1` el bit **Hopper_1**...**Hopper_4** del [paquete de E/S](#sec-fieldbus), sin pasar por la ControlWord.

### Comandos WRITE Hopper

| Parámetro | ControlWord | Range Data_1 | Descripción |
|---|---|---|---|
| Hopper_1_Id | 30001 | 1–100 | ID único del hopper 1 en la red |
| Hopper_1_Amplitude | 30002 | 50–220 | Amplitud de vibración del hopper 1 |
| Hopper_1_Frequency | 30003 | 40–70 | Frecuencia de vibración del hopper 1 |
| Hopper_1_Activation_Time | 30004 | 400–60000 | Tiempo de activación del hopper 1 (ms) |
| Hopper_2_Id | 30005 | 1–100 | ID único del hopper 2 |
| Hopper_2_Amplitude | 30006 | 50–220 | Amplitud de vibración del hopper 2 |
| Hopper_2_Frequency | 30007 | 40–70 | Frecuencia de vibración del hopper 2 |
| Hopper_2_Activation_Time | 30008 | 400–60000 | Tiempo de activación del hopper 2 (ms) |
| Hopper_3_Id | 30009 | 1–100 | ID único del hopper 3 |
| Hopper_3_Amplitude | 30010 | 50–220 | Amplitud de vibración del hopper 3 |
| Hopper_3_Frequency | 30011 | 40–70 | Frecuencia de vibración del hopper 3 |
| Hopper_3_Activation_Time | 30012 | 400–60000 | Tiempo de activación del hopper 3 (ms) |
| Hopper_4_Id | 30013 | 1–100 | ID único del hopper 4 |
| Hopper_4_Amplitude | 30014 | 50–220 | Amplitud de vibración del hopper 4 |
| Hopper_4_Frequency | 30015 | 40–70 | Frecuencia de vibración del hopper 4 |
| Hopper_4_Activation_Time | 30016 | 400–60000 | Tiempo de activación del hopper 4 (ms) |
| Hopper_1_Enable | 30017 | — | Habilitar el hopper 1 (acción inmediata) |
| Hopper_1_Disable | 30018 | — | Deshabilitar el hopper 1 (acción inmediata) |
| Hopper_2_Enable | 30019 | — | Habilitar el hopper 2 |
| Hopper_2_Disable | 30020 | — | Deshabilitar el hopper 2 |
| Hopper_3_Enable | 30021 | — | Habilitar el hopper 3 |
| Hopper_3_Disable | 30022 | — | Deshabilitar el hopper 3 |
| Hopper_4_Enable | 30023 | — | Habilitar el hopper 4 |
| Hopper_4_Disable | 30024 | — | Deshabilitar el hopper 4 |

:::{note}
En el material de formación, la ControlWord `30005` (Hopper_2_Id) indicaba por error el mismo rango que la Amplitude (50–220). En esta tabla se ha corregido a **1–100**, de forma coherente con Hopper_1_Id, Hopper_3_Id y Hopper_4_Id. Verificar este valor con el firmware/la hoja de datos antes de publicar la página.
:::

(TCP_WRITEHOPPER)=
#### Ejemplo práctico — «Habilitar el Hopper 1»

<div class="isw-example">
<div class="isw-example-title">Hopper_1_Enable → ControlWord 30017</div>
<div class="isw-example-body">
<div>

<div>
<div class="isw-example-col-title">TCP Server</div>

Mediante ControlWord genérica:

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>30017[0]%</code><br> RETURN SI OK:&nbsp;&nbsp;&nbsp;<span class="ok">30017[0]</span>
</div>

O, solo para el arranque, con el mensaje específico:

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>Hopper1Start%</code><br> RETURN:&nbsp;&nbsp;&nbsp;<span class="ok">Hopper1Start *</span>
</div>

</div>
</div>
</div>

#### Ejemplo práctico — «Establecer la amplitud del Hopper 2 en 220»

<div class="isw-example">
<div class="isw-example-title">Hopper_2_Amplitude → ControlWord 30006, Data_1 = 220</div>
<div class="isw-example-body">
<div>

<div>
<div class="isw-example-col-title">TCP Server</div>

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>30006[220]%</code><br> RETURN SI OK:&nbsp;&nbsp;&nbsp;<span class="ok">30006[0]</span>
</div>

Ejemplo de **valor fuera de rango** (amplitud 2200 no admitida, rango 50–220):

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>30006[2200]%</code><br> RETURN SI NO OK:&nbsp;&nbsp;&nbsp;<span class="ko">2[0]</span>
</div>

</div>
</div>
</div>

### Comandos READ Hopper

| Parámetro | ControlWord READ | Range ReturnData_2 | Notas |
|---|---|---|---|
| Hopper_1_Id | 30101 | 1–100 | |
| Hopper_1_Amplitude | 30102 | 50–220 | |
| Hopper_1_Frequency | 30103 | 40–70 | |
| Hopper_1_Activation_Time | 30104 | 400–60000 | |
| Hopper_2_Id | 30105 | 1–100 | |
| Hopper_2_Amplitude | 30106 | 50–220 | |
| Hopper_2_Frequency | 30107 | 40–70 | |
| Hopper_2_Activation_Time | 30108 | 400–60000 | |
| Hopper_3_Id | 30109 | 1–100 | |
| Hopper_3_Amplitude | 30110 | 50–220 | |
| Hopper_3_Frequency | 30111 | 40–70 | |
| Hopper_3_Activation_Time | 30112 | 400–60000 | |
| Hopper_4_Id | 30113 | 1–100 | |
| Hopper_4_Amplitude | 30114 | 50–220 | |
| Hopper_4_Frequency | 30115 | 40–70 | |
| Hopper_4_Activation_Time | 30116 | 400–60000 | |
| Hopper_1_Ready | 30117 | 0–1 | 0 = no listo, 1 = listo |
| Hopper_2_Ready | 30118 | 0–1 | 0 = no listo, 1 = listo |
| Hopper_3_Ready | 30119 | 0–1 | 0 = no listo, 1 = listo |
| Hopper_4_Ready | 30120 | 0–1 | 0 = no listo, 1 = listo |
| Hopper_1_InVibration | 30121 | 0–1 | 0 = parado, 1 = en vibración |
| Hopper_2_InVibration | 30122 | 0–1 | 0 = parado, 1 = en vibración |
| Hopper_3_InVibration | 30123 | 0–1 | 0 = parado, 1 = en vibración |
| Hopper_4_InVibration | 30124 | 0–1 | 0 = parado, 1 = en vibración |
| Hopper_1_Enabled | 30125 | 0–1 | 0 = deshabilitado, 1 = habilitado |
| Hopper_2_Enabled | 30126 | 0–1 | 0 = deshabilitado, 1 = habilitado |
| Hopper_3_Enabled | 30127 | 0–1 | 0 = deshabilitado, 1 = habilitado |
| Hopper_4_Enabled | 30128 | 0–1 | 0 = deshabilitado, 1 = habilitado |

(TCP_READHOPPER)=
#### Ejemplo práctico — «Leer la frecuencia del Hopper 4»

<div class="isw-example">
<div class="isw-example-title">Hopper_4_Frequency → ControlWord 30115</div>
<div class="isw-example-body">
<div>

<div>
<div class="isw-example-col-title">TCP Server</div>

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>30115[0]%</code><br> RETURN SI OK:&nbsp;&nbsp;&nbsp;<span class="ok">30115[40]</span>
</div>

Ejemplo de **comando no interpretable** (ControlWord READ inexistente):

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>30199[0]%</code><br> RETURN SI NO OK:&nbsp;&nbsp;&nbsp;<span class="ko">1[0]</span>
</div>

</div>
</div>
</div>

:::{note}
Para los comandos Quick Emptying, consulte la sección [Comandos Quick Emptying](sec-empty)
:::

:::{important}
Para los Códigos de error, consulte la sección [Códigos de error](sec-err)
:::