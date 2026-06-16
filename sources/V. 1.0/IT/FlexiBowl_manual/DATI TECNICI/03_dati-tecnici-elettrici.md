# **[ELE]** Dati Tecnici Elettrici

## Dati di Alimentazione

Di seguito sono riportati i parametri elettrici nominali di alimentazione applicabili a tutte le varianti della famiglia FlexiBowl® FB 3.0.
### Parametri Generali

- **Tensione nominale**: 230 / 120 Vac

- **Frequenza nominale**: 50 Hz / 60 Hz

### Corrente Nominale Assorbita

La corrente assorbita varia in funzione del modello installato:
:::{list-table}
:widths: 50 50
:header-rows: 1
* - Dispositivo
  - Corrente nominale
* - FlexiBowl® 200
  - 1,50 A
* - FlexiBowl® 350
  - 1,50 A
* - FlexiBowl® 500
  - 2,00 A
* - FlexiBowl® 650
  - 2,00 A
* - FlexiBowl® 800
  - 2,50 A
* - FlexiBowl® 1200
  - 4,00 A
:::

### Potenza Nominale Installata

La potenza nominale varia in funzione del modello installato. Il dato per FB 1200 è in fase di aggiornamento.
:::{list-table}
:widths: 50 50
:header-rows: 1
* - Dispositivo
  - Potenza nominale
* - FlexiBowl® 200
  - 350 W
* - FlexiBowl® 350
  - 350 W
* - FlexiBowl® 500
  - 500 W
* - FlexiBowl® 650
  - 500 W
* - FlexiBowl® 800
  - 600 W
* - FlexiBowl® 1200
  - 950 W
:::

## Protezioni Elettriche

### Fusibili

Il circuito di protezione è realizzato con fusibili ad azione rapida. I valori nominali per modello sono i seguenti:

:::{list-table}
:widths: 50 50
:header-rows: 1
* - Dispositivo
  - Fusibile
* - FlexiBowl® 200
  - 3 A
* - FlexiBowl® 350
  - 3 A
* - FlexiBowl® 500
  - 3 A
* - FlexiBowl® 650
  - 3 A
* - FlexiBowl® 800
  - 4 A
* - FlexiBowl® 1200
  - 5 A
:::

### Classe di Protezione Elettrica

- **Classe di protezione**: Classe I

La protezione è realizzata mediante isolamento di base e collegamento di tutte le masse metalliche al conduttore di protezione (PE – terra di impianto).

### Messa a Terra

Il dispositivo deve essere obbligatoriamente collegato al circuito di terra dell'impianto prima di qualsiasi altra operazione.
:::{attention}
Prima di accendere il FlexiBowl, verificare che il dispositivo sia correttamente collegato a terra con l'impianto generale.
:::

## Interfaccia Utente

### Collegamento Elettrico

Per collegare elettricamente il FlexiBowl procedere come segue:

- **Connessione di alimentazione**: collegare il FlexiBowl ad un'alimentazione 230 Vac utilizzando il connettore fornito in dotazione, identificato con la sigla **POWER SUPPLY**.

- **Accensione/Spegnimento**: utilizzare il pulsante di alimentazione per accendere o spegnere il dispositivo.

:::{figure} ../../../../_shared/media/images/stpanel1.PNG
:width: 80%
:center:
:::

:::{attention}
Assicurarsi che il dispositivo sia collegato a terra prima di procedere all'accensione.
:::

### Fusibili – Alloggiamento

Il connettore elettrico è provvisto di un supporto per l'alloggiamento di n. 2 fusibili, aventi la funzione di proteggere il dispositivo da eventuali anomalie elettriche.

## Connettori e Interfacce

### Connettore STO – Safety Torque Off

Per attivare il motore è necessario collegare correttamente il sistema STO (Safety Torque Off) tramite il connettore identificato con la sigla **STO**.

:::{figure} ../../../../_shared/media/images/stpanel7.PNG
:width: 80%
:center:
:::

Di seguito è riportato il pinout del connettore a 10 pin:

:::{list-table}
:widths: 20 80
:header-rows: 1
* - Pin
  - Descrizione
* - 1
  - +24 Vdc
* - 2
  - −24 Vdc
* - 3
  - +STO1
* - 4
  - −STO1
* - 5
  - +STO2
* - 6
  - −STO2
* - 7
  - NC
* - 8
  - NC
* - 9
  - NC
* - 10
  - NC
:::

- **+STO1 e +STO2**: collegare al circuito di sicurezza. Questi ingressi devono ricevere +24 Vdc.

- **−STO1 e −STO2**: collegare a riferimento −24 Vdc.

### Connessione Ethernet

Per la comunicazione con il FlexiBowl è disponibile la porta Ethernet identificata con la sigla **C-ETH**, accessibile anche tramite web browser.

- **Tipo connettore**: M12, codifica D-Code

:::{figure} ../../../../_shared/media/images/stpanel6.PNG
:width: 80%
:center:
:::

### Collegamento Tramogge

Il FlexiBowl è dotato di una connessione verso uno o più controller di tramogge vibranti di produzione ARS, tramite il connettore M12 A-code identificato con la sigla **HOPPER**.

:::{figure} ../../../../_shared/media/images/stpanel5.PNG
:width: 80%
:center:
:::

## LED di Stato

Sul pannello frontale del FlexiBowl sono presenti due LED di stato:

### LED – Light ON

- **Colore**: Verde (unico stato)

Indica se il backlight a bordo del FlexiBowl è nello stato ON (acceso) o OFF (spento). Il backlight viene utilizzato dal sistema di visione per illuminare i componenti e renderli riconoscibili. L'attivazione del backlight è accessibile tramite il software di visione oppure mediante comandi provenienti da un sistema esterno in comunicazione Ethernet.

### LED – Ready / Fault

Questo LED può avere due stati:

:::{list-table}
:widths: 30 70
:header-rows: 1
* - Colore LED
  - Significato
* - Verde
  - Sistema operativo e privo di anomalie. Collegamento Ethernet corretto.
* - Rosso
  - Anomalia interna o anomalia nel collegamento Ethernet. Fare riferimento alla tabella delle anomalie.
:::

## Pannellino FlexiTrack

Il pannellino in dotazione con l'opzione FlexiTrack prevede i seguenti connettori:

:::::{grid} 1
:gutter: 2

::::{grid-item} Sofffi radiali

:::{figure} ../../../../_shared/media/images/encpanel6.PNG
:width: 100%
:::

::::

::::{grid-item} Soffio centrale

:::{figure} ../../../../_shared/media/images/encpanel8.PNG
:width: 100%
:::

::::

- **Connettore I/O**: scambio segnali digitali, inclusa la funzione Latch.

- **Passacavo encoder**: dedicato all'encoder interno al FlexiBowl.

### Connettore I/O – 19 pin

Di seguito è riportata la mappa segnali del connettore a 19 pin:

:::{list-table}
:widths: 25 75
:header-rows: 1
* - Pin
  - Segnale
* - 1
  - IN – Bit 1 – Seq. Cmd
* - 2
  - IN – Bit 2 – Seq. Cmd
* - 3
  - IN – Bit 3 – Seq. Cmd
* - 4
  - IN – Bit 4 – Seq. Cmd
* - 5
  - IN – Bit 5 – Seq. Cmd
* - 6
  - IN – Latch
* - 7
  - NC
* - 8
  - NC
* - 9
  - OUT – Ready
* - 10
  - OUT – Fault
* - 11
  - OUT – Busy
* - 12
  - OUT – Hopper_1_IsVibrating
* - 13
  - OUT – Hopper_2_IsVibrating
* - 14
  - OUT – Hopper_3_IsVibrating
* - 15
  - OUT – Hopper_4_IsVibrating
* - 16
  - NC
* - 17
  - NC
* - 18
  - NC
* - 19
  - NC
:::

## Pannello Rack (FB 200 / FB 350)

I modelli FlexiBowl FB 200 e FB 350 sono dotati di un Rack contenente tutti i dispositivi elettronici necessari al funzionamento. Il pannello di interfaccia prevede connettori dedicati allo scambio dati tra la stazione remota e il FlexiBowl.

Oltre ai connettori standard presenti nei pannelli per le taglie superiori, sono disponibili i seguenti connettori dedicati:
- **C-ETH FB**: collegamento Ethernet con FlexiBowl.
- **C-A Signal**: segnali analogici di comando.
- **C-B Signal**: segnali digitali di comando.
- **Motor**: alimentazione ausiliaria, comando motore e segnali STO.

### Connettore C-A Signal

:::{figure} ../../../../_shared/media/images/rack4.PNG
:width: 80%
:center:
:::

Connettore a 12 pin per segnali analogici:

:::{list-table}
:widths: 20 80
:header-rows: 1
* - Pin
  - Descrizione
* - 1
  - Analog Output 1
* - 2
  - −24 Vdc
* - 3
  - Analog Input 1
* - 4
  - +24 Vdc
* - 5–12
  - NC
:::

### Connettore C-B Signal

:::{figure} ../../../../_shared/media/images/rack5.PNG
:width: 80%
:center:
:::

Connettore a 19 pin per segnali digitali:

:::{list-table}
:widths: 20 80
:header-rows: 1
* - Pin
  - Descrizione
* - 1
  - +24 Vdc – Attivazione Led Verde Stato
* - 2
  - −24 Vdc – Comune Led Stato
* - 3
  - +24 Vdc – Attivazione Led Rosso Stato
* - 4
  - +24 Vdc – Attivazione Led Stato Back light
* - 5
  - −24 Vdc – Attivazione Led Stato Back light
* - 6
  - +24 Vdc – Attivazione Back light
* - 7
  - −24 Vdc – Attivazione Back light
* - 8
  - +24 Vdc – Attivazione Flip
* - 9
  - −24 Vdc – Attivazione Flip
* - 10
  - +24 Vdc – Attivazione Blow
* - 11
  - −24 Vdc – Attivazione Blow
* - 12–19
  - NC
:::
### Connettore Motor

:::{figure} ../../../../_shared/media/images/rack3.PNG
:width: 80%
:center:
:::

Connettore a 9 pin per alimentazione motore e segnali STO:

:::{list-table}
:widths: 20 80
:header-rows: 1
* - Pin
  - Descrizione
* - 1
  - +STO1 – Safety Torque Off
* - 2
  - +24 Vdc – Alimentazione ausiliaria
* - 3
  - +STO2 – Safety Torque Off
* - 4
  - −24 Vdc – Alimentazione ausiliaria
* - 5
  - NC
* - 6
  - +48 Vdc – Motor Power
* - 7
  - −STO1 – Safety Torque Off
* - 8
  - −48 Vdc – Motor Power
* - 9
  - −STO2 – Safety Torque Off
:::

### Connessione Ethernet FlexiBowl

:::{figure} ../../../../_shared/media/images/rack8.PNG
:width: 80%
:center:
:::

Connettore M12 D-Code per il collegamento del Rack con il FlexiBowl.

## Note e Avvertenze Generali

:::{attention}
Tutte le operazioni di connessione devono essere eseguite a dispositivo spento e scollegato dall'alimentazione.
:::

:::{attention}
Il collegamento di terra è obbligatorio e deve essere verificato prima di ogni accensione.
:::

:::{attention}
In caso di anomalia indicata dal LED rosso (Ready/Fault), fare riferimento alla tabella delle anomalie specifica del modello.
:::

:::{attention}
Per ulteriori informazioni tecniche o assistenza, contattare ARS s.r.l. – FlexiBowl® Division.
:::