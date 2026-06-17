(Installazione_Meccanica)=
# **Mechanical Installation of the System**

This section describes the mounting and positioning requirements of the key components of the FlexiVision One vision system. Installation must only be carried out after the basic mechanical installation of the FlexiBowl and the optional hopper has been completed.

```{warning}
**Mandatory prerequisites**

Before proceeding with installation of the vision components, make sure that:

- The FlexiBowl has been mounted and secured to the supporting structure, robot cell
- The hopper, if present, has been installed correctly
- The support structure for camera and illuminator has been prepared

For FlexiBowl installation, refer to the dedicated manual supplied with the system.
```

```{note}
**Required skills**

Mechanical installation requires:
- basic mechanical assembly skills
- use of measuring tools such as caliper, level, and tape measure
- ability to read technical drawings
```

---

## VisionController mounting

The VisionController, industrial PC, manages image processing and communication with the robot.  
As a sensitive electronic component, it requires careful positioning to guarantee proper ventilation and protection from contaminants.

### Technical specifications

```{figure} ../../../../_shared/media/images/Dim_PC.png
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

### Mounting requirements

```{list-table}
:header-rows: 1
:widths: 35 65

* - Requirement
  - Specifications
* - **Recommended position**
  - Inside the electrical cabinet or on a dedicated panel near the robot cell
* - **Ventilation clearance**
  - Minimum 50 mm on all sides for air circulation
* - **Fixing**
  - 35 mm DIN rail or M5 screws on panel
* - **Ambient temperature**
  - `1°C` to `+50°C`, refer to [VisionController Specifications](specifiche_VC) for complete data
* - **Protection**
  - Minimum IP40, installation inside an IP54 electrical cabinet is recommended
```

### Installation procedure

#### Mounting with holes

```{list-table}
   :header-rows: 1
   :widths: 35 65

   * - Phase
     - Operating instructions
   * - **1. Support preparation**
     - Drill the holes according to the technical drawing
   * - **2. Unpacking**
     - Remove the VisionController from the packaging, taking care not to damage the connectors. Verify product integrity.
   * - **3. Fixing**
     - Fix the VisionController using M5 screws
```

#### Mounting on DIN rail

```{list-table}
   :header-rows: 1
   :widths: 35 65

   * - Phase
     - Operating instructions
   * - **1. Support preparation**
     - Verify that the rail is clean and firmly fixed.
   * - **2. Unpacking**
     - Remove the VisionController from the packaging, taking care not to damage the connectors. Verify product integrity.
   * - **3. Fixing**
     - Hook the device onto the rail and slide it until it clicks into position.
```

```{warning}
**Ventilation**

The VisionController generates heat during operation. Always guarantee at least 50 mm of free space around the device.
Otherwise the following may occur:
- overheating and automatic shutdown
- reduced performance
- damage to internal components
```

---

## Camera mounting

Accurate camera positioning and alignment are critical steps that directly affect calibration accuracy and the performance of the picking system.

### Optimal working distance

The camera must be mounted so that the front face of the lens is positioned at a specific distance, Working Distance, from the surface of the FlexiBowl plate.  
For detailed calculation of the optimal distance for your application, refer to [Optimal Working Distance Calculation](distanza_lavoro).

```{image} ../../../../_shared/media/images/working_distance.JPG
:alt: Working Distance
:width: 40%
:align: center
```

```{list-table}
:header-rows: 1
:widths: 25 40 35

* - FlexiBowl model
  - Recommended working distance
  - Lens included in the kit, focal length
* - **FB 200**
  - 800 mm
  - 35 mm
* - **FB 350**
  - 1000 mm
  - 35 mm
* - **FB 500**
  - 1000 mm
  - 25 mm
* - **FB 650**
  - 1000 mm
  - 16 mm
* - **FB 800**
  - 1000 mm
  - 16 mm
* - **FB 1200**
  - 1300 mm
  - 12 mm
```

### Positioning and alignment

Correct camera alignment is essential to obtain high-quality images and guarantee picking accuracy.

**Incorrect configurations.** The images below show examples of incorrect camera positioning: the field of view, shown in red, is off-center with respect to the viewing area, covering only part of the working area or including zones outside it. These configurations compromise part recognition and vision system performance.

```{image} ../../../../_shared/media/images/config_sbagliata.png
:alt: Incorrect working distance configuration
:width: 60%
:align: center
```
```{image} ../../../../_shared/media/images/config_sbagliata2.png
:alt: Incorrect working distance configuration
:width: 60%
:align: center
```

**Correct configuration.** The camera must be positioned centrally with respect to the FlexiBowl viewing area, backlight zone. In this way the field of view, shown in green, symmetrically covers the whole working area, guaranteeing correct operation of the vision system.

```{image} ../../../../_shared/media/images/config_giusta.JPG
:alt: Correct working distance configuration
:width: 70%
:align: center
```

```{list-table}
* - **Centering**
  -
    - The camera must be positioned exactly above the FlexiBowl viewing area
    - Maximum centering tolerance: `±5 mm`
* - **Orthogonality**
  -
    - The camera must be mounted perfectly parallel to the plate surface
    - No lateral tilt or rotation away from vertical is allowed
    - Maximum tilt tolerance: `±1°`
```

```{tip}
To simplify commissioning and allow future adjustments, it is strongly recommended to design the camera support with micro-adjustment capability:
- **Z axis, height**: `-10 mm / +30 mm`, to adapt the working distance
- **X axis, left-right**: `±10 mm`, for fine centering
- **Y axis, front-back**: `±10 mm`, for fine centering

This flexibility is especially useful during initial calibration and for any future recalibration.
```

### Camera dimensions

```{figure} ../../../../_shared/media/images/Dimensioni_Cam.png
:alt: Camera dimensions CAM-CIC-5000-20G-1
:align: center
:width: 100%

CAM-CIC-5000-20G-1 camera dimensions, mm
```

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
* - Center distance of side mounting holes, M2
  - 20.0 × 23.7 mm
* - Front mounting holes
  - 2× M2 depth 3 mm
* - Side mounting holes
  - 4× M2 depth 3.5 mm + 3× M3 depth 3.5 mm
* - Weight
  - 88 g
```

```{warning}
**Fixing**
- Use the 4 M3 mounting holes on the camera body
- Recommended screws: `M3 A2 / M3 8.8`
- Tightening torque: `0.5 Nm`, do not overtighten to avoid deformation
```

```{tip}
**Camera position adjustment**

To allow future corrections and avoid alignment issues, design the mechanical support with micro-adjustment on all axes:

- **Z axis, height**: `-10 mm / +30 mm`
- **X axis, left-right**: `±10 mm`
- **Y axis, front-back**: `±10 mm`

A support fixed permanently with no adjustment capability makes it impossible to correct camera position after first installation.
```

### Verify lens mounting

```{warning}
Before final fixing:
1. Visually verify that the lens is installed
2. Check that the focal length is correct for your FlexiBowl model, lens label or order documentation
3. Make sure the lens is fully screwed in, metal-to-metal contact between lens and camera body
4. Do not remove or loosen the lens if it is already mounted correctly
```

### Camera installation

To guarantee correct operation of the vision system, the camera must be installed on a rigid and stable support.
The FlexiBowl system itself does not generate vibration, but automated lines may include other vibration sources, such as industrial robots, transfer systems, or other machines in the line.

If such vibrations are transmitted to the camera, the acquired image may become unstable and the coordinates calculated by the vision system may become unreliable, compromising robotic picking accuracy.

![Camera installation](../../../../_shared/media/images/installazionecamera.png)

:::{tip}
For this reason it is recommended to:

- install the camera on a rigid and stable structure
- avoid supports affected by vibrations coming from robots or other machines
- preferably use a structure independent from the machine
:::

```{warning}
**Camera fixing screws: loosening prevention**

Camera fixing screws may loosen over time for the following reasons:

- **Excessive tightening torque, above 0.5 Nm**: can deform the camera body and lead to later loosening. Always tighten with a maximum torque of **0.5 Nm**.
- **Vibrations transmitted by the line**: use **medium-strength threadlocker** on all fixing screws.
- **Incorrect screws**: verify the use of **M3 × 8 mm stainless steel** screws as recommended.
```

### Camera position adjustment

The camera support must allow position adjustment to permit correct alignment with the FlexiBowl picking area.

![Camera adjustments](../../../../_shared/media/images/regolazionicamera.png)

:::{note}
Starting from a nominal position with correct inclination, height, and centering over the backlit area, the following adjustments are recommended:

X/Y adjustment -> `±50 mm`  
Z adjustment -> `±50 mm`  
Rotation `θ` -> `±10°`
:::

```{caution}
**Camera damaged during installation**

To avoid damaging the camera during installation and adjustment:

- **Excessive tightening torque**: do not exceed **0.5 Nm** on M3 screws. Exceeding this value can irreversibly deform the optical body.
- **Incorrect handling**: always handle the camera carefully, avoiding direct pressure on the optical body and sensor.
- **Impacts during installation**: protect the camera during nearby mechanical work such as drilling, milling, or tightening structures.
```

---

## TopLight mounting

If the order includes a TopLight, overhead illuminator, it must be mounted on the same support structure as the camera to guarantee uniform illumination of the working surface.

:::{attention}
During installation, the device must be switched off and disconnected from power.
:::

### TopLight dimensions

![TopLight dimensions](../../../../_shared/media/images/toplight_dim.JPG)

| Length × Width (mm) | Height (mm) | Height with fixing plate (mm) | Central hole diameter | Maximum useful surface [A × B] | Maximum useful perimeter |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **A × B** | **C** | **C + 10 mm** | **D** | **-** | **-** |
| 500x300 | 45 | 55 | 65 | 0.15 m² | 1.6 m |
| 700x300 | 45 | 55 | 65 | 0.21 m² | 2 m |
| 700x500 | 45 | 55 | 65 | 0.35 m² | 2.4 m |
| 900x600 | 45 | 55 | 65 | 0.54 m² | 3 m |

### TopLight positioning

The TopLight must be positioned centrally with respect to the useful illuminated panel area, with the camera optics mounted inside the central hole and flush with the upper surface of the TopLight.  
The red arrows indicate the fixing screws of the lens rings, one for focus adjustment and one for iris adjustment. As shown in the figure, the TopLight must be mounted so that both screws remain accessible from above.

![TopLight and camera position](../../../../_shared/media/images/posizione_cam_TPL_B.png)

The camera field of view and the TopLight light beam, shown in green, must be aligned concentrically and perpendicularly with respect to the FlexiBowl viewing area.  
As shown in the three views, front, top, and isometric, the TopLight must illuminate exactly the area framed by the camera, with both components centered on the vertical optical axis of the system.

![TopLight camera and FlexiBowl correct position](../../../../_shared/media/images/posizioneTPL_giusta.png)

An incorrect position occurs when the TopLight and camera are not centered on the FlexiBowl viewing area.  
As illustrated in red, two typical errors are:
- shifting forward or backward with respect to the viewing area
- rotating the TopLight with respect to it

In both cases, illumination becomes misaligned and not perpendicular, compromising acquisition quality.

![TopLight camera and FlexiBowl incorrect position](../../../../_shared/media/images/posizioneTPL_sbagliata.png)

### Installation procedure

```{list-table}
:header-rows: 1
:widths: 35 65

* - **Phase**
  - **Operating instructions**
* - **1. Positioning**
  - Fix the TopLight to the support structure in a concentric position with respect to the camera.
* - **2. Distance from the surface**
  - Position the illuminator at a distance from the FlexiBowl surface similar to that of the camera in order to:

    * minimize shadows cast by the parts
    * maximize lighting uniformity
    * avoid direct reflections into the camera
* - **3. Orientation**
  - Make sure that the emitting surface of the TopLight is parallel to the FlexiBowl plate.
* - **4. Lighting angle**
  - Perpendicular to the surface, `0°` tilt.
* - **5. Fixing**
  - According to the chosen fixing method, see the next section.
```

### Fixing methods

The TopLight can be fixed in two ways: on the [corner](angolo) or on the [side](lato).

:::{note}
Fixing components are **not included** with the TopLight supply. Mounting can therefore be customized according to installation requirements.

- Side fixing, groove: M4 nuts **supplied**
- Corner fixing: `M4x20` CHC screws **not supplied**

In both cases the use of a **threadlocker** compound, not supplied, is recommended to prevent loosening over time. Recommended tightening torque is between **0.5 and 1.5 Nm**.
:::

(angolo)=
#### 1. Corner fixing

Corner fixing uses `M4x20` CHC screws, not supplied, applied in the holes located at the four corners of the TopLight.

```{figure} ../../../../_shared/media/images/fissaggio_angolo.png
:alt: TopLight corner fixing with M4x20 CHC screw
:align: center
:width: 60%

Corner fixing using M4x20 CHC screw, not supplied.
```

(lato)=
#### 2. Side fixing, groove

Side fixing uses 4 M4 nuts, supplied, to be inserted into the side groove of the TopLight profile. The maximum insertion depth of the nut in the groove is **5 mm**.

```{figure} ../../../../_shared/media/images/fissaggio_lato.JPG
:alt: TopLight side fixing using M4 nuts in the groove
:align: center
:width: 100%

Side fixing using 4 supplied M4 nuts inserted in the profile groove. Maximum depth: 5 mm.
```

##### Side fixing with brackets

If the TopLight is mounted using brackets:

:::{error}
![Incorrect side mounting](../../../../_shared/media/images/errorimontaggiolaterale.png)
:::

:::{tip}
![Correct side mounting](../../../../_shared/media/images/montaggiolaterale.png)
:::

### Illuminator wiring

![TopLight pinout](../../../../_shared/media/images/pin_toplight.png)

```{list-table}
:header-rows: 1
:widths: 30 70

* - Parameter
  - Requirement / Action
* - **Voltage**
  - 24 V DC, +/-10%. Minimum operating voltage: 20 V DC at the light input.
* - **Connector**
  - M12 5-pole, T-coding.
* - **Connector pinout**
  - Pin 1: +24V, brown. Pin 3: GND, blue. Pin 4: STROBE PNP, black.
* - **STROBE mode, PNP**
  - From 5 V to 24 V for 100% ON. From 0 V to 1 V for 100% OFF.
* - **CONTINUOUS mode**
  - Pin 1, +24V, and Pin 3, GND, connected. Pin 4, PNP, connected to Pin 1.
* - **Voltage drop, 10 m M12 cable**
  - 1.15V @ 5A - 2.3V @ 10A - 3.5V @ 15A - 4.6V @ 20A, max 20A
* - **Shielding**
  - Use shielded cables to reduce electromagnetic interference, EMI.
```

```{warning}
**Electrical safety**

- Respect the indicated supply voltages and connection terminals.
- Do not modify or disassemble the product.
- Do not connect or clean the device while powered.
- Do not look directly at the light source.
```

```{note}
For details about electrical connections, refer to [Wiring and Connections](10_Cablaggio_Connessioni.md).
```

---

## Shielding from ambient light

The stability of the vision system strongly depends on the consistency of lighting conditions. Variable ambient light can cause inconsistent detections.

```{warning}
**Protection from external light sources**

It is strongly recommended to shield the robot cell from:
- direct or indirect sunlight
- variable artificial lighting, for example lamps with dimmers
- reflections from nearby glossy surfaces
- flashes or intermittent lights in the area
```

---

## Related references

For information complementary to mechanical installation:

- **Optimal camera distance calculation**: [Optimal Working Distance Calculation](distanza_lavoro)
- **Complete technical specifications**: [FlexiVision One Specifications](specifiche_tecniche)
- **Next step - electrical connections**: [Wiring and Connections](cablaggio)
- **Camera calibration**: [Camera Calibration](calibrazione)



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
