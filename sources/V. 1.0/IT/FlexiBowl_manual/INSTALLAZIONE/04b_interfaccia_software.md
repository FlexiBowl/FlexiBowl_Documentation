(tcp)=
# TCP Server

Quando si utilizza la comunicazione **TCP Server**, i comandi non vengono inviati come variabili binarie ma come **stringhe di testo** attraverso una connessione socket sulla porta configurata (default: 8123).


Ogni messaggio ha la forma:

```
NomeVariabile[Valore]%
```

Il carattere `%` è il **terminatore di messaggio** e deve essere sempre presente alla fine. Il campo `[Valore]` contiene il dato numerico associato (ControlWord, stato, ecc.).

## Tabella di sintassi TCP

| Operazione | Messaggio da inviare | Risposta se OK | Risposta se errore |
|---|---|---|---|
| Tutti i comandi EXE | `10[0]%` | `10[0]%` | `1[0]%` |
| Tutti i comandi WRITE | `100[56]%` | `100[0]%` | `2[0]%` |
| Tutti i comandi READ | `10100[0]%` | `10100[valore]%` | `2[0]%` |
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

## Significato di ReturnData_1 (o risposta TCP)

| Valore | Significato |
|---|---|
| `0` | NULL — nessun comando in corso (stato iniziale) |
| `1` | Comando non interpretabile (ControlWord sconosciuta) |
| `2` | Data_1 fuori range, ma il comando è stato riconosciuto |
| `3` | Sistema occupato (Busy) — riprovare dopo che Busy torna a 0 |
| Valore = ControlWord | Comando eseguito correttamente |

---

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

(TCP_EXE)=
#### Esempio pratico — «Esegui Sequenza 3»

<div class="isw-example">
<div class="isw-example-title">Esegui Sequenza 3 → ControlWord 12</div>
<div class="isw-example-body">
<div>

<div>
<div class="isw-example-col-title">TCP Server</div>

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>12[0]%</code><br>
RETURN SE OK:&nbsp;&nbsp;&nbsp;<span class="ok">12[0]</span>
</div>

Esempio di comando **non valido** (es. sequenza 9 inesistente sul dispositivo):

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>9[0]%</code><br>
RETURN SE NON OK:&nbsp;&nbsp;&nbsp;<span class="ko">1[0]</span>
</div>

</div>
</div>
</div>

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

(TCP_write)=
#### Esempio pratico — «Imposta l'accelerazione del Move a 80 nella Sequenza 7»

<div class="isw-example">
<div class="isw-example-title">SpeedMove Seq 7 → ControlWord 700, Data_1 = 80</div>
<div class="isw-example-body">
<div>

<div>
<div class="isw-example-col-title">TCP Server</div>

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>700[80]%</code><br>
RETURN SE OK:&nbsp;&nbsp;&nbsp;<span class="ok">700[0]</span>
</div>

Esempio di **valore fuori range** (accelerazione 1000 non ammessa, range 1–100):

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>700[1000]%</code><br>
RETURN SE NON OK:&nbsp;&nbsp;&nbsp;<span class="ko">2[0]</span>
</div>

</div>
</div>
</div>

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

(TCP_read)=
#### Esempio pratico — «Leggi l'angolo della Sequenza 16»

<div class="isw-example">
<div class="isw-example-title">AngleMove Seq 16 → ControlWord 11603</div>
<div class="isw-example-body">
<div>

<div>
<div class="isw-example-col-title">TCP Server</div>

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>11603[0]%</code><br>
RETURN SE OK:&nbsp;&nbsp;&nbsp;<span class="ok">11603[45]</span>
</div>

Esempio di **valore fuori range** in scrittura sullo stesso parametro (angolo massimo 720°):

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>11603[6799]%</code><br>
RETURN SE NON OK:&nbsp;&nbsp;&nbsp;<span class="ko">1[0]</span>
</div>

</div>
</div>
</div>

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

I comandi Hopper controllano le tramogge vibrazionali collegate al sistema (fino a 4). Seguono la stessa logica ControlWord/WRITE/READ descritta sopra, valida per tutti i protocolli, più una sintassi TCP dedicata per l'avvio rapido.

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

(TCP_WRITEHOPPER)=
#### Esempio pratico — «Abilita Hopper 1»

<div class="isw-example">
<div class="isw-example-title">Hopper_1_Enable → ControlWord 30017</div>
<div class="isw-example-body">
<div>

<div>
<div class="isw-example-col-title">TCP Server</div>

Via ControlWord generica:

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>30017[0]%</code><br>
RETURN SE OK:&nbsp;&nbsp;&nbsp;<span class="ok">30017[0]</span>
</div>

Oppure, per il solo avvio, con il messaggio dedicato:

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>Hopper1Start%</code><br>
RETURN:&nbsp;&nbsp;&nbsp;<span class="ok">Hopper1Start *</span>
</div>

</div>
</div>
</div>

#### Esempio pratico — «Imposta l'ampiezza dell'Hopper 2 a 220»

<div class="isw-example">
<div class="isw-example-title">Hopper_2_Amplitude → ControlWord 30006, Data_1 = 220</div>
<div class="isw-example-body">
<div>

<div>
<div class="isw-example-col-title">TCP Server</div>

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>30006[220]%</code><br>
RETURN SE OK:&nbsp;&nbsp;&nbsp;<span class="ok">30006[0]</span>
</div>

Esempio di **valore fuori range** (ampiezza 2200 non ammessa, range 50–220):

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>30006[2200]%</code><br>
RETURN SE NON OK:&nbsp;&nbsp;&nbsp;<span class="ko">2[0]</span>
</div>

</div>
</div>
</div>

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

(TCP_READHOPPER)=
#### Esempio pratico — «Leggi la frequenza dell'Hopper 4»

<div class="isw-example">
<div class="isw-example-title">Hopper_4_Frequency → ControlWord 30115</div>
<div class="isw-example-body">
<div>

<div>
<div class="isw-example-col-title">TCP Server</div>

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>30115[0]%</code><br>
RETURN SE OK:&nbsp;&nbsp;&nbsp;<span class="ok">30115[40]</span>
</div>

Esempio di **comando non interpretabile** (ControlWord READ inesistente):

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>30199[0]%</code><br>
RETURN SE NON OK:&nbsp;&nbsp;&nbsp;<span class="ko">1[0]</span>
</div>

</div>
</div>
</div>

:::{note}
Per i comandi di Svuotamento, fare riferimento alla sezione [Comandi di Svuotamento](sec-empty)
:::

:::{important}
Per i Codici di Errore, fare riferimento alla sezione [Codici di Errore](sec-err)
:::