# **Mode Standard**

Le **mode Standard** est la configuration opérationnelle par défaut du FlexiBowl® et convient à tout type d'application d'alimentation robotisée. Dans ce mode, le robot et le système de vision partagent la même zone de travail, en opérant de manière coordonnée et séquentielle afin de garantir des performances de cycle élevées.

---

## Principe de fonctionnement

En mode Standard, le FlexiBowl® exécute un cycle continu composé de trois phases principales, qui se répètent en séquence :

```{figure} ../../../../_shared/media/images/flexibowl_standard_cycle.jpg
:align: center
:width: 50%
:alt: *Cycle opérationnel en mode Standard : Detect → Pick-Drop → Move-Flip*
```
```{image} ../../../../_shared/media/videos/STANDARD_MODE.gif
:align: center
:width: 100%
:alt: *Cycle opérationnel en mode Standard : Detect → Pick-Drop → Move-Flip*
```

### 1. Detect (Détection)

Le système de vision acquiert une image de la surface du FlexiBowl® et identifie la position, l'orientation et le type des composants présents. Les informations sont transmises au robot pour planifier les opérations de prélèvement.

### 2. Pick-Drop (Prélèvement et dépose)

Le robot prélève les composants correctement orientés du FlexiBowl® et les dépose à la position de destination (par ex. plateau, tapis roulant, poste d'assemblage). Les activités de vision et de prélèvement sont exécutées **de manière séquentielle** : d'abord le système de vision scanne la scène, puis le robot intervient.

### 3. Move-Flip (Mouvement et retournement)

À la fin du prélèvement, le FlexiBowl® exécute un mouvement combiné de rotation et de vibration (**flip**) pour remélanger les composants restants et favoriser la présentation correcte de nouvelles pièces. Parallèlement, la **décharge du hopper** et le **mouvement du bowl** sont exécutés **simultanément**, ce qui optimise les temps de cycle.

---

## Caractéristiques principales

| Caractéristique | Description |
|---|---|
| **Zone de travail partagée** | Le robot et le système de vision opèrent dans la même zone du FlexiBowl® |
| **Applicabilité** | Adapté à tous les types d'application |
| **Décharge du hopper** | Exécutée simultanément avec le mouvement/l'impulsion du FlexiBowl® |
| **Vision et prélèvement** | Exécutés en séquence |
| **Mesure du cycle** | Le temps de cycle est mesuré sur une base à la minute |

---

## Schéma du cycle opérationnel

Le cycle se déroule selon le schéma en boucle fermée suivant :

1. **Detect** — Le système de vision scanne le FlexiBowl® et localise les composants.
2. **Pick-Drop** — Le robot prélève les pièces identifiées et les dépose à destination.
3. **Move-Flip** — Le FlexiBowl® remélange les composants pour le cycle suivant.
4. Le cycle recommence au point 1.

:::{note} 
Pendant la phase Move-Flip, la décharge du hopper s'effectue en parallèle avec le mouvement du FlexiBowl®, ce qui réduit les temps morts et maximise la productivité.
:::

---
## Exemple d'implantation

:::{figure} ../../../../_shared/media/images/Funz-standard.PNG
:align: center
:width: 60%

Exemple d'implantation en mode Standard : le Bulk Feeder décharge dans le secteur de dépose, le flip sépare les composants, le robot prélève dans la zone de vision et les pièces non prélevées recirculent.
:::

La zone de travail du robot doit couvrir entièrement la zone de vision, de sorte que le robot puisse atteindre tous les composants reconnus comme prenables. Pour le positionnement du robot, du Bulk Feeder, des zones de dépose, de la caméra et de l'éclairage, se référer à {ref}`Layout Best Practice <layoutbp-traditional>`.


---

## Avantages 


:::{grid-item-card} Avantages
- **Précision** : .
- **Séparation** : .
- **Vitesse** : .
:::
