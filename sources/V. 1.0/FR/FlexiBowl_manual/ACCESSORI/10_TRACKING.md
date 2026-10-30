(tracking)=
# **Flexitracking**

## Fonctionnement en tracking

L'option Flexitracking permet de maximiser la productivité du FlexiBowl® en le faisant tourner de manière continue et sans interruption. Au lieu de s'arrêter à chaque cycle pour prendre la photo et laisser au robot le temps de saisir les pièces présentes dans la zone de vision, un codeur suit l'angle de rotation effectué par la surface ou le disque rigide entre le moment de la prise de vue et celui de la saisie de la pièce par le robot.

::::{tip}
Le fonctionnement en tracking déplace la zone de saisie qui, si elle coïncide normalement avec la zone de vision, sera dans ce cas décalée vers l'aval. Se reporter au chapitre {ref}`Layout Best Practice <layoutbp>` pour plus d'informations sur le positionnement recommandé du robot et des autres accessoires en fonctionnement standard et en Flexitracking.

:::{figure} ../../../../_shared/media/images/TrackingLayout.PNG
:width: 80%
:align: center
:::

::::

Le Flexitracking se compose d'un groupe moteur modifié avec un support pour une transmission par courroie qui entraîne le codeur :

:::{figure} ../../../../_shared/media/images/GM001788.PNG
:width: 80%
:align: center
:::

