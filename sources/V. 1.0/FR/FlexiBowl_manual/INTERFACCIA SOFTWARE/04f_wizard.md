# **Wizard**
L'interface **FlexiBowl® Wizard** est un outil interactif conçu pour guider l'utilisateur dans la configuration des paramètres d'alimentation en fonction de la famille de produits spécifique à gérer.

![Page Wizard](../../../../_shared/media/images/wizard_home_page.png)

## Étape 0 : Accès au Wizard

:::{list-table}
* - **1**
  - Pour accéder à la configuration guidée des paramètres du FlexiBowl®, il suffit de cliquer sur la page **Wizard** dans le menu latéral.
:::

:::{note}
Le modèle et le sens de rotation du FlexiBowl® sont automatiquement détectés par le logiciel.
:::

## Étape 1 : Caractérisation du composant

Le système demande des informations sur la morphologie des pièces afin d'optimiser la séparation.
````{list-table}
* - **2**
  - Sélectionner la taille du composant :

    **Pour les modèles FlexiBowl 200, 350, 500, 650 :**

    :::{card}
    <= 150mm
    :::

    :::{card}
    &gt; 150mm
    :::

    **Pour les modèles FlexiBowl 800 et 1200 :**

    :::{card}
    <= 250mm
    :::

    :::{card}
    &gt; 250mm
    :::

* - **3**
  - Sélectionner la géométrie qui décrit le mieux le composant :
      * **FLAT** : Composants plats.
      * **CYLINDRICAL** : Composants cylindriques.
      * **COMPLEX** : Géométries articulées ou irrégulières

      ![Flat, Cylindrical ou Complex](../../../../_shared/media/images/flatorcomplex.png)

      *Exemples de géométries : Flat, Cylindrical et Complex.*

* - **4**
  - Définir comment les composants interagissent entre eux sur la surface :
      * **Overlapping** : Les pièces ont tendance à se chevaucher.
      * **Not Overlapping** : Les pièces ne se chevauchent pas.
      * **Tangling / Stacking** : Les pièces ont tendance à s'accrocher ou à s'empiler.
      * **Not Tangling / Not Stacking** : Les pièces restent séparées et ne s'emboîtent pas.

      ![Overlapping](../../../../_shared/media/videos/overlapping.gif)

      *Not Overlapping : les pièces ne se chevauchent pas sur la surface.*

      ::::{grid} 2
      :::{grid-item}
      ![Stacking](../../../../_shared/media/videos/stacking.gif)

      *Stacking : les pièces s'empilent.*
      :::
      :::{grid-item}
      ![Tangling](../../../../_shared/media/videos/tangling.gif)

      *Tangling : les pièces s'accrochent entre elles.*
      :::
      ::::
````
## Étape 2 : Test des accessoires
```{list-table}
* - **5**
  - Sélectionner dans le menu déroulant si le FlexiBowl® est équipé du module **Air-blow**.
* - **6**
  - Cliquer sur **TEST Air-blow** pour vérifier le fonctionnement.
* - **7**
  - Sélectionner **USE** pour l'activer dans l'application en cours, sinon cliquer sur **DON'T USE**.
* - **8**
  - Cliquer sur **TEST FLIP** pour vérifier l'activation effective du percuteur. Le « Flip » est l'unité qui génère l'impulsion mécanique pour retourner les pièces ; elle est fondamentale pour séparer, démêler ou retourner les composants pendant le cycle d'alimentation.
 
      :::{important}
      Si l'impulsion n'est pas perceptible, vérifier que l'air comprimé est raccordé et agir sur le régulateur de pression mécanique situé sur le panneau de commande.
      :::
* - **9**
  - À la fin du Wizard, en cliquant sur **FINISH**, le système calculera automatiquement les paramètres :
    - Paramètres de mouvement (vitesse, accélération, angle)
    - Paramètres de secouage (shake)
    - Temporisations des accessoires (flip, blow)
* - **10**
  - Il sera ensuite possible de les affiner dans le tableau de bord récapitulatif.
```
```{list-table} Vue d'ensemble des paramètres
   :widths: 20 30 50
   :header-rows: 1

   * - Groupe
     - Paramètre
     - Description
   * - **Move**
     - Accel, Decel, Speed, Angle
     - Paramètres du mouvement principal du disque.
   * - **Option**
     - Flip Count, Flip Delay, Blow Time
     - Gestion des temps d'activation des accessoires.
   * - **Shake**
     - Accel, Speed, Angle CW/CCW
     - Paramètres de la vibration de secouage (séparation).
```

## Étape 3 : Validation de la séquence

Utiliser la fonction **...** pour vérifier que le cycle respecte les critères d'efficacité suivants :
```{list-table}
:widths: 5 95
:header-rows: 0

* - **Synchronisation**
  - L'impulsion de Flip doit se terminer exactement au même instant que le mouvement (*Move*). Régler les valeurs de *Flip Count* et *Delay* pour les aligner.

* - **Stabilité de l'image**
  - Les composants doivent être immobiles au moment de la prise de vue de la caméra.
    - Si les pièces bougent, diminuer la vitesse/l'accélération ou insérer une pause (par ex. `pause 200ms`).

* - **Positionnement des pièces pendant la séquence**
  - Pendant le mouvement, les pièces doivent être acheminées vers le centre du rayon du FlexiBowl® afin de maximiser l'efficacité du Flip. À la fin de la séquence, les pièces doivent se disposer approximativement au centre de la zone de vision.
```

:::{warning}
Cliquer toujours sur **Synchronize Parameters** après chaque modification manuelle afin de rendre les changements actifs dans le contrôleur.
:::
