# **Câblage du FlexiBowl®**

<style>
.ars-dropdown {
  margin-top: 0.35rem;
}
.ars-dropdown summary {
  cursor: pointer;
  color: #2980b9;
  font-weight: 600;
  font-size: 0.82rem;
  padding: 0.35rem 0.7rem;
  border: 1px solid #d0e4f0;
  border-radius: 6px;
  display: inline-block;
  background: #f0f7ff;
  list-style: none;
  user-select: none;
}
.ars-dropdown summary::-webkit-details-marker { display: none; }
.ars-dropdown summary::before {
  content: "▸ ";
}
.ars-dropdown[open] summary::before {
  content: "▾ ";
}
.ars-dropdown[open] summary {
  border-radius: 6px 6px 0 0;
}
.ars-dropdown .ars-dropdown-body {
  border: 1px solid #d0e4f0;
  border-top: none;
  border-radius: 0 0 6px 6px;
  padding: 0.6rem;
  background: #fff;
}
.ars-dropdown img {
  display: block;
  max-width: 100%;
  width: 360px;
  border-radius: 4px;
}
.ars-step-warn, .ars-step-attn, .ars-step-note {
  border-radius: 5px;
  padding: 0.5rem 0.75rem;
  font-size: 0.83rem;
  margin-top: 0.55rem;
  line-height: 1.4;
}
.ars-step-warn { background:#fff3cd; border-left:4px solid #f0ad4e; color:#7a5b00; }
.ars-step-attn { background:#fee2e2; border-left:4px solid #dc2626; color:#8a1c1c; }
.ars-step-note { background:#eef6fc; border-left:4px solid #2980b9; color:#1a3a52; }
.ars-pin-table { width:100%; border-collapse:collapse; font-size:0.8rem; margin-top:0.4rem; }
.ars-pin-table th { background:#f0f4f8; padding:0.3rem 0.5rem; text-align:left; border:1px solid #d0e4f0; }
.ars-pin-table td { padding:0.3rem 0.5rem; border:1px solid #d0e4f0; }


.ars-zoom-img {
  transition: transform 0.35s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.35s ease;
  cursor: zoom-in;
  position: relative;
}
.ars-zoom-img:hover {
  transform: scale(1.8);
  box-shadow: 0 12px 40px rgba(0,0,0,0.22);
  z-index: 10;
}
</style>

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

* - **Mainteneur électricien**
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
Avant d'effectuer toute connexion électrique, s'assurer que l'alimentation est coupée et que le système est en état de sécurité.
:::

Le câblage du FlexiBowl® varie selon la taille de la machine :

- **FlexiBowl® 500 – 1200** : toutes les connexions (STO, Ethernet, Hopper, alimentation, air) se trouvent sur un unique **panneau électrique standard**, monté directement sur la machine.
- **FlexiBowl® 200 / 350** : les connexions principales se trouvent sur un **rack** externe ; le rack est ensuite relié à la machine par 4 câbles dédiés (Ethernet, Moteur+STO, signal A, signal B). Il ne reste à raccorder sur la machine que l'air comprimé.

---

## FlexiBowl® 500 – 1200 — Panneau électrique standard

```{list-table}
:widths: 8 52 40
:header-rows: 1

* - #
  - Action
  - Image
* - 1
  - **Raccorder le STO.**

    <div class="ars-step-note">
    Connecteur à 10 broches. Les entrées <strong>+STO1</strong> et <strong>+STO2</strong> doivent recevoir <strong>+24 Vdc</strong> du circuit de sécurité ; <strong>−STO1</strong> et <strong>−STO2</strong> doivent être reliées à la référence −24 Vdc.
    </div>

    <details class="ars-dropdown"><summary>Brochage du connecteur à 10 broches</summary><div class="ars-dropdown-body">

    | Broche | Description |
    |---|---|
    | 1 | +24 Vdc |
    | 2 | −24 Vdc |
    | 3 | +STO1 |
    | 4 | −STO1 |
    | 5 | +STO2 |
    | 6 | −STO2 |
    | 7–10 | NC |

    </div></details>
  - 
    ```{image} ../../../../_shared/media/images/connectSTO.png
    :alt: Raccorder le STO
    :class: ars-zoom-img
    ```

* - 2
  - **Raccorder l'Ethernet (C-ETH).**

    <div class="ars-step-attn">
    Lorsque le FlexiBowl® est alimenté, la connexion Ethernet est <strong>obligatoire</strong> : si elle est absente, la machine passe à l'état <strong>ERROR</strong> (LED Ready/Fault rouge).
    </div>

    <details class="ars-dropdown"><summary>Brochage M12 → RJ45</summary><div class="ars-dropdown-body">

    Adaptateur M12 8 pôles → RJ45 :

    | Broche RJ45 | Signal | Fonction | Couleur |
    |---|---|---|---|
    | 1 | TD+ | Transmission de données (+) | Jaune |
    | 2 | TD− | Transmission de données (−) | Orange |
    | 3 | RD+ | Réception de données (+) | Blanc |
    | 4 | NC | Non affecté | — |
    | 5 | NC | Non affecté | — |
    | 6 | RD− | Réception de données (−) | Bleu |
    | 7 | NC | Non affecté | — |
    | 8 | NC | Non affecté | — |

    Connecteur M12 codage D 4 pôles :

    | Broche M12 | Signal | Fonction | Couleur |
    |---|---|---|---|
    | 1 | TD+ | Transmission de données (+) | Jaune |
    | 2 | RD+ | Réception de données (+) | Blanc |
    | 3 | TD− | Transmission de données (−) | Orange |
    | 4 | RD− | Réception de données (−) | Bleu |

    </div></details>
  - 
    ```{image} ../../../../_shared/media/images/connectEthernet.png
    :alt: Raccorder l'Ethernet
    :class: ars-zoom-img
    ```

* - 3
  - **Raccorder le Hopper.**

    <div class="ars-step-note">
    Connecteur M12 codage A, utilisé pour communiquer avec les contrôleurs de hopper ARS via le protocole <strong>Modbus RTU</strong>.
    </div>

    <details class="ars-dropdown"><summary>Brochage M12 codage A</summary><div class="ars-dropdown-body">

    | Broche M12 | Signal | Fonction | Couleur |
    |---|---|---|---|
    | 1 | A+ | Ligne de données RS485 (+) | Marron |
    | 2 | NC | Non affecté | Blanc |
    | 3 | B− | Ligne de données RS485 (−) | Bleu |
    | 4 | GND | Référence commune | Noir |
    | 5 | NC | Non affecté | Gris |

    </div></details>
  - 
    ```{image} ../../../../_shared/media/images/connectHopper.png
    :alt: Raccorder le Hopper
    :class: ars-zoom-img
    ```

* - 4
  - **Raccorder l'alimentation (Power Supply).**

    <div class="ars-step-attn">
    S'assurer que le FlexiBowl® est <strong>éteint</strong> avant de raccorder l'alimentation.
    </div>

    <div class="ars-step-warn">
    Tension admise : <strong>120–230 Vac, 50/60 Hz</strong>.
    </div>

    <div class="ars-step-note">
    Au premier démarrage, vérifiez l'état des fusibles. Après la mise sous tension, attendez que la LED d'état (Ready/Fault) s'allume : si le Hopper et le C-ETH sont correctement raccordés, la LED sera <strong>verte</strong>.
    </div>

    <details class="ars-dropdown"><summary>Schéma de brochage du câble d'alimentation</summary><div class="ars-dropdown-body">

    | Couleur | Type | Étiquette |
    |---|---|---|
    | Marron | Phase | L1 |
    | Bleu | Neutre | N1 |
    | Jaune/Vert | Terre | PE1 |

    </div></details>
  - 
    ```{image} ../../../../_shared/media/images/connectSupply.png
    :alt: Raccorder l'alimentation
    :class: ars-zoom-img
    ```

* - 5
  - **Raccorder l'air comprimé** avec un tube **Ø 8 mm**.

    :::{note}
    Pour les caractéristiques d'air requises (pression, classe de propreté ISO), consultez les [Données techniques pneumatiques](datipneum).
    :::
  - 
    ```{image} ../../../../_shared/media/images/connectAir.png
    :alt: Raccorder l'air comprimé Ø8mm
    :class: ars-zoom-img
    ```
```
:::{video} ../../../../_shared/media/videos/cablaggio_FB800.mp4
:width: 100% 
:::

---

## FlexiBowl® 200 / 350 — Rack externe

Pour ces tailles, les connexions vers les installations du client se trouvent sur le **rack** externe (et non sur la machine). Le rack doit ensuite être relié à la machine par 4 câbles dédiés.

### Connexions sur le rack

Les connecteurs du rack sont les mêmes que ceux du panneau standard (même brochage), simplement placés sur un boîtier externe plutôt que sur la machine.

```{list-table}
:header-rows: 1

* - #
  - Action

* - 1
  - **Raccorder le STO** sur le rack — même connecteur à 10 broches que le panneau standard (voir le tableau de brochage ci-dessus).

* - 2
  - **Raccorder le C-ETH IN** sur le rack — même connecteur M12 codage D que le panneau standard. La même règle s'applique : la connexion est obligatoire, sinon la machine passe en ERROR.

* - 3
  - **Raccorder le Hopper** sur le rack — même connecteur M12 codage A (Modbus RTU) que le panneau standard.

* - 4
  - **Raccorder l'alimentation** sur le rack — 120–230 Vac.

    <div class="ars-step-attn">
    S'assurer que le FlexiBowl® est <strong>éteint</strong> avant de raccorder l'alimentation.
    </div>
```

### Raccordement entre le rack et le FlexiBowl®

Le rack communique avec le FlexiBowl® par 4 câbles dédiés, chacun devant être raccordé **exclusivement** au port portant l'étiquette correspondante sur le panneau.

:::{attention}
Raccorder chaque câble au port portant l'**étiquette correspondante** (par ex. MOTOR ↔ MOTOR, C-A SIGNAL ↔ C-A SIGNAL). Un raccordement croisé peut endommager le système.
:::

```{list-table}
:widths: 8 52 40
:header-rows: 1

* - #
  - Action
  - Image
* - 5
  - **Raccorder le câble Ethernet (C-ETH FB)** entre le rack et le FlexiBowl® — connecteur M12 codage D.
  - 
    ```{image} ../../../../_shared/media/images/connectEthernet200.png
    :width: 110%
    :alt: Raccorder le câble C-ETH FB
    :class: ars-zoom-img
    ```
* - 6
  - **Raccorder le câble MOTOR.**

    <div class="ars-step-note">
    Connecteur à 9 broches : véhicule à la fois l'alimentation du moteur et les signaux <strong>STO</strong> vers le FlexiBowl® (sur le rack, STO et Moteur sont des connecteurs séparés ; sur le câble vers la machine, ils sont regroupés en un seul connecteur à 9 broches).
    </div>
  - 
    ```{image} ../../../../_shared/media/images/connectMotor.png
    :width:110%
    :alt: Raccorder le câble Motor
    :class: ars-zoom-img
    ```
* - 7
  - **Raccorder le câble C-A SIGNAL** — connecteur à 19 broches pour les signaux analogiques.
  - 
    ```{image} ../../../../_shared/media/images/connectASignal.png
    :width:110%
    :alt: Raccorder le câble C-A Signal
    :class: ars-zoom-img
    ```
* - 8
  - **Raccorder le câble C-B SIGNAL** — connecteur à 19 broches pour les signaux numériques.
  - 
    ```{image} ../../../../_shared/media/images/connectBSignal.png
    :width:110%
    :alt: Raccorder le câble C-B Signal
    :class: ars-zoom-img
    ```
* - 9
  - **Raccorder l'air comprimé** avec un tube **Ø 6 mm**, directement sur le panneau de la machine.

    :::{note}
    Pour les caractéristiques d'air requises (pression, classe de propreté ISO), consultez les [Données techniques pneumatiques](datipneum).
    :::
  - 
    ```{image} ../../../../_shared/media/images/connectAir200.png
    :width:110%
    :alt: Raccorder l'air comprimé Ø6mm
    :class: ars-zoom-img
    ```
```
:::{video} ../../../../_shared/media/videos/cablaggio_FB200.mp4
:width: 100% 
:::