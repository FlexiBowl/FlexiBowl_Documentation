# **Manual FlexiBowl**

## **¡Bienvenido al manual FlexiBowl®!**  
¡Estamos encantados de darle la bienvenida a su nueva guía de FlexiBowl®!
Este manual ha sido creado específicamente para ser su punto de referencia claro y fiable. Esperamos que, al consultarlo, pueda aprovechar al máximo todos los beneficios de nuestro sistema.
Su opinión es fundamental para nosotros: ¡no dude en enviarnos sus comentarios [contactándonos](https://www.arsautomation.com/contact)!

*- El equipo de Ars Automation*    
<a href="https://www.arsautomation.com" target="_blank">
  <img src="../../_shared/static/logo_fv.png" alt="Ars logo" class="only-light img-logo">
  <img src="../../_shared/static/logo_fv_black.png" alt="Ars logo" class="only-dark img-logo">
</a>
  
## **¿Qué es FlexiBowl?**  
El FlexiBowl® es un sistema de alimentación flexible de disco rotante o vibrante para el posicionamiento y orientación aleatoria de componentes con el fin de facilitar la recogida robótica.

## **Descripción general del sistema** 
El área de trabajo del FlexiBowl® está virtualmente dividida en cuatro partes, cada una dedicada a una fase del ciclo de trabajo:

:::{list-table}
:widths: 20 50
:header-rows: 1

* - Fase
  - Descripción

* - **Descarga**
  - Una tolva descarga los componentes sobre el área de trabajo del FlexiBowl®.

* - **Separación**
  - Una acción combinada del {ref}`grupo flip <panoramica>` y del movimiento de la superficie o disco rígido separa los componentes y los voltea para que siempre haya al menos uno en la posición correcta para la recogida.

* - **Recogida**
  - El sistema de visión reconoce las piezas que pueden recogerse y envía sus coordenadas al robot, que procede con las operaciones de pick and place.

* - **Recirculación**
  - Los componentes no recogidos reinician su recorrido en el FlexiBowl® hasta que son tomados por el robot.

:::

:::{figure} ../../_shared/media/images/Funz-standard.PNG
:align: center
:width: 50%

Esquema ilustrativo del sistema FlexiBowl® en funcionamiento estándar.
:::

:::{note}
El ciclo {ref}`Flexitracking <tracking>` es fundamentalmente igual al tradicional, con la diferencia de que todas las fases ocurren simultáneamente y de forma continua.
:::


## **Cómo leer el manual**  
Este manual ha sido concebido para dar soporte tanto a la fase de diseño e integración del sistema, como a la fase de instalación y puesta en servicio en campo.
Por este motivo, está dividido en macrosecciones con destinatarios y finalidades distintas.
  
## **¿Qué sección está buscando?**  
```{list-table}
:widths: 40 60
:header-rows: 1

* - Si necesita...
  - La información se encuentra en...

* - Verificar dimensiones, pesos, requisitos eléctricos y protocolos de comunicación
  - [**REFERENCIA TÉCNICA Y ESPECIFICACIONES**](specifiche_tecniche)

* - Instalar los componentes, cablear el sistema, configurar la red o calibrar la cámara/robot
  - [**INSTALACIÓN DEL SISTEMA**](Installazione_Meccanica) y [**QUICKSTART**](quickstart)

* - Programar un nuevo modelo de pieza o configurar el sistema de alimentación
  - [**QUICKSTART**](quickstart)

* - Resolver problemas o solicitar asistencia
  - [**TROUBLESHOOTING**](troubleshooting) y [**SUPPORT**](support)
```

## **Convenciones y símbolos utilizados**

A lo largo del manual se utilizan banners informativos para destacar contenidos importantes:

```{list-table}
:widths: 20 80
:header-rows: 1

* - Tipo
  - Significado

* - ```{warning}
    Advertencia
    ```
  - Indica una situación potencialmente peligrosa o un procedimiento crítico que, si no se ejecuta correctamente, podría provocar daños en el equipo o fallos graves del sistema.

* - ```{important}
    Importante
    ```
  - Destaca información fundamental que no debe ignorarse para garantizar el correcto funcionamiento del sistema o la seguridad de la operación.

* - ```{note}
    Nota informativa
    ```
  - Proporciona información esencial para el correcto desarrollo del procedimiento, aclaraciones técnicas o referencias a capítulos relacionados.

* - ```{tip}
    Sugerencia
    ```
  - Sugiere una práctica óptima, una alternativa o un consejo que puede simplificar la instalación o mejorar el rendimiento del sistema.

* - ```{error}
    Error
    ```
  - Indica un error crítico o una condición de fallo que requiere intervención inmediata. Señala situaciones que comprometen el funcionamiento del sistema y requieren acción correctiva.
```


:::{toctree}
:hidden:
:caption: ANTES DE EMPEZAR 
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
:caption: DATOS TÉCNICOS
FlexiBowl_manual/DATI TECNICI/01_panoramica.md
FlexiBowl_manual/DATI TECNICI/02_dati-tecnici-meccanici.md
FlexiBowl_manual/DATI TECNICI/03_dati-tecnici-elettrici.md
FlexiBowl_manual/DATI TECNICI/04_dati-tecnici-pneumatici.md
FlexiBowl_manual/DATI TECNICI/05_dati-tecnici-applicativi.md
:::

:::{toctree}
:hidden:
:caption: INSTALACIÓN
FlexiBowl_manual/INSTALLAZIONE/01_interfaccia-meccanica.md
FlexiBowl_manual/INSTALLAZIONE/02_interfaccia-elettrica.md
FlexiBowl_manual/INSTALLAZIONE/03_interfaccia-pneumatica.md
FlexiBowl_manual/INSTALLAZIONE/04_interfaccia-software.md
:::

:::{toctree}
:hidden:
:caption: DESCRIPCIÓN GENERAL DEL SOFTWARE
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
:caption: MODOS DE FUNCIONAMIENTO 
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
:caption: BUENAS PRÁCTICAS DE LAYOUT
FlexiBowl_manual/LAYOUT BEST PRACTICE/01_layoutbp.md
:::

:::{toctree}
:hidden:
:caption: ACCESORIOS
FlexiBowl_manual/ACCESSORI/00_ACCESSORI.md
FlexiBowl_manual/ACCESSORI/01_SUPERFICI.md
FlexiBowl_manual/ACCESSORI/03_04_illuminazione.md
FlexiBowl_manual/ACCESSORI/05_DEVIATORE.md
FlexiBowl_manual/ACCESSORI/06_SOFFI.md
FlexiBowl_manual/ACCESSORI/07_BRUSH_DIVERTER.md
FlexiBowl_manual/ACCESSORI/08_WEDGE.md
FlexiBowl_manual/ACCESSORI/09_SVUOTAMENTO.md
:::







