(dashboard)=
# **Application Monitoring: Dashboard**

The **Dashboard** is the main interface for real-time monitoring of the FlexiVision One system. On this page it is possible to verify process efficiency, analyze cycle times, validate component recognition, and identify any bottlenecks in the system.

---

## Interface overview

The Dashboard interface is divided into four main sections:

![Dashboard page](../../../../_shared/media/images/pagina_dashboard.png)

1. [**Operational Control**](controllooperativo): commands and execution status
2. [**Vision Analysis**](analisivisione): display of detected parts and details
3. [**Performance Indicators**](indicatoriperformance): connectivity and cycle times
4. [**Graph Analysis**](analisigrafica): historical productivity and timing graphs

---

(controllooperativo)=
## Operational Control - commands and execution status

```{list-table}
:header-rows: 1
:widths: 25 75

* - Element
  - Description and function
* - **In Run**
  - Status indicator showing whether the system is currently operating.  
    **Green** 🟢: system active and running.  
    **Red** 🔴: system stopped or paused.
* - **In Run Time**
  - Displays the total system operating time since application startup.
* - **FlexiBowl selection**
  - Dropdown menu used to select the specific FlexiBowl to monitor.
* - **Test Locator**
  - Captures an image of the viewing area and starts recognition of the parts currently present.
```

```{tip}
**Test Locator**

Useful for:
- verifying that parts are actually recognized by the vision system
- checking Clearance reliability if a collision occurred between the robot and a component
```

---

(analisivisione)=
## Vision Analysis

The center of the Dashboard displays the data related to the components identified by the vision system.

### Detected Vision Parts

**Detected Vision Parts** shows:
- the real-time image acquired by the camera
- a **historical chart** of detections over the last 30 seconds, showing the trend of recognized parts per acquisition

### Detected models table

**Recognized component details**

The table below the image lists all components present in the pick area with the following parameters:

```{list-table}
:header-rows: 1
:widths: 15 20 65

* - Field
  - Data Type
  - Description
* - **Id**
  - Integer
  - Progressive unique identifier of the component, `0`, `1`, `2`, and so on.  
    `Id 0` = component with the highest score, best match to the model when sorted by descending Score as recommended.
* - **X**
  - Millimeters
  - X coordinate of the component.
* - **Y**
  - Millimeters
  - Y coordinate of the component.
* - **Rot (Rotation)**
  - Degrees
  - Rotation angle of the component.
* - **Score**
  - Percentage
  - Percentage value, `0.00-1.00` or `0%-100%`, expressing recognition reliability. It represents similarity to the reference model. Higher score means better correspondence.
```

```{list-table} **Score interpretation**

* - **Score > 0.90, 90%**
  -
    - Excellent match to the model
    - High-confidence picking

* - **Score 0.80-0.90, 80-90%**
  -
    - Good match
    - Safe picking if Accept Threshold is configured correctly

* - **Score 0.70-0.80, 70-80%**
  -
    - Acceptable match
    - Verify consistency over time

* - **Score < 0.70, below 70%**
  -
    - Poor match
    - If recurrent, review the model or the Accept Threshold
```

---

(indicatoriperformance)=
## Status and Performance Indicators

### Connectivity

Status indicators for communication with external devices:

```{list-table}
:header-rows: 1
:widths: 25 75

* - Indicator
  - Description
* - **FlexiBowl**
  - Status of the hardware connection between the VisionController and the FlexiBowl.  
    **Green**: connected and communicating.  
    **Red**: disconnected or communication error.
* - **Robot**
  - Status of communication with the robot.  
    **Green**: TCP/IP connection established.  
    **Red**: disconnected or communication timeout.
```

```{warning}
**Actions in case of disconnection**

**FlexiBowl red**:
- Verify the Ethernet cable from FlexiBowl to VisionController
- Check FlexiBowl power supply
- Verify FlexiBowl IP in FlexiBowl Setup
- Try reconnecting or restarting the software

**Robot red**:
- Verify the Ethernet cable from robot to VisionController
- Check that the robot has opened the TCP/IP connection
- Verify the TCP/IP port in Robot Setup
- Check the robot program, VisionController IP address and port entered correctly in Robot Setup

In production, both indicators must always be green.
```

### Timing analysis

The system provides a detailed breakdown of cycle times in order to identify bottlenecks and optimize the process.

```{list-table}
:header-rows: 1
:widths: 35 65

* - Time Item
  - Description
* - **Camera Processing Time**
  - Time required for image acquisition from the camera sensor. Includes exposure time and data transfer.
* - **Locator Processing Time**
  - Time required by the vision algorithm to locate and recognize the components in the acquired image. It depends on the number of active models, model complexity, and number of Clearances.
* - **Total Vision Processing**
  - Sum of Camera and Locator times. It represents the total time required by the vision system to process one image and send the coordinates.
* - **Total FlexiBowl Time**
  - Time required by the FlexiBowl to execute a complete movement sequence.
* - **Total Robot Time**
  - Estimated or measured time for the complete robot Pick and Place operation. Includes approach, grasp, lift, deposit, and return.
* - **Total Processing Time**
  - Total time of the complete cycle, Vision plus FlexiBowl plus Robot. It represents the time from the start of one cycle to the start of the next. It determines the maximum theoretical productivity, PPM.
```

```{tip}
**How to interpret timings for optimization**

The timing graph makes it possible to identify the **system bottleneck**:

**If Total Vision Processing is the largest**
- Too many active models -> disable models that are not required
- Models too complex -> simplify them using a higher Score Threshold
- Too many Clearances -> reduce the number or size of the Clearances
- Camera Processing too high -> reduce exposure time

**If Total FlexiBowl Time is the largest**
- Too many pauses -> optimize Flip and Move synchronization and reduce stabilization pause, Pause X ms
- Movement sequence too slow -> increase speed in Config FlexiBowl
- Rotation angle too large -> reduce Move Angle
- Shake too long -> increase SHAKE speed and reduce SHAKE cycles

**If Total Robot Time is the largest**
- Robot trajectory not optimized -> optimize robot path planning
- Robot speed too low -> increase movement speed if safe
- Deposit distance too large -> reposition the deposit point closer
- Gripper opening and closing too slow -> optimize gripper timing

**Optimization goal**: balance the three times to reduce overall Total Processing Time.
```

---

(analisigrafica)=
## Graph Analysis

The graphs in the lower part of the Dashboard enable predictive and diagnostic analysis of system performance over time.

### 1. Parts Per Minute, PPM

```{list-table}
* - **Productivity graph**
  - Shows average system productivity expressed as **parts picked per minute**, Parts Per Minute.

* - **Characteristics**
  -
    - X axis: time
    - Y axis: PPM
    - Trend line: moving average used to identify trends

* - **Usage**
  -
    - Monitor productivity stability over time
    - Identify performance degradation
    - Compare actual throughput with theoretical throughput
```

```{tip}
  :::{list-table} **PPM interpretation**

    * - **PPM constant and stable**
      -
        - ✓ System well configured
        - ✓ Parameters optimized
        - ✓ No critical bottleneck

    * - **PPM gradually decreasing**
      -
        - ⚠️ Possible component wear, for example FlexiBowl grip surface
        - ⚠️ Hopper running low, if present, lower pressure means slower discharge
        - ⚠️ Dirt accumulation on camera or lighting

    * - **PPM with wide fluctuations**
      -
        - ⚠️ Process instability
        - ⚠️ Intermittent recognition issues
        - ⚠️ External interference, vibration or variable light

    * - **Corrective actions**
      -
        - Analyze correlation with timing graphs
        - Identify which subsystem, Vision, FlexiBowl, or Robot, causes the variation
        - Intervene on the specific parameters
  :::
```

### 2. Fill Hopper

```{list-table}
* - **Hopper activation graph**
  - Represents the history of discharge pulses sent to the hopper, useful for monitoring component stock autonomy.

* - **Characteristics**
  -
    - X axis: time
    - Y axis: Hopper activations, events
    - Peaks: each peak represents one discharge activation

* - **Usage**
  -
    - Predict when to physically refill the hopper
    - Verify hopper configuration effectiveness
    - Identify anomalies in discharge behavior
```

```{tip}
  :::{list-table} **Fill Hopper pattern analysis**

    * - **Regular and constant activations**
      -
        - ✓ Hopper configuration optimal
        - ✓ Stable and predictable part flow
        - ✓ Autonomy can be estimated, for example one activation every 10 minutes

    * - **Increasingly frequent activations**
      -
        - ⚠️ Hopper is running low, fewer parts mean more activations needed to maintain level
        - ⚠️ Discharge Time insufficient for reduced volume
        - **Action**: schedule hopper refill soon

    * - **No activation for a long period**
      -
        - ⚠️ Robot stopped or slowed down, parts are not being consumed
        - ⚠️ Possible system issue, no request for parts
        - **Action**: verify production status

    * - **Very close activations, burst**
      -
        - ⚠️ Hopper threshold configured incorrectly, too high
        - ⚠️ Steps insufficient, parts do not arrive in time
        - **Action**: review Hopper configuration
  :::
```

### 3. Vision - FlexiBowl - Robot, comparative graph

```{list-table}
* - **Overlapped timing graph**
  - A comparative three-line graph that overlays process times over time.

* - **Usage**
  - Instantly identify which process affects total cycle time the most and how it changes over time.
```

---

## Quality monitoring - critical indicators to monitor

```{list-table}
* - **Component score**
  - Make sure that the **Score** of detected components remains consistently above the tolerance threshold, Accept Threshold, configured during model setup.

* - **Score monitoring**
  -
    - Periodically check the Detected Models table
    - Verify that typical scores are in the `0.85-0.95` range
    - Investigate if scores regularly drop below `0.80`

* - **Progressive score decrease**
  -
    - ⚠️ Real parts differ from the training part, production variation
    - ⚠️ Lighting changed, weaker backlight or dirt
    - ⚠️ Camera no longer in focus, vibration or impacts
    - ⚠️ FlexiBowl surface dirty, interfering pattern

* - **Corrective actions**
  -
    - Clean the camera, lighting, and FlexiBowl surface
    - Verify camera focus
    - Consider retraining the model if the parts have changed
    - Reduce Accept Threshold if scores are still reliable but lower
```

---

## Best practices for production monitoring

### Daily checks

```{list-table}
* - **At production start, 5 minutes**
  -
    - Verify FlexiBowl and Robot connectivity indicators, green
    - Check that the first cycles show normal scores, above `0.85`
    - Observe that PPM stabilizes around the expected value

* - **During production, every 1-2 hours**
  -
    - Check PPM to verify stability
    - Check Fill Hopper to predict required refill
    - Verify absence of errors or warnings in the log

* - **At end of shift, 2 minutes**
  -
    - Record average shift PPM
    - Check the number of hopper activations
    - Verify anomalies or events
    - Compare with the previous day
```

This minimal routine guarantees fast identification of problems and preserves performance traceability.

### Performance reporting

```{tip} **Key metrics to track**
For performance evaluation over time, track:

  :::{list-table}

    * - **Daily**
      -
        - Average shift PPM
        - Total number of picked parts
        - Number of hopper activations
        - Total downtime and causes

    * - **Weekly**
      -
        - PPM trend, increasing or decreasing
        - Comparison between theoretical and actual PPM
        - Average score of detected components
        - Configuration changes and their impact

    * - **Monthly**
      -
        - Overall Equipment Effectiveness, OEE
        - Analysis of the main bottlenecks
        - Need for predictive maintenance
        - System ROI
  :::

This data supports continuous optimization and justifies investment in improvements.
```

---

```{tip}
**System fully operational**

The FlexiVision One system is now fully configured, optimized, and validated for production.

**Completed path summary**
- ✓ hardware setup, FlexiBowl, Robot, Camera
- ✓ complete calibration, Camera and Robot
- ✓ part models created and optimized
- ✓ FlexiBowl configured for optimal movement
- ✓ Hopper configured for automatic feeding, if present
- ✓ system validated through Dashboard monitoring
- ✓ performance verified and stable

The system is ready to operate in production with minimal supervision. Use the Dashboard for continuous monitoring and long-term optimization.

**Total time invested**: 4-8 hours, first complete system

**Result**: fully autonomous and optimized robotic picking system
```

---

Once the system has been validated through the Dashboard:

**-> [Troubleshooting](../TROUBLESHOOTING/26_trb_shooting_guide.md)** - guide to solving common issues

**-> [Support](../27_Support.md)** - technical support contacts



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
