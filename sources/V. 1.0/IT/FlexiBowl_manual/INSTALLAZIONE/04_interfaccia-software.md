# **Interfaccia Software**

## Introduzione

Questa sezione descrive come il FlexiBowl® comunica con i sistemi esterni. La comprensione di questa interfaccia è necessaria per integrare il FlexiBowl® in una cella automatizzata.

Il sistema di comunicazione è basato su un modello a **variabili di Input/Output** e **Control Word numeriche**: il sistema esterno invia un numero (la ControlWord) che identifica l'azione da eseguire e il FlexiBowl® risponde con segnali di stato e dati di ritorno.

I protocolli di comunicazione supportati sono:
- **TCP Server** (Ethernet, via browser o socket)
- **EtherNet/IP**
- **Profinet**
- **Modbus**

---

## Variabili di Input e Output

Le variabili I/O sono i segnali che viaggiano tra il sistema esterno e il FlexiBowl®. Si dividono in **INPUT** (dal sistema esterno verso il FlexiBowl®) e **OUTPUT** (dal FlexiBowl® verso il sistema esterno).

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

---

## Protocollo Comandi

Il protocollo comandi definisce tutte le azioni disponibili attraverso la ControlWord. I comandi sono raggruppati in tre categorie:

- **EXE**: comandi di esecuzione (avvio sequenze, jog, reset)
- **WRITE**: scrittura di parametri (velocità, angoli, tempi, ecc.)
- **READ**: lettura dei parametri attualmente configurati

### Come funziona un comando

1. Il sistema esterno imposta la **ControlWord** con il numero del comando desiderato.
2. Se il comando richiede un argomento, imposta anche **Data_1**.
3. Invia un fronte di salita su **ExecuteControlWord**.
4. Attende che **Busy** torni a `0` e che **ReturnData_1** restituisca il valore della ControlWord (conferma di esecuzione corretta).

:::{warning}
Non inviare un nuovo comando mentre **Busy** è a `1`. Il sistema ignorerà il comando e **ReturnData_1** restituirà il valore `3` (sistema occupato).
:::

---

### Comandi EXE 

I comandi EXE avviano un'azione immediata sul FlexiBowl®. Durante l'esecuzione, **Busy** rimane a `1`.

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

---

### Comandi WRITE 

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

### Comandi READ 

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

## Codici di Errore 
 
Nel caso in cui si verifica un errore, è possibile visualizzarlo tramite il comando `ErrorCode%`. Il valore di ritonro sarà della forma `ErrorCode[X]%`, dove X rappresenta uno dei codici sottostanti: 

### Codici di Errore Generali

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

### Codici di Errore del Driver



:::{warning}
In presenza di un errore, il LED **In_Error** si attiva e il sistema non eseguirà nuovi comandi di movimento fino al reset. Prima di eseguire il reset, identificare e risolvere la causa dell'errore.
:::

| ErrorCode | ErrorCode (Hex) | Errore | Descrizione |
|---|---|---|---|
| 50 | 0x7500 | EtherCAT communication error | |
| 51 | 0xFF01 | Drive Over Current | corrente motore eccessiva |
| 52 | 0xFF02 | Drive Over Voltage | tensione bus DC eccessiva |
| 53 | 0xFF03 | Drive Over Temperature | temperatura driver troppo elevata |
| 54 | 0xFF04 | Reserved | |
| 55 | 0xFF05 | Drive Internal Voltage Error | errore tensione interna |
| 56 | 0xFF06 | Position Error | errore di posizionamento |
| 57 | 0xFF07 | Motor Encoder Disconnected | encoder non collegato o guasto |
| 58 | 0xFF0A | Regen Failed | errore nel circuito di rigenerazione |
| 59 | 0xFF0B | Safe Torque Off (STO) | funzione di sicurezza attiva |
| 60 | 0xFF0C | Reserved | |
| 61 | 0xFF0D | Bad FPGA | errore interno all'FPGA del driver |
| 62 | 0xFF0E | Parameter Read Failed | lettura parametri fallita |
| 63 | 0xFF0F | Motor Encoder Multi-turn Error | errore encoder multi-giro |
| 64 | 0xFF10 | Motor Stall Protection | protezione stallo motore attiva |
| 65 | 0xFF11 | Drive Power Module Over Temperature | modulo di potenza surriscaldato |
| 66 | 0xFF31 | N Limit | limite di posizione negativo raggiunto |
| 67 | 0xFF32 | P Limit | limite di posizione positivo raggiunto |
| 68 | 0xFF33 | N&P Limit | entrambi i limiti di posizione raggiunti |
| 69 | 0xFF34 | Current Foldback | riduzione corrente per protezione termica |
| 70 | 0xFF35 | Move @ Disabled | tentativo di movimento con driver disabilitato |
| 71 | 0xFF36 | Drive Low Voltage | tensione bus DC insufficiente |
| 72 | 0xFF37 | Blank Q Segment | segmento di traiettoria non definito |
| 73 | 0xFF38 | Velocity Limit | limite di velocità superato |
| 74 | 0xFF39 | Drive Power Phase Lost | perdita di una fase di alimentazione |
| 75 | 0xFF3A | Emergency Stop | arresto di emergenza attivo |
| 76 | 0xFF3B | Abs. Encoder Battery | batteria encoder assoluto scarica o assente |
| 77 | 0xFF3C | Abs. Position Lost Warning | avviso perdita posizione assoluta |
| 78 | 0xFF3D | Abs. Position Overflow | overflow posizione assoluta |
| 79 | 0xFF3E | Motor Over Temperature | temperatura motore eccessiva |
| 80 | 0xFF3F | Drive Voltage Warning | avviso tensione driver fuori range |
| 81 | 0xFF41 | Save Failed | salvataggio parametri fallito |
| 82 | 0xFFFF | Other Error | errore generico non classificato |

