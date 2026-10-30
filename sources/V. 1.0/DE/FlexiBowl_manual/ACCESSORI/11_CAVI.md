(cavi)=
# **Anschlusskabel**

Die Anschlusskabel des FlexiBowl® können optional separat erworben werden, in den Längen **3, 5 oder 10 Meter**. Diese Seite fasst die im Katalog verfügbaren Kabel, ihre Voraussetzungen und ihre Steckerbelegungen zusammen.

:::{note}
Die Kabel der Bulk Feeder (Modbus-RTU-Kabel und Input-Kabel des Controllers) sind auf der Seite {ref}`Zubehör und Optionen der Bulk Feeder <tramoggia-cavi>` beschrieben.
:::

:::{warning}
Die Kabel nur bei ausgeschaltetem und von der Stromversorgung getrenntem Gerät anschließen und abziehen.
:::

## Übersicht

:::{list-table}
:widths: 24 32 22 22
:header-rows: 1

* - Kabel
  - Voraussetzungen
  - Kompatible Baugrößen
  - Längen
* - [Kabel für I/O-Option](cavo-io)
  - Option **Digital I/O** (separat erhältlich)
  - Alle Baugrößen
  - · 3
    · 5
    · 10 m
* - [Kabel für externen Schaltschrank (Rack)](cavo-rack)
  - FlexiBowl® mit externem Rack
  - FlexiBowl® 200 · 350
  - · 3 m im Lieferumfang enthalten;
    · 5
    · 10 m
* - [Versorgungskabel](cavo-alim)
  - Keine
  - Alle Baugrößen
  - · 3
    · 5
    · 10 m
* - [Ethernet-Kabel](cavo-eth)
  - Keine
  - Alle Baugrößen
  - · 3
    · 5
    · 10 m
:::

### Katalogartikel

:::{list-table}
:widths: 28 24 24 24
:header-rows: 1

* - Kabel
  - 3 m
  - 5 m
  - 10 m
* - **I/O-Option**
  - FlexiBowl cable for I/O option, 3m
  - FlexiBowl cable for I/O option, 5m
  - FlexiBowl cable for I/O option, 10m
* - **Externer Schaltschrank (Rack)**
  - Cable for remote electronic cabinet, 3m
  - Cable for remote electronic cabinet, 5m
  - Cable for remote electronic cabinet, 10m
* - **Spannungsversorgung**
  - FlexiBowl Power Supply Cable, 3m
  - FlexiBowl Power Supply Cable, 5m
  - FlexiBowl Power Supply Cable, 10m
* - **Ethernet**
  - Ethernet Cable 3m
  - Ethernet Cable 5m
  - Ethernet Cable 10m
:::

---

(cavo-io)=
## Kabel für I/O-Option

**Beschreibung.** Kabel zum Anschluss der Signale der Option **Digital I/O**, die die Steuerung des FlexiBowl® über eine SPS mittels digitaler Ein- und Ausgänge ohne Ethernet-Kommunikation ermöglicht. Signale und Befehlskodierung: [Digital I/O](digIO).

:::{list-table}
:widths: 30 70
:stub-columns: 1

* - Voraussetzungen
  - Option **Digital I/O**, separat erhältlich und nicht in der Standardkonfiguration enthalten.
* - Stecker auf der FlexiBowl®-Seite
  - 19-poliger I/O-Stecker
    :::{dropdown} **Steckerbelegung des I/O-Steckers (19 Pins)**
    | Pin | Signal | Verwendung | 
    |---|---|---|
    | 1 | IN – Bit 1 | Befehlskodierung (Seq. Cmd) | 
    | 2 | IN – Bit 2 | Befehlskodierung (Seq. Cmd) | 
    | 3 | IN – Bit 3 | Befehlskodierung (Seq. Cmd) | 
    | 4 | IN – Bit 4 | Befehlskodierung (Seq. Cmd) | 
    | 5 | IN – Bit 5 | Befehlskodierung (Seq. Cmd) | 
    | 6 | IN – Latch | Befehlsausführung (steigende Flanke) | 
    | 7–8 | NC | Nicht belegt | 
    | 9 | OUT – Ready | Statusausgang | 
    | 10 | OUT – Fault | Statusausgang | 
    | 11 | OUT – Busy | Statusausgang | 
    | 12 | OUT – Hopper_1_IsVibrating | Statusausgang Hopper 1 | 
    | 13 | OUT – Hopper_2_IsVibrating | Statusausgang Hopper 2 | 
    | 14 | OUT – Hopper_3_IsVibrating | Statusausgang Hopper 3 | 
    | 15 | OUT – Hopper_4_IsVibrating | Statusausgang Hopper 4 |
    | 16–19 | NC | Nicht belegt | 
    :::
* - Verfügbare Längen
  - · 3 m
    · 5 m
    · 10 m
:::


---

(cavo-rack)=
## Kabel für externen Elektronikschrank (Rack)

**Beschreibung.** Verbindungskabel zwischen dem externen **Rack** und dem FlexiBowl®. Das Rack kommuniziert mit der Maschine über 4 dedizierte Kabel, die jeweils ausschließlich an den Anschluss mit dem entsprechenden Etikett anzuschließen sind. Anschlussverfahren: {ref}`collegamento-rack`.

:::{list-table}
:widths: 30 70
:stub-columns: 1

* - Voraussetzungen
  - FlexiBowl® mit externem Rack (keine Option erforderlich).
* - Kompatible Baugrößen
  - · FlexiBowl® 200
    · FlexiBowl® 350
* - Verfügbare Längen
  - · 3 m (im Lieferumfang enthalten)
    · 5 m
    · 10 m
:::

:::{attention}
Jedes Kabel mit dem Anschluss mit dem **entsprechenden Etikett** verbinden (z. B. MOTOR ↔ MOTOR, C-A SIGNAL ↔ C-A SIGNAL). Eine vertauschte Verbindung kann das System beschädigen.
:::

:::{list-table}
:header-rows: 1 

* - Kabel
  - Stecker
  - Funktion

* - **C-ETH FB**
  - M12 D-code
    :::{dropdown} **Steckerbelegung C-ETH FB (M12 D-Kodierung)**
    | Signal | Funktion | Farbe | M12-Pin (FlexiBowl®-Seite) | RJ45-Pin (Kundenseite) |
    |---|---|---|---|---|
    | TD+ | Datenübertragung (+) | Gelb | 1 | 1 |
    | TD− | Datenübertragung (−) | Orange | 3 | 2 |
    | RD+ | Datenempfang (+) | Weiß | 2 | 3 |
    | RD− | Datenempfang (−) | Blau | 4 | 6 |
    :::

  - Ethernet-Verbindung zwischen Rack und FlexiBowl®

* - **MOTOR**
  - 9-polig
    :::{dropdown} **Steckerbelegung MOTOR (9 Pins)**

    | Pin | Verwendung | 
    |---|---|
    | 1 | +STO1 – Safe Torque Off | 
    | 2 | +24 Vdc – Hilfsspannungsversorgung | 
    | 3 | +STO2 – Safe Torque Off | 
    | 4 | −24 Vdc – Hilfsspannungsversorgung | 
    | 5 | NC |
    | 6 | +48 Vdc – Motor Power | 
    | 7 | −STO1 – Safe Torque Off | 
    | 8 | −48 Vdc – Motor Power | 
    | 9 | −STO2 – Safe Torque Off | 
    :::
  - Motorversorgung und STO-Signale

* - **C-A SIGNAL**
  - 12-polig
    :::{dropdown} **Steckerbelegung C-A SIGNAL (12 Pins)**

    | Pin | Verwendung |
    |---|---|
    | 1 | Analog Output 1 | 
    | 2 | −24 Vdc | 
    | 3 | Analog Input 1 | 
    | 4 | +24 Vdc | 
    | 5–12 | NC | 
    :::
  - Analoge Signale

* - **C-B SIGNAL**
  - 19-polig
    :::{dropdown} **Steckerbelegung C-B SIGNAL (19 Pins)**
    | Pin | Verwendung | 
    |---|---|
    | 1 | +24 Vdc – Aktivierung der grünen Status-LED | 
    | 2 | −24 Vdc – Gemeinsame Masse der Status-LEDs | 
    | 3 | +24 Vdc – Aktivierung der roten Status-LED | 
    | 4 | +24 Vdc – Aktivierung der Backlight-Status-LED | 
    | 5 | −24 Vdc – Aktivierung der Backlight-Status-LED | 
    | 6 | +24 Vdc – Backlight-Aktivierung |
    | 7 | −24 Vdc – Backlight-Aktivierung | 
    | 8 | +24 Vdc – Flip-Aktivierung | 
    | 9 | −24 Vdc – Flip-Aktivierung | 
    | 10 | +24 Vdc – Blasluft-Aktivierung | 
    | 11 | −24 Vdc – Blasluft-Aktivierung | 
    | 12–19 | NC | 
    :::
  - Digitale Signale, einschließlich der Aktivierung der Status-LEDs
:::


---

(cavo-alim)=
## Versorgungskabel

**Beschreibung.** Netzkabel, das an den Stecker **POWER SUPPLY** des Standard-Schaltschranks (FlexiBowl® 500 – 1200) oder des Racks (FlexiBowl® 200 / 350) anzuschließen ist. Anschlussverfahren: {ref}`pannello-standard` · {ref}`rack-esterno`.

:::{list-table}
:widths: 30 70
:stub-columns: 1

* - Voraussetzungen
  - Keine. Gerät ausgeschaltet, Erdungsanschluss obligatorisch. Der Stecker enthält 2 Schutzsicherungen.
* - Kompatible Baugrößen
  - Alle FlexiBowl®-Baugrößen
* - Zulässige Spannung
  - 120–230 Vac, 50/60 Hz ({ref}`dati_elettrici`)
* - Verfügbare Längen
  - · 3 m
    · 5 m
    · 10 m
:::

| Etikett (FlexiBowl®-Seite) | Typ | Farbe |
|---|---|---|
| L1 | Phase | Braun |
| N1 | Neutralleiter | Blau |
| PE1 | Erde | Gelb/Grün |

:::{attention}
Die Spannungsversorgung **zuletzt** anschließen, wobei der FlexiBowl® ausgeschaltet ist. Der Erdungsanschluss ist obligatorisch und muss vor jedem Einschalten überprüft werden.
:::


---

(cavo-eth)=
## Ethernet-Kabel

**Beschreibung.** Kabel für die Ethernet-Verbindung des FlexiBowl® mit dem System (Stecker **C-ETH** des Standard-Schaltschranks oder **C-ETH IN** des Racks). Es ermöglicht die Kommunikation mit dem FlexiBowl®, auf den auch über einen Webbrowser zugegriffen werden kann.

:::{list-table}
:widths: 30 70
:stub-columns: 1

* - Voraussetzungen
  - Keine. Bei eingeschaltetem FlexiBowl® ist die Ethernet-Verbindung **obligatorisch**: Fehlt sie, wechselt die Maschine in den Zustand **ERROR** (Ready/Fault-LED rot).
* - Kompatible Baugrößen
  - Alle FlexiBowl®-Baugrößen
* - Stecker
  - FlexiBowl®-Seite: M12 D-Kodierung
    :::{dropdown} **Steckerbelegung M12 D-Kodierung und RJ45**
    | Signal | Funktion | Farbe | M12-Pin (FlexiBowl®-Seite) | RJ45-Pin (Kundenseite) |
    |---|---|---|---|---|
    | TD+ | Datenübertragung (+) | Gelb | 1 | 1 |
    | TD− | Datenübertragung (−) | Orange | 3 | 2 |
    | RD+ | Datenempfang (+) | Weiß | 2 | 3 |
    | RD− | Datenempfang (−) | Blau | 4 | 6 |

    Die RJ45-Pins 4, 5, 7 und 8 sind nicht belegt.
    :::
* - Verfügbare Längen
  - · 3 m
    · 5 m
    · 10 m
:::
