# **FlexiBowl Manual**

## **Welcome to the FlexiBowl® manual!**  
We are delighted to welcome you to your new FlexiBowl® guide! This manual has been created specifically to be your clear and reliable point of reference. We hope that, by consulting it, you will be able to fully enjoy all the benefits of our system. Your opinion is essential to us: do not hesitate to give us your feedback by [contacting us](https://www.arsautomation.com/contact)!

*- The Ars Automation Team*
<a href="https://www.arsautomation.com" target="_blank">
  <img src="../../_shared/static/logo_fv.png" alt="ARS logo" class="only-light img-logo">
  <img src="../../_shared/static/logo_fv_black.png" alt="ARS logo" class="only-dark img-logo">
</a>
  
## **What is FlexiBowl?**  
The FlexiBowl® is a flexible rotating-disc feeding system for the positioning and orientation of components for robotic picking.

![Family](../../_shared/media/images/famiglia.png)

## **System overview** 
The working area of the FlexiBowl® is virtually divided into four parts, each dedicated to a phase of the working cycle:

:::{list-table}
:widths: 20 50
:header-rows: 1

* - Phase
  - Description

* - **Release**
  - A hopper discharges the components onto the working area of the FlexiBowl®.

* - **Separation**
  - A combined action of the {ref}`flip unit <panoramica>` and of the movement of the surface or rigid disc separates the components and turns them over, so that at least one is always in the right position for picking.

* - **Picking**
  - The vision system recognises the pickable parts and sends their coordinates to the robot, which proceeds with the pick and place operations.

* - **Recirculation**
  - Components that are not picked start their path again in the FlexiBowl® until they are picked by the robot.

:::

:::{figure} ../../_shared/media/images/Funz-standard.PNG
:align: center
:width: 50%

Example diagram of the FlexiBowl® system in standard operation.
:::

:::{note}
The {ref}`Circular Tracking <tracking>` cycle is substantially the same as the traditional one, with the difference that all the phases take place simultaneously and continuously.
:::


## **How to read the manual**  
This manual has been designed to support both the system design and integration phase and the on-site installation and commissioning phase. For this reason, it is divided into macro-sections with distinct audiences and purposes.
  
## **Which section are you looking for?**  
```{list-table}
:widths: 40 60
:header-rows: 1

* - If you need to...
  - The information is found in...

* - Check dimensions, weights, electrical requirements and communication protocols
  - [**TECHNICAL REFERENCE AND SPECIFICATIONS**](specifiche_tecniche)

* - Install the components, wire the system, configure the network or calibrate the camera/robot
  - [**SYSTEM INSTALLATION**](Installazione_Meccanica) and [**QUICKSTART**](quickstart)

* - Program a new part model or configure the feeding system
  - [**QUICKSTART**](quickstart)

* - Solve problems or request assistance
  - [**TROUBLESHOOTING**](troubleshooting) and [**SUPPORT**](support)
```

## **Conventions and symbols used**

Throughout the manual, information banners are used to highlight important content:

```{list-table}
:widths: 20 80
:header-rows: 1

* - Type
  - Meaning

* - ```{warning}
    Warning
    ```
  - Indicates a potentially hazardous situation or a critical procedure that, if not performed correctly, could cause damage to the equipment or serious malfunctions of the system.

* - ```{important}
    Important
    ```
  - Highlights fundamental information that must not be ignored in order to ensure the correct operation of the system or the safety of the operation.

* - ```{note}
    Information note
    ```
  - Provides essential information for the correct execution of the procedure, technical clarifications or references to related chapters.

* - ```{tip}
    Tip
    ```
  - Suggests an optimal practice, an alternative or a piece of advice that can simplify the installation or improve system performance.

* - ```{error}
    Error
    ```
  - Indicates a critical error or a fault condition that requires immediate intervention. Signals situations that compromise the operation of the system and require corrective action.
```


:::{toctree}
:hidden:
:caption: BEFORE YOU START 
FlexiBowl_manual/PRIMA DI INIZIARE/01_informazioni_preliminari.md
FlexiBowl_manual/PRIMA DI INIZIARE/02_informazioni_sicurezza.md
FlexiBowl_manual/PRIMA DI INIZIARE/03_trasporto.md
FlexiBowl_manual/PRIMA DI INIZIARE/04_cond-util.md
FlexiBowl_manual/PRIMA DI INIZIARE/05_glossario.md
FlexiBowl_manual/PRIMA DI INIZIARE/06_support.md
FlexiBowl_manual/PRIMA DI INIZIARE/07_garanzia.md
:::
  
:::{toctree}
:hidden:
:caption: TECHNICAL DATA
FlexiBowl_manual/DATI TECNICI/01_panoramica.md
FlexiBowl_manual/DATI TECNICI/02_dati-tecnici-meccanici.md
FlexiBowl_manual/DATI TECNICI/03_dati-tecnici-elettrici.md
FlexiBowl_manual/DATI TECNICI/04_dati-tecnici-pneumatici.md
FlexiBowl_manual/DATI TECNICI/05_dati-tecnici-applicativi.md
:::

:::{toctree}
:hidden:
:caption: INSTALLATION
FlexiBowl_manual/INSTALLAZIONE/01_interfaccia-meccanica.md
FlexiBowl_manual/INSTALLAZIONE/02_interfaccia-elettrica.md
FlexiBowl_manual/INSTALLAZIONE/03_interfaccia-pneumatica.md
FlexiBowl_manual/INSTALLAZIONE/04_interfaccia-software.md
:::

:::{toctree}
:hidden:
:caption: SOFTWARE OVERVIEW
FlexiBowl_manual/INTERFACCIA SOFTWARE/04_home.md
FlexiBowl_manual/INTERFACCIA SOFTWARE/04b_maincommand.md
FlexiBowl_manual/INTERFACCIA SOFTWARE/04c_sequence.md
FlexiBowl_manual/INTERFACCIA SOFTWARE/04d_monitor.md
FlexiBowl_manual/INTERFACCIA SOFTWARE/04e_jogmotor.md
FlexiBowl_manual/INTERFACCIA SOFTWARE/04f_wizard.md
FlexiBowl_manual/INTERFACCIA SOFTWARE/04h_graphs.md
FlexiBowl_manual/INTERFACCIA SOFTWARE/04i_filetransfer.md
FlexiBowl_manual/INTERFACCIA SOFTWARE/04l_setup.md
FlexiBowl_manual/INTERFACCIA SOFTWARE/04m_hopper.md
FlexiBowl_manual/INTERFACCIA SOFTWARE/04n_emptying.md
:::

:::{toctree}  
:hidden:
:caption: QUICKSTART
FlexiBowl_manual/QUICKSTART/panoramica.md
FlexiBowl_manual/QUICKSTART/installazione_meccanica.md
FlexiBowl_manual/QUICKSTART/cablaggio_FB.md
FlexiBowl_manual/QUICKSTART/conf_interfaccia.md
FlexiBowl_manual/QUICKSTART/FB_wizard.md
FlexiBowl_manual/QUICKSTART/conf_tramoggia.md
:::

:::{toctree}  
:hidden:
:caption: OPERATING MODES 
FlexiBowl_manual/MODALITA FUNZIONAMENTO/modalita_standard.md
FlexiBowl_manual/MODALITA FUNZIONAMENTO/modalita_mix.md
FlexiBowl_manual/MODALITA FUNZIONAMENTO/modalita_tracking.md
:::

:::{toctree}  
:hidden:
:caption: PLUG-IN 
FlexiBowl_manual/PLUG-IN/01_PlugIn.md
:::

<!--
:::{toctree}
:hidden:
:caption: LAYOUT BEST PRACTICE
FlexiBowl_manual/LAYOUT BEST PRACTICE/01_layoutbp.md
:::
--> 

:::{toctree}
:hidden:
:caption: ACCESSORIES
FlexiBowl_manual/ACCESSORI/00_ACCESSORI.md
FlexiBowl_manual/ACCESSORI/01_SUPERFICI.md
FlexiBowl_manual/ACCESSORI/02_DISCHI_RIGIDI.md
FlexiBowl_manual/ACCESSORI/03_04_illuminazione.md
FlexiBowl_manual/ACCESSORI/05_DEVIATORE.md
FlexiBowl_manual/ACCESSORI/06_SOFFI.md
FlexiBowl_manual/ACCESSORI/07_BRUSH_DIVERTER.md
FlexiBowl_manual/ACCESSORI/08_WEDGE.md
FlexiBowl_manual/ACCESSORI/09_SVUOTAMENTO.md
FlexiBowl_manual/ACCESSORI/11_CAVI.md
FlexiBowl_manual/ACCESSORI/12_KIT_FILTRAGGIO.md
:::

:::{toctree}  
:hidden:
:caption: MAINTENANCE 
FlexiBowl_manual/MANUTENZIONE/01_ordinaria.md
FlexiBowl_manual/MANUTENZIONE/02_straordinaria.md
:::

:::{toctree}  
:hidden:
:caption: WARRANTY 
FlexiBowl_manual/Garanzia.md
:::

<!--  
:::{toctree}  
:hidden:
:caption: TROUBLESHOOTING
FlexiBowl_manual/TROUBLESHOOTING/01_risoluzione-problemi.md
FlexiBowl_manual/TROUBLESHOOTING/02_problemi_meccanici.md
FlexiBowl_manual/TROUBLESHOOTING/03_problemi_elettrici.md
FlexiBowl_manual/TROUBLESHOOTING/04_problemi_pneumatici.md
FlexiBowl_manual/TROUBLESHOOTING/05_problemi_software.md
:::
-->

:::{toctree}  
:hidden:
:caption: DISPOSAL
FlexiBowl_manual/SMALTIMENTO/smaltimento.md
:::

<!-- 
:::{toctree}  
:hidden:
:caption: CERTIFICAZIONI 
FlexiBowl_manual/CERTIFICAZIONI/01_certificazioni.md
:::
-->

:::{toctree}  
:hidden:
:caption: HOPPERS
FlexiBowl_manual/TRAMOGGE/TRAMOGGE VIBRANTI/tramogge_vibranti.md
<!--FlexiBowl_manual/TRAMOGGE/MOTORIZZATE/00_MOTORIZZATE.md
FlexiBowl_manual/TRAMOGGE/CONVEYOR/00_CONVEYOR.md--->
:::

:::{toctree}
:hidden:
:caption: APPENDICES
FlexiBowl_manual/NOTE RILASCIO/release_notes.md
:::

:::{toctree}
:hidden:
:caption: FLEXIBOWL 2.0 VS FLEXIBOWL 3.0
FlexiBowl_manual/COMPARATIVA/panoramica.md
FlexiBowl_manual/COMPARATIVA/comparativa_meccanica.md
FlexiBowl_manual/COMPARATIVA/comparativa_elettrica.md
FlexiBowl_manual/COMPARATIVA/comparativa_pneumatica.md
FlexiBowl_manual/COMPARATIVA/comparativa_software.md
:::