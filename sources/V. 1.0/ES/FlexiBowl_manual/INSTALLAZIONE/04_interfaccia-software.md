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

</style>

## Introduzione

Il sistema di comunicazione è basato su **variabili di Input/Output** e **Control Word numeriche**: il sistema esterno invia un numero (la ControlWord) che identifica l'azione da eseguire e il FlexiBowl® risponde con segnali di stato e dati di ritorno.

Protocolli supportati:  
- **TCP Server**  
- **EtherNet/IP**  
- **Profinet**  
- **Modbus**

---

### Naviga la pagina

<div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:1rem; margin:1.5rem 0 2.5rem;">

  <a href="#sec-io" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit; transition:border-color 0.18s, background 0.18s;">
    <i class="ph ph-arrows-left-right" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Variabili I/O</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Input & Output</span>
  </a>

  <a href="#sec-exe" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-play-circle" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Comandi EXE</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Avvio sequenze & jog</span>
  </a>

  <a href="#sec-write" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-pencil-simple" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Comandi WRITE</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Scrittura parametri</span>
  </a>

  <a href="#sec-read" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-eye" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Comandi READ</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Lettura parametri</span>
  </a>

  <a href="#sec-tcp" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-network" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Sintassi TCP</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Messaggi socket</span>
  </a>

  <a href="#sec-err" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-warning-circle" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Codici di Errore</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Diagnostica</span>
  </a>

</div>

---

### Come funziona un comando

Due modifiche: numeri in grassetto semplice dentro il cerchio, testi più grandi e leggibili.
<table style="width:100%; border-collapse:collapse; margin: 1.5rem 0 2rem;">
  <tr>
    <td style="text-align:center; padding:0 8px; width:22%;">
      <div style="width:52px; height:52px; border-radius:50%; background:#e3f1fb; border:2px solid #2980b9; display:inline-flex; align-items:center; justify-content:center; color:#2980b9; font-size:1.4rem; font-weight:700; margin-bottom:0.5rem;">
        1
      </div><br>
      <span style="font-size:0.92rem; font-weight:700; color:#1a3a52; line-height:1.4;">Imposta<br>ControlWord</span><br>
      <span style="font-size:0.8rem; color:#7a9ab0;">numero del comando</span>
    </td>
    <td style="text-align:center; color:#bcd6ec; font-size:1.6rem; width:4%; vertical-align:middle; padding-bottom:1.8rem;">
      <i class="ph ph-caret-right"></i>
    </td>
    <td style="text-align:center; padding:0 8px; width:22%;">
      <div style="width:52px; height:52px; border-radius:50%; background:#e3f1fb; border:2px solid #2980b9; display:inline-flex; align-items:center; justify-content:center; color:#2980b9; font-size:1.4rem; font-weight:700; margin-bottom:0.5rem;">
        2
      </div><br>
      <span style="font-size:0.92rem; font-weight:700; color:#1a3a52; line-height:1.4;">Imposta<br>Data_1</span><br>
      <span style="font-size:0.8rem; color:#7a9ab0;">se richiesto</span>
    </td>
    <td style="text-align:center; color:#bcd6ec; font-size:1.6rem; width:4%; vertical-align:middle; padding-bottom:1.8rem;">
      <i class="ph ph-caret-right"></i>
    </td>
    <td style="text-align:center; padding:0 8px; width:22%;">
      <div style="width:52px; height:52px; border-radius:50%; background:#e3f1fb; border:2px solid #2980b9; display:inline-flex; align-items:center; justify-content:center; color:#2980b9; font-size:1.4rem; font-weight:700; margin-bottom:0.5rem;">
        3
      </div><br>
      <span style="font-size:0.92rem; font-weight:700; color:#1a3a52; line-height:1.4;">Fronte salita<br>ExecuteCW</span><br>
      <span style="font-size:0.8rem; color:#7a9ab0;">trigger 0 → 1</span>
    </td>
    <td style="text-align:center; color:#bcd6ec; font-size:1.6rem; width:4%; vertical-align:middle; padding-bottom:1.8rem;">
      <i class="ph ph-caret-right"></i>
    </td>
    <td style="text-align:center; padding:0 8px; width:22%;">
      <div style="width:52px; height:52px; border-radius:50%; background:#e3f1fb; border:2px solid #2980b9; display:inline-flex; align-items:center; justify-content:center; color:#2980b9; font-size:1.4rem; font-weight:700; margin-bottom:0.5rem;">
        4
      </div><br>
      <span style="font-size:0.92rem; font-weight:700; color:#1a3a52; line-height:1.4;">Attendi<br>Busy = 0</span><br>
      <span style="font-size:0.8rem; color:#7a9ab0;">e ReturnData_1 = CW</span>
    </td>
  </tr>
</table>


1. Il sistema esterno imposta la **ControlWord** con il numero del comando desiderato.
2. Se il comando richiede un argomento, imposta anche **Data_1**.
3. Invia un fronte di salita su **ExecuteControlWord**.
4. Attende che **Busy** torni a `0` e che **ReturnData_1** restituisca il valore della ControlWord (conferma di esecuzione corretta).

:::{warning}
Non inviare un nuovo comando mentre **Busy** è a `1`. Il sistema ignorerà il comando e **ReturnData_1** restituirà il valore `3` (sistema occupato).
:::

---

(sec-io)=
## Variabili di Input e Output 

### INPUT — Segnali inviati al FlexiBowl®

| Variabile | Tipo | Descrizione |
|---|---|---|
| **ControlWord** | UDINT | Numero intero che identifica il comando da eseguire. Ogni valore corrisponde a un'azione specifica (vedi tabella comandi). |
| **Data_1** | UDINT | Argomento numerico associato alla ControlWord, quando richiesto (es. il valore di velocità da scrivere). Il significato dipende dal comando selezionato. |
| **ExecuteControlWord** | BOOL | Segnale di trigger: sul **fronte di salita** (da 0 a 1) la ControlWord viene letta e il comando viene eseguito. |
| **Hopper_1** | BOOL | Attiva direttamente l'Hopper 1, indipendentemente dalla ControlWord. |
| **Hopper_2** | BOOL | Attiva direttamente l'Hopper 2. |
| **Hopper_3** | BOOL | Attiva direttamente l'Hopper 3. |
| **Hopper_4** | BOOL | Attiva direttamente l'Hopper 4. |
| **Reset** | BOOL | Sul fronte di salita, esegue il reset degli errori attivi sul dispositivo. |

### OUTPUT — Segnali inviati dal FlexiBowl®

| Variabile | Tipo | Descrizione |
|---|---|---|
| **Busy** | BOOL | Vale `1` mentre il FlexiBowl® sta eseguendo un comando. Finché è attivo, non inviare nuovi comandi. |
| **Ready** | BOOL | Vale `1` quando il dispositivo è pronto a ricevere nuovi comandi. |
| **In_Error** | BOOL | Vale `1` se sono presenti errori attivi sul dispositivo. Consultare **ErrorCode** per identificare il tipo di errore. |
| **ReturnData_1** | UDINT | Conferma del comando ricevuto (echo). I valori possibili sono: `0` = stato iniziale (nessun comando), `1` = comando non interpretabile, `2` = Data_1 errato ma comando riconosciuto, `3` = sistema occupato (Busy), oppure il valore stesso della ControlWord = comando eseguito correttamente. |
| **ReturnData_2** | UDINT | Contiene i dati richiesti dai comandi di lettura (READ). |
| **ErrorCode** | UDINT | Codice numerico dell'errore attivo. Vale `0` se non ci sono errori. Vedere la sezione [Codici di Errore](#codici-di-errore) per il significato di ogni codice. |
| **InPowerOn** | BOOL | Vale `1` se il dispositivo è alimentato e operativo. |


### Valori di ReturnData_1

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
      <th style="padding:0.6rem 0.9rem; text-align:left; font-weight:700; white-space:nowrap; width:100px;">Valore</th>
      <th style="padding:0.6rem 0.9rem; text-align:left; font-weight:700;">Significato</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#fff;" onmouseover="this.style.background='#e8f4fc'" onmouseout="this.style.background='#fff'">
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; font-family:monospace; font-size:1.05rem; font-weight:700; color:#2980b9;">0</td>
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; color:#334e5e;">NULL — nessun comando in corso (stato iniziale)</td>
    </tr>
    <tr style="background:#f7fbfe;" onmouseover="this.style.background='#e8f4fc'" onmouseout="this.style.background='#f7fbfe'">
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; font-family:monospace; font-size:1.05rem; font-weight:700; color:#2980b9;">1</td>
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; color:#334e5e;">Comando non interpretabile (ControlWord sconosciuta)</td>
    </tr>
    <tr style="background:#fff;" onmouseover="this.style.background='#e8f4fc'" onmouseout="this.style.background='#fff'">
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; font-family:monospace; font-size:1.05rem; font-weight:700; color:#2980b9;">2</td>
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; color:#334e5e;">Data_1 fuori range, comando riconosciuto</td>
    </tr>
    <tr style="background:#f7fbfe;" onmouseover="this.style.background='#e8f4fc'" onmouseout="this.style.background='#f7fbfe'">
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; font-family:monospace; font-size:1.05rem; font-weight:700; color:#2980b9;">3</td>
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; color:#334e5e;">Sistema occupato (Busy) — riprovare</td>
    </tr>
    <tr style="background:#fff;" onmouseover="this.style.background='#e8f4fc'" onmouseout="this.style.background='#fff'">
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; font-family:monospace; font-size:1.05rem; font-weight:700; color:#2980b9;">= CW</td>
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; color:#334e5e;">Comando eseguito correttamente</td>
    </tr>
  </tbody>
</table>
</div>

---
## Protocollo Comandi

Il protocollo comandi definisce tutte le azioni disponibili attraverso la ControlWord. I comandi sono raggruppati in tre categorie:

<div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:1rem; margin:1.5rem 0 2.5rem;">

  <a href="#sec-exe" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-play-circle" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Comandi EXE</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Comandi di esecuzione (avvio sequenze, jog, reset)</span>
  </a>

  <a href="#sec-write" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-pencil-simple" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Comandi WRITE</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Scrittura di parametri (velocità, angoli, tempi, ecc.)</span>
  </a>

  <a href="#sec-read" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-eye" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Comandi READ</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Lettura dei parametri attualmente configurati</span>
  </a>

</div>

(sec-exe)=
### Comandi <span class="isw-section-badge isw-badge-exe"><i class="ph ph-play-circle"></i> EXE</span>

I comandi EXE avviano un'azione immediata sul FlexiBowl®. Durante l'esecuzione **Busy** rimane a `1`.

| Comando | ControlWord | Busy durante esecuzione | ReturnData_1 | Spiegazione | 
|---|---|---|---|---|
| Exe Seq 1 | 10 | SI | 10 | Esegui Sequenza 1 |
| Exe Seq 2 | 11 | SI | 11 | Esegui Sequenza 2 |
| Exe Seq 3 | 12 | SI | 12 | Esegui Sequenza 3 |
| Exe Seq 4 | 13 | SI | 13 | Esegui Sequenza 4 |
| Exe Seq 5 | 14 | SI | 14 | Esegui Sequenza 5 |
| Exe Seq 6 | 15 | SI | 15 | Esegui Sequenza 6 |
| Exe Seq 7 | 16 | SI | 16 | Esegui Sequenza 7 |
| Exe Seq 8 | 17 | SI | 17 | Esegui Sequenza 8 |
| Exe Seq 9 | 18 | SI | 18 | Esegui Sequenza 9 |
| Exe Seq 10 | 19 | SI | 19 | Esegui Sequenza 10 |
| Exe Seq 11 | 20 | SI | 20 | Esegui Sequenza 11 |
| Exe Seq 12 | 21 | SI | 21 | Esegui Sequenza 12 |
| Exe Seq 13 | 22 | SI | 22 | Esegui Sequenza 13 |
| Exe Seq 14 | 23 | SI | 23 | Esegui Sequenza 14 |
| Exe Seq 15 | 24 | SI | 24 | Esegui Sequenza 15 |
| Exe Seq 16 | 25 | SI | 25 | Esegui Sequenza 16 |
| Exe Seq 17 | 26 | SI | 26 | Esegui Sequenza 17 |
| Exe Seq 18 | 27 | SI | 27 | Esegui Sequenza 18 |
| Exe Seq 19 | 28 | SI | 28 | Esegui Sequenza 19 |
| Exe Seq 20 | 29 | SI | 29 | Esegui Sequenza 20 |
| Start Jog Seq | 40 | SI | 40 | Avvia Jog |
| Stop Jog Seq | 41 | SI | 41 | Ferma Jog |
| Reset Return Data | 50 | NO | 0 | Azzera il valore di ReturnData_1 e ReturnData_2, riportandoli allo stato iniziale `0` |

:::{note}
Il comando **Reset Return Data** (ControlWord 50) azzera il valore di ReturnData_1 e ReturnData_2, riportandoli allo stato iniziale `0`. È utile per verificare che un nuovo comando venga effettivamente ricevuto ed elaborato.
:::

(sec-write)=
### Comandi <span class="isw-section-badge isw-badge-write"><i class="ph ph-pencil-simple"></i> WRITE</span>

I comandi WRITE permettono di modificare i parametri operativi del FlexiBowl® (velocità, angoli, tempi, ecc.) direttamente dal sistema esterno, senza dover accedere all'interfaccia grafica.

#### Logica di indirizzamento delle sequenze

Ogni sequenza (da 1 a 20) ha un proprio blocco di parametri. La ControlWord si calcola con la formula:

> **ControlWord = N × 100 + offset_parametro**

dove `N` è il numero della sequenza (1–20) e `offset_parametro` identifica il parametro specifico.

#### Parametri scrivibili per ogni sequenza

| Parametro | Offset | Range Data_1 | Note |
|---|---|---|---|
| AccelerationMove | 00 | 1–100 | Rampa di accelerazione del movimento rotatorio (%) |
| DecelerationMove | 01 | 1–100 | Rampa di decelerazione del movimento rotatorio (%) |
| SpeedMove | 02 | 1–100 | Velocità del movimento rotatorio (%) |
| AngleMove | 03 | 0–720 | Angolo di rotazione in gradi. Valori 1000–1720 = angolo negativo (direzione opposta) |
| AccelerationShake | 04 | 1–100 | Rampa di accelerazione dello shake (%) |
| DecelerationShake | 05 | 1–100 | Rampa di decelerazione dello shake (%) |
| CountShake | 06 | 2–20 | Numero di oscillazioni per ciclo di shake |
| CwAngleShake | 07 | 0–360 | Angolo di rotazione oraria durante lo shake. Valori 1000–1360 = angolo negativo |
| CcwAngleShake | 08 | 0–360 | Angolo di rotazione antioraria durante lo shake. Valori 1000–1360 = angolo negativo |
| SpeedShake | 09 | 1–100 | Velocità dello shake (%) |
| FlipCount | 10 | 0–20 | Numero di flip per ciclo |
| FlipDelay | 11 | 0–500 | Pausa tra un flip e il successivo (ms) |
| BlowDelay | 12 | 0–500 | Pausa tra un impulso di blow e il successivo (ms) |
| ProportionalValve_Flip | 13 | 0–600 | Pressione valvola proporzionale Flip (valore /100 = Bar) |
| ProportionalValve_Blow | 14 | 0–600 | Pressione valvola proporzionale Blow (valore /100 = Bar) |
| Delete all sequence | 30 | — | Cancella tutti i comandi dalla lista della sequenza |
| Emptying Sequence | 40 | 0–1 | 0 = modalità normale, 1 = modalità svuotamento |
| Seq Add Cmd | 50 | COMANDO FLB | Aggiunge un comando alla lista della sequenza |

#### Esempi di ControlWord WRITE

| Sequenza | Parametro | Offset associato al parametro | Formula (N x 100 + Offset) | ControlWord |
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
La formula è semplice:  
- Per scrivere la velocità (offset 02) della sequenza 7, la ControlWord è `7 × 100 + 2 = 702`.  
- Per scrivere il FlipCount (offset 10) della sequenza 15, la ControlWord è `15 × 100 + 10 = 1510`.
:::

#### Parametri WRITE JOG

I parametri del Jog (funzionamento manuale continuo) sono configurabili separatamente tramite ControlWord nel blocco 20000.

| Parametro | ControlWord | Range Data_1 | Note |
|---|---|---|---|
| AccelerationJog | 20001 | 0–100 | Rampa di accelerazione del jog (%) |
| DecelerationJog | 20002 | 0–100 | Rampa di decelerazione del jog (%) |
| SpeedJog | 20003 | 0–100 | Velocità jog (%). Valori 1000–1100 = velocità negativa (rotazione inversa) |
| FlipJog_Enable | 20004 | 0–1 | 0 = flip disabilitato, 1 = flip abilitato durante jog |
| FlipJog_Duration | 20005 | 0–1000 | Durata impulso flip (ms) |
| FlipJog_Pressure | 20006 | 0–600 | Pressione flip (/100 = Bar) |
| FlipJog_Pause | 20007 | 0–1000 | Pausa tra flip consecutivi (ms) |
| BlowJog_Enable | 20008 | 0–1 | 0 = blow disabilitato, 1 = blow abilitato durante jog |
| BlowJog_Duration | 20009 | 0–1000 | Durata impulso blow (ms) |
| BlowJog_Pressure | 20010 | 0–600 | Pressione blow (/100 = Bar) |
| BlowJog_Pause | 20011 | 0–1000 | Pausa tra blow consecutivi (ms) |
| BlowJog_Type | 20012 | 0–2 | Tipo di blow: 0 = BLOWc, 1 = BLOWe, 2 = BLOWc+BLOWe |
| Backlight_1 | 20013 | 0–1 | 0 = spento, 1 = acceso |
| Backlight_2 | 20014 | 0–1 | 0 = spento, 1 = acceso |

#### Parametri WRITE HOPPER

I parametri degli hopper (tramogge vibrazionali) sono configurabili nel blocco 30000.

| Parametro | ControlWord | Range Data_1 | Tipo |
|---|---|---|---|
| Hopper_1_Id | 30001 | 1–100 | ID univoco dell'hopper 1 sulla rete |
| Hopper_1_Amplitude | 30002 | 1–1000 | Ampiezza vibrazione hopper 1 |
| Hopper_1_Frequency | 30003 | 50–1400 | Frequenza vibrazione hopper 1 |
| Hopper_1_Stop_Time | 30004 | 400–60000 | Tempo di attivazione hopper 1 (ms) |
| Hopper_2_Id | 30005 | 1–100 | ID univoco dell'hopper 2 |
| Hopper_2_Amplitude | 30006 | 1–1000 | Ampiezza vibrazione hopper 2 |
| Hopper_2_Frequency | 30007 | 50–1400 | Frequenza vibrazione hopper 2 |
| Hopper_2_Stop_Time | 30008 | 400–60000 | Tempo di attivazione hopper 2 (ms) |
| Hopper_3_Id | 30009 | 1–100 | ID univoco dell'hopper 3 |
| Hopper_3_Amplitude | 30010 | 1–1000 | Ampiezza vibrazione hopper 3 |
| Hopper_3_Frequency | 30011 | 50–1400 | Frequenza vibrazione hopper 3 |
| Hopper_3_Stop_Time | 30012 | 400–60000 | Tempo di attivazione hopper 3 (ms) |
| Hopper_4_Id | 30013 | 1–100 | ID univoco dell'hopper 4 |
| Hopper_4_Amplitude | 30014 | 1–1000 | Ampiezza vibrazione hopper 4 |
| Hopper_4_Frequency | 30015 | 50–1400 | Frequenza vibrazione hopper 4 |
| Hopper_4_Stop_Time | 30016 | 400–60000 | Tempo di attivazione hopper 4 (ms) |
| Hopper_1_Enable | 30017 | — | Abilita hopper 1 (azione immediata) |
| Hopper_1_Disable | 30018 | — | Disabilita hopper 1 (azione immediata) |
| Hopper_2_Enable | 30019 | — | Abilita hopper 2 |
| Hopper_2_Disable | 30020 | — | Disabilita hopper 2 |
| Hopper_3_Enable | 30021 | — | Abilita hopper 3 |
| Hopper_3_Disable | 30022 | — | Disabilita hopper 3 |
| Hopper_4_Enable | 30023 | — | Abilita hopper 4 |
| Hopper_4_Disable | 30024 | — | Disabilita hopper 4 |

---

(sec-read)=
### Comandi <span class="isw-section-badge isw-badge-read"><i class="ph ph-eye"></i> READ</span>

I comandi READ permettono di leggere i parametri attualmente configurati nel FlexiBowl®. Il valore letto viene restituito in **ReturnData_2**.

#### Logica di indirizzamento READ sequenze

La ControlWord per la lettura si calcola con la formula:

> **ControlWord = 10000 + N × 100 + offset_parametro**

dove `N` è il numero della sequenza (1–20) e `offset_parametro` è lo stesso usato nei comandi WRITE.

I parametri leggibili sono gli stessi del blocco WRITE, con l'aggiunta dei 10 slot della lista comandi:

| Parametro aggiuntivo | Offset | Descrizione |
|---|---|---|
| Seq Slot 1 Cmd | 50 | Comando in posizione 1 nella lista della sequenza |
| Seq Slot 2 Cmd | 51 | Comando in posizione 2 |
| … | … | … |
| Seq Slot 10 Cmd | 59 | Comando in posizione 10 |

#### Esempi di ControlWord READ

| Sequenza | Parametro | ControlWord |
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
Formula rapida:  
 Per leggere la velocità (offset 02) della sequenza 12, la ControlWord è `10000 + 12 × 100 + 2 = 11202`.
:::

#### Parametri READ JOG

Gli stessi parametri scrivibili del JOG (blocco 20000) sono leggibili nel blocco 20100:

| Parametro | ControlWord READ | Range RestituData_2 |
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

#### Parametri READ HOPPER

| Parametro | ControlWord READ | Range ReturnData_2 | Note |
|---|---|---|---|
| Hopper_1_Id | 30101 | 1–100 | |
| Hopper_1_Amplitude | 30102 | 1–1000 | |
| Hopper_1_Frequency | 30103 | 50–1400 | |
| Hopper_1_Stop_Time | 30104 | 400–60000 | |
| Hopper_2_Id | 30105 | 1–100 | |
| Hopper_2_Amplitude | 30106 | 1–1000 | |
| Hopper_2_Frequency | 30107 | 50–1400 | |
| Hopper_2_Stop_Time | 30108 | 400–60000 | |
| Hopper_3_Id | 30109 | 1–100 | |
| Hopper_3_Amplitude | 30110 | 1–1000 | |
| Hopper_3_Frequency | 30111 | 50–1400 | |
| Hopper_3_Stop_Time | 30112 | 400–60000 | |
| Hopper_4_Id | 30113 | 1–100 | |
| Hopper_4_Amplitude | 30114 | 1–1000 | |
| Hopper_4_Frequency | 30115 | 50–1400 | |
| Hopper_4_Stop_Time | 30116 | 400–60000 | |
| Hopper_1_Ready | 30117 | 0–1 | 0 = non pronto, 1 = pronto |
| Hopper_2_Ready | 30118 | 0–1 | 0 = non pronto, 1 = pronto |
| Hopper_3_Ready | 30119 | 0–1 | 0 = non pronto, 1 = pronto |
| Hopper_4_Ready | 30120 | 0–1 | 0 = non pronto, 1 = pronto |
| Hopper_1_InVibration | 30121 | 0–1 | 0 = fermo, 1 = in vibrazione |
| Hopper_2_InVibration | 30122 | 0–1 | 0 = fermo, 1 = in vibrazione |
| Hopper_3_InVibration | 30123 | 0–1 | 0 = fermo, 1 = in vibrazione |
| Hopper_4_InVibration | 30124 | 0–1 | 0 = fermo, 1 = in vibrazione |
| Hopper_1_Enabled | 30125 | 0–1 | 0 = disabilitato, 1 = abilitato |
| Hopper_2_Enabled | 30126 | 0–1 | 0 = disabilitato, 1 = abilitato |
| Hopper_3_Enabled | 30127 | 0–1 | 0 = disabilitato, 1 = abilitato |
| Hopper_4_Enabled | 30128 | 0–1 | 0 = disabilitato, 1 = abilitato |

---

(sec-tcp)=
## Sintassi Messaggi TCP Server

Quando si utilizza la comunicazione **TCP Server**, i comandi non vengono inviati come variabili binarie ma come **stringhe di testo** attraverso una connessione socket sulla porta configurata (default: 8123).

### Struttura del messaggio

Ogni messaggio ha la forma:

```
NomeVariabile[Valore]%
```

Il carattere `%` è il **terminatore di messaggio** e deve essere sempre presente alla fine. Il campo `[Valore]` contiene il dato numerico associato (ControlWord, stato, ecc.).

### Tabella di sintassi TCP

| Operazione | Messaggio da inviare | Risposta se OK | Risposta se errore |
|---|---|---|---|
| Tutti i comandi EXE | `10[0]%` | `10[0]%` | `1[0]%` |
| Tutti i comandi WRITE | `100[56]%` | `100[0]%` | `2[0]%` |
| Tutti i comandi READ | `10100[0]%` | `10100[valore]%` | `2[0]%` |
| Avvia Hopper 1 | `Hopper1Start%` | `Hopper1Start *` | — |
| Avvia Hopper 2 | `Hopper2Start%` | `Hopper2Start *` | — |
| Avvia Hopper 3 | `Hopper3Start%` | `Hopper3Start *` | — |
| Avvia Hopper 4 | `Hopper4Start%` | `Hopper4Start *` | — |
| Reset errori | `Reset%` | `Reset%` | — |
| Leggi stato Busy | `Busy%` | `Busy[1]%` | `Busy[0]%` |
| Leggi stato Ready | `Ready%` | `Ready[1]%` | `Ready[0]%` |
| Leggi stato InError | `InError%` | `InError[1]%` | `InError[0]%` |
| Leggi stato InPowerOn | `InPowerOn%` | `InPowerOn[1]%` | `InPowerOn[0]%` |
| Leggi ErrorCode | `ErrorCode%` | `ErrorCode[56]%` | `ErrorCode[0]%` |

:::{note}
Nelle risposte di tipo READ, il testo `[valore]` viene sostituito con il dato numerico effettivo letto dal sistema. Ad esempio, per leggere la velocità della SEQ 1 (ControlWord 10102), si invia `10102[0]%` e si riceve `10102[35]%` se la velocità è impostata a 35%.
:::

:::{warning}
I comandi Hopper via TCP (`Hopper1Start%`, ecc.) funzionano **solo quando la comunicazione è attiva e il FlexiBowl®  non è in movimento**. Non è garantito il corretto funzionamento se il FlexiBowl® sta eseguendo una sequenza o è in modalità jog.
:::

### Significato di ReturnData_1 (o risposta TCP)

| Valore | Significato |
|---|---|
| `0` | NULL — nessun comando in corso (stato iniziale) |
| `1` | Comando non interpretabile (ControlWord sconosciuta) |
| `2` | Data_1 fuori range, ma il comando è stato riconosciuto |
| `3` | Sistema occupato (Busy) — riprovare dopo che Busy torna a 0 |
| Valore = ControlWord | Comando eseguito correttamente |


---

(sec-err)=
## Codici di Errore

:::{warning}
In presenza di un errore, il LED **In_Error** si attiva e il sistema non eseguirà nuovi comandi di movimento fino al reset. Prima di eseguire il reset, identificare e risolvere la causa dell'errore.
:::


### Codici Generali

| ErrorCode | Descrizione |
|---|---|
| 1 | Il movimento di jog non ha attivato alcuna azione sul motore |
| 2 | Motore non connesso |
| 3 | EtherNet/IP selezionato ma non connesso |
| 4 | Il motore non ha raggiunto la potenza operativa entro il tempo prestabilito |
| 5 | Richiesto movimento del motore, ma il motore non è alimentato |
| 6 | Errore modulo I/O digitale: modulo mancante |
| 7 | Errore modulo I/O digitale: errore di configurazione |
| 8 | Errore modulo I/O digitale: errore generale |

### Codici Errore Driver

<div class="isw-search-wrap">
  <input class="isw-search" id="errSearch" type="text" placeholder="Filtra per codice o descrizione…" oninput="filterErrors()">
  <span class="isw-search-count" id="errCount"></span>
</div>

<div style="margin-top: 2rem;"></div>

<div class="isw-err-wrap">
<table class="isw-err-table" id="errTable">
<thead><tr><th>Codice</th><th>Hex</th><th>Errore</th><th>Descrizione</th></tr></thead>
<tbody>
<tr><td><code>50</code></td><td><code>0x7500</code></td><td>EtherCAT communication error</td><td></td></tr>
<tr><td><code>51</code></td><td><code>0xFF01</code></td><td>Drive Over Current</td><td>Corrente motore eccessiva</td></tr>
<tr><td><code>52</code></td><td><code>0xFF02</code></td><td>Drive Over Voltage</td><td>Tensione bus DC eccessiva</td></tr>
<tr><td><code>53</code></td><td><code>0xFF03</code></td><td>Drive Over Temperature</td><td>Temperatura driver troppo elevata</td></tr>
<tr><td><code>54</code></td><td><code>0xFF04</code></td><td>Reserved</td><td></td></tr>
<tr><td><code>55</code></td><td><code>0xFF05</code></td><td>Drive Internal Voltage Error</td><td>Errore tensione interna</td></tr>
<tr><td><code>56</code></td><td><code>0xFF06</code></td><td>Position Error</td><td>Errore di posizionamento</td></tr>
<tr><td><code>57</code></td><td><code>0xFF07</code></td><td>Motor Encoder Disconnected</td><td>Encoder non collegato o guasto</td></tr>
<tr><td><code>58</code></td><td><code>0xFF0A</code></td><td>Regen Failed</td><td>Errore nel circuito di rigenerazione</td></tr>
<tr><td><code>59</code></td><td><code>0xFF0B</code></td><td>Safe Torque Off (STO)</td><td>Funzione di sicurezza attiva</td></tr>
<tr><td><code>60</code></td><td><code>0xFF0C</code></td><td>Reserved</td><td></td></tr>
<tr><td><code>61</code></td><td><code>0xFF0D</code></td><td>Bad FPGA</td><td>Errore interno all'FPGA del driver</td></tr>
<tr><td><code>62</code></td><td><code>0xFF0E</code></td><td>Parameter Read Failed</td><td>Lettura parametri fallita</td></tr>
<tr><td><code>63</code></td><td><code>0xFF0F</code></td><td>Motor Encoder Multi-turn Error</td><td>Errore encoder multi-giro</td></tr>
<tr><td><code>64</code></td><td><code>0xFF10</code></td><td>Motor Stall Protection</td><td>Protezione stallo motore attiva</td></tr>
<tr><td><code>65</code></td><td><code>0xFF11</code></td><td>Drive Power Module Over Temperature</td><td>Modulo di potenza surriscaldato</td></tr>
<tr><td><code>66</code></td><td><code>0xFF31</code></td><td>N Limit</td><td>Limite di posizione negativo raggiunto</td></tr>
<tr><td><code>67</code></td><td><code>0xFF32</code></td><td>P Limit</td><td>Limite di posizione positivo raggiunto</td></tr>
<tr><td><code>68</code></td><td><code>0xFF33</code></td><td>N&P Limit</td><td>Entrambi i limiti di posizione raggiunti</td></tr>
<tr><td><code>69</code></td><td><code>0xFF34</code></td><td>Current Foldback</td><td>Riduzione corrente per protezione termica</td></tr>
<tr><td><code>70</code></td><td><code>0xFF35</code></td><td>Move @ Disabled</td><td>Tentativo di movimento con driver disabilitato</td></tr>
<tr><td><code>71</code></td><td><code>0xFF36</code></td><td>Drive Low Voltage</td><td>Tensione bus DC insufficiente</td></tr>
<tr><td><code>72</code></td><td><code>0xFF37</code></td><td>Blank Q Segment</td><td>Segmento di traiettoria non definito</td></tr>
<tr><td><code>73</code></td><td><code>0xFF38</code></td><td>Velocity Limit</td><td>Limite di velocità superato</td></tr>
<tr><td><code>74</code></td><td><code>0xFF39</code></td><td>Drive Power Phase Lost</td><td>Perdita di una fase di alimentazione</td></tr>
<tr><td><code>75</code></td><td><code>0xFF3A</code></td><td>Emergency Stop</td><td>Arresto di emergenza attivo</td></tr>
<tr><td><code>76</code></td><td><code>0xFF3B</code></td><td>Abs. Encoder Battery</td><td>Batteria encoder assoluto scarica o assente</td></tr>
<tr><td><code>77</code></td><td><code>0xFF3C</code></td><td>Abs. Position Lost Warning</td><td>Avviso perdita posizione assoluta</td></tr>
<tr><td><code>78</code></td><td><code>0xFF3D</code></td><td>Abs. Position Overflow</td><td>Overflow posizione assoluta</td></tr>
<tr><td><code>79</code></td><td><code>0xFF3E</code></td><td>Motor Over Temperature</td><td>Temperatura motore eccessiva</td></tr>
<tr><td><code>80</code></td><td><code>0xFF3F</code></td><td>Drive Voltage Warning</td><td>Avviso tensione driver fuori range</td></tr>
<tr><td><code>81</code></td><td><code>0xFF41</code></td><td>Save Failed</td><td>Salvataggio parametri fallito</td></tr>
<tr><td><code>82</code></td><td><code>0xFFFF</code></td><td>Other Error</td><td>Errore generico non classificato</td></tr>
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
    countEl.textContent = count + ' risultat' + (count === 1 ? 'o' : 'i');
  } else {
    countEl.textContent = '';
  }
}
</script>

</div>
