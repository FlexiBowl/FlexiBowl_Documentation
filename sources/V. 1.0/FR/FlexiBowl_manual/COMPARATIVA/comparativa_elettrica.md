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
</style>

# **Comparatif électrique**

Cette page compare les principales différences électriques entre le **FlexiBowl® 2.0** et le **FlexiBowl® 3.0**, en termes d'alimentation, de connectivité et de sécurité.

:::{important}
Avant de lire le contenu de la présente page, il est recommandé de bien connaître les informations figurant dans la page [Spécifications électriques et pneumatiques](dati_elettrici)
:::

---

## 1. Alimentation

```{list-table}
:header-rows: 1
:widths: 25 37 38

* -
  - FlexiBowl® 2.0
  - FlexiBowl® 3.0
* - **Alimentation AC**
  - 110-220 Vac ±5%
  - 110-230 Vac ±5%
* - **Fréquence**
  - 50/60 Hz
  - 50/60 Hz
* - **Puissance nominale**
  - 150 W
  - 345-920 W *(selon la taille du FlexiBowl®)*
* - **Alimentation DC**
  - Générée en interne
  - Générée en interne
```

:::{note}
Le FlexiBowl® 3.0 absorbe une puissance nominale supérieure à celle de la génération précédente, car l'électronique d'entraînement (drive) est directement intégrée dans l'unité.
:::

---

## 2. Connectivité Ethernet

<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0</div>
<div class="compare-card-body">

Connecteur **RJ45** standard.

</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0</div>
<div class="compare-card-body">

Connecteur **M12 codage D**.

</div>
</div>
</div>

---

## 3. Sécurité

<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0</div>
<div class="compare-card-body">

Pour arrêter l'unité en toute sécurité, il est nécessaire de **déconnecter complètement l'alimentation 230 Vac**.

</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0</div>
<div class="compare-card-body">

<img src="../../../../_shared/media/images/connettore_STO.png" width="110"/>

Fonction **Safe Torque Off (STO)** intégrée, qui permet l'arrêt sécurisé sans devoir déconnecter l'alimentation.

</div>
</div>
</div>

:::{note}
Pour le détail des canaux STO et de leur câblage, se reporter à la page [Interface électrique](dati_elettrici).
:::

---

## 4. Synthèse

Le FlexiBowl® 3.0 absorbe plus de puissance que la génération précédente en raison de l'électronique d'entraînement intégrée, mais il introduit un connecteur Ethernet plus robuste (M12 codage D) et une fonction de sécurité STO intégrée, qui évite de devoir déconnecter l'alimentation pour arrêter l'unité en toute sécurité.
