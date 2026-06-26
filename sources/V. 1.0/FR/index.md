
# **Manuel FlexiBowl**

## **Bienvenue dans le manuel FlexiBowl® !**   
Nous sommes ravis de vous souhaiter la bienvenue dans votre nouveau guide FlexiBowl® !
Ce manuel a été spécialement conçu pour être votre point de référence clair et fiable. Nous espérons qu'en le consultant, vous pourrez profiter pleinement de tous les avantages de notre système.
Votre avis est essentiel pour nous : n'hésitez pas à nous faire part de vos commentaires en [nous contactant](https://www.arsautomation.com/contact) ! 

*- L'équipe d'Ars Automation*  

 <a href="https://www.arsautomation.com" target="_blank">
  <img src="../../_shared/static/logo_fv.png" alt="Ars logo" class="only-light img-logo">
  <img src="../../_shared/static/logo_fv_black.png" alt="Ars logo" class="only-dark img-logo">
</a>
  
## **Qu'est-ce que FlexiBowl ?**  
 Le FlexiBowl® est un système d'alimentation flexible à disque rotatif ou vibrant destiné au positionnement et à l'orientation aléatoire des composants pour le prélèvement robotique.

## **Présentation du système**  
 L'espace de travail du FlexiBowl® est virtuellement divisé en quatre parties, chacune dédiée à une phase du cycle de travail :

:::{list-table}
:widths: 20 50
:header-rows: 1

* - Phase
  - Description

* - **Alimentation**
  - Une trémie décharge iIes composants sur l'espace de travail du FlexiBowl®.

* - **Séparation**
  - Une action combinée du {ref}`groupe flip <panoramica>` et du mouvement de la surface ou du disque rigide sépare les composants et les retourne afin d'en avoir toujours au moins un dans la bonne position pour la saisie.

* - **Saisie**
  - Le système de vision reconnaît les pièces pouvant être saisies et envoie leurs coordonnées au robot, qui procède aux opérations de pick and place.

* - **Recirculation**
  - Les composants non saisis recommencent leur parcours dans le FlexiBowl® jusqu'à ce qu'ils soient saisis par le robot.

:::

:::{figure} ../../_shared/media/images/Funz-standard.PNG
:align: center
:width: 50%

Exemple de schéma du système FlexiBowl® en fonctionnement standard.
:::

:::{note}
Le cycle {ref}`Flexitracking <tracking>` est sensiblement identique au cycle traditionnel, à la différence que toutes les phases se déroulent simultanément et en continu.
:::

  
## **Comment lire le manuel**  
 Ce manuel a été conçu pour accompagner aussi bien la phase de conception et d'intégration du système que la phase d'installation et de mise en service sur le terrain. 
Pour cette raison, il est divisé en macro-sections ayant des destinataires et des objectifs distincts.
  
## **Quelle est la section que vous recherchez ?**  
 ```{list-table}
:widths: 40 60
:header-rows: 1

* - Si vous devez...
  - L'information se trouve dans...

* - Vérifier les dimensions, les poids, les exigences électriques et les protocoles de communication
  - [**RÉFÉRENCE TECHNIQUE ET SPÉCIFICATIONS**](specifiche_tecniche)

* - Installer les composants, câbler le système, configurer le réseau ou calibrer la caméra/le robot
  - [**INSTALLATION DU SYSTÈME**](Installazione_Meccanica) et [**QUICKSTART**](quickstart)

* - Programmer un nouveau modèle de pièce ou configurer le système d'alimentation
  - [**QUICKSTART**](quickstart)

* - Résoudre des problèmes ou demander de l'assistance
  - [**TROUBLESHOOTING**](troubleshooting) et [**SUPPORT**](support)
```

## **Conventions et symboles utilisés**

Tout au long du manuel, des bannières d'information sont utilisées pour mettre en évidence les contenus importants :

```{list-table}
:widths: 20 80
:header-rows: 1

* - Type
  - Signification

* - ```{warning}
    Avertissement
    ```
  - Indique une situation potentiellement dangereuse ou une procédure critique qui, si elle n'est pas correctement exécutée, pourrait provoquer des dommages à l'équipement ou de graves dysfonctionnements du système.

* - ```{important}
    Important
    ```
  - Met en évidence des informations fondamentales qui ne doivent pas être ignorées pour garantir le bon fonctionnement du système ou la sécurité de l'opération.

* - ```{note}
    Note informative
    ```
  - Fournit des informations essentielles pour le bon déroulement de la procédure, des clarifications techniques ou des renvois à des chapitres connexes.

* - ```{tip}
    Conseil
    ```
  - Suggère une pratique optimale, une alternative ou un conseil pouvant simplifier l'installation ou améliorer les performances du système.

* - ```{error}
    Erreur
    ```
  - Indique une erreur critique ou une condition de panne nécessitant une intervention immédiate. Signale des situations qui compromettent le fonctionnement du système et exigent une action corrective.
```







:::{toctree}
:hidden:
:caption: AVANT DE COMMENCER 
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
:caption: DONNÉES TECHNIQUES
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
:caption: PRÉSENTATION LOGICIEL
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
:caption: MODES DE FONCTIONNEMENT 
FlexiBowl_manual/MODALITA FUNZIONAMENTO/modalita_standard.md
FlexiBowl_manual/MODALITA FUNZIONAMENTO/modalita_mix.md
FlexiBowl_manual/MODALITA FUNZIONAMENTO/modalita_tracking.md
:::

:::{toctree}  
:hidden:
:caption: PLUG-IN 
FlexiBowl_manual/PLUG-IN/01_PlugIn.md
:::

:::{toctree}
:hidden:
:caption: BONNES PRATIQUES DE LAYOUT
FlexiBowl_manual/LAYOUT BEST PRACTICE/01_layoutbp.md
:::

:::{toctree}
:hidden:
:caption: ACCESSOIRES
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
:caption: MAINTENANCE 
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
:caption: DÉPANNAGE
FlexiBowl_manual/TROUBLESHOOTING/01_risoluzione-problemi.md
FlexiBowl_manual/TROUBLESHOOTING/02_problemi_meccanici.md
FlexiBowl_manual/TROUBLESHOOTING/03_problemi_elettrici.md
FlexiBowl_manual/TROUBLESHOOTING/04_problemi_pneumatici.md
FlexiBowl_manual/TROUBLESHOOTING/05_problemi_software.md
:::

:::{toctree}  
:hidden:
:caption: ÉLIMINATION
FlexiBowl_manual/SMALTIMENTO/smaltimento.md
:::

:::{toctree}  
:hidden:
:caption: CERTIFICATIONS 
FlexiBowl_manual/CERTIFICAZIONI/01_certificazioni.md
:::

:::{toctree}  
:hidden:
:caption: TRÉMIES
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

