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

# **Pneumatischer Vergleich**

Diese Seite vergleicht die wichtigsten pneumatischen Unterschiede zwischen **FlexiBowl® 2.0** und **FlexiBowl® 3.0**.

:::{important}
Bevor Sie den Inhalt dieser Seite lesen, empfiehlt es sich, die Informationen auf der Seite [Pneumatische Spezifikationen](datipneum) zu kennen
:::

---

## 1. Eigenschaften der Druckluft

```{list-table}
:header-rows: 1
:widths: 30 35 35

* -
  - FlexiBowl® 2.0
  - FlexiBowl® 3.0
* - **Erforderlicher Luftdruck**
  - 6 Bar
  - 7 Bar
* - **Eigenschaften der Luft**
  - Gefiltert und getrocknet
  - Saubere Druckluft gemäß ISO 8573-1:2010, Klasse 1.3.2
```

---

## 2. Einstellung und Ablesen des Drucks

<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0</div>
<div class="compare-card-body">

<img src="../../../../_shared/media/images/flip_strength_v20.png" width="200"/>

Die Impulskraft wird über den **Druckluftregler** am Bedienfeld eingestellt. Die zugehörige Druckanzeige ist **im Bedienfeld integriert**.

</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0</div>
<div class="compare-card-body">

<img src="../../../../_shared/media/videos/flip_pressure_v30_demo.gif" width="100%"/>

Einstellung und Ablesen des Drucks sind **direkt über die Software-Oberfläche** möglich.

</div>
</div>
</div>

---

## 3. Steuerung der Blasluft (Blow)

<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0</div>
<div class="compare-card-body">

<img src="../../../../_shared/media/images/dettaglio_pneumatico.png" width="220"/>

Einstellung über physische pneumatische Komponenten (Anschlüsse und Regler an der Einheit).

</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0</div>
<div class="compare-card-body">

<img src="../../../../_shared/media/videos/blow_control_v30_demo.gif" width="100%"/>

Native Steuerung der Blasluft (**Native Blow Control**) direkt über die Software-Oberfläche: Flip Pressure, Flip Count, Flip Delay, Blow Pressure, Blow Time.

</div>
</div>
</div>

:::{note}
Einzelheiten zum Anschluss der Luftversorgung finden Sie auf der Seite [Pneumatische Schnittstelle](datipneum).
:::

---

## 4. Zusammenfassung

Der FlexiBowl® 3.0 erfordert einen etwas höheren Luftdruck (7 Bar gegenüber 6 Bar) und gibt eine Reinheitsklasse nach ISO 8573-1:2010 1.3.2 vor, die bei der Vorgängergeneration nicht definiert war. Der aus Sicht der Bedienbarkeit wichtigste Unterschied ist die Verlagerung der Einstellung und Anzeige von Druck, Flip und Blasluft von den physischen Komponenten des Bedienfelds in die Software-Oberfläche.
