(int_software)=
# **Software-Schnittstelle**

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

## Einführung

Die neue FlexiBowl®-Oberfläche ist vollständig webbasiert. Für den Zugriff genügt es, die Standard-IP-Adresse des FlexiBowl® `192.168.1.10` in die Adressleiste Ihres Browsers einzugeben.

:::{video} ../../../../_shared/media/videos/IP_Home.mp4
:width: 90%
:::


## Kommunikation 

Das Kommunikationssystem basiert auf **Ein-/Ausgangsvariablen** und numerischen **Control Words**: Das externe System sendet eine Zahl (das ControlWord), die die auszuführende Aktion kennzeichnet, und der FlexiBowl® antwortet mit Statussignalen und Rückgabedaten.

Unterstützte Protokolle:
- **TCP Server**
- **EtherNet/IP**
- **Profinet**
- **Modbus**

:::{important}
Die Variablen, ControlWords und alle auf dieser Seite beschriebenen Befehle **EXE**, **WRITE** und **READ** sind **für alle vier Kommunikationsprotokolle identisch**. Was sich von Protokoll zu Protokoll ändert, ist **ausschließlich die Art, wie diese Daten physisch ausgetauscht werden**:

- **EtherNet/IP, Profinet und Modbus** verhalten sich untereinander gleich: Sie tauschen ein **zyklisches I/O-Paket** mit festen Feldern aus (siehe [Fieldbus-Transport](#sec-fieldbus)).
- **TCP Server** verwendet dagegen **Textnachrichten** über einen Socket (siehe [TCP-Syntax](#sec-tcp)).

Aus diesem Grund wird jedes Praxisbeispiel auf dieser Seite in beiden Modi gezeigt.
:::

---

### Seite durchsuchen

<div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:1rem; margin:1.5rem 0 2.5rem;">

  <a href="#sec-io" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit; transition:border-color 0.18s, background 0.18s;">
    <i class="ph ph-arrows-left-right" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">I/O-Variablen</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Eingang & Ausgang</span>
  </a>

  <a href="#sec-fieldbus" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-swap" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Fieldbus-Transport</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">EtherNet/IP, Profinet, Modbus</span>
  </a>

  <a href="#sec-tcp" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-network" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">TCP-Syntax</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Socket-Nachrichten</span>
  </a>

  <a href="#sec-exe" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-play-circle" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">EXE-Befehle</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Sequenzen starten & Jog</span>
  </a>

  <a href="#sec-write" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-pencil-simple" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">WRITE-Befehle</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Parameter schreiben</span>
  </a>

  <a href="#sec-read" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-eye" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">READ-Befehle</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Parameter lesen</span>
  </a>

  <a href="#sec-hopper" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-funnel" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Hopper-Befehle</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Bulk Feeder</span>
  </a>

  <a href="#sec-empty" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-arrow-counter-clockwise" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Quick Emptying</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Option Entleerung</span>
  </a>

  <a href="#sec-err" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-warning-circle" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Fehlercodes</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Diagnose</span>
  </a>

</div>

---

### So funktioniert ein Befehl

Diese Logik ist **für alle Protokolle identisch**: Es ändert sich nur die Art, wie die 4 Schritte physisch übertragen werden (I/O-Paket bei den Fieldbus-Protokollen, Textnachricht bei TCP — siehe die folgenden Abschnitte).

<table style="width:100%; border-collapse:collapse; margin: 1.5rem 0 2rem;">
  <tr>
    <td style="text-align:center; padding:0 8px; width:22%;">
      <div style="width:52px; height:52px; border-radius:50%; background:#e3f1fb; border:2px solid #2980b9; display:inline-flex; align-items:center; justify-content:center; color:#2980b9; font-size:1.4rem; font-weight:700; margin-bottom:0.5rem;">
        1
      </div><br>
      <span style="font-size:0.92rem; font-weight:700; color:#1a3a52; line-height:1.4;">Setzen<br>ControlWord</span><br>
      <span style="font-size:0.8rem; color:#7a9ab0;">Befehlsnummer</span>
    </td>
    <td style="text-align:center; color:#bcd6ec; font-size:1.6rem; width:4%; vertical-align:middle; padding-bottom:1.8rem;">
      <i class="ph ph-caret-right"></i>
    </td>
    <td style="text-align:center; padding:0 8px; width:22%;">
      <div style="width:52px; height:52px; border-radius:50%; background:#e3f1fb; border:2px solid #2980b9; display:inline-flex; align-items:center; justify-content:center; color:#2980b9; font-size:1.4rem; font-weight:700; margin-bottom:0.5rem;">
        2
      </div><br>
      <span style="font-size:0.92rem; font-weight:700; color:#1a3a52; line-height:1.4;">Setzen<br>Data_1</span><br>
      <span style="font-size:0.8rem; color:#7a9ab0;">falls erforderlich</span>
    </td>
    <td style="text-align:center; color:#bcd6ec; font-size:1.6rem; width:4%; vertical-align:middle; padding-bottom:1.8rem;">
      <i class="ph ph-caret-right"></i>
    </td>
    <td style="text-align:center; padding:0 8px; width:22%;">
      <div style="width:52px; height:52px; border-radius:50%; background:#e3f1fb; border:2px solid #2980b9; display:inline-flex; align-items:center; justify-content:center; color:#2980b9; font-size:1.4rem; font-weight:700; margin-bottom:0.5rem;">
        3
      </div><br>
      <span style="font-size:0.92rem; font-weight:700; color:#1a3a52; line-height:1.4;">Steigende Flanke<br>ExecuteCW</span><br>
      <span style="font-size:0.8rem; color:#7a9ab0;">trigger 0 → 1</span>
    </td>
    <td style="text-align:center; color:#bcd6ec; font-size:1.6rem; width:4%; vertical-align:middle; padding-bottom:1.8rem;">
      <i class="ph ph-caret-right"></i>
    </td>
    <td style="text-align:center; padding:0 8px; width:22%;">
      <div style="width:52px; height:52px; border-radius:50%; background:#e3f1fb; border:2px solid #2980b9; display:inline-flex; align-items:center; justify-content:center; color:#2980b9; font-size:1.4rem; font-weight:700; margin-bottom:0.5rem;">
        4
      </div><br>
      <span style="font-size:0.92rem; font-weight:700; color:#1a3a52; line-height:1.4;">Warten<br>Busy = 0</span><br>
      <span style="font-size:0.8rem; color:#7a9ab0;">und ReturnData_1 = CW</span>
    </td>
  </tr>
</table>


1. Das externe System setzt das **ControlWord** auf die Nummer des gewünschten Befehls.
2. Erfordert der Befehl ein Argument, setzt es außerdem **Data_1**.
3. Sendet eine steigende Flanke auf **ExecuteControlWord**.
4. Wartet, bis **Busy** wieder auf `0` zurückkehrt und **ReturnData_1** den Wert des ControlWord zurückgibt (Bestätigung der korrekten Ausführung).

:::{warning}
Keinen neuen Befehl senden, solange **Busy** `1` ist. Das System ignoriert den Befehl, und **ReturnData_1** gibt den Wert `3` zurück (System belegt).
:::

---

(sec-io)=
## Ein- und Ausgangsvariablen 

Diese Variablen sind **für alle Kommunikationsprotokolle gleich**: Es ändert sich nur die Art ihres Austauschs (siehe [Fieldbus-Transport](#sec-fieldbus) und [TCP-Syntax](#sec-tcp)).

### INPUT — An den FlexiBowl® gesendete Signale

| Variable | Typ | Beschreibung |
|---|---|---|
| **ControlWord** | UDINT | Ganzzahl, die den auszuführenden Befehl kennzeichnet. Jeder Wert entspricht einer bestimmten Aktion (siehe Befehlstabelle). |
| **Data_1** | UDINT | Dem ControlWord zugeordnetes numerisches Argument, falls erforderlich (z. B. der zu schreibende Geschwindigkeitswert). Die Bedeutung hängt vom gewählten Befehl ab. |
| **ExecuteControlWord** | BOOL | Triggersignal: Bei der **steigenden Flanke** (von 0 auf 1) wird das ControlWord gelesen und der Befehl ausgeführt. |
| **Hopper_1** | BOOL | Aktiviert Hopper 1 direkt, unabhängig vom ControlWord. |
| **Hopper_2** | BOOL | Aktiviert Hopper 2 direkt. |
| **Hopper_3** | BOOL | Aktiviert Hopper 3 direkt. |
| **Hopper_4** | BOOL | Aktiviert Hopper 4 direkt. |
| **Reset** | BOOL | Setzt bei der steigenden Flanke die am Gerät aktiven Fehler zurück. |

### OUTPUT — Vom FlexiBowl® gesendete Signale

| Variable | Typ | Beschreibung |
|---|---|---|
| **Busy** | BOOL | Ist `1`, während der FlexiBowl® einen Befehl ausführt. Solange es aktiv ist, keine neuen Befehle senden. |
| **Ready** | BOOL | Ist `1`, wenn das Gerät bereit ist, neue Befehle zu empfangen. |
| **In_Error** | BOOL | Ist `1`, wenn am Gerät aktive Fehler vorliegen. **ErrorCode** prüfen, um die Fehlerart zu identifizieren. |
| **ReturnData_1** | UDINT | Bestätigung des empfangenen Befehls (Echo). Mögliche Werte: `0` = Anfangszustand (kein Befehl), `1` = Befehl nicht interpretierbar, `2` = falsches Data_1, aber Befehl erkannt, `3` = System belegt (Busy), oder der Wert des ControlWord selbst = Befehl korrekt ausgeführt. |
| **ReturnData_2** | UDINT | Enthält die von den Lesebefehlen (READ) angeforderten Daten. |
| **ErrorCode** | UDINT | Numerischer Code des aktiven Fehlers. Ist `0`, wenn keine Fehler vorliegen. Die Bedeutung der einzelnen Codes finden Sie im Abschnitt [Fehlercodes](#codici-di-errore). |
| **InPowerOn** | BOOL | Ist `1`, wenn das Gerät mit Spannung versorgt und betriebsbereit ist. |


### Werte von ReturnData_1

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
      <th style="padding:0.6rem 0.9rem; text-align:left; font-weight:700; white-space:nowrap; width:100px;">Wert</th>
      <th style="padding:0.6rem 0.9rem; text-align:left; font-weight:700;">Bedeutung</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#fff;" onmouseover="this.style.background='#e8f4fc'" onmouseout="this.style.background='#fff'">
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; font-family:monospace; font-size:1.05rem; font-weight:700; color:#2980b9;">0</td>
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; color:#334e5e;">NULL — kein Befehl in Bearbeitung (Anfangszustand)</td>
    </tr>
    <tr style="background:#f7fbfe;" onmouseover="this.style.background='#e8f4fc'" onmouseout="this.style.background='#f7fbfe'">
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; font-family:monospace; font-size:1.05rem; font-weight:700; color:#2980b9;">1</td>
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; color:#334e5e;">Befehl nicht interpretierbar (unbekanntes ControlWord)</td>
    </tr>
    <tr style="background:#fff;" onmouseover="this.style.background='#e8f4fc'" onmouseout="this.style.background='#fff'">
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; font-family:monospace; font-size:1.05rem; font-weight:700; color:#2980b9;">2</td>
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; color:#334e5e;">Data_1 außerhalb des Bereichs, Befehl erkannt</td>
    </tr>
    <tr style="background:#f7fbfe;" onmouseover="this.style.background='#e8f4fc'" onmouseout="this.style.background='#f7fbfe'">
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; font-family:monospace; font-size:1.05rem; font-weight:700; color:#2980b9;">3</td>
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; color:#334e5e;">System belegt (Busy) — erneut versuchen</td>
    </tr>
    <tr style="background:#fff;" onmouseover="this.style.background='#e8f4fc'" onmouseout="this.style.background='#fff'">
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; font-family:monospace; font-size:1.05rem; font-weight:700; color:#2980b9;">= CW</td>
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; color:#334e5e;">Befehl korrekt ausgeführt</td>
    </tr>
  </tbody>
</table>
</div>

---

(sec-fieldbus)=
## EtherNet/IP, Profinet, Modbus - <span class="isw-section-badge isw-badge-field"><i class="ph ph-swap"></i> FIELDBUS</span>

Bei **EtherNet/IP**, **Profinet** und **Modbus** werden die [Eingangs-](#sec-io) und [Ausgangsvariablen](#sec-io) als **zyklisches I/O-Paket** ausgetauscht: Es gibt keine Textnachrichten, jede Variable belegt eine feste Position im Datenpaket. Alle detaillierten Informationen zu diesem Protokoll finden Sie auf der [nächsten](fieldbus) Seite.

### Datenpaket — Input (zum FlexiBowl®)

| ControlWord | Data_1 | ExecuteControlWord | Hopper_1 | Hopper_2 | Hopper_3 | Hopper_4 | Reset |
|---|---|---|---|---|---|---|---|
| *(Befehlsnummer)* | *(Argument)* | *(Trigger-Bit 0→1)* | *(Bit)* | *(Bit)* | *(Bit)* | *(Bit)* | *(Bit)* |

### Datenpaket — Output (vom FlexiBowl®)

| Busy | Ready | In_Error | In_PowerOn | ReturnData_1 | ReturnData_2 | ErrorCode |
|---|---|---|---|---|---|---|
| *(Bit)* | *(Bit)* | *(Bit)* | *(Bit)* | *(Echo des ControlWord)* | *(gelesener Wert)* | *(Fehlercode)* |

:::{note}
Die Schreibsequenz ist immer dieselbe: **ControlWord** (und ggf. **Data_1**) mit **ExecuteControlWord = 0** setzen, dann **ExecuteControlWord** auf `1` bringen, um die steigende Flanke zu erzeugen, die die Ausführung startet.
:::

:::{card} ZUR ENTSPRECHENDEN SEITE
:link: fieldbus
:link-type: ref
:class-card: isw-card-field
:class-body: isw-card-body

Vollständige Dokumentation des Fieldbus-Protokolls (EtherNet/IP, Profinet, Modbus)
:::

---

(sec-tcp)=
## Nachrichtensyntax <span class="isw-section-badge isw-badge-tcp"><i class="ph ph-network"></i> TCP SERVER</span>

Bei Verwendung der **TCP-Server**-Kommunikation werden die Befehle nicht als binäre Variablen, sondern als **Textzeichenfolgen** über eine Socket-Verbindung auf dem konfigurierten Port (Standard: 8123) gesendet. Alle detaillierten Informationen zu diesem Protokoll finden Sie auf der [nächsten](tcp) Seite.

### Nachrichtenstruktur

Jede Nachricht hat folgende Form:

```
NomeVariabile[Valore]%
```

Das Zeichen `%` ist der **Nachrichtenabschluss** und muss am Ende immer vorhanden sein. Das Feld `[Valore]` enthält die zugehörigen numerischen Daten (ControlWord, Status usw.).

:::{card} ZUR ENTSPRECHENDEN SEITE
:link: tcp
:link-type: ref
:class-card: isw-card-tcp
:class-body: isw-card-body

Vollständige Syntax der TCP-Server-Nachrichten, -Befehle und -Abschlusszeichen
:::
---

## Befehlsprotokoll

Das Befehlsprotokoll definiert alle über das ControlWord verfügbaren Aktionen. Die ControlWords sind **für alle Protokolle gleich**; es ändert sich nur der Transport (siehe [Fieldbus-Transport](#sec-fieldbus) und [TCP-Syntax](#sec-tcp)). Die Befehle sind in Kategorien gruppiert:

<div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:1rem; margin:1.5rem 0 2.5rem;">

  <a href="#sec-exe" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-play-circle" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">EXE-Befehle</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Ausführungsbefehle (Sequenzen starten, Jog, Reset)</span>
  </a>

  <a href="#sec-write" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-pencil-simple" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">WRITE-Befehle</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Schreiben von Parametern (Geschwindigkeit, Winkel, Zeiten usw.)</span>
  </a>

  <a href="#sec-read" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-eye" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">READ-Befehle</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Lesen der aktuell konfigurierten Parameter</span>
  </a>

</div>

(sec-exe)=
### Befehle <span class="isw-section-badge isw-badge-exe"><i class="ph ph-play-circle"></i> EXE</span>

EXE-Befehle starten eine sofortige Aktion am FlexiBowl®. Während der Ausführung bleibt **Busy** auf `1`.

| Befehl | ControlWord | Busy während der Ausführung | ReturnData_1 | Erläuterung | 
|---|---|---|---|---|
| Exe Seq 1 | 10 | JA | 10 | Sequenz 1 ausführen |
| Exe Seq 2 | 11 | JA | 11 | Sequenz 2 ausführen |
| Exe Seq 3 | 12 | JA | 12 | Sequenz 3 ausführen |
| Exe Seq 4 | 13 | JA | 13 | Sequenz 4 ausführen |
| Exe Seq 5 | 14 | JA | 14 | Sequenz 5 ausführen |
| Exe Seq 6 | 15 | JA | 15 | Sequenz 6 ausführen |
| Exe Seq 7 | 16 | JA | 16 | Sequenz 7 ausführen |
| Exe Seq 8 | 17 | JA | 17 | Sequenz 8 ausführen |
| Exe Seq 9 | 18 | JA | 18 | Sequenz 9 ausführen |
| Exe Seq 10 | 19 | JA | 19 | Sequenz 10 ausführen |
| Exe Seq 11 | 20 | JA | 20 | Sequenz 11 ausführen |
| Exe Seq 12 | 21 | JA | 21 | Sequenz 12 ausführen |
| Exe Seq 13 | 22 | JA | 22 | Sequenz 13 ausführen |
| Exe Seq 14 | 23 | JA | 23 | Sequenz 14 ausführen |
| Exe Seq 15 | 24 | JA | 24 | Sequenz 15 ausführen |
| Exe Seq 16 | 25 | JA | 25 | Sequenz 16 ausführen |
| Exe Seq 17 | 26 | JA | 26 | Sequenz 17 ausführen |
| Exe Seq 18 | 27 | JA | 27 | Sequenz 18 ausführen |
| Exe Seq 19 | 28 | JA | 28 | Sequenz 19 ausführen |
| Exe Seq 20 | 29 | JA | 29 | Sequenz 20 ausführen |
| Start Jog Seq | 40 | JA | 40 | Jog starten |
| Stop Jog Seq | 41 | JA | 41 | Jog stoppen |
| Reset Return Data | 50 | NEIN | 0 | Setzt den Wert von ReturnData_1 und ReturnData_2 zurück und bringt sie in den Anfangszustand `0` |

:::{note}
Der Befehl **Reset Return Data** (ControlWord 50) setzt den Wert von ReturnData_1 und ReturnData_2 zurück und bringt sie in den Anfangszustand `0`. Er ist nützlich, um zu überprüfen, dass ein neuer Befehl tatsächlich empfangen und verarbeitet wird.
:::

#### Praxisbeispiel 

Ein Praxisbeispiel für einen EXE-Befehl über Fieldbus finden Sie im Abschnitt [Praxisbeispiel EXE](fieldbus_exe).
Ein Praxisbeispiel für einen EXE-Befehl über TCP finden Sie im Abschnitt [Praxisbeispiel EXE TCP](TCP_EXE).

(sec-write)=
### Befehle <span class="isw-section-badge isw-badge-write"><i class="ph ph-pencil-simple"></i> WRITE</span>

Mit den WRITE-Befehlen können die Betriebsparameter des FlexiBowl® (Geschwindigkeit, Winkel, Zeiten usw.) direkt vom externen System aus geändert werden, ohne die grafische Oberfläche aufrufen zu müssen.

#### Adressierungslogik der Sequenzen

Jede Sequenz (von 1 bis 20) hat einen eigenen Parameterblock. Das ControlWord wird mit folgender Formel berechnet:

> **ControlWord = N × 100 + parameter_offset**

wobei `N` die Sequenznummer (1–20) ist und `offset_parametro` den jeweiligen Parameter kennzeichnet.

#### Beschreibbare Parameter für jede Sequenz

| Parameter | Offset | Range Data_1 | Hinweise |
|---|---|---|---|
| AccelerationMove | 00 | 1–100 | Beschleunigungsrampe der Drehbewegung (%) |
| DecelerationMove | 01 | 1–100 | Verzögerungsrampe der Drehbewegung (%) |
| SpeedMove | 02 | 1–100 | Geschwindigkeit der Drehbewegung (%) |
| AngleMove | 03 | 0–720 | Drehwinkel in Grad. Werte 1000–1720 = negativer Winkel (entgegengesetzte Richtung) |
| AccelerationShake | 04 | 1–100 | Beschleunigungsrampe des Shake (%) |
| DecelerationShake | 05 | 1–100 | Verzögerungsrampe des Shake (%) |
| CountShake | 06 | 2–20 | Anzahl der Schwingungen pro Shake-Zyklus |
| CwAngleShake | 07 | 0–360 | Drehwinkel im Uhrzeigersinn während des Shake. Werte 1000–1360 = negativer Winkel |
| CcwAngleShake | 08 | 0–360 | Drehwinkel gegen den Uhrzeigersinn während des Shake. Werte 1000–1360 = negativer Winkel |
| SpeedShake | 09 | 1–100 | Geschwindigkeit des Shake (%) |
| FlipCount | 10 | 0–20 | Anzahl der Flips pro Zyklus |
| FlipDelay | 11 | 0–500 | Pause zwischen einem Flip und dem nächsten (ms) |
| BlowDelay | 12 | 0–500 | Pause zwischen einem Blasimpuls und dem nächsten (ms) |
| ProportionalValve_Flip | 13 | 0–600 | Druck des Proportionalventils Flip (Wert /100 = Bar) |
| ProportionalValve_Blow | 14 | 0–600 | Druck des Proportionalventils Blow (Wert /100 = Bar) |
| Delete all sequence | 30 | — | Löscht alle Befehle aus der Sequenzliste |
| Emptying Sequence | 40 | 0–1 | 0 = Normalmodus, 1 = Modus Quick Emptying |
| Seq Add Cmd | 50 | FLB-BEFEHL | Fügt der Sequenzliste einen Befehl hinzu |

#### Beispiele für WRITE-ControlWords

| Sequenz | Parameter | Dem Parameter zugeordneter Offset | Formel (N x 100 + Offset) | ControlWord |
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
Die Formel ist einfach:
- Um die Geschwindigkeit (Offset 02) der Sequenz 7 zu schreiben, lautet das ControlWord `7 × 100 + 2 = 702`.
- Um den FlipCount (Offset 10) der Sequenz 15 zu schreiben, lautet das ControlWord `15 × 100 + 10 = 1510`.
:::

#### Praxisbeispiel 

Ein Praxisbeispiel für einen WRITE-Befehl über Fieldbus finden Sie im Abschnitt [Praxisbeispiel WRITE](fieldbus_write).
Ein Praxisbeispiel für einen WRITE-Befehl über TCP finden Sie im Abschnitt [Praxisbeispiel WRITE TCP](TCP_write).

#### WRITE-JOG-Parameter

Die Jog-Parameter (kontinuierlicher Handbetrieb) sind separat über ControlWord im Block 20000 konfigurierbar.

| Parameter | ControlWord | Range Data_1 | Hinweise |
|---|---|---|---|
| AccelerationJog | 20001 | 0–100 | Jog-Beschleunigungsrampe (%) |
| DecelerationJog | 20002 | 0–100 | Jog-Verzögerungsrampe (%) |
| SpeedJog | 20003 | 0–100 | Jog-Geschwindigkeit (%). Werte 1000–1100 = negative Geschwindigkeit (Drehrichtungsumkehr) |
| FlipJog_Enable | 20004 | 0–1 | 0 = Flip deaktiviert, 1 = Flip während des Jog aktiviert |
| FlipJog_Duration | 20005 | 0–1000 | Dauer des Flip-Impulses (ms) |
| FlipJog_Pressure | 20006 | 0–600 | Flip-Druck (/100 = Bar) |
| FlipJog_Pause | 20007 | 0–1000 | Pause zwischen aufeinanderfolgenden Flips (ms) |
| BlowJog_Enable | 20008 | 0–1 | 0 = Blow deaktiviert, 1 = Blow während des Jog aktiviert |
| BlowJog_Duration | 20009 | 0–1000 | Dauer des Blow-Impulses (ms) |
| BlowJog_Pressure | 20010 | 0–600 | Blow-Druck (/100 = Bar) |
| BlowJog_Pause | 20011 | 0–1000 | Pause zwischen aufeinanderfolgenden Blows (ms) |
| BlowJog_Type | 20012 | 0–2 | Blow-Typ: 0 = BLOWc, 1 = BLOWe, 2 = BLOWc+BLOWe |
| Backlight_1 | 20013 | 0–1 | 0 = aus, 1 = ein |
| Backlight_2 | 20014 | 0–1 | 0 = aus, 1 = ein |

---

(sec-read)=
### Befehle <span class="isw-section-badge isw-badge-read"><i class="ph ph-eye"></i> READ</span>

Mit den READ-Befehlen können die aktuell im FlexiBowl® konfigurierten Parameter gelesen werden. Der gelesene Wert wird in **ReturnData_2** zurückgegeben.

#### READ-Adressierungslogik für Sequenzen

Das ControlWord für das Lesen wird mit folgender Formel berechnet:

> **ControlWord = 10000 + N × 100 + parameter_offset**

wobei `N` die Sequenznummer (1–20) ist und `offset_parametro` derselbe ist wie bei den WRITE-Befehlen.

Die lesbaren Parameter sind dieselben wie im WRITE-Block, ergänzt um die 10 Slots der Befehlsliste:

| Zusätzlicher Parameter | Offset | Beschreibung |
|---|---|---|
| Seq Slot 1 Cmd | 50 | Befehl an Position 1 in der Sequenzliste |
| Seq Slot 2 Cmd | 51 | Befehl an Position 2 |
| … | … | … |
| Seq Slot 10 Cmd | 59 | Befehl an Position 10 |

#### Beispiele für READ-ControlWords

| Sequenz | Parameter | ControlWord |
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
Schnellformel:
 Um die Geschwindigkeit (Offset 02) der Sequenz 12 zu lesen, lautet das ControlWord `10000 + 12 × 100 + 2 = 11202`.
:::

#### Praxisbeispiel 

Ein Praxisbeispiel für einen READ-Befehl über Fieldbus finden Sie im Abschnitt [Praxisbeispiel READ](fieldbus_read).
Ein Praxisbeispiel für einen READ-Befehl über TCP finden Sie im Abschnitt [Praxisbeispiel READ TCP](TCP_read).

#### READ-JOG-Parameter

Dieselben beschreibbaren JOG-Parameter (Block 20000) können im Block 20100 gelesen werden:

| Parameter | READ-ControlWord | Bereich ReturnData_2 |
|---|---|---|
| AccelerationJog | 20101 | 0–100 |
| DecelerationJog | 20102 | 0–100 |
| SpeedJog | 20103 | 0–100 (1000–1100 = negativ) |
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
## Befehle <span class="isw-section-badge isw-badge-hop"><i class="ph ph-funnel"></i> HOPPER</span>

Die Hopper-Befehle steuern die an das System angeschlossenen Bulk Feeder (bis zu 4). Sie folgen derselben oben beschriebenen ControlWord-/WRITE-/READ-Logik, die für alle Protokolle gilt, sowie einer dedizierten TCP-Syntax für den Schnellstart.

### Hopper-WRITE-Befehle

| Parameter | ControlWord | Range Data_1 | Beschreibung |
|---|---|---|---|
| Hopper_1_Id | 30001 | 1–100 | Eindeutige ID des Hoppers 1 im Netzwerk |
| Hopper_1_Amplitude | 30002 | 50–220 | Schwingungsamplitude von Hopper 1 |
| Hopper_1_Frequency | 30003 | 40–70 | Schwingungsfrequenz von Hopper 1 |
| Hopper_1_Activation_Time | 30004 | 400–60000 | Aktivierungszeit von Hopper 1 (ms) |
| Hopper_2_Id | 30005 | 1–100 | Eindeutige ID des Hoppers 2 |
| Hopper_2_Amplitude | 30006 | 50–220 | Schwingungsamplitude von Hopper 2 |
| Hopper_2_Frequency | 30007 | 40–70 | Schwingungsfrequenz von Hopper 2 |
| Hopper_2_Activation_Time | 30008 | 400–60000 | Aktivierungszeit von Hopper 2 (ms) |
| Hopper_3_Id | 30009 | 1–100 | Eindeutige ID des Hoppers 3 |
| Hopper_3_Amplitude | 30010 | 50–220 | Schwingungsamplitude von Hopper 3 |
| Hopper_3_Frequency | 30011 | 40–70 | Schwingungsfrequenz von Hopper 3 |
| Hopper_3_Activation_Time | 30012 | 400–60000 | Aktivierungszeit von Hopper 3 (ms) |
| Hopper_4_Id | 30013 | 1–100 | Eindeutige ID des Hoppers 4 |
| Hopper_4_Amplitude | 30014 | 50–220 | Schwingungsamplitude von Hopper 4 |
| Hopper_4_Frequency | 30015 | 40–70 | Schwingungsfrequenz von Hopper 4 |
| Hopper_4_Activation_Time | 30016 | 400–60000 | Aktivierungszeit von Hopper 4 (ms) |
| Hopper_1_Enable | 30017 | — | Hopper 1 aktivieren (sofortige Aktion) |
| Hopper_1_Disable | 30018 | — | Hopper 1 deaktivieren (sofortige Aktion) |
| Hopper_2_Enable | 30019 | — | Hopper 2 aktivieren |
| Hopper_2_Disable | 30020 | — | Hopper 2 deaktivieren |
| Hopper_3_Enable | 30021 | — | Hopper 3 aktivieren |
| Hopper_3_Disable | 30022 | — | Hopper 3 deaktivieren |
| Hopper_4_Enable | 30023 | — | Hopper 4 aktivieren |
| Hopper_4_Disable | 30024 | — | Hopper 4 deaktivieren |

:::{note}
Im Schulungsmaterial wies das ControlWord `30005` (Hopper_2_Id) irrtümlich denselben Bereich wie die Amplitude auf (50–220). In dieser Tabelle wurde er auf **1–100** korrigiert, konsistent mit Hopper_1_Id, Hopper_3_Id und Hopper_4_Id. Diesen Wert vor der Veröffentlichung der Seite anhand von Firmware/Datenblatt überprüfen.
:::

#### Praxisbeispiel

Ein Praxisbeispiel für einen WRITE-HOPPER-Befehl über Fieldbus finden Sie im Abschnitt [Praxisbeispiel WRITE HOPPER](fieldbus_WRITEHOPPER).
Ein Praxisbeispiel für einen WRITE-HOPPER-Befehl über TCP finden Sie im Abschnitt [Praxisbeispiel WRITE HOPPER TCP](TCP_WRITEHOPPER).

### Hopper-READ-Befehle

| Parameter | READ-ControlWord | Range ReturnData_2 | Hinweise |
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
| Hopper_1_Ready | 30117 | 0–1 | 0 = nicht bereit, 1 = bereit |
| Hopper_2_Ready | 30118 | 0–1 | 0 = nicht bereit, 1 = bereit |
| Hopper_3_Ready | 30119 | 0–1 | 0 = nicht bereit, 1 = bereit |
| Hopper_4_Ready | 30120 | 0–1 | 0 = nicht bereit, 1 = bereit |
| Hopper_1_InVibration | 30121 | 0–1 | 0 = steht still, 1 = vibriert |
| Hopper_2_InVibration | 30122 | 0–1 | 0 = steht still, 1 = vibriert |
| Hopper_3_InVibration | 30123 | 0–1 | 0 = steht still, 1 = vibriert |
| Hopper_4_InVibration | 30124 | 0–1 | 0 = steht still, 1 = vibriert |
| Hopper_1_Enabled | 30125 | 0–1 | 0 = deaktiviert, 1 = aktiviert |
| Hopper_2_Enabled | 30126 | 0–1 | 0 = deaktiviert, 1 = aktiviert |
| Hopper_3_Enabled | 30127 | 0–1 | 0 = deaktiviert, 1 = aktiviert |
| Hopper_4_Enabled | 30128 | 0–1 | 0 = deaktiviert, 1 = aktiviert |

#### Praxisbeispiel 

Ein Praxisbeispiel für einen READ-HOPPER-Befehl über Fieldbus finden Sie im Abschnitt [Praxisbeispiel READ HOPPER](fieldbus_READHOPPER).
Ein Praxisbeispiel für einen READ-HOPPER-Befehl über TCP finden Sie im Abschnitt [Praxisbeispiel READ HOPPER TCP](TCP_READHOPPER).

---

(sec-empty)=
## Quick-Emptying-Befehle — <span class="isw-section-badge isw-badge-exe"><i class="ph ph-arrow-counter-clockwise"></i> EMPTYING</span>

Die Funktion **Emptying** ermöglicht es, den Teller des FlexiBowl® zu entleeren, indem bis zu 4 dedizierte Sequenzen mit jeweils eigener Schleifenanzahl ausgeführt werden. Auch diese Befehle folgen derselben ControlWord-Logik, die für alle Protokolle gilt.

### EXE-Befehle

| Befehl | ControlWord | Busy während der Ausführung | ReturnData_1 | Erläuterung |
|---|---|---|---|---|
| Start Emptying | 45 | JA (Emptying aktiv) | 45 | Startet das Quick Emptying  |
| Stop Emptying | 46 | JA (Emptying aktiv) | 46 | Stoppt das Quick Emptying  |
| Emptying Active | 47 | NEIN | 47 | Prüft, ob das Quick Emptying aktiv ist |

### WRITE-Befehle

| Befehl | ControlWord | Range Data_1 | Busy während der Ausführung | ReturnData_1 |
|---|---|---|---|---|
| FirstSequence | 20200 | 1–20 | NEIN | 20200 |
| FirstLoop | 20201 | 0–500 | NEIN | 20201 |
| SecondSequence | 20202 | 1–20 | NEIN | 20202 |
| SecondLoop | 20203 | 0–500 | NEIN | 20203 |
| ThirdSequence | 20204 | 1–20 | NEIN | 20204 |
| ThirdLoop | 20205 | 0–500 | NEIN | 20205 |
| FourthSequence | 20206 | 1–20 | NEIN | 20206 |
| FourthLoop | 20207 | 0–500 | NEIN | 20207 |

### READ-Befehle

| Befehl | ControlWord | Busy während der Ausführung | ReturnData_1 | Range ReturnData_2 |
|---|---|---|---|---|
| FirstSequence | 20300 | NEIN | 20300 | 1–20 |
| FirstLoop | 20301 | NEIN | 20301 | 0–500 |
| SecondSequence | 20302 | NEIN | 20302 | 1–20 |
| SecondLoop | 20303 | NEIN | 20303 | 0–500 |
| ThirdSequence | 20304 | NEIN | 20304 | 1–20 |
| ThirdLoop | 20305 | NEIN | 20305 | 0–500 |
| FourthSequence | 20306 | NEIN | 20306 | 1–20 |
| FourthLoop | 20307 | NEIN | 20307 | 0–500 |

:::{note}
`FirstSequence`...`FourthSequence` geben an, welche der 20 programmierten Sequenzen in jedem der 4 Schritte des Quick Emptying ausgeführt wird; `FirstLoop`...`FourthLoop` geben an, wie oft dieser Schritt wiederholt wird.
:::

---

(sec-err)=
## Fehlercodes

:::{warning}
Bei einem Fehler leuchtet die LED **In_Error** auf, und das System führt bis zum Reset keine neuen Bewegungsbefehle aus. Vor dem Zurücksetzen die Fehlerursache identifizieren und beheben.
:::


### Allgemeine Codes

| ErrorCode | Beschreibung |
|---|---|
| 1 | Die Jog-Bewegung hat am Motor keine Aktion ausgelöst |
| 2 | Motor nicht verbunden |
| 3 | EtherNet/IP ausgewählt, aber nicht verbunden |
| 4 | Der Motor hat die Betriebsleistung nicht innerhalb der vorgegebenen Zeit erreicht |
| 5 | Motorbewegung angefordert, aber der Motor ist nicht mit Spannung versorgt |
| 6 | Fehler des digitalen I/O-Moduls: Modul fehlt |
| 7 | Fehler des digitalen I/O-Moduls: Konfigurationsfehler |
| 8 | Fehler des digitalen I/O-Moduls: allgemeiner Fehler |

### Treiber-Fehlercodes

<div class="isw-search-wrap">
  <input class="isw-search" id="errSearch" type="text" placeholder="Nach Code oder Beschreibung filtern…" oninput="filterErrors()">
  <span class="isw-search-count" id="errCount"></span>
</div>

<div style="margin-top: 2rem;"></div>

<div class="isw-err-wrap">
<table class="isw-err-table" id="errTable">
<thead><tr><th>Code</th><th>Hex</th><th>Fehler</th><th>Beschreibung</th></tr></thead>
<tbody>
<tr><td><code>50</code></td><td><code>0x7500</code></td><td>EtherCAT communication error</td><td></td></tr>
<tr><td><code>51</code></td><td><code>0xFF01</code></td><td>Drive Over Current</td><td>Übermäßiger Motorstrom</td></tr>
<tr><td><code>52</code></td><td><code>0xFF02</code></td><td>Drive Over Voltage</td><td>Übermäßige Zwischenkreisspannung</td></tr>
<tr><td><code>53</code></td><td><code>0xFF03</code></td><td>Drive Over Temperature</td><td>Treibertemperatur zu hoch</td></tr>
<tr><td><code>54</code></td><td><code>0xFF04</code></td><td>Reserved</td><td></td></tr>
<tr><td><code>55</code></td><td><code>0xFF05</code></td><td>Drive Internal Voltage Error</td><td>Interner Spannungsfehler</td></tr>
<tr><td><code>56</code></td><td><code>0xFF06</code></td><td>Position Error</td><td>Positionierfehler</td></tr>
<tr><td><code>57</code></td><td><code>0xFF07</code></td><td>Motor Encoder Disconnected</td><td>Encoder nicht angeschlossen oder defekt</td></tr>
<tr><td><code>58</code></td><td><code>0xFF0A</code></td><td>Regen Failed</td><td>Fehler im Rückspeisekreis</td></tr>
<tr><td><code>59</code></td><td><code>0xFF0B</code></td><td>Safe Torque Off (STO)</td><td>Sicherheitsfunktion aktiv</td></tr>
<tr><td><code>60</code></td><td><code>0xFF0C</code></td><td>Reserved</td><td></td></tr>
<tr><td><code>61</code></td><td><code>0xFF0D</code></td><td>Bad FPGA</td><td>Interner Fehler des Treiber-FPGA</td></tr>
<tr><td><code>62</code></td><td><code>0xFF0E</code></td><td>Parameter Read Failed</td><td>Lesen der Parameter fehlgeschlagen</td></tr>
<tr><td><code>63</code></td><td><code>0xFF0F</code></td><td>Motor Encoder Multi-turn Error</td><td>Fehler des Multiturn-Encoders</td></tr>
<tr><td><code>64</code></td><td><code>0xFF10</code></td><td>Motor Stall Protection</td><td>Motorblockierschutz aktiv</td></tr>
<tr><td><code>65</code></td><td><code>0xFF11</code></td><td>Drive Power Module Over Temperature</td><td>Leistungsmodul überhitzt</td></tr>
<tr><td><code>66</code></td><td><code>0xFF31</code></td><td>N Limit</td><td>Negativer Positionsgrenzwert erreicht</td></tr>
<tr><td><code>67</code></td><td><code>0xFF32</code></td><td>P Limit</td><td>Positiver Positionsgrenzwert erreicht</td></tr>
<tr><td><code>68</code></td><td><code>0xFF33</code></td><td>N&P Limit</td><td>Beide Positionsgrenzwerte erreicht</td></tr>
<tr><td><code>69</code></td><td><code>0xFF34</code></td><td>Current Foldback</td><td>Stromreduzierung zum Wärmeschutz</td></tr>
<tr><td><code>70</code></td><td><code>0xFF35</code></td><td>Move @ Disabled</td><td>Bewegungsversuch bei deaktiviertem Treiber</td></tr>
<tr><td><code>71</code></td><td><code>0xFF36</code></td><td>Drive Low Voltage</td><td>Unzureichende Zwischenkreisspannung</td></tr>
<tr><td><code>72</code></td><td><code>0xFF37</code></td><td>Blank Q Segment</td><td>Nicht definiertes Bahnsegment</td></tr>
<tr><td><code>73</code></td><td><code>0xFF38</code></td><td>Velocity Limit</td><td>Geschwindigkeitsgrenze überschritten</td></tr>
<tr><td><code>74</code></td><td><code>0xFF39</code></td><td>Drive Power Phase Lost</td><td>Ausfall einer Versorgungsphase</td></tr>
<tr><td><code>75</code></td><td><code>0xFF3A</code></td><td>Emergency Stop</td><td>Not-Halt aktiv</td></tr>
<tr><td><code>76</code></td><td><code>0xFF3B</code></td><td>Abs. Encoder Battery</td><td>Batterie des Absolutwertgebers schwach oder fehlend</td></tr>
<tr><td><code>77</code></td><td><code>0xFF3C</code></td><td>Abs. Position Lost Warning</td><td>Warnung vor Verlust der Absolutposition</td></tr>
<tr><td><code>78</code></td><td><code>0xFF3D</code></td><td>Abs. Position Overflow</td><td>Überlauf der Absolutposition</td></tr>
<tr><td><code>79</code></td><td><code>0xFF3E</code></td><td>Motor Over Temperature</td><td>Übermäßige Motortemperatur</td></tr>
<tr><td><code>80</code></td><td><code>0xFF3F</code></td><td>Drive Voltage Warning</td><td>Warnung: Treiberspannung außerhalb des Bereichs</td></tr>
<tr><td><code>81</code></td><td><code>0xFF41</code></td><td>Save Failed</td><td>Speichern der Parameter fehlgeschlagen</td></tr>
<tr><td><code>82</code></td><td><code>0xFFFF</code></td><td>Other Error</td><td>Allgemeiner, nicht klassifizierter Fehler</td></tr>
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
    countEl.textContent = count + ' ' + (count === 1 ? 'Ergebnis' : 'Ergebnisse');
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