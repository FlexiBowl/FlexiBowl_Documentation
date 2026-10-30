
# **Main Command**

## Présentation

La page **Main Command** est la section opérationnelle principale de l'interface logicielle FlexiBowl®. Elle permet à l'opérateur de configurer et de tester les paramètres de mouvement et des options accessoires du système.

La page est divisée en **trois sous-pages**, sélectionnables via le menu déroulant central situé sous la barre de navigation, intitulé **« Chose Visualization Page »** :

| Sous-page | Description succincte |
|---|---|
| **OPTION** | Paramètres pour le flip, le blow et le rétroéclairage |
| **MOVE** | Paramètres du mouvement rotatif du FlexiBowl® |
| **SHAKE** | Paramètres du mouvement oscillatoire du FlexiBowl® |

---

## Sous-page : OPTION

La sous-page **OPTION** regroupe les paramètres relatifs aux fonctions accessoires du FlexiBowl® : le système de retournement des composants (flip), le système de soufflage (blow) et le rétroéclairage (backlight).
![page option](../../../../_shared/media/images/main_command_option.png)

| Paramètre | Unité | Description |
|---|---|---|
| **Flip Pressure** | Bar  | Pression d'air utilisée pour l'actionnement du flip. Réglable au moyen d'un curseur |
| **Flip Count** | N°  | Nombre de flips exécutés en séquence pendant un cycle |
| **Flip Delay** | ms  | Intervalle de temps entre un flip et le suivant |
| **Blow Pressure** | Bar  | Pression d'air utilisée pour le soufflage des composants sur le FlexiBowl® |
| **Blow Time** | ms  | Durée de l'impulsion de soufflage |

Chaque paramètre est réglable au moyen d'un **curseur horizontal** ; la valeur courante est affichée dans la case numérique à droite du curseur.

### Commandes du rétroéclairage

| Commande | Description |
|---|---|
| **Backlight_1** | Interrupteur on/off pour le rétroéclairage 1  |
| **Backlight_2** | Interrupteur on/off pour le rétroéclairage 2  |

Les interrupteurs s'affichent en rouge lorsque le rétroéclairage est **actif**.

### Boutons de test

En bas de la page se trouvent trois boutons permettant de tester les fonctions en temps réel :

| Bouton | Fonction |
|---|---|
| **TEST FLIP** | Exécute un flip avec les paramètres actuellement définis |
| **TEST BLOWe** | Active le soufflage externe (blow externe) avec les paramètres définis |
| **TEST BLOWc** | Active le soufflage central (blow central) avec les paramètres définis |

:::{attention}  
 Avant d'exécuter les tests, s'assurer que le moteur est activé (bouton **ENABLE MOTOR** actif) et que l'état du système est **READY**.
:::

---

## Sous-page : MOVE

La sous-page **MOVE** permet de configurer les paramètres du mouvement rotatif du FlexiBowl® et de le tester directement depuis l'interface.
![page move](../../../../_shared/media/images/main_command_move.png)

| Paramètre | Unité | Valeur par défaut | Description |
|---|---|---|---|
| **Acceleration** | % | 50 | Rampe d'accélération du moteur au démarrage du mouvement. Des valeurs plus élevées produisent un départ plus brusque |
| **Deceleration** | % | 50 | Rampe de décélération du moteur à l'arrêt. Des valeurs plus élevées produisent un arrêt plus brusque |
| **Speed** | % | 50 | Vitesse de rotation du FlexiBowl® pendant le mouvement |
| **Angle** | Degré | 45 | Angle de rotation parcouru par le FlexiBowl® pendant chaque mouvement |

Chaque paramètre est réglable au moyen d'un **curseur horizontal** ; la valeur courante est affichée dans la case numérique à droite du curseur.

### Bouton de test

| Bouton | Champ adjacent | Fonction |
|---|---|---|
| **TEST MOVE** | Temps d'exécution (ms) | Exécute un mouvement de rotation avec les paramètres actuellement définis. Le champ de droite affiche la durée effective du dernier mouvement exécuté, en millisecondes |

:::{note}  
 Le champ **ms** affiche le temps réel mis par le bowl pour achever le mouvement défini. Cette valeur est utile pour synchroniser le FlexiBowl® avec le système de vision industrielle.
:::

:::{attention}   
Avant d'exécuter le test, s'assurer que le moteur est activé (bouton **ENABLE MOTOR** actif) et que l'état du système est **READY**.
:::

---

## Sous-page : SHAKE

La sous-page **SHAKE** permet de configurer les paramètres du mouvement oscillatoire du FlexiBowl® (shake), utilisé pour redistribuer les composants sur le plateau, et de le tester directement depuis l'interface.
![page shake](../../../../_shared/media/images/main_command_shake.png)

| Paramètre | Unité | Valeur par défaut | Description |
|---|---|---|---|
| **Acceleration** | % | 50 | Rampe d'accélération du moteur pendant la phase de shake |
| **Deceleration** | % | 50 | Rampe de décélération du moteur pendant la phase de shake |
| **Speed** | % | 50 | Vitesse de rotation pendant le mouvement de shake |
| **Ccw Angle** | Degré | -45 | Angle de rotation dans le sens **antihoraire** (Counter-ClockWise) pendant chaque oscillation |
| **Cw Angle** | Degré | 45 | Angle de rotation dans le sens **horaire** (ClockWise) pendant chaque oscillation |
| **Count** | N° | 2 | Nombre d'oscillations complètes exécutées pendant un cycle de shake |

Chaque paramètre est réglable au moyen d'un **curseur horizontal** ; la valeur courante est affichée dans la case numérique à droite du curseur.

:::{note}  
 Le mouvement de **shake** consiste en une série de rotations alternées dans le sens horaire et antihoraire, définies respectivement par **Cw Angle** et **Ccw Angle**. Le nombre d'oscillations complètes est contrôlé par le paramètre **Count**.
:::

### Bouton de test

| Bouton | Champ adjacent | Fonction |
|---|---|---|
| **TEST SHAKE** | Temps d'exécution (ms) | Exécute un cycle de shake avec les paramètres actuellement définis. Le champ de droite affiche la durée effective du dernier shake exécuté, en millisecondes |

:::{attention}  
 Avant d'exécuter le test, s'assurer que le moteur est activé (bouton **ENABLE MOTOR** actif) et que l'état du système est **READY**.
:::