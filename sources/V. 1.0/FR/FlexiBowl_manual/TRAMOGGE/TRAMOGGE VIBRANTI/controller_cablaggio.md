# **Contrôleur et câblage**

Pendant son fonctionnement, la machine ne nécessite pas la présence continue d'un opérateur.

:::{attention}
Utiliser la machine à une fin autre que celle prévue par le Constructeur pourrait causer de graves dommages aux personnes et/ou aux biens et/ou aux animaux. La société ARS S.r.l. décline toute responsabilité pour les dommages causés par un usage inapproprié de la machine.
:::

## Description du contrôleur

Le **contrôleur numérique** (mod. SDVC34-XLRH) est un contrôleur à fréquence variable équipé d'un microprocesseur, d'un afficheur **LED** et d'un clavier de commande (boutons **Vol+/Vol-** pour la tension de sortie, boutons **▲/▼** pour les paramètres, touche **FUNC** pour la sélection, touche **ON/OFF** pour la mise sous/hors tension et le verrouillage du clavier).

**Par défaut, le contrôleur ne génère aucune sortie à la mise sous tension** et reste à l'état d'arrêt : pour activer la sortie principale, il faut appliquer un **signal PNP** sur l'**Enable Output Port** (connecteur 4 broches).

Le contrôleur intègre des protections automatiques :

- **Court-circuit** → arrêt immédiat de la sortie, erreur `Err01`
- **Surintensité** → arrêt immédiat de la sortie, erreur `Err02`
- **Surtempérature** → arrêt de la sortie au-delà de 65 °C, réarmement automatique en dessous de 60 °C, erreur `Err03`

La communication s'effectue via le port **RS485** (protocole **Modbus**), avec une adresse réseau réglable de 1 à 31 et un débit en bauds configurable.


### Données techniques du contrôleur

| Caractéristique technique | Min | Typique | Max | Unité | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Tension d'entrée** | 85 | 220 | 250 | V | AC RMS |
| **Plage de tension de sortie réglable** | 0 | — | 260 | V | Inférieure à 150 % de la tension d'entrée |
| **Précision de régulation de la tension** | — | 1 | — | V | — |
| **Précision de régulation de la tension (ΔVout/ΔVin)** | 0 | — | 10 | % | ΔVout/ΔVin |
| **Plage de courant de sortie réglable** | 0 | — | 6 | A | — |
| **Puissance de sortie** | 0 | — | 1320 | VA | — |
| **Fréquence de sortie** | 30,0 | — | 130,0 | Hz | — |
| **Précision de régulation de la fréquence** | — | 0,1 | — | Hz | — |
| **Forme d'onde de sortie** | — | Sinusoïdale | — | — | — |
| **Température de déclenchement de la protection contre la surtempérature** | 60 | 65 | 65 | °C | — |
| **Communication numérique** | — | ModBus 485 | — | — | — |
| **Méthode de réglage** | — | 6 | — | Boutons | — |
| **Consommation en veille** | — | 7 | — | W | — |
| **Méthode d'affichage** | — | 5 | — | Chiffres | LED |
| **Température ambiante** | 0 | 25 | 40 | °C | Sans condensation |
| **Humidité ambiante** | 10 | 60 | 85 | % | Sans condensation |
| **Température ambiante de stockage** | -20 | 25 | 65 | °C | Sans condensation |

:::{attention}
Il est possible d'intégrer des contrôleurs autres que celui fourni par le Constructeur, à condition que ce dernier en ait préalablement validé les caractéristiques techniques. La société ARS s.r.l. décline toute responsabilité pour les dommages causés par l'utilisation d'un contrôleur non validé ou non compatible avec la machine.
:::

#### Commandes du panneau avant

```{image} ../../../../../_shared/media/images/controller_digitale_pannello.jpeg
:alt: Panneau avant du contrôleur numérique CUH SDVC34-XLRH
:width: 90%
:align: center
```

| Élément | Fonction |
|---|---|
| **Afficheur LED** | Affiche le paramètre courant et sa valeur |
| **Indicateur Saturated** | Signale la saturation du signal de sortie |
| **Indicateur Remote** | Signale que la commande à distance est active |
| **Indicateurs Speed A / Speed B** | Signalent la vitesse/sortie active |
| **Indicateur Stop** | Signale l'état d'arrêt |
| **Boutons Vol+ / Vol-** | Règlent les **Paramètres communs** (voir ci-dessous), à tout moment |
| **Bouton FUNC** | Entrée/sortie et navigation dans les **Paramètres de base** |
| **Boutons ▲ / ▼** | Incrémentent/décrémentent la valeur du paramètre sélectionné |
| **Indicateurs Auto / Sync / Sensor / Sync Signal / Communicate** | État du fonctionnement et de la communication RS485 |
| **Bouton ON/OFF** | Mise sous/hors tension du contrôleur |

#### Connecteurs arrière

```{image} ../../../../../_shared/media/images/controller_digitale_connettori.png
:alt: Panneau de connecteurs arrière du contrôleur numérique
:width: 85%
:align: center
```

```{list-table}
:widths: 30 45 25
:header-rows: 1

* - Connecteur
  - Fonction
  - Pinout
* - **Mains Power** (alimentation)
  - Alimentation secteur
  - <details class="ars-dropdown"><summary>Brochage du connecteur</summary><div class="ars-dropdown-body">

    | Broche | Description |
    |---|---|
    | PE-PE | ⏚ Terre |
    | 1 | L |
    | 2 | N |
    | 3 | NC |

    </div></details>
* - **Enable Output Port** (4 broches)
  - Sortie d'activation pour la commande externe du Bulk Feeder, utilisée lorsque celui-ci est acheté séparément et doit être piloté par un dispositif externe. Câble disponible en option : {ref}`cavo-input`.
  - <details class="ars-dropdown"><summary>Brochage du connecteur à 4 broches</summary><div class="ars-dropdown-body">

    | Broche | Description |
    |---|---|
    | 1 | +24V |
    | 2 | NC |
    | 3 | GND |
    | 4 | Entrée |

    </div></details>
* - **RS485 Port** (2× 5 broches)
  - Deux connecteurs RS485 identiques : l'un relie le contrôleur au FlexiBowl®, l'autre permet le raccordement en **daisy chain** de plusieurs Bulk Feeder. Câble disponible en option : {ref}`cavo-modbus`.
    
    :::{important}
    Dans une configuration à Bulk Feeder unique, le connecteur non utilisé doit être fermé avec le **bouchon de terminaison** fourni, doté d'une résistance de **120 Ω** entre A+ et B-
    :::
  
  - <details class="ars-dropdown"><summary>Brochage du connecteur à 5 broches</summary><div class="ars-dropdown-body">

    | Broche | Description |
    |---|---|
    | 1 | A+ |
    | 2 | NC |
    | 3 | B- |
    | 4 | GND |
    | 5 | NC |

    </div></details>
* - **Power Output to Feeder** (sortie vers le Bulk Feeder)
  - Alimentation vers le Bulk Feeder
  - <details class="ars-dropdown"><summary>Brochage du connecteur</summary><div class="ars-dropdown-body">

    | Broche | Description |
    |---|---|
    | PE-PE | ⏚ Terre |
    | 1 | Sortie |
    | 2 | Sortie |
    | 3 | NC |

    </div></details>
* - **Power Switch**
  - Interrupteur marche/arrêt
  - —
```

## Procédures d'utilisation

### Vérifications préliminaires

Avant de procéder à la mise en service de la machine, il faut effectuer les vérifications suivantes :

<div class="isw-symbol-grid">
  <div class="isw-symbol-item">
    <div>
      <div class="isw-symbol-label">Stabilité</div>
      <div class="isw-symbol-desc">Vérifiez que la machine est positionnée sur un plan capable de supporter son poids.</div>
    </div>
  </div>
  <div class="isw-symbol-item">
    <div>
       <div class="isw-symbol-label">Sécurité</div>
      <div class="isw-symbol-desc">Vérifiez le fonctionnement des dispositifs de sécurité et assurez-vous que tous les protecteurs ouvrants sont bien fermés.</div>
    </div>
  </div>
  <div class="isw-symbol-item">
    <div>
      <div class="isw-symbol-label">Espace opérationnel</div>
      <div class="isw-symbol-desc"> Vérifiez que l'espace autour de la machine est dégagé de tout encombrement et/ou piège.</div>
    </div>
  </div>
  <div class="isw-symbol-item">
    <div>
     <div class="isw-symbol-label">Alimentation</div>
      <div class="isw-symbol-desc">Vérifiez que la machine a été raccordée au réseau électrique et que les phases d'alimentation sont correctes.</div>
    </div>
  </div>
  <div class="isw-symbol-item">
    <div>
       <div class="isw-symbol-label">Mécanique</div>
      <div class="isw-symbol-desc">Vérifiez que la cuve peut vibrer en toute liberté.</div>
    </div>
  </div>
  <div class="isw-symbol-item">
    <div>
      <div class="isw-symbol-label">État de la machine</div>
      <div class="isw-symbol-desc">Vérifiez que la machine ne se trouve pas à l'état « Maintenance ».</div>
    </div>
  </div>
</div>

### Séquence de raccordement électrique

Quel que soit le type de contrôleur utilisé (standard, analogique ou numérique), le raccordement électrique entre le Bulk Feeder, le contrôleur et le FlexiBowl® suit une séquence précise. La séquence diffère légèrement selon le modèle : les **FlexiBowl® 500/650/800/1200** disposent d'un panneau standard avec connecteur HOPPER intégré, tandis que les **FlexiBowl® 200/350** utilisent un rack externe doté de son propre connecteur HOPPER.

#### FlexiBowl® 500 / 650 / 800 / 1200 — panneau standard

<div style="display: flex; flex-direction: column; gap: 12px; margin: 20px 0;">
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #0f766e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">1</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Raccordez le <strong>contrôleur</strong> au <strong>Bulk Feeder</strong> (base vibrante).
    </div>
    <img src="../../../../../_shared/media/images/connect_Hopper.png" alt="Raccordement du Hopper Controller au Bulk Feeder" style="display:block; width:100%; max-width:500px; margin-top:10px; border-radius:4px;" />
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #0f766e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">2</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Raccordez le <strong>contrôleur</strong> au connecteur <strong>HOPPER</strong> du panneau standard du FlexiBowl®.
    </div>
    <img src="../../../../../_shared/media/images/connect_FB.png" alt="Raccordement du Hopper Controller au Bulk Feeder" style="display:block; width:100%; max-width:500px; margin-top:10px; border-radius:4px;" />
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #0f766e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">3</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Si le connecteur Hopper du FlexiBowl® n'est pas utilisé, mettez en place le <strong>capuchon de terminaison</strong>* prévu.
    </div>
    <img src="../../../../../_shared/media/images/cover_cap.png" alt="Raccordement du Hopper Controller au Bulk Feeder" style="display:block; width:100%; max-width:500px; margin-top:10px; border-radius:4px;" />
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #0f766e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">4</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Branchez le câble d'<strong>alimentation</strong> au contrôleur, en vérifiant que l'interrupteur est en position <strong>OFF</strong>.
    </div>
    <img src="../../../../../_shared/media/images/connect_Supply.png" alt="Raccordement du Hopper Controller au Bulk Feeder" style="display:block; width:100%; max-width:500px; margin-top:10px; border-radius:4px;" />
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #0f766e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">5</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Branchez la fiche du câble d'alimentation à la <strong>prise de courant</strong> uniquement après avoir confirmé que l'interrupteur du contrôleur est sur OFF.
    </div>
  </div>
</div>

:::{attention}
*Le capuchon doit assurer une résistance de **120 Ω** entre les canaux A+ et B-.
:::

:::{important}
Raccordez toujours **d'abord le côté contrôleur** du câble d'alimentation, et n'insérez la fiche dans la prise de courant qu'ensuite.
:::

```{image} ../../../../../_shared/media/images/controller_side.png
:alt: Raccordez toujours d'abord le côté contrôleur
:width: 70%
:align: center
```

```{image} ../../../../../_shared/media/images/power_outlet.png
:alt: Branchement de la fiche à la prise de courant
:width: 70%
:align: center
```

#### **Raccordement en cascade de plusieurs Bulk Feeder**

Sur les modèles avec panneau standard, il est possible de raccorder plusieurs unités Hopper Controller en cascade, en alimentant chaque contrôleur individuellement et en reliant les connecteurs d'une unité à la suivante.

```{image} ../../../../../_shared/media/images/daisy_chain.png
:alt: Raccordement en cascade de plusieurs Hopper Controller
:width: 100%
:align: center
```

#### FlexiBowl® 200 / 350 — panneau rack

<div style="display: flex; flex-direction: column; gap: 12px; margin: 20px 0;">
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #0f766e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">1</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Raccordez le <strong>contrôleur</strong> au <strong>Bulk Feeder</strong> (base vibrante).
    </div>
    <img src="../../../../../_shared/media/images/connect_Hopper.png" alt="Raccordement du Hopper Controller au Bulk Feeder" style="display:block; width:100%; max-width:500px; margin-top:10px; border-radius:4px;" />
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #0f766e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">2</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Raccordez le <strong>contrôleur</strong> au connecteur <strong>HOPPER</strong> du panneau du <strong>rack</strong>.
    </div>
    <img src="../../../../../_shared/media/images/controller_Rack.png" alt="Raccordement du Hopper Controller au Bulk Feeder" style="display:block; width:100%; max-width:500px; margin-top:10px; border-radius:4px;" />
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #0f766e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">3</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Si le connecteur Hopper du rack n'est pas utilisé, mettez en place le <strong>capuchon de terminaison</strong>* prévu.
    </div>
    <img src="../../../../../_shared/media/images/cover_cap.png" alt="Raccordement du Hopper Controller au Bulk Feeder" style="display:block; width:100%; max-width:500px; margin-top:10px; border-radius:4px;" />
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #0f766e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">4</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Branchez le câble d'<strong>alimentation</strong> au contrôleur, en vérifiant que l'interrupteur est en position <strong>OFF</strong>.
    </div>
    <img src="../../../../../_shared/media/images/connect_Supply.png" alt="Raccordement du Hopper Controller au Bulk Feeder" style="display:block; width:100%; max-width:500px; margin-top:10px; border-radius:4px;" />
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #0f766e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">5</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Branchez la fiche du câble d'alimentation à la <strong>prise de courant</strong> uniquement après avoir confirmé que l'interrupteur du contrôleur est sur OFF.
    </div>
  </div>
</div>

:::{attention}
*Le capuchon doit assurer une résistance de **120 Ω** entre les canaux A+ et B-.
:::

:::{important}
Raccordez toujours **d'abord le côté contrôleur** du câble d'alimentation, et n'insérez la fiche dans la prise de courant qu'ensuite.
:::

```{image} ../../../../../_shared/media/images/controller_side.png
:alt: Raccordez toujours d'abord le côté contrôleur
:width: 70%
:align: center
```

```{image} ../../../../../_shared/media/images/power_outlet.png
:alt: Branchement de la fiche à la prise de courant
:width: 70%
:align: center
```

:::{note}
Alimentation standard du contrôleur : **115 Vac** ou **230 Vac ±5 %**. Vérifiez toujours que le conducteur de terre est correctement installé et intact avant de mettre le système sous tension.
:::

---

#### Réglage de l'adresse de communication

Une fois le câblage électrique terminé, l'étape suivante consiste à définir une **adresse de communication unique** sur chaque contrôleur, via le paramètre **Communication Address** (`r`).

:::{note}
Le paramètre `r` représente l'**ID du contrôleur** sur le réseau de communication **RS485**. Lorsque plusieurs contrôleurs sont raccordés au même réseau (p. ex. plusieurs Bulk Feeder), il est **obligatoire** d'attribuer à chacun une adresse différente, dans la plage **1–31**, afin de pouvoir les distinguer et les commander individuellement.
:::

<div style="display: flex; flex-direction: column; gap: 12px; margin: 20px 0;">
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #7c3aed; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">1</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Maintenez <strong>FUNC</strong> enfoncé pendant 2 secondes pour entrer dans le mode de réglage des Paramètres de base.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #7c3aed; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">2</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Appuyez plusieurs fois sur <strong>FUNC</strong> pour faire défiler jusqu'au paramètre <code>r</code>.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #7c3aed; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">3</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Appuyez sur <strong>▲</strong> ou <strong>▼</strong> pour modifier la valeur (1–31).
    </div>
  </div>
</div>

---

#### Interface logicielle Hopper

Une fois l'adresse unique attribuée à chaque contrôleur, les Bulk Feeder sont **intégrés au logiciel FlexiBowl®** et peuvent être commandés directement depuis son interface, sans avoir besoin d'agir manuellement sur chaque contrôleur.

```{image} ../../../../../_shared/media/images/hopper.png
:alt: Interface logicielle FlexiBowl — gestion des Bulk Feeder (Hopper 1–4)
:width: 100%
:align: center
```

Depuis l'interface logicielle, il est possible, pour chaque Bulk Feeder connecté, de :

| Champ | Fonction |
|---|---|
| **ID** | Adresse de communication du contrôleur (doit correspondre à celle définie manuellement) |
| **ENABLE** | Active le Bulk Feeder pour le fonctionnement |
| **Set New ID** | Attribue une nouvelle adresse de communication depuis le logiciel |
| **STATUS** | État actuel du Bulk Feeder (p. ex. Disabled) |
| **Amplitude** | Amplitude de vibration |
| **Frequency** | Fréquence de vibration |
| **Activation Time** | Temps d'activation du Bulk Feeder (ms) |
| **Start Hopper** | Démarre manuellement le Bulk Feeder |

:::{note}
Tous les réglages disponibles via l'interface logicielle peuvent également être effectués **directement depuis le contrôleur**, au moyen des Paramètres communs et de base décrits ci-dessous.
:::

---
#### Paramètres communs

Les **Paramètres communs** peuvent être réglés à tout moment avec les boutons **Vol+ / Vol-**, même lorsqu'un autre paramètre est affiché : à la fin du réglage, le contrôleur revient automatiquement à l'affichage du paramètre précédent.

```{image} ../../../../../_shared/media/images/controller_changing_common_parameters.png
:alt: Contrôleur numérique — réglage des Paramètres communs avec Vol+/Vol-
:width: 50%
:align: center
```

| Définition | Symbole | Plage | Par défaut |
|---|---|---|---|
| Output Voltage (tension de sortie) | `U` | 0–260 (V) | 50 |

#### Paramètres de base

<div style="display: flex; flex-direction: column; gap: 12px; margin: 20px 0;">
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #34495e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">1</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Maintenez <strong>FUNC</strong> enfoncé pendant 2 secondes pour entrer dans le mode de réglage des Paramètres de base.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #34495e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">2</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Appuyez plusieurs fois sur <strong>FUNC</strong> pour faire défiler cycliquement les différents paramètres.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #34495e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">3</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Appuyez sur <strong>▲</strong> ou <strong>▼</strong> pour modifier la valeur du paramètre.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #34495e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">4</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Maintenez à nouveau <strong>FUNC</strong> enfoncé pendant 2 secondes pour quitter le mode de réglage des Paramètres de base.
      <img src="../../../../../_shared/media/images/controller_changing_basic_parameters.png" alt="Contrôleur numérique — procédure de réglage des Paramètres de base" style="display:block; width:60%; max-width:500px; margin-top:10px; border-radius:4px;" />
    </div>
  </div>
</div>

| Définition | Symbole | Plage | Par défaut |
|---|---|---|---|
| Output Frequency (fréquence de sortie) | `E` | 40,0–200,0 (Hz) | 100,0 |
| Max Adjustable Output Voltage (tension maximale réglable) | `h` | 0–260 (V) | 260 |
| Communication Address (adresse RS485) | `r` | 1–31 | 1 |
| Communication Baud Rate (vitesse de communication) | `c` | 0,3–115,2 kbit/s | 115,2 |
| Controller Reset | `88888` | — | — |

#### Procédure de Controller Reset

<div style="display: flex; flex-direction: column; gap: 12px; margin: 20px 0;">
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #7c3aed; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">1</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Maintenez <strong>FUNC</strong> enfoncé pendant 2 secondes pour entrer dans le mode de réglage des Paramètres de base.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #7c3aed; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">2</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Appuyez sur <strong>FUNC</strong> jusqu'à ce que le paramètre <code>88888</code> clignote sur l'afficheur.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #7c3aed; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">3</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Maintenez <strong>▲</strong> enfoncé jusqu'à ce que l'afficheur indique <code>-----</code> (« Ready to restore »).
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #7c3aed; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">4</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Relâchez <strong>▲</strong> pour terminer la réinitialisation (« Restore successfully ») : l'afficheur indique <code>U 50</code> pour confirmer que la restauration a été effectuée.
      <img src="../../../../../_shared/media/images/controller_reset_procedure.png" alt="Contrôleur numérique — séquence de réinitialisation, de Ready to restore à Restore successfully" style="display:block; width:100%; max-width:700px; margin-top:10px; border-radius:4px;" />
    </div>
  </div>
</div>

:::{warning}
Le **Controller Reset** ramène tous les Paramètres communs et de base à leurs valeurs par défaut (Output Voltage 50, Output Frequency 100,0 Hz, Max Output Voltage 260, Communication Address 1, Baud Rate 115,2 kbit/s). L'utiliser avec prudence si des configurations personnalisées sont présentes — en particulier l'adresse de communication, qui devra être redéfinie.
:::


---

## **Mise en service du Bulk Feeder**

:::{important}
- Si le système inclut **FlexiVision One**, la configuration des paramètres du Bulk Feeder est guidée dans la section [Configuration du Bulk Feeder]().
- Sinon, reportez-vous à la section [Hopper](hopper) de ce manuel.
:::

