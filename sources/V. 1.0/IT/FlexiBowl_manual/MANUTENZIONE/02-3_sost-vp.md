# **Sostituzione Valvola Proporzionale**

:::::{important}

:::{raw} html
   <style>
     .ars-img-row { display: flex; gap: 12px; align-items: center; justify-content: center; }
     .ars-img-row img { width: 25%; }
   </style>
:::

::::{list-table}
:widths: 30 60
:header-rows: 1
* - {ref}`Qualifica operatore <operatori>`
  - {ref}`D.P.I. Necessari <dpi>`

* - **Manutentore meccanico**
  - :::{raw} html
       <div class="ars-img-row">
         <img src="../../../../_shared/media/images/guanti.png" alt="guanti">
         <img src="../../../../_shared/media/images/scarpe.png" alt="scarpe">
         <img src="../../../../_shared/media/images/tuta.png" alt="tuta">
       </div>
    :::
::::
:::::

:::{warning}
Disconnettere l'alimentazione elettrica e pneumatica prima di procedere con la sostituzione della valvola proporzionale.
:::

## Cosa serve?

:::{list-table}
:widths: 40 40
:header-rows: 1

* - Oggetto/attrezzatura
  - Quantità

* - Chiave esagonale H5
  - 1

* - Chiave esagonale H4
  - 1

* - Chiave esagonale H2.5
  - 1

* - Valvola proporzionale sostitutiva
  - 1

:::

## Procedimento

| Step | Operazione |
|:----:|-----------|
| 1 | {ref}`Rimuovere la superficie o disco rigido <sost-disco>` |
| 2 | Rimuovere il gruppo schermo flip |
| 3 | Rimuovere la piastra di copertura del gruppo flip (usare due delle viti di fissaggio per la rimzozione tramite gli appositi fori filettati) |
| 4 | Scollegare, rimuovere gli allacciamenti pneumatici e smontare la staffa della valvola proporzionale |
| 5 | Sostituire la valvola proporzionale danneggiata con quella nuova |
| 6 | A sostituzione terminata, rimontare tutti i componenti |

::::{raw} html
<figure style="text-align: center;">
  <video id="sostprop" width="100%" height="auto" controls>
    <source src="../../../../_shared/media/videos/AS000006_cambioprop.mp4" type="video/mp4">
    Il tuo browser non supporta il video.
  </video>
  <br>
  <label for="velcamprop">Velocità:</label>
  <select id="velcamprop" onchange="document.getElementById('sostprop').playbackRate = this.value">
    <option value="0.5">0.5x</option>
    <option value="1" selected>1x</option>
    <option value="1.5">1.5x</option>
    <option value="2">2x</option>
  </select>
  <figcaption><i>Procedura di sostituzione della valvola proporzionale illustrata su FlexiBowl® 800</i></figcaption>
</figure>
::::

:::{note}
In base alla presenza o meno dei soffi, possono essere presenti una o due valvole proporzionali: la seconda si trova sotto alla piastra opposta a quella che copre il gruppo flip.
:::