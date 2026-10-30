(digIO)=
# **Digital I/O**

La communication avec E/S numériques est une option achetable et ne fait pas partie du FlexiBowl® standard. Le connecteur d'entrée de la nouvelle génération de FlexiBowl® prend en charge des signaux numériques et analogiques pour l'intégration directe avec un automate sans nécessiter de communication Ethernet.

### Entrées disponibles sur le connecteur principal

| Type | Signal | Type électrique | Niveau actif | Description |
|---|---|---|---|---|
| Standard | Bit 1 | Numérique | 0–24Vdc, actif haut | Bit de codage de la commande (voir tableau de codage) |
| Standard | Bit 2 | Numérique | 0–24Vdc, actif haut | Bit de codage de la commande |
| Standard | Bit 3 | Numérique | 0–24Vdc, actif haut | Bit de codage de la commande |
| Standard | Bit 4 | Numérique | 0–24Vdc, actif haut | Bit de codage de la commande |
| Standard | Bit 5 | Numérique | 0–24Vdc, actif haut | Bit de codage de la commande |
| Standard | Latch | Numérique | 0–24Vdc, actif haut | Exécution de la commande (front montant) |
| Standard | Empty Sensor | Numérique | 0–24Vdc, actif haut | Capteur de détection de FlexiBowl® vide |
| Standard | Zeroing | Numérique | 0–24Vdc, actif haut | Prévu pour un capteur de fixation de disque multi-secteurs |
| Option | Retour de l'électrovanne proportionnelle flip | Analogique | 0–10Vdc | Signal de retour de l'électrovanne proportionnelle flip |
| Option | Retour de l'électrovanne proportionnelle blow | Analogique | 0–10Vdc | Signal de retour de l'électrovanne proportionnelle blow |
| Option | Strobe Backlight + / − | — | — | Commande strobe externe du backlight (protection par diode et fusible requise) |
| Option | Strobe Backlight 2+ / 2− | — | — | Commande strobe externe secondaire du backlight |

### Connecteur STO (Safe Torque Off)

Le connecteur STO est dédié à la fonction de sécurité d'arrêt du moteur :

| Broche | Signal | Description |
|---|---|---|
| 1 | STO1+ | Safe Torque Off 1 |
| 2 | STO1- | Retour STO1 |
| 3 | STO2+ | Safe Torque Off 2 |
| 4 | STO2- | Retour STO2 |
| 5 | 24V | Alimentation |
| 6 | 0V | Masse |

### Codage des commandes via bits numériques (Bit 1–5)

Les 5 bits d'entrée numériques forment un mot binaire à 5 chiffres qui identifie la commande à exécuter. La commande est acquise sur le front montant du signal **Latch**.

| Code binaire (Bit5–Bit1) | Commande |
|---|---|
| `00000` | Réinitialisation des alarmes |
| `00001` | Exe Seq 1 |
| `00010` | Exe Seq 2 |
| `00011` | Exe Seq 3 |
| `00100` | Exe Seq 4 |
| `00101` | Exe Seq 5 |
| `00110` | Exe Seq 6 |
| `00111` | Exe Seq 7 |
| `01000` | Exe Seq 8 |
| `01001` | Exe Seq 9 |
| `01010` | Exe Seq 10 |
| `01011` | Exe Seq 11 |
| `01100` | Exe Seq 12 |
| `01101` | Exe Seq 13 |
| `01110` | Exe Seq 14 |
| `01111` | Exe Seq 15 |
| `10000` | Exe Seq 16 |
| `10001` | Exe Seq 17 |
| `10010` | Exe Seq 18 |
| `10011` | Exe Seq 19 |
| `10100` | Exe Seq 20 |
| `10101` | Hopper Activation 1 |
| `10110` | Hopper Activation 2 |
| `10111` | Hopper Activation 3 |
| `11000` | Hopper Activation 4 |
| `11001`–`11111` | Spare |

:::{tip}
Exemple : pour exécuter la Séquence 5, régler Bit1=1, Bit2=0, Bit3=1, Bit4=0, Bit5=0 (code binaire `00101`) puis envoyer un front montant sur **Latch**.
:::
