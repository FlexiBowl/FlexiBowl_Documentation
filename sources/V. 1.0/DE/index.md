# **FlexiBowl Handbuch**

## **Willkommen im FlexiBowl®-Handbuch!**  
Wir freuen uns, Sie zu Ihrem neuen FlexiBowl®-Leitfaden willkommen zu heißen!
Dieses Handbuch wurde eigens als Ihre klare und zuverlässige Referenz erstellt. Wir hoffen, dass Sie durch dessen Konsultation alle Vorteile unseres Systems voll ausschöpfen können.
Ihr Feedback ist für uns von grundlegender Bedeutung: Zögern Sie nicht, uns Ihre Meinung mitzuteilen, indem Sie uns [kontaktieren](https://www.arsautomation.com/contact)!

*- Das ARS Automation Team*    
<a href="https://www.arsautomation.com" target="_blank">
  <img src="../../_shared/static/logo_fv.png" alt="Ars logo" class="only-light img-logo">
  <img src="../../_shared/static/logo_fv_black.png" alt="Ars logo" class="only-dark img-logo">
</a>
  
## **Was ist der FlexiBowl?**  
Der FlexiBowl® ist ein flexibles Zuführsystem mit rotierender oder vibrierender Scheibe zur zufälligen Positionierung und Ausrichtung von Bauteilen für die Robotergreifung.

## **Systemübersicht** 
Der Arbeitsbereich des FlexiBowl® ist virtuell in vier Bereiche unterteilt, von denen jeder einer Phase des Arbeitszyklus gewidmet ist:

:::{list-table}
:widths: 20 50
:header-rows: 1

* - Phase
  - Beschreibung

* - **Übergabe**
  - Eine Zuführeinheit lädt die Bauteile auf den Arbeitsbereich des FlexiBowl®.

* - **Vereinzelung**
  - Eine kombinierte Aktion der {ref}`Flip-Einheit <panoramica>` und der Bewegung der Oberfläche oder Hartscheibe vereinzelt die Bauteile und wendet sie, sodass sich stets mindestens eines in der richtigen Greifposition befindet.

* - **Entnahme**
  - Das Bildverarbeitungssystem erkennt greifbare Bauteile und übermittelt deren Koordinaten an den Roboter, der anschließend die Pick-and-Place-Vorgänge durchführt.

* - **Rückführung**
  - Nicht entnommene Bauteile beginnen ihren Weg im FlexiBowl® erneut, bis sie vom Roboter gegriffen werden.

:::

:::{figure} ../../_shared/media/images/Funz-standard.PNG
:align: center
:width: 50%

Schematische Darstellung des FlexiBowl®-Systems im Standardbetrieb.
:::

:::{note}
Der {ref}`Flexitracking <tracking>`-Zyklus ist dem herkömmlichen Zyklus im Wesentlichen gleich, mit dem Unterschied, dass alle Phasen gleichzeitig und kontinuierlich ablaufen.
:::


## **So lesen Sie das Handbuch**  
Dieses Handbuch wurde entwickelt, um sowohl die Projektierungs- und Systemintegrationsphase als auch die Installation und Inbetriebnahme vor Ort zu unterstützen.
Aus diesem Grund ist es in Makro-Abschnitte mit unterschiedlichen Zielgruppen und Zielsetzungen unterteilt.
  
## **Welchen Abschnitt suchen Sie?**  
```{list-table}
:widths: 40 60
:header-rows: 1

* - Wenn Sie...
  - Die Information befindet sich in...

* - Maße, Gewichte, elektrische Anforderungen und Kommunikationsprotokolle prüfen möchten
  - [**TECHNISCHE REFERENZ UND SPEZIFIKATIONEN**](specifiche_tecniche)

* - Komponenten installieren, das System verkabeln, das Netzwerk konfigurieren oder Kamera/Roboter kalibrieren möchten
  - [**SYSTEMINSTALLATION**](Installazione_Meccanica) und [**QUICKSTART**](quickstart)

* - Ein neues Bauteilmodell programmieren oder das Zuführsystem konfigurieren möchten
  - [**QUICKSTART**](quickstart)

* - Probleme beheben oder Unterstützung anfordern möchten
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
    Warnung
    ```
  - Weist auf eine potenziell gefährliche Situation oder einen kritischen Vorgang hin, der bei falscher Ausführung zu Geräteschäden oder schwerwiegenden Systemstörungen führen könnte.

* - ```{important}
    Wichtig
    ```
  - Hebt grundlegende Informationen hervor, die nicht ignoriert werden dürfen, um den ordnungsgemäßen Betrieb des Systems oder die Sicherheit des Vorgangs zu gewährleisten.

* - ```{note}
    Hinweis
    ```
  - Liefert wesentliche Informationen für die korrekte Durchführung des Verfahrens, technische Erläuterungen oder Verweise auf verwandte Kapitel.

* - ```{tip}
    Tipp
    ```
  - Empfiehlt eine bewährte Vorgehensweise, eine Alternative oder einen Ratschlag, der die Installation vereinfachen oder die Systemleistung verbessern kann.

* - ```{error}
    Fehler
    ```
  - Weist auf einen kritischen Fehler oder eine Störungsbedingung hin, die sofortiges Eingreifen erfordert. Zeigt Situationen an, die den Systembetrieb beeinträchtigen und Korrekturmaßnahmen erfordern.
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
:caption: BETRIEBSMODI 
FlexiBowl_manual/MODALITA FUNZIONAMENTO/modalita_standard.md
FlexiBowl_manual/MODALITA FUNZIONAMENTO/modalita_mix.md
FlexiBowl_manual/MODALITA FUNZIONAMENTO/modalita_tracking.md
:::

:::{toctree}  
:hidden:
:caption: PLUG-INS 
FlexiBowl_manual/PLUG-IN/01_PlugIn.md
:::

:::{toctree}
:hidden:
:caption: LAYOUT BEST PRACTICES
FlexiBowl_manual/LAYOUT BEST PRACTICE/01_layoutbp.md
:::

:::{toctree}
:hidden:
:caption: ZUBEHÖR
FlexiBowl_manual/ACCESSORI/00_ACCESSORI.md
FlexiBowl_manual/ACCESSORI/01_SUPERFICI.md
FlexiBowl_manual/ACCESSORI/03_04_illuminazione.md
FlexiBowl_manual/ACCESSORI/05_DEVIATORE.md
FlexiBowl_manual/ACCESSORI/06_SOFFI.md
FlexiBowl_manual/ACCESSORI/07_BRUSH_DIVERTER.md
FlexiBowl_manual/ACCESSORI/08_WEDGE.md
FlexiBowl_manual/ACCESSORI/09_SVUOTAMENTO.md
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

:::{toctree}  
:hidden:
:caption: FEHLERBEHEBUNG
FlexiBowl_manual/TROUBLESHOOTING/01_risoluzione-problemi.md
FlexiBowl_manual/TROUBLESHOOTING/02_problemi_meccanici.md
FlexiBowl_manual/TROUBLESHOOTING/03_problemi_elettrici.md
FlexiBowl_manual/TROUBLESHOOTING/04_problemi_pneumatici.md
FlexiBowl_manual/TROUBLESHOOTING/05_problemi_software.md
:::

:::{toctree}  
:hidden:
:caption: ENTSORGUNG
FlexiBowl_manual/SMALTIMENTO/smaltimento.md
:::

:::{toctree}  
:hidden:
:caption: ZERTIFIZIERUNGEN 
FlexiBowl_manual/CERTIFICAZIONI/01_certificazioni.md
:::

:::{toctree}  
:hidden:
:caption: ZUFÜHREINHEITEN
FlexiBowl_manual/TRAMOGGE/TRAMOGGE VIBRANTI/tramogge_vibranti.md
FlexiBowl_manual/TRAMOGGE/TRAMOGGE A NASTRO/tramogge_nastro.md

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




