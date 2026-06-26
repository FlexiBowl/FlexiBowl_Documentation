# [SOF] **Modalità Mix**

## Funzionamento in MIX Mode

La **MIX Mode** consente di alimentare contemporaneamente pezzi di tipologie diverse sulla stessa superficie del FlexiBowl®.    

Questa modalità è particolarmente indicata per applicazioni di **smistamento** (sorting) in cui è richiesta la presenza di più referenze sullo stesso piano di lavoro senza dover moltiplicare le stazioni robotizzate.

```{figure}  ../../../../_shared/media/images/flexibowl_standard_cycle.jpg
:align: center
:width: 50%
:alt: *Ciclo operativo in Modalità Mix: Detect → Pick-Drop → Move-Flip*
```

```{image}  ../../../../_shared/media/videos/MIX_MODE.gif
:align: center
:width: 100%
:alt: *Ciclo operativo in Modalità Mix: Detect → Pick-Drop → Move-Flip*
```
---

## Caratteristiche principali

| Caratteristica | Descrizione |
|---|---|
| **Applicazione** | Ideale per applicazioni di sorting con più tipologie di pezzi |
| **Flessibilità** | Alimentazione di pezzi misti sulla stessa superficie |

---

## Ciclo operativo

Il ciclo della MIX Mode è semplificato rispetto alla modalità standard, con soli tre stadi
che si ripetono in sequenza:

```{list-table}
:header-rows: 1
:widths: 20 80

* - Fase
  - Descrizione
* - **Detect**
  - La telecamera acquisisce l'immagine della superficie comune, identificando posizione e orientamento di tutti i pezzi presenti, indipendentemente dalla loro tipologia.
* - **Move-Flip**
  - Il FlexiBowl® ruota e i pezzi non correttamente orientati vengono ribaltati o riposizionati.
* - **Pick-Drop**
  - Il robot preleva il pezzo corretto in base alla logica di sorting e lo deposita nella posizione di destinazione.
```

---

## Schema di installazione


:::{figure} ../../../../_shared/media/images/MixLayout.PNG
:width: 80%
:align: center
:::

---

## Note operative

:::{tip}
La MIX Mode non richiede hardware aggiuntivo rispetto a una configurazione standard.  
 È sufficiente configurare il software di visione per il riconoscimento di più referenze e impostare la logica di sorting nel programma robot.
:::

:::{note}
Per il piazzamento ottimale del FlexiBowl® e del robot, fare riferimento al capitolo di {ref}`Layout Best Practice <layoutbp>`.
:::
