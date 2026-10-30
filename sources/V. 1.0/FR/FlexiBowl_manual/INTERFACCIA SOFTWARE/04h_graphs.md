# **Graphs**

## Présentation

La page **Graphs** fournit un tableau de bord de surveillance en temps réel des grandeurs électriques et thermiques du driver moteur du FlexiBowl®. Sur cette page, l'opérateur peut vérifier les performances du système et détecter d'éventuelles anomalies pendant le fonctionnement.

![page d'accueil](../../../../_shared/media/images/pagina_Graphs.png)

---

## Barre des compteurs et des indicateurs

La partie supérieure de la page regroupe les principaux paramètres d'état du système, répartis en trois colonnes.

### Colonne de gauche

| Champ | Valeur d'exemple | Description |
|---|---|---|
| **Timer Global** | 30 d: 0 h: 14 min: 48 s | Temps total de mise sous tension du système depuis la dernière réinitialisation du compteur global |
| **Drive Temperature** | 45.2 °C | Température actuelle du driver moteur |
| **DC Voltage** | 48.4 V | Tension du bus DC qui alimente le driver moteur |

### Colonne centrale

| Champ | Valeur d'exemple | Description |
|---|---|---|
| **Timer Run** | 4 d: 14 h: 8 min: 34 s | Temps total de fonctionnement du moteur (temps effectif de mouvement) depuis la dernière réinitialisation |
| **Dsp Temperature** | 50.7 °C | Température du processeur DSP interne au driver |
| **Total Revolutions** | 127023 | Nombre total de tours effectués par le FlexiBowl® depuis la dernière réinitialisation du compteur |

### Colonne de droite

| Champ | Valeur d'exemple | Description |
|---|---|---|
| **Utilization** | 15 % | Pourcentage d'utilisation actuel du moteur par rapport à la capacité maximale. Affiché au moyen d'une barre de progression accompagnée de la valeur en pourcentage en texte coloré |
| **Max Drive Temperature** | 45.7 °C | Température maximale atteinte par le driver moteur depuis la dernière réinitialisation |
| **Max Dsp Temperature** | 51.1 °C | Température maximale atteinte par le DSP depuis la dernière réinitialisation |

### ECO LOAD %

L'indicateur à aiguille **ECO LOAD %** en haut à droite indique la charge moyenne du moteur en pourcentage. La valeur affichée dans l'exemple est de **9,1 %**, ce qui indique une faible charge — condition typique d'un système avec des cycles de travail courts ou des vitesses peu élevées.

:::{tip}
La valeur **ECO LOAD %** est un indicateur utile pour évaluer l'efficacité opérationnelle du système dans le temps. Des valeurs constamment élevées peuvent indiquer une surcharge mécanique ou des paramètres de vitesse trop agressifs.
:::

---

## Graphiques en temps réel

La partie inférieure de la page affiche trois graphiques de type oscilloscope qui tracent l'évolution dans le temps des grandeurs du moteur. L'axe horizontal indique le temps écoulé depuis le démarrage, au format `Xh Ym Zs` (les champs égaux à zéro, comme les heures, peuvent ne pas être affichés — par ex. `33m46s`).

### Velocity Motor %

Graphique de la **vitesse du moteur** exprimée en pourcentage de la vitesse maximale.

| Axe | Description |
|---|---|
| **Y** | Vitesse en **pourcentage** de la vitesse maximale, avec signe : les valeurs **négatives** indiquent une rotation **antihoraire**, les valeurs **positives** une rotation **horaire**. La valeur **0** correspond au moteur à l'arrêt |
| **X** | Temps d'exécution |

:::{note}
Une valeur de vitesse négative indique une rotation **antihoraire** ; une valeur positive indique une rotation **horaire**. Cela est cohérent avec le paramètre **Speed** de la page Jog Motor.
:::

### Current Motor %

Graphique du **courant absorbé par le moteur** exprimé en pourcentage du courant nominal maximal.

| Axe | Description |
|---|---|
| **Y** | Courant normalisé en pourcentage. Il peut prendre des valeurs aussi bien **positives** que **négatives** selon la phase de fonctionnement (par ex. accélération/décélération) ; les pics correspondent aux variations de vitesse les plus brusques |
| **X** | Temps d'exécution |

:::{tip}
Des pics de courant élevés et récurrents peuvent indiquer des rampes d'accélération trop agressives. Dans ce cas, augmenter les valeurs d'**Acceleration** et de **Deceleration** pour répartir l'effort sur un intervalle de temps plus long.
:::

### Torque Motor %

Graphique du **couple fourni par le moteur** exprimé en pourcentage du couple nominal maximal.

| Axe | Description |
|---|---|
| **Y** | Couple normalisé en pourcentage. Comme pour le courant, il peut prendre des valeurs aussi bien **positives** que **négatives** selon la phase de mouvement |
| **X** | Temps d'exécution |

:::{note}
Les graphiques **Current Motor %** et **Torque Motor %** montrent généralement une évolution très similaire, car dans un moteur à courant continu le couple est directement proportionnel au courant. Des différences significatives entre les deux peuvent indiquer des anomalies dans le driver.
:::

---

## Notes d'utilisation

:::{warning}
Des valeurs de **Drive Temperature** ou **Dsp Temperature** constamment supérieures à 70 °C peuvent réduire la durée de vie du driver et provoquer des arrêts de protection thermique. Vérifier les conditions de ventilation de l'armoire et le cycle de travail du système.
:::

:::{warning}
Une valeur de **DC Voltage** hors de la plage nominale (typiquement 48 V ± 10 %) peut indiquer des problèmes au niveau de l'alimentation. Interrompre le fonctionnement et contacter le service technique.
:::
