(cavi)=
# [ELE] **Connection Cables**

The FlexiBowl® connection cables can be purchased separately as an option, in lengths of **3, 5 or 10 metres**. This page lists all the cables available in the price list: each length has its own section, reachable through a direct link.

:::{note}
The connection cables for the vibratory hoppers (controller Modbus RTU cable and Input cable) are described on the {ref}`Hopper Accessories and Options <tramoggia-cavi>` page.
:::

:::{warning}
Connect and disconnect the cables only with the device switched off and disconnected from the power supply.
:::

---

(cavo-io)=
## I/O Option Cable

Cable for connecting the signals of the **Digital I/O** option, which allows the FlexiBowl® to be controlled from a PLC through digital inputs and outputs, without Ethernet communication.

:::{list-table}
:widths: 30 70
:stub-columns: 1

* - Compatibility
  - 
* - FlexiBowl® side connector
  - 
* - System side connector
  - 
* - References
  - Signals and command encoding: {ref}`Digital I/O <quickstart>` · I/O connector pinout: {ref}`io-flexitrack`
:::

:::{note}
The **Digital I/O** mode is an option that can be purchased separately and is not included in the standard FlexiBowl® configuration.
:::

<!-- DA COMPLETARE: tipo di connettore, sezione/schermatura, compatibilità per taglia -->

(cavo-io-3m)=
### I/O Option Cable — 3 m

:::{list-table}
:widths: 30 70
:stub-columns: 1

* - Price list item
  - FlexiBowl cable for I/O option, 3m
* - Item code
  - 
* - Length
  - 3 m
:::

(cavo-io-5m)=
### I/O Option Cable — 5 m

:::{list-table}
:widths: 30 70
:stub-columns: 1

* - Price list item
  - FlexiBowl cable for I/O option, 5m
* - Item code
  - 
* - Length
  - 5 m
:::

(cavo-io-10m)=
### I/O Option Cable — 10 m

:::{list-table}
:widths: 30 70
:stub-columns: 1

* - Price list item
  - FlexiBowl cable for I/O option, 10m
* - Item code
  - 
* - Length
  - 10 m
:::

---

(cavo-rack)=
## Remote Electronic Cabinet (Rack) Cable

Connection cables between the external **rack** and the FlexiBowl®, for the **FlexiBowl® 200 / 350** sizes. The rack communicates with the machine through 4 dedicated cables, each of which must be connected only to the port with the matching label:

:::{list-table}
:widths: 30 70
:header-rows: 1

* - Cable
  - Function
* - **C-ETH FB**
  - Ethernet connection between rack and FlexiBowl® (M12 D-code connector)
* - **MOTOR**
  - Motor power supply and STO signals (9-pin connector)
* - **C-A SIGNAL**
  - Analog signals
* - **C-B SIGNAL**
  - Digital signals, including status LED activation
:::

:::{list-table}
:widths: 30 70
:stub-columns: 1

* - Compatibility
  - FlexiBowl® 200 · FlexiBowl® 350
* - Standard supply
  - The 3 m cables are supplied with the FlexiBowl® 200 / 350; the 5 m and 10 m lengths are available as an option.
* - References
  - Pinout and connection procedure: {ref}`collegamento-rack`
:::

:::{attention}
Connect each cable to the port with the **matching label** (e.g. MOTOR ↔ MOTOR, C-A SIGNAL ↔ C-A SIGNAL). A crossed connection can damage the system.
:::

(cavo-rack-3m)=
### Remote Electronic Cabinet Cable — 3 m

:::{list-table}
:widths: 30 70
:stub-columns: 1

* - Price list item
  - Cable for remote electronic cabinet, 3m
* - Item code
  - 
* - Length
  - 3 m
:::

(cavo-rack-5m)=
### Remote Electronic Cabinet Cable — 5 m

:::{list-table}
:widths: 30 70
:stub-columns: 1

* - Price list item
  - Cable for remote electronic cabinet, 5m
* - Item code
  - 
* - Length
  - 5 m
:::

(cavo-rack-10m)=
### Remote Electronic Cabinet Cable — 10 m

:::{list-table}
:widths: 30 70
:stub-columns: 1

* - Price list item
  - Cable for remote electronic cabinet, 10m
* - Item code
  - 
* - Length
  - 10 m
:::

---

(cavo-alim)=
## FlexiBowl® Power Supply Cable

Mains power cable, to be connected to the **POWER SUPPLY** connector of the standard electrical panel (FlexiBowl® 500 – 1200) or of the rack (FlexiBowl® 200 / 350).

:::{list-table}
:widths: 30 70
:stub-columns: 1

* - Compatibility
  - All FlexiBowl® sizes
* - Permitted voltage
  - 120–230 Vac, 50/60 Hz
* - References
  - Connection procedure: {ref}`pannello-standard` · {ref}`rack-esterno` · Power supply data: {ref}`dati_elettrici`
:::

| Colour | Type | Label |
|---|---|---|
| Brown | Phase | L1 |
| Blue | Neutral | N1 |
| Yellow/Green | Earth | PE1 |

:::{attention}
Connect the power supply **last**, with the FlexiBowl® switched off. The earth connection is mandatory and must be checked before each power-up.
:::

(cavo-alim-3m)=
### Power Supply Cable — 3 m

:::{list-table}
:widths: 30 70
:stub-columns: 1

* - Price list item
  - FlexiBowl Power Supply Cable, 3m
* - Item code
  - 
* - Length
  - 3 m
:::

(cavo-alim-5m)=
### Power Supply Cable — 5 m

:::{list-table}
:widths: 30 70
:stub-columns: 1

* - Price list item
  - FlexiBowl Power Supply Cable, 5m
* - Item code
  - 
* - Length
  - 5 m
:::

(cavo-alim-10m)=
### Power Supply Cable — 10 m

:::{list-table}
:widths: 30 70
:stub-columns: 1

* - Price list item
  - FlexiBowl Power Supply Cable, 10m
* - Item code
  - 
* - Length
  - 10 m
:::

---

(cavo-eth)=
## Ethernet Cable

Cable for the Ethernet connection of the FlexiBowl® to the system (**C-ETH** connector on the standard panel or **C-ETH IN** on the rack). It enables communication with the FlexiBowl®, which can also be accessed via web browser.

:::{list-table}
:widths: 30 70
:stub-columns: 1

* - Compatibility
  - All FlexiBowl® sizes
* - FlexiBowl® side connector
  - M12, D-code
* - System side connector
  - 
* - References
  - M12 → RJ45 pinout: {ref}`pannello-standard` · {ref}`rack-esterno`
:::

:::{important}
When the FlexiBowl® is powered, the Ethernet connection is **mandatory**: if it is missing, the machine enters the **ERROR** state (red Ready/Fault LED).
:::

(cavo-eth-3m)=
### Ethernet Cable — 3 m

:::{list-table}
:widths: 30 70
:stub-columns: 1

* - Price list item
  - Ethernet Cable 3m
* - Item code
  - 
* - Length
  - 3 m
:::

(cavo-eth-5m)=
### Ethernet Cable — 5 m

:::{list-table}
:widths: 30 70
:stub-columns: 1

* - Price list item
  - Ethernet Cable 5m
* - Item code
  - 
* - Length
  - 5 m
:::

(cavo-eth-10m)=
### Ethernet Cable — 10 m

:::{list-table}
:widths: 30 70
:stub-columns: 1

* - Price list item
  - Ethernet Cable 10m
* - Item code
  - 
* - Length
  - 10 m
:::
