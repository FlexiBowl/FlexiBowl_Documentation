# **Configuration du Bulk Feeder**


Cette page vous guide dans la mise en service du Bulk Feeder vibrant, l'accessoire optionnel qui alimente le FlexiBowl® de façon continue et uniforme. Suivez les quatre phases dans l'ordre : positionnement et montage mécanique, connexions électriques, réglage de l'adresse de communication et configuration des paramètres depuis l'interface logicielle.

<script src="https://unpkg.com/@phosphor-icons/web"></script>

<div class="quickstart-workflow">
  <style>
    .quickstart-workflow {
      font-family: inherit;
      max-width: 680px;
      margin: 2.5rem auto;
      padding: 0 1rem;
    }

    .qs-step {
      display: flex;
      align-items: stretch;
      gap: 1.25rem;
      margin-bottom: 0;
    }

    .qs-step:hover .qs-card {
      border-color: #2980b9;
      background: #f0f7ff;
      transform: translateX(4px);
    }

    .qs-step:hover .qs-number {
      background: #2980b9;
    }

    .qs-left {
      display: flex;
      flex-direction: column;
      align-items: center;
      flex-shrink: 0;
      width: 44px;
    }

    .qs-number {
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: #3498db;
      color: #fff;
      font-weight: 700;
      font-size: 1rem;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      transition: background 0.2s;
    }

    .qs-connector {
      flex: 1;
      width: 3px;
      background: linear-gradient(to bottom, #3498db 0%, #bcd6ec 100%);
      margin: 6px auto 0;
      min-height: 32px;
    }

    .qs-last .qs-connector {
      display: none;
    }

    .qs-card {
      flex: 1;
      border: 1.5px solid #d0e4f0;
      border-radius: 10px;
      padding: 0.85rem 1.1rem;
      background: #fff;
      transition: border-color 0.2s, background 0.2s, transform 0.2s;
      margin-bottom: 0.65rem;
    }

    .qs-card-title {
      font-weight: 700;
      font-size: 1rem;
      color: #1a3a52;
      margin-bottom: 0.3rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .qs-card-title i {
      font-size: 1.2rem;
      color: #1a3a52;
      flex-shrink: 0;
    }

    .qs-title-link {
      color: inherit;
      text-decoration: none;
    }

    .qs-title-link:hover {
      color: #2980b9;
      text-decoration: none;
    }

    .qs-card-desc {
      font-size: 0.875rem;
      color: #556b7d;
      margin: 0;
      line-height: 1.45;
    }
  </style>

  <!-- Step 1 -->
  <div class="qs-step">
    <div class="qs-left">
      <div class="qs-number">1</div>
      <div class="qs-connector"></div>
    </div>
    <div class="qs-card">
      <div class="qs-card-title">
        <i class="ph ph-package"></i>
        <a class="qs-title-link" href="conf_tramoggia.html#posizionamento-e-installazione-meccanica">Positionnement et installation mécanique</a>
      </div>
      <p class="qs-card-desc">
        Positionnez le Bulk Feeder en respectant l'orientation correcte par rapport au FlexiBowl® et fixez-le à l'étrier de support.
      </p>
    </div>
  </div>

  <!-- Step 2 -->
  <div class="qs-step">
    <div class="qs-left">
      <div class="qs-number">2</div>
      <div class="qs-connector"></div>
    </div>
    <div class="qs-card">
      <div class="qs-card-title">
        <i class="ph ph-plugs"></i>
        <a class="qs-title-link" href="conf_tramoggia.html#collegamenti-elettrici">Connexions électriques</a>
      </div>
      <p class="qs-card-desc">
        Raccordez le contrôleur au Bulk Feeder, au FlexiBowl® (ou au rack) et à l'alimentation, en respectant l'ordre de connexion.
      </p>
    </div>
  </div>

  <!-- Step 3 -->
  <div class="qs-step">
    <div class="qs-left">
      <div class="qs-number">3</div>
      <div class="qs-connector"></div>
    </div>
    <div class="qs-card">
      <div class="qs-card-title">
        <i class="ph ph-hash"></i>
        <a class="qs-title-link" href="conf_tramoggia.html#indirizzo-di-comunicazione-rs485">Adresse de communication RS485</a>
      </div>
      <p class="qs-card-desc">
        Depuis le panneau du contrôleur, réglez une adresse unique, nécessaire pour communiquer avec le FlexiBowl® et d'éventuels autres Bulk Feeder.
      </p>
    </div>
  </div>

  <!-- Step 4 -->
  <div class="qs-step">
    <div class="qs-left">
      <div class="qs-number">4</div>
      <div class="qs-connector"></div>
    </div>
    <div class="qs-card">
      <div class="qs-card-title">
        <i class="ph ph-hash"></i>
        <a class="qs-title-link" href="conf_tramoggia.html#configurazione-da-interfaccia-software">Configuration depuis l'interface logicielle</a>
      </div>
      <p class="qs-card-desc">
        Activez le Bulk Feeder depuis l'interface web du FlexiBowl® et réglez l'amplitude, la fréquence et le temps d'activation de la vibration.
      </p>
    </div>
  </div>
</div>

---

## 1. Positionnement et installation mécanique

Les Bulk Feeder sont disponibles en plusieurs tailles, chacune avec sa propre charge maximale :

| Capacité | Charge maximale |
|---|---|
| 1,5 l | 1 kg |
| 3 l | 1,5 kg |
| 5 l | 6 kg |
| 10 l | 6 kg |
| 20 l | 6 kg |
| 40 l | 15 kg |

Le Bulk Feeder arrive déjà assemblé : il n'est pas nécessaire de le monter, il suffit de le positionner et de le fixer.

::::{tab-set}
:::{tab-item} Positionnement correct
![Positionnement correct du Bulk Feeder par rapport au FlexiBowl®](../../../../_shared/media/images/posizione_giustatramoggia.png)

La goulotte du Bulk Feeder doit déverser les composants directement dans la zone de travail du plateau, avec une inclinaison suivant le profil du FlexiBowl®.
:::
:::{tab-item} Positionnement incorrect
![Exemple de positionnement incorrect du Bulk Feeder](../../../../_shared/media/images/posizione_sbagliatatramoggia.png)

Une goulotte trop éloignée de la zone de travail génère une alimentation irrégulière et pénalise les performances de l'application.
:::
::::

**Étapes :**

1. Placez le Bulk Feeder sur une surface stable et horizontale, près du FlexiBowl®, en respectant l'orientation correcte indiquée ci-dessus.
2. Si le Bulk Feeder est installé sur le plan d'une machine sensible aux vibrations, interposez un matériau isolant et antivibratoire entre les deux surfaces, afin d'éviter que les vibrations du Bulk Feeder ne se transmettent au FlexiBowl®.
3. Fixez le Bulk Feeder à l'étrier de support par les trous prévus, à l'aide de vis M8 : le Bulk Feeder standard comporte 4 trous à la base, tandis que la version plus petite (1,5 l) en comporte 2.

## 2. Connexions électriques

:::{warning}
Avant d'effectuer ou de modifier toute connexion électrique, assurez-vous que le système est hors tension. Vérifiez toujours que le conducteur de terre est correctement installé et intact : la connexion électrique, y compris la mise à la terre, doit toujours être garantie pour le bon fonctionnement de la machine.
:::

![Schéma des connecteurs du contrôleur du Bulk Feeder](../../../../_shared/media/images/controller_digitale_connettori.png)

Le contrôleur du Bulk Feeder comprend : une entrée d'alimentation secteur (terre, phase, neutre), un connecteur RS485 pour la communication (A+, B-, GND), une sortie de puissance vers le moteur du Bulk Feeder et un interrupteur général.

**Étapes :**

1. Raccordez le contrôleur au Bulk Feeder à l'aide du câble dédié.
2. Raccordez le contrôleur au FlexiBowl® via le connecteur M12 codage A (communication Modbus RTU). Dans les installations multi-feeder avec rack, raccordez plutôt le contrôleur au rack.
3. Obturez tout connecteur non utilisé avec le capuchon prévu, afin de le protéger de la poussière et des débris. Le capuchon doit assurer une résistance de 120 Ω entre les canaux A+ et B- de la ligne RS485.
4. Branchez le câble d'alimentation au contrôleur : raccordez toujours en premier le côté contrôleur du câble, avant de brancher l'autre extrémité.
5. Avec l'interrupteur du contrôleur en position OFF, branchez le câble d'alimentation à la prise secteur. L'alimentation standard est de 115 ou 230 VAC ±5 % (la version 115 V n'est disponible que sur demande explicite).
6. Mettez le contrôleur sous tension avec l'interrupteur général.

:::{tip}
Le câble Modbus RTU entre le contrôleur et le FlexiBowl® est disponible en longueurs de 3, 5 et 10 m : voir {ref}`cavo-modbus`.
:::

:::{note}
Un seul FlexiBowl® prend en charge jusqu'à **4 Bulk Feeder**. Pour les installations multi-feeder, raccordez chaque Bulk Feeder à son propre contrôleur, raccordez le premier contrôleur au FlexiBowl® (ou au rack) et chaînez les contrôleurs suivants via le port du connecteur Bulk Feeder (daisy-chain). Obturez le port inutilisé du dernier contrôleur de la chaîne et branchez le câble d'alimentation à chaque contrôleur.
:::

## 3. Adresse de communication RS485

Chaque contrôleur de Bulk Feeder doit avoir une adresse de communication unique sur le réseau RS485 (paramètre **r**, plage 1–31). En présence de plusieurs Bulk Feeder, assurez-vous que chaque contrôleur du même réseau possède une adresse différente.

![Panneau avant du contrôleur : indicateurs, afficheur et commandes](../../../../_shared/media/images/tramoggia-pannello-controller.jpg)


**Étapes depuis le panneau du contrôleur :**

1. Maintenez **FUNC** enfoncé pendant 2 secondes pour entrer dans l'état de réglage des paramètres de base.
2. Appuyez plusieurs fois sur **FUNC** pour sélectionner le paramètre **r** (adresse de communication).
3. Appuyez sur **▲** ou **▼** pour modifier la valeur (1–31).
4. Maintenez à nouveau **FUNC** enfoncé pendant 2 secondes pour quitter et enregistrer.

## 4. Configuration depuis l'interface logicielle

Une fois les connexions terminées et l'adresse définie, le Bulk Feeder peut être configuré et commandé depuis la page dédiée de l'interface web du FlexiBowl®.

![Interface logicielle de configuration des Bulk Feeder](../../../../_shared/media/images/tramoggia-interfaccia-software.png)

Pour chacun des 4 Bulk Feeder disponibles, il est possible de régler :

| Champ | Description |
|---|---|
| **Enable** | Active le Bulk Feeder correspondant. |
| **ID** | Adresse RS485 du contrôleur connecté ; utilisez **Set New ID** pour en attribuer une nouvelle par logiciel. |
| **Status** | État actuel du Bulk Feeder (p. ex. Disabled). |
| **Amplitude** | Amplitude de la vibration. |
| **Frequency** | Fréquence de la vibration. |
| **Activation Time** | Durée, en millisecondes, de chaque impulsion de vibration. |

**Étapes :**

1. Accédez à l'interface web du FlexiBowl® et ouvrez la page des Bulk Feeder.
2. Sélectionnez **Enable** sur le Bulk Feeder à activer.
3. Vérifiez que le champ **ID** correspond à l'adresse définie sur le contrôleur (étape 3) ; dans le cas contraire, utilisez **Set New ID**.
4. Réglez les valeurs initiales d'**Amplitude**, **Frequency** et **Activation Time** en fonction du composant à alimenter.
5. Appuyez sur **Start Hopper** pour démarrer le Bulk Feeder et vérifier son fonctionnement ; ajustez les paramètres jusqu'à ce que l'alimentation des composants soit continue et uniforme.

:::{note}
Les valeurs optimales d'amplitude, de fréquence et de temps d'activation dépendent du composant et de la géométrie du Bulk Feeder : ajustez-les progressivement en observant le flux d'alimentation, en partant de valeurs basses et en augmentant jusqu'à obtenir une alimentation constante sans blocages.
:::

## Paramètres avancés du contrôleur 

### **Paramètres communs** 
Les paramètres communs peuvent être réglés à tout moment avec les touches **Vol+** / **Vol-**, même lorsqu'un autre paramètre est affiché :

![Paramètres communs du contrôleur](../../../../_shared/media/images/tramoggia-parametri-comuni.png)

| Définition | Symbole | Plage | Par défaut |
|---|---|---|---|
| Tension de sortie | U | 0–260 V | 50 |

### **Paramètres de base**
Pour accéder aux paramètres de base, maintenez **FUNC** enfoncé pendant 2 secondes ; appuyez sur **FUNC** pour faire défiler les paramètres, sur **▲/▼** pour les modifier, et maintenez **FUNC** enfoncé pendant 2 secondes pour quitter :

![Paramètres de base du contrôleur](../../../../_shared/media/images/tramoggia-parametri-base.png)

| Définition | Symbole | Plage | Par défaut |
|---|---|---|---|
| Fréquence de sortie | E | 40,0–200,0 Hz | 100,0 |
| Tension de sortie maximale réglable | h | 0–260 V | 260 |
| Adresse de communication | r | 1–31 | 1 |
| Débit en bauds de la communication | c | 0,3–115,2 kbit/s | 115,2 |
| Réinitialisation du contrôleur | — | — | — |

### **Réinitialisation du contrôleur**

![Procédure de réinitialisation du contrôleur](../../../../_shared/media/images/tramoggia-reset-controller.png)

1. Maintenez **FUNC** enfoncé pendant 2 secondes pour entrer dans l'état de réglage des paramètres de base.
2. Appuyez sur **FUNC** jusqu'à ce que le paramètre de réinitialisation (`88888`) clignote sur l'afficheur.
3. Maintenez **▲** enfoncé jusqu'à ce que `-----` apparaisse sur l'afficheur.
4. Relâchez **▲** pour terminer la réinitialisation : l'afficheur indiquera `U 50`, confirmant que l'opération a réussi.


