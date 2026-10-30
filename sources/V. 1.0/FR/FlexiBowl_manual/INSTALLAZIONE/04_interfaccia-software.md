(int_software)=
# **Interface logicielle**

<script src="https://unpkg.com/@phosphor-icons/web"></script>

<div class="isw-page">
<style>
  /* ── Reset & base ── */
  .isw-page { font-family: inherit; max-width: 860px; margin: 0 auto; padding: 0 0 3rem; }

 /* ── NAV CARDS ── */
  .isw-nav {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    gap: 0.75rem;
    margin: 1.5rem 0 2.5rem;
  }
  .isw-nav-card {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 0.45rem;
    padding: 0.9rem 1rem;
    border: 1.5px solid #d0e4f0;
    border-radius: 10px;
    background: #fff;
    text-decoration: none;
    color: inherit;
    transition: border-color 0.18s, background 0.18s, transform 0.18s;
  }
  .isw-nav-card:hover {
    border-color: #2980b9;
    background: #f0f7ff;
    transform: translateY(-2px);
    text-decoration: none;
  }
  .isw-nav-card i {
    font-size: 1.4rem;
    color: #2980b9;
  }
  .isw-nav-card-title {
    font-weight: 700;
    font-size: 0.82rem;
    color: #1a3a52;
    line-height: 1.3;
  }
  .isw-nav-card-sub {
    font-size: 0.72rem;
    color: #7a9ab0;
  }

  /* ── FLOW DIAGRAM — orizzontale ── */
  .isw-flow {
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 0;
    margin: 1.5rem 0 2rem;
    overflow-x: auto;
    padding-bottom: 0.5rem;
    flex-wrap: nowrap;
  }
  .isw-flow-step {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.35rem;
    min-width: 110px;
    flex: 1;
  }
  .isw-flow-bubble {
    width: 48px;
    height: 48px;
    border-radius: 50%;
    background: #e3f1fb;
    border: 2px solid #2980b9;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #2980b9;
    font-size: 1.2rem;
    flex-shrink: 0;
  }
  .isw-flow-label {
    font-size: 0.72rem;
    font-weight: 600;
    color: #1a3a52;
    text-align: center;
    line-height: 1.3;
  }
  .isw-flow-sub {
    font-size: 0.65rem;
    color: #7a9ab0;
    text-align: center;
  }
  .isw-flow-arrow {
    color: #bcd6ec;
    font-size: 1.6rem;
    flex-shrink: 0;
    margin: 0 2px;
    padding-bottom: 1.8rem;
    display: flex;
    align-items: flex-start;
    padding-top: 0.2rem;
  }

  /* ── FORMULA BOX ── */
  .isw-formula {
    background: #f0f7ff;
    border-left: 4px solid #2980b9;
    border-radius: 0 8px 8px 0;
    padding: 1rem 1.25rem;
    margin: 1rem 0 1.5rem;
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    align-items: center;
  }
  .isw-formula-main {
    font-family: monospace;
    font-size: 1.05rem;
    font-weight: 700;
    color: #1a3a52;
    white-space: nowrap;
  }
  .isw-formula-example {
    font-size: 0.8rem;
    color: #556b7d;
    border-left: 1px solid #bcd6ec;
    padding-left: 1rem;
  }
  .isw-formula-example strong { color: #2980b9; }

  /* ── SECTION BADGES ── */
  .isw-section-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    border-radius: 5px;
    padding: 3px 10px;
    margin-bottom: 0.6rem;
  }
  .isw-badge-exe  { background: #dbeafe; color: #1d4ed8; }
  .isw-badge-write{ background: #fef3c7; color: #92400e; }
  .isw-badge-read { background: #d1fae5; color: #065f46; }
  .isw-badge-io   { background: #ede9fe; color: #5b21b6; }
  .isw-badge-tcp  { background: #fce7f3; color: #9d174d; }
  .isw-badge-err  { background: #fee2e2; color: #991b1b; }
  .isw-badge-field { background: #dcfce7; color: #166534; }
  .isw-badge-hop  { background: #ffe4e6; color: #9f1239; }

  /* ── TABLES ── */
  .isw-table-wrap {
    overflow-x: auto;
    border-radius: 8px;
    border: 1px solid #e2eef6;
    margin: 0.75rem 0 1.5rem;
  }
  .isw-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.82rem;
  }
  .isw-table thead tr {
    background: #1a3a52;
    color: #fff;
    position: sticky;
    top: 0;
    z-index: 1;
  }
  .isw-table thead th {
    padding: 0.6rem 0.9rem;
    text-align: left;
    font-weight: 600;
    white-space: nowrap;
  }
  .isw-table tbody tr:nth-child(even) { background: #f7fbfe; }
  .isw-table tbody tr:hover { background: #e8f4fc; }
  .isw-table tbody td {
    padding: 0.5rem 0.9rem;
    border-bottom: 1px solid #e9f2f9;
    color: #334e5e;
    vertical-align: top;
  }
  .isw-table tbody td:first-child {
    font-weight: 600;
    color: #1a3a52;
    white-space: nowrap;
  }
  .isw-table code {
    background: #e3f1fb;
    color: #1d4ed8;
    border-radius: 3px;
    padding: 1px 5px;
    font-size: 0.8rem;
  }
  .isw-table tbody tr.isw-hidden { display: none; }

  /* ── TABELLA ERRORI DRIVER — stile Sphinx standard ── */
  .isw-err-wrap {
    overflow-x: auto;
    margin: 0.75rem 0 1.5rem;
  }
  .isw-err-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.85rem;
  }
  .isw-err-table thead tr {
    background: #f0f4f8;
  }
  .isw-err-table thead th {
    padding: 0.55rem 0.8rem;
    text-align: left;
    font-weight: 700;
    color: #1a3a52;
    border: 1px solid #c8d8e4;
  }
  .isw-err-table tbody tr:nth-child(even) { background: #f7fbfe; }
  .isw-err-table tbody tr:hover { background: #cfe2ff; }
  .isw-err-table tbody td {
    padding: 0.45rem 0.8rem;
    border: 1px solid #c8d8e4;
    color: #334e5e;
    vertical-align: top;
  }
  .isw-err-table tbody td:first-child {
    font-weight: 600;
    color: #1a3a52;
    white-space: nowrap;
  }
  .isw-err-table code {
    font-family: monospace;
    font-size: 0.82rem;
    color: #1a3a52;
    background: none;
    padding: 0;
  }
  .isw-err-table tbody tr.isw-hidden { display: none; }

  /* ── SEARCH BOX ── */
  .isw-search-wrap {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-bottom: 0.75rem;
  }
  .isw-search {
    flex: 1;
    max-width: 340px;
    padding: 0.45rem 0.75rem 0.45rem 2.2rem;
    border: 1.5px solid #d0e4f0;
    border-radius: 7px;
    font-size: 0.85rem;
    color: #1a3a52;
    outline: none;
    background: #fff url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='14' height='14' viewBox='0 0 256 256'%3E%3Cpath fill='%237a9ab0' d='M229.66 218.34l-50.07-50.07a88.11 88.11 0 1 0-11.31 11.31l50.06 50.07a8 8 0 0 0 11.32-11.31ZM40 112a72 72 0 1 1 72 72 72.08 72.08 0 0 1-72-72Z'/%3E%3C/svg%3E") no-repeat 0.6rem center;
    transition: border-color 0.18s;
  }
  .isw-search:focus { border-color: #2980b9; }
  .isw-search-count {
    font-size: 0.75rem;
    color: #7a9ab0;
  }

  /* ── RETURN DATA — tabella leggibile ── */
  .isw-return-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.88rem;
    margin: 0.75rem 0 1.5rem;
  }
  .isw-return-table thead tr {
    background: #e3f1fb;
  }
  .isw-return-table thead th {
    padding: 0.55rem 1rem;
    text-align: left;
    font-weight: 700;
    color: #1a3a52;
    border-bottom: 2px solid #2980b9;
  }
  .isw-return-table tbody tr:nth-child(even) { background: #f7fbfe; }
  .isw-return-table tbody tr:hover { background: #cfe2ff; }
  .isw-return-table tbody td {
    padding: 0.55rem 1rem;
    border-bottom: 1px solid #d0e4f0;
    color: #334e5e;
    vertical-align: middle;
  }
  .isw-return-table tbody td:first-child {
    font-family: monospace;
    font-size: 1rem;
    font-weight: 700;
    color: #2980b9;
    white-space: nowrap;
    width: 90px;
  }

  /* ── ESEMPI PRATICI (pacchetto dati) ── */
  .isw-example {
    border: 1px solid #d0e4f0;
    border-radius: 10px;
    margin: 1rem 0 1.75rem;
    overflow: hidden;
  }
  .isw-example-title {
    background: #f0f7ff;
    padding: 0.6rem 1rem;
    font-weight: 700;
    font-size: 0.88rem;
    color: #1a3a52;
    border-bottom: 1px solid #d0e4f0;
  }
  .isw-example-body {
    padding: 1rem;
    display: grid;
    grid-template-columns: 1fr;
    gap: 1.25rem;
  }
  .isw-example-body > div + div {
    border-top: 1px solid #e2eef6;
    padding-top: 1rem;
  }
  .isw-example-col-title {
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    color: #2980b9;
    margin-bottom: 0.5rem;
    text-transform: uppercase;
  }
  .isw-example-body table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.78rem;
    margin-bottom: 0.5rem;
  }
  .isw-example-body table th {
    background: #f0f4f8;
    padding: 0.35rem 0.5rem;
    text-align: center;
    font-weight: 700;
    color: #1a3a52;
    border: 1px solid #d0e4f0;
    white-space: nowrap;
  }
  .isw-example-body table td {
    padding: 0.35rem 0.5rem;
    text-align: center;
    border: 1px solid #d0e4f0;
    color: #334e5e;
  }
  .isw-example-tcp {
    font-family: monospace;
    font-size: 0.85rem;
    background: #f7fbfe;
    border-radius: 6px;
    padding: 0.6rem 0.8rem;
    margin: 0.35rem 0;
  }
  .isw-example-tcp .ok { color: #166534; font-weight: 700; }
  .isw-example-tcp .ko { color: #991b1b; font-weight: 700; }
</style>

## Introduction

La nouvelle interface FlexiBowl® est entièrement web. Pour y accéder, il suffit de saisir l'adresse IP par défaut du FlexiBowl® `192.168.1.10` dans la barre d'adresse de votre navigateur.

:::{video} ../../../../_shared/media/videos/IP_Home.mp4
:width: 90%
:::


## Communication 

Le système de communication repose sur des **variables d'entrée/sortie** et des **Control Words numériques** : le système externe envoie un nombre (le ControlWord) qui identifie l'action à exécuter et le FlexiBowl® répond par des signaux d'état et des données de retour.

Protocoles pris en charge :
- **TCP Server**
- **EtherNet/IP**
- **Profinet**
- **Modbus**

:::{important}
Les variables, les ControlWords et toutes les commandes **EXE**, **WRITE** et **READ** décrites dans cette page sont **identiques pour les quatre protocoles de communication**. Ce qui change d'un protocole à l'autre, c'est **uniquement la manière dont ces données sont échangées physiquement** :

- **EtherNet/IP, Profinet et Modbus** se comportent de la même manière entre eux : ils échangent un **paquet d'E/S cyclique** à champs fixes (voir [Transport Fieldbus](#sec-fieldbus)).
- **TCP Server** utilise en revanche des **messages texte** sur socket (voir [Syntaxe TCP](#sec-tcp)).

Pour cette raison, chaque exemple pratique de cette page est présenté dans les deux modes.
:::

---

### Naviguer dans la page

<div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:1rem; margin:1.5rem 0 2.5rem;">

  <a href="#sec-io" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit; transition:border-color 0.18s, background 0.18s;">
    <i class="ph ph-arrows-left-right" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Variables E/S</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Entrée et sortie</span>
  </a>

  <a href="#sec-fieldbus" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-swap" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Transport Fieldbus</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">EtherNet/IP, Profinet, Modbus</span>
  </a>

  <a href="#sec-tcp" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-network" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Syntaxe TCP</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Messages socket</span>
  </a>

  <a href="#sec-exe" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-play-circle" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Commandes EXE</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Démarrage des séquences et jog</span>
  </a>

  <a href="#sec-write" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-pencil-simple" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Commandes WRITE</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Écriture des paramètres</span>
  </a>

  <a href="#sec-read" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-eye" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Commandes READ</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Lecture des paramètres</span>
  </a>

  <a href="#sec-hopper" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-funnel" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Commandes Hopper</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Bulk Feeder</span>
  </a>

  <a href="#sec-empty" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-arrow-counter-clockwise" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Quick Emptying</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Option de vidage</span>
  </a>

  <a href="#sec-err" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-warning-circle" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Codes d'erreur</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Diagnostic</span>
  </a>

</div>

---

### Comment fonctionne une commande

Cette logique est **identique pour tous les protocoles** : seule change la manière dont les 4 étapes sont transmises physiquement (paquet d'E/S pour les protocoles fieldbus, message texte pour TCP — voir les sections suivantes).

<table style="width:100%; border-collapse:collapse; margin: 1.5rem 0 2rem;">
  <tr>
    <td style="text-align:center; padding:0 8px; width:22%;">
      <div style="width:52px; height:52px; border-radius:50%; background:#e3f1fb; border:2px solid #2980b9; display:inline-flex; align-items:center; justify-content:center; color:#2980b9; font-size:1.4rem; font-weight:700; margin-bottom:0.5rem;">
        1
      </div><br>
      <span style="font-size:0.92rem; font-weight:700; color:#1a3a52; line-height:1.4;">Définir<br>ControlWord</span><br>
      <span style="font-size:0.8rem; color:#7a9ab0;">numéro de la commande</span>
    </td>
    <td style="text-align:center; color:#bcd6ec; font-size:1.6rem; width:4%; vertical-align:middle; padding-bottom:1.8rem;">
      <i class="ph ph-caret-right"></i>
    </td>
    <td style="text-align:center; padding:0 8px; width:22%;">
      <div style="width:52px; height:52px; border-radius:50%; background:#e3f1fb; border:2px solid #2980b9; display:inline-flex; align-items:center; justify-content:center; color:#2980b9; font-size:1.4rem; font-weight:700; margin-bottom:0.5rem;">
        2
      </div><br>
      <span style="font-size:0.92rem; font-weight:700; color:#1a3a52; line-height:1.4;">Définir<br>Data_1</span><br>
      <span style="font-size:0.8rem; color:#7a9ab0;">si nécessaire</span>
    </td>
    <td style="text-align:center; color:#bcd6ec; font-size:1.6rem; width:4%; vertical-align:middle; padding-bottom:1.8rem;">
      <i class="ph ph-caret-right"></i>
    </td>
    <td style="text-align:center; padding:0 8px; width:22%;">
      <div style="width:52px; height:52px; border-radius:50%; background:#e3f1fb; border:2px solid #2980b9; display:inline-flex; align-items:center; justify-content:center; color:#2980b9; font-size:1.4rem; font-weight:700; margin-bottom:0.5rem;">
        3
      </div><br>
      <span style="font-size:0.92rem; font-weight:700; color:#1a3a52; line-height:1.4;">Front montant<br>ExecuteCW</span><br>
      <span style="font-size:0.8rem; color:#7a9ab0;">trigger 0 → 1</span>
    </td>
    <td style="text-align:center; color:#bcd6ec; font-size:1.6rem; width:4%; vertical-align:middle; padding-bottom:1.8rem;">
      <i class="ph ph-caret-right"></i>
    </td>
    <td style="text-align:center; padding:0 8px; width:22%;">
      <div style="width:52px; height:52px; border-radius:50%; background:#e3f1fb; border:2px solid #2980b9; display:inline-flex; align-items:center; justify-content:center; color:#2980b9; font-size:1.4rem; font-weight:700; margin-bottom:0.5rem;">
        4
      </div><br>
      <span style="font-size:0.92rem; font-weight:700; color:#1a3a52; line-height:1.4;">Attendre<br>Busy = 0</span><br>
      <span style="font-size:0.8rem; color:#7a9ab0;">et ReturnData_1 = CW</span>
    </td>
  </tr>
</table>


1. Le système externe définit le **ControlWord** avec le numéro de la commande souhaitée.
2. Si la commande nécessite un argument, il définit également **Data_1**.
3. Envoie un front montant sur **ExecuteControlWord**.
4. Attend que **Busy** repasse à `0` et que **ReturnData_1** renvoie la valeur du ControlWord (confirmation de la bonne exécution).

:::{warning}
Ne pas envoyer de nouvelle commande tant que **Busy** est à `1`. Le système ignorera la commande et **ReturnData_1** renverra la valeur `3` (système occupé).
:::

---

(sec-io)=
## Variables d'entrée et de sortie 

Ces variables sont **les mêmes pour tous les protocoles de communication** : seule change la manière dont elles sont échangées (voir [Transport Fieldbus](#sec-fieldbus) et [Syntaxe TCP](#sec-tcp)).

### INPUT — Signaux envoyés au FlexiBowl®

| Variable | Type | Description |
|---|---|---|
| **ControlWord** | UDINT | Nombre entier qui identifie la commande à exécuter. Chaque valeur correspond à une action spécifique (voir tableau des commandes). |
| **Data_1** | UDINT | Argument numérique associé au ControlWord, lorsqu'il est requis (par ex. la valeur de vitesse à écrire). La signification dépend de la commande sélectionnée. |
| **ExecuteControlWord** | BOOL | Signal de déclenchement : sur le **front montant** (de 0 à 1), le ControlWord est lu et la commande est exécutée. |
| **Hopper_1** | BOOL | Active directement le Hopper 1, indépendamment du ControlWord. |
| **Hopper_2** | BOOL | Active directement le Hopper 2. |
| **Hopper_3** | BOOL | Active directement le Hopper 3. |
| **Hopper_4** | BOOL | Active directement le Hopper 4. |
| **Reset** | BOOL | Sur le front montant, réinitialise les erreurs actives sur l'appareil. |

### OUTPUT — Signaux envoyés par le FlexiBowl®

| Variable | Type | Description |
|---|---|---|
| **Busy** | BOOL | Vaut `1` pendant que le FlexiBowl® exécute une commande. Tant qu'il est actif, ne pas envoyer de nouvelles commandes. |
| **Ready** | BOOL | Vaut `1` lorsque l'appareil est prêt à recevoir de nouvelles commandes. |
| **In_Error** | BOOL | Vaut `1` si des erreurs actives sont présentes sur l'appareil. Consulter **ErrorCode** pour identifier le type d'erreur. |
| **ReturnData_1** | UDINT | Confirmation de la commande reçue (écho). Les valeurs possibles sont : `0` = état initial (aucune commande), `1` = commande non interprétable, `2` = Data_1 erroné mais commande reconnue, `3` = système occupé (Busy), ou la valeur même du ControlWord = commande exécutée correctement. |
| **ReturnData_2** | UDINT | Contient les données demandées par les commandes de lecture (READ). |
| **ErrorCode** | UDINT | Code numérique de l'erreur active. Vaut `0` s'il n'y a pas d'erreurs. Voir la section [Codes d'erreur](#codici-di-errore) pour la signification de chaque code. |
| **InPowerOn** | BOOL | Vaut `1` si l'appareil est alimenté et opérationnel. |


### Valeurs de ReturnData_1

<div class="isw-ret">
<style>
.isw-ret table thead tr,
.isw-ret table thead tr th {
  background: #f0f4f8 !important;
  color: #1a3a52 !important;
  border-bottom: 2px solid #2980b9 !important;
}
</style>
<table style="width:100%; border-collapse:collapse; font-size:0.95rem; margin:0.75rem 0 1.5rem;">
  <thead>
    <tr>
      <th style="padding:0.6rem 0.9rem; text-align:left; font-weight:700; white-space:nowrap; width:100px;">Valeur</th>
      <th style="padding:0.6rem 0.9rem; text-align:left; font-weight:700;">Signification</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background:#fff;" onmouseover="this.style.background='#e8f4fc'" onmouseout="this.style.background='#fff'">
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; font-family:monospace; font-size:1.05rem; font-weight:700; color:#2980b9;">0</td>
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; color:#334e5e;">NULL — aucune commande en cours (état initial)</td>
    </tr>
    <tr style="background:#f7fbfe;" onmouseover="this.style.background='#e8f4fc'" onmouseout="this.style.background='#f7fbfe'">
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; font-family:monospace; font-size:1.05rem; font-weight:700; color:#2980b9;">1</td>
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; color:#334e5e;">Commande non interprétable (ControlWord inconnu)</td>
    </tr>
    <tr style="background:#fff;" onmouseover="this.style.background='#e8f4fc'" onmouseout="this.style.background='#fff'">
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; font-family:monospace; font-size:1.05rem; font-weight:700; color:#2980b9;">2</td>
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; color:#334e5e;">Data_1 hors plage, commande reconnue</td>
    </tr>
    <tr style="background:#f7fbfe;" onmouseover="this.style.background='#e8f4fc'" onmouseout="this.style.background='#f7fbfe'">
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; font-family:monospace; font-size:1.05rem; font-weight:700; color:#2980b9;">3</td>
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; color:#334e5e;">Système occupé (Busy) — réessayer</td>
    </tr>
    <tr style="background:#fff;" onmouseover="this.style.background='#e8f4fc'" onmouseout="this.style.background='#fff'">
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; font-family:monospace; font-size:1.05rem; font-weight:700; color:#2980b9;">= CW</td>
      <td style="padding:0.55rem 0.9rem; border-bottom:1px solid #e9f2f9; color:#334e5e;">Commande exécutée correctement</td>
    </tr>
  </tbody>
</table>
</div>

---

(sec-fieldbus)=
## EtherNet/IP, Profinet, Modbus - <span class="isw-section-badge isw-badge-field"><i class="ph ph-swap"></i> FIELDBUS</span>

Pour **EtherNet/IP**, **Profinet** et **Modbus**, les variables d'[entrée](#sec-io) et de [sortie](#sec-io) sont échangées sous forme de **paquet d'E/S cyclique** : il n'existe pas de messages texte, chaque variable occupe une position fixe dans le paquet de données. Pour toutes les informations détaillées sur ce protocole, se reporter à la [page suivante](fieldbus).

### Paquet de données — Input (vers le FlexiBowl®)

| ControlWord | Data_1 | ExecuteControlWord | Hopper_1 | Hopper_2 | Hopper_3 | Hopper_4 | Reset |
|---|---|---|---|---|---|---|---|
| *(numéro de commande)* | *(argument)* | *(bit de déclenchement 0→1)* | *(bit)* | *(bit)* | *(bit)* | *(bit)* | *(bit)* |

### Paquet de données — Output (depuis le FlexiBowl®)

| Busy | Ready | In_Error | In_PowerOn | ReturnData_1 | ReturnData_2 | ErrorCode |
|---|---|---|---|---|---|---|
| *(bit)* | *(bit)* | *(bit)* | *(bit)* | *(écho du ControlWord)* | *(donnée lue)* | *(code d'erreur)* |

:::{note}
La séquence d'écriture est toujours la même : définir **ControlWord** (et **Data_1** si nécessaire) avec **ExecuteControlWord = 0**, puis amener **ExecuteControlWord** à `1` pour générer le front montant qui démarre l'exécution.
:::

:::{card} ALLER À LA PAGE DÉDIÉE
:link: fieldbus
:link-type: ref
:class-card: isw-card-field
:class-body: isw-card-body

Documentation complète du protocole Fieldbus (EtherNet/IP, Profinet, Modbus)
:::

---

(sec-tcp)=
## Syntaxe des messages <span class="isw-section-badge isw-badge-tcp"><i class="ph ph-network"></i> TCP SERVER</span>

Lorsque la communication **TCP Server** est utilisée, les commandes ne sont pas envoyées sous forme de variables binaires mais sous forme de **chaînes de texte** via une connexion socket sur le port configuré (par défaut : 8123). Pour toutes les informations détaillées sur ce protocole, se reporter à la [page suivante](tcp).

### Structure du message

Chaque message a la forme :

```
NomeVariabile[Valore]%
```

Le caractère `%` est le **terminateur de message** et doit toujours être présent à la fin. Le champ `[Valore]` contient la donnée numérique associée (ControlWord, état, etc.).

:::{card} ALLER À LA PAGE DÉDIÉE
:link: tcp
:link-type: ref
:class-card: isw-card-tcp
:class-body: isw-card-body

Syntaxe complète des messages TCP Server, des commandes et des terminateurs
:::
---

## Protocole de commandes

Le protocole de commandes définit toutes les actions disponibles via le ControlWord. Les ControlWords sont **les mêmes pour tous les protocoles** ; seul le transport change (voir [Transport Fieldbus](#sec-fieldbus) et [Syntaxe TCP](#sec-tcp)). Les commandes sont regroupées en catégories :

<div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:1rem; margin:1.5rem 0 2.5rem;">

  <a href="#sec-exe" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-play-circle" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Commandes EXE</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Commandes d'exécution (démarrage des séquences, jog, réinitialisation)</span>
  </a>

  <a href="#sec-write" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-pencil-simple" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Commandes WRITE</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Écriture de paramètres (vitesse, angles, temps, etc.)</span>
  </a>

  <a href="#sec-read" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-eye" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">Commandes READ</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Lecture des paramètres actuellement configurés</span>
  </a>

</div>

(sec-exe)=
### Commandes <span class="isw-section-badge isw-badge-exe"><i class="ph ph-play-circle"></i> EXE</span>

Les commandes EXE démarrent une action immédiate sur le FlexiBowl®. Pendant l'exécution, **Busy** reste à `1`.

| Commande | ControlWord | Busy pendant l'exécution | ReturnData_1 | Explication | 
|---|---|---|---|---|
| Exe Seq 1 | 10 | OUI | 10 | Exécuter la Séquence 1 |
| Exe Seq 2 | 11 | OUI | 11 | Exécuter la Séquence 2 |
| Exe Seq 3 | 12 | OUI | 12 | Exécuter la Séquence 3 |
| Exe Seq 4 | 13 | OUI | 13 | Exécuter la Séquence 4 |
| Exe Seq 5 | 14 | OUI | 14 | Exécuter la Séquence 5 |
| Exe Seq 6 | 15 | OUI | 15 | Exécuter la Séquence 6 |
| Exe Seq 7 | 16 | OUI | 16 | Exécuter la Séquence 7 |
| Exe Seq 8 | 17 | OUI | 17 | Exécuter la Séquence 8 |
| Exe Seq 9 | 18 | OUI | 18 | Exécuter la Séquence 9 |
| Exe Seq 10 | 19 | OUI | 19 | Exécuter la Séquence 10 |
| Exe Seq 11 | 20 | OUI | 20 | Exécuter la Séquence 11 |
| Exe Seq 12 | 21 | OUI | 21 | Exécuter la Séquence 12 |
| Exe Seq 13 | 22 | OUI | 22 | Exécuter la Séquence 13 |
| Exe Seq 14 | 23 | OUI | 23 | Exécuter la Séquence 14 |
| Exe Seq 15 | 24 | OUI | 24 | Exécuter la Séquence 15 |
| Exe Seq 16 | 25 | OUI | 25 | Exécuter la Séquence 16 |
| Exe Seq 17 | 26 | OUI | 26 | Exécuter la Séquence 17 |
| Exe Seq 18 | 27 | OUI | 27 | Exécuter la Séquence 18 |
| Exe Seq 19 | 28 | OUI | 28 | Exécuter la Séquence 19 |
| Exe Seq 20 | 29 | OUI | 29 | Exécuter la Séquence 20 |
| Start Jog Seq | 40 | OUI | 40 | Démarrer le Jog |
| Stop Jog Seq | 41 | OUI | 41 | Arrêter le Jog |
| Reset Return Data | 50 | NON | 0 | Remet à zéro la valeur de ReturnData_1 et ReturnData_2, en les ramenant à l'état initial `0` |

:::{note}
La commande **Reset Return Data** (ControlWord 50) remet à zéro la valeur de ReturnData_1 et ReturnData_2, en les ramenant à l'état initial `0`. Elle est utile pour vérifier qu'une nouvelle commande est effectivement reçue et traitée.
:::

#### Exemple pratique 

Pour consulter un exemple pratique de commande EXE en fieldbus, se reporter à la section [Exemple pratique EXE](fieldbus_exe).
Pour consulter un exemple pratique de commande EXE en TCP, se reporter à la section [Exemple pratique EXE TCP](TCP_EXE).

(sec-write)=
### Commandes <span class="isw-section-badge isw-badge-write"><i class="ph ph-pencil-simple"></i> WRITE</span>

Les commandes WRITE permettent de modifier les paramètres opérationnels du FlexiBowl® (vitesse, angles, temps, etc.) directement depuis le système externe, sans avoir à accéder à l'interface graphique.

#### Logique d'adressage des séquences

Chaque séquence (de 1 à 20) possède son propre bloc de paramètres. Le ControlWord se calcule avec la formule :

> **ControlWord = N × 100 + parameter_offset**

où `N` est le numéro de la séquence (1–20) et `offset_parametro` identifie le paramètre spécifique.

#### Paramètres inscriptibles pour chaque séquence

| Paramètre | Offset | Range Data_1 | Notes |
|---|---|---|---|
| AccelerationMove | 00 | 1–100 | Rampe d'accélération du mouvement rotatif (%) |
| DecelerationMove | 01 | 1–100 | Rampe de décélération du mouvement rotatif (%) |
| SpeedMove | 02 | 1–100 | Vitesse du mouvement rotatif (%) |
| AngleMove | 03 | 0–720 | Angle de rotation en degrés. Valeurs 1000–1720 = angle négatif (sens opposé) |
| AccelerationShake | 04 | 1–100 | Rampe d'accélération du shake (%) |
| DecelerationShake | 05 | 1–100 | Rampe de décélération du shake (%) |
| CountShake | 06 | 2–20 | Nombre d'oscillations par cycle de shake |
| CwAngleShake | 07 | 0–360 | Angle de rotation horaire pendant le shake. Valeurs 1000–1360 = angle négatif |
| CcwAngleShake | 08 | 0–360 | Angle de rotation antihoraire pendant le shake. Valeurs 1000–1360 = angle négatif |
| SpeedShake | 09 | 1–100 | Vitesse du shake (%) |
| FlipCount | 10 | 0–20 | Nombre de flips par cycle |
| FlipDelay | 11 | 0–500 | Pause entre un flip et le suivant (ms) |
| BlowDelay | 12 | 0–500 | Pause entre une impulsion de blow et la suivante (ms) |
| ProportionalValve_Flip | 13 | 0–600 | Pression de l'électrovanne proportionnelle Flip (valeur /100 = Bar) |
| ProportionalValve_Blow | 14 | 0–600 | Pression de l'électrovanne proportionnelle Blow (valeur /100 = Bar) |
| Delete all sequence | 30 | — | Supprime toutes les commandes de la liste de la séquence |
| Emptying Sequence | 40 | 0–1 | 0 = mode normal, 1 = mode Quick Emptying |
| Seq Add Cmd | 50 | COMMANDE FLB | Ajoute une commande à la liste de la séquence |

#### Exemples de ControlWord WRITE

| Séquence | Paramètre | Offset associé au paramètre | Formule (N x 100 + Offset) | ControlWord |
|---|---|---|---|---|
| SEQ 1 (N=1) | AccelerationMove | 00 | 1 x 100 + 00 | 100 |
| SEQ 1 (N=1) | SpeedMove | 02 | 1 x 100 + 02 | 102 |
| SEQ 1 (N=1) | FlipCount | 10 | 1 x 100 + 10 | 110 |
| SEQ 1 (N=1) | Emptying Sequence | 40 | 1 x 100 + 40 | 140 |
| SEQ 1 (N=1) | Seq Add Cmd | 50 | 1 x 100 + 50 | 150 |
| SEQ 2 (N=2) | AccelerationMove | 00 | 2 x 100 + 00 | 200 |
| SEQ 2 (N=2) | SpeedMove | 02 | 2 x 100 + 02 | 202 |
| SEQ 5 (N=5) | AngleMove | 03 | 5 x 100 + 03 | 503 |
| SEQ 10 (N=10) | FlipDelay | 11 | 10 x 100 + 11 |1011 |
| SEQ 20 (N=20) | SpeedMove | 02 | 20 x 100 + 02 | 2002 |

:::{tip}
La formule est simple :
- Pour écrire la vitesse (offset 02) de la séquence 7, le ControlWord est `7 × 100 + 2 = 702`.
- Pour écrire le FlipCount (offset 10) de la séquence 15, le ControlWord est `15 × 100 + 10 = 1510`.
:::

#### Exemple pratique 

Pour consulter un exemple pratique de commande WRITE en fieldbus, se reporter à la section [Exemple pratique WRITE](fieldbus_write).
Pour consulter un exemple pratique de commande WRITE en TCP, se reporter à la section [Exemple pratique WRITE TCP](TCP_write).

#### Paramètres WRITE JOG

Les paramètres du Jog (fonctionnement manuel continu) sont configurables séparément via ControlWord dans le bloc 20000.

| Paramètre | ControlWord | Range Data_1 | Notes |
|---|---|---|---|
| AccelerationJog | 20001 | 0–100 | Rampe d'accélération du jog (%) |
| DecelerationJog | 20002 | 0–100 | Rampe de décélération du jog (%) |
| SpeedJog | 20003 | 0–100 | Vitesse du jog (%). Valeurs 1000–1100 = vitesse négative (rotation inverse) |
| FlipJog_Enable | 20004 | 0–1 | 0 = flip désactivé, 1 = flip activé pendant le jog |
| FlipJog_Duration | 20005 | 0–1000 | Durée de l'impulsion de flip (ms) |
| FlipJog_Pressure | 20006 | 0–600 | Pression de flip (/100 = Bar) |
| FlipJog_Pause | 20007 | 0–1000 | Pause entre flips consécutifs (ms) |
| BlowJog_Enable | 20008 | 0–1 | 0 = blow désactivé, 1 = blow activé pendant le jog |
| BlowJog_Duration | 20009 | 0–1000 | Durée de l'impulsion de blow (ms) |
| BlowJog_Pressure | 20010 | 0–600 | Pression de blow (/100 = Bar) |
| BlowJog_Pause | 20011 | 0–1000 | Pause entre blows consécutifs (ms) |
| BlowJog_Type | 20012 | 0–2 | Type de blow : 0 = BLOWc, 1 = BLOWe, 2 = BLOWc+BLOWe |
| Backlight_1 | 20013 | 0–1 | 0 = éteint, 1 = allumé |
| Backlight_2 | 20014 | 0–1 | 0 = éteint, 1 = allumé |

---

(sec-read)=
### Commandes <span class="isw-section-badge isw-badge-read"><i class="ph ph-eye"></i> READ</span>

Les commandes READ permettent de lire les paramètres actuellement configurés dans le FlexiBowl®. La valeur lue est renvoyée dans **ReturnData_2**.

#### Logique d'adressage READ des séquences

Le ControlWord pour la lecture se calcule avec la formule :

> **ControlWord = 10000 + N × 100 + parameter_offset**

où `N` est le numéro de la séquence (1–20) et `offset_parametro` est le même que celui utilisé dans les commandes WRITE.

Les paramètres lisibles sont les mêmes que ceux du bloc WRITE, avec en plus les 10 emplacements de la liste de commandes :

| Paramètre supplémentaire | Offset | Description |
|---|---|---|
| Seq Slot 1 Cmd | 50 | Commande en position 1 dans la liste de la séquence |
| Seq Slot 2 Cmd | 51 | Commande en position 2 |
| … | … | … |
| Seq Slot 10 Cmd | 59 | Commande en position 10 |

#### Exemples de ControlWord READ

| Séquence | Paramètre | ControlWord |
|---|---|---|
| SEQ 1 | AccelerationMove | 10100 |
| SEQ 1 | SpeedMove | 10102 |
| SEQ 1 | FlipCount | 10110 |
| SEQ 1 | Emptying Sequence | 10140 |
| SEQ 1 | Slot 1 Cmd | 10150 |
| SEQ 1 | Slot 10 Cmd | 10159 |
| SEQ 5 | AngleMove | 10503 |
| SEQ 10 | SpeedMove | 11002 |
| SEQ 20 | Emptying Sequence | 12040 |

:::{tip}
Formule rapide :
 Pour lire la vitesse (offset 02) de la séquence 12, le ControlWord est `10000 + 12 × 100 + 2 = 11202`.
:::

#### Exemple pratique 

Pour consulter un exemple pratique de commande READ en fieldbus, se reporter à la section [Exemple pratique READ](fieldbus_read).
Pour consulter un exemple pratique de commande READ en TCP, se reporter à la section [Exemple pratique READ TCP](TCP_read).

#### Paramètres READ JOG

Les mêmes paramètres JOG inscriptibles (bloc 20000) sont lisibles dans le bloc 20100 :

| Paramètre | ControlWord READ | Plage ReturnData_2 |
|---|---|---|
| AccelerationJog | 20101 | 0–100 |
| DecelerationJog | 20102 | 0–100 |
| SpeedJog | 20103 | 0–100 (1000–1100 = négatif) |
| FlipJog_Enable | 20104 | 0–1 |
| FlipJog_Duration | 20105 | 0–1000 |
| FlipJog_Pressure | 20106 | 0–600 (/100) |
| FlipJog_Pause | 20107 | 0–1000 |
| BlowJog_Enable | 20108 | 0–1 |
| BlowJog_Duration | 20109 | 0–1000 |
| BlowJog_Pressure | 20110 | 0–600 (/100) |
| BlowJog_Pause | 20111 | 0–1000 |
| BlowJog_Type | 20112 | 0–2 |
| Backlight_1 | 20113 | 0–1 |
| Backlight_2 | 20114 | 0–1 |

---

(sec-hopper)=
## Commandes <span class="isw-section-badge isw-badge-hop"><i class="ph ph-funnel"></i> HOPPER</span>

Les commandes Hopper pilotent les Bulk Feeders connectés au système (jusqu'à 4). Elles suivent la même logique ControlWord/WRITE/READ décrite ci-dessus, valable pour tous les protocoles, ainsi qu'une syntaxe TCP dédiée pour le démarrage rapide.

### Commandes WRITE Hopper

| Paramètre | ControlWord | Range Data_1 | Description |
|---|---|---|---|
| Hopper_1_Id | 30001 | 1–100 | ID unique du hopper 1 sur le réseau |
| Hopper_1_Amplitude | 30002 | 50–220 | Amplitude de vibration du hopper 1 |
| Hopper_1_Frequency | 30003 | 40–70 | Fréquence de vibration du hopper 1 |
| Hopper_1_Activation_Time | 30004 | 400–60000 | Temps d'activation du hopper 1 (ms) |
| Hopper_2_Id | 30005 | 1–100 | ID unique du hopper 2 |
| Hopper_2_Amplitude | 30006 | 50–220 | Amplitude de vibration du hopper 2 |
| Hopper_2_Frequency | 30007 | 40–70 | Fréquence de vibration du hopper 2 |
| Hopper_2_Activation_Time | 30008 | 400–60000 | Temps d'activation du hopper 2 (ms) |
| Hopper_3_Id | 30009 | 1–100 | ID unique du hopper 3 |
| Hopper_3_Amplitude | 30010 | 50–220 | Amplitude de vibration du hopper 3 |
| Hopper_3_Frequency | 30011 | 40–70 | Fréquence de vibration du hopper 3 |
| Hopper_3_Activation_Time | 30012 | 400–60000 | Temps d'activation du hopper 3 (ms) |
| Hopper_4_Id | 30013 | 1–100 | ID unique du hopper 4 |
| Hopper_4_Amplitude | 30014 | 50–220 | Amplitude de vibration du hopper 4 |
| Hopper_4_Frequency | 30015 | 40–70 | Fréquence de vibration du hopper 4 |
| Hopper_4_Activation_Time | 30016 | 400–60000 | Temps d'activation du hopper 4 (ms) |
| Hopper_1_Enable | 30017 | — | Activer le hopper 1 (action immédiate) |
| Hopper_1_Disable | 30018 | — | Désactiver le hopper 1 (action immédiate) |
| Hopper_2_Enable | 30019 | — | Activer le hopper 2 |
| Hopper_2_Disable | 30020 | — | Désactiver le hopper 2 |
| Hopper_3_Enable | 30021 | — | Activer le hopper 3 |
| Hopper_3_Disable | 30022 | — | Désactiver le hopper 3 |
| Hopper_4_Enable | 30023 | — | Activer le hopper 4 |
| Hopper_4_Disable | 30024 | — | Désactiver le hopper 4 |

:::{note}
Dans le matériel de formation, le ControlWord `30005` (Hopper_2_Id) indiquait par erreur la même plage que l'Amplitude (50–220). Dans ce tableau, elle a été corrigée à **1–100**, de manière cohérente avec Hopper_1_Id, Hopper_3_Id et Hopper_4_Id. Vérifier cette valeur avec le firmware/la fiche technique avant de publier la page.
:::

#### Exemple pratique

Pour consulter un exemple pratique de commande WRITE HOPPER en fieldbus, se reporter à la section [Exemple pratique WRITE HOPPER](fieldbus_WRITEHOPPER).
Pour consulter un exemple pratique de commande WRITE HOPPER en TCP, se reporter à la section [Exemple pratique WRITE HOPPER TCP](TCP_WRITEHOPPER).

### Commandes READ Hopper

| Paramètre | ControlWord READ | Range ReturnData_2 | Notes |
|---|---|---|---|
| Hopper_1_Id | 30101 | 1–100 | |
| Hopper_1_Amplitude | 30102 | 50–220 | |
| Hopper_1_Frequency | 30103 | 40–70 | |
| Hopper_1_Activation_Time | 30104 | 400–60000 | |
| Hopper_2_Id | 30105 | 1–100 | |
| Hopper_2_Amplitude | 30106 | 50–220 | |
| Hopper_2_Frequency | 30107 | 40–70 | |
| Hopper_2_Activation_Time | 30108 | 400–60000 | |
| Hopper_3_Id | 30109 | 1–100 | |
| Hopper_3_Amplitude | 30110 | 50–220 | |
| Hopper_3_Frequency | 30111 | 40–70 | |
| Hopper_3_Activation_Time | 30112 | 400–60000 | |
| Hopper_4_Id | 30113 | 1–100 | |
| Hopper_4_Amplitude | 30114 | 50–220 | |
| Hopper_4_Frequency | 30115 | 40–70 | |
| Hopper_4_Activation_Time | 30116 | 400–60000 | |
| Hopper_1_Ready | 30117 | 0–1 | 0 = non prêt, 1 = prêt |
| Hopper_2_Ready | 30118 | 0–1 | 0 = non prêt, 1 = prêt |
| Hopper_3_Ready | 30119 | 0–1 | 0 = non prêt, 1 = prêt |
| Hopper_4_Ready | 30120 | 0–1 | 0 = non prêt, 1 = prêt |
| Hopper_1_InVibration | 30121 | 0–1 | 0 = arrêté, 1 = en vibration |
| Hopper_2_InVibration | 30122 | 0–1 | 0 = arrêté, 1 = en vibration |
| Hopper_3_InVibration | 30123 | 0–1 | 0 = arrêté, 1 = en vibration |
| Hopper_4_InVibration | 30124 | 0–1 | 0 = arrêté, 1 = en vibration |
| Hopper_1_Enabled | 30125 | 0–1 | 0 = désactivé, 1 = activé |
| Hopper_2_Enabled | 30126 | 0–1 | 0 = désactivé, 1 = activé |
| Hopper_3_Enabled | 30127 | 0–1 | 0 = désactivé, 1 = activé |
| Hopper_4_Enabled | 30128 | 0–1 | 0 = désactivé, 1 = activé |

#### Exemple pratique 

Pour consulter un exemple pratique de commande READ HOPPER en fieldbus, se reporter à la section [Exemple pratique READ HOPPER](fieldbus_READHOPPER).
Pour consulter un exemple pratique de commande READ HOPPER en TCP, se reporter à la section [Exemple pratique READ HOPPER TCP](TCP_READHOPPER).

---

(sec-empty)=
## Commandes Quick Emptying — <span class="isw-section-badge isw-badge-exe"><i class="ph ph-arrow-counter-clockwise"></i> EMPTYING</span>

La fonction **Emptying** permet de vider le plateau du FlexiBowl® en exécutant jusqu'à 4 séquences dédiées, chacune avec son propre nombre de boucles. Ces commandes suivent elles aussi la même logique ControlWord, valable pour tous les protocoles.

### Commandes EXE

| Commande | ControlWord | Busy pendant l'exécution | ReturnData_1 | Explication |
|---|---|---|---|---|
| Start Emptying | 45 | OUI (Emptying actif) | 45 | Démarre le Quick Emptying  |
| Stop Emptying | 46 | OUI (Emptying actif) | 46 | Arrête le Quick Emptying  |
| Emptying Active | 47 | NON | 47 | Vérifie si le Quick Emptying est actif |

### Commandes WRITE

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

:::{note}
`FirstSequence`...`FourthSequence` indiquent laquelle des 20 séquences programmées est exécutée dans chacune des 4 étapes du Quick Emptying ; `FirstLoop`...`FourthLoop` indiquent combien de fois cette étape est répétée.
:::

---

(sec-err)=
## Codes d'erreur

:::{warning}
En présence d'une erreur, la LED **In_Error** s'active et le système n'exécutera pas de nouvelles commandes de mouvement jusqu'à la réinitialisation. Avant d'effectuer la réinitialisation, identifier et résoudre la cause de l'erreur.
:::


### Codes généraux

| ErrorCode | Description |
|---|---|
| 1 | Le mouvement de jog n'a déclenché aucune action sur le moteur |
| 2 | Moteur non connecté |
| 3 | EtherNet/IP sélectionné mais non connecté |
| 4 | Le moteur n'a pas atteint la puissance de fonctionnement dans le délai prévu |
| 5 | Mouvement du moteur demandé, mais le moteur n'est pas alimenté |
| 6 | Erreur du module E/S numérique : module manquant |
| 7 | Erreur du module E/S numérique : erreur de configuration |
| 8 | Erreur du module E/S numérique : erreur générale |

### Codes d'erreur du driver

<div class="isw-search-wrap">
  <input class="isw-search" id="errSearch" type="text" placeholder="Filtrer par code ou description…" oninput="filterErrors()">
  <span class="isw-search-count" id="errCount"></span>
</div>

<div style="margin-top: 2rem;"></div>

<div class="isw-err-wrap">
<table class="isw-err-table" id="errTable">
<thead><tr><th>Code</th><th>Hex</th><th>Erreur</th><th>Description</th></tr></thead>
<tbody>
<tr><td><code>50</code></td><td><code>0x7500</code></td><td>EtherCAT communication error</td><td></td></tr>
<tr><td><code>51</code></td><td><code>0xFF01</code></td><td>Drive Over Current</td><td>Courant moteur excessif</td></tr>
<tr><td><code>52</code></td><td><code>0xFF02</code></td><td>Drive Over Voltage</td><td>Tension du bus DC excessive</td></tr>
<tr><td><code>53</code></td><td><code>0xFF03</code></td><td>Drive Over Temperature</td><td>Température du driver trop élevée</td></tr>
<tr><td><code>54</code></td><td><code>0xFF04</code></td><td>Reserved</td><td></td></tr>
<tr><td><code>55</code></td><td><code>0xFF05</code></td><td>Drive Internal Voltage Error</td><td>Erreur de tension interne</td></tr>
<tr><td><code>56</code></td><td><code>0xFF06</code></td><td>Position Error</td><td>Erreur de positionnement</td></tr>
<tr><td><code>57</code></td><td><code>0xFF07</code></td><td>Motor Encoder Disconnected</td><td>Encodeur non connecté ou défectueux</td></tr>
<tr><td><code>58</code></td><td><code>0xFF0A</code></td><td>Regen Failed</td><td>Erreur dans le circuit de régénération</td></tr>
<tr><td><code>59</code></td><td><code>0xFF0B</code></td><td>Safe Torque Off (STO)</td><td>Fonction de sécurité active</td></tr>
<tr><td><code>60</code></td><td><code>0xFF0C</code></td><td>Reserved</td><td></td></tr>
<tr><td><code>61</code></td><td><code>0xFF0D</code></td><td>Bad FPGA</td><td>Erreur interne du FPGA du driver</td></tr>
<tr><td><code>62</code></td><td><code>0xFF0E</code></td><td>Parameter Read Failed</td><td>Échec de la lecture des paramètres</td></tr>
<tr><td><code>63</code></td><td><code>0xFF0F</code></td><td>Motor Encoder Multi-turn Error</td><td>Erreur de l'encodeur multi-tours</td></tr>
<tr><td><code>64</code></td><td><code>0xFF10</code></td><td>Motor Stall Protection</td><td>Protection contre le calage du moteur active</td></tr>
<tr><td><code>65</code></td><td><code>0xFF11</code></td><td>Drive Power Module Over Temperature</td><td>Module de puissance en surchauffe</td></tr>
<tr><td><code>66</code></td><td><code>0xFF31</code></td><td>N Limit</td><td>Limite de position négative atteinte</td></tr>
<tr><td><code>67</code></td><td><code>0xFF32</code></td><td>P Limit</td><td>Limite de position positive atteinte</td></tr>
<tr><td><code>68</code></td><td><code>0xFF33</code></td><td>N&P Limit</td><td>Les deux limites de position sont atteintes</td></tr>
<tr><td><code>69</code></td><td><code>0xFF34</code></td><td>Current Foldback</td><td>Réduction du courant pour protection thermique</td></tr>
<tr><td><code>70</code></td><td><code>0xFF35</code></td><td>Move @ Disabled</td><td>Tentative de mouvement avec driver désactivé</td></tr>
<tr><td><code>71</code></td><td><code>0xFF36</code></td><td>Drive Low Voltage</td><td>Tension du bus DC insuffisante</td></tr>
<tr><td><code>72</code></td><td><code>0xFF37</code></td><td>Blank Q Segment</td><td>Segment de trajectoire non défini</td></tr>
<tr><td><code>73</code></td><td><code>0xFF38</code></td><td>Velocity Limit</td><td>Limite de vitesse dépassée</td></tr>
<tr><td><code>74</code></td><td><code>0xFF39</code></td><td>Drive Power Phase Lost</td><td>Perte d'une phase d'alimentation</td></tr>
<tr><td><code>75</code></td><td><code>0xFF3A</code></td><td>Emergency Stop</td><td>Arrêt d'urgence actif</td></tr>
<tr><td><code>76</code></td><td><code>0xFF3B</code></td><td>Abs. Encoder Battery</td><td>Batterie de l'encodeur absolu faible ou absente</td></tr>
<tr><td><code>77</code></td><td><code>0xFF3C</code></td><td>Abs. Position Lost Warning</td><td>Avertissement de perte de position absolue</td></tr>
<tr><td><code>78</code></td><td><code>0xFF3D</code></td><td>Abs. Position Overflow</td><td>Dépassement de la position absolue</td></tr>
<tr><td><code>79</code></td><td><code>0xFF3E</code></td><td>Motor Over Temperature</td><td>Température du moteur excessive</td></tr>
<tr><td><code>80</code></td><td><code>0xFF3F</code></td><td>Drive Voltage Warning</td><td>Avertissement : tension du driver hors plage</td></tr>
<tr><td><code>81</code></td><td><code>0xFF41</code></td><td>Save Failed</td><td>Échec de la sauvegarde des paramètres</td></tr>
<tr><td><code>82</code></td><td><code>0xFFFF</code></td><td>Other Error</td><td>Erreur générique non classifiée</td></tr>
</tbody>
</table>
</div>

<script>
function filterErrors() {
  var input = document.getElementById('errSearch').value.toLowerCase();
  var rows = document.querySelectorAll('#errTable tbody tr');
  var count = 0;
  rows.forEach(function(row) {
    var text = row.textContent.toLowerCase();
    if (text.includes(input)) {
      row.classList.remove('isw-hidden');
      count++;
    } else {
      row.classList.add('isw-hidden');
    }
  });
  var countEl = document.getElementById('errCount');
  if (input) {
    countEl.textContent = count + ' ' + (count === 1 ? 'résultat' : 'résultats');
  } else {
    countEl.textContent = '';
  }
}
</script>

</div>


:::{toctree}
:hidden:
04a_interfaccia_software.md
04b_interfaccia_software.md
04c_interfaccia_software.md
:::