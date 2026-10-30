(info)=
# **Información preliminar**

Esta sección contiene información legal y advertencias importantes relativas al uso del FlexiBowl® y de la presente documentación.   Se ruega leerla atentamente antes de proceder con la instalación y el uso del sistema.

---

## Destinatarios y público objetivo

```{note}
**A quién va dirigido este manual**

Esta documentación está dirigida a técnicos cualificados con competencias en:
- Integración de sistemas robotizados
- Configuración de sistemas de visión industrial
- Instalación y mantenimiento de equipos electromecánicos

Se presupone que el lector posee los conocimientos técnicos básicos necesarios para comprender la información proporcionada.   La información fácilmente deducible de planos técnicos o diagramas puede no detallarse más.
```

---

## Advertencias importantes

### **Leer antes del uso**
```{warning}

Antes de utilizar el FlexiBowl®, es obligatorio:
- Leer íntegramente este manual para garantizar un uso correcto del sistema
- Respetar las instrucciones de funcionamiento y las recomendaciones
- Formar adecuadamente al personal encargado del uso
- Consultar los manuales de instrucciones de todos los componentes de hardware conectados (FlexiVision One, Bulk Feeder, VisionController, cámara, robot, etc.)

El incumplimiento de estas indicaciones puede provocar fallos de funcionamiento, daños en los equipos o situaciones peligrosas.
```
### **Contexto operativo y limitaciones de responsabilidad**

El FlexiBowl® es un sistema de alimentación flexible de disco giratorio vibrante para el posicionamiento y la orientación aleatorios de los componentes con vistas a la recogida robotizada.

```{warning}
Durante el uso, el operario debe:
- Tener en cuenta las dimensiones físicas del sistema
- Supervisar los movimientos del robot y del alimentador
- Prever y gestionar situaciones operativas imprevistas
- Cumplir las normas de seguridad aplicables a robots y maquinaria industrial
```
```{warning}
**ARS S.r.l. declina toda responsabilidad por daños a personas o bienes derivados del movimiento de máquinas y sistemas conectados al software FlexiVision One.**

La integración del sistema en el entorno de trabajo y la evaluación de riesgos son responsabilidad del integrador de sistemas y del usuario final.
```

(operatori)=
## Operarios

Para establecer con certeza las competencias y cualificaciones de los operarios encargados de las distintas tareas (puesta en marcha, limpieza, mantenimiento ordinario), consulte la siguiente tabla:

:::{list-table}
:header-rows: 1
:widths: 30 70

* - Cualificación
  - Definición

* - **Integrador de sistemas**
  - Personal encargado del diseño de las disposiciones, del dimensionamiento de los componentes y de la verificación de los requisitos técnicos para la instalación del FlexiBowl®.

* - **Técnico instalador**
  - Personal encargado del montaje mecánico, de la conexión eléctrica y neumática y de la configuración de la red.

* - **Operario**
  - Personal del usuario formado y habilitado para el uso y la conducción de la máquina con fines productivos, para las actividades para las que ha sido construida y suministrada. Debe ser capaz de realizar todas las operaciones necesarias para el buen funcionamiento de la máquina y para la seguridad propia y la de posibles colaboradores. Debe tener una experiencia comprobada en el uso correcto de este tipo de máquinas y estar formado, informado e instruido al respecto. En caso de duda, debe comunicar cualquier anomalía a su superior.

    **Nota:** No está habilitado para realizar ninguna actividad de mantenimiento.
    
* - **Técnico de mantenimiento mecánico**
  - Técnico cualificado capaz de:

    * realizar actividades de mantenimiento preventivo/correctivo en todas las partes mecánicas de la máquina sujetas a mantenimiento o reparación;
    * tener acceso a todas las partes de la máquina para el análisis visual, el control del estado de los equipos, los ajustes y las calibraciones;
    * intervenir en los órganos mecánicos para ajustes, mantenimientos y reparaciones;
    * leer esquemas neumáticos e hidráulicos, planos técnicos y listados de repuestos.

    En casos excepcionales, está autorizado a hacer funcionar la máquina con seguridades reducidas. Cuando sea necesario, puede dar al operario instrucciones para el buen uso de la máquina con fines productivos.

    **Nota:** No está habilitado para intervenir en instalaciones eléctricas bajo tensión (si las hay).

* - **Técnico de mantenimiento eléctrico**
  - Técnico cualificado capaz de:
    * realizar actividades de mantenimiento preventivo/correctivo en todas las partes mecánicas de la máquina sujetas a mantenimiento o reparación;
    * tener acceso a todas las partes de la máquina para el análisis visual, el control del estado de los equipos, los ajustes y las calibraciones;
    * manejar la máquina como el operario;
    * intervenir en los ajustes y en las instalaciones eléctricas para mantenimiento, reparación y sustitución de piezas desgastadas;
    * leer esquemas eléctricos y verificar el correcto ciclo funcional. Cuando sea necesario, puede dar al operario instrucciones para el buen uso de la máquina con fines productivos. Puede trabajar con tensión presente en el interior de los cuadros eléctricos, cajas de derivación, aparatos de control, etc. solo si se trata de una persona idónea (PEI). (Véase la norma **EN50110-1**). No realiza la programación de software de sistemas como PLC (lógica o seguridad) ni puede modificar las contraseñas del sistema.

* - **Técnico experto en software**
  - Técnico cualificado capaz de:
    * realizar actividades preventivas/correctivas en todas las partes de software de la máquina;
    * tener acceso a todas las partes de la máquina para el análisis visual, el control del estado de los equipos, los ajustes y las calibraciones. Técnico cualificado del Fabricante con experiencia y formación comprobadas en sistemas basados en: PLC/PC, accionamientos, etc. (conocimiento de programación, funciones de la máquina, etc.) para operaciones complejas como, por ejemplo:
    * modificación de los datos de la máquina;
    * creación de programas de trabajo;
    * ajuste de los parámetros de los accionamientos, etc., por conocer el ciclo productivo, tecnológico y de construcción de la máquina suministrada. Puede trabajar en el interior de los cuadros eléctricos, cajas de derivación, aparatos de control, etc. con tensión presente solo si se trata de una persona idónea (PEI) (véase la norma **EN50110-1**). Sus competencias son de tipo electrónico y/o de software.

* - **Técnico del Fabricante**
  - Técnico cualificado por el Fabricante y/o por su distribuidor para operaciones complejas, por conocer el ciclo productivo de construcción de la máquina. Esta persona interviene de acuerdo con las solicitudes del usuario. Sus competencias son de tipo mecánico.

* - **Persona adiestrada**
  - Agrupa todas las cualificaciones indicadas en esta tabla: se trata de quien ha sido informado, instruido y adiestrado sobre el trabajo y sobre los posibles peligros derivados de un uso indebido. Conoce además la importancia de los dispositivos de seguridad, las normas de prevención de accidentes y las condiciones de trabajo seguro.

:::

---

## Notas sobre la documentación

### **Versión y actualizaciones**

```{note}

- **Idioma de referencia**: la versión italiana de este documento es la oficial y prevalece en caso de discrepancias con otras traducciones
- **Actualizaciones**: la información contenida está sujeta a modificaciones sin previo aviso por mejoras del producto
- **Unidades de medida**: salvo indicación en contrario, todas las dimensiones se expresan en milímetros (mm)
- **Versión del documento**: compruebe siempre que dispone de la versión más reciente consultando el sitio web [www.flexibowl.it](https://www.flexibowl.it)
```
### **Cómo aprovechar al máximo este manual**

```{tip}

Para una experiencia óptima:
- Utilice el menú de navegación lateral para pasar rápidamente de una sección a otra
- Consulte el índice inicial para identificar de inmediato la sección que le interesa
- Preste especial atención a los avisos de advertencia, nota y sugerencia
- Siga los procedimientos en el orden indicado, especialmente durante la instalación inicial
- Conserve este manual en formato digital para facilitar las búsquedas rápidas por palabras clave
```

---


## Derechos de reproducción y avisos legales

```{important}
**Copyright © ARS S.r.l. - Todos los derechos reservados**

Ninguna parte de esta publicación puede ser reproducida, distribuida, traducida ni transmitida por ningún medio (electrónico, mecánico, fotocopia, grabación u otro sistema de almacenamiento) con fines distintos del uso personal, sin la autorización previa por escrito de ARS S.r.l.

ARS S.r.l. declina toda responsabilidad por las consecuencias derivadas de operaciones erróneas realizadas por el usuario o del uso indebido del producto.

**Marcas registradas**: FlexiBowl® es una marca registrada de ARS S.r.l. Todas las demás marcas, nombres comerciales y logotipos mencionados en este documento pertenecen a sus respectivos propietarios y se utilizan exclusivamente con fines de identificación.
```
---


