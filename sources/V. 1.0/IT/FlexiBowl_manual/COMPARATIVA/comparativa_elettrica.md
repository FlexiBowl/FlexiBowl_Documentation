# **[ELE]** Comparativa Elettrica

Le seguenti informazioni sono tutte da verificare:
## Componenti del sistema elettrico

| Componente              | FlexiBowl® 2.0 | FlexiBowl® 3.0 |
|-------------------------|----------------|----------------|
| Filtro EMC              | ✓              |                |
| Scheda di Interfaccia   | ✓ (progettata da ARS) |         |
| Alimentatore 24V DC     | ✓              |                |
| Driver                  | ✓ (MOONS')     |                |
| Motore brushless        | ✓              |                |
| Fusibili                | ✓ (6 fusibili) |                |
| Relè                    | ✓ (6 relè: K1–K6) |             |
| Varistori               | ✓ (2×, su linea 110/220V) |     |

---

## Alimentazione

| Parametro                        | FlexiBowl® 2.0      | FlexiBowl® 3.0 |
|----------------------------------|---------------------|----------------|
| Tensione di rete                 | 110 / 220 V AC      |                |
| Tensione di lavoro               | 24V DC              |                |
| Potenza massima alimentatore     | 108 W               |                |
| Carichi alimentati               | LED, Backlight, Elettrovalvole, Pannello Frontale | |

---

## Fusibili

| Riferimento | Funzione                                    | Valore (FB 2.0) | Valore (FB 3.0) |
|-------------|---------------------------------------------|-----------------|-----------------|
| F1          | Protezione alimentazione driver             | 3 A             |                 |
| F2          | Protezione alimentatore 24V                 | 2 A             |                 |
| F3          | Protezione 24VDC (scheda di interfaccia)    | 2.5 A           |                 |
| F4          | Illuminatore in modalità strobe             | 2 A             |                 |
| F5          | —                                           | —               |                 |
| F6          | —                                           | —               |                 |

> **Nota FB 2.0:** sono presenti 6 fusibili in totale; F5 e F6 non sono esplicitamente nominati nel materiale di training disponibile.

---

## Scheda di Interfaccia — Connettori lato sinistro

| Connettore        | Funzione (FB 2.0)                              | FB 3.0 |
|-------------------|------------------------------------------------|--------|
| Empty – Optional  | Svuotamento opzionale                          |        |
| Led Ready – Fault | Segnalazione stato pronto / errore             |        |
| Empty Open        | Segnale apertura svuotamento                   |        |
| Spare             | Riservato                                      |        |
| Flip              | Attivazione flip                               |        |
| Blow              | Attivazione soffio                             |        |
| Backlight         | Controllo retroilluminazione                   |        |
| Led – Light       | Controllo luce LED                             |        |
| +24V – IN         | Ingresso alimentazione 24V                     |        |
| Pressure Switch   | Sensore pressione aria                         |        |
| Strobe IN         | Ingresso segnale strobe                        |        |
| Strobe OUT        | Uscita segnale strobe                          |        |

---

## Scheda di Interfaccia — Relè

| Relè | Funzione (FB 2.0)        | Connettore associato (FB 2.0)   | FB 3.0 |
|------|--------------------------|---------------------------------|--------|
| K1   | Backlight                | INPUT / OUTPUT 1 – Driver       |        |
| K2   | QuickEmpty               | INPUT – Pannello Frontale       |        |
| K3   | Blow                     | INPUT / OUTPUT 1 – Driver       |        |
| K4   | Flip                     | INPUT / OUTPUT 2 – Driver       |        |
| K5   | Led Ready / Fault        | OUTPUT – Pannello Frontale      |        |
| K6   | Busy                     | OUTPUT – Pannello Frontale      |        |

---

## Filtro EMC

| Parametro               | FlexiBowl® 2.0                                                       | FlexiBowl® 3.0 |
|-------------------------|----------------------------------------------------------------------|----------------|
| Tipo                    | Filtro passivo (condensatori, bobine, resistenze) — es. Corcom 6ET1 |                |
| Tensione nominale       | 6A / 120–250V, 50–60 Hz                                              |                |
| Funzione                | Blocca le interferenze elettromagnetiche sulla linea di alimentazione |               |

---

## Driver

| Parametro               | FlexiBowl® 2.0                           | FlexiBowl® 3.0 |
|-------------------------|------------------------------------------|----------------|
| Marca / modello         | MOONS'                                   |                |
| Funzione                | Pilota il motore; ponte I/O con la scheda di interfaccia | |
| Connessione motore      | Via connettore MOTOR (linea + encoder)   |                |
| Connessione I/O         | IN/OUT 1 (J15) e IN/OUT 2 (J14)          |                |
| Connessione rete        | Porta Ethernet + Rotary Switch IP        |                |
| Indirizzi IP configurabili | Da 10.10.10.10 a 192.168.0.140, oppure DHCP (pos. F) | |

---

## Motore

| Parametro                  | FlexiBowl® 2.0                   | FlexiBowl® 3.0 |
|----------------------------|----------------------------------|----------------|
| Tipo                       | Brushless ad albero unico        |                |
| Corrente nominale massima  | 2,4 A                            |                |
| Peso motore                | ~9 kg                            |                |
| Connessione al driver      | Alimentazione motore + Encoder   |                |
