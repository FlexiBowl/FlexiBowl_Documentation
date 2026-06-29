# **Main Command**

## Panoramica

La pagina **Main Command** è la sezione operativa principale dell'interfaccia software FlexiBowl®. Consente all'operatore di configurare e testare i parametri di movimento e delle opzioni accessorie del sistema.

La pagina è suddivisa in **tre sottopagine**, selezionabili tramite il menu a tendina centrale posizionato sotto la barra di navigazione, etichettato **"Chose Visualization Page"**:

| Sottopagina | Descrizione sintetica |
|---|---|
| **OPTION** | Parametri per flip, blow e retroilluminazione |
| **MOVE** | Parametri per il movimento rotatorio del FlexiBowl® |
| **SHAKE** | Parametri per il movimento oscillatorio del FlexiBowl® |

---

## Sottopagina: OPTION

La sottopagina **OPTION** raccoglie i parametri relativi alle funzioni accessorie del FlexiBowl®: il sistema di ribaltamento dei componenti (flip), il sistema di soffiaggio (blow) e la retroilluminazione (backlight).
![pagina option](../../../../_shared/media/images/main_command_option.png)

| Parametro | Unità | Descrizione |
|---|---|---|
| **Flip Pressure** | Bar  | Pressione dell'aria utilizzata per l'attuazione del flip. Regolabile tramite slider |
| **Flip Count** | N°  | Numero di flip eseguiti in sequenza durante un ciclo |
| **Flip Delay** | ms  | Intervallo di tempo tra un flip e il successivo |
| **Blow Pressure** | Bar  | Pressione dell'aria utilizzata per il soffiaggio dei componenti sul FlexiBowl® |
| **Blow Time** | ms  | Durata dell'impulso di soffiaggio |

Ogni parametro è regolabile tramite uno **slider orizzontale**; il valore corrente è visualizzato nel riquadro numerico a destra dello slider.

### Controlli retroilluminazione

| Controllo | Descrizione |
|---|---|
| **Backlight_1** | Toggle on/off per la retroilluminazione 1  |
| **Backlight_2** | Toggle on/off per la retroilluminazione 2  |

I toggle mostrano rosso quando la retroilluminazione è **attiva**.

### Pulsanti di test

In fondo alla pagina sono presenti tre pulsanti per testare le funzioni in tempo reale:

| Pulsante | Funzione |
|---|---|
| **TEST FLIP** | Esegue un flip con i parametri correntemente impostati |
| **TEST BLOWe** | Attiva il soffiaggio esterno (blow esterno) con i parametri impostati |
| **TEST BLOWc** | Attiva il soffiaggio centrale (blow centrale) con i parametri impostati |

:::{attention}  
 Prima di eseguire i test, assicurarsi che il motore sia abilitato (pulsante **ENABLE MOTOR** attivo) e che lo stato del sistema sia **READY**.
:::

---

## Sottopagina: MOVE

La sottopagina **MOVE** consente di configurare i parametri del movimento rotatorio del FlexiBowl® e di testarlo direttamente dall'interfaccia.
![pagina move](../../../../_shared/media/images/main_command_move.png)

| Parametro | Unità | Valore predefinito | Descrizione |
|---|---|---|---|
| **Acceleration** | % | 50 | Rampa di accelerazione del motore all'avvio del movimento. Valori più alti producono una partenza più brusca |
| **Deceleration** | % | 50 | Rampa di decelerazione del motore in fase di arresto. Valori più alti producono un arresto più brusco |
| **Speed** | % | 50 | Velocità di rotazione del FlexiBowl® durante il movimento |
| **Angle** | Degree | 45 | Angolo di rotazione percorso dal FlexiBowl® durante ogni singolo movimento |

Ogni parametro è regolabile tramite uno **slider orizzontale**; il valore corrente è visualizzato nel riquadro numerico a destra dello slider.

### Pulsante di test

| Pulsante | Campo affiancato | Funzione |
|---|---|---|
| **TEST MOVE** | Tempo esecuzione (ms) | Esegue un movimento di rotazione con i parametri correntemente impostati. Il campo a destra mostra la durata effettiva dell'ultimo movimento eseguito in millisecondi |

:::{note}  
 Il campo **ms** visualizza il tempo reale impiegato dal bowl per completare il movimento impostato. Questo valore è utile per sincronizzare il FlexiBowl® con il sistema di visione artificiale.
:::

:::{attention}   
Prima di eseguire il test, assicurarsi che il motore sia abilitato (pulsante **ENABLE MOTOR** attivo) e che lo stato del sistema sia **READY**.
:::

---

## Sottopagina: SHAKE

La sottopagina **SHAKE** consente di configurare i parametri del movimento oscillatorio del FlexiBowl® (shake), utilizzato per ridistribuire i componenti sul piatto, e di testarlo direttamente dall'interfaccia.
![pagina shake](../../../../_shared/media/images/main_command_shake.png)

| Parametro | Unità | Valore predefinito | Descrizione |
|---|---|---|---|
| **Acceleration** | % | 50 | Rampa di accelerazione del motore durante la fase di shake |
| **Deceleration** | % | 50 | Rampa di decelerazione del motore durante la fase di shake |
| **Speed** | % | 50 | Velocità di rotazione durante il movimento di shake |
| **Ccw Angle** | Degree | -45 | Angolo di rotazione in senso **antiorario** (Counter-ClockWise) durante ogni oscillazione |
| **Cw Angle** | Degree | 45 | Angolo di rotazione in senso **orario** (ClockWise) durante ogni oscillazione |
| **Count** | N° | 2 | Numero di oscillazioni complete eseguite durante un ciclo di shake |

Ogni parametro è regolabile tramite uno **slider orizzontale**; il valore corrente è visualizzato nel riquadro numerico a destra dello slider.

:::{note}  
 Il movimento di **shake** consiste in una serie di rotazioni alternate in senso orario e antiorario, definite rispettivamente da **Cw Angle** e **Ccw Angle**. Il numero di oscillazioni complete è controllato dal parametro **Count**.
:::

### Pulsante di test

| Pulsante | Campo affiancato | Funzione |
|---|---|---|
| **TEST SHAKE** | Tempo esecuzione (ms) | Esegue un ciclo di shake con i parametri correntemente impostati. Il campo a destra mostra la durata effettiva dell'ultimo shake eseguito in millisecondi |

:::{attention}  
 Prima di eseguire il test, assicurarsi che il motore sia abilitato (pulsante **ENABLE MOTOR** attivo) e che lo stato del sistema sia **READY**.
:::