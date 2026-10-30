# **Austausch des Proportionalventils**

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

:::{warning}
Vor dem Austausch des Proportionalventils die elektrische und pneumatische Versorgung trennen.
:::

:::{warning}
Einige von den hier beschriebenen Wartungsarbeiten betroffene Teile können im Betrieb {ref}`hohe Temperaturen <temp>` erreicht haben; den FlexiBowl® ausreichend lange ausgeschaltet lassen, damit alle Teile gefahrlos gehandhabt werden können.
:::

## Was wird benötigt?

:::{list-table}
:widths: 40 40
:header-rows: 1

* - Gegenstand/Ausrüstung
  - Menge

* - Sechskantschlüssel H5
  - 1

* - Sechskantschlüssel H4
  - 1

* - Sechskantschlüssel H2.5
  - 1

* - Ersatz-Proportionalventil
  - 1

:::

## Vorgehensweise

| Schritt | Vorgang |
|:----:|-----------|
| 1 | {ref}`Oberfläche oder starre Scheibe entfernen <sost-disco>` |
| 2 | Flip-Schirmgruppe entfernen |
| 3 | Die Abdeckplatte der Flip-Einheit entfernen (zwei der Befestigungsschrauben in die dafür vorgesehenen Gewindebohrungen eindrehen, um sie abzudrücken) |
| 4 | Die pneumatischen Anschlüsse trennen und entfernen und die Halterung des Proportionalventils ausbauen |
| 5 | Das beschädigte Proportionalventil durch das neue ersetzen |
| 6 | Nach Abschluss des Austauschs alle Komponenten wieder montieren |

::::{raw} html
<figure style="text-align: center;">
  <video id="sostprop" width="100%" height="auto" controls>
    <source src="../../../../_shared/media/videos/AS000006_cambioprop.mp4" type="video/mp4">
    Ihr Browser unterstützt das Video nicht.
  </video>
  <br>
  <label for="velcamprop">Geschwindigkeit:</label>
  <select id="velcamprop" onchange="document.getElementById('sostprop').playbackRate = this.value">
    <option value="0.5">0.5x</option>
    <option value="1" selected>1x</option>
    <option value="1.5">1.5x</option>
    <option value="2">2x</option>
  </select>
  <figcaption><i>Austauschverfahren des Proportionalventils, dargestellt an einem FlexiBowl® 800</i></figcaption>
</figure>
::::

:::{note}
Je nachdem, ob die Blasluftfunktionen vorhanden sind, können ein oder zwei Proportionalventile vorhanden sein: Das zweite befindet sich unter der Platte gegenüber derjenigen, die die Flip-Einheit abdeckt.
:::