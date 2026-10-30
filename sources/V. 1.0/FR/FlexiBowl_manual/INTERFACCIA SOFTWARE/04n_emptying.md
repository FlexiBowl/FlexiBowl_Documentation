(emptying)=
# **Emptying**

La page Emptying est mise automatiquement à disposition lorsque l'option Vidage est achetée.

## Présentation

La fonction **Emptying** permet de vider automatiquement le FlexiBowl® en enchaînant jusqu'à **4 séquences** dédiées, chacune répétée un nombre de fois (loop) configurable. Elle est conçue pour libérer rapidement le disque des pièces résiduelles, par exemple en fin de poste ou lors d'un changement de production, sans devoir appeler manuellement les séquences une par une.

![Page Emptying](../../../../_shared/media/images/pagina_Emptying.png)

---

## Configuration via l'interface web

La page est organisée en **4 colonnes**, une pour chacune des séquences qui composent le cycle de vidage (« Select the first/second/third/fourth sequence »), plus les commandes de démarrage/arrêt en bas de page.

### AUTO CONFIG

Le bouton **AUTO CONFIG**, en haut, insère automatiquement une configuration par défaut qui occupe les **séquences 17, 18, 19 et 20**. Il est également possible de personnaliser librement ces séquences ou d'en sélectionner d'autres parmi les 20 disponibles.

:::{note}
Dans la configuration par défaut, la première séquence abaisse la barrière (**FLB_BARRIER_DOWN**), les deux séquences centrales répètent plusieurs fois un mouvement combiné de rotation et de soufflage suivi d'un shake (**FLB_MOVE_BLOWc** + **FLB_SHAKE**), tandis que la dernière relève la barrière (**FLB_BARRIER_UP**) à la fin du cycle.
:::

### Éléments de chaque colonne

| Élément | Fonction |
|---|---|
| **Select the first/second/third/fourth sequence** | Menu déroulant pour sélectionner laquelle des 20 séquences programmées est exécutée à cette étape du cycle de vidage |
| **Active Command** | Liste des commandes actives dans la séquence sélectionnée (jusqu'à 10 emplacements, même structure que la page Main Command) |
| **N° Loop** | Nombre de fois où la séquence sélectionnée est répétée pendant cette étape |
| **EDIT SEQUENCE** | Ouvre la séquence sélectionnée pour modifier les commandes qui la composent |

### Démarrage et arrêt

| Commande | Fonction |
|---|---|
| **START EMPTYING** | Démarre le cycle de vidage : exécute dans l'ordre les 4 séquences configurées, chacune pour le nombre de loops défini |
| **STOP EMPTYING** | Interrompt le cycle de vidage en cours |

---
## Page Option

Si la fonction Emptying est présente, l'encadré suivant sera affiché dans la section OPTION de la page « Main Command » :

![Emptying OPTION](../../../../_shared/media/images/emptying_option.png)

Cet encadré, contenant les deux boutons « Raise Barrier » et « Lower Barrier », permet de relever et d'abaisser la barrière de vidage et donc d'en vérifier le bon fonctionnement. Lorsque la barrière est abaissée, le capteur présent dans cet encadré est activé.

## Page Sequence 

:::{image} ../../../../_shared/media/images/box_emptying.png
:width: 50% 
:align: center
:::

Dans la page Sequence, la case « Emptying Sequence » cochée permet de déplacer le FlexiBowl même avec la barrière de vidage abaissée. En effet, si la barrière est abaissée et que la case de la page Sequence n'est pas cochée, il ne sera pas possible d'effectuer le mouvement associé à la séquence en cours.

## Commandes via protocole

Comme pour le reste de l'interface logicielle, le cycle Emptying peut également être démarré, configuré et vérifié par protocole (TCP Server, EtherNet/IP, Profinet, Modbus), avec les mêmes ControlWords quel que soit le protocole utilisé — seul le transport change, comme décrit dans la page [Interface logicielle](int_software).

### Commandes EXE

| Commande | ControlWord | Busy pendant l'exécution | ReturnData_1 | Explication |
|---|---|---|---|---|
| Start Emptying | 45 | OUI (Emptying actif) | 45 | Démarre le vidage |
| Stop Emptying | 46 | OUI (Emptying actif) | 46 | Arrête le vidage |
| Emptying Active | 47 | NON | 47 | Vérifie si le vidage est actif |

### Commandes WRITE

Chaque paire Séquence/Loop correspond à l'une des 4 colonnes de la page web :

| Commande | ControlWord | Range Data_1 | Busy pendant l'exécution | ReturnData_1 |
|---|---|---|---|---|
| FirstSequence | 20200 | 1–20 | NON | 20200 |
| FirstLoop | 20201 | 0–500 | NON | 20201 |
| SecondSequence | 20202 | 1–20 | NON | 20202 |
| SecondLoop | 20203 | 0–500 | NON | 20203 |
| ThirdSequence | 20204 | 1–20 | NON | 20204 |
| ThirdLoop | 20205 | 0–500 | NON | 20205 |
| FourthSequence | 20206 | 1–20 | NON | 20206 |
| FourthLoop | 20207 | 0–500 | NON | 20207 |

### Commandes READ

| Commande | ControlWord | Busy pendant l'exécution | ReturnData_1 | Range ReturnData_2 |
|---|---|---|---|---|
| FirstSequence | 20300 | NON | 20300 | 1–20 |
| FirstLoop | 20301 | NON | 20301 | 0–500 |
| SecondSequence | 20302 | NON | 20302 | 1–20 |
| SecondLoop | 20303 | NON | 20303 | 0–500 |
| ThirdSequence | 20304 | NON | 20304 | 1–20 |
| ThirdLoop | 20305 | NON | 20305 | 0–500 |
| FourthSequence | 20306 | NON | 20306 | 1–20 |
| FourthLoop | 20307 | NON | 20307 | 0–500 |

:::{tip}
Pour l'explication complète de la logique ControlWord, du fonctionnement en 4 étapes et des exemples pratiques via bus de terrain/TCP, se référer à la section [Commandes de vidage](int_software.html#sec-empty) de la page Interface logicielle.
:::

---

## Notes d'utilisation

:::{note}
Les 4 séquences appelées par Emptying (par défaut 17–20, ou personnalisées) restent des séquences programmables normales : elles peuvent être modifiées depuis la page **Main Command** exactement comme n'importe quelle autre séquence, ainsi qu'au moyen du bouton **EDIT SEQUENCE** de cette page.
:::

:::{warning}
Ne pas envoyer une nouvelle commande **Start Emptying** alors qu'un cycle de vidage est déjà en cours (**Emptying Active** = 1). Vérifier que le cycle précédent est terminé, ou envoyer **Stop Emptying**, avant d'en démarrer un nouveau.
:::
