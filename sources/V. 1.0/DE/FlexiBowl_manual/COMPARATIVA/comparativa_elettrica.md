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

# **Elektrischer Vergleich**

Diese Seite vergleicht die wichtigsten elektrischen Unterschiede zwischen **FlexiBowl® 2.0** und **FlexiBowl® 3.0** hinsichtlich Spannungsversorgung, Konnektivität und Sicherheit.

:::{important}
Bevor Sie den Inhalt dieser Seite lesen, empfiehlt es sich, die Informationen auf der Seite [Elektrische und pneumatische Spezifikationen](dati_elettrici) zu kennen
:::

---

## 1. Spannungsversorgung

```{list-table}
:header-rows: 1
:widths: 25 37 38

* -
  - FlexiBowl® 2.0
  - FlexiBowl® 3.0
* - **AC-Versorgung**
  - 110-220 Vac ±5%
  - 110-230 Vac ±5%
* - **Frequenz**
  - 50/60 Hz
  - 50/60 Hz
* - **Nennleistung**
  - 150 W
  - 345-920 W *(je nach FlexiBowl®-Baugröße)*
* - **DC-Versorgung**
  - Intern erzeugt
  - Intern erzeugt
```

:::{note}
Der FlexiBowl® 3.0 nimmt eine höhere Nennleistung auf als die Vorgängergeneration, da die Antriebselektronik (Drive) direkt in die Einheit integriert ist.
:::

---

## 2. Ethernet-Konnektivität

<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0</div>
<div class="compare-card-body">

Standard-Stecker **RJ45**.

</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0</div>
<div class="compare-card-body">

Stecker **M12 D-Kodierung**.

</div>
</div>
</div>

---

## 3. Sicherheit

<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0</div>
<div class="compare-card-body">

Um die Einheit sicher anzuhalten, muss die **230-Vac-Versorgung vollständig getrennt werden**.

</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0</div>
<div class="compare-card-body">

<img src="../../../../_shared/media/images/connettore_STO.png" width="110"/>

Integrierte Funktion **Safe Torque Off (STO)**, die ein sicheres Anhalten ermöglicht, ohne die Versorgung trennen zu müssen.

</div>
</div>
</div>

:::{note}
Einzelheiten zu den STO-Kanälen und deren Verdrahtung finden Sie auf der Seite [Elektrische Schnittstelle](dati_elettrici).
:::

---

## 4. Zusammenfassung

Der FlexiBowl® 3.0 nimmt aufgrund der integrierten Antriebselektronik mehr Leistung auf als die Vorgängergeneration, bietet jedoch einen robusteren Ethernet-Stecker (M12 D-Kodierung) und eine integrierte STO-Sicherheitsfunktion, die es überflüssig macht, die Versorgung zu trennen, um die Einheit sicher anzuhalten.
