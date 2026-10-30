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
  text-align: center;
}
.compare-card-body p, .compare-card-body li { margin: 0.25rem 0; text-align: left; }
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
.compare-card-body video { border-radius: 4px; }
</style>

# **Comparatif pneumatique**

Cette page compare les principales différences pneumatiques entre le **FlexiBowl® 2.0** et le **FlexiBowl® 3.0**.

:::{important}
Avant de lire le contenu de la présente page, il est recommandé de bien connaître les informations figurant dans la page [Spécifications pneumatiques](datipneum)
:::

---

## 1. Caractéristiques de l'air comprimé

```{list-table}
:header-rows: 1
:widths: 30 35 35

* -
  - FlexiBowl® 2.0
  - FlexiBowl® 3.0
* - **Pression d'air requise**
  - 6 Bar
  - 7 Bar
* - **Caractéristiques de l'air**
  - Filtré et séché
  - Air comprimé propre selon ISO 8573-1:2010, classe 1.3.2
```

---

## 2. Réglage et lecture de la pression

<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0</div>
<div class="compare-card-body">

<img src="../../../../_shared/media/images/flip_strength_v20.png" width="200"/>

La force de l'impulsion est réglée au moyen du **régulateur d'air comprimé** situé sur le panneau de commande. L'indicateur de pression correspondant est **intégré au panneau**.

</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0</div>
<div class="compare-card-body">

<img src="../../../../_shared/media/videos/flip_pressure_v30_demo.gif" width="100%"/>

Le réglage et la lecture de la pression sont paramétrables **directement depuis l'interface logicielle**.

</div>
</div>
</div>

---

## 3. Commande du soufflage (Blow)

<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0</div>
<div class="compare-card-body">

<img src="../../../../_shared/media/images/dettaglio_pneumatico.png" width="220"/>

Réglage au moyen de composants pneumatiques physiques (raccords et régulateurs sur l'unité).

</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0</div>
<div class="compare-card-body">

<img src="../../../../_shared/media/videos/blow_control_v30_demo.gif" width="100%"/>

Commande native du soufflage (**Native Blow Control**) directement depuis l'interface logicielle : Flip Pressure, Flip Count, Flip Delay, Blow Pressure, Blow Time.

</div>
</div>
</div>

:::{note}
Pour le détail du raccordement de l'alimentation en air, se reporter à la page [Interface pneumatique](datipneum).
:::

---

## 4. Synthèse

Le FlexiBowl® 3.0 nécessite une pression d'air légèrement supérieure (7 Bar contre 6 Bar) et spécifie une classe de propreté ISO 8573-1:2010 1.3.2, non définie sur la génération précédente. La différence la plus significative du point de vue de l'utilisabilité est le déplacement du réglage et de la lecture de la pression, du flip et du soufflage, des composants physiques du panneau vers l'interface logicielle.
