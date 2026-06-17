# **3 FlexiBowl® and 3 Cameras**

This section describes the available configurations when operating with **three FlexiBowl® units** and **three cameras** inside the same picking cell, managed by a single FlexiVision One VisionController.

---

## Configuration overview

In a **3 FlexiBowl® + 3 Cameras** configuration, the system includes three independent feeding and vision stations, all managed by the same VisionController. Each station consists of:

* 1 FlexiBowl®
* 1 camera with dedicated optics
* 1 hopper, optional if present

The three stations communicate with the VisionController through a **network switch**.

```{important}
The **switch** is a **mandatory** component in all multi-device configurations. Without it, it is not possible to connect multiple FlexiBowl® units and multiple cameras to the VisionController at the same time. For technical specifications and order codes, refer to [Switch](../rif_tecnico_specifiche/08_Opzioni.md#switch).
```

This configuration supports three operating variants depending on the number of robots available in the plant:

| | **Variant A** | **Variant B** | **Variant C** |
|---|---|---|---|
| **Robots** | 1 | 2 | 3 |
| **FlexiBowl®** | 3 | 3 | 3 |
| **Cameras** | 3 | 3 | 3 |
| **Operating logic** | The robot reaches all three stations | First robot works on one FlexiBowl, second robot works on two FlexiBowl units | Each robot is dedicated to one station |
| **Switch required** | Yes | Yes | Yes |

---

## Variant A - 1 Robot, 3 FlexiBowl®

![3FB3CAM1Robot system overview](../../../../_shared/media/images/3FB3CAM1R.png)

A **single robot** operates on all three stations. The robot must be positioned so that it can reach the picking area of each FlexiBowl®. The VisionController manages the three stations independently, each with its own recipe and TCP/IP communication channel.

Each station supports both **Standard** and **Mix** applications.

| Parameter | Value |
|---|---|
| FlexiBowl® | 3 |
| Cameras | 3 |
| Robots | 1 |
| Switch required | **Yes** |

```{important}
**Base recipe and recipe management**

As in the single-station configuration, even in a 3FB + 3CAM setup the process starts from a single **base recipe** containing the hardware setup and camera calibration for the entire system. This base recipe is then **duplicated** for each station. Each duplicate becomes the operating recipe of that station, inside which the part models are created, up to 8 per station.

For this reason, it is essential that device association is configured correctly from the start:

* **Camera 1** -> FlexiBowl® 1, plus Hopper 1 if present
* **Camera 2** -> FlexiBowl® 2, plus Hopper 2 if present
* **Camera 3** -> FlexiBowl® 3, plus Hopper 3 if present

An incorrect association during setup affects all derived recipes, compromising part recognition and the correct operation of the whole system.
```

---

## Variant B - 2 Robots, 3 FlexiBowl®

![3FB3CAM2Robot system overview](../../../../_shared/media/images/3FB3CAM2R.png)

In this variant, **two robots** share the three stations. The first robot performs picking on one FlexiBowl, while the second robot works on the other two FlexiBowl units. The workload distribution between the robots is defined by the robot program logic and the physical plant layout.

Each station supports both **Standard** and **Mix** applications.

| Parameter | Value |
|---|---|
| FlexiBowl® | 3 |
| Cameras | 3 |
| Robots | 2 |
| Switch required | **Yes** |

```{important}
**Base recipe and recipe management**

As in the single-station configuration, even in a 3FB + 3CAM setup the process starts from a single **base recipe** containing the hardware setup and camera calibration for the entire system. This base recipe is then **duplicated** for each station. Each duplicate becomes the operating recipe of that station, inside which the part models are created, up to 8 per station.

For this reason, it is essential that device association is configured correctly from the start:

* **Camera 1** -> FlexiBowl® 1, plus Hopper 1 if present
* **Camera 2** -> FlexiBowl® 2, plus Hopper 2 if present
* **Camera 3** -> FlexiBowl® 3, plus Hopper 3 if present

An incorrect association during setup affects all derived recipes, compromising part recognition and the correct operation of the whole system.
```

---

## Variant C - 3 Robots, 3 FlexiBowl®

![3FB3CAM3Robot system overview](../../../../_shared/media/images/3FB3CAM3R.png)

Each robot is dedicated to one single station, providing maximum productivity, with the three cells operating in parallel and completely independently.

Each station supports both **Standard** and **Mix** applications.

| Parameter | Value |
|---|---|
| FlexiBowl® | 3 |
| Cameras | 3 |
| Robots | 3 |
| Switch required | **Yes** |

```{tip}
Variant C guarantees the best overall performance. Each cell is completely autonomous and does not depend on the availability of the others.
```

```{important}
**Base recipe and recipe management**

As in the single-station configuration, even in a 3FB + 3CAM setup the process starts from a single **base recipe** containing the hardware setup and camera calibration for the entire system. This base recipe is then **duplicated** for each station. Each duplicate becomes the operating recipe of that station, inside which the part models are created, up to 8 per station.

For this reason, it is essential that device association is configured correctly from the start:

* **Camera 1** -> FlexiBowl® 1, plus Hopper 1 if present
* **Camera 2** -> FlexiBowl® 2, plus Hopper 2 if present
* **Camera 3** -> FlexiBowl® 3, plus Hopper 3 if present

An incorrect association during setup affects all derived recipes, compromising part recognition and the correct operation of the whole system.
```

---

## Required components

### FlexiVision One base kit

The **FlexiVision One base kit**, supplied with the system, already includes everything required for the **first station**, including the VisionController, camera, optics, cables, and calibration grid. It is not necessary to purchase a second complete kit for the additional stations.

### Additional Camera Kit, quantity 2

For stations 2 and 3 it is necessary to purchase **two Additional Camera Kits**, one for each station, selecting the code corresponding to the FlexiBowl® size of each station. The kit includes:

* 1 camera
* 1 optic dedicated to the FlexiBowl® size
* 1 calibration grid
* 1 camera power cable
* 2 Ethernet cables

Select the kit according to the FlexiBowl® size of each additional station:

| FlexiBowl® size | Additional Camera Kit code | Included optic |
|---|---|---|
| FB 200 | GM002002 | CE000881 - FlexiVision One 35 mm optic |
| FB 350 | GM002003 | CE000881 - FlexiVision One 35 mm optic |
| FB 500 | GM002004 | CE000880 - FlexiVision One 25 mm optic |
| FB 650 | GM002005 | CE000879 - FlexiVision One 16 mm optic |
| FB 800 | GM002006 | CE000879 - FlexiVision One 16 mm optic |
| FB 1200 | GM002007 | CE000878 - FlexiVision One 12 mm optic |

```{note}
If the additional stations use FlexiBowl® units of different sizes, purchase one kit for each required size.  
For example, with a configuration FB500 + FB650 + FB800, the base kit covers the first station, while the second and third stations require GM002005 and GM002006 respectively, according to the size installed on those stations.
```

### Switch

The switch is always required in multi-device configurations. For code, electrical specifications, and physical specifications, refer to:

**-> [Switch](../rif_tecnico_specifiche/08_Opzioni.md#switch)**

---

## Wiring

In **Variant A**, meaning 1 robot, all field devices, meaning FlexiBowl® units, cameras, and robot, connect to the **switch**, and the switch connects to the **VisionController** through a single Ethernet port. The total number of connections fits within the 8 available switch ports.

From **Variant B** onward, the total number of devices exceeds the ports available on the switch.  
In these cases, one VisionController port is used to connect it to the switch, while the remaining free VisionController ports are used for the devices that cannot fit on the switch:

- In **Variant B**, 2 robots, **FlexiBowl® 3** connects directly to a free VisionController port
- In **Variant C**, 3 robots, **FlexiBowl® 3** and **Camera 3** connect directly to the free VisionController ports

```{important}
The switch provides **8 Ethernet ports**. Starting from Variant B, it is no longer possible to connect all devices only through the switch. The extra devices must be connected directly to the free Ethernet ports on the VisionController, as indicated in the tables below.
```

:::{note}
You may choose arbitrarily which devices connect directly to the VisionController. The important point is to always keep one free port available for the connection between VisionController and switch.
:::

### Connection scheme

| Device | Variant A, 1 Robot | Variant B, 2 Robots | Variant C, 3 Robots |
|---|---|---|---|
| FlexiBowl® 1 | -> Switch | -> Switch | -> Switch |
| FlexiBowl® 2 | -> Switch | -> Switch | -> Switch |
| FlexiBowl® 3 | -> Switch | **-> VisionController, free port** | **-> VisionController, free port** |
| Camera 1 | -> Switch | -> Switch | -> Switch |
| Camera 2 | -> Switch | -> Switch | -> Switch |
| Camera 3 | -> Switch | -> Switch | **-> VisionController, free port** |
| Robot 1 | -> Switch | -> Switch | -> Switch |
| Robot 2 | — | -> Switch | -> Switch |
| Robot 3 | — | — | -> Switch |
| **Switch** | **-> VisionController** | **-> VisionController** | **-> VisionController** |

:::{note}
You may choose arbitrarily which devices connect directly to the VisionController. The important point is to always keep one free port available for the connection between VisionController and switch.
:::

```{tip}
Verify that each device is assigned a unique IP address in the same subnet.  
The TCP/IP ports used by the VisionController for the three stations are configurable. By default they are **FB1 -> 4001**, **FB2 -> 4002**, and **FB3 -> 4003**. Refer to [Robot-Vision Communication Protocol](../rif_tecnico_specifiche/04b_Protocolli_Comunicazione.md) for details.
```

### Switch ports used by variant

| Switch port | Variant A, 1 Robot | Variant B, 2 Robots | Variant C, 3 Robots |
|---|---|---|---|
| 1 | FlexiBowl® 1 | FlexiBowl® 1 | FlexiBowl® 1 |
| 2 | FlexiBowl® 2 | FlexiBowl® 2 | FlexiBowl® 2 |
| 3 | FlexiBowl® 3 | Camera 1 | Camera 1 |
| 4 | Camera 1 | Camera 2 | Camera 2 |
| 5 | Camera 2 | Camera 3 | Robot 1 |
| 6 | Camera 3 | Robot 1 | Robot 2 |
| 7 | Robot 1 | Robot 2 | Robot 3 |
| 8 | VisionController | VisionController | VisionController |

### VisionController ports used by variant

| VisionController port | Variant A, 1 Robot | Variant B, 2 Robots | Variant C, 3 Robots |
|---|---|---|---|
| 1 | Switch | Switch | Switch |
| 2 | — | FlexiBowl® 3 | FlexiBowl® 3 |
| 3 | — | — | Camera 3 |

:::{note}
You may choose arbitrarily which devices connect directly to the VisionController. The important point is to always keep one free port available for the connection between VisionController and switch.
:::

```{note}
In **Variant B**, the switch ports are all occupied, meaning 7 field devices plus the VisionController, so **FlexiBowl® 3** connects directly to the VisionController. In **Variant C**, **Camera 3** also connects directly to the VisionController, occupying the third available port.
```

```{note}
**Wiring of the individual components**

The physical connection procedures for each component, meaning FlexiBowl®, camera, hopper, and robot, are fully described in [Wiring and Connections](../INSTALLAZIONE_SISTEMA/10_Cablaggio_Connessioni.md).  
In a 3FB + 3CAM configuration, the same operations simply need to be performed **three times**, once for each station, with the only difference that each device connects to the **switch** instead of directly to the VisionController, except for **FlexiBowl® 3** in Variant B and Variant C, and **Camera 3** in Variant C, which connect directly to the free Ethernet ports on the VisionController.
```

```{important}
**Device association in the software**

FlexiVision One is able to manage all stations simultaneously, but it is essential that the association between devices is configured correctly in the software. Make sure to associate:

* **Camera 1** -> FlexiBowl® 1, plus Hopper 1 if present
* **Camera 2** -> FlexiBowl® 2, plus Hopper 2 if present
* **Camera 3** -> FlexiBowl® 3, plus Hopper 3 if present

An incorrect association would compromise part localization and the correct operation of the whole system.
```

**-> [Initial System Configuration](../QUICKSTART/SETUP/13_setup.md)**



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
