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

# **Pneumatic Comparison**

This page compares the main pneumatic differences between **FlexiBowl® 2.0** and **FlexiBowl® 3.0**.

:::{important}
Before reading the contents of this page, it is good practice to be familiar with the information given on the [Pneumatic Specifications](datipneum) page
:::

---

## 1. Compressed air characteristics

```{list-table}
:header-rows: 1
:widths: 30 35 35

* -
  - FlexiBowl® 2.0
  - FlexiBowl® 3.0
* - **Required air pressure**
  - 6 Bar
  - 7 Bar
* - **Air characteristics**
  - Filtered and dried
  - Clean compressed air according to ISO 8573-1:2010, class 1.3.2
```

---

## 2. Pressure adjustment and reading

<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0</div>
<div class="compare-card-body">

<img src="../../../../_shared/media/images/flip_strength_v20.png" width="200"/>

The impulse force is adjusted via the **compressed air regulator** located on the control panel. The corresponding pressure gauge is **integrated into the panel**.

</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0</div>
<div class="compare-card-body">

<img src="../../../../_shared/media/videos/flip_pressure_v30_demo.gif" width="100%"/>

Pressure adjustment and reading can be set **directly from the software interface**.

</div>
</div>
</div>

---

## 3. Blow control

<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0</div>
<div class="compare-card-body">

<img src="../../../../_shared/media/images/dettaglio_pneumatico.png" width="220"/>

Adjustment via physical pneumatic components (fittings and regulators on the unit).

</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0</div>
<div class="compare-card-body">

<img src="../../../../_shared/media/videos/blow_control_v30_demo.gif" width="100%"/>

Native blow control (**Native Blow Control**) directly from the software interface: Flip Pressure, Flip Count, Flip Delay, Blow Pressure, Blow Time.

</div>
</div>
</div>

:::{note}
For details on connecting the air supply, refer to the [Pneumatic Interface](datipneum) page.
:::

---

## 4. Summary

FlexiBowl® 3.0 requires a slightly higher air pressure (7 Bar versus 6 Bar) and specifies an ISO 8573-1:2010 1.3.2 cleanliness class, which was not defined for the previous generation. The most significant difference from a usability standpoint is the shift of pressure, flip and blow adjustment and reading from the physical components of the panel to the software interface.
