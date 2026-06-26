(quickstart)=
# **Quickstart**
## Ingressi Digitali e Analogici (Digital I/O)

:::{note}
La modalità **Digital I/O** è un'opzione acquistabile separatamente e non è inclusa nella configurazione standard del FlexiBowl®.
:::

Il connettore di ingresso del FlexiBowl® EVO supporta segnali digitali e analogici per l'integrazione diretta con un PLC senza necessità di comunicazione Ethernet.

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

## Schema ConfigIO — Configurazione PLC (Wago)

Il seguente schema descrive la configurazione tipica di un PLC Wago utilizzato per il controllo del FlexiBowl® tramite Digital I/O.

**Hardware utilizzato:**
- CPU: PFC300, 2× Ethernet, RS-485
- Moduli I/O digitali: 8DI/8DO (750-1502) — 2 moduli
- Modulo ingressi analogici: 0–10V (750-467)
- Modulo uscite analogiche: 0–10V (750-550)

### Ingressi digitali (DI) — Modulo 1

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

### Uscite digitali (DO) — Modulo 1

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

### Ingressi analogici (AI)

| AI | Descrizione |
|---|---|
| 1 | Feedback Elv. Flip |
| 2 | Feedback Elv. Blow |

### Uscite analogiche (AO)

| AO | Descrizione |
|---|---|
| 1 | Regol. Elv. Flip |
| 2 | Regol. Elv. Blow |
