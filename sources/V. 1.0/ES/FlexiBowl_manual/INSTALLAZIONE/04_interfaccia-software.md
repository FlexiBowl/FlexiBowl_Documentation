(int_software)=
# **Interfaz de software**

<script src="https://unpkg.com/@phosphor-icons/web"></script>

<div class="isw-page">
<style>
  /* ── Reset & base ── */
  .isw-page { font-family: inherit; max-width: 860px; margin: 0 auto; padding: 0 0 3rem; }

 /* ── NAV CARDS ── */
  .isw-nav {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    gap: 0.75rem;
    margin: 1.5rem 0 2.5rem;
  }
  .isw-nav-card {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 0.45rem;
    padding: 0.9rem 1rem;
    border: 1.5px solid #d0e4f0;
    border-radius: 10px;
    background: #fff;
    text-decoration: none;
    color: inherit;
    transition: border-color 0.18s, background 0.18s, transform 0.18s;
  }
  .isw-nav-card:hover {
    border-color: #2980b9;
    background: #f0f7ff;
    transform: translateY(-2px);
    text-decoration: none;
  }
  .isw-nav-card i {
    font-size: 1.4rem;
    color: #2980b9;
  }
  .isw-nav-card-title {
    font-weight: 700;
    font-size: 0.82rem;
    color: #1a3a52;
    line-height: 1.3;
  }
  .isw-nav-card-sub {
    font-size: 0.72rem;
    color: #7a9ab0;
  }

  /* ── FLOW DIAGRAM — orizzontale ── */
  .isw-flow {
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 0;
    margin: 1.5rem 0 2rem;
    overflow-x: auto;
    padding-bottom: 0.5rem;
    flex-wrap: nowrap;
  }
  .isw-flow-step {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.35rem;
    min-width: 110px;
    flex: 1;
  }
  .isw-flow-bubble {
    width: 48px;
    height: 48px;
    border-radius: 50%;
    background: #e3f1fb;
    border: 2px solid #2980b9;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #2980b9;
    font-size: 1.2rem;
    flex-shrink: 0;
  }
  .isw-flow-label {
    font-size: 0.72rem;
    font-weight: 600;
    color: #1a3a52;
    text-align: center;
    line-height: 1.3;
  }
  .isw-flow-sub {
    font-size: 0.65rem;
    color: #7a9ab0;
    text-align: center;
  }
  .isw-flow-arrow {
    color: #bcd6ec;
    font-size: 1.6rem;
    flex-shrink: 0;
    margin: 0 2px;
    padding-bottom: 1.8rem;
    display: flex;
    align-items: flex-start;
    padding-top: 0.2rem;
  }

  /* ── FORMULA BOX ── */
  .isw-formula {
    background: #f0f7ff;
    border-left: 4px solid #2980b9;
    border-radius: 0 8px 8px 0;
    padding: 1rem 1.25rem;
    margin: 1rem 0 1.5rem;
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    align-items: center;
  }
  .isw-formula-main {
    font-family: monospace;
    font-size: 1.05rem;
    font-weight: 700;
    color: #1a3a52;
    white-space: nowrap;
  }
  .isw-formula-example {
    font-size: 0.8rem;
    color: #556b7d;
    border-left: 1px solid #bcd6ec;
    padding-left: 1rem;
  }
  .isw-formula-example strong { color: #2980b9; }

  /* ── SECTION BADGES ── */
  .isw-section-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    border-radius: 5px;
    padding: 3px 10px;
    margin-bottom: 0.6rem;
  }
  .isw-badge-exe  { background: #dbeafe; color: #1d4ed8; }
  .isw-badge-write{ background: #fef3c7; color: #92400e; }
  .isw-badge-read { background: #d1fae5; color: #065f46; }
  .isw-badge-io   { background: #ede9fe; color: #5b21b6; }
  .isw-badge-tcp  { background: #fce7f3; color: #9d174d; }
  .isw-badge-err  { background: #fee2e2; color: #991b1b; }
  .isw-badge-field { background: #dcfce7; color: #166534; }
  .isw-badge-hop  { background: #ffe4e6; color: #9f1239; }

  /* ── TABLES ── */
  .isw-table-wrap {
    overflow-x: auto;
    border-radius: 8px;
    border: 1px solid #e2eef6;
    margin: 0.75rem 0 1.5rem;
  }
  .isw-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.82rem;
  }
  .isw-table thead tr {
    background: #1a3a52;
    color: #fff;
    position: sticky;
    top: 0;
    z-index: 1;
  }
  .isw-table thead th {
    padding: 0.6rem 0.9rem;
    text-align: left;
    font-weight: 600;
    white-space: nowrap;
  }
  .isw-table tbody tr:nth-child(even) { background: #f7fbfe; }
  .isw-table tbody tr:hover { background: #e8f4fc; }
  .isw-table tbody td {
    padding: 0.5rem 0.9rem;
    border-bottom: 1px solid #e9f2f9;
    color: #334e5e;
    vertical-align: top;
  }
  .isw-table tbody td:first-child {
    font-weight: 600;
    color: #1a3a52;
    white-space: nowrap;
  }
  .isw-table code {
    background: #e3f1fb;
    color: #1d4ed8;
    border-radius: 3px;
    padding: 1px 5px;
    font-size: 0.8rem;
  }
  .isw-table tbody tr.isw-hidden { display: none; }

  /* ── TABELLA ERRORI DRIVER — stile Sphinx standard ── */
  .isw-err-wrap {
    overflow-x: auto;
    margin: 0.75rem 0 1.5rem;
  }
  .isw-err-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.85rem;
  }
  .isw-err-table thead tr {
    background: #f0f4f8;
  }
  .isw-err-table thead th {
    padding: 0.55rem 0.8rem;
    text-align: left;
    font-weight: 700;
    color: #1a3a52;
    border: 1px solid #c8d8e4;
  }
  .isw-err-table tbody tr:nth-child(even) { background: #f7fbfe; }
  .isw-err-table tbody tr:hover { background: #cfe2ff; }
  .isw-err-table tbody td {
    padding: 0.45rem 0.8rem;
    border: 1px solid #c8d8e4;
    color: #334e5e;
    vertical-align: top;
  }
  .isw-err-table tbody td:first-child {
    font-weight: 600;
    color: #1a3a52;
    white-space: nowrap;
  }
  .isw-err-table code {
    font-family: monospace;
    font-size: 0.82rem;
    color: #1a3a52;
    background: none;
    padding: 0;
  }
  .isw-err-table tbody tr.isw-hidden { display: none; }

  /* ── SEARCH BOX ── */
  .isw-search-wrap {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-bottom: 0.75rem;
  }
  .isw-search {
    flex: 1;
    max-width: 340px;
    padding: 0.45rem 0.75rem 0.45rem 2.2rem;
    border: 1.5px solid #d0e4f0;
    border-radius: 7px;
    font-size: 0.85rem;
    color: #1a3a52;
    outline: none;
    background: #fff url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='14' height='14' viewBox='0 0 256 256'%3E%3Cpath fill='%237a9ab0' d='M229.66 218.34l-50.07-50.07a88.11 88.11 0 1 0-11.31 11.31l50.06 50.07a8 8 0 0 0 11.32-11.31ZM40 112a72 72 0 1 1 72 72 72.08 72.08 0 0 1-72-72Z'/%3E%3C/svg%3E") no-repeat 0.6rem center;
    transition: border-color 0.18s;
  }
  .isw-search:focus { border-color: #2980b9; }
  .isw-search-count {
    font-size: 0.75rem;
    color: #7a9ab0;
  }

  /* ── RETURN DATA — tabella leggibile ── */
  .isw-return-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.88rem;
    margin: 0.75rem 0 1.5rem;
  }
  .isw-return-table thead tr {
    background: #e3f1fb;
  }
  .isw-return-table thead th {
    padding: 0.55rem 1rem;
    text-align: left;
    font-weight: 700;
    color: #1a3a52;
    border-bottom: 2px solid #2980b9;
  }
  .isw-return-table tbody tr:nth-child(even) { background: #f7fbfe; }
  .isw-return-table tbody tr:hover { background: #cfe2ff; }
  .isw-return-table tbody td {
    padding: 0.55rem 1rem;
    border-bottom: 1px solid #d0e4f0;
    color: #334e5e;
    vertical-align: middle;
  }
  .isw-return-table tbody td:first-child {
    font-family: monospace;
    font-size: 1rem;
    font-weight: 700;
    color: #2980b9;
    white-space: nowrap;
    width: 90px;
  }

  /* ── ESEMPI PRATICI (pacchetto dati) ── */
  .isw-example {
    border: 1px solid #d0e4f0;
    border-radius: 10px;
    margin: 1rem 0 1.75rem;
    overflow: hidden;
  }
  .isw-example-title {
    background: #f0f7ff;
    padding: 0.6rem 1rem;
    font-weight: 700;
    font-size: 0.88rem;
    color: #1a3a52;
    border-bottom: 1px solid #d0e4f0;
  }
  .isw-example-body {
    padding: 1rem;
    display: grid;
    grid-template-columns: 1fr;
    gap: 1.25rem;
  }
  .isw-example-body > div + div {
    border-top: 1px solid #e2eef6;
    padding-top: 1rem;
  }
  .isw-example-col-title {
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    color: #2980b9;
    margin-bottom: 0.5rem;
    text-transform: uppercase;
  }
  .isw-example-body table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.78rem;
    margin-bottom: 0.5rem;
  }
  .isw-example-body table th {
    background: #f0f4f8;
    padding: 0.35rem 0.5rem;
    text-align: center;
    font-weight: 700;
    color: #1a3a52;
    border: 1px solid #d0e4f0;
    white-space: nowrap;
  }
  .isw-example-body table td {
    padding: 0.35rem 0.5rem;
    text-align: center;
    border: 1px solid #d0e4f0;
    color: #334e5e;
  }
  .isw-example-tcp {
    font-family: monospace;
    font-size: 0.85rem;
    background: #f7fbfe;
    border-radius: 6px;
    padding: 0.6rem 0.8rem;
    margin: 0.35rem 0;
  }
  .isw-example-tcp .ok { color: #166534; font-weight: 700; }
  .isw-example-tcp .ko { color: #991b1b; font-weight: 700; }
</style>

## Introducción

La nueva interfaz del FlexiBowl® está totalmente basada en web. Para acceder a ella basta con introducir la dirección IP por defecto del FlexiBowl® `192.168.1.10` en la barra de direcciones de su navegador.

:::{video} ../../../../_shared/media/videos/IP_Home.mp4
:width: 90%
:::


## Comunicación 

El sistema de comunicación se basa en **variables de entrada/salida** y **Control Words numéricas**: el sistema externo envía un número (la ControlWord) que identifica la acción que se debe ejecutar y el FlexiBowl® responde con señales de estado y datos de retorno.

Protocolos compatibles:
- **TCP Server**
- **EtherNet/IP**
- **Profinet**
- **Modbus**

:::{important}
Las variables, las ControlWords y todos los comandos **EXE**, **WRITE** y **READ** descritos en esta página son **idénticos para los cuatro protocolos de comunicación**. Lo que cambia de un protocolo a otro es **exclusivamente la forma en que estos datos se intercambian físicamente**:

- **EtherNet/IP, Profinet y Modbus** se comportan de la misma manera entre sí: intercambian un **paquete de E/S cíclico** con campos fijos (véase [Transporte Fieldbus](#sec-fieldbus)).
- **TCP Server**, en cambio, utiliza **mensajes de texto** sobre socket (véase [Sintaxis TCP](#sec-tcp)).

Por este motivo, cada ejemplo práctico de esta página se muestra en ambos modos.
:::

---

### Navegar por la página

<div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:1rem; margin:1.5rem 0 2.5rem;">

  <a href="#sec-io" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit; transition:border-color 0.18s, background 0.18s;">
    <i class="ph ph-arrows-left-right" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Variables de E/S</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Entrada y salida</span>
  </a>

  <a href="#sec-fieldbus" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-swap" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Transporte Fieldbus</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">EtherNet/IP, Profinet, Modbus</span>
  </a>

  <a href="#sec-tcp" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-network" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Sintaxis TCP</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Mensajes socket</span>
  </a>

  <a href="#sec-exe" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-play-circle" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Comandos EXE</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Inicio de secuencias y jog</span>
  </a>

  <a href="#sec-write" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-pencil-simple" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Comandos WRITE</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Escritura de parámetros</span>
  </a>

  <a href="#sec-read" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-eye" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Comandos READ</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Lectura de parámetros</span>
  </a>

  <a href="#sec-hopper" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-funnel" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Comandos Hopper</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Bulk Feeder</span>
  </a>

  <a href="#sec-empty" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-arrow-counter-clockwise" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Quick Emptying</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Opción de vaciado</span>
  </a>

  <a href="#sec-err" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-warning-circle" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Códigos de error</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Diagnóstico</span>
  </a>

</div>

---

### Cómo funciona un comando

Esta lógica es **idéntica para todos los protocolos**: solo cambia la forma en que se transmiten físicamente los 4 pasos (paquete de E/S para los protocolos fieldbus, mensaje de texto para TCP — véanse las secciones siguientes).

<table style="width:100%; border-collapse:collapse; margin: 1.5rem 0 2rem;">
  <tr>
    <td style="text-align:center; padding:0 8px; width:22%;">
      <div style="width:52px; height:52px; border-radius:50%; background:#e3f1fb; border:2px solid #2980b9; display:inline-flex; align-items:center; justify-content:center; color:#2980b9; font-size:1.4rem; font-weight:700; margin-bottom:0.5rem;">
        1
      </div><br>
      <span style="font-size:0.92rem; font-weight:700; color:#1a3a52; line-height:1.4;">Establecer<br>ControlWord</span><br>
      <span style="font-size:0.8rem; color:#7a9ab0;">número del comando</span>
    </td>
    <td style="text-align:center; color:#bcd6ec; font-size:1.6rem; width:4%; vertical-align:middle; padding-bottom:1.8rem;">
      <i class="ph ph-caret-right"></i>
    </td>
    <td style="text-align:center; padding:0 8px; width:22%;">
      <div style="width:52px; height:52px; border-radius:50%; background:#e3f1fb; border:2px solid #2980b9; display:inline-flex; align-items:center; justify-content:center; color:#2980b9; font-size:1.4rem; font-weight:700; margin-bottom:0.5rem;">
        2
      </div><br>
      <span style="font-size:0.92rem; font-weight:700; color:#1a3a52; line-height:1.4;">Establecer<br>Data_1</span><br>
      <span style="font-size:0.8rem; color:#7a9ab0;">si se requiere</span>
    </td>
    <td style="text-align:center; color:#bcd6ec; font-size:1.6rem; width:4%; vertical-align:middle; padding-bottom:1.8rem;">
      <i class="ph ph-caret-right"></i>
    </td>
    <td style="text-align:center; padding:0 8px; width:22%;">
      <div style="width:52px; height:52px; border-radius:50%; background:#e3f1fb; border:2px solid #2980b9; display:inline-flex; align-items:center; justify-content:center; color:#2980b9; font-size:1.4rem; font-weight:700; margin-bottom:0.5rem;">
        3
      </div><br>
      <span style="font-size:0.92rem; font-weight:700; color:#1a3a52; line-height:1.4;">Flanco de subida<br>ExecuteCW</span><br>
      <span style="font-size:0.8rem; color:#7a9ab0;">trigger 0 → 1</span>
    </td>
    <td style="text-align:center; color:#bcd6ec; font-size:1.6rem; width:4%; vertical-align:middle; padding-bottom:1.8rem;">
      <i class="ph ph-caret-right"></i>
    </td>
    <td style="text-align:center; padding:0 8px; width:22%;">
      <div style="width:52px; height:52px; border-radius:50%; background:#e3f1fb; border:2px solid #2980b9; display:inline-flex; align-items:center; justify-content:center; color:#2980b9; font-size:1.4rem; font-weight:700; margin-bottom:0.5rem;">
        4
      </div><br>
      <span style="font-size:0.92rem; font-weight:700; color:#1a3a52; line-height:1.4;">Esperar<br>Busy = 0</span><br>
      <span style="font-size:0.8rem; color:#7a9ab0;">y ReturnData_1 = CW</span>
    </td>
  </tr>
</table>


1. El sistema externo establece la **ControlWord** con el número del comando deseado.
2. Si el comando requiere un argumento, establece también **Data_1**.
3. Envía un flanco de subida en **ExecuteControlWord**.
4. Espera a que **Busy** vuelva a `0` y a que **ReturnData_1** devuelva el valor de la ControlWord (confirmación de ejecución correcta).

:::{warning}
No enviar un nuevo comando mientras **Busy** esté a `1`. El sistema ignorará el comando y **ReturnData_1** devolverá el valor `3` (sistema ocupado).
:::

---

(sec-io)=
## Variables de entrada y salida 

Estas variables son **las mismas para todos los protocolos de comunicación**: solo cambia la forma en que se intercambian (véanse [Transporte Fieldbus](#sec-fieldbus) y [Sintaxis TCP](#sec-tcp)).

### INPUT — Señales enviadas al FlexiBowl®

| Variable | Tipo | Descripción |
|---|---|---|
| **ControlWord** | UDINT | Número entero que identifica el comando que se debe ejecutar. Cada valor corresponde a una acción específica (véase la tabla de comandos). |
| **Data_1** | UDINT | Argumento numérico asociado a la ControlWord, cuando se requiere (p. ej. el valor de velocidad que se debe escribir). El significado depende del comando seleccionado. |
| **ExecuteControlWord** | BOOL | Señal de disparo: en el **flanco de subida** (de 0 a 1) se lee la ControlWord y se ejecuta el comando. |
| **Hopper_1** | BOOL | Activa directamente el Hopper 1, independientemente de la ControlWord. |
| **Hopper_2** | BOOL | Activa directamente el Hopper 2. |
| **Hopper_3** | BOOL | Activa directamente el Hopper 3. |
| **Hopper_4** | BOOL | Activa directamente el Hopper 4. |
| **Reset** | BOOL | En el flanco de subida, restablece los errores activos del dispositivo. |

### OUTPUT — Señales enviadas por el FlexiBowl®

| Variable | Tipo | Descripción |
|---|---|---|
| **Busy** | BOOL | Vale `1` mientras el FlexiBowl® ejecuta un comando. Mientras esté activo, no enviar nuevos comandos. |
| **Ready** | BOOL | Vale `1` cuando el dispositivo está listo para recibir nuevos comandos. |
| **In_Error** | BOOL | Vale `1` si hay errores activos en el dispositivo. Consulte **ErrorCode** para identificar el tipo de error. |
| **ReturnData_1** | UDINT | Confirmación del comando recibido (eco). Los valores posibles son: `0` = estado inicial (ningún comando), `1` = comando no interpretable, `2` = Data_1 erróneo pero comando reconocido, `3` = sistema ocupado (Busy), o el propio valor de la ControlWord = comando ejecutado correctamente. |
| **ReturnData_2** | UDINT | Contiene los datos solicitados por los comandos de lectura (READ). |
| **ErrorCode** | UDINT | Código numérico del error activo. Vale `0` si no hay errores. Véase la sección [Códigos de error](#codici-di-errore) para el significado de cada código. |
| **InPowerOn** | BOOL | Vale `1` si el dispositivo está alimentado y operativo. |


### Valores de ReturnData_1

<div class="isw-ret">
<style>
.isw-ret table thead tr,
.isw-ret table thead tr th {
  background: #f0f4f8 !important;
  color: #1a3a52 !important;
  border-bottom: 2px solid #2980b9 !important;
}
</style>
<table style="width:100%; border-collapse:collapse; font-size:0.95rem; margin:0.75rem 0 1.5rem;">
  <thead>
    <tr>
      <th style="padding:0.6rem 0.9rem; text-align:left; font-weight:700; white-space:nowrap; width:100px;">Valor</th>
      <th style="padding:0.6rem 0.9rem; text-align:left; font-weight:700;">Significado</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#fff;" onmouseover="this.style.background='#e8f4fc'" onmouseout="this.style.background='#fff'">
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; font-family:monospace; font-size:1.05rem; font-weight:700; color:#2980b9;">0</td>
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; color:#334e5e;">NULL — ningún comando en curso (estado inicial)</td>
    </tr>
    <tr style="background:#f7fbfe;" onmouseover="this.style.background='#e8f4fc'" onmouseout="this.style.background='#f7fbfe'">
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; font-family:monospace; font-size:1.05rem; font-weight:700; color:#2980b9;">1</td>
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; color:#334e5e;">Comando no interpretable (ControlWord desconocida)</td>
    </tr>
    <tr style="background:#fff;" onmouseover="this.style.background='#e8f4fc'" onmouseout="this.style.background='#fff'">
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; font-family:monospace; font-size:1.05rem; font-weight:700; color:#2980b9;">2</td>
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; color:#334e5e;">Data_1 fuera de rango, comando reconocido</td>
    </tr>
    <tr style="background:#f7fbfe;" onmouseover="this.style.background='#e8f4fc'" onmouseout="this.style.background='#f7fbfe'">
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; font-family:monospace; font-size:1.05rem; font-weight:700; color:#2980b9;">3</td>
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; color:#334e5e;">Sistema ocupado (Busy) — volver a intentarlo</td>
    </tr>
    <tr style="background:#fff;" onmouseover="this.style.background='#e8f4fc'" onmouseout="this.style.background='#fff'">
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; font-family:monospace; font-size:1.05rem; font-weight:700; color:#2980b9;">= CW</td>
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; color:#334e5e;">Comando ejecutado correctamente</td>
    </tr>
  </tbody>
</table>
</div>

---

(sec-fieldbus)=
## EtherNet/IP, Profinet, Modbus - <span class="isw-section-badge isw-badge-field"><i class="ph ph-swap"></i> FIELDBUS</span>

Para **EtherNet/IP**, **Profinet** y **Modbus**, las variables de [entrada](#sec-io) y [salida](#sec-io) se intercambian como un **paquete de E/S cíclico**: no existen mensajes de texto, cada variable ocupa una posición fija en el paquete de datos. Para toda la información detallada sobre este protocolo, consulte la [página siguiente](fieldbus).

### Paquete de datos — Input (hacia el FlexiBowl®)

| ControlWord | Data_1 | ExecuteControlWord | Hopper_1 | Hopper_2 | Hopper_3 | Hopper_4 | Reset |
|---|---|---|---|---|---|---|---|
| *(número de comando)* | *(argumento)* | *(bit de disparo 0→1)* | *(bit)* | *(bit)* | *(bit)* | *(bit)* | *(bit)* |

### Paquete de datos — Output (desde el FlexiBowl®)

| Busy | Ready | In_Error | In_PowerOn | ReturnData_1 | ReturnData_2 | ErrorCode |
|---|---|---|---|---|---|---|
| *(bit)* | *(bit)* | *(bit)* | *(bit)* | *(eco de la ControlWord)* | *(dato leído)* | *(código de error)* |

:::{note}
La secuencia de escritura es siempre la misma: establecer **ControlWord** (y **Data_1** si se requiere) con **ExecuteControlWord = 0**, y después llevar **ExecuteControlWord** a `1` para generar el flanco de subida que inicia la ejecución.
:::

:::{card} IR A LA PÁGINA CORRESPONDIENTE
:link: fieldbus
:link-type: ref
:class-card: isw-card-field
:class-body: isw-card-body

Documentación completa del protocolo Fieldbus (EtherNet/IP, Profinet, Modbus)
:::

---

(sec-tcp)=
## Sintaxis de mensajes <span class="isw-section-badge isw-badge-tcp"><i class="ph ph-network"></i> TCP SERVER</span>

Cuando se utiliza la comunicación **TCP Server**, los comandos no se envían como variables binarias sino como **cadenas de texto** a través de una conexión socket en el puerto configurado (por defecto: 8123). Para toda la información detallada sobre este protocolo, consulte la [página siguiente](tcp).

### Estructura del mensaje

Cada mensaje tiene la forma:

```
NomeVariabile[Valore]%
```

El carácter `%` es el **terminador de mensaje** y debe estar siempre presente al final. El campo `[Valore]` contiene el dato numérico asociado (ControlWord, estado, etc.).

:::{card} IR A LA PÁGINA CORRESPONDIENTE
:link: tcp
:link-type: ref
:class-card: isw-card-tcp
:class-body: isw-card-body

Sintaxis completa de los mensajes TCP Server, de los comandos y de los terminadores
:::
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

#### Ejemplo práctico 

Para ver un ejemplo práctico de comando EXE en fieldbus, consulte la sección [Ejemplo práctico EXE](fieldbus_exe).
Para ver un ejemplo práctico de comando EXE en TCP, consulte la sección [Ejemplo práctico EXE TCP](TCP_EXE).

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

#### Ejemplo práctico 

Para ver un ejemplo práctico de comando WRITE en fieldbus, consulte la sección [Ejemplo práctico WRITE](fieldbus_write).
Para ver un ejemplo práctico de comando WRITE en TCP, consulte la sección [Ejemplo práctico WRITE TCP](TCP_write).

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

#### Ejemplo práctico 

Para ver un ejemplo práctico de comando READ en fieldbus, consulte la sección [Ejemplo práctico READ](fieldbus_read).
Para ver un ejemplo práctico de comando READ en TCP, consulte la sección [Ejemplo práctico READ TCP](TCP_read).

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

#### Ejemplo práctico

Para ver un ejemplo práctico de comando WRITE HOPPER en fieldbus, consulte la sección [Ejemplo práctico WRITE HOPPER](fieldbus_WRITEHOPPER).
Para ver un ejemplo práctico de comando WRITE HOPPER en TCP, consulte la sección [Ejemplo práctico WRITE HOPPER TCP](TCP_WRITEHOPPER).

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

#### Ejemplo práctico 

Para ver un ejemplo práctico de comando READ HOPPER en fieldbus, consulte la sección [Ejemplo práctico READ HOPPER](fieldbus_READHOPPER).
Para ver un ejemplo práctico de comando READ HOPPER en TCP, consulte la sección [Ejemplo práctico READ HOPPER TCP](TCP_READHOPPER).

---

(sec-empty)=
## Comandos Quick Emptying — <span class="isw-section-badge isw-badge-exe"><i class="ph ph-arrow-counter-clockwise"></i> EMPTYING</span>

La función **Emptying** permite vaciar el plato del FlexiBowl® ejecutando hasta 4 secuencias específicas, cada una con su propio número de bucles. Estos comandos también siguen la misma lógica ControlWord, válida para todos los protocolos.

### Comandos EXE

| Comando | ControlWord | Busy durante la ejecución | ReturnData_1 | Explicación |
|---|---|---|---|---|
| Start Emptying | 45 | SÍ (Emptying activo) | 45 | Inicia el Quick Emptying  |
| Stop Emptying | 46 | SÍ (Emptying activo) | 46 | Detiene el Quick Emptying  |
| Emptying Active | 47 | NO | 47 | Comprueba si el Quick Emptying está activo |

### Comandos WRITE

| Comando | ControlWord | Range Data_1 | Busy durante la ejecución | ReturnData_1 |
|---|---|---|---|---|
| FirstSequence | 20200 | 1–20 | NO | 20200 |
| FirstLoop | 20201 | 0–500 | NO | 20201 |
| SecondSequence | 20202 | 1–20 | NO | 20202 |
| SecondLoop | 20203 | 0–500 | NO | 20203 |
| ThirdSequence | 20204 | 1–20 | NO | 20204 |
| ThirdLoop | 20205 | 0–500 | NO | 20205 |
| FourthSequence | 20206 | 1–20 | NO | 20206 |
| FourthLoop | 20207 | 0–500 | NO | 20207 |

### Comandos READ

| Comando | ControlWord | Busy durante la ejecución | ReturnData_1 | Range ReturnData_2 |
|---|---|---|---|---|
| FirstSequence | 20300 | NO | 20300 | 1–20 |
| FirstLoop | 20301 | NO | 20301 | 0–500 |
| SecondSequence | 20302 | NO | 20302 | 1–20 |
| SecondLoop | 20303 | NO | 20303 | 0–500 |
| ThirdSequence | 20304 | NO | 20304 | 1–20 |
| ThirdLoop | 20305 | NO | 20305 | 0–500 |
| FourthSequence | 20306 | NO | 20306 | 1–20 |
| FourthLoop | 20307 | NO | 20307 | 0–500 |

:::{note}
`FirstSequence`...`FourthSequence` indican cuál de las 20 secuencias programadas se ejecuta en cada uno de los 4 pasos del Quick Emptying; `FirstLoop`...`FourthLoop` indican cuántas veces se repite ese paso.
:::

---

(sec-err)=
## Códigos de error

:::{warning}
En presencia de un error, el LED **In_Error** se activa y el sistema no ejecutará nuevos comandos de movimiento hasta el reinicio. Antes de realizar el reinicio, identificar y resolver la causa del error.
:::


### Códigos generales

| ErrorCode | Descripción |
|---|---|
| 1 | El movimiento de jog no ha activado ninguna acción en el motor |
| 2 | Motor no conectado |
| 3 | EtherNet/IP seleccionado pero no conectado |
| 4 | El motor no ha alcanzado la potencia operativa dentro del tiempo preestablecido |
| 5 | Se ha solicitado un movimiento del motor, pero el motor no está alimentado |
| 6 | Error del módulo de E/S digital: módulo ausente |
| 7 | Error del módulo de E/S digital: error de configuración |
| 8 | Error del módulo de E/S digital: error general |

### Códigos de error del driver

<div class="isw-search-wrap">
  <input class="isw-search" id="errSearch" type="text" placeholder="Filtrar por código o descripción…" oninput="filterErrors()">
  <span class="isw-search-count" id="errCount"></span>
</div>

<div style="margin-top: 2rem;"></div>

<div class="isw-err-wrap">
<table class="isw-err-table" id="errTable">
<thead><tr><th>Código</th><th>Hex</th><th>Error</th><th>Descripción</th></tr></thead>
<tbody>
<tr><td><code>50</code></td><td><code>0x7500</code></td><td>EtherCAT communication error</td><td></td></tr>
<tr><td><code>51</code></td><td><code>0xFF01</code></td><td>Drive Over Current</td><td>Corriente del motor excesiva</td></tr>
<tr><td><code>52</code></td><td><code>0xFF02</code></td><td>Drive Over Voltage</td><td>Tensión excesiva del bus DC</td></tr>
<tr><td><code>53</code></td><td><code>0xFF03</code></td><td>Drive Over Temperature</td><td>Temperatura del driver demasiado alta</td></tr>
<tr><td><code>54</code></td><td><code>0xFF04</code></td><td>Reserved</td><td></td></tr>
<tr><td><code>55</code></td><td><code>0xFF05</code></td><td>Drive Internal Voltage Error</td><td>Error de tensión interna</td></tr>
<tr><td><code>56</code></td><td><code>0xFF06</code></td><td>Position Error</td><td>Error de posicionamiento</td></tr>
<tr><td><code>57</code></td><td><code>0xFF07</code></td><td>Motor Encoder Disconnected</td><td>Encoder no conectado o averiado</td></tr>
<tr><td><code>58</code></td><td><code>0xFF0A</code></td><td>Regen Failed</td><td>Error en el circuito de regeneración</td></tr>
<tr><td><code>59</code></td><td><code>0xFF0B</code></td><td>Safe Torque Off (STO)</td><td>Función de seguridad activa</td></tr>
<tr><td><code>60</code></td><td><code>0xFF0C</code></td><td>Reserved</td><td></td></tr>
<tr><td><code>61</code></td><td><code>0xFF0D</code></td><td>Bad FPGA</td><td>Error interno de la FPGA del driver</td></tr>
<tr><td><code>62</code></td><td><code>0xFF0E</code></td><td>Parameter Read Failed</td><td>Fallo en la lectura de parámetros</td></tr>
<tr><td><code>63</code></td><td><code>0xFF0F</code></td><td>Motor Encoder Multi-turn Error</td><td>Error del encoder multivuelta</td></tr>
<tr><td><code>64</code></td><td><code>0xFF10</code></td><td>Motor Stall Protection</td><td>Protección contra bloqueo del motor activa</td></tr>
<tr><td><code>65</code></td><td><code>0xFF11</code></td><td>Drive Power Module Over Temperature</td><td>Módulo de potencia sobrecalentado</td></tr>
<tr><td><code>66</code></td><td><code>0xFF31</code></td><td>N Limit</td><td>Límite de posición negativo alcanzado</td></tr>
<tr><td><code>67</code></td><td><code>0xFF32</code></td><td>P Limit</td><td>Límite de posición positivo alcanzado</td></tr>
<tr><td><code>68</code></td><td><code>0xFF33</code></td><td>N&P Limit</td><td>Ambos límites de posición alcanzados</td></tr>
<tr><td><code>69</code></td><td><code>0xFF34</code></td><td>Current Foldback</td><td>Reducción de corriente por protección térmica</td></tr>
<tr><td><code>70</code></td><td><code>0xFF35</code></td><td>Move @ Disabled</td><td>Intento de movimiento con el driver deshabilitado</td></tr>
<tr><td><code>71</code></td><td><code>0xFF36</code></td><td>Drive Low Voltage</td><td>Tensión insuficiente del bus DC</td></tr>
<tr><td><code>72</code></td><td><code>0xFF37</code></td><td>Blank Q Segment</td><td>Segmento de trayectoria no definido</td></tr>
<tr><td><code>73</code></td><td><code>0xFF38</code></td><td>Velocity Limit</td><td>Límite de velocidad superado</td></tr>
<tr><td><code>74</code></td><td><code>0xFF39</code></td><td>Drive Power Phase Lost</td><td>Pérdida de una fase de alimentación</td></tr>
<tr><td><code>75</code></td><td><code>0xFF3A</code></td><td>Emergency Stop</td><td>Parada de emergencia activa</td></tr>
<tr><td><code>76</code></td><td><code>0xFF3B</code></td><td>Abs. Encoder Battery</td><td>Batería del encoder absoluto baja o ausente</td></tr>
<tr><td><code>77</code></td><td><code>0xFF3C</code></td><td>Abs. Position Lost Warning</td><td>Aviso de pérdida de posición absoluta</td></tr>
<tr><td><code>78</code></td><td><code>0xFF3D</code></td><td>Abs. Position Overflow</td><td>Desbordamiento de la posición absoluta</td></tr>
<tr><td><code>79</code></td><td><code>0xFF3E</code></td><td>Motor Over Temperature</td><td>Temperatura del motor excesiva</td></tr>
<tr><td><code>80</code></td><td><code>0xFF3F</code></td><td>Drive Voltage Warning</td><td>Aviso de tensión del driver fuera de rango</td></tr>
<tr><td><code>81</code></td><td><code>0xFF41</code></td><td>Save Failed</td><td>Fallo al guardar los parámetros</td></tr>
<tr><td><code>82</code></td><td><code>0xFFFF</code></td><td>Other Error</td><td>Error genérico no clasificado</td></tr>
</tbody>
</table>
</div>

<script>
function filterErrors() {
  var input = document.getElementById('errSearch').value.toLowerCase();
  var rows = document.querySelectorAll('#errTable tbody tr');
  var count = 0;
  rows.forEach(function(row) {
    var text = row.textContent.toLowerCase();
    if (text.includes(input)) {
      row.classList.remove('isw-hidden');
      count++;
    } else {
      row.classList.add('isw-hidden');
    }
  });
  var countEl = document.getElementById('errCount');
  if (input) {
    countEl.textContent = count + ' ' + (count === 1 ? 'resultado' : 'resultados');
  } else {
    countEl.textContent = '';
  }
}
</script>

</div>


:::{toctree}
:hidden:
04a_interfaccia_software.md
04b_interfaccia_software.md
04c_interfaccia_software.md
:::