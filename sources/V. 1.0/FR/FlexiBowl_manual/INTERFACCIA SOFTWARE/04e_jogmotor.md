(jog)=
# **Jog Motor**

## Présentation

La page **Jog Motor** permet de piloter le FlexiBowl® en mode manuel continu (jog), sans utiliser de séquences programmées. Elle est principalement utilisée pendant les phases de configuration, de mise en service et de test du système, et permet à l'opérateur de contrôler directement la rotation du FlexiBowl® et les fonctions accessoires.
![page jog motor](../../../../_shared/media/images/jog_motor.png)

---

## Paramètres de mouvement

Les trois curseurs en haut définissent le comportement du moteur pendant le jog.

| Paramètre | Unité | Valeur d'exemple | Description |
|---|---|---|---|
| **Acceleration** | % | 50 | Rampe d'accélération au démarrage du jog |
| **Deceleration** | % | 50 | Rampe de décélération à l'arrêt du jog |
| **Speed** | % | -30 | Vitesse de rotation du FlexiBowl®. Une valeur **négative** indique une rotation **antihoraire** ; une valeur **positive** indique une rotation **horaire** |

:::{tip}
Pour inverser le sens de rotation du FlexiBowl® pendant le jog, il suffit de placer le curseur **Speed** sur une valeur négative. Il n'est pas nécessaire d'arrêter le jog pour modifier le paramètre.
:::

---

## Panneau FLIP

Le panneau **Flip Enable** gère l'activation et les paramètres du système de retournement pendant le jog.

| Commande | Valeur d'exemple | Description |
|---|---|---|
| **Flip Enable** (interrupteur) | Actif (rouge) | Active le flip automatique pendant le jog |
| **Flip Duration** | 200 ms | Durée de l'impulsion d'actionnement du flip |
| **Flip Pression** | 3,00 Bar | Pression d'air utilisée pour le flip |
| **Flip Pause** | 200 ms | Pause entre un flip et le suivant pendant le jog |

:::{note}
Le flip est exécuté de manière cyclique pendant le jog, avec la cadence définie par **Flip Pause**, uniquement si l'interrupteur **Flip Enable** est actif.
:::

---

## Panneau BLOW

Le panneau **Blow Enable** gère l'activation et les paramètres du système de soufflage pendant le jog.

| Commande | Valeur d'exemple | Description |
|---|---|---|
| **Blow Enable** (interrupteur) | Actif (rouge) | Active le soufflage automatique pendant le jog |
| **Blow Duration** | 200 ms | Durée de l'impulsion de soufflage |
| **Blow Pression** | 3,00 Bar | Pression d'air utilisée pour le soufflage |
| **Blow Pause** | 200 ms | Pause entre une impulsion de soufflage et la suivante pendant le jog |
| **Blow Type** | BLOWc + BLOWe | Type de soufflage activé. Les options combinent le soufflage central (BLOWc) et/ou le soufflage externe (BLOWe) |

### Options de Blow Type

| Valeur | Description |
|---|---|
| **BLOWc** | Soufflage central uniquement |
| **BLOWe** | Soufflage externe uniquement |
| **BLOWc + BLOWe** | Les deux soufflages activés simultanément |

---

## Panneau BACKLIGHT

Le panneau **Backlight** gère l'état des rétroéclairages indépendamment du jog.

| Commande | Description |
|---|---|
| **Backlight 1** (interrupteur) | Active/désactive le rétroéclairage 1 |
| **Backlight 2** (interrupteur) | Active/désactive le rétroéclairage 2 |

Les interrupteurs s'affichent en rouge lorsque le rétroéclairage est **actif**.

---

## Démarrage et arrêt du jog

| Bouton | Fonction |
|---|---|
| **START JOG** | Démarre la rotation continue du FlexiBowl® avec les paramètres définis, en activant simultanément flip et blow si les interrupteurs respectifs sont activés |
| **STOP JOG** | Interrompt le jog et arrête le FlexiBowl® |

:::{important}
Avant d'appuyer sur **START JOG**, vérifier que :
- le moteur est activé (**ENABLE MOTOR** actif)
- l'état du système est **READY**
- les paramètres Speed, Flip et Blow sont correctement définis afin d'éviter des mouvements indésirables
:::

:::{warning}
Pendant le jog, le FlexiBowl® tourne en continu. Avant de démarrer le jog, s'assurer que la zone autour du FlexiBowl® est dégagée de tout obstacle et que le personnel n'est pas en contact avec les parties en mouvement.
:::
