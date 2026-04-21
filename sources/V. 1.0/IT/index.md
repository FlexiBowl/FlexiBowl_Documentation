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
Schema esemplificativo del sistema con collegamenti fino a tre FlexiBowl, tre camere e tre tramogge.

```{figure} ../../_shared/media/images/Icon_FlexiVision.png
:align: center
:width: 50%

Schema esemplificativo del sistema FlexiVision One
```
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
## **Gruppi di intervento e responsabilità**

La corretta implementazione di FlexiVision One richiede la collaborazione di diverse figure professionali. Questa tabella chiarisce ruoli e responsabilità:

```{list-table}
:widths: 25 35 40
:header-rows: 1

* - Figura professionale
  - Responsabilità principali
  - Sezioni del manuale di riferimento

* - **Integratore di sistema**
  - Progettazione layout, dimensionamento componenti, verifica requisiti tecnici
  - Riferimento tecnico e specifiche, Opzioni

* - **Tecnico installatore**
  - Montaggio meccanico, allacciamento elettrico e pneumatico, configurazione rete
  - Installazione del sistema, Cablaggio e connessioni

* - **Manutentore**
  - Diagnosi problemi, sostituzione componenti, aggiornamenti software
  - Nuovo modello, Configurazione FlexiBowl, Troubleshooting, Support
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
FlexiBowl_manual/PRIMA DI INIZIARE/03_unboxing.md
FlexiBowl_manual/PRIMA DI INIZIARE/04_support.md
FlexiBowl_manual/PRIMA DI INIZIARE/05_glossario.md
:::
  
:::{toctree}
:hidden:
:caption: QUICKSTART
FlexiBowl_manual/QUICKSTART/01_panoramica.md
FlexiBowl_manual/QUICKSTART/02_dati-tecnici-meccanici.md
FlexiBowl_manual/QUICKSTART/03_dati-tecnici-elettrici.md
FlexiBowl_manual/QUICKSTART/04_dati-tecnici-pneumatici.md
FlexiBowl_manual/QUICKSTART/05_dati-tecnici-applicativi.md
FlexiBowl_manual/QUICKSTART/06_componenti-opzionali.md
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
:caption: PLUG-IN 
FlexiBowl_manual/PLUG-IN/01_PlugIn.md
:::

:::{toctree}
:hidden:
:caption: LAYOUT BEST PRACTICE
FlexiBowl_manual/LAYOUT BEST PRACTICE/01_layoutbd.md
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
:caption: CERTIFICAZIONI 
FlexiBowl_manual/CERTIFICAZIONI/01_certificazioni.md
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
