(tcp)=
# **TCP Server**

Lorsque la communication **TCP Server** est utilisée, les commandes ne sont pas envoyées sous forme de variables binaires mais sous forme de **chaînes de texte** via une connexion socket sur le port configuré (par défaut : 8123).


Chaque message a la forme :

```
NomeVariabile[Valore]%
```

Le caractère `%` est le **terminateur de message** et doit toujours être présent à la fin. Le champ `[Valore]` contient la donnée numérique associée (ControlWord, état, etc.).

## Tableau de la syntaxe TCP

| Opération | Message à envoyer | Réponse si OK | Réponse en cas d'erreur |
|---|---|---|---|
| Toutes les commandes EXE | `10[0]%` | `10[0]%` | `1[0]%` |
| Toutes les commandes WRITE | `100[56]%` | `100[0]%` | `2[0]%` |
| Toutes les commandes READ | `10100[0]%` | `10100[valore]%` | `2[0]%` |
| Réinitialisation des erreurs | `Reset%` | `Reset%` | — |
| Lire l'état Busy | `Busy%` | `Busy[1]%` | `Busy[0]%` |
| Lire l'état Ready | `Ready%` | `Ready[1]%` | `Ready[0]%` |
| Lire l'état InError | `InError%` | `InError[1]%` | `InError[0]%` |
| Lire l'état InPowerOn | `InPowerOn%` | `InPowerOn[1]%` | `InPowerOn[0]%` |
| Lire ErrorCode | `ErrorCode%` | `ErrorCode[56]%` | `ErrorCode[0]%` |

:::{note}
Dans les réponses de type READ, le texte `[valore]` est remplacé par la valeur numérique effective lue par le système. Par exemple, pour lire la vitesse de la SEQ 1 (ControlWord 10102), on envoie `10102[0]%` et on reçoit `10102[35]%` si la vitesse est réglée à 35 %.
:::

:::{warning}
Les commandes Hopper via TCP (`Hopper1Start%`, etc.) fonctionnent **uniquement lorsque la communication est active et que le FlexiBowl® n'est pas en mouvement**. Le bon fonctionnement n'est pas garanti si le FlexiBowl® exécute une séquence ou est en mode jog.
:::

## Signification de ReturnData_1 (ou de la réponse TCP)

| Valeur | Signification |
|---|---|
| `0` | NULL — aucune commande en cours (état initial) |
| `1` | Commande non interprétable (ControlWord inconnu) |
| `2` | Data_1 hors plage, mais la commande a été reconnue |
| `3` | Système occupé (Busy) — réessayer une fois que Busy est revenu à 0 |
| Valeur = ControlWord | Commande exécutée correctement |

---

## Protocole de commandes

Le protocole de commandes définit toutes les actions disponibles via le ControlWord. Les ControlWords sont **les mêmes pour tous les protocoles** ; seul le transport change (voir [Transport Fieldbus](#sec-fieldbus) et [Syntaxe TCP](#sec-tcp)). Les commandes sont regroupées en catégories :

<div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:1rem; margin:1.5rem 0 2.5rem;">

  <a href="#sec-exe" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-play-circle" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Commandes EXE</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Commandes d'exécution (démarrage des séquences, jog, réinitialisation)</span>
  </a>

  <a href="#sec-write" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-pencil-simple" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Commandes WRITE</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Écriture de paramètres (vitesse, angles, temps, etc.)</span>
  </a>

  <a href="#sec-read" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-eye" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Commandes READ</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Lecture des paramètres actuellement configurés</span>
  </a>

</div>

(sec-exe)=
### Commandes <span class="isw-section-badge isw-badge-exe"><i class="ph ph-play-circle"></i> EXE</span>

Les commandes EXE démarrent une action immédiate sur le FlexiBowl®. Pendant l'exécution, **Busy** reste à `1`.

| Commande | ControlWord | Busy pendant l'exécution | ReturnData_1 | Explication | 
|---|---|---|---|---|
| Exe Seq 1 | 10 | OUI | 10 | Exécuter la Séquence 1 |
| Exe Seq 2 | 11 | OUI | 11 | Exécuter la Séquence 2 |
| Exe Seq 3 | 12 | OUI | 12 | Exécuter la Séquence 3 |
| Exe Seq 4 | 13 | OUI | 13 | Exécuter la Séquence 4 |
| Exe Seq 5 | 14 | OUI | 14 | Exécuter la Séquence 5 |
| Exe Seq 6 | 15 | OUI | 15 | Exécuter la Séquence 6 |
| Exe Seq 7 | 16 | OUI | 16 | Exécuter la Séquence 7 |
| Exe Seq 8 | 17 | OUI | 17 | Exécuter la Séquence 8 |
| Exe Seq 9 | 18 | OUI | 18 | Exécuter la Séquence 9 |
| Exe Seq 10 | 19 | OUI | 19 | Exécuter la Séquence 10 |
| Exe Seq 11 | 20 | OUI | 20 | Exécuter la Séquence 11 |
| Exe Seq 12 | 21 | OUI | 21 | Exécuter la Séquence 12 |
| Exe Seq 13 | 22 | OUI | 22 | Exécuter la Séquence 13 |
| Exe Seq 14 | 23 | OUI | 23 | Exécuter la Séquence 14 |
| Exe Seq 15 | 24 | OUI | 24 | Exécuter la Séquence 15 |
| Exe Seq 16 | 25 | OUI | 25 | Exécuter la Séquence 16 |
| Exe Seq 17 | 26 | OUI | 26 | Exécuter la Séquence 17 |
| Exe Seq 18 | 27 | OUI | 27 | Exécuter la Séquence 18 |
| Exe Seq 19 | 28 | OUI | 28 | Exécuter la Séquence 19 |
| Exe Seq 20 | 29 | OUI | 29 | Exécuter la Séquence 20 |
| Start Jog Seq | 40 | OUI | 40 | Démarrer le Jog |
| Stop Jog Seq | 41 | OUI | 41 | Arrêter le Jog |
| Reset Return Data | 50 | NON | 0 | Remet à zéro la valeur de ReturnData_1 et ReturnData_2, en les ramenant à l'état initial `0` |

:::{note}
La commande **Reset Return Data** (ControlWord 50) remet à zéro la valeur de ReturnData_1 et ReturnData_2, en les ramenant à l'état initial `0`. Elle est utile pour vérifier qu'une nouvelle commande est effectivement reçue et traitée.
:::

(TCP_EXE)=
#### Exemple pratique — « Exécuter la Séquence 3 »

<div class="isw-example">
<div class="isw-example-title">Exécuter la Séquence 3 → ControlWord 12</div>
<div class="isw-example-body">
<div>

<div>
<div class="isw-example-col-title">TCP Server</div>

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>12[0]%</code><br> RETURN SI OK:&nbsp;&nbsp;&nbsp;<span class="ok">12[0]</span>
</div>

Exemple de commande **non valide** (par ex. la séquence 9 n'existe pas sur l'appareil) :

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>9[0]%</code><br> RETURN SI NON OK:&nbsp;&nbsp;&nbsp;<span class="ko">1[0]</span>
</div>

</div>
</div>
</div>

(sec-write)=
### Commandes <span class="isw-section-badge isw-badge-write"><i class="ph ph-pencil-simple"></i> WRITE</span>

Les commandes WRITE permettent de modifier les paramètres opérationnels du FlexiBowl® (vitesse, angles, temps, etc.) directement depuis le système externe, sans avoir à accéder à l'interface graphique.

#### Logique d'adressage des séquences

Chaque séquence (de 1 à 20) possède son propre bloc de paramètres. Le ControlWord se calcule avec la formule :

> **ControlWord = N × 100 + parameter_offset**

où `N` est le numéro de la séquence (1–20) et `offset_parametro` identifie le paramètre spécifique.

#### Paramètres inscriptibles pour chaque séquence

| Paramètre | Offset | Range Data_1 | Notes |
|---|---|---|---|
| AccelerationMove | 00 | 1–100 | Rampe d'accélération du mouvement rotatif (%) |
| DecelerationMove | 01 | 1–100 | Rampe de décélération du mouvement rotatif (%) |
| SpeedMove | 02 | 1–100 | Vitesse du mouvement rotatif (%) |
| AngleMove | 03 | 0–720 | Angle de rotation en degrés. Valeurs 1000–1720 = angle négatif (sens opposé) |
| AccelerationShake | 04 | 1–100 | Rampe d'accélération du shake (%) |
| DecelerationShake | 05 | 1–100 | Rampe de décélération du shake (%) |
| CountShake | 06 | 2–20 | Nombre d'oscillations par cycle de shake |
| CwAngleShake | 07 | 0–360 | Angle de rotation horaire pendant le shake. Valeurs 1000–1360 = angle négatif |
| CcwAngleShake | 08 | 0–360 | Angle de rotation antihoraire pendant le shake. Valeurs 1000–1360 = angle négatif |
| SpeedShake | 09 | 1–100 | Vitesse du shake (%) |
| FlipCount | 10 | 0–20 | Nombre de flips par cycle |
| FlipDelay | 11 | 0–500 | Pause entre un flip et le suivant (ms) |
| BlowDelay | 12 | 0–500 | Pause entre une impulsion de blow et la suivante (ms) |
| ProportionalValve_Flip | 13 | 0–600 | Pression de l'électrovanne proportionnelle Flip (valeur /100 = Bar) |
| ProportionalValve_Blow | 14 | 0–600 | Pression de l'électrovanne proportionnelle Blow (valeur /100 = Bar) |
| Delete all sequence | 30 | — | Supprime toutes les commandes de la liste de la séquence |
| Emptying Sequence | 40 | 0–1 | 0 = mode normal, 1 = mode Quick Emptying |
| Seq Add Cmd | 50 | COMMANDE FLB | Ajoute une commande à la liste de la séquence |

#### Exemples de ControlWord WRITE

| Séquence | Paramètre | Offset associé au paramètre | Formule (N x 100 + Offset) | ControlWord |
|---|---|---|---|---|
| SEQ 1 (N=1) | AccelerationMove | 00 | 1 x 100 + 00 | 100 |
| SEQ 1 (N=1) | SpeedMove | 02 | 1 x 100 + 02 | 102 |
| SEQ 1 (N=1) | FlipCount | 10 | 1 x 100 + 10 | 110 |
| SEQ 1 (N=1) | Emptying Sequence | 40 | 1 x 100 + 40 | 140 |
| SEQ 1 (N=1) | Seq Add Cmd | 50 | 1 x 100 + 50 | 150 |
| SEQ 2 (N=2) | AccelerationMove | 00 | 2 x 100 + 00 | 200 |
| SEQ 2 (N=2) | SpeedMove | 02 | 2 x 100 + 02 | 202 |
| SEQ 5 (N=5) | AngleMove | 03 | 5 x 100 + 03 | 503 |
| SEQ 10 (N=10) | FlipDelay | 11 | 10 x 100 + 11 |1011 |
| SEQ 20 (N=20) | SpeedMove | 02 | 20 x 100 + 02 | 2002 |

:::{tip}
La formule est simple :
- Pour écrire la vitesse (offset 02) de la séquence 7, le ControlWord est `7 × 100 + 2 = 702`.
- Pour écrire le FlipCount (offset 10) de la séquence 15, le ControlWord est `15 × 100 + 10 = 1510`.
:::

(TCP_write)=
#### Exemple pratique — « Régler l'accélération du Move à 80 dans la Séquence 7 »

<div class="isw-example">
<div class="isw-example-title">SpeedMove Seq 7 → ControlWord 700, Data_1 = 80</div>
<div class="isw-example-body">
<div>

<div>
<div class="isw-example-col-title">TCP Server</div>

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>700[80]%</code><br> RETURN SI OK:&nbsp;&nbsp;&nbsp;<span class="ok">700[0]</span>
</div>

Exemple de **valeur hors plage** (accélération 1000 non admise, plage 1–100) :

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>700[1000]%</code><br> RETURN SI NON OK:&nbsp;&nbsp;&nbsp;<span class="ko">2[0]</span>
</div>

</div>
</div>
</div>

#### Paramètres WRITE JOG

Les paramètres du Jog (fonctionnement manuel continu) sont configurables séparément via ControlWord dans le bloc 20000.

| Paramètre | ControlWord | Range Data_1 | Notes |
|---|---|---|---|
| AccelerationJog | 20001 | 0–100 | Rampe d'accélération du jog (%) |
| DecelerationJog | 20002 | 0–100 | Rampe de décélération du jog (%) |
| SpeedJog | 20003 | 0–100 | Vitesse du jog (%). Valeurs 1000–1100 = vitesse négative (rotation inverse) |
| FlipJog_Enable | 20004 | 0–1 | 0 = flip désactivé, 1 = flip activé pendant le jog |
| FlipJog_Duration | 20005 | 0–1000 | Durée de l'impulsion de flip (ms) |
| FlipJog_Pressure | 20006 | 0–600 | Pression de flip (/100 = Bar) |
| FlipJog_Pause | 20007 | 0–1000 | Pause entre flips consécutifs (ms) |
| BlowJog_Enable | 20008 | 0–1 | 0 = blow désactivé, 1 = blow activé pendant le jog |
| BlowJog_Duration | 20009 | 0–1000 | Durée de l'impulsion de blow (ms) |
| BlowJog_Pressure | 20010 | 0–600 | Pression de blow (/100 = Bar) |
| BlowJog_Pause | 20011 | 0–1000 | Pause entre blows consécutifs (ms) |
| BlowJog_Type | 20012 | 0–2 | Type de blow : 0 = BLOWc, 1 = BLOWe, 2 = BLOWc+BLOWe |
| Backlight_1 | 20013 | 0–1 | 0 = éteint, 1 = allumé |
| Backlight_2 | 20014 | 0–1 | 0 = éteint, 1 = allumé |

---

(sec-read)=
### Commandes <span class="isw-section-badge isw-badge-read"><i class="ph ph-eye"></i> READ</span>

Les commandes READ permettent de lire les paramètres actuellement configurés dans le FlexiBowl®. La valeur lue est renvoyée dans **ReturnData_2**.

#### Logique d'adressage READ des séquences

Le ControlWord pour la lecture se calcule avec la formule :

> **ControlWord = 10000 + N × 100 + parameter_offset**

où `N` est le numéro de la séquence (1–20) et `offset_parametro` est le même que celui utilisé dans les commandes WRITE.

Les paramètres lisibles sont les mêmes que ceux du bloc WRITE, avec en plus les 10 emplacements de la liste de commandes :

| Paramètre supplémentaire | Offset | Description |
|---|---|---|
| Seq Slot 1 Cmd | 50 | Commande en position 1 dans la liste de la séquence |
| Seq Slot 2 Cmd | 51 | Commande en position 2 |
| … | … | … |
| Seq Slot 10 Cmd | 59 | Commande en position 10 |

#### Exemples de ControlWord READ

| Séquence | Paramètre | ControlWord |
|---|---|---|
| SEQ 1 | AccelerationMove | 10100 |
| SEQ 1 | SpeedMove | 10102 |
| SEQ 1 | FlipCount | 10110 |
| SEQ 1 | Emptying Sequence | 10140 |
| SEQ 1 | Slot 1 Cmd | 10150 |
| SEQ 1 | Slot 10 Cmd | 10159 |
| SEQ 5 | AngleMove | 10503 |
| SEQ 10 | SpeedMove | 11002 |
| SEQ 20 | Emptying Sequence | 12040 |

:::{tip}
Formule rapide :
 Pour lire la vitesse (offset 02) de la séquence 12, le ControlWord est `10000 + 12 × 100 + 2 = 11202`.
:::

(TCP_read)=
#### Exemple pratique — « Lire l'angle de la Séquence 16 »

<div class="isw-example">
<div class="isw-example-title">AngleMove Seq 16 → ControlWord 11603</div>
<div class="isw-example-body">
<div>

<div>
<div class="isw-example-col-title">TCP Server</div>

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>11603[0]%</code><br> RETURN SI OK:&nbsp;&nbsp;&nbsp;<span class="ok">11603[45]</span>
</div>

Exemple de **valeur hors plage** en écriture sur le même paramètre (angle maximal 720°) :

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>11603[6799]%</code><br> RETURN SI NON OK:&nbsp;&nbsp;&nbsp;<span class="ko">1[0]</span>
</div>

</div>
</div>
</div>

#### Paramètres READ JOG

Les mêmes paramètres JOG inscriptibles (bloc 20000) sont lisibles dans le bloc 20100 :

| Paramètre | ControlWord READ | Plage ReturnData_2 |
|---|---|---|
| AccelerationJog | 20101 | 0–100 |
| DecelerationJog | 20102 | 0–100 |
| SpeedJog | 20103 | 0–100 (1000–1100 = négatif) |
| FlipJog_Enable | 20104 | 0–1 |
| FlipJog_Duration | 20105 | 0–1000 |
| FlipJog_Pressure | 20106 | 0–600 (/100) |
| FlipJog_Pause | 20107 | 0–1000 |
| BlowJog_Enable | 20108 | 0–1 |
| BlowJog_Duration | 20109 | 0–1000 |
| BlowJog_Pressure | 20110 | 0–600 (/100) |
| BlowJog_Pause | 20111 | 0–1000 |
| BlowJog_Type | 20112 | 0–2 |
| Backlight_1 | 20113 | 0–1 |
| Backlight_2 | 20114 | 0–1 |

---

(sec-hopper)=
## Commandes <span class="isw-section-badge isw-badge-hop"><i class="ph ph-funnel"></i> HOPPER</span>

Les commandes Hopper pilotent les Bulk Feeders connectés au système (jusqu'à 4). Elles suivent la même logique ControlWord/WRITE/READ décrite ci-dessus, valable pour tous les protocoles, ainsi qu'une syntaxe TCP dédiée pour le démarrage rapide.

### Démarrage rapide via TCP

Outre la syntaxe générale ControlWord, le protocole **TCP Server** propose des messages dédiés pour démarrer directement un hopper :

| Opération | Message à envoyer | Réponse |
|---|---|---|
| Démarrer le Hopper 1 | `Hopper1Start%` | `Hopper1Start *` |
| Démarrer le Hopper 2 | `Hopper2Start%` | `Hopper2Start *` |
| Démarrer le Hopper 3 | `Hopper3Start%` | `Hopper3Start *` |
| Démarrer le Hopper 4 | `Hopper4Start%` | `Hopper4Start *` |

Sur les protocoles fieldbus (EtherNet/IP, Profinet, Modbus), le même démarrage immédiat s'obtient en mettant directement à `1` le bit **Hopper_1**...**Hopper_4** du [paquet d'E/S](#sec-fieldbus), sans passer par le ControlWord.

### Commandes WRITE Hopper

| Paramètre | ControlWord | Range Data_1 | Description |
|---|---|---|---|
| Hopper_1_Id | 30001 | 1–100 | ID unique du hopper 1 sur le réseau |
| Hopper_1_Amplitude | 30002 | 50–220 | Amplitude de vibration du hopper 1 |
| Hopper_1_Frequency | 30003 | 40–70 | Fréquence de vibration du hopper 1 |
| Hopper_1_Activation_Time | 30004 | 400–60000 | Temps d'activation du hopper 1 (ms) |
| Hopper_2_Id | 30005 | 1–100 | ID unique du hopper 2 |
| Hopper_2_Amplitude | 30006 | 50–220 | Amplitude de vibration du hopper 2 |
| Hopper_2_Frequency | 30007 | 40–70 | Fréquence de vibration du hopper 2 |
| Hopper_2_Activation_Time | 30008 | 400–60000 | Temps d'activation du hopper 2 (ms) |
| Hopper_3_Id | 30009 | 1–100 | ID unique du hopper 3 |
| Hopper_3_Amplitude | 30010 | 50–220 | Amplitude de vibration du hopper 3 |
| Hopper_3_Frequency | 30011 | 40–70 | Fréquence de vibration du hopper 3 |
| Hopper_3_Activation_Time | 30012 | 400–60000 | Temps d'activation du hopper 3 (ms) |
| Hopper_4_Id | 30013 | 1–100 | ID unique du hopper 4 |
| Hopper_4_Amplitude | 30014 | 50–220 | Amplitude de vibration du hopper 4 |
| Hopper_4_Frequency | 30015 | 40–70 | Fréquence de vibration du hopper 4 |
| Hopper_4_Activation_Time | 30016 | 400–60000 | Temps d'activation du hopper 4 (ms) |
| Hopper_1_Enable | 30017 | — | Activer le hopper 1 (action immédiate) |
| Hopper_1_Disable | 30018 | — | Désactiver le hopper 1 (action immédiate) |
| Hopper_2_Enable | 30019 | — | Activer le hopper 2 |
| Hopper_2_Disable | 30020 | — | Désactiver le hopper 2 |
| Hopper_3_Enable | 30021 | — | Activer le hopper 3 |
| Hopper_3_Disable | 30022 | — | Désactiver le hopper 3 |
| Hopper_4_Enable | 30023 | — | Activer le hopper 4 |
| Hopper_4_Disable | 30024 | — | Désactiver le hopper 4 |

:::{note}
Dans le matériel de formation, le ControlWord `30005` (Hopper_2_Id) indiquait par erreur la même plage que l'Amplitude (50–220). Dans ce tableau, elle a été corrigée à **1–100**, de manière cohérente avec Hopper_1_Id, Hopper_3_Id et Hopper_4_Id. Vérifier cette valeur avec le firmware/la fiche technique avant de publier la page.
:::

(TCP_WRITEHOPPER)=
#### Exemple pratique — « Activer le Hopper 1 »

<div class="isw-example">
<div class="isw-example-title">Hopper_1_Enable → ControlWord 30017</div>
<div class="isw-example-body">
<div>

<div>
<div class="isw-example-col-title">TCP Server</div>

Via ControlWord générique :

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>30017[0]%</code><br> RETURN SI OK:&nbsp;&nbsp;&nbsp;<span class="ok">30017[0]</span>
</div>

Ou, pour le seul démarrage, avec le message dédié :

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>Hopper1Start%</code><br> RETURN:&nbsp;&nbsp;&nbsp;<span class="ok">Hopper1Start *</span>
</div>

</div>
</div>
</div>

#### Exemple pratique — « Régler l'amplitude du Hopper 2 à 220 »

<div class="isw-example">
<div class="isw-example-title">Hopper_2_Amplitude → ControlWord 30006, Data_1 = 220</div>
<div class="isw-example-body">
<div>

<div>
<div class="isw-example-col-title">TCP Server</div>

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>30006[220]%</code><br> RETURN SI OK:&nbsp;&nbsp;&nbsp;<span class="ok">30006[0]</span>
</div>

Exemple de **valeur hors plage** (amplitude 2200 non admise, plage 50–220) :

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>30006[2200]%</code><br> RETURN SI NON OK:&nbsp;&nbsp;&nbsp;<span class="ko">2[0]</span>
</div>

</div>
</div>
</div>

### Commandes READ Hopper

| Paramètre | ControlWord READ | Range ReturnData_2 | Notes |
|---|---|---|---|
| Hopper_1_Id | 30101 | 1–100 | |
| Hopper_1_Amplitude | 30102 | 50–220 | |
| Hopper_1_Frequency | 30103 | 40–70 | |
| Hopper_1_Activation_Time | 30104 | 400–60000 | |
| Hopper_2_Id | 30105 | 1–100 | |
| Hopper_2_Amplitude | 30106 | 50–220 | |
| Hopper_2_Frequency | 30107 | 40–70 | |
| Hopper_2_Activation_Time | 30108 | 400–60000 | |
| Hopper_3_Id | 30109 | 1–100 | |
| Hopper_3_Amplitude | 30110 | 50–220 | |
| Hopper_3_Frequency | 30111 | 40–70 | |
| Hopper_3_Activation_Time | 30112 | 400–60000 | |
| Hopper_4_Id | 30113 | 1–100 | |
| Hopper_4_Amplitude | 30114 | 50–220 | |
| Hopper_4_Frequency | 30115 | 40–70 | |
| Hopper_4_Activation_Time | 30116 | 400–60000 | |
| Hopper_1_Ready | 30117 | 0–1 | 0 = non prêt, 1 = prêt |
| Hopper_2_Ready | 30118 | 0–1 | 0 = non prêt, 1 = prêt |
| Hopper_3_Ready | 30119 | 0–1 | 0 = non prêt, 1 = prêt |
| Hopper_4_Ready | 30120 | 0–1 | 0 = non prêt, 1 = prêt |
| Hopper_1_InVibration | 30121 | 0–1 | 0 = arrêté, 1 = en vibration |
| Hopper_2_InVibration | 30122 | 0–1 | 0 = arrêté, 1 = en vibration |
| Hopper_3_InVibration | 30123 | 0–1 | 0 = arrêté, 1 = en vibration |
| Hopper_4_InVibration | 30124 | 0–1 | 0 = arrêté, 1 = en vibration |
| Hopper_1_Enabled | 30125 | 0–1 | 0 = désactivé, 1 = activé |
| Hopper_2_Enabled | 30126 | 0–1 | 0 = désactivé, 1 = activé |
| Hopper_3_Enabled | 30127 | 0–1 | 0 = désactivé, 1 = activé |
| Hopper_4_Enabled | 30128 | 0–1 | 0 = désactivé, 1 = activé |

(TCP_READHOPPER)=
#### Exemple pratique — « Lire la fréquence du Hopper 4 »

<div class="isw-example">
<div class="isw-example-title">Hopper_4_Frequency → ControlWord 30115</div>
<div class="isw-example-body">
<div>

<div>
<div class="isw-example-col-title">TCP Server</div>

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>30115[0]%</code><br> RETURN SI OK:&nbsp;&nbsp;&nbsp;<span class="ok">30115[40]</span>
</div>

Exemple de **commande non interprétable** (ControlWord READ inexistant) :

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>30199[0]%</code><br> RETURN SI NON OK:&nbsp;&nbsp;&nbsp;<span class="ko">1[0]</span>
</div>

</div>
</div>
</div>

:::{note}
Pour les commandes Quick Emptying, se reporter à la section [Commandes Quick Emptying](sec-empty)
:::

:::{important}
Pour les Codes d'erreur, se reporter à la section [Codes d'erreur](sec-err)
:::