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
 
# **Comparativa Software**
 
Questa pagina confronta le principali differenze software tra **FlexiBowl® 2.0** e **FlexiBowl® 3.0**, con l'obiettivo di guidare l'utente nella comprensione delle nuove funzionalità e dei cambiamenti operativi introdotti dalla nuova generazione.
 
:::{important}
Prima di leggere i contenuti della pagina corrente, è buona pratica avere chiare le informazioni riportate nella pagina [Interfaccia Software](int_software)
:::
---
 
## 1. Protocolli di comunicazione disponibili
 
| Protocollo | FlexiBowl® 2.0 | FlexiBowl® 3.0 |
|---|---|---|
| TCP/IP – UDP | ✓ | ✓ (TCP Server) |
| EtherNet/IP | ✓ | ✓ |
| Profinet | ✗ | ✓ |
| Modbus | ✗ | ✓ |
| Digital I/O | ✓ | ✓ (opzionale) |
 
---
 
## 2. Interfaccia utente: com'è fatta e come si accede
 
<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0 — Software Parameters</div>
<div class="compare-card-body">
 
Interfaccia **desktop** chiamata **FlexiBowl® Parameters**, da installare sul PC di controllo.
 
**Installazione e accesso:**
 
1. Installare il programma **FlexiBowl® Parameters** sul PC (fornito da ARS).
2. Collegare il PC al FlexiBowl® tramite **cavo Ethernet** (LAN diretta o via switch).
3. Avviare il programma e inserire l'**indirizzo IP** del FlexiBowl® per connettersi.
 
Dalla schermata **Main Commands** sono accessibili i pannelli **Move**, **Shake** e **Option** tramite tab nella parte superiore.
 
</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0 — Interfaccia Web</div>
<div class="compare-card-body">
 
Interfaccia **completamente web-based**: non richiede alcuna installazione. È sufficiente un browser moderno.
 
**Accesso:**
 
1. Collegare il PC al FlexiBowl® tramite Ethernet.
2. Aprire il browser e digitare nella barra degli indirizzi l'**indirizzo IP** del FlexiBowl®.
3. Si apre la **Home page** dell'interfaccia.
 
**Struttura dell'interfaccia:**
 
Il menu laterale include pagine dedicate a ogni funzione operativa (Main Command, Jog Motor, Setup, Monitor, ecc.), accessibili direttamente dal browser.
 
</div>
</div>
</div>
 
:::{note}
Se il sistema in uso è **FlexiVision One**, la configurazione viene gestita dalla sua interfaccia dedicata. Non è necessario utilizzare l'interfaccia software FlexiBowl® descritta in questa sezione.
:::
 
---
 
## 3. Come cambiare l'indirizzo IP
 
<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0</div>
<div class="compare-card-body">
 
1. Utilizzare il programma fornito sulla USB.
2. Collegare il FlexiBowl® tramite cavo Ethernet.
3. Accendere il dispositivo.
4. Avviare il programma.
5. Nella casella **IP Address**, inserire l'indirizzo: `192.168.1.10`  
   *(Il PC collegato deve essere nella stessa subnet mask Classe B — 255.255.0.0)*
6. Premere **Ping** → pop-up **"FlexiBowl® found"**.
7. Premere **Ok** per abilitare **CONNECT** e avviare la connessione.
8. Dopo la connessione verrà visualizzata la home screen.
 
</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0</div>
<div class="compare-card-body">
 
1. Aprire il browser e accedere all'interfaccia tramite l'IP corrente.
2. Dal menu laterale, aprire la pagina **Setup**.
3. Cliccare su **Get IP** per leggere i parametri di rete correnti.
4. Inserire il nuovo indirizzo IP nei campi dedicati e cliccare **Set IP**.
5. Cliccare **Apply** per confermare, poi **Reboot** per rendere effettive le modifiche.
 
</div>
</div>
</div>
 
:::{note}
**FlexiBowl® 2.0** — Se è installata una versione precedente del programma, è necessario disinstallarla prima.
:::
 
:::{important}
**FlexiBowl® 3.0** — Dopo il reboot, riconnettersi al FlexiBowl® utilizzando il nuovo indirizzo IP impostato.
:::
 
---
 
## 4. Come gestire i movimenti
 
<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0</div>
<div class="compare-card-body">
 
I movimenti vengono configurati e testati da **Main Commands**, con tre pannelli:
 
- **Move**: imposta Acceleration, Deceleration, Speed e Angle tramite slider o campo numerico. **Test Move** esegue il movimento con i valori impostati.
- **Shake**: parametri CCW Angle, CW Angle, Count, Acceleration, Deceleration e Speed. **Test Shake** esegue lo shake.
- **Try Commands**: combina più comandi in una sequenza con loop configurabile, selezionando da **All Commands** e aggiungendo a **Selected Commands**.
 
Per la produzione via protocollo, si inviano comandi ASCII (es. `QX2` per Move, `QX6` per Shake) tramite il canale TCP/UDP configurato.
 
</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0</div>
<div class="compare-card-body">
 
I movimenti sono organizzati in **sequenze** (fino a 20), configurabili dalla pagina **Main Command**. Ogni sequenza contiene fino a 10 slot di comandi (Move, Shake, Flip, Blow).
 
Dalla pagina **Main Command** è possibile:
 
- Selezionare la sequenza tramite **Select the sequence**.
- Impostare tutti i parametri nei campi numerici.
- Aggiungere comandi con **Command Available** + **ADD**; riordinarli con **UP/DOWN**; eliminarli con **DELETE** o svuotare con **CLEAR**.
- Testare con **TEST SEQUENCE** o avviare in produzione con **RUN**.
 
La pagina **Jog Motor** consente rotazione continua (Speed positivo = orario, negativo = antiorario) con Flip e Blow integrati.
 
Per la produzione via protocollo: `10[0]%` per Sequenza 1 via TCP, oppure ControlWord `10` via EtherNet/IP o Profinet.
 
</div>
</div>
</div>
 
---
 
## 5. Come cambiare i parametri
 
<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0</div>
<div class="compare-card-body">
 
I parametri operativi vengono modificati in due modalità:
 
- **Interfaccia grafica**: slider o campi numerici nelle schermate Move e Shake di **Main Commands**.
- **Via protocollo (runtime)**: comandi `RW` (Write) e `RL` (Read) via TCP/UDP. I valori devono essere moltiplicati per il **fattore di riduzione** della macchina (ottenuto con il comando `RR114`), poiché i parametri sono espressi in unità interne del driver.
 
</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0</div>
<div class="compare-card-body">
 
I parametri vengono modificati in tre modalità:
 
- **Interfaccia web**: direttamente nei campi numerici della pagina **Main Command** per ogni sequenza.
- **Via protocollo WRITE**: ControlWord blocco WRITE con formula `N × 100 + offset_parametro`
- **Via protocollo READ**: ControlWord blocco READ con formula `10000 + N × 100 + offset_parametro`
 
</div>
</div>
</div>
 
---
 
### Esempio pratico: Move + Shake su FlexiBowl® 800
 
Lo scenario è il seguente: eseguire un **Move** a 360°, poi uno **Shake**, poi un wait di 200 ms.
 
<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0 — Sequenza comandi TCP</div>
<div class="compare-card-body">
 
I parametri devono essere scalati tramite il **fattore di riduzione** della macchina:
 
<pre>QX7                     → Accendi backlight
RR114                   → Leggi fattore di riduzione
variabile_riduzione = RX 1
 
RL1 (50 × variabile_riduzione), RW11   → Acceleration Move = 50%
RL1 (50 × variabile_riduzione), RW12   → Deceleration Move = 50%
RL1 (35 × variabile_riduzione), RW13   → Speed Move = 35%
RL1 (360 × variabile_riduzione), RW14  → Angle Move = 360°
QX2                     → Esegui Move
 
RL1 (50 × variabile_riduzione), RW15  → Acceleration Shake = 50%
RL1 (50 × variabile_riduzione), RW16  → Deceleration Shake = 50%
RL1 (50 × variabile_riduzione), RW110 → Speed Shake = 50%
RL1 (30 × variabile_riduzione), RW18  → Angle CW Shake = -30°
RL1 (30 × variabile_riduzione), RW19  → Angle CCW Shake = -45°
RL1 2, RW17                           → Count Shake = 2
QX6                     → Esegui Shake</pre>
 
Il wait di 200 ms è gestito dal sistema chiamante (robot o PLC).
 
</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0 — Configurazione interfaccia web</div>
<div class="compare-card-body">
 
Dalla pagina **Main Command**, selezionare **SEQUENCE 1** e impostare:
 
| Parametro | Valore |
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
 
Aggiungere alla lista: `FLB_MOVE` → `FLB_SHAKE`. Verificare Backlight dalla pagina **Option**. Il wait di 200 ms si gestisce aggiungendo `FLB_WAIT` alla lista o lato sistema chiamante.
 
Per eseguire la sequenza via TCP:
 
<pre>10[0]%    → Esegui Sequenza 1</pre>
 
Il sistema risponde con `10[0]` a conferma.
 
</div>
</div>
</div>
 
---
 
## 6. Come leggere gli allarmi
 
<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0</div>
<div class="compare-card-body">
 
Gli allarmi si consultano da **Monitor → Alarm Status** del programma **FlexiBowl® Parameters**. La schermata mostra gli stati del driver con indicatori LED (verde = OK, rosso = errore). La schermata **Driver Status** mostra in tempo reale tutte le variabili operative.
 
Reset allarme via protocollo:
 
<pre>Chr(0)Chr(7)QX12Chr(13)    → Reset allarme e riabilitazione motore</pre>
 
</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0</div>
<div class="compare-card-body">
 
Gli allarmi si consultano dalla pagina **Monitor** (tab: **I/O Status**, **Driver Status**, **Alarm Status**).
 
Via protocollo, il segnale di allarme è esposto da **In_Error** (BOOL) e il codice attivo da **ErrorCode** (UDINT):
 
<pre>InError%         → InError[1]% se c'è errore, InError[0]% se OK
ErrorCode%       → ErrorCode[N]% con il codice dell'errore attivo</pre>
 
Reset dell'allarme:
- Via protocollo TCP: `Reset%`
- Via variabile digitale: fronte di salita sul segnale di input **Reset** (BOOL)
 
</div>
</div>
</div>
 
:::{warning}
Prima di eseguire il reset, identificare e risolvere la causa dell'errore. Il sistema non eseguirà nuovi comandi di movimento finché è presente un errore attivo.
:::
 
:::{note}
Per la lista completa dei codici errore fare riferimento alla sezione [Codici Di Errore](sec-err)
:::
 
---
 
## 7. Modalità tracking (FlexiTrack)
 
<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0</div>
<div class="compare-card-body">
 
La modalità **FlexiTrack** è un'opzione acquistabile separatamente che consente di mantenere il FlexiBowl® in **rotazione continua** (jog) sincronizzando il segnale encoder con il robot di pick.
 
**Hardware richiesto:**
 
- Connessione all'**encoder interno** tramite il connettore del pannello di controllo (segnale quadratura TTL, 4000 conteggi/giro sul motore; per FlexiBowl® 500/650/800 con riduzione 1:3 → 12000 conteggi/giro sul disco).
- In alternativa, **encoder esterno** (incremental, TTL RS422, ≥ 12000 ppr) sul perno solidale alla puleggia condotta.
 
**Comandi principali FlexiTrack (via TCP/UDP):**
 
| Comando | Descrizione |
|---|---|
| `JA<valore>` | Accelerazione/decelerazione in giri/s² |
| `JL<valore>` | Decelerazione (se diversa da JA, inviare dopo JA) |
| `JS<valore>` | Velocità di rotazione in giri/s |
| `CC<valore>` | Corrente diretta al motore |
| `DI1` | Direzione oraria |
| `DI-1` | Direzione antioraria |
| `CJ` | Avvia jog (rotazione continua) |
| `SJ` | Ferma jog (con rampa JL) |
| `IL2` / `IH2` | Attiva / disattiva Flip |
| `IL3` / `IH3` | Attiva / disattiva Blow |
 
**Parametri consigliati:**
 
<pre>JA0.2    → accelerazione 0.2 giri/s²
JL0.2    → decelerazione 0.2 giri/s²
JS0.2    → velocità 0.2 giri/s
CC1.3    → corrente motore
DI1      → rotazione oraria</pre>
 
Flip e Blow vanno implementati tramite un **programma in background** con ciclo iterativo che commuta lo stato delle valvole.
 
</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0</div>
<div class="compare-card-body">
 
La modalità jog è **integrata nativamente** nella pagina **Jog Motor** — senza opzioni hardware aggiuntive.
 
**Parametri di movimento Jog:**
 
| Parametro | Unità | Descrizione |
|---|---|---|
| Acceleration | % | Rampa di accelerazione all'avvio |
| Deceleration | % | Rampa di decelerazione all'arresto |
| Speed | % | Velocità — positivo = orario; negativo = antiorario |
 
**Funzioni accessorie durante il Jog:**
 
- **Flip Enable**: flip automatico ciclico con Flip Duration, Flip Pression, Flip Pause.
- **Blow Enable**: soffio automatico ciclico con Blow Duration, Blow Pression, Blow Pause, Blow Type (BLOWc, BLOWe, BLOWc+BLOWe).
- **Backlight 1 / 2**: toggle retroilluminazione, indipendente dallo stato del jog.
 
**Avvio e arresto:**
 
- **START JOG**: avvia la rotazione continua.
- **STOP JOG**: interrompe con rampa di decelerazione.
 
Controllo via protocollo:
 
<pre>40[0]%    → Start Jog Seq (via TCP)
41[0]%    → Stop Jog Seq (via TCP)</pre>
 
</div>
</div>
</div>
 
:::{important}
Prima di avviare il jog, verificare che il motore sia abilitato (**ENABLE MOTOR** attivo) e che lo stato del sistema sia **READY**.
:::
 
:::{important}
Con FlexiTrack **(FlexiBowl® 2.0)**, il controllo del movimento è possibile **solo via protocollo Ethernet** (TCP/UDP). Il protocollo Digital I/O non è supportato.
:::