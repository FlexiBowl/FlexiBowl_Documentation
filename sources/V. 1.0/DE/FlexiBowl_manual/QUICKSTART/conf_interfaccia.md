# **Konfiguration der Schnittstelle**


:::{note}
Se il sistema in uso è **FlexiVision One**, la configurazione viene gestita interamente dalla sua interfaccia dedicata. Non è necessario utilizzare l'interfaccia software FlexiBowl® descritta in questa sezione. Fare riferimento al {ref}`Manuale FlexiVision One <flexivision_one>`.
:::

## Primo avvio

Al primo avvio del sistema, seguire la procedura guidata di seguito per configurare la comunicazione e preparare il FlexiBowl® all'uso.

::::{list-table}
:widths: 10 90
:header-rows: 1

* - Step
  - Operazione

* - 1
  - Inserire l'**indirizzo IP** del FlexiBowl® nella barra di ricerca del browser per accedere all'interfaccia software.

* - 2
  - Si apre la **Home page**. Selezionare la **lingua** desiderata dal menu a tendina in alto a destra.

* - 3
  - Aprire la pagina **Setup** dal menu laterale.

* - 4
  - Cliccare su **Get IP** per leggere i parametri di rete correnti del dispositivo.

* - 5
  - Inserire il **nuovo indirizzo IP** che si intende assegnare al FlexiBowl® nei campi dedicati, quindi cliccare su **Set IP**.

* - 6
  - Selezionare il **tipo di comunicazione** desiderato dal menu a tendina. L'opzione predefinita è **TCP Server**.

    :::{note}
    La modalità **Digital I/O** non è inclusa nella configurazione standard, ma è disponibile come opzione acquistabile separatamente.
    :::

* - 7
  - Cliccare su **Apply** per confermare le impostazioni di comunicazione.

* - 8
  - Cliccare su **Reboot** per riavviare il software e rendere effettive le modifiche.

::::

:::{important}
Dopo il reboot, riconnettersi al FlexiBowl® utilizzando il nuovo indirizzo IP impostato al punto 5.
:::

## Abilitazione del Backlight (se necessario)

Se è richiesta la calibrazione del sistema di visione, abilitare la retroilluminazione prima di procedere:

::::{list-table}
:widths: 10 90
:header-rows: 0

* - 1
  - Aprire la pagina **Main Command** dal menu laterale.

* - 2
  - Selezionare **OPTION** dal menu a tendina **"Chose Visualization Page"**.

* - 3
  - Attivare il toggle **Backlight 1** e/o **Backlight 2** in base alle necessità.

::::