(cavi)=
# **Cavi di collegamento**

I cavi di collegamento del FlexiBowl® sono acquistabili separatamente come opzione, nelle lunghezze da **3, 5 o 10 metri**. Questa pagina riepiloga i cavi disponibili a listino, i relativi prerequisiti e le piedinature.

:::{note}
I cavi delle Bulk Feeder (cavo Modbus RTU e cavo Input del controller) sono descritti nella pagina {ref}`Accessori e Opzioni delle Bulk Feeder <tramoggia-cavi>`.
:::

:::{warning}
Collegare e scollegare i cavi solo a dispositivo spento e scollegato dall'alimentazione.
:::

## Riepilogo

:::{list-table}
:widths: 24 32 22 22
:header-rows: 1

* - Cavo
  - Prerequisiti
  - Taglie compatibili
  - Lunghezze
* - [Cavo per opzione I/O](cavo-io)
  - Opzione **Digital I/O** (acquistabile separatamente)
  - Tutte le taglie
  - · 3
    · 5
    · 10 m
* - [Cavo per quadro remoto (rack)](cavo-rack)
  - FlexiBowl® con rack esterno
  - FlexiBowl® 200 · 350
  - · 3 m incluso nella fornitura;
    · 5
    · 10 m
* - [Cavo di alimentazione](cavo-alim)
  - Nessuno
  - Tutte le taglie
  - · 3
    · 5
    · 10 m
* - [Cavo Ethernet](cavo-eth)
  - Nessuno
  - Tutte le taglie
  - · 3
    · 5
    · 10 m
:::

### Articoli a listino

:::{list-table}
:widths: 28 24 24 24
:header-rows: 1

* - Cavo
  - 3 m
  - 5 m
  - 10 m
* - **Opzione I/O**
  - FlexiBowl cable for I/O option, 3m
  - FlexiBowl cable for I/O option, 5m
  - FlexiBowl cable for I/O option, 10m
* - **Quadro remoto (rack)**
  - Cable for remote electronic cabinet, 3m
  - Cable for remote electronic cabinet, 5m
  - Cable for remote electronic cabinet, 10m
* - **Alimentazione**
  - FlexiBowl Power Supply Cable, 3m
  - FlexiBowl Power Supply Cable, 5m
  - FlexiBowl Power Supply Cable, 10m
* - **Ethernet**
  - Ethernet Cable 3m
  - Ethernet Cable 5m
  - Ethernet Cable 10m
:::

---

(cavo-io)=
## Cavo per opzione I/O

**Descrizione.** Cavo per il collegamento dei segnali dell'opzione **Digital I/O**, che consente il controllo del FlexiBowl® da PLC tramite ingressi e uscite digitali, senza comunicazione Ethernet. Segnali e codifica dei comandi: [Digital I/O](digIO).

:::{list-table}
:widths: 30 70
:stub-columns: 1

* - Prerequisiti
  - Opzione **Digital I/O**, acquistabile separatamente e non inclusa nella configurazione standard.
* - Connettore lato FlexiBowl®
  - Connettore I/O a 19 pin
    :::{dropdown} **Pinout connettore I/O (19 pin)**
    | Pin | Segnale | Utilizzo | 
    |---|---|---|
    | 1 | IN – Bit 1 | Codifica comando (Seq. Cmd) | 
    | 2 | IN – Bit 2 | Codifica comando (Seq. Cmd) | 
    | 3 | IN – Bit 3 | Codifica comando (Seq. Cmd) | 
    | 4 | IN – Bit 4 | Codifica comando (Seq. Cmd) | 
    | 5 | IN – Bit 5 | Codifica comando (Seq. Cmd) | 
    | 6 | IN – Latch | Esecuzione comando (fronte di salita) | 
    | 7–8 | NC | Non assegnati | 
    | 9 | OUT – Ready | Uscita di stato | 
    | 10 | OUT – Fault | Uscita di stato | 
    | 11 | OUT – Busy | Uscita di stato | 
    | 12 | OUT – Hopper_1_IsVibrating | Uscita di stato Hopper 1 | 
    | 13 | OUT – Hopper_2_IsVibrating | Uscita di stato Hopper 2 | 
    | 14 | OUT – Hopper_3_IsVibrating | Uscita di stato Hopper 3 | 
    | 15 | OUT – Hopper_4_IsVibrating | Uscita di stato Hopper 4 |
    | 16–19 | NC | Non assegnati | 
    :::
* - Lunghezze disponibili
  - · 3 m
    · 5 m
    · 10 m
:::


---

(cavo-rack)=
## Cavo per quadro elettronico remoto (rack)

**Descrizione.** Cavi di collegamento tra il **rack** esterno e il FlexiBowl®. Il rack comunica con la macchina tramite 4 cavi dedicati, ciascuno da collegare esclusivamente alla porta con l'etichetta corrispondente. Procedura di collegamento: {ref}`collegamento-rack`.

:::{list-table}
:widths: 30 70
:stub-columns: 1

* - Prerequisiti
  - FlexiBowl® con rack esterno (nessuna opzione da acquistare).
* - Taglie compatibili
  - · FlexiBowl® 200
    · FlexiBowl® 350
* - Lunghezze disponibili
  - · 3 m (incluso nella fornitura)
    · 5 m
    · 10 m
:::

:::{attention}
Collegare ogni cavo alla porta con l'**etichetta corrispondente** (es. MOTOR ↔ MOTOR, C-A SIGNAL ↔ C-A SIGNAL). Un collegamento incrociato può danneggiare il sistema.
:::

:::{list-table}
:header-rows: 1 

* - Cavo
  - Connettore
  - Funzione

* - **C-ETH FB**
  - M12 D-code
    :::{dropdown} **Pinout C-ETH FB (M12 D-code)**
    | Segnale | Funzione | Colore | Pin M12 (lato FlexiBowl®) | Pin RJ45 (lato cliente) |
    |---|---|---|---|---|
    | TD+ | Trasmissione dati (+) | Giallo | 1 | 1 |
    | TD− | Trasmissione dati (−) | Arancione | 3 | 2 |
    | RD+ | Ricezione dati (+) | Bianco | 2 | 3 |
    | RD− | Ricezione dati (−) | Blu | 4 | 6 |
    :::

  - Collegamento Ethernet tra rack e FlexiBowl®

* - **MOTOR**
  - 9 pin
    :::{dropdown} **Pinout MOTOR (9 pin)**

    | Pin | Utilizzo | 
    |---|---|
    | 1 | +STO1 – Safe Torque Off | 
    | 2 | +24 Vdc – Alimentazione ausiliaria | 
    | 3 | +STO2 – Safe Torque Off | 
    | 4 | −24 Vdc – Alimentazione ausiliaria | 
    | 5 | NC |
    | 6 | +48 Vdc – Motor Power | 
    | 7 | −STO1 – Safe Torque Off | 
    | 8 | −48 Vdc – Motor Power | 
    | 9 | −STO2 – Safe Torque Off | 
    :::
  - Alimentazione motore e segnali STO

* - **C-A SIGNAL**
  - 12 pin
    :::{dropdown} **Pinout C-A SIGNAL (12 pin)**

    | Pin | Utilizzo |
    |---|---|
    | 1 | Analog Output 1 | 
    | 2 | −24 Vdc | 
    | 3 | Analog Input 1 | 
    | 4 | +24 Vdc | 
    | 5–12 | NC | 
    :::
  - Segnali analogici

* - **C-B SIGNAL**
  - 19 pin
    :::{dropdown} **Pinout C-B SIGNAL (19 pin)**
    | Pin | Utilizzo | 
    |---|---|
    | 1 | +24 Vdc – Attivazione Led Verde Stato | 
    | 2 | −24 Vdc – Comune Led Stato | 
    | 3 | +24 Vdc – Attivazione Led Rosso Stato | 
    | 4 | +24 Vdc – Attivazione Led Stato Back light | 
    | 5 | −24 Vdc – Attivazione Led Stato Back light | 
    | 6 | +24 Vdc – Attivazione Back light |
    | 7 | −24 Vdc – Attivazione Back light | 
    | 8 | +24 Vdc – Attivazione Flip | 
    | 9 | −24 Vdc – Attivazione Flip | 
    | 10 | +24 Vdc – Attivazione Blow | 
    | 11 | −24 Vdc – Attivazione Blow | 
    | 12–19 | NC | 
    :::
  - Segnali digitali, incluse le attivazioni dei LED di stato
:::


---

(cavo-alim)=
## Cavo di alimentazione

**Descrizione.** Cavo di alimentazione di rete, da collegare al connettore **POWER SUPPLY** del pannello elettrico standard (FlexiBowl® 500 – 1200) o del rack (FlexiBowl® 200 / 350). Procedura di collegamento: {ref}`pannello-standard` · {ref}`rack-esterno`.

:::{list-table}
:widths: 30 70
:stub-columns: 1

* - Prerequisiti
  - Nessuno. Dispositivo spento, collegamento di terra obbligatorio. Il connettore ospita 2 fusibili di protezione.
* - Taglie compatibili
  - Tutte le taglie FlexiBowl®
* - Tensione ammessa
  - 120–230 Vac, 50/60 Hz ({ref}`dati_elettrici`)
* - Lunghezze disponibili
  - · 3 m
    · 5 m
    · 10 m
:::

| Etichetta (lato FlexiBowl®) | Tipo | Colore |
|---|---|---|
| L1 | Fase | Marrone |
| N1 | Neutro | Blu |
| PE1 | Terra | Giallo/Verde |

:::{attention}
Collegare l'alimentazione **per ultima**, con il FlexiBowl® spento. Il collegamento di terra è obbligatorio e deve essere verificato prima di ogni accensione.
:::


---

(cavo-eth)=
## Cavo Ethernet

**Descrizione.** Cavo per il collegamento Ethernet del FlexiBowl® al sistema (connettore **C-ETH** del pannello standard o **C-ETH IN** del rack). Consente la comunicazione con il FlexiBowl®, accessibile anche tramite web browser.

:::{list-table}
:widths: 30 70
:stub-columns: 1

* - Prerequisiti
  - Nessuno. Con FlexiBowl® alimentato il collegamento Ethernet è **obbligatorio**: se assente, la macchina entra in stato di **ERROR** (LED Ready/Fault rosso).
* - Taglie compatibili
  - Tutte le taglie FlexiBowl®
* - Connettori
  - Lato FlexiBowl®: M12 D-code
    :::{dropdown} **Pinout M12 D-Code e RJ45**
    | Segnale | Funzione | Colore | Pin M12 (lato FlexiBowl®) | Pin RJ45 (lato cliente) |
    |---|---|---|---|---|
    | TD+ | Trasmissione dati (+) | Giallo | 1 | 1 |
    | TD− | Trasmissione dati (−) | Arancione | 3 | 2 |
    | RD+ | Ricezione dati (+) | Bianco | 2 | 3 |
    | RD− | Ricezione dati (−) | Blu | 4 | 6 |

    I pin RJ45 4, 5, 7 e 8 non sono assegnati.
    :::
* - Lunghezze disponibili
  - · 3 m
    · 5 m
    · 10 m
:::
