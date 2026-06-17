(camerasetup)=
# **Step 3: Camera Setup**

This section describes the procedure to configure and test the industrial camera of the FlexiVision One system. Correct camera configuration is essential to guarantee acquisition of high-quality images.

```{note}
**Prerequisites**

Before proceeding, make sure that:
- the camera has been installed mechanically at the correct distance
- the camera Ethernet cable is connected to the VisionController
- the camera is powered, through PoE or external power supply
- the FlexiBowl is configured and the backlight is working, for acquisition tests
```

---

## Accessing Camera configuration

```{list-table}

* - **1**
  - From the main software page, click <img src="../../../../../_shared/media/images/tasto_setup1.png" class="inline-icon">
* - **2**
  - In the SETUP page, locate and click the **Camera Setup** icon
    ```{dropdown} Setup page
       ![Setup page](../../../../../_shared/media/images/pagina_setup1.png)
    ```
* - **3**
  - The camera configuration page opens
```

---

## Camera Setup interface overview

The Camera Setup page includes three main information panels and one configuration area:

![Camera Setup page](../../../../../_shared/media/images/pagina_camsetup.png)

```{list-table}
:header-rows: 1
:widths: 30 70

* - Section
  - Description
* - **Selected Camera**
  - Shows the identification of the currently selected camera
* - **Camera Serial Number**
  - Displays the unique serial number of the connected camera
* - **Status**
  - Indicates connection status
* - **Calibration Result**
  - Shows the result of camera calibration
* - **Config Camera**
  - Button used to open the detailed configuration page
```

---

## Configuration procedure

```{note}
For consistency and convenience, it is recommended to match camera numbering with the corresponding FlexiBowl:
- ✅ Camera installed above FlexiBowl 1: `CAM-CIC-5000-20G-12345` -> select **Camera 1 FlexiBowl 1** and then select `CAM-CIC-5000-20G-12345` under **Image Acquisition Device**
```

```{list-table}
* - **Configuration access**
  - 1. Click **Config Camera X**, where `X` is the camera number
    2. The first page of the calibration wizard opens, where the **Cam Exposure** parameter can be modified

* - **Advanced mode activation**
  - 3. Click **Expert** in the lower right corner
    4. This mode provides access to all advanced camera settings required during initial configuration
* - **Image acquisition device configuration**
  - 5. In the **Expert** panel, click **Image Acquisition** under **Settings**
    6. Click **Image Acquisition Device**
    7. A selection menu opens with the available acquisition devices
* - **Specific camera identification**
  - 8. From the device list, select the desired camera
        - search the list by serial number or camera model
        - example: `CAM-CIC-5000-20G-XXXXX`, where `XXXXX` is the serial number
    9. Click the camera to select it
```

```{tip}
**How to identify the correct serial number**

If multiple cameras or devices are listed:
- the serial number is printed on a label on the physical camera
- compare the last group of characters in the serial number to identify the correct camera
- if in doubt, temporarily disconnect other cameras to identify the one in use
```

```{list-table}
* - **Video format selection**
  - 11. Click **Video Formats**
    12. From the list of available formats, select **Generic GigEVision**
    13. Select **Mono**, monochrome, as the sensor type
```

```{warning}
**Correct format is mandatory**

It is essential to select **Generic GigEVision Mono**:
- other formats may not work or may generate errors
- color formats are not compatible with this camera
- if the format is not available, required drivers or system settings may be missing
```

```{list-table}
* - **Acquisition system activation**
  - 14. After selecting the correct format, click **Initialize Acquisition**
    15. Wait a few seconds for initialization to complete
* - **Acquisition verification**
  - 16. Locate the **Run** button in the top left of the interface, play icon
    17. Click **Run** repeatedly, `5-10` times, to acquire test images
    18. Observe the image display area:
        - it should show the camera view of the FlexiBowl
        - the image should update every time **Run** is pressed
```

```{warning}
**Diagnosis of a completely blue screen**

If, during testing, the acquired image appears **completely blue** even once:

**Cause**: GigE communication problem, network latency or packet size not optimized

**Solution**:

1. From the top menu, select **GigE** or **GigE Vision Settings**

2. Modify the following parameters:
   - **Latency Level**
   - **Packet Size**

Proceed with the next steps for optimal configuration of these parameters.
```

---

### Latency Level

```{note}
**Latency adjustment**

The **Latency Level** parameter controls the communication buffer between the camera and the VisionController.

**Typical values**:
- default value: `0`
- available range: `0-3`

**How to adjust it**:

1. Increase the value gradually
2. After each change, test acquisition using the **Run** button `5-10` times
3. If blue screens no longer appear, the value is correct
4. If blue screens persist, increase it further or try adjustments to Packet Size
```

### Packet Size

```{note}
**Packet Size adjustment**

The **Packet Size** parameter defines the size of the data packets transmitted over the Ethernet network.

**Typical values**:
- default value: `8164 bytes`

**How to adjust it**:

1. Reduce the value gradually, `8000`, `7000`, and so on
2. After each change, test acquisition using the **Run** button `5-10` times
3. If blue screens no longer appear, the value is correct
4. If blue screens persist, reduce it further or try adjustments to Latency Level
```

---

```{list-table}
* - **Final verification and saving**
  - 19. Click **Run** at least `2-3` times consecutively
    20. Verify that:
      - no image appears completely blue or black
      - images update regularly
      - the FlexiBowl surface is clearly visible
      - illumination is uniform
    21. If all tests are positive, the configuration is correct
```

---

(calibrazione_camera_setup)=
# **Camera Calibration**

Calibration is the crucial step that establishes the exact geometric relationship between the real world, coordinates in millimeters, and the image acquired by the camera, coordinates in pixels. Without accurate calibration, the precision of the picking system is compromised, making the entire application unreliable.

```{warning}
Calibration must be repeated every time the position of the camera and or the robot is changed.
```

:::{tip}
It is not necessary to recalibrate if only the position of the FlexiBowl is changed.
:::

---

## **Why calibration is necessary**

Calibration is necessary because every sensor and lens combination introduces specific alterations into the image. Its main goal is to correct these distortions.

### Types of optical distortion

```{figure} ../../../../../_shared/media/images/distorsioni_new.png
:alt: Types of optical distortion
:width: 80%
:align: center
```

---

## **Step 1: Calibration grid**

:::{error}
Make sure that:
- the backlight is on
- the TopLight is off
:::

:::{video} ../../../../../_shared/media/videos/Step1_calib.mp4
    :width: 100%
    :align: center
:::

The dedicated ARS calibration grid must be positioned on the FlexiBowl:

```{list-table}
* - **0**
  - If present, remove the diverters mounted on the FlexiBowl.
* - **1**
  - **Loosen the four screws** of the central FlexiBowl flange
* - **2**
  - **Rotate the central flange slightly** counterclockwise and **remove it**
* - **3**
  - Carefully **lift** and **remove the surface**
* - **4**
  - **Position the ARS grid** on the FlexiBowl, aligning the positioning pins with the predefined holes
```

```{figure} ../../../../../_shared/media/images/griglia_su_flexibowl.png
:alt: Calibration grid positioning
:width: 60%
:align: center

Correct positioning of the ARS calibration grid on the FlexiBowl
```

:::{attention}
The calibration grid must be positioned **at the same height as the object** used in the application.

For this reason, the grid is supplied with **spacers** that must be inserted in the grid pins before installation on the FlexiBowl. They are used to raise the grid up to the part height, ensuring accurate calibration.

![Spacers](../../../../../_shared/media/images/distanziali_griglia.JPG)

```{figure} ../../../../../_shared/media/images/altezzacalibrazione.png
  :width: 100%
  :align: center
```
:::

## **Step 2: Basic adjustments**

:::{video} ../../../../../_shared/media/videos/Step2_calib.mp4
    :width: 100%
    :align: center
:::

```{list-table}
* - **5**
  - Open Camera SETUP from SETUP
* - **6**
  - Click the **Config Camera** button for the corresponding camera
* - **7**
  - Click **EXPERT** from the Camera FLB page
* - **8**
  - **Set the camera to live display mode**
      - activate continuous image display before adjusting the aperture
* - **9**
  - **Set the iris aperture**
    - slightly loosen the screw of the upper ring on the camera lens
    - rotate the ring while observing the live image until the correct amount of light enters the camera
    - tighten the screw of the upper ring

    :::{figure} ../../../../../_shared/media/images/Esp_Corretta.png
    :width: 100%
    :align: center
    :::
* - **10**
  - **Adjust camera focus manually**
    - slightly loosen the screw of the lower ring
    - rotate the ring slowly while observing the live image
    - when the pattern appears sharp, focus is correct
    - tighten the lower-ring screw
    - close the screen
    :::{figure} ../../../../../_shared/media/images/Fuoco_Corretto.png
    :width: 100%
    :align: center
    :::
* - **11**
  - Click **Back**
```

```{warning}
**Pay attention to depth of field**

Focus must guarantee sharpness over the **entire FlexiBowl surface**, not only in the center.

If the center is sharp but the edges are blurred:
- verify that the optics are clean
- verify that the working distance is correct
- verify that the camera is perfectly parallel to the plate
- close the iris slightly to increase depth of field

If the problem persists, the mechanical installation of the camera may need to be reviewed.
```

:::{video} ../../../../../_shared/media/videos/Step2b_calib.mp4
    :width: 100%
    :align: center
:::

:::{error}
If, by clicking **RUN** multiple times, even once you see a completely blue screen, refer to [Camera Calibration Troubleshooting](../../TROUBLESHOOTING/26e_Calib_Cam.md)
:::

```{list-table}
* - **12**
  - **Adjust camera exposure**
    - In the **Camera FLB x** page, locate the **Cam Exposure** parameter
    - Adjust **Cam Exposure** and click **TEST**, repeating until correct image exposure is obtained:
        - grid pattern clearly visible
        - high contrast between black and white squares
        - no burned white areas
        - no underexposed image
* - **13**
  - Click **NEXT**
```

```{figure} ../../../../../_shared/media/images/Esposizioni.png
:alt: Example of correct exposure
:width: 60%
:align: center

Example of correct exposure: high contrast, well-defined pattern, no burned areas
```

```{tip}
**Exposure optimization**

The higher the exposure time, the more light enters the optics.

- **Time too short**: image dark, pattern poorly visible
- **Time too long**: image overexposed, detail lost
- **Optimal time**: maximum contrast without saturation
```

## **Step 3: Camera calibration**

:::{video} ../../../../../_shared/media/videos/Step3_calib.mp4
    :width: 100%
    :align: center
:::

```{list-table}
:widths: 5 95

* - **14**
  - Verify that the grid is centered, sharp, and fully visible before acquiring the calibration image.
* - **15**
  - Click **Grab Image Calib** to capture the calibration grid image.

    Visually verify that:
    - the entire grid is visible
    - the pattern is sharp
    - there are no shadows or reflections

* - **16**
  - Set both **Tile Size X** and **Tile Size Y** to `10`

* - **17**
  - Click **Calibrate**

* - **18**
  - **Evaluate calibration quality**

    The **Result Calibration** parameter will return:

    🟢 **Excellent**: excellent calibration, optimal precision

    🟠 **Acceptable**: acceptable calibration, good but not optimal precision

    🔴 **Bad**: poor calibration, insufficient precision, must be repeated

    :::{important}
    Accept only **Excellent** calibrations. Other results compromise the entire application.
    :::
```

```{note}
**Acceptance criterion**

A satisfactory result includes correct aperture, correct focus, and the best exposure setting for the application.
```

```{warning}
**Errors during calculation**

If calibration fails:

**Possible causes**
- pattern not detected, image too dark or overexposed
- grid squares partially obscured
- excessive distortion, camera too close or too far
- incorrect Tile Size value

**Solution**
- verify and improve image quality
- make sure the entire grid is visible and well illuminated
- verify the Tile Size value
- repeat image acquisition and try again
```

---

### When calibration must be repeated

```{list-table}
:widths: 50 50
:header-rows: 0

* - **Recalibrate when**
  - first system setup, mandatory. After changing camera position. After moving the robot. If systematic picking errors are detected.

* - **Recalibration is not necessary when**
  - part type changes while FlexiBowl and camera remain the same. Lens focus or aperture is adjusted. Only the recipe changes. Only recognition parameters are adjusted. Robot programs are updated.
```

---

# **Robot Calibration**

## **Step 4: Laser mounting**

:::{video} ../../../../../_shared/media/videos/Step4_calib.mp4
    :width: 100%
    :align: center
:::

```{list-table}
* - **19**
  - Once excellent calibration quality is achieved, click **NEXT**.  
    A window will appear requiring robot calibration before proceeding. **Do not** click **Yes** yet and follow the next steps.
* - **20**
  - Mount the Laser Tool with its dedicated support
* - **21**
  - Position the Spacer Bracket (**A**) under the laser
* - **22**
  - Lower the laser to the level of Spacer (**A**), so the laser is exactly `3 cm` above the calibration grid
    :::{image} ../../../../../_shared/media/images/spacerbracket.png
    :align: center
    :width: 75%
    :::
* - **23**
  - Remove the Spacer Bracket
* - **24**
  - Turn on the laser
```

## **Step 5: Define a 3-point plane**

:::{video} ../../../../../_shared/media/videos/Step5_calib.mp4
    :width: 100%
    :align: center
:::

```{list-table}
* - **25**
  - Move the laser to the origin point
* - **26**
  - Move the laser to the end point of the X axis
* - **27**
  - Move the laser to the end point of the Y axis
```

## **Step 6: Verify robot trajectory**

:::{video} ../../../../../_shared/media/videos/Step6_calib.mp4
    :width: 100%
    :align: center
:::

```{list-table}
* - **28**
  - Bring the laser back to the origin point
* - **29**
  - Move the robot from its teach pendant along the X and Y axes
* - **30**
  - Verify that the correct trajectory is followed: moving only along X and Y, the robot must follow the grid lines correctly
* - **31**
  - Click **YES**
```

## **Step 7: Save the base recipe**

```{list-table}
:header-rows: 0
:widths: 10 90

* - **32**
  - Click **Recipes**

* - **33**
  - Verify that the recipe containing all setup steps and calibration is selected in the left menu, then click **Save Recipe**

* - **34**
  - This makes it possible to keep all completed steps stored separately, providing a base recipe for all future recipes containing the different models for the calibrated system

* - **35**
  - To continue with model creation, duplicate the base recipe, rename it as desired, and click **Edit Recipe**. A page listing all available models will open
```

---

# **Common calibration problems**

## **Pattern not detected**

```{warning}
**Error: "Unable to detect calibration pattern"**

Cause: the software cannot identify the grid pattern.

**Solutions**:
- increase contrast by adjusting exposure or illumination
- verify that the entire grid is visible in the image
- improve focus
- clean the grid surface, dust or fingerprints may interfere
```

## **Calibration always "Bad" or "Acceptable"**

```{warning}
**Insufficient calibration quality**

If calibration remains below **Excellent** despite the adjustments:

1. Verify the camera-FlexiBowl working distance, which must match the calculated one
2. Check that the camera is parallel to the FlexiBowl plane and perfectly horizontal
3. Make sure the camera is stable, no vibration during acquisition
4. Verify that the lens is fully screwed in

If the problem persists, there may be a mechanical installation issue. Review [Mechanical Installation](../../INSTALLAZIONE_SISTEMA/09_Installazione_Meccanica.md).
```



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
