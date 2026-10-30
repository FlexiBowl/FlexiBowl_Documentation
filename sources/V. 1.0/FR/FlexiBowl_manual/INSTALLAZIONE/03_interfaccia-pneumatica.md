(intpneum)=
# **Interface pneumatique**

La machine est équipée d'un actionnement pneumatique. Avant d'effectuer le **raccordement pneumatique**, vérifier que :
- l'installation d'alimentation en air comprimé présente garantit à la machine la quantité d'air à la bonne pression ;
- le réservoir d'air comprimé prévu est correctement dimensionné.

Le raccordement pneumatique doit être effectué en raccordant la ligne principale au circuit de la machine. Le client doit en outre garantir une alimentation en air présentant les caractéristiques indiquées dans le paragraphe {ref}`« Données techniques pneumatiques » <datipneum>` du présent manuel.

:::{warning}
Ne jamais dépasser 7 bar de pression dans l'installation pneumatique de la machine.
:::

:::{warning}
Le FlexiBowl® est fourni sans dispositif manuel de coupure et de décharge de l'alimentation pneumatique. L'intégrateur doit prévoir en amont un dispositif clairement identifié, facilement accessible et verrouillable en position fermée, permettant d'interrompre l'alimentation, de décharger la pression résiduelle et d'empêcher toute remise en marche involontaire. Les tuyauteries et raccords doivent être adaptés à la pression de service, correctement fixés et protégés contre l'arrachement. Les éventuels dispositifs pneumatiques de sécurité supplémentaires doivent être définis au moyen de l'évaluation des risques de la machine finale.
:::

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

Pour le raccordement au réseau pneumatique, raccorder un tuyau d'air {ref}`de la bonne taille <datipneum>` à l'entrée « Air Supply » présente sur le {ref}`panneau de commande <intele>`.

:::{raw} html
<style>
.img-zoom-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 16px;
  padding: 1rem 0;
}
.img-zoom-wrap {
  flex: 1 1 0;
  min-width: 0;
  overflow: visible;
  display: flex;
  align-items: center;
  justify-content: center;
}
.img-zoom-wrap img {
  width: 100%;
  border-radius: 8px;
  transition: transform 0.35s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.35s ease;
  cursor: zoom-in;
  position: relative;
  transform: scale(1);
}
.img-zoom-wrap img:hover {
  transform: scale(1.85);
  box-shadow: 0 12px 40px rgba(0,0,0,0.22);
  z-index: 10;
}
</style>

<div class="img-zoom-grid">
  <div class="img-zoom-wrap">
    <img src="../../../../_shared/media/images/smallpanel5.PNG" alt="Panneau small" />
  </div>
  <div class="img-zoom-wrap">
    <img src="../../../../_shared/media/images/stpanel2.PNG" alt="Panneau ST" />
  </div>
  <div class="img-zoom-wrap">
    <img src="../../../../_shared/media/images/encpanel7.PNG" alt="Panneau ENC" />
  </div>
</div>
:::

<style>
.ars-dropdown {
  margin: 0.9rem 0 0.4rem 0;
  border: 2px solid #7fb3dd;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 6px rgba(26,111,196,0.10);
}
.ars-dropdown summary {
  cursor: pointer;
  color: #2980b9;
  font-weight: 600;
  font-size: 0.83rem;
  padding: 0.5rem 0.9rem;
  display: block;
  background: #eaf3fb;
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
  border-bottom: 2px solid #7fb3dd;
}
.ars-dropdown .ars-dropdown-body {
  padding: 0.9rem 1rem;
  background: #fff;
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

---

## Caractéristiques d'air requises

| Paramètre | Valeur |
|---|---|
| Qualité de l'air | Air comprimé propre et sec, selon **ISO 8573-1:2010, classe 1.3.2** |
| Pression d'alimentation recommandée | **7 bar** (à ne jamais dépasser) |
| Diamètre du tuyau — FB200 / FB350 | **Ø 6 mm** |
| Diamètre du tuyau — FB500E / FB500 / FB650 / FB800 / FB1200 | **Ø 8 mm** |

<details class="ars-dropdown"><summary>Consommation d'air indicative par modèle (action Flip)</summary><div class="ars-dropdown-body">

| Modèle | Consommation moyenne | Consommation de pointe |
|---|---|---|
| FB200 | 25 l/min | 45 l/min |
| FB350 | 15 l/min | 24 l/min |
| FB500E | 55 l/min | 74 l/min |
| FB500 | 35 l/min | 48 l/min |
| FB650 | 30 l/min | 45 l/min |
| FB800 | 45 l/min | 60 l/min |
| FB1200 | 135 l/min | 176 l/min |

Les valeurs indiquées se rapportent à la seule action Flip ; pour le détail complet des consommations, se reporter au paragraphe {ref}`« Données techniques pneumatiques » <datipneum>`.

</div></details>

:::{note}
Sur le FlexiBowl® 3.0, le réglage de la pression et la lecture du manomètre s'effectuent au moyen de l'**interface logicielle**, et non plus avec un régulateur et un manomètre physiques sur le panneau comme sur la génération précédente 2.0.
:::

---

## Procédure guidée — Raccordement pneumatique

Pour le raccordement pneumatique également, la procédure change légèrement en fonction de la taille de la machine, en particulier pour le diamètre du tuyau et la position du connecteur **AIR SUPPLY**.

:::{attention}
Avant de commencer tout raccordement pneumatique, s'assurer que l'alimentation en air comprimé est **coupée** et que la pression résiduelle dans le circuit a été **déchargée**.
:::

### FlexiBowl® 500 – 1200 — Panneau électrique standard

```{list-table}
:widths: 8 52 40
:header-rows: 1

* - #
  - Action
  - Image
* - 1
  - **Vérifications préliminaires.**

    Contrôler que l'installation d'alimentation garantit la pression et le débit requis, et que le réservoir d'air comprimé est correctement dimensionné pour le modèle installé.

    <div class="ars-step-note">
    Air propre et sec selon ISO 8573-1:2010, classe 1.3.2. Pression recommandée : 7 bar.
    </div>
  -

* - 2
  - **Couper l'alimentation en air** en amont de l'installation, avant de raccorder le tuyau.

    <div class="ars-step-attn">
    Ne jamais raccorder ou débrancher le tuyau d'air lorsque l'installation est encore sous pression.
    </div>
  -

* - 3
  - **Raccorder le tuyau d'air** à l'entrée **AIR SUPPLY** du panneau électrique standard, en utilisant un tuyau de diamètre extérieur **Ø 8 mm**.
  -
    ```{image} ../../../../_shared/media/images/connectAir.png
    :alt: Raccorder l'air comprimé Ø8mm
    :class: ars-zoom-img
    ```

* - 4
  - **Vérifier l'étanchéité du raccordement** : contrôler que le raccord est correctement enfoncé et qu'il n'y a pas de fuites audibles ou perceptibles au toucher le long du tuyau et du raccord.
  -

* - 5
  - **Rétablir l'alimentation en air** et vérifier que la pression en aval se situe dans les paramètres prévus.

    <div class="ars-step-note">
    Sur le FlexiBowl® 3.0, la pression peut être lue et réglée directement depuis l'interface logicielle.
    </div>
  -
```

### FlexiBowl® 200 / 350

Sur ces tailles, le connecteur **AIR SUPPLY** se trouve directement sur le panneau de la machine (et non sur le rack externe), en aval de tous les autres câblages.

```{list-table}
:widths: 8 52 40
:header-rows: 1

* - #
  - Action
  - Image
* - 1
  - **Vérifications préliminaires.**

    Contrôler que l'installation d'alimentation garantit la pression et le débit requis, et que le réservoir d'air comprimé est correctement dimensionné pour le modèle installé.

    <div class="ars-step-note">
    Air propre et sec selon ISO 8573-1:2010, classe 1.3.2. Pression recommandée : 7 bar.
    </div>
  -

* - 2
  - **Couper l'alimentation en air** en amont de l'installation, avant de raccorder le tuyau.

    <div class="ars-step-attn">
    Ne jamais raccorder ou débrancher le tuyau d'air lorsque l'installation est encore sous pression.
    </div>
  -

* - 3
  - **Raccorder le tuyau d'air** directement sur le panneau de la machine, en utilisant un tuyau de diamètre extérieur **Ø 6 mm**.
  -
    ```{image} ../../../../_shared/media/images/connectAir200.png
    :width: 110%
    :alt: Raccorder l'air comprimé Ø6mm
    :class: ars-zoom-img
    ```

* - 4
  - **Vérifier l'étanchéité du raccordement** : contrôler que le raccord est correctement enfoncé et qu'il n'y a pas de fuites audibles ou perceptibles au toucher le long du tuyau et du raccord.
  -

* - 5
  - **Rétablir l'alimentation en air** et vérifier que la pression en aval se situe dans les paramètres prévus.

    <div class="ars-step-note">
    Sur le FlexiBowl® 3.0, la pression peut être lue et réglée directement depuis l'interface logicielle.
    </div>
  -
```

---

## Notes et avertissements généraux

:::{attention}
Toutes les opérations de raccordement et de débranchement pneumatique doivent être effectuées avec l'installation **coupée** et la **pression résiduelle déchargée**.
:::

:::{attention}
Ne jamais dépasser **7 bar** de pression dans l'installation pneumatique de la machine.
:::

:::{attention}
Le FlexiBowl® n'est pas équipé d'un dispositif manuel de coupure et de décharge : il incombe à l'intégrateur d'en prévoir un en amont, clairement identifié, accessible et verrouillable en position fermée.
:::

:::{attention}
Utiliser exclusivement des tuyaux et raccords adaptés à la pression de service, correctement fixés et protégés contre l'arrachement.
:::

:::{attention}
Pour toute information technique complémentaire ou assistance, contacter ARS s.r.l. – FlexiBowl® Division.
:::
