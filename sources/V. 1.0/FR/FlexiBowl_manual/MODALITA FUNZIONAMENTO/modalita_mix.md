# **Mode Mix**

(funzionamento-in-mix-mode)=
## Fonctionnement en MIX Mode

Le **mode Mix** permet d'alimenter simultanément des pièces de types différents sur la même surface du FlexiBowl®.

Ce mode est particulièrement indiqué pour les applications de **tri** (sorting) où la présence de plusieurs références sur le même plan de travail est requise sans devoir multiplier les postes robotisés.

```{figure}  ../../../../_shared/media/images/flexibowl_standard_cycle.jpg
:align: center
:width: 50%
:alt: *Cycle opérationnel en mode Mix : Detect → Pick-Drop → Move-Flip*
```

```{image}  ../../../../_shared/media/videos/MIX_MODE.gif
:align: center
:width: 100%
:alt: *Cycle opérationnel en mode Mix : Detect → Pick-Drop → Move-Flip*
```
---

## Caractéristiques principales

| Caractéristique | Description |
|---|---|
| **Application** | Idéal pour les applications de tri avec plusieurs types de pièces |
| **Flexibilité** | Alimentation de pièces mixtes sur la même surface |

---

## Cycle opérationnel

Le cycle du MIX Mode est simplifié par rapport au mode standard, avec seulement trois étapes qui se répètent en séquence :

```{list-table}
:header-rows: 1
:widths: 20 80

* - Phase
  - Description
* - **Detect**
  - La caméra acquiert l'image de la surface commune, en identifiant la position et l'orientation de toutes les pièces présentes, indépendamment de leur type.
* - **Move-Flip**
  - Le FlexiBowl® tourne et les pièces mal orientées sont retournées ou repositionnées.
* - **Pick-Drop**
  - Le robot prélève la pièce correcte selon la logique de tri et la dépose à la position de destination.
```


---
## Avantages 


:::{grid-item-card} Avantages
- **Flexibilité maximale** : .
- **Coûts réduits** : .
- **Empreinte au sol réduite** : .
:::


:::{note}
Le mode Mix est disponible pour les FlexiBowl® 500, 650 et 800.
:::

---
## Notes d'utilisation

:::{tip}
Le mode Mix ne nécessite aucun matériel supplémentaire par rapport à une configuration standard.
 Il suffit de configurer le logiciel de vision pour la reconnaissance de plusieurs références et de définir la logique de tri dans le programme du robot.
:::

:::{note}
Pour le placement optimal du FlexiBowl® et du robot, se référer au chapitre {ref}`Layout Best Practice <layoutbp>`.
:::
