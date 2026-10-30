(info)=
# **Informations préliminaires**

Cette section contient des informations juridiques et des avertissements importants relatifs à l'utilisation du FlexiBowl® et de la présente documentation.   Veuillez la lire attentivement avant de procéder à l'installation et à l'utilisation du système.

---

## Destinataires et public cible

```{note}
**À qui s'adresse ce manuel**

Cette documentation s'adresse à des techniciens qualifiés possédant des compétences en :
- Intégration de systèmes robotisés
- Configuration de systèmes de vision industrielle
- Installation et maintenance d'équipements électromécaniques

Il est supposé que le lecteur possède les connaissances techniques de base nécessaires pour comprendre les informations fournies.   Les informations facilement déductibles de dessins techniques ou de schémas peuvent ne pas être détaillées davantage.
```

---

## Avertissements importants

### **À lire avant utilisation**
```{warning}

Avant d'utiliser le FlexiBowl®, il est obligatoire de :
- Lire intégralement ce manuel afin de garantir une utilisation correcte du système
- Respecter les instructions opérationnelles et les recommandations
- Former de manière adéquate le personnel chargé de l'utilisation
- Consulter les manuels d'instructions de tous les composants matériels raccordés (FlexiVision One, Bulk Feeder, VisionController, caméra, robot, etc.)

Le non-respect de ces indications peut provoquer des dysfonctionnements, des dommages aux équipements ou des situations dangereuses.
```
### **Contexte opérationnel et limitations de responsabilité**

Le FlexiBowl® est un système d'alimentation flexible à disque rotatif vibrant pour le positionnement et l'orientation aléatoires des composants en vue du prélèvement robotisé.

```{warning}
Pendant l'utilisation, l'opérateur doit :
- Tenir compte de l'encombrement physique du système
- Surveiller les mouvements du robot et de l'alimentateur
- Prévoir et gérer les situations opérationnelles imprévues
- Respecter les normes de sécurité applicables aux robots et aux machines industrielles
```
```{warning}
**ARS S.r.l. décline toute responsabilité pour les dommages aux personnes ou aux biens résultant du mouvement des machines et des systèmes raccordés au logiciel FlexiVision One.**

L'intégration du système dans l'environnement de travail et l'évaluation des risques relèvent de la responsabilité de l'intégrateur de système et de l'utilisateur final.
```

(operatori)=
## Opérateurs

Afin d'établir avec certitude les compétences et les qualifications des opérateurs affectés aux différentes tâches (mise en marche, nettoyage, maintenance courante), consulter le tableau suivant :

:::{list-table}
:header-rows: 1
:widths: 30 70

* - Qualification
  - Définition

* - **Intégrateur de système**
  - Personnel chargé de la conception des implantations, du dimensionnement des composants et de la vérification des exigences techniques pour l'installation du FlexiBowl®.

* - **Technicien installateur**
  - Personnel chargé du montage mécanique, du raccordement électrique et pneumatique et de la configuration du réseau.

* - **Opérateur**
  - Personnel de l'utilisateur formé et habilité à l'utilisation et à la conduite de la machine à des fins de production, pour les activités pour lesquelles elle a été construite et fournie. Il doit être en mesure d'exécuter toutes les opérations nécessaires au bon fonctionnement de la machine et à la sécurité de lui-même et de ses éventuels collaborateurs. Il doit avoir une expérience avérée dans l'utilisation correcte de ce type de machines et être formé, informé et instruit à ce sujet. En cas de doute, il doit signaler toute anomalie à son supérieur.

    **Remarque :** Non habilité à effectuer toute activité de maintenance.
    
* - **Technicien de maintenance mécanique**
  - Technicien qualifié capable de :

    * effectuer des activités de maintenance préventive/corrective sur toutes les parties mécaniques de la machine soumises à maintenance ou réparation ;
    * avoir accès à toutes les parties de la machine pour l'analyse visuelle, le contrôle de l'état des équipements, les réglages et les étalonnages ;
    * intervenir sur les organes mécaniques pour les réglages, la maintenance et les réparations ;
    * lire les schémas pneumatiques et hydrauliques, les dessins techniques et les listes des pièces de rechange.

    Dans des cas exceptionnels, il est autorisé à faire fonctionner la machine avec des sécurités réduites. Si nécessaire, il peut donner à l'opérateur des instructions pour une bonne utilisation de la machine à des fins de production.

    **Remarque :** Non habilité à intervenir sur des installations électriques sous tension (le cas échéant).

* - **Mainteneur électricien**
  - Technicien qualifié capable de :
    * effectuer des activités de maintenance préventive/corrective sur toutes les parties mécaniques de la machine soumises à maintenance ou réparation ;
    * avoir accès à toutes les parties de la machine pour l'analyse visuelle, le contrôle de l'état des équipements, les réglages et les étalonnages ;
    * conduire la machine comme l'opérateur ;
    * intervenir sur les réglages et sur les installations électriques pour la maintenance, la réparation et le remplacement des pièces usées ;
    * lire les schémas électriques et vérifier le bon cycle fonctionnel. Si nécessaire, il peut donner à l'opérateur des instructions pour une bonne utilisation de la machine à des fins de production. Il peut intervenir sous tension à l'intérieur des armoires électriques, boîtes de dérivation, appareils de commande, etc. uniquement s'il s'agit d'une personne qualifiée (PEI). (Se référer à la norme **EN50110-1**). Il n'effectue pas de programmation logicielle de systèmes tels que les automates (logique ou sécurité) et ne peut pas modifier les mots de passe du système.

* - **Technicien expert logiciel**
  - Technicien qualifié capable de :
    * effectuer des activités préventives/correctives sur toutes les parties logicielles de la machine ;
    * avoir accès à toutes les parties de la machine pour l'analyse visuelle, le contrôle de l'état des équipements, les réglages et les étalonnages. Technicien qualifié du Constructeur avec une expérience avérée et une formation sur les systèmes basés sur : automate/PC, variateurs, etc. (connaissance de la programmation, des fonctions machine, etc.) pour des opérations complexes telles que, par exemple :
    * modification des données machine ;
    * création de programmes de travail ;
    * réglage des paramètres des variateurs, etc., du fait de sa connaissance du cycle de production, technologique et de construction de la machine fournie. Il peut intervenir à l'intérieur des armoires électriques, boîtes de dérivation, appareils de commande, etc. sous tension uniquement s'il s'agit d'une personne qualifiée (PEI) (se référer à la norme **EN50110-1**). Ses compétences sont de type électronique et/ou logiciel.

* - **Technicien du Constructeur**
  - Technicien qualifié par le Constructeur et/ou par son distributeur pour des opérations complexes, du fait de sa connaissance du cycle de production de construction de la machine. Cette personne intervient conformément aux demandes de l'utilisateur. Ses compétences sont de type mécanique.

* - **Personne formée**
  - Regroupe toutes les qualifications indiquées dans ce tableau : il s'agit d'une personne qui a été informée, instruite et formée sur le travail et sur les dangers éventuels découlant d'une utilisation inappropriée. Elle connaît en outre l'importance des dispositifs de sécurité, les règles de prévention des accidents et les conditions de travail en sécurité.

:::

---

## Remarques sur la documentation

### **Version et mises à jour**

```{note}

- **Langue de référence** : la version italienne de ce document est la version officielle et prévaut en cas de divergences avec d'autres traductions
- **Mises à jour** : les informations contenues sont susceptibles d'être modifiées sans préavis en vue d'améliorations du produit
- **Unités de mesure** : sauf indication contraire, toutes les dimensions sont exprimées en millimètres (mm)
- **Version du document** : vérifier toujours que vous disposez de la version la plus récente en consultant le site [www.flexibowl.it](https://www.flexibowl.it)
```
### **Comment tirer le meilleur parti de ce manuel**

```{tip}

Pour une expérience optimale :
- Utilisez le menu de navigation latéral pour passer rapidement d'une section à l'autre
- Consultez l'index initial pour identifier immédiatement la section qui vous intéresse
- Prêtez une attention particulière aux bandeaux d'avertissement, de remarque et de conseil
- Suivez les procédures dans l'ordre indiqué, surtout lors de l'installation initiale
- Conservez ce manuel au format numérique pour faciliter les recherches rapides par mots-clés
```

---


## Droits de reproduction et mentions légales

```{important}
**Copyright © ARS S.r.l. - Tous droits réservés**

Aucune partie de cette publication ne peut être reproduite, distribuée, traduite ou transmise par quelque moyen que ce soit (électronique, mécanique, photocopie, enregistrement ou autre système de stockage) à des fins autres que l'usage personnel, sans l'autorisation écrite préalable d'ARS S.r.l.

ARS S.r.l. décline toute responsabilité pour les conséquences découlant d'opérations erronées effectuées par l'utilisateur ou d'une utilisation inappropriée du produit.

**Marques déposées** : FlexiBowl® est une marque déposée d'ARS S.r.l. Toutes les autres marques, noms commerciaux et logos mentionnés dans ce document appartiennent à leurs propriétaires respectifs et sont utilisés exclusivement à des fins d'identification.
```
---


