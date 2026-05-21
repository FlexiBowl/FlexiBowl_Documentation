# **Manuale FlexiBowl**

## **Benvenuto nel manuale FlexiBowl®!**  
Siamo entusiasti di darvi il benvenuto alla vostra nuova guida di FlexiBowl®!
Questo manuale è stato creato appositamente per essere il vostro punto di riferimento chiaro e affidabile. Ci auguriamo che, consultandolo, possiate godere appieno di tutti i benefici del nostro sistema.
Il vostro parere è fondamentale per noi: non esitate a fornirci il vostro feedback [contattandoci](https://www.flexibowl.it/contatti)! 

*- Il Team di Ars Automation*    
<a href="https://www.arsautomation.com" target="_blank">
  <img src="../../_shared/static/logo_fv.png" alt="Ars logo" class="only-light img-logo">
  <img src="../../_shared/static/logo_fv_black.png" alt="Ars logo" class="only-dark img-logo">
</a>
  
## **Cosa è FlexiBowl?**  
Il FlexiBowl® è un sistema di alminentazione flessibile a disco rotante vibrante per il posizionamento e orientamento casuale dei componenti ai fini del prelievo robotico.

## **Panoramica del sistema** 
L'area di lavoro del FlexiBowl® è virtualmente divisa in quattro parti, ognuna dedicata a una fase del ciclo di lavoro:

:::{list-table}
:widths: 20 50
:header-rows: 1

* - Fase
  - Descrizione

* - **Rilascio**
  - Una tramoggia scarica i componenti sull'area di lavoro del FlexiBowl®.

* - **Separazione**
  - Un'azione combinata del {ref}`gruppo flip <panoramica>` e del movimento della superficie o disco rigido separa i componenti e li ribalta per averne sempre almeno uno nella giusta posizione per la presa.

* - **Presa**
  - Il sistema di visione riconosce i pezi prendibile e ne invia le coordinate al robot, che procede con le operazioni di pick and place.

* - **Ricircolo**
  - I componenti non presi ricominciano il loro percorso nel FlexiBowl® finché non vengono presi dal robot.

:::

:::{figure} ../../_shared/media/images/Funz-standard.PNG
:align: center
:width: 50%

Schema esemplificativo del sistema FlexiBowl® in funzionamento standard.
:::

:::{note}
Il ciclo {ref}`Flexitracking <tracking>` è sostanzialmente uguale a quello tradizionale, con la differenza che tutte le fasi avvengono contemporaneamente e in continuazione.
:::


## **Come leggere il manuale**  
Questo manuale è stato concepito per supportare sia la fase di progettazione e integrazione di sistema, sia la fase di installazione e messa in servizio in campo. 
Per questo motivo, è diviso in delle macro-sezioni con destinatari e finalità distinte.
  
## **Qual è la sezione che stai cercando?**  
```{list-table}
:widths: 40 60
:header-rows: 1

* - Se devi...
  - L'informazione si trova in...

* - Verificare dimensioni, pesi, requisiti elettrici e protocolli di comunicazione
  - [**RIFERIMENTO TECNICO E SPECIFICHE**](specifiche_tecniche)

* - Installare i componenti, cablare il sistema, configurare la rete o calibrare camera/robot
  - [**INSTALLAZIONE DEL SISTEMA**](Installazione_Meccanica) e [**QUICKSTART**](quickstart)

* - Programmare un nuovo modello pezzo o configurare il sistema di alimentazione
  - [**QUICKSTART**](quickstart)

* - Risolvere problemi o richiedere assistenza
  - [**TROUBLESHOOTING**](troubleshooting) e [**SUPPORT**](support)
```

## **Convenzioni e simboli utilizzati**

In tutto il manuale vengono utilizzati banner informativi per evidenziare contenuti importanti:

```{list-table}
:widths: 20 80
:header-rows: 1

* - Tipo
  - Significato

* - ```{warning}
    Avvertenza
    ```
  - Indica una situazione potenzialmente pericolosa o una procedura critica che, se non eseguita correttamente, potrebbe provocare danni all'apparecchiatura o malfunzionamenti gravi del sistema.

* - ```{important}
    Importante
    ```
  - Evidenzia informazioni fondamentali che non devono essere ignorate per garantire il corretto funzionamento del sistema o la sicurezza dell'operazione.

* - ```{note}
    Nota informativa
    ```
  - Fornisce informazioni essenziali per il corretto svolgimento della procedura, chiarimenti tecnici o rimandi a capitoli correlati.

* - ```{tip}
    Suggerimento
    ```
  - Suggerisce una pratica ottimale, un'alternativa o un consiglio che può semplificare l'installazione o migliorare le prestazioni del sistema.

* - ```{error}
    Errore
    ```
  - Indica un errore critico o una condizione di guasto che richiede intervento immediato. Segnala situazioni che compromettono il funzionamento del sistema e richiedono azione correttiva.
```







:::{toctree}
:hidden:
:caption: PRIMA DI INIZIARE 
FlexiBowl_manual/PRIMA DI INIZIARE/01_informazioni_preliminari.md
FlexiBowl_manual/PRIMA DI INIZIARE/02_informazioni_sicurezza.md
FlexiBowl_manual/PRIMA DI INIZIARE/03_trasporto.md
FlexiBowl_manual/PRIMA DI INIZIARE/04_cond-util.md
FlexiBowl_manual/PRIMA DI INIZIARE/05_glossario.md
FlexiBowl_manual/PRIMA DI INIZIARE/06_support.md
FlexiBowl_manual/PRIMA DI INIZIARE/07_garanzia.md
:::
  
:::{toctree}
:hidden:
:caption: DATI TECNICI
FlexiBowl_manual/DATI TECNICI/01_panoramica.md
FlexiBowl_manual/DATI TECNICI/02_dati-tecnici-meccanici.md
FlexiBowl_manual/DATI TECNICI/03_dati-tecnici-elettrici.md
FlexiBowl_manual/DATI TECNICI/04_dati-tecnici-pneumatici.md
FlexiBowl_manual/DATI TECNICI/05_dati-tecnici-applicativi.md
:::

:::{toctree}
:hidden:
:caption: INSTALLAZIONE
FlexiBowl_manual/INSTALLAZIONE/01_interfaccia-meccanica.md
FlexiBowl_manual/INSTALLAZIONE/02_interfaccia-elettrica.md
FlexiBowl_manual/INSTALLAZIONE/03_interfaccia-pneumatica.md
FlexiBowl_manual/INSTALLAZIONE/04_interfaccia-software.md
:::

:::{toctree}
:hidden:
:caption: PANORAMICA SOFTWARE
FlexiBowl_manual/INTERFACCIA SOFTWARE/04_home.md
FlexiBowl_manual/INTERFACCIA SOFTWARE/04b_maincommand.md
FlexiBowl_manual/INTERFACCIA SOFTWARE/04c_sequence.md
FlexiBowl_manual/INTERFACCIA SOFTWARE/04d_monitor.md
FlexiBowl_manual/INTERFACCIA SOFTWARE/04e_jogmotor.md
FlexiBowl_manual/INTERFACCIA SOFTWARE/04f_wizard.md
FlexiBowl_manual/INTERFACCIA SOFTWARE/04g_manual.md
FlexiBowl_manual/INTERFACCIA SOFTWARE/04h_graphs.md
FlexiBowl_manual/INTERFACCIA SOFTWARE/04i_filetransfer.md
FlexiBowl_manual/INTERFACCIA SOFTWARE/04l_setup.md
FlexiBowl_manual/INTERFACCIA SOFTWARE/04m_hopper.md
:::

:::{toctree}  
:hidden:
:caption: QUICKSTART
FlexiBowl_manual/QUICKSTART/panoramica.md
FlexiBowl_manual/QUICKSTART/installazione_meccanica.md
FlexiBowl_manual/QUICKSTART/cablaggio_FB.md
FlexiBowl_manual/QUICKSTART/conf_interfaccia.md
FlexiBowl_manual/QUICKSTART/FB_wizard.md
FlexiBowl_manual/QUICKSTART/monitoraggio.md
:::

:::{toctree}  
:hidden:
:caption: PLUG-IN 
FlexiBowl_manual/PLUG-IN/01_PlugIn.md
:::

:::{toctree}
:hidden:
:caption: LAYOUT BEST PRACTICE
FlexiBowl_manual/LAYOUT BEST PRACTICE/01_layoutbp.md
:::

:::{toctree}
:hidden:
:caption: ACCESSORI
FlexiBowl_manual/ACCESSORI/00_ACCESSORI.md
FlexiBowl_manual/ACCESSORI/01_SUPERFICI.md
FlexiBowl_manual/ACCESSORI/02_DISCHI_RIGIDI.md
FlexiBowl_manual/ACCESSORI/03_BACKLIGHT.md
FlexiBowl_manual/ACCESSORI/04_TOPLIGHT.md
FlexiBowl_manual/ACCESSORI/05_DEVIATORE.md
FlexiBowl_manual/ACCESSORI/06_SOFFI.md
FlexiBowl_manual/ACCESSORI/07_BRUSH_DIVERTER.md
FlexiBowl_manual/ACCESSORI/08_WEDGE.md
FlexiBowl_manual/ACCESSORI/09_SVUOTAMENTO.md
FlexiBowl_manual/ACCESSORI/10_TRACKING.md
FlexiBowl_manual/ACCESSORI/11_RINGLIGHT.md
:::

:::{toctree}  
:hidden:
:caption: MANUTENZIONE 
FlexiBowl_manual/MANUTENZIONE/01_ordinaria.md
FlexiBowl_manual/MANUTENZIONE/02_straordinaria.md
:::

:::{toctree}  
:hidden:
:caption: GARANZIA 
FlexiBowl_manual/Garanzia.md
:::

:::{toctree}  
:hidden:
:caption: TROUBLESHOOTING
FlexiBowl_manual/TROUBLESHOOTING/01_risoluzione-problemi.md
:::

:::{toctree}  
:hidden:
:caption: SMALTIMENTO
FlexiBowl_manual/SMALTIMENTO/smaltimento.md
:::

:::{toctree}  
:hidden:
:caption: CERTIFICAZIONI 
FlexiBowl_manual/CERTIFICAZIONI/01_certificazioni.md
:::
