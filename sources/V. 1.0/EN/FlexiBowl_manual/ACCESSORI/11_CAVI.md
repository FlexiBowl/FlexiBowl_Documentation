(cavi)=
# **Connection cables**

The FlexiBowl® connection cables can be purchased separately as an option, in lengths of **3, 5 or 10 meters**. This page summarizes the cables available in the catalog, their prerequisites and their pinouts.

:::{note}
The cables for the Bulk Feeders (Modbus RTU cable and controller Input cable) are described on the {ref}`Bulk Feeder Accessories and Options <tramoggia-cavi>` page.
:::

:::{warning}
Connect and disconnect the cables only when the device is switched off and disconnected from the power supply.
:::

## Summary

:::{list-table}
:widths: 24 32 22 22
:header-rows: 1

* - Cable
  - Prerequisites
  - Compatible sizes
  - Lengths
* - [I/O option cable](cavo-io)
  - **Digital I/O** option (purchased separately)
  - All sizes
  - · 3
    · 5
    · 10 m
* - [Cable for remote cabinet (rack)](cavo-rack)
  - FlexiBowl® with external rack
  - FlexiBowl® 200 · 350
  - · 3 m included in the supply;
    · 5
    · 10 m
* - [Power supply cable](cavo-alim)
  - None
  - All sizes
  - · 3
    · 5
    · 10 m
* - [Ethernet cable](cavo-eth)
  - None
  - All sizes
  - · 3
    · 5
    · 10 m
:::

### Catalog items

:::{list-table}
:widths: 28 24 24 24
:header-rows: 1

* - Cable
  - 3 m
  - 5 m
  - 10 m
* - **I/O option**
  - FlexiBowl cable for I/O option, 3m
  - FlexiBowl cable for I/O option, 5m
  - FlexiBowl cable for I/O option, 10m
* - **Remote cabinet (rack)**
  - Cable for remote electronic cabinet, 3m
  - Cable for remote electronic cabinet, 5m
  - Cable for remote electronic cabinet, 10m
* - **Power supply**
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
## I/O option cable

**Description.** Cable for connecting the signals of the **Digital I/O** option, which allows the FlexiBowl® to be controlled from a PLC via digital inputs and outputs, without Ethernet communication. Signals and command coding: [Digital I/O](digIO).

:::{list-table}
:widths: 30 70
:stub-columns: 1

* - Prerequisites
  - **Digital I/O** option, purchased separately and not included in the standard configuration.
* - FlexiBowl® side connector
  - 19-pin I/O connector
    :::{dropdown} **I/O connector pinout (19 pin)**
    | Pin | Signal | Use | 
    |---|---|---|
    | 1 | IN – Bit 1 | Command coding (Seq. Cmd) | 
    | 2 | IN – Bit 2 | Command coding (Seq. Cmd) | 
    | 3 | IN – Bit 3 | Command coding (Seq. Cmd) | 
    | 4 | IN – Bit 4 | Command coding (Seq. Cmd) | 
    | 5 | IN – Bit 5 | Command coding (Seq. Cmd) | 
    | 6 | IN – Latch | Command execution (rising edge) | 
    | 7–8 | NC | Not assigned | 
    | 9 | OUT – Ready | Status output | 
    | 10 | OUT – Fault | Status output | 
    | 11 | OUT – Busy | Status output | 
    | 12 | OUT – Hopper_1_IsVibrating | Hopper 1 status output | 
    | 13 | OUT – Hopper_2_IsVibrating | Hopper 2 status output | 
    | 14 | OUT – Hopper_3_IsVibrating | Hopper 3 status output | 
    | 15 | OUT – Hopper_4_IsVibrating | Hopper 4 status output |
    | 16–19 | NC | Not assigned | 
    :::
* - Available lengths
  - · 3 m
    · 5 m
    · 10 m
:::


---

(cavo-rack)=
## Cable for remote electronic cabinet (rack)

**Description.** Connection cables between the external **rack** and the FlexiBowl®. The rack communicates with the machine through 4 dedicated cables, each to be connected exclusively to the port with the matching label. Connection procedure: {ref}`collegamento-rack`.

:::{list-table}
:widths: 30 70
:stub-columns: 1

* - Prerequisites
  - FlexiBowl® with external rack (no option to purchase).
* - Compatible sizes
  - · FlexiBowl® 200
    · FlexiBowl® 350
* - Available lengths
  - · 3 m (included in the supply)
    · 5 m
    · 10 m
:::

:::{attention}
Connect each cable to the port with the **matching label** (e.g. MOTOR ↔ MOTOR, C-A SIGNAL ↔ C-A SIGNAL). A crossed connection can damage the system.
:::

:::{list-table}
:header-rows: 1 

* - Cable
  - Connector
  - Function

* - **C-ETH FB**
  - M12 D-code
    :::{dropdown} **C-ETH FB pinout (M12 D-code)**
    | Signal | Function | Color | M12 pin (FlexiBowl® side) | RJ45 pin (customer side) |
    |---|---|---|---|---|
    | TD+ | Data transmission (+) | Yellow | 1 | 1 |
    | TD− | Data transmission (−) | Orange | 3 | 2 |
    | RD+ | Data reception (+) | White | 2 | 3 |
    | RD− | Data reception (−) | Blue | 4 | 6 |
    :::

  - Ethernet connection between rack and FlexiBowl®

* - **MOTOR**
  - 9-pin
    :::{dropdown} **MOTOR pinout (9 pin)**

    | Pin | Use | 
    |---|---|
    | 1 | +STO1 – Safe Torque Off | 
    | 2 | +24 Vdc – Auxiliary power supply | 
    | 3 | +STO2 – Safe Torque Off | 
    | 4 | −24 Vdc – Auxiliary power supply | 
    | 5 | NC |
    | 6 | +48 Vdc – Motor Power | 
    | 7 | −STO1 – Safe Torque Off | 
    | 8 | −48 Vdc – Motor Power | 
    | 9 | −STO2 – Safe Torque Off | 
    :::
  - Motor power supply and STO signals

* - **C-A SIGNAL**
  - 12-pin
    :::{dropdown} **C-A SIGNAL pinout (12 pin)**

    | Pin | Use |
    |---|---|
    | 1 | Analog Output 1 | 
    | 2 | −24 Vdc | 
    | 3 | Analog Input 1 | 
    | 4 | +24 Vdc | 
    | 5–12 | NC | 
    :::
  - Analog signals

* - **C-B SIGNAL**
  - 19-pin
    :::{dropdown} **C-B SIGNAL pinout (19 pin)**
    | Pin | Use | 
    |---|---|
    | 1 | +24 Vdc – Green status LED activation | 
    | 2 | −24 Vdc – Status LED common | 
    | 3 | +24 Vdc – Red status LED activation | 
    | 4 | +24 Vdc – Backlight status LED activation | 
    | 5 | −24 Vdc – Backlight status LED activation | 
    | 6 | +24 Vdc – Backlight activation |
    | 7 | −24 Vdc – Backlight activation | 
    | 8 | +24 Vdc – Flip activation | 
    | 9 | −24 Vdc – Flip activation | 
    | 10 | +24 Vdc – Blow activation | 
    | 11 | −24 Vdc – Blow activation | 
    | 12–19 | NC | 
    :::
  - Digital signals, including status LED activations
:::


---

(cavo-alim)=
## Power supply cable

**Description.** Mains power cable, to be connected to the **POWER SUPPLY** connector of the standard electrical panel (FlexiBowl® 500 – 1200) or of the rack (FlexiBowl® 200 / 350). Connection procedure: {ref}`pannello-standard` · {ref}`rack-esterno`.

:::{list-table}
:widths: 30 70
:stub-columns: 1

* - Prerequisites
  - None. Device switched off, earth connection mandatory. The connector houses 2 protection fuses.
* - Compatible sizes
  - All FlexiBowl® sizes
* - Permitted voltage
  - 120–230 Vac, 50/60 Hz ({ref}`dati_elettrici`)
* - Available lengths
  - · 3 m
    · 5 m
    · 10 m
:::

| Label (FlexiBowl® side) | Type | Color |
|---|---|---|
| L1 | Phase | Brown |
| N1 | Neutral | Blue |
| PE1 | Earth | Yellow/Green |

:::{attention}
Connect the power supply **last**, with the FlexiBowl® switched off. The earth connection is mandatory and must be verified before every power-up.
:::


---

(cavo-eth)=
## Ethernet cable

**Description.** Cable for the Ethernet connection of the FlexiBowl® to the system (**C-ETH** connector of the standard panel or **C-ETH IN** of the rack). It enables communication with the FlexiBowl®, which can also be accessed via a web browser.

:::{list-table}
:widths: 30 70
:stub-columns: 1

* - Prerequisites
  - None. With the FlexiBowl® powered, the Ethernet connection is **mandatory**: if it is absent, the machine enters the **ERROR** state (red Ready/Fault LED).
* - Compatible sizes
  - All FlexiBowl® sizes
* - Connectors
  - FlexiBowl® side: M12 D-code
    :::{dropdown} **M12 D-Code and RJ45 pinout**
    | Signal | Function | Color | M12 pin (FlexiBowl® side) | RJ45 pin (customer side) |
    |---|---|---|---|---|
    | TD+ | Data transmission (+) | Yellow | 1 | 1 |
    | TD− | Data transmission (−) | Orange | 3 | 2 |
    | RD+ | Data reception (+) | White | 2 | 3 |
    | RD− | Data reception (−) | Blue | 4 | 6 |

    RJ45 pins 4, 5, 7 and 8 are not assigned.
    :::
* - Available lengths
  - · 3 m
    · 5 m
    · 10 m
:::
