# **Maintenance et dépannage**

:::{warning}
Effectuer les opérations de maintenance lorsque la machine est à l'arrêt.
:::

:::{warning}
Les opérations de maintenance doivent être effectuées par du personnel qualifié et autorisé.
::: 

La maintenance de la machine comprend les interventions (inspection, vérification, contrôle, réglage et remplacement) rendues nécessaires par l'utilisation normale.

**Lignes directrices pour une maintenance correcte :**

<style>
  .isw-timeline-custom {
    display: flex !important;
    flex-direction: column !important;
    position: relative !important;
    padding-left: 45px !important;
    margin: 2.5rem 0 !important;
    list-style: none !important;
  }

  .isw-timeline-custom .isw-timeline-item-fixed {
    display: block !important;
    position: relative !important;
    padding-bottom: 2.5rem !important;
  }

  .isw-timeline-custom .isw-timeline-item-fixed:last-child {
    padding-bottom: 0 !important;
  }

  /* Forza la card con il tuo bordo azzurro e sfondo alternativo */
  .isw-timeline-custom .isw-card-fixed {
    display: block !important;
    padding: 1.4rem !important;
    border: 2px solid var(--c-accent, #2980b9) !important;
    border-radius: var(--radius, 10px) !important;
    background: var(--c-bg-alt, #f7fbfe) !important;
    box-shadow: var(--shadow-sm, 0 1px 4px rgba(41,128,185,.08)) !important;
  }

  /* Forza lo stile del titolo */
  .isw-timeline-custom .isw-card-fixed .isw-symbol-label {
    color: var(--c-accent, #2980b9) !important;
    font-size: 19px !important;
    font-weight: 700 !important;
    margin-bottom: 0.5rem !important;
    display: block !important;
    text-transform: none !important;
  }

  /* Linea verticale tratteggiata */
  .isw-timeline-custom .isw-timeline-item-fixed::before {
    content: '' !important;
    position: absolute !important;
    left: -24px !important;
    top: 25px !important;
    bottom: -15px !important;
    width: 2px !important;
    border-left: 2px dashed var(--c-accent, #2980b9) !important;
    z-index: 1 !important;
  }

  .isw-timeline-custom .isw-timeline-item-fixed:last-child::before {
    display: none !important;
  }

  /* Punta della freccia a V minimale */
  .isw-timeline-custom .isw-timeline-arrow-fixed {
    display: block !important;
    content: '' !important;
    position: absolute !important;
    left: -28px !important;
    bottom: 8px !important;
    width: 8px !important;
    height: 8px !important;
    border-right: 2px solid var(--c-accent, #2980b9) !important;
    border-bottom: 2px solid var(--c-accent, #2980b9) !important;
    transform: rotate(45deg) !important;
    z-index: 2 !important;
    background: var(--c-bg, #ffffff) !important;
  }
</style>

<div class="isw-timeline-custom">
  
  <div class="isw-timeline-item-fixed">
    <div class="isw-timeline-arrow-fixed"></div>
    <div class="isw-card-fixed">
      <span class="isw-symbol-label">Composants</span>
      <div class="isw-symbol-desc">N'utiliser que des pièces de rechange d'origine et des outils adaptés à l'usage et en bon état.</div>
    </div>
  </div>

  <div class="isw-timeline-item-fixed">
    <div class="isw-timeline-arrow-fixed"></div>
    <div class="isw-card-fixed">
      <span class="isw-symbol-label">Fréquences d'intervention</span>
      <div class="isw-symbol-desc">Respecter les échéances indiquées dans le manuel pour la maintenance programmée (préventive et périodique). L'intervalle de temps ou les cycles de travail entre deux interventions s'entendent comme la valeur maximale acceptable et ne doivent pas être dépassés.</div>
    </div>
  </div>

  <div class="isw-timeline-item-fixed">
    <div class="isw-timeline-arrow-fixed"></div>
    <div class="isw-card-fixed">
      <span class="isw-symbol-label">Surveillance préventive</span>
      <div class="isw-symbol-desc">Vérifier rapidement la cause d'éventuelles anomalies telles qu'un bruit excessif, des surchauffes, des fuites de fluides, etc.</div>
    </div>
  </div>

  <div class="isw-timeline-item-fixed">
    <div class="isw-card-fixed">
      <span class="isw-symbol-label">Réactivité</span>
      <div class="isw-symbol-desc">
        L'élimination immédiate des causes d'anomalie ou de dysfonctionnement évite d'autres dommages aux équipements et garantit la sécurité des opérateurs.
      </div>
    </div>
  </div>

</div>

Le personnel préposé doit être bien formé et avoir une connaissance approfondie des règles de prévention des accidents. Le personnel non autorisé doit rester à l'extérieur de la zone de travail pendant les opérations.

Les activités de nettoyage et de réglage sont effectuées uniquement et exclusivement en phase de maintenance, machine à l'arrêt, hors énergie et armoire électrique sectionnée.

:::{important}
En cas de doute, il est interdit d'intervenir. Consulter le Constructeur pour les éclaircissements nécessaires.
:::

:::{attention}
Les interventions de réparation ou de maintenance non prévues dans le présent manuel ne peuvent être effectuées qu'avec l'autorisation préalable d'ARS S.r.l. Aucune responsabilité relative à des dommages aux personnes ou aux biens ne peut être imputée à ARS S.r.l. pour des interventions différentes de celles décrites ou exécutées selon des modalités différentes de celles indiquées.
:::

### Classification opérationnelle des maintenances

| Type de maintenance | Description |
| :--- | :--- |
| **Maintenance ordinaire** | Opérations préventives visant à garantir le bon fonctionnement de la machine dans le temps (inspection, contrôle, réglage, nettoyage et lubrification). |
| **Maintenance extraordinaire** | Interventions correctives en fonction des besoins (révision, réparation, rétablissement des conditions nominales ou remplacement d'un ensemble en panne, défectueux ou usé). |

---

## Avertissements de sécurité 

:::{attention} 
Avant de commencer toute intervention de maintenance sur la machine, sectionner et cadenasser toutes les sources d'énergie, et mettre en condition de blocage de sécurité les groupes mobiles qui la composent. Apposer le panneau « Machine en maintenance - ne pas mettre sous tension » près de l'interrupteur général.
:::

:::{attention}
Lorsque la machine est en maintenance, afin d'éviter qu'elle ne puisse être mise en marche accidentellement, apposer des panneaux portant la mention : « ATTENTION ! Machine en maintenance ».
:::

<div class="isw-page">
  <div class="isw-timeline-container">
    <div class="isw-timeline-item">
      <div class="isw-timeline-arrow"></div>
      <div class="isw-timeline-card">
        <span class="isw-symbol-label">EPI</span>
        <div class="isw-symbol-desc">Les agents de maintenance doivent obligatoirement porter tous les équipements de protection individuelle nécessaires (gants, lunettes, combinaisons) à l'activité à effectuer.</div>
      </div>
    </div>
    <div class="isw-timeline-item">
      <div class="isw-timeline-arrow"></div>
      <div class="isw-timeline-card">
        <span class="isw-symbol-label">Signalisation</span>
        <div class="isw-symbol-desc">Si l'opération prévoit le retrait de protections, délimiter la zone d'intervention et signaler l'interdiction d'accès aux personnes étrangères.</div>
      </div>
    </div>
    <div class="isw-timeline-item">
      <div class="isw-timeline-arrow"></div>
      <div class="isw-timeline-card">
        <span class="isw-symbol-label">Vérification de la déconnexion</span>
        <div class="isw-symbol-desc">Avant de procéder à toute activité, vérifier la déconnexion effective des sources d'énergie (courant électrique, air comprimé, énergie hydraulique, etc.).</div>
      </div>
    </div>
    <div class="isw-timeline-item">
      <div class="isw-timeline-card">
        <span class="isw-symbol-label">Compétence</span>
        <div class="isw-symbol-desc">L'agent de maintenance ne doit exécuter que les opérations relevant de sa compétence (Mécanique, Électrique, Fluidique) pour lesquelles il est expressément autorisé, en utilisant l'instrumentation adaptée à la recherche de pannes.</div>
      </div>
    </div>
  </div>
</div>

---

## Maintenance ordinaire 

La maintenance ordinaire permet de contrôler les conditions mécaniques et la propreté de la machine. Les périodicités indiquées se réfèrent à des conditions de fonctionnement normales.

:::{important}
Pour la maintenance ordinaire des machines provenant de fournisseurs externes, se référer aux manuels des sous-traitants joints.
::: 

:::{important}
Pour la fixation des vis, utiliser toujours LOCTITE 243 afin de garantir un serrage antivibratoire parfait.
:::

### Contrôles et vérifications

#### Tableau de maintenance ordinaire – Contrôles

| Opération | Quotidienne | Hebdomadaire | Mensuelle | Semestrielle | Annuelle |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Contrôle de l'état de la cuve avant chaque démarrage | ◈ | | | | |
| Contrôle de l'état d'usure des relais | | | |  | ◈ |
| Contrôle du bon fonctionnement des fusibles | | | |  | ◈ |
| Contrôle de l'état d'usure des ressorts à lames | | | | ◈ |  |
| Contrôle du bon fonctionnement de l'électroaimant | | | | ◈ |  |
| Contrôle de l'usure du revêtement en polyuréthane *(le cas échéant)* | | | ◈ | |  |

#### Vérification des dispositifs de sécurité

Pour vérifier l'intégrité des systèmes de protection, effectuer les étapes suivantes :

<div style="display: flex; flex-direction: column; gap: 12px; margin: 20px 0;">
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #34495e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">1</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Vérifier que tous les capots et carters de la machine sont présents et correctement fixés.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #34495e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">2</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Vérifier que le câble d'alimentation électrique ne présente pas de dommages, de coupures ou de signes d'usure superficielle.
    </div>
  </div>
</div>

#### Nettoyage

:::{attention} 
Les opérations de nettoyage doivent être effectuées uniquement par du personnel qualifié et autorisé.
:::

:::{attention} 
Pour nettoyer la machine, ne pas utiliser de fragments d'éponge, de chiffons humides et/ou abrasifs, de chiffons filamenteux, d'essence ou de solvants inflammables comme détergent.
:::

:::{attention} 
Ne pas utiliser d'acides ni de solvants chimiques agressifs pour nettoyer la base du Bulk Feeder.
:::

:::{important}
Utiliser des produits doux et non abrasifs, tels que des dégraissants neutres ou du savon domestique ordinaire. Pour enlever les fragments et les poussières, utiliser un pinceau en veillant à porter des lunettes de protection.
:::

#### Tableau de maintenance ordinaire – Nettoyage

| Opération | Quotidienne | Hebdomadaire | Mensuelle | Semestrielle | Annuelle |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Élimination des résidus et déchets de process de la surface de la cuve | ◈ | | | | |
| Élimination de la graisse et de l'huile avec des produits ou solvants neutres | ◈ |  | | | |
| Nettoyage général de la machine | | ◈ |  | | |

#### Procédure de nettoyage général

<div style="display: flex; flex-direction: column; gap: 12px; margin: 20px 0;">
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #7f8c8d; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">1</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Débrancher complètement l'alimentation électrique de la machine.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #7f8c8d; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">2</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Retirer manuellement les éventuels résidus de produit accumulés.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #7f8c8d; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">3</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Éliminer la saleté localisée à l'aide de solvants du commerce non inflammables et non toxiques.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #7f8c8d; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">4</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Si nécessaire, utiliser un aspirateur pour retirer les petits résidus présents sur la surface tournante.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #7f8c8d; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">5</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Une fois le nettoyage terminé, rétablir les raccordements de la machine.
    </div>
  </div>
</div>

:::{important}
Le nettoyage général de la machine doit être effectué chaque fois que le type de composant à traiter est changé, afin d'éliminer les résidus contaminants du traitement précédent.
:::

---

## Maintenance extraordinaire

:::{attention} 
La maintenance extraordinaire et la réparation de la machine sont réservées aux techniciens qualifiés, formés et autorisés, employés par le Constructeur ou par le centre d'assistance agréé.
:::

Si des événements exceptionnels surviennent nécessitant des interventions extraordinaires, les agents de maintenance internes de l'utilisateur doivent :
1. Vérifier avec précision l'état des ensembles endommagés ou déphasés.
2. Exécuter exclusivement les opérations décrites dans ce paragraphe, s'ils y sont autorisés.
3. Si les opérations ne sont pas prévues dans ce manuel, transmettre au Constructeur un rapport détaillé des faits, le résultat de l'inspection et les observations relevées.

:::{attention} 
Les pièces de rechange à remplacer doivent être commandées directement auprès d'ARS S.r.l. Si des pièces de rechange d'origine ou autorisées par écrit ne sont pas utilisées, le Constructeur décline toute responsabilité quant au fonctionnement de la machine et à la sécurité des opérateurs.
:::

:::{attention} 
Débrancher l'alimentation électrique et pneumatique avant toute opération de maintenance extraordinaire ou avant de retirer les capots de protection.
:::

:::{important}
Lors du serrage des vis, utiliser toujours du frein-filet LOCTITE 243 pour garantir la tenue mécanique.
:::

### Réglage de l'entrefer

L'entrefer est la distance physique entre le noyau et le contre-noyau ; un réglage millimétrique est fondamental :
* **Entrefer trop étroit :** Les surfaces du noyau et du contre-noyau entrent en contact mécanique pendant le fonctionnement, provoquant un « martèlement ».
* **Entrefer trop large :** Le courant électrique du vibrateur peut atteindre des niveaux critiques, provoquant la brûlure de l'enroulement et l'endommagement des composants internes du contrôleur.

:::{attention}
Ne faire fonctionner en aucun cas le vibrateur si l'une des deux conditions décrites ci-dessus se présente.
:::

:::{important}
L'entrefer est étalonné de manière appropriée en usine ; des interventions de réglage ne sont nécessaires qu'en cas de manipulations inappropriées ou d'application de surtensions.
:::

| Données opérationnelles | Spécifications d'intervention |
| :--- | :--- |
| **Qualification de l'opérateur** | Agent de maintenance mécanique |
| **Outils à utiliser** | Clé à fourche |

#### Procédure de réglage de l'entrefer

![Réglage de l'entrefer](../../../../../_shared/media/images/regolazione_traferro.png)

<div style="display: flex; flex-direction: column; gap: 12px; margin: 20px 0;">
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">1</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Desserrer le contre-écrou de blocage <strong>(Écrou 2)</strong>.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">2</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Visser la <strong>Vis 1</strong> dans le sens horaire jusqu'en fin de course, c'est-à-dire en butée mécanique contre le contre-noyau.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">3</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Dévisser la <strong>Vis 1</strong> dans le sens antihoraire : se reporter au tableau ci-dessous pour identifier la valeur correcte et faire effectuer à la vis le nombre de tours et de fractions nécessaires pour régler la distance correcte.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">4</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Serrer à fond l'<strong>Écrou 2</strong> pour assurer la stabilité de la vis de réglage 1.
    </div>
  </div>
</div>

:::{note} 
 Le réglage de l'entrefer est une opération de précision qui peut nécessiter des vérifications répétées pour obtenir le réglage idéal.
:::
![Réglage de l'entrefer](../../../../../_shared/media/images/disegno_tecnico.png)

#### Tableau technique de référence de l'entrefer

| Modèle | Taille de l'aimant | Entrefer requis | Rotation de la vis de réglage |
| :---: | :---: | :---: | :---: |
| **1,5 l** | Ø21 | 1,5 mm | 360° (1 tour complet) |
| **3 l** | Ø24 | 2 mm | 480° (1 tour + 1/3) |
| **5 l** | Ø28 | 3 mm | 720° (2 tours complets) |
| **10 l** | Ø28 | 3 mm | 720° (2 tours complets) |
| **20 l** | Ø28 | 3 mm | 720° (2 tours complets) |
| **40 l** | 32x30 | 3 mm | 720° (2 tours complets) |

### Remplacement des ressorts à lames

| Données opérationnelles | Spécifications d'intervention |
| :--- | :--- |
| **Qualification de l'opérateur** | Agent de maintenance mécanique |
| **Outils à utiliser** | Clé à fourche |

La modification du dimensionnement du paquet de ressorts à lames (nombre et épaisseur des lames) sert à faire varier et à adapter la capacité utile du vibrateur.

#### Procédure de remplacement des ressorts à lames

<div style="display: flex; flex-direction: column; gap: 12px; margin: 20px 0;">
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">1</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Intervenir sur un seul paquet de ressorts à lames à la fois, en commençant impérativement par celui situé du côté arrière.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">2</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Noter ou photographier la position exacte et l'ordre de séquence de chaque ressort à lames, entretoise et bride de retenue.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">3</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Retirer les boulons d'ancrage mécanique à la base puis les boulons de fixation au pont du canal vibrant.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">4</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Remplacer les éléments usés ou fissurés par des pièces de rechange d'origine.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">5</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Remonter le paquet de ressorts à lames en suivant exactement l'ordre inverse du démontage.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">6</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Serrer toutes les vis en appliquant le couple de serrage indiqué dans le tableau suivant.
    </div>
  </div>
</div>

#### Tableau technique des ressorts à lames et couples de serrage

| Modèle | Taille des ressorts à lames | Épaisseur des lames | Couple de serrage et filetage |
| :---: | :---: | :---: | :--- |
| **1,5 l** | 40x48 mm | 1 - 1,5 - 2 mm | 7,5 N·m – M5 |
| **3 l** | 40x48 mm | 1 - 1,5 - 2 mm | 7,5 N·m – M5 |
| **5 l** | 70x82 mm | 1,5 - 2 mm | 30 N·m – M8 |
| **10 l** | 70x82 mm | 1,5 - 2 mm | 30 N·m – M8 |
| **20 l** | 70x82 mm | 1,5 - 2 mm | 30 N·m – M8 |
| **40 l** | 80x91 mm | 1,5 - 2 - 2,5 mm | 70 N·m – M10 |

### Remplacement de la cuve

| Données opérationnelles | Spécifications d'intervention |
| :--- | :--- |
| **Qualification de l'opérateur** | Agent de maintenance mécanique |
| **Outils à utiliser** | Clé à fourche |

#### Procédure de démontage et de montage de la cuve

<div style="display: flex; flex-direction: column; gap: 12px; margin: 20px 0;">
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">1</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Soutenir fermement la cuve pour éviter sa chute accidentelle lors du retrait.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">2</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Desserrer les quatre vis sans tête de serrage présentes sur la plaque de base de la cuve.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">3</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Soulever avec précaution la cuve d'origine et l'extraire de son logement.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">4</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Retirer le joint de la plaque de base.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">5</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Positionner le joint sur la nouvelle cuve en vérifiant son logement correct.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">6</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Insérer la nouvelle cuve dans son logement en vérifiant sa bonne insertion sur les goujons de serrage et le bon positionnement du joint.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">7</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Serrer les quatre vis sans tête présentes sur la plaque de base pour fixer la nouvelle cuve.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">8</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Vérifier que la nouvelle cuve est correctement positionnée et solidement fixée.
    </div>
  </div>
</div>

![Démontage et montage de la cuve](../../../../../_shared/media/images/vasca.jpg)

:::{attention}
Dans le cas de modèles personnalisés, les composants peuvent différer, en partie ou en totalité, de ceux indiqués. Pour ces modèles, il faut se référer au dossier technique du projet.
:::

---

## Dépannage

:::{attention}
Pendant le fonctionnement normal, le vibrateur doit fonctionner silencieusement. En cas de bruit sourd causé par un martèlement interne, éteindre immédiatement le système.
:::

En cas de martèlement, contrôler et rétablir l'entrefer optimal : si les surfaces sont trop proches, elles s'entrechoqueront mécaniquement ; si elles sont trop éloignées, l'élévation anormale du courant brûlera les enroulements du stator.

| Symptôme constaté | Cause racine possible | Action corrective requise |
| :--- | :--- | :--- |
| **Le vibrateur fonctionne trop lentement** | La tension d'alimentation est inférieure au seuil nominal. | Augmenter la tension électrique jusqu'à la valeur correcte de plaque. |
| | L'unité entre en contact avec des objets rigides externes ou des structures adjacentes. | Rétablir les jeux physiques en isolant l'unité vibrante (3-5 cm). |
| | L'oscillation des paquets de ressorts à lames est entravée ou freinée par des accumulations. | Démonter, nettoyer à fond et éliminer les résidus des paquets de ressorts à lames. |
| | Les ressorts à lames présentent des fissures, des défauts ou un fléchissement structurel. | Procéder au remplacement immédiat du jeu de ressorts à lames. |
| | Le canal vibrant est fissuré ou mécaniquement usé. | Remplacer le canal. |
| **Le vibrateur fonctionne trop vite** | La tension d'alimentation dépasse les limites nominales *(cause première de martèlement)*. | Stabiliser et réduire la tension d'alimentation à la valeur de plaque. |
| **L'unité émet un bruit (ronflement) mais ne vibre pas** | La carte électronique de régulation à l'intérieur du boîtier est défectueuse. | Remplacer la carte électronique du contrôleur. |
| **L'unité ne s'active pas et ne répond pas** | Absence totale d'alimentation électrique en entrée du contrôleur. | Inspecter la ligne et éliminer d'éventuelles coupures électriques. |
| | Le disjoncteur magnétothermique ou le fusible de protection est coupé. | Remplacer les fusibles ou réarmer. |
| | La carte électronique interne au boîtier de commande est endommagée. | Remplacer la carte électronique. |
| | L'enroulement interne du vibrateur est brûlé ou décharge à la masse. | Remplacer l'ensemble électroaimant. |
| | L'enroulement est en court-circuit interne. | Remplacer l'enroulement. |
| | L'enroulement du rhéostat de réglage est ouvert. | Remplacer le composant défectueux. |


