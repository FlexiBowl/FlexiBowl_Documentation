<style>

/* ── Corpo generale ──────────────────────────────────────── */
body, .md-content {
  color: var(--text);
  background: #f4f8fd;
  line-height: 1.65;
}

/* ── Header principale ───────────────────────────────────── */
.page-header {
  background: linear-gradient(135deg, var(--blue-deep) 0%, var(--blue-mid) 60%, var(--blue-bright) 100%);
  color: var(--white);
  border-radius: 10px;
  padding: 2rem 2.5rem 1.6rem;
  margin-bottom: 2rem;
  box-shadow: 0 4px 18px rgba(13,43,78,0.18);
  position: relative;
  overflow: hidden;
}
.page-header::before {
  content: '';
  position: absolute;
  top: -40px; right: -40px;
  width: 160px; height: 160px;
  border-radius: 50%;
  background: rgba(255,255,255,0.06);
}
.page-header h1 {
  margin: 0 0 0.3rem;
  font-size: 1.75rem;
  font-weight: 700;
  letter-spacing: 0.01em;
}
.page-header p {
  margin: 0;
  opacity: 0.82;
  font-size: 0.95rem;
}


/* ── Sezioni numerate ────────────────────────────────────── */
.section-title {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin: 2.2rem 0 1rem;
  color: var(--blue-deep);
}
.section-num {
  background: var(--blue-bright);
  color: var(--white);
  border-radius: 50%;
  width: 2rem; height: 2rem;
  display: flex; align-items: center; justify-content: center;
  font-size: 0.85rem;
  font-weight: 700;
  flex-shrink: 0;
}
.section-title h2 {
  margin: 0;
  font-size: 1.2rem;
  font-weight: 700;
  border-bottom: 2px solid var(--blue-border);
  padding-bottom: 0.25rem;
  flex: 1;
}

/* ── Confronto 2.0 vs 3.0 side-by-side ──────────────────── */
.compare-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.1rem;
  margin: 1rem 0 1.5rem;
}
@media (max-width: 700px) {
  .compare-grid { grid-template-columns: 1fr; }
}
.compare-card {
  border: 1px solid var(--blue-border);
  border-radius: 8px;
  overflow: hidden;
}
.compare-card-header {
  padding: 0.55rem 1rem;
  font-weight: 700;
  font-size: 0.88rem;
  letter-spacing: 0.04em;
  color: var(--white);
}
.v20 .compare-card-header { background: var(--blue-mid); }
.v30 .compare-card-header { background: var(--blue-bright); }
.compare-card-body {
  padding: 0.9rem 1rem;
  background: var(--white);
  font-size: 0.91rem;
}
.compare-card-body ol, .compare-card-body ul {
  margin: 0; padding-left: 1.2rem;
}
.compare-card-body li { margin-bottom: 0.3rem; }

/* ── Tabelle ─────────────────────────────────────────────── */
table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.9rem;
  margin: 1rem 0 1.5rem;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 1px 6px rgba(13,43,78,0.07);
}
thead tr {
  background: var(--blue-deep);
  color: var(--white);
}
thead th {
  padding: 0.6rem 0.9rem;
  text-align: left;
  font-weight: 600;
  font-size: 0.82rem;
  letter-spacing: 0.05em;
}
tbody tr:nth-child(even) { background: var(--blue-light); }
tbody tr:nth-child(odd)  { background: var(--white); }
tbody td {
  padding: 0.55rem 0.9rem;
  border-bottom: 1px solid var(--blue-border);
}
tbody tr:last-child td { border-bottom: none; }

/* ── Codice ──────────────────────────────────────────────── */
pre {
  background: var(--blue-deep);
  color: #c9dff5;
  border-radius: 7px;
  padding: 1rem 1.2rem;
  overflow-x: auto;
  font-size: 0.83rem;
  line-height: 1.6;
  margin: 0.8rem 0 1.2rem;
  box-shadow: 0 2px 10px rgba(13,43,78,0.15);
}
code {
  background: var(--blue-light);
  color: var(--blue-deep);
  border-radius: 3px;
  padding: 0.1em 0.35em;
  font-size: 0.88em;
}
pre code {
  background: none;
  color: inherit;
  padding: 0;
}

/* ── H3 interni ──────────────────────────────────────────── */
h3 {
  color: var(--blue-mid);
  font-size: 1rem;
  margin: 1.4rem 0 0.6rem;
  padding-left: 0.7rem;
  border-left: 3px solid var(--blue-accent);
}

/* ── Badge versione inline ───────────────────────────────── */
.badge {
  display: inline-block;
  padding: 0.1em 0.55em;
  border-radius: 3px;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  vertical-align: middle;
}
.badge-v20 { background: var(--blue-mid);    color: var(--white); }
.badge-v30 { background: var(--blue-bright); color: var(--white); }
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
| TCP/IP – UDP | ✅ | ✅ (TCP Server) |
| EtherNet/IP | ✅ | ✅ |
| Profinet | ❌ | ✅ |
| Modbus | ❌ | ✅ |
| Digital I/O | ✅ | ✅ (opzionale) |


---

<div class="section-title">
  <span class="section-num">2</span>
  <h2>Interfaccia utente: com'è fatta e come si accede</h2>
</div>

<div class="compare-grid">

<div class="compare-card v20">
  <div class="compare-card-header">FlexiBowl® 2.0 — Software Parameters</div>
  <div class="compare-card-body">

Applicazione **desktop** chiamata **FlexiBowl® Parameters**, da installare sul PC di controllo.

**Installazione e accesso:**
1. Installare il programma **FlexiBowl® Parameters** sul PC.
2. Collegare il PC tramite **cavo Ethernet**.
3. Avviare il programma e inserire l'**indirizzo IP** del FlexiBowl®.

**Menu laterale:**

| Voce | Descrizione |
|---|---|
| **1 – Main Commands** | Configurazione e test di Move e Shake |
| **2 – Try Commands** | Sequenze combinate di comandi |
| **3 – Monitor** | Stato I/O, driver e allarmi |
| **4 – Console** | Comandi stringa diretti al driver |
| **5 – Reset Option** | Ripristino parametri e svuotamento manuale |

  </div>
</div>

<div class="compare-card v30">
  <div class="compare-card-header">FlexiBowl® 3.0 — Interfaccia Web</div>
  <div class="compare-card-body">

Interfaccia **completamente web-based**: nessuna installazione richiesta. È sufficiente un browser moderno.

**Accesso:**
1. Collegare il PC tramite Ethernet.
2. Aprire il browser e digitare l'**indirizzo IP** del FlexiBowl®.
3. Si apre la **Home page** dell'interfaccia.

**Menu laterale:** pagine dedicate a ogni funzione — Main Command, Jog Motor, Setup, Monitor, ecc. — accessibili direttamente dal browser.

  </div>
</div>

</div>

:::{note}
  Se il sistema in uso è FlexiVision One, la configurazione viene gestita dalla sua interfaccia dedicata. Non è necessario utilizzare l'interfaccia software FlexiBowl® descritta in questa sezione.
:::

---

## 3. Come cambiare l'indirizzo IP

### FlexiBowl® 2.0

1. Utilizzare il programma fornito sulla USB.

:::{note} 
Se è installata una versione precedente del programma, è necessario disinstallarla prima.
::: 

2. Collegare il FlexiBowl® tramite cavo Ethernet.
3. Accendere il dispositivo.
4. Avviare il programma.
5. Nella casella **IP Address**, inserire l'indirizzo di rete: `192.168.1.10`.
   > L'indirizzo IP del PC collegato deve essere necessariamente nella stessa subnet mask di Classe B (Subnet Mask 255.255.0.0).
6. Premere **Ping**: verrà visualizzato un pop-up con la scritta **"FlexiBowl® found"**.
7. Premere **Ok** per abilitare il pulsante **CONNECT** e avviare la connessione.
8. Dopo la connessione, verrà visualizzata la schermata principale (home screen).

### FlexiBowl® 3.0

1. Aprire il browser e accedere all'interfaccia tramite l'IP corrente.
2. Dal menu laterale, aprire la pagina **Setup**.
3. Cliccare su **Get IP** per leggere i parametri di rete correnti.
4. Inserire il nuovo indirizzo IP nei campi dedicati e cliccare **Set IP**.
5. Cliccare **Apply** per confermare, poi **Reboot** per rendere effettive le modifiche.

:::{important}
Dopo il reboot, riconnettersi al FlexiBowl® utilizzando il nuovo indirizzo IP impostato.
:::

---

## 4. Come gestire i movimenti

### FlexiBowl® 2.0

I movimenti vengono configurati e testati direttamente dall'interfaccia **Main Commands**, che espone tre pannelli:

- **Move**: imposta Acceleration, Deceleration, Speed e Angle tramite slider o campo numerico. Il pulsante **Test Move** esegue il movimento con i valori impostati.
- **Shake**: espone i parametri CCW Angle, CW Angle, Count, Acceleration, Deceleration e Speed. Il pulsante **Test Shake** esegue lo shake.
- **Try Commands**: permette di combinare più comandi in una sequenza con un numero configurabile di loop, selezionando i comandi dalla lista **All Commands** e aggiungendoli alla lista **Selected Commands**.

Per eseguire movimenti in produzione tramite protocollo, si inviano comandi ASCII (es. `QX2` per Move, `QX6` per Shake) attraverso il canale TCP/UDP configurato.

### FlexiBowl® 3.0

I movimenti sono organizzati in **sequenze** (fino a 20), configurabili dalla pagina **Main Command** dell'interfaccia web. Ogni sequenza contiene una lista di comandi (fino a 10 slot), con i relativi parametri di Move, Shake, Flip e Blow.

Dalla pagina **Main Command** è possibile:

- Selezionare la sequenza da configurare tramite il menu a tendina **Select the sequence**.
- Impostare tutti i parametri (Acceleration/Deceleration/Speed Move, Angle Move, parametri Shake, Flip e Blow) direttamente nei campi numerici.
- Aggiungere comandi alla lista tramite il selettore **Command Available** + pulsante **ADD**.
- Riordinare i comandi con i pulsanti **UP** / **DOWN**, eliminarli con **DELETE** o svuotare la lista con **CLEAR**.
- Testare la sequenza con **TEST SEQUENCE** o avviarla in produzione con **RUN**.

Per la modalità manuale continua, la pagina **Jog Motor** consente di avviare una rotazione continua con parametri di Speed (positivo = orario, negativo = antiorario), Acceleration e Deceleration, con possibilità di attivare contestualmente Flip e Blow.

Per eseguire movimenti in produzione tramite protocollo, si invia la ControlWord corrispondente (es. `10[0]%` per eseguire la Sequenza 1 via TCP, oppure ControlWord `10` via EtherNet/IP o Profinet).

---

## 5. Come cambiare i parametri

### FlexiBowl® 2.0

I parametri operativi (velocità, angoli, accelerazioni) vengono modificati in due modalità:

- **Interfaccia grafica**: tramite gli slider o i campi numerici nelle schermate Move e Shake di **Main Commands**.
- **Via protocollo (runtime)**: usando comandi di lettura/scrittura come `RW` (Write) e `RL` (Read) inviati tramite TCP/UDP. I valori da inviare al driver devono essere moltiplicati per il **fattore di riduzione** della macchina (ottenuto con il comando `RR114`), poiché i parametri sono espressi in unità interne del driver.

### FlexiBowl® 3.0

I parametri vengono modificati in tre modalità:

- **Interfaccia web**: direttamente nei campi numerici della pagina **Main Command** per ogni sequenza.
- **Via protocollo WRITE**: usando le ControlWord del blocco WRITE (formula: `N × 100 + offset_parametro`) per scrivere singoli parametri di una sequenza dall'esterno.
- **Via protocollo READ**: usando le ControlWord del blocco READ (formula: `10000 + N × 100 + offset_parametro`) per leggere i valori correnti.



---

### Esempio pratico: Move + Shake su FlexiBowl® 800

Lo scenario è il seguente: eseguire un **Move** a 360°, poi uno **Shake**, poi un wait di 200 ms; 
#### Con FlexiBowl® 2.0

I parametri devono essere scalati tramite il **fattore di riduzione** della macchina. La sequenza di comandi da inviare via TCP è:

```
QX7                          → Accendi backlight
RR114                        → Leggi fattore di riduzione → variabile_riduzione

RL1 (50 × variabile_riduzione)  → RW11  → Scrivi Acceleration Move = 50%
RL1 (50 × variabile_riduzione)  → RW12  → Scrivi Deceleration Move = 50%
RL1 (35 × variabile_riduzione)  → RW13  → Scrivi Speed Move = 35%
RL1 (360 × variabile_riduzione) → RW14  → Scrivi Angle Move = 360°
QX2                          → Esegui Move

RL1 (50 × variabile_riduzione)  → RW15  → Scrivi Acceleration Shake = 50%
RL1 (50 × variabile_riduzione)  → RW16  → Scrivi Deceleration Shake = 50%
RL1 (50 × variabile_riduzione)  → RW110 → Scrivi Speed Shake = 50%
RL1 (30 × variabile_riduzione)  → RW18  → Scrivi Angle CW Shake = -30°
RL1 (30 × variabile_riduzione)  → RW19  → Scrivi Angle CCW Shake = -45°
RL1 2                        → RW17  → Scrivi Count Shake = 2
QX6                          → Esegui Shake
```

Il wait di 200 ms è gestito dal sistema chiamante (robot o PLC), in attesa che il FlexiBowl® abbia completato il comando corrente prima di inviare il successivo.

#### Con FlexiBowl® 3.0

I parametri si impostano direttamente dall'interfaccia web, senza conversioni. Dalla pagina **Main Command**:

1. Selezionare **SEQUENCE 1** dal menu a tendina.
2. Impostare i campi:
   - Acceleration Move: `50 %`
   - Deceleration Move: `50 %`
   - Speed Move: `35 %`
   - Angle Move: `360 Degree`
   - Acceleration Shake: `50 %`
   - Deceleration Shake: `50 %`
   - Speed Shake: `50 %`
   - Ccw Angle Shake: `-45 Degree`
   - Cw Angle Shake: `-30 Degree`
   - Count Shake: `2 N°`
![pagina sequence](../../../../_shared/media/images/sequence.png)

3. Aggiungere alla lista dei comandi: `FLB_MOVE`, poi `FLB_SHAKE`.
4. Verificare che il Backlight sia abilitato dalla pagina **Option** (toggle Backlight 1).
5. Il wait di 200 ms si gestisce aggiungendo il comando `FLB_WAIT` alla lista con il valore opportuno, oppure lato sistema chiamante.

Per eseguire la sequenza via protocollo TCP, inviare:

```
10[0]%    → Esegui Sequenza 1
```

Il sistema risponde con `10[0]` a conferma dell'avvenuta esecuzione. 

---

## 6. Come leggere gli allarmi

### FlexiBowl® 2.0

Gli allarmi si consultano dalla sezione **Monitor → Alarm Status** del programma **FlexiBowl® Parameters**. La schermata mostra una lista di stati del driver con indicatori LED (verde = OK, rosso = errore). La schermata **Driver Status** mostra in tempo reale tutte le variabili operative (Motor Enabled, In Motion, Drive Fault, ecc.).

Per il reset di un allarme via protocollo, inviare:

```
Chr(0)Chr(7)QX12Chr(13)    → Reset allarme e riabilitazione motore
```

### FlexiBowl® 3.0

Gli allarmi si consultano dalla pagina **Monitor** dell'interfaccia web, con tre tab: **I/O Status**, **Driver Status** e **Alarm Status**.

Via protocollo, il segnale di allarme è esposto dalla variabile di output **In_Error** (BOOL) e il codice dell'errore attivo è disponibile in **ErrorCode** (UDINT). Per leggere lo stato via TCP:

```
InError%         → risposta: InError[1]% se c'è errore, InError[0]% se OK
ErrorCode%       → risposta: ErrorCode[N]% con il codice dell'errore attivo##
```

Per il reset dell'allarme:

- Via protocollo TCP: `Reset%`
- Via variabile digitale: fronte di salita sul segnale di input **Reset** (BOOL)

:::{warning}
Prima di eseguire il reset, identificare e risolvere la causa dell'errore. Il sistema non eseguirà nuovi comandi di movimento finché è presente un errore attivo.
:::

:::{note}
Per la lista completa dei codici errore fare riferimento alla sezione [Codici Di Errore](sec-err)
:::
---

## 7. Modalità tracking (FlexiTrack)

### FlexiBowl® 2.0 

La modalità **FlexiTrack** è un'opzione acquistabile separatamente che consente di mantenere il FlexiBowl® in **rotazione continua** (jog) sincronizzando il segnale encoder con il robot di pick, per aumentare la produttività in applicazioni ad alta cadenza.

**Hardware richiesto:**

- Connessione all'**encoder interno** tramite il connettore del pannello di controllo (segnale quadratura TTL, 4000 conteggi/giro sul motore; per FlexiBowl® 500/650/800 con riduzione 1:3 → 12000 conteggi/giro sul disco).
- In alternativa, installazione di un **encoder esterno** (incremental, TTL RS422, ≥ 12000 ppr) sul perno solidale alla puleggia condotta.

:::{important}
Con FlexiTrack, il controllo del movimento è possibile **solo via protocollo Ethernet** (TCP/UDP). Il protocollo Digital I/O non è supportato.
:::

**Comandi principali FlexiTrack (inviati via TCP/UDP):**

| Comando | Descrizione |
|---|---|
| `JA<valore>` | Imposta accelerazione/decelerazione in giri/s² |
| `JL<valore>` | Imposta decelerazione (se diversa da JA, inviare dopo JA) |
| `JS<valore>` | Imposta velocità di rotazione in giri/s |
| `CC<valore>` | Imposta corrente diretta al motore |
| `DI1` | Direzione oraria |
| `DI-1` | Direzione antioraria |
| `CJ` | Avvia jog (rotazione continua) |
| `SJ` | Ferma jog (con rampa JL) |
| `IL2` / `IH2` | Attiva / disattiva Flip |
| `IL3` / `IH3` | Attiva / disattiva Blow |

**Parametri consigliati:**

```
JA0.2    → accelerazione 0.2 giri/s²
JL0.2    → decelerazione 0.2 giri/s²
JS0.2    → velocità 0.2 giri/s
CC1.3    → corrente motore
DI1      → rotazione oraria
```

Flip e Blow, non gestibili con i comandi `QX` standard durante il jog, vanno implementati tramite un **programma in background** con ciclo iterativo che commuta lo stato delle valvole con i tempi e le iterazioni desiderati.

---

### FlexiBowl® 3.0

Nel FlexiBowl® 3.0, la modalità di rotazione continua è integrata nativamente nella pagina **Jog Motor** dell'interfaccia web, senza necessità di opzioni hardware aggiuntive.

**Parametri di movimento Jog:**

| Parametro | Unità | Descrizione |
|---|---|---|
| Acceleration | % | Rampa di accelerazione all'avvio |
| Deceleration | % | Rampa di decelerazione all'arresto |
| Speed | % | Velocità di rotazione. Valore **positivo** = orario; valore **negativo** = antiorario |

**Funzioni accessorie durante il Jog:**

Il jog gestisce direttamente Flip e Blow tramite toggle dedicati, senza necessità di programmi in background:

- **Flip Enable**: abilita il flip automatico ciclico durante il jog, con parametri di Flip Duration, Flip Pression e Flip Pause configurabili direttamente nell'interfaccia.
- **Blow Enable**: abilita il soffio automatico ciclico, con Blow Duration, Blow Pression, Blow Pause e Blow Type (BLOWc, BLOWe, BLOWc+BLOWe).
- **Backlight 1 / Backlight 2**: toggle per la gestione retroilluminazione, indipendente dallo stato del jog.

**Avvio e arresto:**

- **START JOG**: avvia la rotazione continua con i parametri impostati.
- **STOP JOG**: interrompe il jog con rampa di decelerazione.

Per controllare il jog via protocollo, usare le ControlWord EXE:

```
40[0]%    → Start Jog Seq (via TCP)
41[0]%    → Stop Jog Seq (via TCP)
```

:::{important}
Prima di avviare il jog, verificare che il motore sia abilitato (**ENABLE MOTOR** attivo) e che lo stato del sistema sia **READY**.
:::

---