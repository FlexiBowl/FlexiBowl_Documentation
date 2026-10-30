# **Steuerung und Verdrahtung**

Die Maschine benötigt im Betrieb nicht die ständige Anwesenheit eines Bedieners.

:::{attention}
Die Verwendung der Maschine für einen anderen als den vom Hersteller vorgesehenen Zweck kann zu schweren Schäden an Personen und/oder Sachen und/oder Tieren führen. Die Firma ARS S.r.l. haftet nicht für Schäden, die durch unsachgemäße Verwendung der Maschine entstehen.
:::

## Beschreibung der Steuerung

Die **digitale Steuerung** (Mod. SDVC34-XLRH) ist eine frequenzvariable Steuerung mit Mikroprozessor, **LED**-Display und Bedientastatur (Tasten **Vol+/Vol-** für die Ausgangsspannung, Tasten **▲/▼** für die Parameter, Taste **FUNC** zur Auswahl, Taste **ON/OFF** zum Ein-/Ausschalten und zur Tastensperre).

**Standardmäßig erzeugt die Steuerung beim Einschalten keinen Ausgang** und bleibt im Stoppzustand: Um den Hauptausgang freizugeben, muss ein **PNP-Signal** an den **Enable Output Port** (4-poliger Steckverbinder) angelegt werden.

Die Steuerung verfügt über automatische Schutzfunktionen:

- **Kurzschluss** → sofortige Abschaltung des Ausgangs, Fehler `Err01`
- **Überstrom** → sofortige Abschaltung des Ausgangs, Fehler `Err02`
- **Übertemperatur** → Abschaltung des Ausgangs über 65 °C, automatische Rückstellung unter 60 °C, Fehler `Err03`

Die Kommunikation erfolgt über den Port **RS485** (Protokoll **Modbus**) mit einer von 1 bis 31 einstellbaren Netzwerkadresse und konfigurierbarer Baudrate.


### Technische Daten der Steuerung

| Technisches Merkmal | Min | Typisch | Max | Einheit | Hinweise |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Eingangsspannung** | 85 | 220 | 250 | V | AC RMS |
| **Einstellbarer Ausgangsspannungsbereich** | 0 | — | 260 | V | Weniger als 150 % der Eingangsspannung |
| **Genauigkeit der Spannungsregelung** | — | 1 | — | V | — |
| **Genauigkeit der Spannungsregelung (ΔVout/ΔVin)** | 0 | — | 10 | % | ΔVout/ΔVin |
| **Einstellbarer Ausgangsstrombereich** | 0 | — | 6 | A | — |
| **Ausgangsleistung** | 0 | — | 1320 | VA | — |
| **Ausgangsfrequenz** | 30,0 | — | 130,0 | Hz | — |
| **Genauigkeit der Frequenzregelung** | — | 0,1 | — | Hz | — |
| **Ausgangskurvenform** | — | Sinusförmig | — | — | — |
| **Auslösetemperatur des Übertemperaturschutzes** | 60 | 65 | 65 | °C | — |
| **Digitale Kommunikation** | — | ModBus 485 | — | — | — |
| **Einstellmethode** | — | 6 | — | Tasten | — |
| **Standby-Verbrauch** | — | 7 | — | W | — |
| **Anzeigeart** | — | 5 | — | Ziffernanzeige | LED |
| **Umgebungstemperatur** | 0 | 25 | 40 | °C | Nicht kondensierend |
| **Umgebungsfeuchtigkeit** | 10 | 60 | 85 | % | Nicht kondensierend |
| **Umgebungstemperatur bei Lagerung** | -20 | 25 | 65 | °C | Nicht kondensierend |

:::{attention}
Es können andere als die vom Hersteller gelieferten Steuerungen integriert werden, sofern der Hersteller deren technische Eigenschaften zuvor validiert hat. Die Firma ARS s.r.l. haftet nicht für Schäden, die durch die Verwendung einer nicht validierten oder mit der Maschine nicht kompatiblen Steuerung entstehen.
:::

#### Bedienelemente der Frontplatte

```{image} ../../../../../_shared/media/images/controller_digitale_pannello.jpeg
:alt: Frontplatte der digitalen Steuerung CUH SDVC34-XLRH
:width: 90%
:align: center
```

| Element | Funktion |
|---|---|
| **LED-Display** | Zeigt den aktuellen Parameter und seinen Wert an |
| **Anzeige Saturated** | Signalisiert die Sättigung des Ausgangssignals |
| **Anzeige Remote** | Signalisiert, dass die Fernsteuerung aktiv ist |
| **Anzeigen Speed A / Speed B** | Signalisieren die aktive Geschwindigkeit/den aktiven Ausgang |
| **Anzeige Stop** | Signalisiert den Stoppzustand |
| **Tasten Vol+ / Vol-** | Stellen jederzeit die **allgemeinen Parameter** ein (siehe unten) |
| **Taste FUNC** | Aufrufen/Verlassen und Navigation durch die **Basisparameter** |
| **Tasten ▲ / ▼** | Erhöhen/verringern den Wert des ausgewählten Parameters |
| **Anzeigen Auto / Sync / Sensor / Sync Signal / Communicate** | Betriebs- und RS485-Kommunikationsstatus |
| **Taste ON/OFF** | Schaltet die Steuerung ein/aus |

#### Anschlüsse auf der Rückseite

```{image} ../../../../../_shared/media/images/controller_digitale_connettori.png
:alt: Rückseitiges Anschlussfeld der digitalen Steuerung
:width: 85%
:align: center
```

```{list-table}
:widths: 30 45 25
:header-rows: 1

* - Stecker
  - Funktion
  - Pinout
* - **Mains Power** (Stromversorgung)
  - Netzversorgung
  - <details class="ars-dropdown"><summary>Pinbelegung des Steckverbinders</summary><div class="ars-dropdown-body">

    | Pin | Beschreibung |
    |---|---|
    | PE-PE | ⏚ Erde |
    | 1 | L |
    | 2 | N |
    | 3 | NC |

    </div></details>
* - **Enable Output Port** (4-polig)
  - Freigabeausgang für die externe Ansteuerung des Bulk Feeders, der verwendet wird, wenn dieser separat erworben wurde und von einem externen Gerät angesteuert werden muss. Kabel als Option erhältlich: {ref}`cavo-input`.
  - <details class="ars-dropdown"><summary>Pinbelegung des 4-poligen Steckverbinders</summary><div class="ars-dropdown-body">

    | Pin | Beschreibung |
    |---|---|
    | 1 | +24V |
    | 2 | NC |
    | 3 | GND |
    | 4 | Eingang |

    </div></details>
* - **RS485 Port** (2× 5-polig)
  - Zwei identische RS485-Steckverbinder: Einer verbindet die Steuerung mit dem FlexiBowl®, der andere ermöglicht die **Daisy-Chain**-Verbindung mehrerer Bulk Feeder. Kabel als Option erhältlich: {ref}`cavo-modbus`.
    
    :::{important}
    Bei einer Konfiguration mit einem einzelnen Bulk Feeder muss der nicht verwendete Steckverbinder mit dem mitgelieferten **Abschlussstecker** verschlossen werden, der einen **120-Ω**-Widerstand zwischen A+ und B- besitzt
    :::
  
  - <details class="ars-dropdown"><summary>Pinbelegung des 5-poligen Steckverbinders</summary><div class="ars-dropdown-body">

    | Pin | Beschreibung |
    |---|---|
    | 1 | A+ |
    | 2 | NC |
    | 3 | B- |
    | 4 | GND |
    | 5 | NC |

    </div></details>
* - **Power Output to Feeder** (Ausgang zum Bulk Feeder)
  - Versorgung des Bulk Feeders
  - <details class="ars-dropdown"><summary>Pinbelegung des Steckverbinders</summary><div class="ars-dropdown-body">

    | Pin | Beschreibung |
    |---|---|
    | PE-PE | ⏚ Erde |
    | 1 | Ausgang |
    | 2 | Ausgang |
    | 3 | NC |

    </div></details>
* - **Power Switch**
  - Ein-/Ausschalter
  - —
```

## Bedienverfahren

### Vorabprüfungen

Vor der Inbetriebnahme der Maschine sind die folgenden Prüfungen durchzuführen:

<div class="isw-symbol-grid">
  <div class="isw-symbol-item">
    <div>
      <div class="isw-symbol-label">Standsicherheit</div>
      <div class="isw-symbol-desc">Prüfen Sie, dass die Maschine auf einer Fläche steht, die ihr Gewicht tragen kann.</div>
    </div>
  </div>
  <div class="isw-symbol-item">
    <div>
       <div class="isw-symbol-label">Sicherheit</div>
      <div class="isw-symbol-desc">Prüfen Sie die Funktion der Sicherheitseinrichtungen und stellen Sie sicher, dass alle zu öffnenden Schutzeinrichtungen fest geschlossen sind.</div>
    </div>
  </div>
  <div class="isw-symbol-item">
    <div>
      <div class="isw-symbol-label">Arbeitsbereich</div>
      <div class="isw-symbol-desc"> Prüfen Sie, dass der Bereich um die Maschine frei von Hindernissen und/oder Stolperfallen ist.</div>
    </div>
  </div>
  <div class="isw-symbol-item">
    <div>
     <div class="isw-symbol-label">Spannungsversorgung</div>
      <div class="isw-symbol-desc">Prüfen Sie, dass die Maschine an das Stromnetz angeschlossen wurde und die Versorgungsphasen korrekt sind.</div>
    </div>
  </div>
  <div class="isw-symbol-item">
    <div>
       <div class="isw-symbol-label">Mechanik</div>
      <div class="isw-symbol-desc">Prüfen Sie, dass die Wanne vollständig frei schwingen kann.</div>
    </div>
  </div>
  <div class="isw-symbol-item">
    <div>
      <div class="isw-symbol-label">Maschinenstatus</div>
      <div class="isw-symbol-desc">Prüfen Sie, dass sich die Maschine nicht im Zustand „Wartung“ befindet.</div>
    </div>
  </div>
</div>

### Reihenfolge der elektrischen Anschlüsse

Unabhängig vom verwendeten Steuerungstyp (Standard, analog oder digital) folgt der elektrische Anschluss zwischen Bulk Feeder, Steuerung und FlexiBowl® einer genauen Reihenfolge. Die Reihenfolge unterscheidet sich je nach Modell leicht: Die **FlexiBowl® 500/650/800/1200** verfügen über ein Standard-Schaltfeld mit integriertem HOPPER-Steckverbinder, während die **FlexiBowl® 200/350** ein externes Rack mit eigenem HOPPER-Steckverbinder verwenden.

#### FlexiBowl® 500 / 650 / 800 / 1200 — Standard-Schaltfeld

<div style="display: flex; flex-direction: column; gap: 12px; margin: 20px 0;">
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #0f766e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">1</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Verbinden Sie die <strong>Steuerung</strong> mit dem <strong>Bulk Feeder</strong> (Vibrationssockel).
    </div>
    <img src="../../../../../_shared/media/images/connect_Hopper.png" alt="Anschluss des Hopper Controllers an den Bulk Feeder" style="display:block; width:100%; max-width:500px; margin-top:10px; border-radius:4px;" />
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #0f766e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">2</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Verbinden Sie die <strong>Steuerung</strong> mit dem Steckverbinder <strong>HOPPER</strong> am Standard-Schaltfeld des FlexiBowl®.
    </div>
    <img src="../../../../../_shared/media/images/connect_FB.png" alt="Anschluss des Hopper Controllers an den Bulk Feeder" style="display:block; width:100%; max-width:500px; margin-top:10px; border-radius:4px;" />
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #0f766e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">3</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Wenn der Hopper-Steckverbinder des FlexiBowl® nicht verwendet wird, setzen Sie die vorgesehene <strong>Abschlusskappe</strong>* auf.
    </div>
    <img src="../../../../../_shared/media/images/cover_cap.png" alt="Anschluss des Hopper Controllers an den Bulk Feeder" style="display:block; width:100%; max-width:500px; margin-top:10px; border-radius:4px;" />
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #0f766e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">4</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Schließen Sie das <strong>Netz</strong>kabel an die Steuerung an und stellen Sie sicher, dass der Netzschalter in Stellung <strong>OFF</strong> steht.
    </div>
    <img src="../../../../../_shared/media/images/connect_Supply.png" alt="Anschluss des Hopper Controllers an den Bulk Feeder" style="display:block; width:100%; max-width:500px; margin-top:10px; border-radius:4px;" />
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #0f766e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">5</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Stecken Sie den Stecker des Netzkabels erst in die <strong>Steckdose</strong>, nachdem Sie bestätigt haben, dass der Schalter der Steuerung auf OFF steht.
    </div>
  </div>
</div>

:::{attention}
*Die Kappe muss zwischen den Kanälen A+ und B- einen Widerstand von **120 Ω** gewährleisten.
:::

:::{important}
Schließen Sie immer **zuerst das Ende des Netzkabels auf der Steuerungsseite** an und stecken Sie den Stecker erst danach in die Steckdose.
:::

```{image} ../../../../../_shared/media/images/controller_side.png
:alt: Schließen Sie immer zuerst das Ende auf der Steuerungsseite an
:width: 70%
:align: center
```

```{image} ../../../../../_shared/media/images/power_outlet.png
:alt: Einstecken in die Steckdose
:width: 70%
:align: center
```

#### **Kaskadenverbindung mehrerer Bulk Feeder**

Bei Modellen mit Standard-Schaltfeld können mehrere Hopper-Controller-Einheiten in Kaskade verbunden werden; jede Steuerung wird einzeln versorgt, und die Steckverbinder werden von einer Einheit zur nächsten verbunden.

```{image} ../../../../../_shared/media/images/daisy_chain.png
:alt: Kaskadenverbindung mehrerer Hopper Controller
:width: 100%
:align: center
```

#### FlexiBowl® 200 / 350 — Rack-Schaltfeld

<div style="display: flex; flex-direction: column; gap: 12px; margin: 20px 0;">
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #0f766e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">1</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Verbinden Sie die <strong>Steuerung</strong> mit dem <strong>Bulk Feeder</strong> (Vibrationssockel).
    </div>
    <img src="../../../../../_shared/media/images/connect_Hopper.png" alt="Anschluss des Hopper Controllers an den Bulk Feeder" style="display:block; width:100%; max-width:500px; margin-top:10px; border-radius:4px;" />
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #0f766e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">2</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Verbinden Sie die <strong>Steuerung</strong> mit dem Steckverbinder <strong>HOPPER</strong> am Schaltfeld des <strong>Racks</strong>.
    </div>
    <img src="../../../../../_shared/media/images/controller_Rack.png" alt="Anschluss des Hopper Controllers an den Bulk Feeder" style="display:block; width:100%; max-width:500px; margin-top:10px; border-radius:4px;" />
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #0f766e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">3</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Wenn der Hopper-Steckverbinder des Racks nicht verwendet wird, setzen Sie die vorgesehene <strong>Abschlusskappe</strong>* auf.
    </div>
    <img src="../../../../../_shared/media/images/cover_cap.png" alt="Anschluss des Hopper Controllers an den Bulk Feeder" style="display:block; width:100%; max-width:500px; margin-top:10px; border-radius:4px;" />
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #0f766e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">4</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Schließen Sie das <strong>Netz</strong>kabel an die Steuerung an und stellen Sie sicher, dass der Netzschalter in Stellung <strong>OFF</strong> steht.
    </div>
    <img src="../../../../../_shared/media/images/connect_Supply.png" alt="Anschluss des Hopper Controllers an den Bulk Feeder" style="display:block; width:100%; max-width:500px; margin-top:10px; border-radius:4px;" />
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #0f766e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">5</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Stecken Sie den Stecker des Netzkabels erst in die <strong>Steckdose</strong>, nachdem Sie bestätigt haben, dass der Schalter der Steuerung auf OFF steht.
    </div>
  </div>
</div>

:::{attention}
*Die Kappe muss zwischen den Kanälen A+ und B- einen Widerstand von **120 Ω** gewährleisten.
:::

:::{important}
Schließen Sie immer **zuerst das Ende des Netzkabels auf der Steuerungsseite** an und stecken Sie den Stecker erst danach in die Steckdose.
:::

```{image} ../../../../../_shared/media/images/controller_side.png
:alt: Schließen Sie immer zuerst das Ende auf der Steuerungsseite an
:width: 70%
:align: center
```

```{image} ../../../../../_shared/media/images/power_outlet.png
:alt: Einstecken in die Steckdose
:width: 70%
:align: center
```

:::{note}
Standardversorgung der Steuerung: **115 V AC** oder **230 V AC ±5 %**. Prüfen Sie stets, dass der Schutzleiter korrekt installiert und unversehrt ist, bevor Sie das System einschalten.
:::

---

#### Einstellen der Kommunikationsadresse

Nach Abschluss der elektrischen Verdrahtung besteht der nächste Schritt darin, an jeder Steuerung über den Parameter **Communication Address** (`r`) eine **eindeutige Kommunikationsadresse** einzustellen.

:::{note}
Der Parameter `r` stellt die **Steuerungs-ID** im **RS485**-Kommunikationsnetzwerk dar. Wenn mehrere Steuerungen am selben Netzwerk angeschlossen sind (z. B. mehrere Bulk Feeder), ist es **zwingend erforderlich**, jeder eine andere Adresse im Bereich **1–31** zuzuweisen, damit sie unterschieden und einzeln gesteuert werden können.
:::

<div style="display: flex; flex-direction: column; gap: 12px; margin: 20px 0;">
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #7c3aed; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">1</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Halten Sie <strong>FUNC</strong> 2 Sekunden lang gedrückt, um in den Einstellmodus der Basisparameter zu gelangen.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #7c3aed; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">2</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Drücken Sie wiederholt <strong>FUNC</strong>, um bis zum Parameter <code>r</code> zu blättern.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #7c3aed; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">3</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Drücken Sie <strong>▲</strong> oder <strong>▼</strong>, um den Wert zu ändern (1–31).
    </div>
  </div>
</div>

---

#### Hopper-Software-Oberfläche

Sobald jeder Steuerung die eindeutige Adresse zugewiesen wurde, sind die Bulk Feeder **in die FlexiBowl®-Software integriert** und können direkt über deren Oberfläche gesteuert werden, ohne dass die einzelnen Steuerungen manuell bedient werden müssen.

```{image} ../../../../../_shared/media/images/hopper.png
:alt: FlexiBowl-Software-Oberfläche — Verwaltung der Bulk Feeder (Hopper 1–4)
:width: 100%
:align: center
```

Über die Software-Oberfläche ist es für jeden angeschlossenen Bulk Feeder möglich:

| Feld | Funktion |
|---|---|
| **ID** | Kommunikationsadresse der Steuerung (muss mit der manuell eingestellten übereinstimmen) |
| **ENABLE** | Gibt den Bulk Feeder für den Betrieb frei |
| **Set New ID** | Weist per Software eine neue Kommunikationsadresse zu |
| **STATUS** | Aktueller Status des Bulk Feeders (z. B. Disabled) |
| **Amplitude** | Vibrationsamplitude |
| **Frequency** | Vibrationsfrequenz |
| **Activation Time** | Aktivierungszeit des Bulk Feeders (ms) |
| **Start Hopper** | Startet den Bulk Feeder manuell |

:::{note}
Alle über die Software-Oberfläche verfügbaren Einstellungen können auch **direkt an der Steuerung** über die nachstehend beschriebenen allgemeinen Parameter und Basisparameter vorgenommen werden.
:::

---
#### Allgemeine Parameter

Die **allgemeinen Parameter** können jederzeit mit den Tasten **Vol+ / Vol-** eingestellt werden, auch wenn auf dem Display ein anderer Parameter angezeigt wird: Nach Abschluss der Einstellung kehrt die Steuerung automatisch zur Anzeige des vorherigen Parameters zurück.

```{image} ../../../../../_shared/media/images/controller_changing_common_parameters.png
:alt: Digitale Steuerung — Einstellung der allgemeinen Parameter mit Vol+/Vol-
:width: 50%
:align: center
```

| Definition | Symbol | Bereich | Standard |
|---|---|---|---|
| Output Voltage (Ausgangsspannung) | `U` | 0–260 (V) | 50 |

#### Basisparameter

<div style="display: flex; flex-direction: column; gap: 12px; margin: 20px 0;">
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #34495e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">1</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Halten Sie <strong>FUNC</strong> 2 Sekunden lang gedrückt, um in den Einstellmodus der Basisparameter zu gelangen.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #34495e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">2</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Drücken Sie wiederholt <strong>FUNC</strong>, um zyklisch durch die verschiedenen Parameter zu blättern.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #34495e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">3</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Drücken Sie <strong>▲</strong> oder <strong>▼</strong>, um den Wert des Parameters zu ändern.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #34495e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">4</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Halten Sie <strong>FUNC</strong> erneut 2 Sekunden lang gedrückt, um den Einstellmodus der Basisparameter zu verlassen.
      <img src="../../../../../_shared/media/images/controller_changing_basic_parameters.png" alt="Digitale Steuerung — Vorgehensweise zur Einstellung der Basisparameter" style="display:block; width:60%; max-width:500px; margin-top:10px; border-radius:4px;" />
    </div>
  </div>
</div>

| Definition | Symbol | Bereich | Standard |
|---|---|---|---|
| Output Frequency (Ausgangsfrequenz) | `E` | 40,0–200,0 (Hz) | 100,0 |
| Max Adjustable Output Voltage (maximal einstellbare Ausgangsspannung) | `h` | 0–260 (V) | 260 |
| Communication Address (RS485-Adresse) | `r` | 1–31 | 1 |
| Communication Baud Rate (Kommunikationsgeschwindigkeit) | `c` | 0,3–115,2 kbit/s | 115,2 |
| Controller Reset | `88888` | — | — |

#### Vorgehensweise beim Controller Reset

<div style="display: flex; flex-direction: column; gap: 12px; margin: 20px 0;">
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #7c3aed; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">1</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Halten Sie <strong>FUNC</strong> 2 Sekunden lang gedrückt, um in den Einstellmodus der Basisparameter zu gelangen.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #7c3aed; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">2</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Drücken Sie <strong>FUNC</strong>, bis der Parameter <code>88888</code> auf dem Display blinkt.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #7c3aed; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">3</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Halten Sie <strong>▲</strong> gedrückt, bis das Display <code>-----</code> („Ready to restore“) anzeigt.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #7c3aed; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">4</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Lassen Sie <strong>▲</strong> los, um das Zurücksetzen abzuschließen („Restore successfully“): Das Display zeigt <code>U 50</code> als Bestätigung der erfolgten Wiederherstellung.
      <img src="../../../../../_shared/media/images/controller_reset_procedure.png" alt="Digitale Steuerung — Reset-Ablauf, von Ready to restore bis Restore successfully" style="display:block; width:100%; max-width:700px; margin-top:10px; border-radius:4px;" />
    </div>
  </div>
</div>

:::{warning}
Der **Controller Reset** setzt alle allgemeinen Parameter und Basisparameter auf ihre Standardwerte zurück (Output Voltage 50, Output Frequency 100,0 Hz, Max Output Voltage 260, Communication Address 1, Baud Rate 115,2 kbit/s). Verwenden Sie ihn mit Vorsicht, wenn individuelle Konfigurationen vorhanden sind – insbesondere die Kommunikationsadresse, die neu eingestellt werden muss.
:::


---

## **Inbetriebnahme des Bulk Feeders**

:::{important}
- Wenn das System **FlexiVision One** enthält, wird die Konfiguration der Bulk-Feeder-Parameter im Abschnitt [Konfiguration des Bulk Feeders]() angeleitet.
- Andernfalls beachten Sie den Abschnitt [Hopper](hopper) dieses Handbuchs.
:::

