(sostbl)=
# **Austausch des Backlight**

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
* - {ref}`Qualifikation des Bedieners <operatori>`
  - {ref}`Erforderliche PSA <dpi>`

* - **Mechanischer Instandhalter**
  - :::{raw} html
       <div class="ars-img-row">
         <img src="../../../../_shared/media/images/guanti.png" alt="Handschuhe">
         <img src="../../../../_shared/media/images/scarpe.png" alt="Schuhe">
         <img src="../../../../_shared/media/images/tuta.png" alt="Overall">
       </div>
    :::
::::
:::::

Das Backlight ist auszutauschen, wenn es Fehlfunktionen aufweist oder wenn nach einem Produktionswechsel die Lichtart geändert werden muss.

:::{warning}
Vor dem Austausch des Backlight die elektrische Stromversorgung trennen.
:::

:::{warning}
Einige von den hier beschriebenen Wartungsarbeiten betroffene Teile können im Betrieb {ref}`hohe Temperaturen <temp>` erreicht haben; den FlexiBowl® ausreichend lange ausgeschaltet lassen, damit alle Teile gefahrlos gehandhabt werden können.
:::

:::{important}
Das Infrarot-Backlight emittiert nicht sichtbares Licht und kann daher defekt erscheinen. Mit einer Infrarotkamera prüfen, ob es funktioniert.

**Hinweis:** Die meisten Smartphones können Infrarot sichtbar machen.
:::

## Was wird benötigt?

:::{list-table}
:widths: 40 40
:header-rows: 1

* - Gegenstand/Ausrüstung
  - Menge

* - Sechskantschlüssel H2.5
  - 1

* - Sechskantschlüssel H5
  - 1

* - Ersatz-Backlight
  - 1

:::

## Vorgehensweise

| Schritt | Vorgang |
|:----:|-----------|
| 1 | {ref}`Oberfläche oder starre Scheibe entfernen <sost-disco>` |
| 2 | Das Schutzglas des Leuchtkörpers entfernen (die dafür vorgesehenen seitlichen Aussparungen verwenden) |
| 3 | Die Schrauben entfernen, die die Leuchtkörperplatine in ihrem Sitz befestigen |
| 4 | Die Leuchtkörperplatine herausziehen und ihren Stecker trennen |
| 5 | Die neue Platine anschließen und in der richtigen Position montieren |
| 6 | Nach Abschluss des Austauschs alle Komponenten wieder montieren |

::::{raw} html
<figure style="text-align: center;">
  <video id="myVideo" width="100%" height="auto" controls>
    <source src="../../../../_shared/media/videos/AS000006_cambio-backlight.mp4" type="video/mp4">
    Ihr Browser unterstützt das Video nicht.
  </video>
  <br>
  <label for="speedControl">Geschwindigkeit:</label>
  <select id="speedControl" onchange="document.getElementById('myVideo').playbackRate = this.value">
    <option value="0.5">0.5x</option>
    <option value="1" selected>1x</option>
    <option value="1.5">1.5x</option>
    <option value="2">2x</option>
  </select>
  <figcaption><i>Austauschverfahren des Backlight, dargestellt an einem FlexiBowl® 800</i></figcaption>
</figure>
::::