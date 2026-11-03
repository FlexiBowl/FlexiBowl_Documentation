(tramoggia-accessori)=
# **Accessories and Options**

This page collects the variants, accessories and options available in the price list for the vibrating Bulk Feeders, grouped by function. The Bulk Feeders are available in six base models (1.5 l, 3 l, 5 l, 10 l, 20 l and 40 l); the 1.5 l bowl is made of plastic, the others are in INOX stainless steel.

:::{attention}
Unless otherwise indicated, accessories and options **are not available for the 1.5 l Bulk Feeder**. For custom models, refer to the project technical file.
:::

## Summary

| Option | Function | Sizes |
|---|---|---|
| {ref}`Version 110 V <tramoggia-110v>` | Low-voltage power supply (115 Vac) | 3 l · 5 l · 10 l · 20 l · 40 l |
| {ref}`PU coating <tramoggia-pu>` | Polyurethane coating of the bowl | 3 l · 5 l · 10 l · 20 l · 40 l |
| {ref}`Dosing barrier <barriera>` | Adjustment of the flow of components at the outlet | 3 l · 5 l · 10 l · 20 l · 40 l |
| {ref}`Hand guard <hand-guard>` | Safety guard for the hands | 3 l · 5 l · 10 l · 20 l · 40 l |
| {ref}`Front photocell <fotocellula-frontale>` | Presence of components in the front area of the bowl | 3 l · 5 l · 10 l · 20 l · 40 l |
| {ref}`Rear photocell <fotocellula-posteriore>` | Level control of the parts in the bowl | 3 l · 5 l · 10 l · 20 l · 40 l |
| {ref}`Anti-vibration <tramoggia-antivibrazione>` | Isolation of vibrations towards the FlexiBowl® | 3 l · 5 l · 10 l · 20 l · 40 l |
| {ref}`Controller cables <tramoggia-cavi>` | Modbus RTU communication and external command | All (controller) |

---

(tramoggia-varianti)=
## Bulk Feeder variants

(tramoggia-110v)=
### Version 110 V

The standard power supply of the Bulk Feeder is **230 Vac ±5%**. A variant for low-voltage power networks is available, supplied **only on explicit request**. To check the current draw of each size, refer to the technical data.

| | |
|---|---|
| **Power supply** | 115 Vac ±5% |
| **Frequency / Phase** | 50-60 Hz / single-phase |
| **Sizes** | INOX 3 l · 5 l · 10 l · 20 l · 40 l |
| **References** | {doc}`Technical data <descrizione_macchina>` · {doc}`Electrical connection <trasporto_installazione>` |

(tramoggia-pu)=
### Version with polyurethane (PU) coating

This version provides a **polyurethane coating of the INOX stainless steel bowl**, available on request for all sizes except the 1.5 l Bulk Feeder. The coating is a wear item: its condition must be **checked every month**, as indicated in the maintenance plan.

:::{image} ../../../../../_shared/media/images/rivestimento.png
:alt: Polyurethane coating
:width: 240px
:align: center
:::

| | |
|---|---|
| **Sizes** | INOX 3 l · 5 l · 10 l · 20 l · 40 l |
| **Maintenance** | Monthly wear check: see {doc}`manutenzione` |

---

(tramoggia-dosaggio-protezione)=
## Dosing and protection

(barriera)=
### Dosing barrier

The dosing barrier is an **adjustable** doser fitted at the bowl outlet: by adjusting its position, the flow of components leaving the Bulk Feeder is controlled.

:::{image} ../../../../../_shared/media/images/barriera_dosatrice.jpg
:alt: Dosing barrier
:width: 240px
:align: center
:::

| | |
|---|---|
| **Function** | Adjustment of the flow of components at the outlet |
| **Adjustment** | Adjustable |
| **Sizes** | 3 l · 5 l · 10 l · 20 l · 40 l |

(hand-guard)=
### Hand guard (Hand Guard)

Safety guard for the hands, available as an optional accessory. Being a safety device, it must not be removed or bypassed.

:::{image} ../../../../../_shared/media/images/protezione_sicurezza.jpg
:alt: Hand safety guard
:width: 240px
:align: center
:::

| | |
|---|---|
| **Function** | Safety guard for the hands |
| **Sizes** | 3 l · 5 l · 10 l · 20 l · 40 l |

---

(tramoggia-fotocellule)=
## Photocells

The photocells make it possible to monitor the state of the bowl during the feeding process. They are available in two kits, both for all sizes except the 1.5 l Bulk Feeder.

(fotocellula-frontale)=
### Front photocell kit

Checks the **presence of components in the front area** of the vibrating bowl during the feeding process.

:::{image} ../../../../../_shared/media/images/fotocellula_frontale.png
:alt: Front photocell
:width: 240px
:align: center
:::

(fotocellula-posteriore)=
### Rear photocell kit

Monitors the **level of the parts** inside the bowl.

:::{image} ../../../../../_shared/media/images/fotocellula_posteriore.png
:alt: Rear photocell
:width: 240px
:align: center
:::

---

(tramoggia-antivibrazione)=
## Anti-vibration

The Bulk Feeder generates vibrations to move the parts along the bowl. If it is installed on the surface of a machine sensitive to vibrations, insulating and anti-vibration material must be placed between the two surfaces, to prevent the vibrations from being transmitted to the FlexiBowl®. **Anti-vibration elements** and an **anti-vibration kit** are available, for sizes from 3 l to 40 l.

| | |
|---|---|
| **Function** | Isolation of the vibrations of the Bulk Feeder |
| **Sizes** | 3 l · 5 l · 10 l · 20 l · 40 l |
| **References** | Installation: {doc}`trasporto_installazione` |

---

(tramoggia-cavi)=
## Controller cables

:::{note}
The FlexiBowl® connection cables (power, Ethernet, I/O, rack) are described on the {ref}`Connection cables <cavi>` page.
:::

The Bulk Feeder controller uses two cables, both available in lengths of **3 m, 5 m and 10 m**.

(cavo-modbus)=
### Modbus RTU cable

**RS485 (Modbus RTU)** communication cable between the Bulk Feeder controller and the FlexiBowl®. It connects to the **HOPPER** connector of the FlexiBowl® (standard panel for sizes 500 – 1200, rack for sizes 200 / 350) and to one of the two **RS485** ports of the controller; the other RS485 port allows **daisy-chain** connection between several Bulk Feeders.

| Controller pins (RS485) | Description |
|---|---|
| 1 | A+ |
| 2 | NC |
| 3 | B- |
| 4 | GND |
| 5 | NC |

FlexiBowl® side connector: M12, A-code. Pinout and connection sequence: {doc}`controller_cablaggio`.

:::{important}
In a single Bulk Feeder configuration, the unused RS485 connector must be closed with the dedicated **termination plug**, fitted with a **120 Ω** resistor between A+ and B-.
:::

(cavo-input)=
### Input cable

Cable for connecting the **Enable Output Port** (4-pin) of the controller, used for commanding the Bulk Feeder from an external device when it is purchased separately. To enable the controller output, a **PNP signal** must be applied to this port. Pinout and connection sequence: {doc}`controller_cablaggio`.

| Controller pin | Description |
|---|---|
| 1 | +24V |
| 2 | NC |
| 3 | GND |
| 4 | Input |

### Available lengths

| Cable | 3 m | 5 m | 10 m |
|---|:---:|:---:|:---:|
| **Modbus RTU** | ✓ | ✓ | ✓ |
| **Input** | ✓ | ✓ | ✓ |
