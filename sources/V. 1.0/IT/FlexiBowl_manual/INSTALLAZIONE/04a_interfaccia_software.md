(fieldbus)=
# Ethernet/IP, Profinet, Modbus

Per **EtherNet/IP**, **Profinet** e **Modbus** le variabili di [Input](#sec-io) e [Output](#sec-io) vengono scambiate come **pacchetto di I/O ciclico**: non esistono messaggi testuali, ogni variabile occupa una posizione fissa nel pacchetto dati.

### Pacchetto dati — Input (verso il FlexiBowl®)

| ControlWord | Data_1 | ExecuteControlWord | Hopper_1 | Hopper_2 | Hopper_3 | Hopper_4 | Reset |
|---|---|---|---|---|---|---|---|
| *(numero comando)* | *(argomento)* | *(bit trigger 0→1)* | *(bit)* | *(bit)* | *(bit)* | *(bit)* | *(bit)* |

### Pacchetto dati — Output (dal FlexiBowl®)

| Busy | Ready | In_Error | In_PowerOn | ReturnData_1 | ReturnData_2 | ErrorCode |
|---|---|---|---|---|---|---|
| *(bit)* | *(bit)* | *(bit)* | *(bit)* | *(eco ControlWord)* | *(dato letto)* | *(codice errore)* |

:::{note}
La sequenza di scrittura è sempre la stessa: impostare **ControlWord** (e **Data_1** se richiesto) con **ExecuteControlWord = 0**, poi portare **ExecuteControlWord** a `1` per generare il fronte di salita che avvia l'esecuzione.
:::


## Protocollo Comandi

Il protocollo comandi definisce tutte le azioni disponibili attraverso la ControlWord. Le ControlWord sono **le stesse per tutti i protocolli**; cambia solo il trasporto (vedi [Trasporto Fieldbus](#sec-fieldbus) e [Sintassi TCP](#sec-tcp)). I comandi sono raggruppati in categorie:

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

(fieldbus_exe)=
#### Esempio pratico — «Esegui Sequenza 3»

<div class="isw-example">
<div class="isw-example-title">Esegui Sequenza 3 → ControlWord 12</div>
<div class="isw-example-body">
<div>
<div class="isw-example-col-title">EtherNet/IP · Profinet · Modbus</div>

Pacchetto inviato:

| ControlWord | Data_1 | ExecuteCW | Hopper_1 | Hopper_2 | Hopper_3 | Hopper_4 | Reset |
|---|---|---|---|---|---|---|---|
| 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 12 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |

Pacchetto ricevuto:

| Busy | Ready | In_Error | In_PowerOn | ReturnData_1 | ReturnData_2 | ErrorCode |
|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 1 | 12 | 0 | 0 |


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
| Emptying Sequence | 40 | 0–1 | 0 = modalità normale, 1 = modalità Quick Emptying |
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

(fieldbus_write)=
#### Esempio pratico — «Imposta l'accelerazione del Move a 80 nella Sequenza 7»

<div class="isw-example">
<div class="isw-example-title">SpeedMove Seq 7 → ControlWord 700, Data_1 = 80</div>
<div class="isw-example-body">
<div>
<div class="isw-example-col-title">EtherNet/IP · Profinet · Modbus</div>

Pacchetto inviato:

| ControlWord | Data_1 | ExecuteCW | Hopper_1 | Hopper_2 | Hopper_3 | Hopper_4 | Reset |
|---|---|---|---|---|---|---|---|
| 700 | 80 | 0 | 0 | 0 | 0 | 0 | 0 |
| 700 | 80 | 1 | 0 | 0 | 0 | 0 | 0 |

Pacchetto ricevuto:

| Busy | Ready | In_Error | In_PowerOn | ReturnData_1 | ReturnData_2 | ErrorCode |
|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 1 | 700 | 0 | 0 |


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

(fieldbus_read)=
#### Esempio pratico — «Leggi l'angolo della Sequenza 16»

<div class="isw-example">
<div class="isw-example-title">AngleMove Seq 16 → ControlWord 11603</div>
<div class="isw-example-body">
<div>
<div class="isw-example-col-title">EtherNet/IP · Profinet · Modbus</div>

Pacchetto inviato:

| ControlWord | Data_1 | ExecuteCW | Hopper_1 | Hopper_2 | Hopper_3 | Hopper_4 | Reset |
|---|---|---|---|---|---|---|---|
| 11603 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 11603 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |

Pacchetto ricevuto (angolo letto = 45°):

| Busy | Ready | In_Error | In_PowerOn | ReturnData_1 | ReturnData_2 | ErrorCode |
|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 1 | 11603 | 45 | 0 |


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

---

(sec-hopper)=
## Comandi <span class="isw-section-badge isw-badge-hop"><i class="ph ph-funnel"></i> HOPPER</span>

I comandi Hopper controllano le Bulk Feeder vibrazionali collegate al sistema (fino a 4). Seguono la stessa logica ControlWord/WRITE/READ descritta sopra, valida per tutti i protocolli, più una sintassi TCP dedicata per l'avvio rapido.

### Avvio rapido via TCP

Oltre alla sintassi generale ControlWord, il protocollo **TCP Server** offre messaggi dedicati per avviare direttamente un hopper:

| Operazione | Messaggio da inviare | Risposta |
|---|---|---|
| Avvia Hopper 1 | `Hopper1Start%` | `Hopper1Start *` |
| Avvia Hopper 2 | `Hopper2Start%` | `Hopper2Start *` |
| Avvia Hopper 3 | `Hopper3Start%` | `Hopper3Start *` |
| Avvia Hopper 4 | `Hopper4Start%` | `Hopper4Start *` |

Sui protocolli fieldbus (EtherNet/IP, Profinet, Modbus) lo stesso avvio immediato si ottiene impostando direttamente a `1` il bit **Hopper_1**...**Hopper_4** del [pacchetto I/O](#sec-fieldbus), senza passare dalla ControlWord.

### Comandi WRITE Hopper

| Parametro | ControlWord | Range Data_1 | Descrizione |
|---|---|---|---|
| Hopper_1_Id | 30001 | 1–100 | ID univoco dell'hopper 1 sulla rete |
| Hopper_1_Amplitude | 30002 | 50–220 | Ampiezza vibrazione hopper 1 |
| Hopper_1_Frequency | 30003 | 40–70 | Frequenza vibrazione hopper 1 |
| Hopper_1_Activation_Time | 30004 | 400–60000 | Tempo di attivazione hopper 1 (ms) |
| Hopper_2_Id | 30005 | 1–100 | ID univoco dell'hopper 2 |
| Hopper_2_Amplitude | 30006 | 50–220 | Ampiezza vibrazione hopper 2 |
| Hopper_2_Frequency | 30007 | 40–70 | Frequenza vibrazione hopper 2 |
| Hopper_2_Activation_Time | 30008 | 400–60000 | Tempo di attivazione hopper 2 (ms) |
| Hopper_3_Id | 30009 | 1–100 | ID univoco dell'hopper 3 |
| Hopper_3_Amplitude | 30010 | 50–220 | Ampiezza vibrazione hopper 3 |
| Hopper_3_Frequency | 30011 | 40–70 | Frequenza vibrazione hopper 3 |
| Hopper_3_Activation_Time | 30012 | 400–60000 | Tempo di attivazione hopper 3 (ms) |
| Hopper_4_Id | 30013 | 1–100 | ID univoco dell'hopper 4 |
| Hopper_4_Amplitude | 30014 | 50–220 | Ampiezza vibrazione hopper 4 |
| Hopper_4_Frequency | 30015 | 40–70 | Frequenza vibrazione hopper 4 |
| Hopper_4_Activation_Time | 30016 | 400–60000 | Tempo di attivazione hopper 4 (ms) |
| Hopper_1_Enable | 30017 | — | Abilita hopper 1 (azione immediata) |
| Hopper_1_Disable | 30018 | — | Disabilita hopper 1 (azione immediata) |
| Hopper_2_Enable | 30019 | — | Abilita hopper 2 |
| Hopper_2_Disable | 30020 | — | Disabilita hopper 2 |
| Hopper_3_Enable | 30021 | — | Abilita hopper 3 |
| Hopper_3_Disable | 30022 | — | Disabilita hopper 3 |
| Hopper_4_Enable | 30023 | — | Abilita hopper 4 |
| Hopper_4_Disable | 30024 | — | Disabilita hopper 4 |

:::{note}
Nel materiale di training, la ControlWord `30005` (Hopper_2_Id) riportava per errore lo stesso range dell'Amplitude (50–220). In questa tabella è stata corretta a **1–100**, coerente con Hopper_1_Id, Hopper_3_Id e Hopper_4_Id. Verificare questo valore con il firmware/datasheet prima di pubblicare la pagina.
:::

(fieldbus_WRITEHOPPER)=
#### Esempio pratico — «Abilita Hopper 1»

<div class="isw-example">
<div class="isw-example-title">Hopper_1_Enable → ControlWord 30017</div>
<div class="isw-example-body">
<div>
<div class="isw-example-col-title">EtherNet/IP · Profinet · Modbus</div>

Pacchetto inviato:

| ControlWord | Data_1 | ExecuteCW | Hopper_1 | Hopper_2 | Hopper_3 | Hopper_4 | Reset |
|---|---|---|---|---|---|---|---|
| 30017 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 30017 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |

Pacchetto ricevuto:

| Busy | Ready | In_Error | In_PowerOn | ReturnData_1 | ReturnData_2 | ErrorCode |
|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 1 | 30017 | 0 | 0 |



#### Esempio pratico — «Imposta l'ampiezza dell'Hopper 2 a 220»

<div class="isw-example">
<div class="isw-example-title">Hopper_2_Amplitude → ControlWord 30006, Data_1 = 220</div>
<div class="isw-example-body">
<div>
<div class="isw-example-col-title">EtherNet/IP · Profinet · Modbus</div>

Pacchetto inviato:

| ControlWord | Data_1 | ExecuteCW | Hopper_1 | Hopper_2 | Hopper_3 | Hopper_4 | Reset |
|---|---|---|---|---|---|---|---|
| 30006 | 220 | 0 | 0 | 0 | 0 | 0 | 0 |
| 30006 | 220 | 1 | 0 | 0 | 0 | 0 | 0 |

Pacchetto ricevuto:

| Busy | Ready | In_Error | In_PowerOn | ReturnData_1 | ReturnData_2 | ErrorCode |
|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 1 | 30006 | 0 | 0 |


### Comandi READ Hopper

| Parametro | ControlWord READ | Range ReturnData_2 | Note |
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

(fieldbus_READHOPPER)=
#### Esempio pratico — «Leggi la frequenza dell'Hopper 4»

<div class="isw-example">
<div class="isw-example-title">Hopper_4_Frequency → ControlWord 30115</div>
<div class="isw-example-body">
<div>
<div class="isw-example-col-title">EtherNet/IP · Profinet · Modbus</div>

Pacchetto inviato:

| ControlWord | Data_1 | ExecuteCW | Hopper_1 | Hopper_2 | Hopper_3 | Hopper_4 | Reset |
|---|---|---|---|---|---|---|---|
| 30115 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 30115 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |

Pacchetto ricevuto (frequenza letta = 40):

| Busy | Ready | In_Error | In_PowerOn | ReturnData_1 | ReturnData_2 | ErrorCode |
|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 1 | 30115 | 40 | 0 |


:::{note}
Per i comandi di Quick Emptying, fare riferimento alla sezione [Comandi di Quick Emptying](sec-empty)
:::

:::{important}
Per i Codici di Errore, fare riferimento alla sezione [Codici di Errore](sec-err)
:::

(digIO)=
## Ingressi Digitali e Analogici (Digital I/O)

Il connettore di ingresso della nuova generazione di FlexiBowl® supporta segnali digitali e analogici per l'integrazione diretta con un PLC senza necessità di comunicazione Ethernet.

### Ingressi disponibili sul connettore principale

| Tipo | Segnale | Tipo elettrico | Livello attivo | Descrizione |
|---|---|---|---|---|
| Standard | Bit 1 | Digitale | 0–24Vdc, Attivo Alto | Bit di codifica comando (vedi tabella codifica) |
| Standard | Bit 2 | Digitale | 0–24Vdc, Attivo Alto | Bit di codifica comando |
| Standard | Bit 3 | Digitale | 0–24Vdc, Attivo Alto | Bit di codifica comando |
| Standard | Bit 4 | Digitale | 0–24Vdc, Attivo Alto | Bit di codifica comando |
| Standard | Bit 5 | Digitale | 0–24Vdc, Attivo Alto | Bit di codifica comando |
| Standard | Latch | Digitale | 0–24Vdc, Attivo Alto | Esecuzione comando (fronte di salita) |
| Standard | Empty Sensor | Digitale | 0–24Vdc, Attivo Alto | Sensore rilevamento FlexiBowl®  vuoto |
| Standard | Zeroing | Digitale | 0–24Vdc, Attivo Alto | Previsione per sensore fissatura disco multi-settori |
| Opzione | Ritorno valvola proporzionale flip | Analogico | 0–10Vdc | Segnale di feedback valvola proporzionale flip |
| Opzione | Ritorno valvola proporzionale blow | Analogico | 0–10Vdc | Segnale di feedback valvola proporzionale blow |
| Opzione | Strobe Backlight + / − | — | — | Comando strobe backlight esterno (protezione con diodo e fusibile richiesta) |
| Opzione | Strobe Backlight 2+ / 2− | — | — | Comando strobe backlight esterno secondario |

### Connettore STO (Safety Torque Off)

Il connettore STO è dedicato alla funzione di sicurezza per l'arresto del motore:

| Pin | Segnale | Descrizione |
|---|---|---|
| 1 | STO1+ | Safety Torque Off 1 |
| 2 | STO1- | Ritorno STO1 |
| 3 | STO2+ | Safety Torque Off 2 |
| 4 | STO2- | Ritorno STO2 |
| 5 | 24V | Alimentazione |
| 6 | 0V | Massa |

### Codifica comandi tramite bit digitali (Bit 1–5)

I 5 bit di ingresso digitale formano una parola binaria a 5 cifre che identifica il comando da eseguire. Il comando viene acquisito sul fronte di salita del segnale **Latch**.

| Codice Binario (Bit5–Bit1) | Comando |
|---|---|
| `00000` | Reset allarmi |
| `00001` | Exe Seq 1 |
| `00010` | Exe Seq 2 |
| `00011` | Exe Seq 3 |
| `00100` | Exe Seq 4 |
| `00101` | Exe Seq 5 |
| `00110` | Exe Seq 6 |
| `00111` | Exe Seq 7 |
| `01000` | Exe Seq 8 |
| `01001` | Exe Seq 9 |
| `01010` | Exe Seq 10 |
| `01011` | Exe Seq 11 |
| `01100` | Exe Seq 12 |
| `01101` | Exe Seq 13 |
| `01110` | Exe Seq 14 |
| `01111` | Exe Seq 15 |
| `10000` | Exe Seq 16 |
| `10001` | Exe Seq 17 |
| `10010` | Exe Seq 18 |
| `10011` | Exe Seq 19 |
| `10100` | Exe Seq 20 |
| `10101` | Hopper Activation 1 |
| `10110` | Hopper Activation 2 |
| `10111` | Hopper Activation 3 |
| `11000` | Hopper Activation 4 |
| `11001`–`11111` | Spare |

:::{tip}
Esempio: per eseguire la Sequenza 5, impostare Bit1=1, Bit2=0, Bit3=1, Bit4=0, Bit5=0 (codice binario `00101`) e poi inviare un fronte di salita su **Latch**.
:::

---

### Schema ConfigIO — Configurazione PLC 

Il seguente schema descrive la configurazione tipica di un PLC Wago utilizzato per il controllo del FlexiBowl® tramite Digital I/O.

**Hardware utilizzato:**
- CPU: PFC300, 2× Ethernet, RS-485
- Moduli I/O digitali: 8DI/8DO (750-1502) — 2 moduli
- Modulo ingressi analogici: 0–10V (750-467)
- Modulo uscite analogiche: 0–10V (750-550)

#### Ingressi digitali (DI) — Modulo 1

| DI | Descrizione |
|---|---|
| 1 | Bit 1 — Seg. Cmd |
| 2 | Bit 2 — Seg. Cmd |
| 3 | Bit 3 — Seg. Cmd |
| 4 | Bit 4 — Seg. Cmd |
| 5 | Latch |
| 6 | Empty Sensor |
| 7 | Zeroing |
| 8 | Spare |

#### Uscite digitali (DO) — Modulo 1

| DO | Descrizione |
|---|---|
| 1 | Backlight 1 & 2 |
| 2 | Ready Led + Sgn |
| 3 | Fault Led + Sgn |
| 4 | Busy Sgn |
| 5 | Flip 1 Comando |
| 6 | Blow 1 Comando |
| 7 | Blow 2 Comando |
| 8 | Cmd Slitta Empty |

#### Ingressi analogici (AI)

| AI | Descrizione |
|---|---|
| 1 | Feedback Elv. Flip |
| 2 | Feedback Elv. Blow |

#### Uscite analogiche (AO)

| AO | Descrizione |
|---|---|
| 1 | Regol. Elv. Flip |
| 2 | Regol. Elv. Blow |
