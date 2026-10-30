# **Air Blow Kit**

:::{note}
La mise en œuvre des soufflages entraîne une modification du circuit pneumatique du FlexiBowl® ; pour plus d'informations, se reporter aux {ref}`schémas pneumatiques <sc-pneum>`.
:::

Le kit de soufflage (ou *Air Blow Kit*) est composé des éléments suivants :

## Soufflage radial

Le soufflage radial consiste en une cartouche pouvant être montée à la place du déviateur standard, qui présente deux trous radiaux à des hauteurs différentes : par l'un des deux, au choix de l'opérateur en fonction des dimensions des pièces à manutentionner, sort un jet d'air qui éloigne les composants de l'anneau de retenue.

:::{figure} ../../../../_shared/media/images/sofrad500.PNG
:width: 100%
:align: center
:::

### Procédure de montage

:::{warning}
Déconnecter l'alimentation électrique avant de procéder au montage des soufflages.
:::

| Étape | Opération |
|:----:|-----------|
| 1 | Retirer les vis de fixation du déviateur |
| 2 | Dévisser les vis de réglage pour retirer le déviateur |
| 3 | Placer le joint plein et le joint percé dans leurs logements en fonction de la hauteur de soufflage souhaitée |
| 4 | Positionner la cartouche de soufflage radial et la fixer avec les vis prévues à cet effet |

### Procédure de réglage

Le soufflage radial peut être réglé aussi bien par logiciel que mécaniquement, en agissant sur la vis sans tête prévue à cet effet à l'intérieur de la cartouche avec une clé Allen de 1,5 mm, en veillant à bloquer sa position en vissant le poussoir avec un tournevis plat.

::::{raw} html
<figure style="text-align: center;">
  <video id="regsof500" width="100%" height="auto" controls>
    <source src="../../../../_shared/media/videos/FB500regsof.mp4" type="video/mp4">
    Votre navigateur ne prend pas en charge la vidéo.
  </video>
  <br>
  <label for="Velsof500">Vitesse :</label>
  <select id="Velsof500" onchange="document.getElementById('regsof500').playbackRate = this.value">
    <option value="0.5">0.5x</option>
    <option value="1" selected>1x</option>
    <option value="1.5">1.5x</option>
    <option value="2">2x</option>
  </select> 
  <figcaption><i>Procédure de réglage mécanique du soufflage radial illustrée sur un FlexiBowl® 500</i></figcaption>
</figure>
::::

Il est en outre possible de choisir la hauteur de soufflage en échangeant le joint avec le bouchon sous la cartouche :

:::{figure} ../../../../_shared/media/images/sofrad500-sm.PNG
:width: 100%
:align: center
:::

## Soufflage central

Le soufflage central consiste en une buse montée sur la pointe de l'écran flip, dont le jet d'air est orienté de manière à éloigner les composants de la calotte de serrage du disque. Son rôle est double :

- Amener les composants au-dessus du flip pour en maximiser l'efficacité ;
- Éviter que les composants soient considérés comme non saisissables en raison d'une trop grande proximité avec la calotte de serrage du disque, ce qui provoquerait une collision du robot.

:::{figure} ../../../../_shared/media/images/sofcen500.PNG
:width: 100%
:align: center
:::

### Procédure de montage

| Étape | Opération |
|:----:|-----------|
| 1 | Retirer l'ensemble écran-barrière flip en dévissant les quatre vis de fixation |
| 2 | Remplacer l'écran par l'ensemble de soufflage central |
| 3 | Fixer le nouvel ensemble soufflage central-barrière flip |

### Procédure de réglage 

Le réglage de l'intensité du soufflage s'effectue par logiciel. En outre, en vissant ou en dévissant des mêmes quantités les vis de réglage des soufflages radiaux, il est possible d'étrangler ou de relâcher le flux d'air qui arrive au soufflage central.

## Applications recommandées

Ils sont à privilégier par rapport au déviateur standard lorsque :
- il est nécessaire de manutentionner des composants présentant des détails ou des saillies de petites dimensions, susceptibles de se coincer dans le jeu entre le déviateur et la surface ou le disque rigide ;
- une surface ou un disque rigide anti-roll est utilisé.

## Vérification du bon fonctionnement

Des soufflages radiaux bien réglés se comportent de la manière suivante :

* Le soufflage en amont du flip amène les composants à environ la moitié du rayon du FlexiBowl®, là où le flip est le plus efficace pour retourner et séparer les pièces ;

* Le soufflage central éloigne les pièces de la calotte de serrage du disque de manière à éviter toute collision avec l'outil de préhension ;

* Le soufflage en aval du flip éloigne légèrement les composants du bord du FlexiBowl®, de manière à prévenir d'éventuelles collisions avec l'outil de préhension.