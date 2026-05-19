# Monitoraggio Applicazione

Una volta completata la configurazione tramite il Wizard e salvata la sequenza, il sistema è pronto per l'utilizzo operativo. Le pagine di monitoraggio consentono di verificare il corretto funzionamento del FlexiBowl® in tempo reale durante il ciclo di produzione.

## Avvio della Sequenza

::::{list-table}
:widths: 10 90
:header-rows: 1

* - Step
  - Operazione

* - 1
  - Aprire la pagina **Sequence** dal menu laterale.

* - 2
  - Selezionare la sequenza configurata dal menu a tendina **"Select the sequence"**.

* - 3
  - Verificare che i parametri visualizzati siano corretti.

* - 4
  - Premere **RUN** per avviare la sequenza in modalità operativa continua.

::::

:::{important}
Prima di avviare la sequenza, verificare che il motore sia abilitato (pulsante **ENABLE MOTOR** attivo) e che lo stato del sistema sia **READY**.
:::

## Monitoraggio in Esercizio

Durante il funzionamento, utilizzare le seguenti pagine per tenere sotto controllo lo stato del sistema:

### Pagina Monitor

La pagina **Monitor** consente di verificare lo stato del driver motore e di consultare il log degli eventi in tempo reale.

I principali indicatori da tenere sotto controllo durante l'esercizio sono:

- **Operation Enabled** — deve essere verde: il motore è in controllo attivo.
- **Target Reached** — si illumina al termine di ogni movimento.
- **Communication State** — deve indicare **RUNNING**.
- **Error Code** — deve rimanere a **0**. In caso di valore diverso, consultare il log degli eventi per identificare la causa.

:::{tip}
In caso di allarme nel log, eseguire sempre l'**ACK** solo dopo aver verificato e risolto la condizione che ha generato il messaggio.
:::

### Pagina Graphs

La pagina **Graphs** fornisce una dashboard in tempo reale delle grandezze elettriche e termiche del driver.

I principali valori da monitorare sono:

- **Drive Temperature** e **Dsp Temperature** — valori costantemente superiori a 70 °C indicano un possibile problema di raffreddamento.
- **DC Voltage** — deve mantenersi nel range nominale (48 V ± 10%).
- **ECO LOAD %** — indica il carico medio del motore; valori elevati e persistenti possono segnalare un sovraccarico meccanico.
- **Current Motor %** e **Torque Motor %** — picchi eccessivi e ricorrenti suggeriscono di rivedere le rampe di accelerazione e decelerazione.

:::{warning}
In caso di anomalie rilevate nelle pagine Monitor o Graphs, fermare la sequenza tramite il pulsante **RUN** (che diventa **STOP** durante l'esecuzione) e consultare la sezione di diagnostica del manuale prima di riprendere il ciclo produttivo.
:::
