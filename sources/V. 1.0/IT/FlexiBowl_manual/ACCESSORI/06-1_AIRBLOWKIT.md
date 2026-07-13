# [MEC] **Air Blow Kit**

:::{note}
L'implementazione dei soffi comporta una modifica dell'impianto pneumatico del FlexiBowl®, per maggiori informazioni fare riferimento agli {ref}`schemi pneumatici <sc-pneum>`.
:::

Il kit soffi (o *Air Blow Kit*) è composto dalle seguenti parti:

## Soffio radiale

Il soffio raadiale consiste in una cartuccia che può essere montata al posto del deviatore standard che presenta due fori radiali ad altezze diverse: da uno dei due, a scelta dell'Operatore in base alle dimensioni dei pezzi da movimentare, esce un getto d'aria che allontana i componenti dall'anello di contenimento.

:::{figure} ../../../../_shared/media/images/sofrad500.PNG
:width: 100%
:align: center
:::

### Procedura di montaggio

:::{warning}
Disconnettere l'alimentazione elettrica prima di procedere con il montaggio dei soffi.
:::

| Step | Operazione |
|:----:|-----------|
| 1 | Rimuovere le viti di fissaggio del deviatore |
| 2 | Svitare le viti di regolazione per rimuovere il deviatore |
| 3 | Posizionare il gommino pieno e quello forato nelle relative sedi in base all’altezza del soffio desiderata |
| 4 | Posizionare la cartuccia soffio radiale e fissarla con le apposite viti |

### Procedura di regolazione

Il soffio radiale si può regolare sia tramite software che meccanicamente agendo sull'apposito grano posto dentro alla cartuccia con una chiave a brugola da 1.5mm, facendo attenzione a fissarne la posizione avvitando lo spintore con un cacciavite piatto.

::::{raw} html
<figure style="text-align: center;">
  <video id="regsof500" width="100%" height="auto" controls>
    <source src="../../../../_shared/media/videos/FB500regsof.mp4" type="video/mp4">
    Il tuo browser non supporta il video.
  </video>
  <br>
  <label for="Velsof500">Velocità:</label>
  <select id="Velsof500" onchange="document.getElementById('regsof500').playbackRate = this.value">
    <option value="0.5">0.5x</option>
    <option value="1" selected>1x</option>
    <option value="1.5">1.5x</option>
    <option value="2">2x</option>
  </select> 
  <figcaption><i>Procedura di regolazione meccanica del soffio radiale illustrata su FlexiBowl® 500</i></figcaption>
</figure>
::::

Si può inoltre scegliere l'altezza del soffio scambiando la guardnizione con il tappo sotto alla cartuccia:

:::{figure} ../../../../_shared/media/images/sofrad500-sm.PNG
:width: 100%
:align: center
:::

## Soffio centrale

Il soffio centrale consiste in un beccuccio montato sulla punta dello schermo flip il cui getto d'aria è direzionato in modo da allontanare i componenti dalla calotta stringi-disco. Il suo scopo è duplice:

- Portare i componenti sopra al flip per massimizzarne l'efficienza;
- Impedire che i componenti vengano considerati non prendibili per via di una eccessiva vicinanza con la calotta stringi-disco, che provocherebbe una collisione del robot.

:::{figure} ../../../../_shared/media/images/sofcen500.PNG
:width: 100%
:align: center
:::

### Procedura di montaggio

| Step | Operazione |
|:----:|-----------|
| 1 | Rimuovere tutto il gruppo schermo-barriera flip svitando le quattro viti di fissaggio |
| 2 | Sostituire lo schermo con il gruppo soffio centrale |
| 3 | Fissare il nuovo gruppo soffio centrale-barriera flip |

### Procedura di regolazione 

La regolazione dell'intensità del soffio avviene via software.

## Applicazioni consigliate

Sono da preferire rispetto al deviatore standard qualora:
- ci sia il bisogno di movimentare componenti che presentano feature o sporgenze di dimensioni ridotte, che potrebbero incastrarsi nel gap tra il deviatore e la superficie o disco rigido;
- si utilizzi una superficie o un disco rigido anti-roll.

## Valutazione del corretto funzionamento

Test standardizzato?