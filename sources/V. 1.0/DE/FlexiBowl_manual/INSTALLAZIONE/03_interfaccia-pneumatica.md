(intpneum)=
# **Pneumatische Schnittstelle**

Die Maschine ist mit einem pneumatischen Antrieb ausgestattet. Vor dem **Druckluftanschluss** ist Folgendes zu prüfen:
- die vorhandene Druckluftversorgungsanlage der Maschine die Luftmenge mit dem richtigen Druck sicherstellt;
- der vorgesehene Druckluftbehälter korrekt dimensioniert ist.

Der Druckluftanschluss ist durch Verbinden der Hauptleitung mit dem Maschinenkreis herzustellen. Der Kunde muss außerdem eine Luftversorgung mit den im Absatz {ref}`„Technische Daten Pneumatik“ <datipneum>` dieses Handbuchs aufgeführten Eigenschaften sicherstellen.

:::{warning}
Im pneumatischen System der Maschine niemals einen Druck von 7 bar überschreiten.
:::

:::{warning}
Der FlexiBowl® wird ohne manuelle Absperr- und Entlüftungseinrichtung für die Druckluftversorgung geliefert. Der Integrator muss vorgelagert eine klar gekennzeichnete, leicht zugängliche und in Schließstellung verriegelbare Einrichtung vorsehen, die es ermöglicht, die Versorgung zu unterbrechen, den Restdruck abzubauen und ein unbeabsichtigtes Wiedereinschalten zu verhindern. Rohre und Anschlüsse müssen für den Betriebsdruck geeignet, korrekt befestigt und gegen Herausrutschen gesichert sein. Eventuelle weitere pneumatische Sicherheitseinrichtungen sind anhand der Risikobeurteilung der Endmaschine festzulegen.
:::

:::::{important}

:::{raw} html
   <style>
     .ars-img-row { display: flex; gap: 12px; align-items: center; justify-content: center; }
     .ars-img-row img { width: 25%; }
   </style>
:::

::::{list-table}
:widths: 30 60
:header-rows: 1
* - {ref}`Qualifikation des Bedieners <operatori>`
  - {ref}`Erforderliche PSA <dpi>`

* - **Mechanischer Instandhalter**
  - :::{raw} html
       <div class="ars-img-row">
         <img src="../../../../_shared/media/images/guanti.png" alt="Handschuhe">
         <img src="../../../../_shared/media/images/scarpe.png" alt="Schuhe">
         <img src="../../../../_shared/media/images/tuta.png" alt="Overall">
       </div>
    :::
::::
:::::

Für den Anschluss an das Druckluftnetz einen Luftschlauch {ref}`in der richtigen Größe <datipneum>` an den Eingang „Air Supply“ am {ref}`Bedienfeld <intele>` anschließen.

:::{raw} html
<style>
.img-zoom-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 16px;
  padding: 1rem 0;
}
.img-zoom-wrap {
  flex: 1 1 0;
  min-width: 0;
  overflow: visible;
  display: flex;
  align-items: center;
  justify-content: center;
}
.img-zoom-wrap img {
  width: 100%;
  border-radius: 8px;
  transition: transform 0.35s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.35s ease;
  cursor: zoom-in;
  position: relative;
  transform: scale(1);
}
.img-zoom-wrap img:hover {
  transform: scale(1.85);
  box-shadow: 0 12px 40px rgba(0,0,0,0.22);
  z-index: 10;
}
</style>

<div class="img-zoom-grid">
  <div class="img-zoom-wrap">
    <img src="../../../../_shared/media/images/smallpanel5.PNG" alt="Small-Anschlussfeld" />
  </div>
  <div class="img-zoom-wrap">
    <img src="../../../../_shared/media/images/stpanel2.PNG" alt="ST-Anschlussfeld" />
  </div>
  <div class="img-zoom-wrap">
    <img src="../../../../_shared/media/images/encpanel7.PNG" alt="ENC-Anschlussfeld" />
  </div>
</div>
:::

<style>
.ars-dropdown {
  margin: 0.9rem 0 0.4rem 0;
  border: 2px solid #7fb3dd;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 6px rgba(26,111,196,0.10);
}
.ars-dropdown summary {
  cursor: pointer;
  color: #2980b9;
  font-weight: 600;
  font-size: 0.83rem;
  padding: 0.5rem 0.9rem;
  display: block;
  background: #eaf3fb;
  list-style: none;
  user-select: none;
}
.ars-dropdown summary::-webkit-details-marker { display: none; }
.ars-dropdown summary::before {
  content: "▸ ";
}
.ars-dropdown[open] summary::before {
  content: "▾ ";
}
.ars-dropdown[open] summary {
  border-bottom: 2px solid #7fb3dd;
}
.ars-dropdown .ars-dropdown-body {
  padding: 0.9rem 1rem;
  background: #fff;
}
.ars-step-warn, .ars-step-attn, .ars-step-note {
  border-radius: 5px;
  padding: 0.5rem 0.75rem;
  font-size: 0.83rem;
  margin-top: 0.55rem;
  line-height: 1.4;
}
.ars-step-warn { background:#fff3cd; border-left:4px solid #f0ad4e; color:#7a5b00; }
.ars-step-attn { background:#fee2e2; border-left:4px solid #dc2626; color:#8a1c1c; }
.ars-step-note { background:#eef6fc; border-left:4px solid #2980b9; color:#1a3a52; }

.ars-zoom-img {
  transition: transform 0.35s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.35s ease;
  cursor: zoom-in;
  position: relative;
}
.ars-zoom-img:hover {
  transform: scale(1.8);
  box-shadow: 0 12px 40px rgba(0,0,0,0.22);
  z-index: 10;
}
</style>

---

## Erforderliche Eigenschaften der Luft

| Parameter | Wert |
|---|---|
| Luftqualität | Saubere und trockene Druckluft gemäß **ISO 8573-1:2010, Klasse 1.3.2** |
| Empfohlener Versorgungsdruck | **7 bar** (darf niemals überschritten werden) |
| Schlauchdurchmesser — FB200 / FB350 | **Ø 6 mm** |
| Schlauchdurchmesser — FB500E / FB500 / FB650 / FB800 / FB1200 | **Ø 8 mm** |

<details class="ars-dropdown"><summary>Richtwerte des Luftverbrauchs je Modell (Flip-Aktion)</summary><div class="ars-dropdown-body">

| Modell | Durchschnittlicher Verbrauch | Spitzenverbrauch |
|---|---|---|
| FB200 | 25 l/min | 45 l/min |
| FB350 | 15 l/min | 24 l/min |
| FB500E | 55 l/min | 74 l/min |
| FB500 | 35 l/min | 48 l/min |
| FB650 | 30 l/min | 45 l/min |
| FB800 | 45 l/min | 60 l/min |
| FB1200 | 135 l/min | 176 l/min |

Die angegebenen Werte beziehen sich nur auf die Flip-Aktion; für vollständige Angaben zum Verbrauch siehe Absatz {ref}`„Technische Daten Pneumatik“ <datipneum>`.

</div></details>

:::{note}
Beim FlexiBowl® 3.0 erfolgen die Druckeinstellung und das Ablesen des Manometers über die **Software-Oberfläche** und nicht mehr über einen physischen Regler und ein Manometer am Bedienfeld wie bei der Vorgängergeneration 2.0.
:::

---

## Geführtes Verfahren — Druckluftanschluss

Auch beim Druckluftanschluss ändert sich das Verfahren je nach Baugröße der Maschine leicht, insbesondere beim Schlauchdurchmesser und bei der Position des Anschlusses **AIR SUPPLY**.

:::{attention}
Vor Beginn jedes Druckluftanschlusses sicherstellen, dass die Druckluftversorgung **getrennt** und der Restdruck im Kreis **abgebaut** wurde.
:::

### FlexiBowl® 500 – 1200 — Elektrisches Standard-Anschlussfeld

```{list-table}
:widths: 8 52 40
:header-rows: 1

* - #
  - Aktion
  - Bild
* - 1
  - **Vorprüfungen.**

    Prüfen, ob die Versorgungsanlage den erforderlichen Druck und Volumenstrom sicherstellt und ob der Druckluftbehälter für das installierte Modell korrekt dimensioniert ist.

    <div class="ars-step-note">
    Saubere und trockene Luft gemäß ISO 8573-1:2010, Klasse 1.3.2. Empfohlener Druck: 7 bar.
    </div>
  -

* - 2
  - **Die Luftversorgung abtrennen**, und zwar vorgelagert an der Anlage, bevor der Schlauch angeschlossen wird.

    <div class="ars-step-attn">
    Den Luftschlauch niemals anschließen oder abziehen, solange die Anlage noch unter Druck steht.
    </div>
  -

* - 3
  - **Den Luftschlauch** an den Eingang **AIR SUPPLY** am elektrischen Standard-Anschlussfeld anschließen, wobei ein Schlauch mit einem Außendurchmesser von **Ø 8 mm** zu verwenden ist.
  -
    ```{image} ../../../../_shared/media/images/connectAir.png
    :alt: Die Druckluft Ø8mm anschließen
    :class: ars-zoom-img
    ```

* - 4
  - **Die Dichtheit des Anschlusses prüfen**: Kontrollieren, dass der Anschluss korrekt eingesteckt ist und dass entlang des Schlauchs und des Anschlusses keine hörbaren oder fühlbaren Leckagen vorhanden sind.
  -

* - 5
  - **Die Luftversorgung wieder zuschalten** und prüfen, ob der Druck stromabwärts innerhalb der vorgesehenen Parameter liegt.

    <div class="ars-step-note">
    Beim FlexiBowl® 3.0 kann der Druck direkt über die Software-Oberfläche abgelesen und eingestellt werden.
    </div>
  -
```

### FlexiBowl® 200 / 350

Bei diesen Baugrößen befindet sich der Anschluss **AIR SUPPLY** direkt am Maschinen-Anschlussfeld (nicht am externen Rack), nach allen anderen Verdrahtungen.

```{list-table}
:widths: 8 52 40
:header-rows: 1

* - #
  - Aktion
  - Bild
* - 1
  - **Vorprüfungen.**

    Prüfen, ob die Versorgungsanlage den erforderlichen Druck und Volumenstrom sicherstellt und ob der Druckluftbehälter für das installierte Modell korrekt dimensioniert ist.

    <div class="ars-step-note">
    Saubere und trockene Luft gemäß ISO 8573-1:2010, Klasse 1.3.2. Empfohlener Druck: 7 bar.
    </div>
  -

* - 2
  - **Die Luftversorgung abtrennen**, und zwar vorgelagert an der Anlage, bevor der Schlauch angeschlossen wird.

    <div class="ars-step-attn">
    Den Luftschlauch niemals anschließen oder abziehen, solange die Anlage noch unter Druck steht.
    </div>
  -

* - 3
  - **Den Luftschlauch** direkt am Maschinen-Anschlussfeld anschließen, wobei ein Schlauch mit einem Außendurchmesser von **Ø 6 mm** zu verwenden ist.
  -
    ```{image} ../../../../_shared/media/images/connectAir200.png
    :width: 110%
    :alt: Die Druckluft Ø6mm anschließen
    :class: ars-zoom-img
    ```

* - 4
  - **Die Dichtheit des Anschlusses prüfen**: Kontrollieren, dass der Anschluss korrekt eingesteckt ist und dass entlang des Schlauchs und des Anschlusses keine hörbaren oder fühlbaren Leckagen vorhanden sind.
  -

* - 5
  - **Die Luftversorgung wieder zuschalten** und prüfen, ob der Druck stromabwärts innerhalb der vorgesehenen Parameter liegt.

    <div class="ars-step-note">
    Beim FlexiBowl® 3.0 kann der Druck direkt über die Software-Oberfläche abgelesen und eingestellt werden.
    </div>
  -
```

---

## Allgemeine Hinweise und Warnungen

:::{attention}
Alle Arbeiten zum Anschließen und Trennen der Druckluft müssen bei **abgetrennter** Anlage und **abgebautem Restdruck** durchgeführt werden.
:::

:::{attention}
Im pneumatischen System der Maschine niemals einen Druck von **7 bar** überschreiten.
:::

:::{attention}
Der FlexiBowl® ist nicht mit einer manuellen Absperr- und Entlüftungseinrichtung ausgestattet: Es liegt in der Verantwortung des Integrators, vorgelagert eine solche vorzusehen, die klar gekennzeichnet, zugänglich und in Schließstellung verriegelbar ist.
:::

:::{attention}
Ausschließlich Schläuche und Anschlüsse verwenden, die für den Betriebsdruck geeignet, korrekt befestigt und gegen Herausrutschen gesichert sind.
:::

:::{attention}
Für weitere technische Informationen oder Unterstützung wenden Sie sich an ARS s.r.l. – FlexiBowl® Division.
:::
