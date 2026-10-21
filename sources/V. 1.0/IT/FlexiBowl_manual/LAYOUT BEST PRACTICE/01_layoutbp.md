(layoutbp)=
# **Layout Best Practice**

L'area di lavoro del FlexiBowl® è virtualmente divisa in quattro settori, ognuno dedicato a una fase del ciclo: **rilascio** dei componenti dalla tramoggia, **separazione** tramite flip, **presa** da parte del robot e **ricircolo** dei componenti non presi. Un buon layout rispetta questa sequenza nel senso di rotazione del FlexiBowl® e riduce al minimo i percorsi di *pick and place*.

:::{figure} ../../../../_shared/media/images/Funz-standard.PNG
:align: center
:width: 50%

Settori di lavoro del FlexiBowl®: rilascio, separazione, presa e ricircolo.
:::

## Linee guida per il posizionamento del robot

:::{tip}
Il modo migliore per piazzare il robot rispetto al FlexiBowl® è quello che minimizza i percorsi di *pick and place*.
:::

(layoutbp-traditional)=
### Traditional Feeding

Nel {ref}`Traditional Feeding <sof-modalita-standard>` l'area di presa coincide con l'area di visione. L'area di lavoro del robot deve quindi coprire interamente l'area di visione, in modo da garantire che il robot possa raggiungere tutti i componenti individuati come prendibili.

<!-- DA COMPLETARE: distanze consigliate robot/FlexiBowl® per taglia -->

(layoutbp-tracking)=
### Circular Tracking

Nel {ref}`Circular Tracking <tracking>` il FlexiBowl® ruota in modo continuo: l'area di visione si trova un settore **a monte** dell'area di presa, che risulta quindi spostata **a valle** nel senso di rotazione. L'area di lavoro del robot deve coprire il settore di presa a valle dell'area di visione.

:::{figure} ../../../../_shared/media/images/TrackingLayout.PNG
:width: 80%
:align: center
:::

<!-- DA COMPLETARE -->

## Linee guida per il posizionamento delle tramogge

### Precauzioni generali

- Posizionare la tramoggia su un piano stabile e orizzontale, vicino al FlexiBowl®.
- Se la tramoggia è installata sul piano di una macchina sensibile alle vibrazioni, interporre materiale isolante e antivibrante tra le superfici, per evitare che le vibrazioni si trasmettano al FlexiBowl® (vedi {ref}`tramoggia-antivibrazione`).
- Fissare la tramoggia alla staffa di supporto con viti M8: 4 fori per le tramogge standard, 2 fori per la tramoggia da 1,5 l.
- Un singolo FlexiBowl® gestisce fino a **4 tramogge**: nel {ref}`Multiple Parts Feeding <funzionamento-in-mix-mode>` è possibile dedicare una tramoggia a ciascuna referenza.

### Posizione consigliata

Lo scivolo della tramoggia deve scaricare i componenti direttamente nel **settore di rilascio**, a monte del flip, con un'inclinazione che segue il profilo del FlexiBowl®.

::::{tab-set}
:::{tab-item} Posizionamento corretto
![Posizionamento corretto della tramoggia rispetto al FlexiBowl®](../../../../_shared/media/images/posizione_giustatramoggia.png)
:::
:::{tab-item} Posizionamento errato
![Esempio di posizionamento errato della tramoggia](../../../../_shared/media/images/posizione_sbagliatatramoggia.png)

Uno scivolo troppo lontano dall'area di lavoro genera un'alimentazione incostante e penalizza le prestazioni dell'applicazione.
:::
::::

## Linee guida per il posizionamento dei depositi

### Indicazioni generali

Posizionare i depositi (vassoi, nastri, stazioni di assemblaggio) il più vicino possibile all'area di presa, per ridurre la corsa del robot a ogni ciclo.

<!-- DA COMPLETARE -->

### Posizione consigliata

<!-- DA COMPLETARE -->

## Linee guida per la configurazione ottimale del movimento

<!-- DA COMPLETARE -->

## Linee guida per la scelta del tool di presa

<!-- DA COMPLETARE -->

## Linee guida per il posizionamento del Toplight

Il {ref}`Toplight <toplight>` deve essere centrato sull'area di visione, con la superficie emittente parallela al piano del FlexiBowl® e la telecamera montata nel foro centrale. La distanza dalla superficie deve essere simile a quella della telecamera, per ridurre le ombre e i riflessi diretti. Per le modalità di fissaggio vedi {ref}`montaggio_staffa`.

## Linee guida per il posizionamento della telecamera

La telecamera deve essere centrata sull'area di visione, con l'asse ottico perpendicolare alla superficie del FlexiBowl® e, se presente, concentrica con il Toplight. La calibrazione con la griglia ARS va eseguita con il Backlight acceso e il Toplight spento.

<!-- DA COMPLETARE: altezze di montaggio e ottiche consigliate per taglia -->
