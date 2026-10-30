# **Sequence**

## Présentation

La page **Sequence** permet de créer, modifier et gérer des séquences opérationnelles personnalisées pour le FlexiBowl®. Une séquence est une liste ordonnée de commandes que le système exécute en succession automatique, en combinant des mouvements de rotation (MOVE), d'oscillation (SHAKE), de flip et de soufflage.

---

## Structure de l'interface
![page sequence](../../../../_shared/media/images/sequence.png)

La page est organisée en quatre zones principales :

| N° | Zone | Position | Description |
|---|---|---|---|
| 1 | [**Sélection de la séquence**](seq) | En haut à gauche | Menu déroulant pour sélectionner la séquence active |
| 2 | [**Emptying Sequence**](empty) | En haut au centre | Interrupteur pour activer le mode de vidage |
| 3 | [**Panneau des paramètres**](param) | Gauche | Paramètres MOVE, SHAKE et OPTION ; ajout de commandes à la séquence |
| 4 | [**Panneau des commandes**](comm) | Droite | Liste ordonnée des commandes de la séquence active et outils de gestion |

---
(seq)=
## 1. Sélection de la séquence

:::{important}
**Avant toute opération**, sélectionner la séquence à modifier au moyen du menu déroulant **« Select the sequence »** en haut à gauche.
:::

![select the sequence](../../../../_shared/media/images/sequence_combo_box.png)

Le système prend en charge jusqu'à **20 séquences indépendantes** (SEQUENCE 1 – SEQUENCE 20), chacune avec sa propre liste de commandes et ses paramètres indépendants. La séquence sélectionnée devient la séquence active sur laquelle portent toutes les modifications suivantes.

---
(empty)=
## 2. Emptying Sequence

![panneau des commandes](../../../../_shared/media/images/empty_sequence.png)

L'interrupteur **Emptying Sequence** (en haut au centre) active un mode dans lequel la séquence est exécutée dans le but de vider le FlexiBowl® des composants présents. Il est utilisé lorsque l'option de vidage a été achetée.
Pour plus d'informations sur l'option de vidage, consulter la [page dédiée](svuotamento).

---
(param)=
## 3. Panneau des paramètres

### Paramètres MOVE

| Paramètre | Valeur d'exemple | Description |
|---|---|---|
| **Acceleration Move** | 50 % | Rampe d'accélération pour le mouvement de rotation |
| **Deceleration Move** | 50 % | Rampe de décélération pour le mouvement de rotation |
| **Speed Move** | 35 % | Vitesse de rotation du FlexiBowl® |
| **Angle Move** | 360 degrés | Angle de rotation parcouru pendant la commande MOVE |

### Paramètres SHAKE

| Paramètre | Valeur d'exemple | Description |
|---|---|---|
| **Acceleration Shake** | 50 % | Rampe d'accélération pendant le shake |
| **Deceleration Shake** | 50 % | Rampe de décélération pendant le shake |
| **Speed Shake** | 50 % | Vitesse de rotation pendant le shake |
| **Ccw Angle Shake** | -45 degrés | Angle de rotation antihoraire pendant chaque oscillation |
| **Cw Angle Shake** | -30 degrés | Angle de rotation horaire pendant chaque oscillation |
| **Count Shake** | 2 N° | Nombre d'oscillations complètes par cycle de shake |

### Paramètres OPTION (flip et blow)

| Paramètre | Valeur d'exemple | Description |
|---|---|---|
| **Flip Pressure** | 5,00 Bar | Pression d'air pour l'actionnement du flip |
| **Flip Count** | 4 N° | Nombre de flips exécutés par cycle |
| **Flip Delay** | 100 ms | Intervalle entre un flip et le suivant |
| **Blow Pressure** | 5,00 Bar | Pression d'air pour le soufflage |
| **Blow Time** | 200 ms | Durée de l'impulsion de soufflage |

:::{note}
Les paramètres affichés dans le panneau de gauche s'appliquent aux commandes de la séquence. Avant d'ajouter une commande avec **ADD**, vérifier que les valeurs sont correctes : les paramètres sont associés à la commande au moment de l'insertion.
:::

---
(comm)=
## 4. Panneau des commandes
### Sélection et ajout d'une commande

![panneau des commandes](../../../../_shared/media/images/pannello_comandi_sequence.png)

Le panneau central supérieur contient :

- Le menu déroulant **« Command Available »** : il permet de sélectionner le type de commande à ajouter à la séquence.
- Le bouton **ADD** (flèche →) : il ajoute la commande sélectionnée à la fin de la liste des commandes actives.

Les commandes disponibles sont :

| Commande | Description |
|---|---|
| `FLB_NULL` | Commande nulle, aucune action exécutée |
| `FLB_MOVE` | Rotation du FlexiBowl® selon les paramètres MOVE |
| `FLB_MOVE_FLIP` | Rotation combinée avec le flip (retournement) du plateau |
| `FLB_MOVE_BLOWe` | Rotation combinée avec le soufflage externe |
| `FLB_MOVE_BLOWc` | Rotation combinée avec le soufflage central |
| `FLB_MOVE_BLOWce` | Rotation combinée avec le soufflage central et externe |
| `FLB_MOVE_BLOWe_FLIP` | Rotation, soufflage externe et flip combinés |
| `FLB_MOVE_BLOWc_FLIP` | Rotation, soufflage central et flip combinés |
| `FLB_MOVE_BLOWce_FLIP` | Rotation, soufflage central et externe et flip combinés |
| `FLB_SHAKE` | Secouage du plateau sans rotation |
| `FLB_BLOWe` | Soufflage externe, sans rotation |
| `FLB_BLOWc` | Soufflage central, sans rotation |
| `FLB_BLOWce` | Soufflage central et externe, sans rotation |
| `FLB_FLIP` | Flip (retournement) du plateau, sans rotation |
| `FLB_PAUSE_100ms` | Pause de 100 millisecondes |
| `FLB_PAUSE_200ms` | Pause de 200 millisecondes |
| `FLB_PAUSE_500ms` | Pause de 500 millisecondes |
| `FLB_LIGHT_1_ON` | Allumage de la lumière 1 |
| `FLB_LIGHT_1_OFF` | Extinction de la lumière 1 |
| `FLB_LIGHT_2_ON` | Allumage de la lumière 2 |
| `FLB_LIGHT_2_OFF` | Extinction de la lumière 2 |
| `FLB_ENABLE` | Activation du FlexiBowl® |
| `FLB_DISABLE` | Désactivation du FlexiBowl® |
| `FLB_BARRIER_DOWN` | Abaissement de la barrière |
| `FLB_BARRIER_UP` | Relevage de la barrière |

:::{tip}
Sélectionner la commande souhaitée dans le menu déroulant avant d'appuyer sur **ADD**. La commande sera insérée dans la première ligne libre de la liste **Command Active**.
:::

Le tableau **Command Active** affiche la séquence de commandes dans l'ordre d'exécution, numérotées de 1 à 10.

Dans l'exemple affiché, la séquence ne contient qu'une seule commande :

| N° | Commande |
|---|---|
| 1 | FLB_MOVE |
| 2–10 | *(vide)* |

### Outils de gestion de la liste

| Bouton | Fonction |
|---|---|
| **DELETE** | Supprime la commande sélectionnée de la liste |
| **UP** | Déplace la commande sélectionnée d'une position vers le haut |
| **DOWN** | Déplace la commande sélectionnée d'une position vers le bas |
| **CLEAR** | Supprime toutes les commandes présentes dans la liste |

:::{warning}
Le bouton **CLEAR** supprime **toutes** les commandes de la séquence sans possibilité de récupération. L'utiliser avec précaution.
:::

---

## 5. Exécution de la séquence

Deux boutons d'exécution se trouvent en bas à droite :

| Bouton | Champ adjacent | Fonction |
|---|---|---|
| **TEST SEQUENCE** | Temps d'exécution (ms) | Exécute la séquence une seule fois. Le champ de droite affiche la durée totale de la dernière exécution, en millisecondes |
| **RUN** | — | Démarre la séquence en mode opérationnel continu (boucle), en attente des déclenchements du système de vision |

:::{note}
Le champ **ms** à côté de **TEST SEQUENCE** indique le temps total d'exécution de la séquence complète. Dans l'exemple affiché, la valeur est de **1140 ms**. Cette donnée est utile pour la synchronisation avec le système de vision artificielle.
:::

:::{important}
Avant d'appuyer sur **RUN**, vérifier que :
- le moteur est activé (**ENABLE MOTOR** actif)
- l'état du système est **READY**
- la séquence contient au moins une commande valide dans la liste **Command Active**
:::
