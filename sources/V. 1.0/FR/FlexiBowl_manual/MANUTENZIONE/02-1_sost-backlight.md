(sostbl)=
# **Remplacement du Backlight**

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

Le backlight doit être remplacé s'il présente des dysfonctionnements ou s'il est nécessaire de changer le type de lumière à la suite d'un changement de production.

:::{warning}
Débrancher l'alimentation électrique avant de procéder au remplacement du Backlight.
:::

:::{warning}
Certaines parties concernées par l'opération de maintenance décrite ici peuvent avoir atteint des {ref}`températures élevées <temp>` pendant le fonctionnement ; veiller à laisser le FlexiBowl® éteint suffisamment longtemps pour que toutes ses parties puissent être manipulées en toute sécurité.
:::

:::{important}
Le Backlight infrarouge émet une lumière non visible et peut donc sembler ne pas fonctionner. Contrôler avec une caméra infrarouge pour vérifier son fonctionnement.

**Remarque :** La plupart des smartphones affichent l'infrarouge.
:::

## De quoi a-t-on besoin ?

:::{list-table}
:widths: 40 40
:header-rows: 1

* - Objet/équipement
  - Quantité

* - Clé hexagonale H2.5
  - 1

* - Clé hexagonale H5
  - 1

* - Backlight de remplacement
  - 1

:::

## Procédure

| Étape | Opération |
|:----:|-----------|
| 1 | {ref}`Retirer la surface ou le disque rigide <sost-disco>` |
| 2 | Retirer la vitre de protection de l'illuminateur (utiliser les poches latérales prévues à cet effet) |
| 3 | Retirer les vis qui fixent la carte de l'illuminateur à son logement |
| 4 | Extraire la carte de l'illuminateur et débrancher son connecteur |
| 5 | Connecter la nouvelle carte et la monter dans la bonne position |
| 6 | Une fois le remplacement terminé, remonter tous les composants |

::::{raw} html
<figure style="text-align: center;">
  <video id="myVideo" width="100%" height="auto" controls>
    <source src="../../../../_shared/media/videos/AS000006_cambio-backlight.mp4" type="video/mp4">
    Votre navigateur ne prend pas en charge la vidéo.
  </video>
  <br>
  <label for="speedControl">Vitesse :</label>
  <select id="speedControl" onchange="document.getElementById('myVideo').playbackRate = this.value">
    <option value="0.5">0.5x</option>
    <option value="1" selected>1x</option>
    <option value="1.5">1.5x</option>
    <option value="2">2x</option>
  </select>
  <figcaption><i>Procédure de remplacement du backlight illustrée sur un FlexiBowl® 800</i></figcaption>
</figure>
::::