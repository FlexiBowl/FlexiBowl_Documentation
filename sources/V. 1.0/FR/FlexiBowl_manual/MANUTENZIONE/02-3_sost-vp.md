# **Remplacement de la vanne proportionnelle**

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
* - {ref}`Qualification de l'opérateur <operatori>`
  - {ref}`EPI nécessaires <dpi>`

* - **Technicien de maintenance mécanique**
  - :::{raw} html
       <div class="ars-img-row">
         <img src="../../../../_shared/media/images/guanti.png" alt="gants">
         <img src="../../../../_shared/media/images/scarpe.png" alt="chaussures">
         <img src="../../../../_shared/media/images/tuta.png" alt="combinaison">
       </div>
    :::
::::
:::::

:::{warning}
Débrancher l'alimentation électrique et pneumatique avant de procéder au remplacement de la vanne proportionnelle.
:::

:::{warning}
Certaines parties concernées par l'opération de maintenance décrite ici peuvent avoir atteint des {ref}`températures élevées <temp>` pendant le fonctionnement ; veiller à laisser le FlexiBowl® éteint suffisamment longtemps pour que toutes ses parties puissent être manipulées en toute sécurité.
:::

## De quoi a-t-on besoin ?

:::{list-table}
:widths: 40 40
:header-rows: 1

* - Objet/équipement
  - Quantité

* - Clé hexagonale H5
  - 1

* - Clé hexagonale H4
  - 1

* - Clé hexagonale H2.5
  - 1

* - Vanne proportionnelle de remplacement
  - 1

:::

## Procédure

| Étape | Opération |
|:----:|-----------|
| 1 | {ref}`Retirer la surface ou le disque rigide <sost-disco>` |
| 2 | Retirer le groupe écran flip |
| 3 | Retirer la plaque de recouvrement du groupe flip (utiliser deux des vis de fixation pour la déposer au moyen des trous filetés prévus à cet effet) |
| 4 | Débrancher, retirer les raccordements pneumatiques et démonter le support de la vanne proportionnelle |
| 5 | Remplacer la vanne proportionnelle endommagée par la nouvelle |
| 6 | Une fois le remplacement terminé, remonter tous les composants |

::::{raw} html
<figure style="text-align: center;">
  <video id="sostprop" width="100%" height="auto" controls>
    <source src="../../../../_shared/media/videos/AS000006_cambioprop.mp4" type="video/mp4">
    Votre navigateur ne prend pas en charge la vidéo.
  </video>
  <br>
  <label for="velcamprop">Vitesse :</label>
  <select id="velcamprop" onchange="document.getElementById('sostprop').playbackRate = this.value">
    <option value="0.5">0.5x</option>
    <option value="1" selected>1x</option>
    <option value="1.5">1.5x</option>
    <option value="2">2x</option>
  </select>
  <figcaption><i>Procédure de remplacement de la vanne proportionnelle illustrée sur un FlexiBowl® 800</i></figcaption>
</figure>
::::

:::{note}
Selon la présence ou non des soufflages, une ou deux vannes proportionnelles peuvent être présentes : la seconde se trouve sous la plaque opposée à celle qui recouvre le groupe flip.
:::