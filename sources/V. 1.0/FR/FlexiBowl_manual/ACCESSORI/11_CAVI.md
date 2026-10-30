(cavi)=
# **Câbles de raccordement**

Les câbles de raccordement du FlexiBowl® peuvent être achetés séparément en option, dans les longueurs de **3, 5 ou 10 mètres**. Cette page récapitule les câbles disponibles au catalogue, leurs prérequis et leurs brochages.

:::{note}
Les câbles des Bulk Feeder (câble Modbus RTU et câble d'entrée du contrôleur) sont décrits dans la page {ref}`Accessoires et options des Bulk Feeder <tramoggia-cavi>`.
:::

:::{warning}
Ne raccorder et débrancher les câbles que lorsque l'appareil est éteint et déconnecté de l'alimentation.
:::

## Récapitulatif

:::{list-table}
:widths: 24 32 22 22
:header-rows: 1

* - Câble
  - Prérequis
  - Tailles compatibles
  - Longueurs
* - [Câble pour option E/S](cavo-io)
  - Option **Digital I/O** (achetée séparément)
  - Toutes les tailles
  - · 3
    · 5
    · 10 m
* - [Câble pour armoire déportée (rack)](cavo-rack)
  - FlexiBowl® avec rack externe
  - FlexiBowl® 200 · 350
  - · 3 m inclus dans la fourniture ;
    · 5
    · 10 m
* - [Câble d'alimentation](cavo-alim)
  - Aucun
  - Toutes les tailles
  - · 3
    · 5
    · 10 m
* - [Câble Ethernet](cavo-eth)
  - Aucun
  - Toutes les tailles
  - · 3
    · 5
    · 10 m
:::

### Articles du catalogue

:::{list-table}
:widths: 28 24 24 24
:header-rows: 1

* - Câble
  - 3 m
  - 5 m
  - 10 m
* - **Option E/S**
  - FlexiBowl cable for I/O option, 3m
  - FlexiBowl cable for I/O option, 5m
  - FlexiBowl cable for I/O option, 10m
* - **Armoire déportée (rack)**
  - Cable for remote electronic cabinet, 3m
  - Cable for remote electronic cabinet, 5m
  - Cable for remote electronic cabinet, 10m
* - **Alimentation**
  - FlexiBowl Power Supply Cable, 3m
  - FlexiBowl Power Supply Cable, 5m
  - FlexiBowl Power Supply Cable, 10m
* - **Ethernet**
  - Ethernet Cable 3m
  - Ethernet Cable 5m
  - Ethernet Cable 10m
:::

---

(cavo-io)=
## Câble pour option E/S

**Description.** Câble pour le raccordement des signaux de l'option **Digital I/O**, qui permet de commander le FlexiBowl® depuis un automate via des entrées et sorties numériques, sans communication Ethernet. Signaux et codage des commandes : [Digital I/O](digIO).

:::{list-table}
:widths: 30 70
:stub-columns: 1

* - Prérequis
  - Option **Digital I/O**, achetée séparément et non incluse dans la configuration standard.
* - Connecteur côté FlexiBowl®
  - Connecteur E/S à 19 broches
    :::{dropdown} **Brochage du connecteur E/S (19 broches)**
    | Broche | Signal | Utilisation | 
    |---|---|---|
    | 1 | IN – Bit 1 | Codage de la commande (Seq. Cmd) | 
    | 2 | IN – Bit 2 | Codage de la commande (Seq. Cmd) | 
    | 3 | IN – Bit 3 | Codage de la commande (Seq. Cmd) | 
    | 4 | IN – Bit 4 | Codage de la commande (Seq. Cmd) | 
    | 5 | IN – Bit 5 | Codage de la commande (Seq. Cmd) | 
    | 6 | IN – Latch | Exécution de la commande (front montant) | 
    | 7–8 | NC | Non affectées | 
    | 9 | OUT – Ready | Sortie d'état | 
    | 10 | OUT – Fault | Sortie d'état | 
    | 11 | OUT – Busy | Sortie d'état | 
    | 12 | OUT – Hopper_1_IsVibrating | Sortie d'état Hopper 1 | 
    | 13 | OUT – Hopper_2_IsVibrating | Sortie d'état Hopper 2 | 
    | 14 | OUT – Hopper_3_IsVibrating | Sortie d'état Hopper 3 | 
    | 15 | OUT – Hopper_4_IsVibrating | Sortie d'état Hopper 4 |
    | 16–19 | NC | Non affectées | 
    :::
* - Longueurs disponibles
  - · 3 m
    · 5 m
    · 10 m
:::


---

(cavo-rack)=
## Câble pour armoire électronique déportée (rack)

**Description.** Câbles de liaison entre le **rack** externe et le FlexiBowl®. Le rack communique avec la machine par 4 câbles dédiés, chacun devant être raccordé exclusivement au port portant l'étiquette correspondante. Procédure de raccordement : {ref}`collegamento-rack`.

:::{list-table}
:widths: 30 70
:stub-columns: 1

* - Prérequis
  - FlexiBowl® avec rack externe (aucune option à acheter).
* - Tailles compatibles
  - · FlexiBowl® 200
    · FlexiBowl® 350
* - Longueurs disponibles
  - · 3 m (inclus dans la fourniture)
    · 5 m
    · 10 m
:::

:::{attention}
Raccorder chaque câble au port portant l'**étiquette correspondante** (par ex. MOTOR ↔ MOTOR, C-A SIGNAL ↔ C-A SIGNAL). Un raccordement croisé peut endommager le système.
:::

:::{list-table}
:header-rows: 1 

* - Câble
  - Connecteur
  - Fonction

* - **C-ETH FB**
  - M12 D-code
    :::{dropdown} **Brochage C-ETH FB (M12 codage D)**
    | Signal | Fonction | Couleur | Broche M12 (côté FlexiBowl®) | Broche RJ45 (côté client) |
    |---|---|---|---|---|
    | TD+ | Transmission de données (+) | Jaune | 1 | 1 |
    | TD− | Transmission de données (−) | Orange | 3 | 2 |
    | RD+ | Réception de données (+) | Blanc | 2 | 3 |
    | RD− | Réception de données (−) | Bleu | 4 | 6 |
    :::

  - Liaison Ethernet entre le rack et le FlexiBowl®

* - **MOTOR**
  - 9 broches
    :::{dropdown} **Brochage MOTOR (9 broches)**

    | Broche | Utilisation | 
    |---|---|
    | 1 | +STO1 – Safe Torque Off | 
    | 2 | +24 Vdc – Alimentation auxiliaire | 
    | 3 | +STO2 – Safe Torque Off | 
    | 4 | −24 Vdc – Alimentation auxiliaire | 
    | 5 | NC |
    | 6 | +48 Vdc – Motor Power | 
    | 7 | −STO1 – Safe Torque Off | 
    | 8 | −48 Vdc – Motor Power | 
    | 9 | −STO2 – Safe Torque Off | 
    :::
  - Alimentation du moteur et signaux STO

* - **C-A SIGNAL**
  - 12 broches
    :::{dropdown} **Brochage C-A SIGNAL (12 broches)**

    | Broche | Utilisation |
    |---|---|
    | 1 | Analog Output 1 | 
    | 2 | −24 Vdc | 
    | 3 | Analog Input 1 | 
    | 4 | +24 Vdc | 
    | 5–12 | NC | 
    :::
  - Signaux analogiques

* - **C-B SIGNAL**
  - 19 broches
    :::{dropdown} **Brochage C-B SIGNAL (19 broches)**
    | Broche | Utilisation | 
    |---|---|
    | 1 | +24 Vdc – Activation de la LED d'état verte | 
    | 2 | −24 Vdc – Commun des LED d'état | 
    | 3 | +24 Vdc – Activation de la LED d'état rouge | 
    | 4 | +24 Vdc – Activation de la LED d'état du Backlight | 
    | 5 | −24 Vdc – Activation de la LED d'état du Backlight | 
    | 6 | +24 Vdc – Activation du Backlight |
    | 7 | −24 Vdc – Activation du Backlight | 
    | 8 | +24 Vdc – Activation du Flip | 
    | 9 | −24 Vdc – Activation du Flip | 
    | 10 | +24 Vdc – Activation du Blow | 
    | 11 | −24 Vdc – Activation du Blow | 
    | 12–19 | NC | 
    :::
  - Signaux numériques, y compris les activations des LED d'état
:::


---

(cavo-alim)=
## Câble d'alimentation

**Description.** Câble d'alimentation secteur, à raccorder au connecteur **POWER SUPPLY** du panneau électrique standard (FlexiBowl® 500 – 1200) ou du rack (FlexiBowl® 200 / 350). Procédure de raccordement : {ref}`pannello-standard` · {ref}`rack-esterno`.

:::{list-table}
:widths: 30 70
:stub-columns: 1

* - Prérequis
  - Aucun. Appareil éteint, raccordement à la terre obligatoire. Le connecteur loge 2 fusibles de protection.
* - Tailles compatibles
  - Toutes les tailles de FlexiBowl®
* - Tension admise
  - 120–230 Vac, 50/60 Hz ({ref}`dati_elettrici`)
* - Longueurs disponibles
  - · 3 m
    · 5 m
    · 10 m
:::

| Étiquette (côté FlexiBowl®) | Type | Couleur |
|---|---|---|
| L1 | Phase | Marron |
| N1 | Neutre | Bleu |
| PE1 | Terre | Jaune/Vert |

:::{attention}
Raccorder l'alimentation **en dernier**, le FlexiBowl® étant éteint. Le raccordement à la terre est obligatoire et doit être vérifié avant chaque mise sous tension.
:::


---

(cavo-eth)=
## Câble Ethernet

**Description.** Câble pour la liaison Ethernet du FlexiBowl® avec le système (connecteur **C-ETH** du panneau standard ou **C-ETH IN** du rack). Il permet la communication avec le FlexiBowl®, également accessible via un navigateur web.

:::{list-table}
:widths: 30 70
:stub-columns: 1

* - Prérequis
  - Aucun. Lorsque le FlexiBowl® est alimenté, la liaison Ethernet est **obligatoire** : si elle est absente, la machine passe à l'état **ERROR** (LED Ready/Fault rouge).
* - Tailles compatibles
  - Toutes les tailles de FlexiBowl®
* - Connecteurs
  - Côté FlexiBowl® : M12 codage D
    :::{dropdown} **Brochage M12 codage D et RJ45**
    | Signal | Fonction | Couleur | Broche M12 (côté FlexiBowl®) | Broche RJ45 (côté client) |
    |---|---|---|---|---|
    | TD+ | Transmission de données (+) | Jaune | 1 | 1 |
    | TD− | Transmission de données (−) | Orange | 3 | 2 |
    | RD+ | Réception de données (+) | Blanc | 2 | 3 |
    | RD− | Réception de données (−) | Bleu | 4 | 6 |

    Les broches RJ45 4, 5, 7 et 8 ne sont pas affectées.
    :::
* - Longueurs disponibles
  - · 3 m
    · 5 m
    · 10 m
:::
