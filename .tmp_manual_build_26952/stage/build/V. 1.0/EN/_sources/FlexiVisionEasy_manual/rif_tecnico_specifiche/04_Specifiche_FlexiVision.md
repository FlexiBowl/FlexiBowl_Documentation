(specifiche_tecniche)=
# **Detailed FlexiVision One Specifications**

This section provides the complete technical specifications of the FlexiVision One system, including details about the industrial camera, VisionController, calibration grid, communication interfaces, and hardware configurations.

---

(specifiche_camera)=
## Camera

```{figure} ../../../../_shared/media/images/Camera2.png
:alt: FlexiVision One camera CAM-CIC-5000-20G-1
:align: center
:width: 50%
```

The FlexiVision One system uses high-resolution cameras with Gigabit Ethernet interface to guarantee fast image acquisition and accurate component recognition.

### Electrical specifications

```{list-table}
:header-rows: 1
:widths: 40 60

* - **Feature**
  - **Specification**
* - Model
  - CAM-CIC-5000-20G-1
* - Effective Pixels
  - 5 MP, `2448 × 2048`
* - SNR
  - `>38 dB`
* - Dynamic Range
  - `70 dB`
* - GPIO
  - 6-pin Hirose connector: 1 opto-isolated input, 1 opto-isolated output, 1 configurable I/O without optical isolation
* - Image Format
  - Mono8 / 10 / 10Packed
* - Binning
  - Supported
* - Gain
  - X1 ~ X32
* - Gamma
  - From 0 to 4, LUT supported
* - Exposure Time
  - `34.23 μs ~ 1 s`
* - Trigger Mode
  - Software / Hardware / Free run
* - Image Buffer
  - 256 MB
* - User Settings
  - Supports two sets of user-defined configuration
* - Power Supply
  - PoE or DC through Hirose connector, `12 V` or `24 V`
* - Power Consumption
  - `12V ≈ 3.2 W`
* - Lens Mount
  - C-mount
* - Operating Temperature
  - `-30°C ~ +50°C`
* - Storage Temperature
  - `-30°C ~ +80°C`
* - Certifications
  - CE, UL, FCC, RoHS
* - Resolution
  - `2448 x 2048`
* - Pixel Size
  - `3.45 × 3.45 μm`
* - Sensor
  - IMX264 CMOS Global Shutter
* - Sensor Size
  - `2/3"`
* - Frame Rate
  - `24 fps`
* - Bit Depth
  - `12 bit`
* - Interface
  - GigE, PoE
```

### GPIO connector, Hirose 6-pin

```{figure} ../../../../_shared/media/images/Pin_Cam.png
:alt: Hirose 6-pin GPIO connector
:align: center
:width: 70%

Rear view of the camera with connectors
```

```{list-table}
:header-rows: 1
:widths: 10 20 70

* - **Pin**
  - **Signal**
  - **Description**
* - 1
  - Power
  - `12V` or `24V` DC power input
* - 2
  - Line1
  - Opto-isolated input
* - 3
  - Line2
  - Configurable GPIO, software-controlled, without opto-isolation
* - 4
  - Line0
  - Opto-isolated output
* - 5
  - IO GND
  - Opto-isolated ground
* - 6
  - GND
  - Ground
```

```{warning}
**Mandatory network requirements**

The Gigabit Ethernet interface is mandatory and requires compatible network infrastructure, Gigabit Ethernet switch and Ethernet cables of at least Cat6 or Cat7 with S/STP shielding.

Failure to comply with this requirement completely compromises camera operation. Verify that all network components, cables, switches, and ports, support the GigE standard.
```

### Power supply methods

```{list-table}
:header-rows: 1
:widths: 25 40 35

* - **Method**
  - **Description**
  - **Requirements**
* - **PoE**
  - Power and data over a single Ethernet cable. Consumption `3.2 W @ 12 Vdc`.
  - Requires a compatible PoE injector or PoE switch, `IEEE 802.3af/at`
* - **External Camera Cable Supplied in the Kit**
  - External DC power through 6-pin Hirose connector, `12V or 24V`. Included in the kit.
  - A separate Ethernet cable is still required for data
```

```{tip}
**Which method to choose**

- **PoE**: ideal for clean installations with a single cable, but requires dedicated network hardware
- **External power supply**: the most flexible standard solution, recommended for most applications
```

(cavo)=
### Power Cable

```{figure} ../../../../_shared/media/images/Cavo_Specfiche.png
:alt: Camera power cable specifications
:align: center
:width: 100%

Camera power cable specifications
```

```{list-table}
:widths: 30 70
:header-rows: 1

* - Parameter
  - Value
* - **Description**
  - 10 m I/O cable, HRS6P connector
* - **Compatibility**
  - CIC-series cameras
* - **Length**
  - 10 m, 33 ft
* - **Connector 1**
  - Push/Pull 6P RECP Shell SZ 7 Female
* - **Conductor section**
  - 22 AWG
* - **Cable type**
  - Shielded, 3 twisted pairs, flexible
* - **Cable colors**
  - Pin 1: Brown, Pin 2: Green, Pin 3: Pink, Pin 4: Yellow, Pin 5: Gray, Pin 6: White
* - **Shielding**
  - Shield on all conductors
* - **Compliance**
  - UL/CSA and RoHS
```

### Physical specifications and dimensions

![Camera dimensions](../../../../_shared/media/images/Dimensioni_Cam__ab884007b7.png)

```{list-table}
:header-rows: 1
:widths: 40 60

* - **Feature**
  - **Value**
* - Width × Height, body
  - 29 × 29 mm
* - Depth, body
  - 42.0 mm
* - Total depth, including rear connector
  - 48.9 mm
* - Front protrusion, lens mount
  - 12.60 mm
* - Side mounting hole center distance, M2
  - 20.0 × 23.7 mm
* - Front mounting holes
  - 2× M2, depth 3 mm
* - Side mounting holes
  - 4× M2, depth 3.5 mm + 3× M3, depth 3.5 mm
* - Weight
  - 88 g
```

---

(specifiche_obiettivo)=
## Lens

```{figure} ../../../../_shared/media/images/Ottica_000046.png
:alt: FlexiVision One lens
:align: center
:width: 50%
```

```{dropdown} 35 mm Lens
| Parameter | Reference Magnification | M.O.D. |
|------------|-----------------------------|--------|
| **Lens Type** | CCTV Lens | CCTV Lens |
| **Focus Position** | Reference Magnification | M.O.D. |
| **Magnification** | 0.069 | 0.167 |
| **Focal Length (mm)** | 34.97 | 34.97 |
| **F Number (Fno)** | 2.00 ~ 16.00 | 2.00 ~ 16.00 |
| **Numerical Aperture (NA)** | - | - |
| **Working Distance / Object (mm)** | 500.0 / 507.0 | 200.0 / 207.0 |
| **Object-Image Distance (mm)** | 555.75 | 259.16 |
| **Mechanical Tube Length (mm)** | 36.30 ~ 38.20 | 36.30 ~ 38.20 |
| **Lens Back Focus (mm)** | 14.75 | 18.16 |
| **Depth of Field (mm)** | 35.476 | 6.336 |
| **Resolution @550nm (µm)** | - | - |
| **Main Plane Position Front/Rear (mm)** | 37.60 / -22.61 | 37.60 / -22.61 |
| **Entrance/Exit Pupil Position (mm)** | 25.22 / -41.78 | 25.22 / -41.78 |
| **Entrance/Exit Pupil Diameter (mm)** | 17.03 / 26.36 | 17.03 / 26.36 |
| **Field Angle (°) H × V** | 13.69 × 10.34 | 12.62 × 9.76 |
| **TV Distortion (%)** | -0.088 | -0.142 |
| **Relative Illumination (%)** | 44.95 | 50.20 |
| **Weight (g)** | 50 | 50 |
| **Mount** | C-mount | C-mount |
| **Image Circle (mm)** | φ11 | φ11 |
| **Maximum Compatible Camera** | 2/3" | 2/3" |
```

```{dropdown} 25 mm Lens
| Parameter | Reference Magnification | M.O.D. |
|-----------|:----------------------------:|:------:|
| **Lens Type** | CCTV Lens | CCTV Lens |
| **Focus Position** | Reference Magnification | M.O.D. |
| **Magnification** | 0.049 | 0.152 |
| **Focal Length (mm)** | 25.00 | 25.00 |
| **F Number (Fno)** | 1.60 ~ 16.00 | 1.60 ~ 16.00 |
| **Numerical Aperture (NA)** | - | - |
| **Working Distance / Object (mm)** | 500.0 / 510.0 | 150.0 / 160.0 |
| **Object-Image Distance (mm)** | 553.34 | 205.92 |
| **Mechanical Tube Length (mm)** | 34.60 ~ 38.50 | 34.60 ~ 38.50 |
| **Lens Back Focus (mm)** | 13.75 | 16.33 |
| **Depth of Field @PCoC 0.04 mm (mm)** | 54.223 | 5.835 |
| **Resolution @550nm (µm)** | - | - |
| **Main Plane Position Front/Rear (mm)** | 29.42 / -12.46 | 29.42 / -12.46 |
| **Entrance/Exit Pupil Position (mm)** | 18.48 / -31.94 | 18.48 / -31.94 |
| **Entrance/Exit Pupil Diameter (mm)** | 15.92 / 28.32 | 15.92 / 28.32 |
| **Field Angle (°) H × V** | 19.39 × 14.64 | 18.05 × 13.89 |
| **TV Distortion (%)** | -0.041 | -0.271 |
| **Relative Illumination (%)** | 49.78 | 53.52 |
| **Weight (g)** | 50 | 50 |
| **Mount** | C-mount | C-mount |
| **Image Circle (mm)** | φ11 | φ11 |
| **Maximum Compatible Camera** | 2/3" | 2/3" |
```

```{dropdown} 16 mm Lens
| Parameter | Reference Magnification | M.O.D. |
|-----------|:----------------------------:|:------:|
| **Lens Type** | CCTV Lens | CCTV Lens |
| **Focus Position** | Reference Magnification | M.O.D. |
| **Magnification** | 0.031 | 0.095 |
| **Focal Length (mm)** | 16.16 | 16.16 |
| **F Number (Fno)** | 1.60 ~ 16.00 | 1.60 ~ 16.00 |
| **Numerical Aperture (NA)** | - | - |
| **Working Distance / Object (mm)** | 500.0 / 507.0 | 150.0 / 157.0 |
| **Object-Image Distance (mm)** | 554.26 | 205.30 |
| **Mechanical Tube Length (mm)** | 35.50 ~ 37.00 | 35.50 ~ 37.00 |
| **Lens Back Focus (mm)** | 12.16 | 13.20 |
| **Depth of Field @PCoC 0.04 mm (mm)** | 131.893 | 14.387 |
| **Resolution @550nm (µm)** | - | - |
| **Main Plane Position Front/Rear (mm)** | 28.44 / -4.50 | 28.44 / -4.50 |
| **Entrance/Exit Pupil Position (mm)** | 18.85 / -28.07 | 18.85 / -28.07 |
| **Entrance/Exit Pupil Diameter (mm)** | 10.18 / 25.02 | 10.18 / 25.02 |
| **Field Angle (°) H × V** | 30.37 × 22.92 | 29.62 × 22.39 |
| **TV Distortion (%)** | -0.472 | -0.674 |
| **Relative Illumination (%)** | 32.75 | 36.61 |
| **Weight (g)** | 50 | 50 |
| **Mount** | C-mount | C-mount |
| **Image Circle (mm)** | φ11 | φ11 |
| **Maximum Compatible Camera** | 2/3" | 2/3" |
```

```{dropdown} 12 mm Lens
| Parameter | Reference Magnification | M.O.D. |
|-----------|:----------------------------:|:------:|
| **Lens Type** | CCTV Lens | CCTV Lens |
| **Focus Position** | Reference Magnification | M.O.D. |
| **Magnification** | 0.023 | 0.075 |
| **Focal Length (mm)** | 12.00 | 12.00 |
| **F Number (Fno)** | 1.80 ~ 16.00 | 1.80 ~ 16.00 |
| **Numerical Aperture (NA)** | - | - |
| **Working Distance / Object (mm)** | 500.0 / 505.6 | 150.0 / 155.0 |
| **Object-Image Distance (mm)** | 559.55 | 209.55 |
| **Mechanical Tube Length (mm)** | 39.20 ~ 40.10 | 39.20 ~ 40.10 |
| **Lens Back Focus (mm)** | 12.23 | 12.84 |
| **Depth of Field @PCoC 0.04 mm (mm)** | 277.576 | 28.121 |
| **Resolution @550nm (µm)** | - | - |
| **Main Plane Position Front/Rear (mm)** | 17.71 / -0.05 | 17.71 / -0.05 |
| **Entrance/Exit Pupil Position (mm)** | 11.68 / -12.18 | 11.68 / -12.18 |
| **Entrance/Exit Pupil Diameter (mm)** | 6.67 / 13.41 | 6.67 / 13.41 |
| **Field Angle (°) H × V** | 40.54 × 30.77 | 39.40 × 30.05 |
| **TV Distortion (%)** | -0.983 | -0.905 |
| **Relative Illumination (%)** | 40.64 | 42.64 |
| **Weight (g)** | 60 | 60 |
| **Mount** | C-mount | C-mount |
| **Image Circle (mm)** | φ11 | φ11 |
| **Maximum Compatible Camera** | 2/3" | 2/3" |
```

---

(specifiche_VC)=
## VisionController

```{figure} ../../../../_shared/media/images/PC.png
:alt: FlexiVision One VisionController
:align: center
:width: 50%
```

The FlexiVision One system operates on an industrial PC, the VisionController, which acts as the main controller for the vision software. ARS supplies the VisionController already preconfigured and tested with FlexiVision One installed.

### Electrical specifications

```{list-table}
:header-rows: 1
:widths: 40 60

* - **Feature**
  - **Specification**
* - CPU
  - Intel Core i3-1115G4 `1.7 (4.1) GHz`
* - Memory, RAM
  - 8G DDR4 3200 MHz
* - Storage
  - 256G
* - TPM
  - TPM 2.0
* - Operating System
  - Win11 LTSC 2024
* - Power Button
  - Yes, front panel with indicator light
* - Ethernet Ports
  - **i3/i7:** 3× Gb LAN
* - USB Ports
  - 6× USB 3.0 Type A
* - Video Output
  - 2× HDMI
* - Audio
  - Line Out + MIC, 2-in-1 jack
* - Power Supply, V DC
  - 12 ~ 32 V DC
* - Operating Temperature
  - `1°C ~ +50°C`
* - Storage Temperature
  - `-20°C ~ +65°C`
* - Humidity
  - `<90%`, non-condensing
* - Enclosure Material
  - Aluminum alloy + steel
* - Protection Rating
  - IP20
* - Installation Method
  - Wall mounting, optional DIN rail
* - Power Consumption
  - 25 W
* - Dimensions, W × H × D
  - 59.8 × 200 × 119.5 mm
* - Weight
  - 2 kg
* - Certifications
  - CE, UL
```

### PC ports

```{figure} ../../../../_shared/media/images/Spec_Elettriche_PC.png
:alt: VisionController electrical layout
:align: center
:width: 50%
```

```{list-table}
:header-rows: 1
:widths: 10 25 65

* - **Ref.**
  - **Connector**
  - **Description**
* - A
  - Power button
  - Device power on and off
* - B
  - ETH 10/100/1000 Mbit - RJ45, LAN 1
  - Gigabit Ethernet Port 1
* - C
  - ETH 10/100/1000 Mbit - RJ45, LAN 2
  - Gigabit Ethernet Port 2
* - D
  - Serial Port, RS232, COM1
  - RS232 serial interface COM1
* - E
  - Serial Port, RS232, COM2
  - RS232 serial interface COM2
* - F
  - Power input connector
  - `12-32V DC` power input, 3-pin terminal block
* - G
  - Audio Out + MIC, 3.5 mm jack
  - 1× line audio output + microphone input, 3.5 mm jack
* - H
  - 6× USB-A
  - USB ports, USB 3.0 Type A for i3/i7 versions
* - I
  - Video Port 2
  - **B2B12/B2B14:** HDMI 2 - **B2B15/B2B16:** DisplayPort
* - L
  - HDMI Port 1
  - HDMI video output 1
* - M
  - ETH 10/100/1000 Mbit - RJ45, LAN 3
  - Gigabit Ethernet Port 3
```

### Physical specifications

```{figure} ../../../../_shared/media/images/dimensioni_VC.png
:alt: VisionController dimensions
:align: center
:width: 80%
```

```{list-table}
:header-rows: 1
:widths: 40 60

* - **Screw holes**
  - M5
* - **Feature**
  - **Value**
* - Width, overall with brackets
  - 245.00 mm
* - Width, body
  - 227.00 mm
* - Connector panel width
  - 200.00 mm
* - Height, overall with brackets
  - 123.00 mm
* - Height, body
  - 120.00 mm
* - Depth
  - 61.10 mm
```

---

(laser)=
## Laser Tool for Calibration

The Laser Tool is an advanced calibration solution that improves the precision with which the robot reference point is saved.
Its main advantage is that it does not require physical contact with the calibration grid. By working as a high-precision pointer, the laser allows the operator to align the target point visually and repeatably on the grid, offering much greater accuracy than a physical tip tool.
This precision is essential for successful calibration and fits perfectly with the repeatability guaranteed by the ARS dedicated calibration grid.

![Laser Calibration Tool](../../../../_shared/media/images/laser.png)

| Feature | Laser Tool | Standard Tip Tool |
|--|--|--|
| Reference Method | Non-contact, visual pointer | Contact, physical mechanical tip |
| Reference Precision | Maximum precision, the operator aligns the point visually with high accuracy | Medium, dependent on operator visibility |
| Ease of Use | Simplifies the visual alignment procedure | Requires more attention in positioning and avoiding tilt |
| Key Advantage | Makes it possible to save the robot reference point with the highest possible fidelity, essential for final picking accuracy | Basic method, but less precise than the laser |

```{image} ../../../../_shared/media/images/laserscomp.png
:width: 1px
:class: hidden
```
```{raw} html
<div style="display: flex; align-items: flex-start; gap: 2rem;">
  <img src="../../_images/laserscomp.png" style="width: 280px; flex-shrink: 0;" />
  <table style="border-collapse: collapse; font-size: 0.95em; align-self: center;">
    <thead>
      <tr style="background: #d0d0d0;">
        <th style="padding: 6px 16px; text-align: left;">POS.</th>
        <th style="padding: 6px 16px; text-align: left;">DESCRIPTION</th>
      </tr>
    </thead>
    <tbody>
      <tr><td style="padding: 5px 16px;">1</td><td style="padding: 5px 16px;">UPPER CLOSING CAP</td></tr>
      <tr><td style="padding: 5px 16px;">2</td><td style="padding: 5px 16px;">CR2032 3V COIN BATTERY HOLDER</td></tr>
      <tr><td style="padding: 5px 16px;">3</td><td style="padding: 5px 16px;">COUPLING FLANGE</td></tr>
      <tr><td style="padding: 5px 16px;">4</td><td style="padding: 5px 16px;">CLAMP</td></tr>
      <tr><td style="padding: 5px 16px;">5</td><td style="padding: 5px 16px;">TOOL BODY</td></tr>
      <tr><td style="padding: 5px 16px;">6</td><td style="padding: 5px 16px;">LASER POINTER</td></tr>
      <tr><td style="padding: 5px 16px;">7</td><td style="padding: 5px 16px;">SPRING DAMPER</td></tr>
      <tr><td style="padding: 5px 16px;">8</td><td style="padding: 5px 16px;">SPACER SUPPORT</td></tr>
    </tbody>
  </table>
</div>
```

:::{important}
To replace the two batteries of the laser tool, follow the dedicated maintenance procedure.
:::

:::{admonition} Recommendation
:class: tip
Using the Laser Tool together with the ARS dedicated calibration grid is the most robust and precise method for FlexiVision One system installation.
:::

---

(specifiche_griglia)=
## Calibration Grid

```{figure} ../../../../_shared/media/images/Calib_Grid.png
:alt: Calibration Grid
:align: center
:width: 50%
```

Excellent calibration is the fundamental requirement for FlexiVision One system accuracy. Only high-precision calibration guarantees that the coordinates detected by the camera, in pixels, are converted accurately into real robot coordinates, in millimeters, ensuring success of the picking application.

### Calibration grid technical specifications

```{dropdown} Grid for FlexiBowl 200
![Grid 200](../../../../_shared/media/images/griglia200.JPG)
```

```{dropdown} Grid for FlexiBowl 350
![Grid 350](../../../../_shared/media/images/griglia350.JPG)
```

```{dropdown} Grid for FlexiBowl 500
![Grid 500](../../../../_shared/media/images/griglia500.JPG)
```

```{dropdown} Grid for FlexiBowl 650
![Grid 650](../../../../_shared/media/images/griglia650.JPG)
```

```{dropdown} Grid for FlexiBowl 800
![Grid 800](../../../../_shared/media/images/griglia800.JPG)
```

```{dropdown} Grid for FlexiBowl 1200
![Grid 1200](../../../../_shared/media/images/griglia1200.JPG)
```

For detailed calibration procedures, refer to [Camera Calibration](../QUICKSTART/SETUP/14_calibrazione_camera.md).

---

## Connection overview

![Connection overview](../../../../_shared/media/images/panoramicacollegamenti.png)

*Complete connection diagram of the FlexiVision One system with robot and FlexiBowl*

```{list-table}
:widths: 25 25 50
:header-rows: 1

* - **From**
  - **To**
  - **Connection**
* - Power mains
  - FlexiBowl
  - `110/230 Vac` power supply
* - Power mains
  - Robot
  - Power supply according to the specifications of your robot
* - Power mains
  - Camera
  - `24 Vdc` power supply
* - Power mains
  - Illuminator, light
  - `24 Vdc` power supply
* - Power mains
  - Hopper Controller
  - `110/230 Vac` power supply
* - Hopper Controller
  - Hopper
  - Power and signal
* - Robot
  - Hopper Controller
  - Digital I/O
* - VisionController
  - Camera
  - Ethernet TCP
* - VisionController
  - FlexiBowl
  - Ethernet TCP
* - VisionController
  - Robot
  - Ethernet TCP
```

For detailed electrical diagrams, refer to [Wiring and Connections](cablaggio).

---

## Optional components

Additional components available separately:

:::{card} TopLight
:link: toplight
:link-type: ref
:class-card: shadow
:::

:::{card} TopLight Power Cable
:link: cavoalimtoplight
:link-type: ref
:class-card: shadow
:::

:::{card} Backlight
:link: backlight
:link-type: ref
:class-card: shadow
:::

:::{card} Switch
:link: switch
:link-type: ref
:class-card: shadow
:::

:::{card} Display
:link: display
:link-type: ref
:class-card: shadow
:::



<br>

<!-- Versions and languages set-up -->
<style>
  .fixed-bar {
    position: fixed;
    bottom: 10px;
    right: 10px;
    background: rgba(240, 240, 240, 0.85);
    border: 1px solid rgba(100, 100, 100, 0.3);
    border-radius: 6px;
    box-shadow: 0 1px 6px rgba(0, 0, 0, 0.1);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 0.9rem;
    color: #222;
    display: flex;
    gap: 12px;
    padding: 6px 12px;
    align-items: center;
    z-index: 9999;
    backdrop-filter: saturate(180%) blur(10px);
  }

  @media print {
    .fixed-bar {
      display: none !important;
    }
  }

  .fixed-bar .dropdown {
    position: relative;
    user-select: none;
  }

  .fixed-bar .dropdown-toggle {
    background-color: rgba(200, 200, 200, 0.4);
    color: #222;
    padding: 6px 10px;
    border: 1px solid rgba(100, 100, 100, 0.3);
    border-radius: 4px;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 6px;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
    white-space: nowrap;
    transition: background-color 0.3s ease;
  }

  .fixed-bar .dropdown-toggle::after {
    content: none !important;
    display: none !important;
  }

  .fixed-bar .dropdown-toggle:hover {
    background-color: rgba(100, 150, 220, 0.2);
    color: #1a3e72;
    border-color: rgba(26, 62, 114, 0.6);
  }

  .fixed-bar .dropdown-toggle .fa {
    font-size: 0.9rem;
  }

  .fixed-bar .dropdown-menu {
    position: absolute;
    bottom: 100%;
    left: 0;
    background-color: rgba(250, 250, 250, 0.95);
    border: 1px solid rgba(150, 150, 150, 0.3);
    border-radius: 4px;
    box-shadow: 0 3px 8px rgba(0, 0, 0, 0.1);
    min-width: 140px;
    max-height: 200px;
    overflow-y: auto;
    display: none;
    flex-direction: column;
    z-index: 10000;
    backdrop-filter: saturate(180%) blur(8px);
  }

  .fixed-bar .dropdown-menu.show {
    display: flex;
  }

  .fixed-bar .dropdown-menu a {
    padding: 8px 12px;
    color: #1a3e72;
    text-decoration: none;
    border-bottom: 1px solid rgba(200, 200, 200, 0.5);
    white-space: nowrap;
    transition: background-color 0.25s ease;
  }

  .fixed-bar .dropdown-menu a:last-child {
    border-bottom: none;
  }

  .fixed-bar .dropdown-menu a:hover {
    background-color: rgba(100, 150, 220, 0.15);
  }

  .dropdown-download-buttons .btn__icon-container svg {
    width: 1em;
    height: 1em;
    stroke: currentColor;
    fill: none;
    stroke-width: 1.6;
    stroke-linecap: round;
    stroke-linejoin: round;
    vertical-align: middle;
  }

  a.headerlink.manual-heading-action {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    margin-left: 0.2em;
    text-decoration: none;
    color: #7b8493;
    transition: color 0.2s ease, opacity 0.2s ease;
  }

  a.headerlink.manual-heading-action svg {
    width: 0.8em;
    height: 0.8em;
    stroke: currentColor;
    fill: none;
    stroke-width: 1.6;
    stroke-linecap: round;
    stroke-linejoin: round;
    vertical-align: middle;
  }

  a.headerlink.manual-feedback-link:hover,
  a.headerlink.manual-feedback-link:focus-visible {
    color: #2563eb;
  }

  a.headerlink.manual-service-link:hover,
  a.headerlink.manual-service-link:focus-visible {
    color: #d97706;
  }
</style>

<div class="fixed-bar" role="region" aria-label="Version and language selector">
  <div class="dropdown" data-selector="version">
    <div class="dropdown-toggle" tabindex="0" aria-haspopup="listbox" aria-expanded="false">
      Version: <span class="current-value">V. 1.0</span>
      <span class="caret-icon" aria-hidden="true">&#9662;</span>
    </div>
    <div class="dropdown-menu" role="listbox">
      	<a href="#" role="option">V. 1.0</a>
    </div>
  </div>

  <div class="dropdown" data-selector="language">
    <div class="dropdown-toggle" tabindex="0" aria-haspopup="listbox" aria-expanded="false">
      Language: <span class="current-value">EN</span>
      <span class="caret-icon" aria-hidden="true">&#9662;</span>
    </div>
    <div class="dropdown-menu" role="listbox">
      	<a href="#" role="option">DE</a>
				<a href="#" role="option">EN</a>
				<a href="#" role="option">ES</a>
				<a href="#" role="option">FR</a>
				<a href="#" role="option">IT</a>
    </div>
  </div>
</div>

<script>
  (function () {
    const bar = document.querySelector('.fixed-bar');
    if (!bar) {
      return;
    }

    const inlineVersions = ["V. 1.0"];
    const inlineLanguages = ["DE", "EN", "ES", "FR", "IT"];
    const manifest = window.FV_VERSIONING || null;
    const versions = Array.isArray(manifest && manifest.versions) && manifest.versions.length
      ? manifest.versions
      : inlineVersions;
    const offlineZipEnabled = false;
    const offlineZipFileName = 'Offline manual.zip';
    const americanRegions = new Set([
      'AG', 'AR', 'AW', 'BB', 'BL', 'BM', 'BO', 'BQ', 'BR', 'BS', 'BZ', 'CA', 'CL', 'CO', 'CR',
      'CU', 'CW', 'DM', 'DO', 'EC', 'FK', 'GD', 'GF', 'GL', 'GP', 'GT', 'GY', 'HN', 'HT', 'JM',
      'KN', 'KY', 'LC', 'MF', 'MQ', 'MS', 'MX', 'NI', 'PA', 'PE', 'PM', 'PR', 'PY', 'SR', 'SV',
      'SX', 'TC', 'TT', 'US', 'UY', 'VC', 'VE', 'VG', 'VI', '419'
    ]);
    const additionalAmericanTimeZones = new Set([
      'Atlantic/Bermuda',
      'Pacific/Easter',
      'Pacific/Galapagos',
      'Pacific/Honolulu',
      'Pacific/Pitcairn'
    ]);

    function setCaret(toggle, isOpen) {
      const caret = toggle.querySelector('.caret-icon');
      if (caret) {
        caret.innerHTML = isOpen ? '&#9652;' : '&#9662;';
      }
    }

    function closeAllMenus() {
      bar.querySelectorAll('.dropdown').forEach(dropdown => {
        const menu = dropdown.querySelector('.dropdown-menu');
        const toggle = dropdown.querySelector('.dropdown-toggle');
        menu.classList.remove('show');
        toggle.setAttribute('aria-expanded', 'false');
        setCaret(toggle, false);
      });
    }

    function getLanguagesForVersion(version) {
      const manifestLanguages = manifest &&
        manifest.languagesByVersion &&
        Array.isArray(manifest.languagesByVersion[version]) &&
        manifest.languagesByVersion[version].length
          ? manifest.languagesByVersion[version]
          : null;

      if (manifestLanguages) {
        return manifestLanguages;
      }

      return inlineLanguages;
    }

    function getDefaultLanguageForVersion(version) {
      const manifestDefault = manifest &&
        manifest.defaultLanguageByVersion &&
        typeof manifest.defaultLanguageByVersion[version] === 'string'
          ? manifest.defaultLanguageByVersion[version]
          : '';

      if (manifestDefault) {
        return manifestDefault;
      }

      const availableLanguages = getLanguagesForVersion(version);
      return availableLanguages.length ? availableLanguages[0] : (inlineLanguages[0] || '');
    }

    function populateSelectorMenu(selector, values) {
      const menu = bar.querySelector(`[data-selector="${selector}"] .dropdown-menu`);
      if (!menu) {
        return;
      }

      menu.innerHTML = '';
      values.forEach(value => {
        const link = document.createElement('a');
        link.href = '#';
        link.setAttribute('role', 'option');
        link.textContent = value;
        menu.appendChild(link);
      });
    }

    function getNavigationContext() {
      const currentUrl = new URL(window.location.href);
      const rawSegments = currentUrl.pathname.split('/').filter(Boolean);
      const decodedSegments = rawSegments.map(segment => decodeURIComponent(segment));
      const currentVersionLabel = bar.querySelector('[data-selector="version"] .current-value');
      const currentLanguageLabel = bar.querySelector('[data-selector="language"] .current-value');
      const fallbackVersion = currentVersionLabel ? currentVersionLabel.textContent.trim() : '';
      const versionIndex = decodedSegments.findIndex(segment => versions.includes(segment));
      const currentVersion = versionIndex !== -1 ? decodedSegments[versionIndex] : fallbackVersion;
      const availableLanguages = getLanguagesForVersion(currentVersion);
      const fallbackLanguage = currentLanguageLabel ? currentLanguageLabel.textContent.trim() : '';
      const languageIndex = decodedSegments.findIndex(
        (segment, index) => index > versionIndex && availableLanguages.includes(segment)
      );

      return {
        currentUrl: currentUrl,
        rawSegments: rawSegments,
        versionIndex: versionIndex,
        currentVersion: currentVersion,
        currentLanguage: languageIndex !== -1 ? decodedSegments[languageIndex] : fallbackLanguage
      };
    }

    function refreshNavigationMenus() {
      const context = getNavigationContext();
      const resolvedVersion = versions.includes(context.currentVersion) ? context.currentVersion : (versions[0] || context.currentVersion);
      const availableLanguages = getLanguagesForVersion(resolvedVersion);
      const resolvedLanguage = availableLanguages.includes(context.currentLanguage)
        ? context.currentLanguage
        : (getDefaultLanguageForVersion(resolvedVersion) || context.currentLanguage);

      populateSelectorMenu('version', versions);
      populateSelectorMenu('language', availableLanguages);

      const versionLabel = bar.querySelector('[data-selector="version"] .current-value');
      const languageLabel = bar.querySelector('[data-selector="language"] .current-value');
      if (versionLabel) {
        versionLabel.textContent = resolvedVersion;
      }
      if (languageLabel) {
        languageLabel.textContent = resolvedLanguage;
      }
    }

    function buildScopedUrl(targetVersion, targetLanguage, pageName) {
      const context = getNavigationContext();
      const rootSegments = context.versionIndex !== -1 ? context.rawSegments.slice(0, context.versionIndex) : [];
      const targetPath = '/' + rootSegments.concat([
        encodeURIComponent(targetVersion),
        encodeURIComponent(targetLanguage),
        encodeURIComponent(pageName)
      ]).join('/');

      if (context.currentUrl.protocol === 'file:') {
        return 'file://' + targetPath;
      }

      return context.currentUrl.origin + targetPath;
    }

    function buildTargetUrl(targetVersion, targetLanguage) {
      return buildScopedUrl(targetVersion, targetLanguage, 'index.html');
    }

    function buildSiteRootAssetUrl(fileName) {
      const context = getNavigationContext();
      const rootSegments = context.versionIndex !== -1 ? context.rawSegments.slice(0, context.versionIndex) : [];
      const targetPath = '/' + rootSegments.concat([encodeURIComponent(fileName)]).join('/');

      if (context.currentUrl.protocol === 'file:') {
        return 'file://' + targetPath;
      }

      return context.currentUrl.origin + targetPath;
    }

    function buildClientSiteZipUrl() {
      return buildSiteRootAssetUrl(offlineZipFileName);
    }

    function getHeadingText(heading) {
      const clone = heading.cloneNode(true);
      clone.querySelectorAll('a.headerlink').forEach(link => link.remove());
      return clone.textContent.replace(/\s+/g, ' ').trim();
    }

    function normalizeMailText(text) {
      return String(text || '').replace(/\u00AE/g, '');
    }

    function getTimeZoneAmericaDecision() {
      try {
        const timeZone = String(Intl.DateTimeFormat().resolvedOptions().timeZone || '').trim();
        if (!timeZone) {
          return null;
        }
        return timeZone.startsWith('America/') || additionalAmericanTimeZones.has(timeZone);
      } catch (error) {
        return null;
      }
    }

    function isCoordinateInAmericas(latitude, longitude) {
      if (!Number.isFinite(latitude) || !Number.isFinite(longitude)) {
        return null;
      }

      return latitude >= -60 && latitude <= 85 && longitude >= -170 && longitude <= -25;
    }

    function getCurrentPosition(options) {
      return new Promise((resolve, reject) => {
        if (!navigator.geolocation || typeof navigator.geolocation.getCurrentPosition !== 'function') {
          reject(new Error('Geolocation unavailable'));
          return;
        }

        navigator.geolocation.getCurrentPosition(resolve, reject, options);
      });
    }

    async function resolveServiceAddress() {
      const timeZoneDecision = getTimeZoneAmericaDecision();
      if (timeZoneDecision === false) {
        return 'service@arsautomation.com';
      }

      const canTryGeolocation = Boolean(
        navigator.onLine &&
        window.isSecureContext &&
        navigator.geolocation &&
        typeof navigator.geolocation.getCurrentPosition === 'function'
      );

      if (canTryGeolocation) {
        try {
          const position = await getCurrentPosition({
            enableHighAccuracy: false,
            timeout: 4000,
            maximumAge: 300000
          });
          const inAmericas = isCoordinateInAmericas(position.coords.latitude, position.coords.longitude);
          if (inAmericas !== null) {
            return inAmericas ? 'us.service@arsautomation.com' : 'service@arsautomation.com';
          }
        } catch (error) {
        }
      }

      if (timeZoneDecision === true) {
        return 'us.service@arsautomation.com';
      }

      return 'service@arsautomation.com';
    }

    function buildMailtoUrl(address, subject, body) {
      return 'mailto:' + address +
        '?subject=' + encodeURIComponent(normalizeMailText(subject)) +
        '&body=' + encodeURIComponent(normalizeMailText(body));
    }

    function createHeadingActionLink(className, title, mailtoUrl, svgMarkup) {
      const link = document.createElement('a');
      link.className = 'headerlink manual-heading-action ' + className;
      link.href = mailtoUrl;
      link.title = title;
      link.setAttribute('aria-label', title);
      link.innerHTML = svgMarkup;
      return link;
    }

    function addHeadingActions() {
      const feedbackIcon = [
        '<svg viewBox="0 0 16 16" aria-hidden="true">',
        '<path d="M3 3.5h10v6.5H7.5L4.5 13v-3H3z"></path>',
        '<path d="M6 6.2h4"></path>',
        '<path d="M6 8.2h3"></path>',
        '</svg>'
      ].join('');

        const serviceIcon = [
          '<svg viewBox="0 0 16 16" aria-hidden="true">',
          '<circle cx="8" cy="8" r="5.2"></circle>',
          '<path d="M6.4 6.1A1.9 1.9 0 0 1 8 5.2c1.1 0 1.9.7 1.9 1.7 0 .8-.4 1.3-1.2 1.8-.6.4-.9.8-.9 1.5"></path>',
          '<circle cx="8" cy="11.7" r="0.45" style="fill:currentColor;stroke:none"></circle>',
          '</svg>'
        ].join('');

      document.querySelectorAll('h1 > a.headerlink, h2 > a.headerlink, h3 > a.headerlink, h4 > a.headerlink, h5 > a.headerlink, h6 > a.headerlink').forEach(link => {
        const heading = link.parentElement;
        if (!heading || heading.querySelector('.manual-feedback-link') || heading.querySelector('.manual-service-link')) {
          return;
        }

        const sectionTitle = getHeadingText(heading);
        const sectionUrl = new URL(link.getAttribute('href'), window.location.href).href;
        const pageUrl = window.location.href.split('#')[0];
        const feedbackBody = [
          'Hello Documentation Team,',
          '',
          'I would like to suggest an improvement for this section of the manual.',
          '',
          'Section: ' + sectionTitle,
          'Page: ' + pageUrl,
          'Section link: ' + sectionUrl,
          '',
          'Suggestion:',
          ''
        ].join('\n');
          const serviceBody = [
            'Hello Service Team,',
            '',
            'I need support related to this section of the manual.',
            '',
            'Section: ' + sectionTitle,
            'Page: ' + pageUrl,
            'Section link: ' + sectionUrl,
            '',
            'FlexiBowl serial number:',
            '',
            'Photos or videos of the issue attached:',
            '',
            'Issue description:',
            ''
          ].join('\n');

        const feedbackLink = createHeadingActionLink(
          'manual-feedback-link',
          'Suggest an improvement for this section',
          buildMailtoUrl('documentation@arsautomation.com', 'Documentation suggestion: ' + sectionTitle, feedbackBody),
          feedbackIcon
        );
          const serviceLink = createHeadingActionLink(
            'manual-service-link',
            'Contact service about this section',
            '#',
            serviceIcon
          );
          serviceLink.addEventListener('click', async event => {
            event.preventDefault();
            const serviceAddress = await resolveServiceAddress();
            window.location.href = buildMailtoUrl(serviceAddress, 'Service request: ' + sectionTitle, serviceBody);
          });

          heading.appendChild(feedbackLink);
          heading.appendChild(serviceLink);
        });
    }

    function enhancePrintMenu() {
      const dropdown = document.querySelector('.dropdown-download-buttons');
      if (!dropdown || dropdown.dataset.printMenuEnhanced === 'true') {
        return;
      }

      dropdown.dataset.printMenuEnhanced = 'true';

      const toggleButton = dropdown.querySelector('.dropdown-toggle');
      const hasReleaseDownloads = offlineZipEnabled;

      if (toggleButton) {
        const toggleLabel = hasReleaseDownloads ? 'Export options' : 'Print options';
        toggleButton.setAttribute('aria-label', toggleLabel);
        toggleButton.setAttribute('title', toggleLabel);
        toggleButton.setAttribute('data-bs-original-title', toggleLabel);
        const toggleIcon = toggleButton.querySelector('i');
        if (toggleIcon) {
          toggleIcon.className = hasReleaseDownloads ? 'fas fa-download' : 'fas fa-print';
        }
      }

      dropdown.querySelectorAll('.btn-download-source-button').forEach(sourceButton => {
        const sourceItem = sourceButton.closest('li');
        if (sourceItem) {
          sourceItem.remove();
        }
      });

      const pagePrintButton = dropdown.querySelector('.btn-download-pdf-button');
      if (pagePrintButton) {
        pagePrintButton.setAttribute('title', 'Print this page');
        pagePrintButton.setAttribute('aria-label', 'Print this page');
        pagePrintButton.setAttribute('data-bs-original-title', 'Print this page');
        const textContainer = pagePrintButton.querySelector('.btn__text-container');
        if (textContainer) {
          textContainer.textContent = 'Print this page';
        }
      }

      const menu = dropdown.querySelector('.dropdown-menu');
      if (!menu) {
        return;
      }

      menu.querySelectorAll('.btn-download-client-site-zip-button').forEach(button => {
        const item = button.closest('li');
        if (item) {
          item.remove();
        }
      });

      if (offlineZipEnabled) {
        const siteZipItem = document.createElement('li');
        const siteZipLink = document.createElement('a');
        siteZipLink.className = 'btn btn-sm dropdown-item btn-download-client-site-zip-button';
        siteZipLink.title = 'Download offline manual';
        siteZipLink.setAttribute('aria-label', 'Download offline manual');
        siteZipLink.setAttribute('download', offlineZipFileName);
        siteZipLink.href = buildClientSiteZipUrl();
        siteZipLink.innerHTML = [
          '<span class="btn__icon-container">',
          '<svg viewBox="0 0 16 16" aria-hidden="true">',
          '<path d="M4 3.5h8v2.5H4z"></path>',
          '<path d="M4 6h8v6.5H4z"></path>',
          '<path d="M8 3.5v9"></path>',
          '<path d="M6.3 9.2L8 10.9l1.7-1.7"></path>',
          '</svg>',
          '</span>',
          '<span class="btn__text-container">Download offline manual</span>'
        ].join('');
        siteZipItem.appendChild(siteZipLink);
        menu.appendChild(siteZipItem);
      }
    }

    refreshNavigationMenus();

    bar.querySelectorAll('.dropdown').forEach(dropdown => {
      const toggle = dropdown.querySelector('.dropdown-toggle');
      const menu = dropdown.querySelector('.dropdown-menu');
      const selector = dropdown.getAttribute('data-selector');

      toggle.addEventListener('click', event => {
        event.stopPropagation();
        const willOpen = toggle.getAttribute('aria-expanded') !== 'true';
        closeAllMenus();

        if (willOpen) {
          menu.classList.add('show');
          toggle.setAttribute('aria-expanded', 'true');
          setCaret(toggle, true);
        }
      });

      menu.addEventListener('click', event => {
        const link = event.target.closest('a');
        if (!link) {
          return;
        }

        event.preventDefault();
        const selectedValue = link.textContent.trim();
        const context = getNavigationContext();
        if (!selectedValue) {
          return;
        }

        if (selector === 'version') {
          const targetVersion = selectedValue;
          const availableLanguages = getLanguagesForVersion(targetVersion);
          const targetLanguage = availableLanguages.includes(context.currentLanguage)
            ? context.currentLanguage
            : getDefaultLanguageForVersion(targetVersion);
          if (targetLanguage) {
            window.location.href = buildTargetUrl(targetVersion, targetLanguage);
          }
          return;
        }

        window.location.href = buildTargetUrl(context.currentVersion, selectedValue);
      });
    });

    window.addEventListener('click', closeAllMenus);
    window.addEventListener('keydown', event => {
      if (event.key === 'Escape') {
        closeAllMenus();
      }
    });

    addHeadingActions();
    enhancePrintMenu();
  })();
</script>
