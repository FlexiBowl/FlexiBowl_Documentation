<style>
.compare-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  margin: 1rem 0 1.5rem;
}
@media (max-width: 680px) {
  .compare-grid { grid-template-columns: 1fr; }
}
.compare-card {
  border: 1px solid #5a9fd4;
  border-radius: 7px;
  overflow: hidden;
  font-size: 0.92rem;
}
.compare-card-header {
  padding: 0.5rem 1rem;
  font-weight: 700;
  font-size: 0.82rem;
  letter-spacing: 0.05em;
  color: #ffffff;
}
.v20 .compare-card-header { background: #1a4a7a; }
.v30 .compare-card-header { background: #1e6fbf; }
.compare-card-body {
  padding: 0.85rem 1rem;
}
.compare-card-body p, .compare-card-body li { margin: 0.25rem 0; }
.compare-card-body ul, .compare-card-body ol { padding-left: 1.2rem; margin: 0.4rem 0; }
.compare-card-body table {
  width: 100%;
  border-collapse: collapse;
  margin: 0.5rem 0;
  font-size: 0.88rem;
}
.compare-card-body table th {
  padding: 0.35rem 0.6rem;
  text-align: left;
  font-size: 0.78rem;
  font-weight: 700;
  border-bottom: 2px solid #5a9fd4;
  opacity: 0.75;
}
.compare-card-body table td {
  padding: 0.35rem 0.6rem;
  border-bottom: 1px solid rgba(90, 159, 212, 0.3);
}
.compare-card-body table tr:last-child td { border-bottom: none; }
.compare-card-body pre {
  border: 1px solid rgba(90, 159, 212, 0.4);
  border-radius: 5px;
  padding: 0.7rem 0.9rem;
  font-size: 0.8rem;
  overflow-x: auto;
  margin: 0.5rem 0 0;
}
</style>
 
# **Comparatif logiciel**
 
Cette page compare les principales différences logicielles entre le **FlexiBowl® 2.0** et le **FlexiBowl® 3.0**, dans le but de guider l'utilisateur dans la compréhension des nouvelles fonctionnalités et des changements opérationnels introduits par la nouvelle génération.
 
:::{important}
Avant de lire le contenu de la présente page, il est recommandé de bien connaître les informations figurant dans la page [Interface logicielle](int_software)
:::
---
 
## 1. Protocoles de communication disponibles
 
| Protocole | FlexiBowl® 2.0 | FlexiBowl® 3.0 |
|---|---|---|
| TCP/IP – UDP | ✓ | ✓ (TCP Server) |
| EtherNet/IP | ✓ | ✓ |
| Profinet | ✗ | ✓ |
| Modbus | ✗ | ✓ |
| Digital I/O | ✓ | ✓ (en option) |
 
---
 
## 2. Interface utilisateur : comment elle est faite et comment y accéder
 
<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0 — Software Parameters</div>
<div class="compare-card-body">
 
Interface **desktop** appelée **FlexiBowl® Parameters**, à installer sur le PC de contrôle.
 
**Installation et accès :**
 
1. Installer le programme **FlexiBowl® Parameters** sur le PC (fourni par ARS).
2. Raccorder le PC au FlexiBowl® au moyen d'un **câble Ethernet** (LAN directe ou via un switch).
3. Lancer le programme et saisir l'**adresse IP** du FlexiBowl® pour se connecter.
 
Depuis l'écran **Main Commands**, les panneaux **Move**, **Shake** et **Option** sont accessibles au moyen d'onglets situés en haut.
 
</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0 — Interface web</div>
<div class="compare-card-body">
 
Interface **entièrement web** : aucune installation n'est requise. Un navigateur récent suffit.
 
**Accès :**
 
1. Raccorder le PC au FlexiBowl® via Ethernet.
2. Ouvrir le navigateur et saisir l'**adresse IP** du FlexiBowl® dans la barre d'adresse.
3. La **page d'accueil** de l'interface s'ouvre.
 
**Structure de l'interface :**
 
Le menu latéral comprend des pages dédiées à chaque fonction opérationnelle (Main Command, Jog Motor, Setup, Monitor, etc.), accessibles directement depuis le navigateur.
 
</div>
</div>
</div>
 
:::{note}
Si le système utilisé est **FlexiVision One**, la configuration est gérée depuis son interface dédiée. Il n'est pas nécessaire d'utiliser l'interface logicielle du FlexiBowl® décrite dans cette section.
:::
 
---
 
## 3. Comment modifier l'adresse IP
 
<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0</div>
<div class="compare-card-body">
 
1. Utiliser le programme fourni sur la clé USB.
2. Raccorder le FlexiBowl® au moyen d'un câble Ethernet.
3. Allumer l'appareil.
4. Lancer le programme.
5. Dans la case **IP Address**, saisir l'adresse : `192.168.1.10`
   *(Le PC connecté doit se trouver dans le même masque de sous-réseau de classe B — 255.255.0.0)*
6. Appuyer sur **Ping** → fenêtre contextuelle **« FlexiBowl® found »**.
7. Appuyer sur **Ok** pour activer **CONNECT** et lancer la connexion.
8. Après la connexion, l'écran d'accueil s'affichera.
 
</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0</div>
<div class="compare-card-body">
 
1. Ouvrir le navigateur et accéder à l'interface via l'IP actuelle.
2. Dans le menu latéral, ouvrir la page **Setup**.
3. Cliquer sur **Get IP** pour lire les paramètres réseau actuels.
4. Saisir la nouvelle adresse IP dans les champs prévus et cliquer sur **Set IP**.
5. Cliquer sur **Apply** pour confirmer, puis sur **Reboot** pour que les modifications soient prises en compte.
 
</div>
</div>
</div>
 
:::{note}
**FlexiBowl® 2.0** — Si une version précédente du programme est installée, il est nécessaire de la désinstaller au préalable.
:::
 
:::{important}
**FlexiBowl® 3.0** — Après le redémarrage, se reconnecter au FlexiBowl® en utilisant la nouvelle adresse IP définie.
:::
 
---
 
## 4. Comment gérer les mouvements
 
<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0</div>
<div class="compare-card-body">
 
Les mouvements sont configurés et testés depuis **Main Commands**, avec trois panneaux :
 
- **Move** : règle Acceleration, Deceleration, Speed et Angle au moyen d'un curseur ou d'un champ numérique. **Test Move** exécute le mouvement avec les valeurs définies.
- **Shake** : paramètres CCW Angle, CW Angle, Count, Acceleration, Deceleration et Speed. **Test Shake** exécute le shake.
- **Try Commands** : combine plusieurs commandes en une séquence avec une boucle configurable, en sélectionnant dans **All Commands** et en ajoutant à **Selected Commands**.
 
Pour la production via protocole, des commandes ASCII (par ex. `QX2` pour Move, `QX6` pour Shake) sont envoyées via le canal TCP/UDP configuré.
 
</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0</div>
<div class="compare-card-body">
 
Les mouvements sont organisés en **séquences** (jusqu'à 20), configurables depuis la page **Main Command**. Chaque séquence contient jusqu'à 10 emplacements de commande (Move, Shake, Flip, Blow).
 
Depuis la page **Main Command**, il est possible de :
 
- Sélectionner la séquence au moyen de **Select the sequence**.
- Définir tous les paramètres dans les champs numériques.
- Ajouter des commandes avec **Command Available** + **ADD** ; les réordonner avec **UP/DOWN** ; les supprimer avec **DELETE** ou vider la liste avec **CLEAR**.
- Tester avec **TEST SEQUENCE** ou démarrer la production avec **RUN**.
 
La page **Jog Motor** permet la rotation continue (Speed positive = sens horaire, négative = sens antihoraire) avec Flip et Blow intégrés.
 
Pour la production via protocole : `10[0]%` pour la Séquence 1 via TCP, ou ControlWord `10` via EtherNet/IP ou Profinet.
 
</div>
</div>
</div>
 
---
 
## 5. Comment modifier les paramètres
 
<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0</div>
<div class="compare-card-body">
 
Les paramètres opérationnels se modifient de deux manières :
 
- **Interface graphique** : curseurs ou champs numériques dans les écrans Move et Shake de **Main Commands**.
- **Via protocole (runtime)** : commandes `RW` (Write) et `RL` (Read) via TCP/UDP. Les valeurs doivent être multipliées par le **facteur de réduction** de la machine (obtenu avec la commande `RR114`), car les paramètres sont exprimés en unités internes du driver.
 
</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0</div>
<div class="compare-card-body">
 
Les paramètres se modifient de trois manières :
 
- **Interface web** : directement dans les champs numériques de la page **Main Command** pour chaque séquence.
- **Via protocole WRITE** : ControlWord bloc WRITE avec la formule `N × 100 + offset_parametro`
- **Via protocole READ** : ControlWord bloc READ avec la formule `10000 + N × 100 + offset_parametro`
 
</div>
</div>
</div>
 
---
 
### Exemple pratique : Move + Shake sur FlexiBowl® 800
 
Le scénario est le suivant : exécuter un **Move** de 360°, puis un **Shake**, puis une attente de 200 ms.
 
<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0 — Séquence de commandes TCP</div>
<div class="compare-card-body">
 
Les paramètres doivent être mis à l'échelle au moyen du **facteur de réduction** de la machine :
 
<pre>QX7                     → Allumer le rétroéclairage
RR114                   → Lire le facteur de réduction
reduction_factor = RX 1
 
RL1 (50 × reduction_factor), RW11   → Acceleration Move = 50 %
RL1 (50 × reduction_factor), RW12   → Deceleration Move = 50 %
RL1 (35 × reduction_factor), RW13   → Speed Move = 35 %
RL1 (360 × reduction_factor), RW14  → Angle Move = 360°
QX2                     → Exécuter Move
 
RL1 (50 × reduction_factor), RW15  → Acceleration Shake = 50 %
RL1 (50 × reduction_factor), RW16  → Deceleration Shake = 50 %
RL1 (50 × reduction_factor), RW110 → Speed Shake = 50 %
RL1 (30 × reduction_factor), RW18  → Angle CW Shake = -30°
RL1 (30 × reduction_factor), RW19  → Angle CCW Shake = -45°
RL1 2, RW17                           → Count Shake = 2
QX6                     → Exécuter Shake</pre>
 
L'attente de 200 ms est gérée par le système appelant (robot ou automate).
 
</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0 — Configuration de l'interface web</div>
<div class="compare-card-body">
 
Depuis la page **Main Command**, sélectionner **SEQUENCE 1** et définir :
 
| Paramètre | Valeur |
|---|---|
| Acceleration Move | 50 % |
| Deceleration Move | 50 % |
| Speed Move | 35 % |
| Angle Move | 360° |
| Acceleration Shake | 50 % |
| Deceleration Shake | 50 % |
| Speed Shake | 50 % |
| Ccw Angle Shake | −45° |
| Cw Angle Shake | −30° |
| Count Shake | 2 |
 
Ajouter à la liste : `FLB_MOVE` → `FLB_SHAKE`. Vérifier Backlight depuis la page **Option**. L'attente de 200 ms se gère en ajoutant `FLB_WAIT` à la liste ou côté système appelant.
 
Pour exécuter la séquence via TCP :
 
<pre>10[0]%    → Exécuter la Séquence 1</pre>
 
Le système répond par `10[0]` en confirmation.
 
</div>
</div>
</div>
 
---
 
## 6. Comment lire les alarmes
 
<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0</div>
<div class="compare-card-body">
 
Les alarmes se consultent depuis **Monitor → Alarm Status** du programme **FlexiBowl® Parameters**. L'écran affiche les états du driver au moyen d'indicateurs LED (vert = OK, rouge = erreur). L'écran **Driver Status** affiche en temps réel toutes les variables opérationnelles.
 
Réinitialisation de l'alarme via protocole :
 
<pre>Chr(0)Chr(7)QX12Chr(13)    → Réinitialiser l'alarme et réactiver le moteur</pre>
 
</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0</div>
<div class="compare-card-body">
 
Les alarmes se consultent depuis la page **Monitor** (onglets : **I/O Status**, **Driver Status**, **Alarm Status**).
 
Via protocole, le signal d'alarme est exposé par **In_Error** (BOOL) et le code actif par **ErrorCode** (UDINT) :
 
<pre>InError%         → InError[1]% en cas d'erreur, InError[0]% si OK
ErrorCode%       → ErrorCode[N]% avec le code de l'erreur active</pre>
 
Réinitialisation de l'alarme :
- Via protocole TCP : `Reset%`
- Via variable numérique : front montant sur le signal d'entrée **Reset** (BOOL)
 
</div>
</div>
</div>
 
:::{warning}
Avant d'effectuer la réinitialisation, identifier et résoudre la cause de l'erreur. Le système n'exécutera pas de nouvelles commandes de mouvement tant qu'une erreur est active.
:::
 
:::{note}
Pour la liste complète des codes d'erreur, se reporter à la section [Codes d'erreur](sec-err)
:::
 
---
 
## 7. Mode tracking (FlexiTrack)
 
<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0</div>
<div class="compare-card-body">
 
Le mode **FlexiTrack** est une option achetable séparément qui permet de maintenir le FlexiBowl® en **rotation continue** (jog) en synchronisant le signal de l'encodeur avec le robot de pick.
 
**Matériel requis :**
 
- Raccordement à l'**encodeur interne** via le connecteur du panneau de commande (signal en quadrature TTL, 4000 impulsions/tour sur le moteur ; pour les FlexiBowl® 500/650/800 avec réduction 1:3 → 12000 impulsions/tour sur le disque).
- En alternative, **encodeur externe** (incrémental, TTL RS422, ≥ 12000 ppr) sur l'axe solidaire de la poulie menée.
 
**Principales commandes FlexiTrack (via TCP/UDP) :**
 
| Commande | Description |
|---|---|
| `JA<valore>` | Accélération/décélération en tr/s² |
| `JL<valore>` | Décélération (si différente de JA, envoyer après JA) |
| `JS<valore>` | Vitesse de rotation en tr/s |
| `CC<valore>` | Courant envoyé au moteur |
| `DI1` | Sens horaire |
| `DI-1` | Sens antihoraire |
| `CJ` | Démarrer le jog (rotation continue) |
| `SJ` | Arrêter le jog (avec rampe JL) |
| `IL2` / `IH2` | Activer / désactiver Flip |
| `IL3` / `IH3` | Activer / désactiver Blow |
 
**Paramètres recommandés :**
 
<pre>JA0.2    → accélération 0.2 tr/s²
JL0.2    → décélération 0.2 tr/s²
JS0.2    → vitesse 0.2 tr/s
CC1.3    → courant moteur
DI1      → rotation horaire</pre>
 
Flip et Blow doivent être mis en œuvre au moyen d'un **programme en arrière-plan** avec une boucle itérative qui commute l'état des électrovannes.
 
</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0</div>
<div class="compare-card-body">
 
Le mode jog est **intégré nativement** dans la page **Jog Motor** — sans options matérielles supplémentaires.
 
**Paramètres de mouvement Jog :**
 
| Paramètre | Unité | Description |
|---|---|---|
| Acceleration | % | Rampe d'accélération au démarrage |
| Deceleration | % | Rampe de décélération à l'arrêt |
| Speed | % | Vitesse — positive = sens horaire ; négative = sens antihoraire |
 
**Fonctions accessoires pendant le Jog :**
 
- **Flip Enable** : flip automatique cyclique avec Flip Duration, Flip Pression, Flip Pause.
- **Blow Enable** : soufflage automatique cyclique avec Blow Duration, Blow Pression, Blow Pause, Blow Type (BLOWc, BLOWe, BLOWc+BLOWe).
- **Backlight 1 / 2** : commutateur du rétroéclairage, indépendant de l'état du jog.
 
**Démarrage et arrêt :**
 
- **START JOG** : démarre la rotation continue.
- **STOP JOG** : arrête avec une rampe de décélération.
 
Commande via protocole :
 
<pre>40[0]%    → Start Jog Seq (via TCP)
41[0]%    → Stop Jog Seq (via TCP)</pre>
 
</div>
</div>
</div>
 
:::{important}
Avant de démarrer le jog, vérifier que le moteur est activé (**ENABLE MOTOR** actif) et que l'état du système est **READY**.
:::
 
:::{important}
Avec FlexiTrack **(FlexiBowl® 2.0)**, le contrôle du mouvement est possible **uniquement via le protocole Ethernet** (TCP/UDP). Le protocole Digital I/O n'est pas pris en charge.
:::