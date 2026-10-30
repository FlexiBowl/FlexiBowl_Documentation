# **FlexiBowl-Handbuch**

## **Willkommen im FlexiBowl®-Handbuch!**  
Wir freuen uns, Sie zu Ihrem neuen FlexiBowl®-Leitfaden willkommen zu heißen! Dieses Handbuch wurde eigens dafür erstellt, Ihr klarer und verlässlicher Anlaufpunkt zu sein. Wir hoffen, dass Sie mit seiner Hilfe alle Vorteile unseres Systems voll nutzen können. Ihre Meinung ist uns sehr wichtig: Zögern Sie nicht, uns Ihr Feedback zu geben, indem Sie [uns kontaktieren](https://www.arsautomation.com/contact)!

*- Das Team von Ars Automation*
<a href="https://www.arsautomation.com" target="_blank">
  <img src="../../_shared/static/logo_fv.png" alt="ARS-Logo" class="only-light img-logo">
  <img src="../../_shared/static/logo_fv_black.png" alt="ARS-Logo" class="only-dark img-logo">
</a>
  
## **Was ist FlexiBowl?**  
Der FlexiBowl® ist ein flexibles Zuführsystem mit rotierender Scheibe zur Positionierung und Ausrichtung von Bauteilen für das robotergestützte Greifen.

![Produktfamilie](../../_shared/media/images/famiglia.png)

## **Systemübersicht** 
Der Arbeitsbereich des FlexiBowl® ist virtuell in vier Teile unterteilt, die jeweils einer Phase des Arbeitszyklus zugeordnet sind:

:::{list-table}
:widths: 20 50
:header-rows: 1

* - Phase
  - Beschreibung

* - **Abgabe**
  - Ein Hopper gibt die Bauteile auf den Arbeitsbereich des FlexiBowl® ab.

* - **Vereinzelung**
  - Ein kombiniertes Zusammenwirken der {ref}`Flip-Einheit <panoramica>` und der Bewegung der Oberfläche bzw. der starren Scheibe vereinzelt die Bauteile und wendet sie, sodass stets mindestens eines in der richtigen Position zum Greifen liegt.

* - **Greifen**
  - Das Bildverarbeitungssystem erkennt die greifbaren Teile und sendet deren Koordinaten an den Roboter, der die Pick-and-Place-Vorgänge ausführt.

* - **Rückführung**
  - Nicht gegriffene Bauteile beginnen ihren Weg im FlexiBowl® erneut, bis sie vom Roboter gegriffen werden.

:::

:::{figure} ../../_shared/media/images/Funz-standard.PNG
:align: center
:width: 50%

Beispielschema des FlexiBowl®-Systems im Standardbetrieb.
:::

:::{note}
Der Zyklus {ref}`Circular Tracking <tracking>` entspricht im Wesentlichen dem herkömmlichen, mit dem Unterschied, dass alle Phasen gleichzeitig und fortlaufend stattfinden.
:::


## **So lesen Sie das Handbuch**  
Dieses Handbuch wurde konzipiert, um sowohl die Phase der Systemplanung und -integration als auch die Phase der Installation und Inbetriebnahme vor Ort zu unterstützen. Aus diesem Grund ist es in Hauptabschnitte mit unterschiedlichen Zielgruppen und Zwecken gegliedert.
  
## **Welchen Abschnitt suchen Sie?**  
```{list-table}
:widths: 40 60
:header-rows: 1

* - Wenn Sie ...
  - Die Informationen finden Sie in ...

* - Abmessungen, Gewichte, elektrische Anforderungen und Kommunikationsprotokolle prüfen möchten
  - [**TECHNISCHE REFERENZ UND SPEZIFIKATIONEN**](specifiche_tecniche)

* - die Komponenten installieren, das System verdrahten, das Netzwerk konfigurieren oder Kamera/Roboter kalibrieren möchten
  - [**SYSTEMINSTALLATION**](Installazione_Meccanica) und [**QUICKSTART**](quickstart)

* - ein neues Teilemodell programmieren oder das Zuführsystem konfigurieren möchten
  - [**QUICKSTART**](quickstart)

* - Probleme lösen oder Unterstützung anfordern möchten
  - [**FEHLERBEHEBUNG**](troubleshooting) und [**SUPPORT**](support)
```

## **Verwendete Konventionen und Symbole**

Im gesamten Handbuch werden Informationsbanner verwendet, um wichtige Inhalte hervorzuheben:

```{list-table}
:widths: 20 80
:header-rows: 1

* - Typ
  - Bedeutung

* - ```{warning}
    Warnhinweis
    ```
  - Weist auf eine potenziell gefährliche Situation oder ein kritisches Verfahren hin, das bei nicht korrekter Ausführung zu Schäden an der Ausrüstung oder zu schwerwiegenden Fehlfunktionen des Systems führen könnte.

* - ```{important}
    Wichtig
    ```
  - Hebt grundlegende Informationen hervor, die nicht ignoriert werden dürfen, um den korrekten Betrieb des Systems oder die Sicherheit des Vorgangs zu gewährleisten.

* - ```{note}
    Informationshinweis
    ```
  - Liefert wesentliche Informationen für die korrekte Durchführung des Verfahrens, technische Erläuterungen oder Verweise auf zugehörige Kapitel.

* - ```{tip}
    Tipp
    ```
  - Schlägt eine optimale Vorgehensweise, eine Alternative oder einen Rat vor, der die Installation vereinfachen oder die Systemleistung verbessern kann.

* - ```{error}
    Fehler
    ```
  - Weist auf einen kritischen Fehler oder einen Störungszustand hin, der sofortiges Eingreifen erfordert. Signalisiert Situationen, die den Betrieb des Systems beeinträchtigen und Abhilfemaßnahmen erfordern.
```


:::{toctree}
:hidden:
:caption: VOR DEM START 
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
:caption: TECHNISCHE DATEN
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
:caption: SOFTWARE-ÜBERSICHT
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
:caption: BETRIEBSARTEN 
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
:caption: ZUBEHÖR
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
:caption: WARTUNG 
FlexiBowl_manual/MANUTENZIONE/01_ordinaria.md
FlexiBowl_manual/MANUTENZIONE/02_straordinaria.md
:::

:::{toctree}  
:hidden:
:caption: GARANTIE 
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
:caption: ENTSORGUNG
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
:caption: HOPPER
FlexiBowl_manual/TRAMOGGE/TRAMOGGE VIBRANTI/tramogge_vibranti.md
<!--FlexiBowl_manual/TRAMOGGE/MOTORIZZATE/00_MOTORIZZATE.md
FlexiBowl_manual/TRAMOGGE/CONVEYOR/00_CONVEYOR.md--->
:::

:::{toctree}
:hidden:
:caption: ANHÄNGE
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