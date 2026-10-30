# **Verdrahtung des FlexiBowl®**

<style>
.ars-dropdown {
  margin-top: 0.35rem;
}
.ars-dropdown summary {
  cursor: pointer;
  color: #2980b9;
  font-weight: 600;
  font-size: 0.82rem;
  padding: 0.35rem 0.7rem;
  border: 1px solid #d0e4f0;
  border-radius: 6px;
  display: inline-block;
  background: #f0f7ff;
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
  border-radius: 6px 6px 0 0;
}
.ars-dropdown .ars-dropdown-body {
  border: 1px solid #d0e4f0;
  border-top: none;
  border-radius: 0 0 6px 6px;
  padding: 0.6rem;
  background: #fff;
}
.ars-dropdown img {
  display: block;
  max-width: 100%;
  width: 360px;
  border-radius: 4px;
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
.ars-pin-table { width:100%; border-collapse:collapse; font-size:0.8rem; margin-top:0.4rem; }
.ars-pin-table th { background:#f0f4f8; padding:0.3rem 0.5rem; text-align:left; border:1px solid #d0e4f0; }
.ars-pin-table td { padding:0.3rem 0.5rem; border:1px solid #d0e4f0; }


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

* - **Elektrofachkraft für die Wartung**
  - :::{raw} html
       <div class="ars-img-row">
         <img src="../../../../_shared/media/images/guanti.png" alt="Handschuhe">
         <img src="../../../../_shared/media/images/scarpe.png" alt="Schuhe">
         <img src="../../../../_shared/media/images/tuta.png" alt="Overall">
       </div>
    :::
::::
:::::

:::{warning}
Vor jedem elektrischen Anschluss sicherstellen, dass die Spannungsversorgung getrennt ist und sich das System in einem sicheren Zustand befindet.
:::

Die Verdrahtung des FlexiBowl® richtet sich nach der Baugröße der Maschine:

- **FlexiBowl® 500 – 1200**: Alle Anschlüsse (STO, Ethernet, Hopper, Stromversorgung, Luft) befinden sich auf einem einzigen **Standard-Schaltfeld**, das direkt an der Maschine montiert ist.
- **FlexiBowl® 200 / 350**: Die Hauptanschlüsse befinden sich an einem externen **Rack**; das Rack wird anschließend über 4 dedizierte Kabel (Ethernet, Motor+STO, Signal A, Signal B) mit der Maschine verbunden. An der Maschine muss nur noch die Druckluft angeschlossen werden.

---

## FlexiBowl® 500 – 1200 — Elektrisches Standard-Anschlussfeld

```{list-table}
:widths: 8 52 40
:header-rows: 1

* - #
  - Aktion
  - Bild
* - 1
  - **Den STO anschließen.**

    <div class="ars-step-note">
    10-poliger Steckverbinder. Die Eingänge <strong>+STO1</strong> und <strong>+STO2</strong> müssen vom Sicherheitskreis <strong>+24 V DC</strong> erhalten; <strong>−STO1</strong> und <strong>−STO2</strong> sind mit dem Bezugspotenzial −24 V DC zu verbinden.
    </div>

    <details class="ars-dropdown"><summary>Pinbelegung des 10-poligen Steckverbinders</summary><div class="ars-dropdown-body">

    | Pin | Beschreibung |
    |---|---|
    | 1 | +24 Vdc |
    | 2 | −24 Vdc |
    | 3 | +STO1 |
    | 4 | −STO1 |
    | 5 | +STO2 |
    | 6 | −STO2 |
    | 7–10 | NC |

    </div></details>
  - 
    ```{image} ../../../../_shared/media/images/connectSTO.png
    :alt: Den STO anschließen
    :class: ars-zoom-img
    ```

* - 2
  - **Das Ethernet (C-ETH) anschließen.**

    <div class="ars-step-attn">
    Wenn der FlexiBowl® mit Spannung versorgt wird, ist die Ethernet-Verbindung <strong>zwingend erforderlich</strong>: Fehlt sie, geht die Maschine in den Zustand <strong>ERROR</strong> über (rote LED Ready/Fault).
    </div>

    <details class="ars-dropdown"><summary>Pinbelegung M12 → RJ45</summary><div class="ars-dropdown-body">

    Adapter M12 8-polig → RJ45:

    | RJ45-Pin | Signal | Funktion | Farbe |
    |---|---|---|---|
    | 1 | TD+ | Datenübertragung (+) | Gelb |
    | 2 | TD− | Datenübertragung (−) | Orange |
    | 3 | RD+ | Datenempfang (+) | Weiß |
    | 4 | NC | Nicht belegt | — |
    | 5 | NC | Nicht belegt | — |
    | 6 | RD− | Datenempfang (−) | Blau |
    | 7 | NC | Nicht belegt | — |
    | 8 | NC | Nicht belegt | — |

    4-poliger M12-Stecker, D-kodiert:

    | M12-Pin | Signal | Funktion | Farbe |
    |---|---|---|---|
    | 1 | TD+ | Datenübertragung (+) | Gelb |
    | 2 | RD+ | Datenempfang (+) | Weiß |
    | 3 | TD− | Datenübertragung (−) | Orange |
    | 4 | RD− | Datenempfang (−) | Blau |

    </div></details>
  - 
    ```{image} ../../../../_shared/media/images/connectEthernet.png
    :alt: Das Ethernet anschließen
    :class: ars-zoom-img
    ```

* - 3
  - **Den Hopper anschließen.**

    <div class="ars-step-note">
    M12-Steckverbinder mit A-Kodierung, der zur Kommunikation mit ARS-Hopper-Steuerungen über das Protokoll <strong>Modbus RTU</strong> dient.
    </div>

    <details class="ars-dropdown"><summary>Pinbelegung M12 A-kodiert</summary><div class="ars-dropdown-body">

    | M12-Pin | Signal | Funktion | Farbe |
    |---|---|---|---|
    | 1 | A+ | RS485-Datenleitung (+) | Braun |
    | 2 | NC | Nicht belegt | Weiß |
    | 3 | B− | RS485-Datenleitung (−) | Blau |
    | 4 | GND | Gemeinsame Bezugsmasse | Schwarz |
    | 5 | NC | Nicht belegt | Grau |

    </div></details>
  - 
    ```{image} ../../../../_shared/media/images/connectHopper.png
    :alt: Den Hopper anschließen
    :class: ars-zoom-img
    ```

* - 4
  - **Stromversorgung (Power Supply) anschließen.**

    <div class="ars-step-attn">
    Sicherstellen, dass der FlexiBowl® <strong>ausgeschaltet</strong> ist, bevor die Spannungsversorgung angeschlossen wird.
    </div>

    <div class="ars-step-warn">
    Zulässige Spannung: <strong>120–230 Vac, 50/60 Hz</strong>.
    </div>

    <div class="ars-step-note">
    Prüfen Sie beim ersten Start den Zustand der Sicherungen. Warten Sie nach dem Einschalten, bis die Status-LED (Ready/Fault) leuchtet: Wenn Hopper und C-ETH korrekt angeschlossen sind, leuchtet die LED <strong>grün</strong>.
    </div>

    <details class="ars-dropdown"><summary>Pinbelegungsschema des Stromversorgungskabels</summary><div class="ars-dropdown-body">

    | Farbe | Typ | Beschriftung |
    |---|---|---|
    | Braun | Phase | L1 |
    | Blau | Neutralleiter | N1 |
    | Gelb/Grün | Erde | PE1 |

    </div></details>
  - 
    ```{image} ../../../../_shared/media/images/connectSupply.png
    :alt: Die Spannungsversorgung anschließen
    :class: ars-zoom-img
    ```

* - 5
  - **Druckluft anschließen** mit einem Schlauch **Ø 8 mm**.

    :::{note}
    Die erforderlichen Luftkennwerte (Druck, ISO-Reinheitsklasse) finden Sie in den [Technischen Daten Pneumatik](datipneum).
    :::
  - 
    ```{image} ../../../../_shared/media/images/connectAir.png
    :alt: Die Druckluft Ø8mm anschließen
    :class: ars-zoom-img
    ```
```
:::{video} ../../../../_shared/media/videos/cablaggio_FB800.mp4
:width: 100% 
:::

---

## FlexiBowl® 200 / 350 — Externes Rack

Bei diesen Baugrößen befinden sich die Anschlüsse zu den Anlagen des Kunden am externen **Rack** (nicht an der Maschine). Das Rack muss anschließend über 4 dedizierte Kabel mit der Maschine verbunden werden.

### Anschlüsse am Rack

Die Steckverbinder des Racks entsprechen denen des Standard-Schaltfelds (gleiche Pinbelegung), sind jedoch in einem externen Gehäuse statt an der Maschine angeordnet.

```{list-table}
:header-rows: 1

* - #
  - Aktion

* - 1
  - **STO anschließen** am Rack — derselbe 10-polige Steckverbinder wie am Standard-Schaltfeld (siehe Pinbelegungstabelle oben).

* - 2
  - **C-ETH IN anschließen** am Rack — derselbe M12-Steckverbinder mit D-Kodierung wie am Standard-Schaltfeld. Es gilt dieselbe Regel: Der Anschluss ist zwingend erforderlich, andernfalls geht die Maschine in den Zustand ERROR.

* - 3
  - **Hopper anschließen** am Rack — derselbe M12-Steckverbinder mit A-Kodierung (Modbus RTU) wie am Standard-Schaltfeld.

* - 4
  - **Stromversorgung anschließen** am Rack — 120–230 V AC.

    <div class="ars-step-attn">
    Sicherstellen, dass der FlexiBowl® <strong>ausgeschaltet</strong> ist, bevor die Spannungsversorgung angeschlossen wird.
    </div>
```

### Verbindung zwischen Rack und FlexiBowl®

Das Rack kommuniziert über 4 dedizierte Kabel mit dem FlexiBowl®; jedes davon ist **ausschließlich** an den Anschluss mit der entsprechenden Beschriftung am Schaltfeld anzuschließen.

:::{attention}
Jedes Kabel mit dem Anschluss mit dem **entsprechenden Etikett** verbinden (z. B. MOTOR ↔ MOTOR, C-A SIGNAL ↔ C-A SIGNAL). Eine vertauschte Verbindung kann das System beschädigen.
:::

```{list-table}
:widths: 8 52 40
:header-rows: 1

* - #
  - Aktion
  - Bild
* - 5
  - **Ethernet-Kabel (C-ETH FB) anschließen** zwischen Rack und FlexiBowl® — M12-Steckverbinder mit D-Kodierung.
  - 
    ```{image} ../../../../_shared/media/images/connectEthernet200.png
    :width: 110%
    :alt: Das Kabel C-ETH FB anschließen
    :class: ars-zoom-img
    ```
* - 6
  - **Das MOTOR-Kabel anschließen.**

    <div class="ars-step-note">
    9-poliger Steckverbinder: führt sowohl die Motorversorgung als auch die <strong>STO</strong>-Signale zum FlexiBowl® (am Rack sind STO und Motor getrennte Steckverbinder; am Kabel zur Maschine sind sie in einem einzigen 9-poligen Steckverbinder zusammengefasst).
    </div>
  - 
    ```{image} ../../../../_shared/media/images/connectMotor.png
    :width:110%
    :alt: Das Motor-Kabel anschließen
    :class: ars-zoom-img
    ```
* - 7
  - **Kabel C-A SIGNAL anschließen** — 19-poliger Steckverbinder für die analogen Signale.
  - 
    ```{image} ../../../../_shared/media/images/connectASignal.png
    :width:110%
    :alt: Das Kabel C-A Signal anschließen
    :class: ars-zoom-img
    ```
* - 8
  - **Kabel C-B SIGNAL anschließen** — 19-poliger Steckverbinder für die digitalen Signale.
  - 
    ```{image} ../../../../_shared/media/images/connectBSignal.png
    :width:110%
    :alt: Das Kabel C-B Signal anschließen
    :class: ars-zoom-img
    ```
* - 9
  - **Druckluft anschließen** mit einem Schlauch **Ø 6 mm**, direkt am Schaltfeld der Maschine.

    :::{note}
    Die erforderlichen Luftkennwerte (Druck, ISO-Reinheitsklasse) finden Sie in den [Technischen Daten Pneumatik](datipneum).
    :::
  - 
    ```{image} ../../../../_shared/media/images/connectAir200.png
    :width:110%
    :alt: Die Druckluft Ø6mm anschließen
    :class: ars-zoom-img
    ```
```
:::{video} ../../../../_shared/media/videos/cablaggio_FB200.mp4
:width: 100% 
:::