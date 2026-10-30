# **Ancien contrôleur**
## Contrôleur standard

#### Connexions électriques et configuration du contrôleur

:::{attention}
Avant de mettre le contrôleur sous tension, branchez la fiche Schuko à la prise de courant en vérifiant que l'installation dispose d'un système de mise à la terre adéquat.
:::

Pour effectuer le démarrage, procédez comme décrit :

<div style="display: flex; flex-direction: column; gap: 12px; margin: 20px 0;">
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #34495e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">1</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Raccordez le câble de la base linéaire au connecteur de sortie du contrôleur (c'est-à-dire raccordez le vibrateur au connecteur de sortie <strong>(1)</strong>).
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #34495e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">2</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Tournez le bouton de réglage de la fréquence <strong>(2)</strong> et le bouton de réglage de l'amplitude <strong>(3)</strong> du contrôleur sur la position « • ».
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #34495e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">3</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Mettez le contrôleur sous tension avec le bouton ON/OFF (bouton en position 1 <strong>(4)</strong>).
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #34495e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">4</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Tournez lentement les boutons de réglage <strong>(2 et 3)</strong>. Avant de porter la vibration au maximum (potentiomètre Amplitude <strong>(3)</strong>), il est conseillé de rechercher avec le potentiomètre Frequency <strong>(2)</strong> la fréquence de résonance correcte (50 Hertz).
    </div>
  </div>
</div>

![Contrôleur avec repères](../../../../../_shared/media/images/controller_puntatori.png)

Pour respecter la réglementation CEM, le circuit est doté d'un filtre avec des courants de fuite à la terre inférieurs à 1 mA.
 Le circuit fournit au vibrateur un signal PWM (modulation de largeur d'impulsion) réglable en amplitude et en fréquence, compensé par rapport aux variations de la tension de ligne.
  La section de commande est isolée galvaniquement de la section de puissance.
   À la mise sous tension, le circuit attend quelques secondes avant d'activer le vibrateur.

Le circuit est commandé par microprocesseur et dispose d'une limitation du courant de sortie par le fusible F4 (4 A).

**Protections par fusibles**

| Fusible | Valeur | Position |
| :--- | :--- | :--- |
| **F1** | 6,3 A | Entrée de ligne |
| **F3** | 250 mA | Entrée ON/OFF — limite le courant disponible pour le capteur NPN/PNP et l'éventuelle électrovanne |
| **F4** | 4 A | Sortie vibrateur |

**Indicateurs LED à l'intérieur de la carte**

| LED | Couleur | État : allumé |
| :--- | :--- | :--- |
| **LD1** | Rouge | Haute tension présente sur les condensateurs de filtrage (jusqu'à plus de 300 V avec une ligne à 230 V) |
| **LD2** | Vert | Tension présente dans le circuit de commande. Éteint si F1, F2 ou F3 sont coupés |
| **LD3** | Vert | Relais ON/OFF commuté — vibrateur en marche ou à l'arrêt |
| **LD4** | Jaune | Relais commuté suite au dépassement du temps d'absence de pièces |

:::{attention}
Évitez absolument de toucher le circuit lorsque la LED rouge (LD1) est allumée.
:::

Les relais associés à LD3 et LD4 exposent un contact inverseur sur les connecteurs **CONN4** et **CONN5** : **CONN4** permet la commande en cascade d'un module supplémentaire, **CONN5** l'activation d'une alarme de flux de pièces.

**Réglages disponibles**

Les trimmers de la carte permettent d'adapter le comportement du vibrateur à l'application :

- **TR2** — retard à l'arrêt du vibrateur (0 ÷ 10 s)
- **TR3** — retard au démarrage du vibrateur (0 ÷ 10 s)
- **TR4** — amplitude maximale
- **TR5** — retard supplémentaire au démarrage
- **TR6** — amplitude minimale

Le vibrateur peut être arrêté et redémarré par une commande externe sur **CONN3**, compatible avec un contact sec, un capteur NPN/PNP ou une sortie 0–24 V, avec ou sans les retards configurés.
 Avec **DP1**, il est possible de sélectionner la logique directe ou inversée du signal ON/OFF.

**Configuration standard recommandée par ARS**

| Composant | Réglage |
| :--- | :--- |
| **DP1** | Les deux interrupteurs en position ON |
| **DP2** | Interrupteur 2 ON — Interrupteur 1 OFF |
| **TR2 e TR3** | Vis de réglage tournée dans le sens antihoraire jusqu'en fin de course |
| **CONN3** | Démarrage d'un Bulk Feeder avec contact sec |

![Dessin du contrôleur](../../../../../_shared/media/images/disegno_controller.jpg)

---

### Contrôleur analogique

![Contrôleur analogique](../../../../../_shared/media/images/controller_analogico.png)

#### Connexions électriques et configuration du contrôleur

Pour effectuer le démarrage, procédez comme décrit et reportez-vous à l'image en fin de paragraphe :

<div style="display: flex; flex-direction: column; gap: 12px; margin: 20px 0;">
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">1</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Raccordez l'alimentation 80/250 Vac au connecteur <strong>CONN 1</strong>.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">2</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Raccordez le câble provenant de la base vibrante au connecteur <strong>CONN 2</strong>.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">3</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Raccordez la commande d'actionnement au connecteur <strong>CONN 3</strong>.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">4</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Raccordez l'entrée analogique au connecteur <strong>CONN 7</strong>.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">5</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Réglez le trimmer <strong>TR1</strong> de manière à ce que la fréquence soit égale à 50 Hertz.
    </div>
  </div>
</div>

Pour respecter la réglementation CEM, le circuit est doté d'un filtre avec des courants de fuite à la terre inférieurs à 1 mA.
 Le circuit fournit au vibrateur un signal PWM réglable en amplitude par un signal analogique et en fréquence par le trimmer **TR1**.
  Le signal est compensé par rapport aux variations de la tension de ligne. La section de commande est isolée galvaniquement de la section de puissance.
   À la mise sous tension, le circuit attend quelques secondes avant d'activer le vibrateur.

Le circuit est commandé par microprocesseur et dispose d'une limitation du courant de sortie par le fusible F4 (4 A).

**Protections par fusibles**

| Fusible | Valeur | Position |
| :--- | :--- | :--- |
| **F1–F2** | 6,3 A | Entrée de ligne |
| **F3** | 250 mA | Entrée ON/OFF — limite le courant disponible pour le capteur NPN/PNP et l'éventuelle électrovanne |
| **F4** | 4 A | Sortie vibrateur |

**Indicateurs LED à l'intérieur de la carte**

| LED | Couleur | État : allumé |
| :--- | :--- | :--- |
| **LD1** | Rouge | Haute tension présente sur les condensateurs de filtrage (jusqu'à plus de 300 V avec une ligne à 230 V) |
| **LD2** | Vert | Tension présente dans le circuit de commande. Éteint si F1, F2 ou F3 sont coupés |
| **LD3** | Vert | Relais ON/OFF commuté — vibrateur en marche ou à l'arrêt |
| **LD4** | Jaune | Relais commuté suite au dépassement du temps d'absence de pièces |

:::{attention}
Évitez absolument de toucher le circuit lorsque la LED rouge (LD1) est allumée.
:::

Les relais associés à LD3 et LD4 exposent un contact inverseur sur les connecteurs **CONN4** et **CONN5** : **CONN4** permet la commande en cascade d'un module supplémentaire, **CONN5** l'activation d'une alarme de flux de pièces.

**Réglages disponibles**

Les trimmers de la carte permettent d'adapter le comportement du vibrateur à l'application :

- **TR2** — retard à l'arrêt du vibrateur (0 ÷ 10 s)
- **TR3** — retard au démarrage du vibrateur (0 ÷ 10 s)
- **TR4** — retard au-delà duquel l'alarme d'absence de pièces se déclenche (0 ÷ 10 s)
- **TR5** — temps d'activation supplémentaire de l'électrovanne de soufflage d'air après l'arrêt du vibrateur (0 ÷ 3 s)
- **TR6** — rampe à la mise en marche du vibrateur (0 ÷ 3 s)
- **TR7** — amplitude maximale sur le vibrateur

Le vibrateur peut être arrêté et redémarré par une commande externe sur **CONN3**, compatible avec un contact sec, un capteur NPN/PNP ou une sortie 0–24 V, avec ou sans les retards configurés.
 Avec **DP1**, il est possible de sélectionner la logique NC ou NO du signal ON/OFF.
 L'amplitude de vibration se règle en appliquant la tension analogique appropriée sur **CONN7**.

**Configuration standard recommandée par ARS**

| Composant | Réglage |
| :--- | :--- |
| **DP1** | Les deux interrupteurs en position ON |
| **DP2** | Interrupteur 1 ON — Interrupteur 2 OFF |
| **TR2 e TR3** | Vis de réglage tournée dans le sens antihoraire jusqu'en fin de course |
| **CONN3** | Démarrage d'un Bulk Feeder avec contact sec |


![Schéma du contrôleur](../../../../../_shared/media/images/controller_schema.png)