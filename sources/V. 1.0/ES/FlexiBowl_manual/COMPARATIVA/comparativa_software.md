<style>
.compare-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  margin: 1rem 0 1.5rem;
}
@media (max-width: 680px) {
  .compare-grid { grid-template-columns: 1fr; }
}
.compare-card {
  border: 1px solid #5a9fd4;
  border-radius: 7px;
  overflow: hidden;
  font-size: 0.92rem;
}
.compare-card-header {
  padding: 0.5rem 1rem;
  font-weight: 700;
  font-size: 0.82rem;
  letter-spacing: 0.05em;
  color: #ffffff;
}
.v20 .compare-card-header { background: #1a4a7a; }
.v30 .compare-card-header { background: #1e6fbf; }
.compare-card-body {
  padding: 0.85rem 1rem;
}
.compare-card-body p, .compare-card-body li { margin: 0.25rem 0; }
.compare-card-body ul, .compare-card-body ol { padding-left: 1.2rem; margin: 0.4rem 0; }
.compare-card-body table {
  width: 100%;
  border-collapse: collapse;
  margin: 0.5rem 0;
  font-size: 0.88rem;
}
.compare-card-body table th {
  padding: 0.35rem 0.6rem;
  text-align: left;
  font-size: 0.78rem;
  font-weight: 700;
  border-bottom: 2px solid #5a9fd4;
  opacity: 0.75;
}
.compare-card-body table td {
  padding: 0.35rem 0.6rem;
  border-bottom: 1px solid rgba(90, 159, 212, 0.3);
}
.compare-card-body table tr:last-child td { border-bottom: none; }
.compare-card-body pre {
  border: 1px solid rgba(90, 159, 212, 0.4);
  border-radius: 5px;
  padding: 0.7rem 0.9rem;
  font-size: 0.8rem;
  overflow-x: auto;
  margin: 0.5rem 0 0;
}
</style>
 
# **Comparativa de software**
 
Esta página compara las principales diferencias de software entre el **FlexiBowl® 2.0** y el **FlexiBowl® 3.0**, con el objetivo de guiar al usuario en la comprensión de las nuevas funcionalidades y de los cambios operativos introducidos por la nueva generación.
 
:::{important}
Antes de leer el contenido de esta página, es recomendable tener claras las informaciones recogidas en la página [Interfaz de software](int_software)
:::
---
 
## 1. Protocolos de comunicación disponibles
 
| Protocolo | FlexiBowl® 2.0 | FlexiBowl® 3.0 |
|---|---|---|
| TCP/IP – UDP | ✓ | ✓ (TCP Server) |
| EtherNet/IP | ✓ | ✓ |
| Profinet | ✗ | ✓ |
| Modbus | ✗ | ✓ |
| Digital I/O | ✓ | ✓ (opcional) |
 
---
 
## 2. Interfaz de usuario: cómo es y cómo se accede a ella
 
<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0 — Software Parameters</div>
<div class="compare-card-body">
 
Interfaz de **escritorio** llamada **FlexiBowl® Parameters**, que debe instalarse en el PC de control.
 
**Instalación y acceso:**
 
1. Instalar el programa **FlexiBowl® Parameters** en el PC (suministrado por ARS).
2. Conectar el PC al FlexiBowl® mediante un **cable Ethernet** (LAN directa o a través de un switch).
3. Iniciar el programa e introducir la **dirección IP** del FlexiBowl® para conectarse.
 
Desde la pantalla **Main Commands** se accede a los paneles **Move**, **Shake** y **Option** mediante pestañas situadas en la parte superior.
 
</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0 — Interfaz web</div>
<div class="compare-card-body">
 
Interfaz **totalmente basada en web**: no requiere ninguna instalación. Basta con un navegador moderno.
 
**Acceso:**
 
1. Conectar el PC al FlexiBowl® mediante Ethernet.
2. Abrir el navegador e introducir la **dirección IP** del FlexiBowl® en la barra de direcciones.
3. Se abre la **página de inicio** de la interfaz.
 
**Estructura de la interfaz:**
 
El menú lateral incluye páginas dedicadas a cada función operativa (Main Command, Jog Motor, Setup, Monitor, etc.), accesibles directamente desde el navegador.
 
</div>
</div>
</div>
 
:::{note}
Si el sistema utilizado es **FlexiVision One**, la configuración se gestiona desde su interfaz específica. No es necesario utilizar la interfaz de software del FlexiBowl® descrita en esta sección.
:::
 
---
 
## 3. Cómo cambiar la dirección IP
 
<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0</div>
<div class="compare-card-body">
 
1. Utilizar el programa suministrado en la memoria USB.
2. Conectar el FlexiBowl® mediante un cable Ethernet.
3. Encender el equipo.
4. Iniciar el programa.
5. En el cuadro **IP Address**, introducir la dirección: `192.168.1.10`
   *(El PC conectado debe estar en la misma máscara de subred de clase B — 255.255.0.0)*
6. Pulsar **Ping** → ventana emergente **«FlexiBowl® found»**.
7. Pulsar **Ok** para habilitar **CONNECT** e iniciar la conexión.
8. Tras la conexión se mostrará la pantalla de inicio.
 
</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0</div>
<div class="compare-card-body">
 
1. Abrir el navegador y acceder a la interfaz mediante la IP actual.
2. En el menú lateral, abrir la página **Setup**.
3. Hacer clic en **Get IP** para leer los parámetros de red actuales.
4. Introducir la nueva dirección IP en los campos correspondientes y hacer clic en **Set IP**.
5. Hacer clic en **Apply** para confirmar y, a continuación, en **Reboot** para que los cambios surtan efecto.
 
</div>
</div>
</div>
 
:::{note}
**FlexiBowl® 2.0** — Si hay instalada una versión anterior del programa, es necesario desinstalarla antes.
:::
 
:::{important}
**FlexiBowl® 3.0** — Tras el reinicio, volver a conectarse al FlexiBowl® utilizando la nueva dirección IP configurada.
:::
 
---
 
## 4. Cómo gestionar los movimientos
 
<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0</div>
<div class="compare-card-body">
 
Los movimientos se configuran y prueban desde **Main Commands**, con tres paneles:
 
- **Move**: establece Acceleration, Deceleration, Speed y Angle mediante deslizador o campo numérico. **Test Move** ejecuta el movimiento con los valores establecidos.
- **Shake**: parámetros CCW Angle, CW Angle, Count, Acceleration, Deceleration y Speed. **Test Shake** ejecuta el shake.
- **Try Commands**: combina varios comandos en una secuencia con un bucle configurable, seleccionando desde **All Commands** y añadiendo a **Selected Commands**.
 
Para la producción mediante protocolo, se envían comandos ASCII (p. ej. `QX2` para Move, `QX6` para Shake) a través del canal TCP/UDP configurado.
 
</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0</div>
<div class="compare-card-body">
 
Los movimientos se organizan en **secuencias** (hasta 20), configurables desde la página **Main Command**. Cada secuencia contiene hasta 10 ranuras de comandos (Move, Shake, Flip, Blow).
 
Desde la página **Main Command** es posible:
 
- Seleccionar la secuencia mediante **Select the sequence**.
- Establecer todos los parámetros en los campos numéricos.
- Añadir comandos con **Command Available** + **ADD**; reordenarlos con **UP/DOWN**; eliminarlos con **DELETE** o vaciar la lista con **CLEAR**.
- Probar con **TEST SEQUENCE** o iniciar la producción con **RUN**.
 
La página **Jog Motor** permite la rotación continua (Speed positivo = sentido horario, negativo = sentido antihorario) con Flip y Blow integrados.
 
Para la producción mediante protocolo: `10[0]%` para la Secuencia 1 vía TCP, o ControlWord `10` vía EtherNet/IP o Profinet.
 
</div>
</div>
</div>
 
---
 
## 5. Cómo cambiar los parámetros
 
<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0</div>
<div class="compare-card-body">
 
Los parámetros operativos se modifican de dos maneras:
 
- **Interfaz gráfica**: deslizadores o campos numéricos en las pantallas Move y Shake de **Main Commands**.
- **Mediante protocolo (runtime)**: comandos `RW` (Write) y `RL` (Read) vía TCP/UDP. Los valores deben multiplicarse por el **factor de reducción** de la máquina (obtenido con el comando `RR114`), ya que los parámetros se expresan en unidades internas del driver.
 
</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0</div>
<div class="compare-card-body">
 
Los parámetros se modifican de tres maneras:
 
- **Interfaz web**: directamente en los campos numéricos de la página **Main Command** para cada secuencia.
- **Mediante protocolo WRITE**: ControlWord bloque WRITE con la fórmula `N × 100 + offset_parametro`
- **Mediante protocolo READ**: ControlWord bloque READ con la fórmula `10000 + N × 100 + offset_parametro`
 
</div>
</div>
</div>
 
---
 
### Ejemplo práctico: Move + Shake en el FlexiBowl® 800
 
El escenario es el siguiente: ejecutar un **Move** de 360°, después un **Shake**, y luego una espera de 200 ms.
 
<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0 — Secuencia de comandos TCP</div>
<div class="compare-card-body">
 
Los parámetros deben escalarse mediante el **factor de reducción** de la máquina:
 
<pre>QX7                     → Encender la retroiluminación
RR114                   → Leer el factor de reducción
reduction_factor = RX 1
 
RL1 (50 × reduction_factor), RW11   → Acceleration Move = 50 %
RL1 (50 × reduction_factor), RW12   → Deceleration Move = 50 %
RL1 (35 × reduction_factor), RW13   → Speed Move = 35 %
RL1 (360 × reduction_factor), RW14  → Angle Move = 360°
QX2                     → Ejecutar Move
 
RL1 (50 × reduction_factor), RW15  → Acceleration Shake = 50 %
RL1 (50 × reduction_factor), RW16  → Deceleration Shake = 50 %
RL1 (50 × reduction_factor), RW110 → Speed Shake = 50 %
RL1 (30 × reduction_factor), RW18  → Angle CW Shake = -30°
RL1 (30 × reduction_factor), RW19  → Angle CCW Shake = -45°
RL1 2, RW17                           → Count Shake = 2
QX6                     → Ejecutar Shake</pre>
 
La espera de 200 ms la gestiona el sistema llamante (robot o PLC).
 
</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0 — Configuración de la interfaz web</div>
<div class="compare-card-body">
 
Desde la página **Main Command**, seleccionar **SEQUENCE 1** y establecer:
 
| Parámetro | Valor |
|---|---|
| Acceleration Move | 50 % |
| Deceleration Move | 50 % |
| Speed Move | 35 % |
| Angle Move | 360° |
| Acceleration Shake | 50 % |
| Deceleration Shake | 50 % |
| Speed Shake | 50 % |
| Ccw Angle Shake | −45° |
| Cw Angle Shake | −30° |
| Count Shake | 2 |
 
Añadir a la lista: `FLB_MOVE` → `FLB_SHAKE`. Comprobar Backlight desde la página **Option**. La espera de 200 ms se gestiona añadiendo `FLB_WAIT` a la lista o en el lado del sistema llamante.
 
Para ejecutar la secuencia vía TCP:
 
<pre>10[0]%    → Ejecutar la Secuencia 1</pre>
 
El sistema responde con `10[0]` como confirmación.
 
</div>
</div>
</div>
 
---
 
## 6. Cómo leer las alarmas
 
<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0</div>
<div class="compare-card-body">
 
Las alarmas se consultan desde **Monitor → Alarm Status** del programa **FlexiBowl® Parameters**. La pantalla muestra los estados del driver mediante indicadores LED (verde = OK, rojo = error). La pantalla **Driver Status** muestra en tiempo real todas las variables operativas.
 
Reinicio de la alarma mediante protocolo:
 
<pre>Chr(0)Chr(7)QX12Chr(13)    → Reiniciar la alarma y rehabilitar el motor</pre>
 
</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0</div>
<div class="compare-card-body">
 
Las alarmas se consultan desde la página **Monitor** (pestañas: **I/O Status**, **Driver Status**, **Alarm Status**).
 
Mediante protocolo, la señal de alarma la expone **In_Error** (BOOL) y el código activo **ErrorCode** (UDINT):
 
<pre>InError%         → InError[1]% si hay error, InError[0]% si OK
ErrorCode%       → ErrorCode[N]% con el código del error activo</pre>
 
Reinicio de la alarma:
- Mediante protocolo TCP: `Reset%`
- Mediante variable digital: flanco de subida en la señal de entrada **Reset** (BOOL)
 
</div>
</div>
</div>
 
:::{warning}
Antes de realizar el reinicio, identificar y resolver la causa del error. El sistema no ejecutará nuevos comandos de movimiento mientras haya un error activo.
:::
 
:::{note}
Para la lista completa de códigos de error, consulte la sección [Códigos de error](sec-err)
:::
 
---
 
## 7. Modo tracking (FlexiTrack)
 
<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0</div>
<div class="compare-card-body">
 
El modo **FlexiTrack** es una opción que se adquiere por separado y permite mantener el FlexiBowl® en **rotación continua** (jog) sincronizando la señal del encoder con el robot de pick.
 
**Hardware requerido:**
 
- Conexión al **encoder interno** mediante el conector del panel de control (señal en cuadratura TTL, 4000 cuentas/vuelta en el motor; para FlexiBowl® 500/650/800 con reducción 1:3 → 12000 cuentas/vuelta en el disco).
- Como alternativa, **encoder externo** (incremental, TTL RS422, ≥ 12000 ppr) en el eje solidario de la polea conducida.
 
**Comandos principales de FlexiTrack (vía TCP/UDP):**
 
| Comando | Descripción |
|---|---|
| `JA<valore>` | Aceleración/deceleración en rev/s² |
| `JL<valore>` | Deceleración (si es distinta de JA, enviar después de JA) |
| `JS<valore>` | Velocidad de rotación en rev/s |
| `CC<valore>` | Corriente suministrada al motor |
| `DI1` | Sentido horario |
| `DI-1` | Sentido antihorario |
| `CJ` | Iniciar jog (rotación continua) |
| `SJ` | Detener jog (con rampa JL) |
| `IL2` / `IH2` | Activar / desactivar Flip |
| `IL3` / `IH3` | Activar / desactivar Blow |
 
**Parámetros recomendados:**
 
<pre>JA0.2    → aceleración 0.2 rev/s²
JL0.2    → deceleración 0.2 rev/s²
JS0.2    → velocidad 0.2 rev/s
CC1.3    → corriente del motor
DI1      → rotación en sentido horario</pre>
 
Flip y Blow deben implementarse mediante un **programa en segundo plano** con un ciclo iterativo que conmute el estado de las válvulas.
 
</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0</div>
<div class="compare-card-body">
 
El modo jog está **integrado de forma nativa** en la página **Jog Motor** — sin opciones de hardware adicionales.
 
**Parámetros de movimiento Jog:**
 
| Parámetro | Unidad | Descripción |
|---|---|---|
| Acceleration | % | Rampa de aceleración al inicio |
| Deceleration | % | Rampa de deceleración al detenerse |
| Speed | % | Velocidad — positiva = sentido horario; negativa = sentido antihorario |
 
**Funciones accesorias durante el Jog:**
 
- **Flip Enable**: flip automático cíclico con Flip Duration, Flip Pression, Flip Pause.
- **Blow Enable**: soplado automático cíclico con Blow Duration, Blow Pression, Blow Pause, Blow Type (BLOWc, BLOWe, BLOWc+BLOWe).
- **Backlight 1 / 2**: interruptor de la retroiluminación, independiente del estado del jog.
 
**Inicio y parada:**
 
- **START JOG**: inicia la rotación continua.
- **STOP JOG**: detiene con una rampa de deceleración.
 
Control mediante protocolo:
 
<pre>40[0]%    → Start Jog Seq (via TCP)
41[0]%    → Stop Jog Seq (via TCP)</pre>
 
</div>
</div>
</div>
 
:::{important}
Antes de iniciar el jog, comprobar que el motor esté habilitado (**ENABLE MOTOR** activo) y que el estado del sistema sea **READY**.
:::
 
:::{important}
Con FlexiTrack **(FlexiBowl® 2.0)**, el control del movimiento es posible **únicamente mediante el protocolo Ethernet** (TCP/UDP). El protocolo Digital I/O no es compatible.
:::