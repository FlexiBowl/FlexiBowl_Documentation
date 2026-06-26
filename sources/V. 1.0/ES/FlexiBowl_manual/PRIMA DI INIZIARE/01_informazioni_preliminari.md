(info)=
# **Información Preliminar**

Esta sección contiene información legal y advertencias importantes relativas al uso del FlexiBowl® y de la presente documentación. Se ruega leerla atentamente antes de proceder con la instalación y el uso del sistema.

---

## Destinatarios y público objetivo

```{note}
**A quién va dirigido este manual**

Esta documentación está dirigida a técnicos cualificados con competencias en:
- Integración de sistemas robotizados
- Configuración de sistemas de visión industrial
- Instalación y mantenimiento de equipos electromecánicos

Se presupone que el lector posee los conocimientos técnicos básicos necesarios para comprender la información aquí recogida. La información fácilmente deducible de planos técnicos o diagramas podría no estar detallada adicionalmente.
```

---

## Advertencias importantes

### **Leer antes de usar**
```{warning}

Antes de utilizar el FlexiBowl®, es obligatorio:
- Leer íntegramente este manual para garantizar un uso correcto del sistema
- Respetar las instrucciones operativas y las recomendaciones
- Formar adecuadamente al personal encargado del uso
- Consultar los manuales de instrucciones de todos los componentes hardware conectados (FlexiVision One, Tolva, VisionController, Cámara, Robot, etc.)

El incumplimiento de estas indicaciones puede provocar fallos de funcionamiento, daños en los equipos o situaciones peligrosas.
```
### **Contexto operativo y limitaciones de responsabilidad**

El FlexiBowl® es un sistema de alimentación flexible de disco rotante vibrante para el posicionamiento y orientación aleatoria de componentes con el fin de facilitar la recogida robótica.

```{warning}
Durante el uso, el operario debe:
- Tener en cuenta las dimensiones físicas del sistema
- Supervisar los movimientos del robot y del alimentador
- Prever y gestionar situaciones operativas imprevistas
- Cumplir las normas de seguridad aplicables a robots y maquinaria industrial
```
```{warning}
**ARS S.r.l. declina toda responsabilidad por daños a personas o cosas derivados del movimiento de máquinas y sistemas conectados al software FlexiVision One.**

La integración del sistema en el entorno de trabajo y la evaluación de riesgos son responsabilidad del integrador de sistema y del usuario final.
```

(operadores)=
## Operadores

Con el fin de establecer con certeza cuáles son las competencias y cualificaciones de los operadores asignados a las distintas tareas (puesta en marcha, limpieza, mantenimiento ordinario), consulte la siguiente tabla:

:::{list-table}
:header-rows: 1
:widths: 30 70

* - Cualificación
  - Definición

* - **Integrador de sistema**
  - Personal encargado del diseño de los layouts, del dimensionamiento de los componentes y de la verificación de los requisitos técnicos para la instalación del FlexiBowl®.

* - **Técnico instalador**
  - Personal encargado del montaje mecánico, la conexión eléctrica y neumática y la configuración de la red.

* - **Operario**
  - Personal del usuario entrenado y habilitado para el uso y la conducción
    de la máquina con fines productivos para las actividades para las que ha sido
    construida y suministrada. Deberá ser capaz de realizar todas las operaciones
    necesarias para el buen funcionamiento de la máquina y para su propia seguridad
    y la de posibles colaboradores. Debe tener experiencia demostrada en el uso
    correcto de este tipo de máquinas y haber recibido formación, información e
    instrucción al respecto. En caso de duda, deberá notificar cualquier anomalía
    a su superior.

    **Nota:** No está habilitado para realizar ninguna actividad de mantenimiento.
    
* - **Técnico de mantenimiento mecánico**
  - Técnico cualificado capaz de:

    * realizar actividades de mantenimiento preventivo/correctivo en todas las partes
      mecánicas de la máquina sujetas a mantenimiento o reparación;
    * acceder a todas las partes de la máquina para análisis visual, control
      del estado de los equipos, ajustes y calibraciones;
    * intervenir en los órganos mecánicos para ajustes, mantenimientos y
      reparaciones;
    * leer esquemas neumáticos, oleohidráulicos, planos técnicos y listas de
      piezas de repuesto.

    En casos extraordinarios, está autorizado a poner en funcionamiento la máquina
    con los dispositivos de seguridad reducidos. Cuando sea necesario, puede dar
    al operario instrucciones para un buen uso de la máquina con fines productivos.

    **Nota:** No está habilitado para intervenir en instalaciones eléctricas
    bajo tensión (si las hubiera).

* - **Técnico de mantenimiento eléctrico**
  - Técnico cualificado capaz de:
    * realizar actividades de mantenimiento preventivo/correctivo en todas las partes mecánicas de la máquina sujetas a mantenimiento o reparación;
    * acceder a todas las partes de la máquina para análisis visual, control del estado de los equipos, ajustes y calibraciones;
    * conducir la máquina como el operario;
    * intervenir en los ajustes y en las instalaciones eléctricas para mantenimiento, reparación y sustitución de piezas desgastadas;
    * leer esquemas eléctricos y verificar el correcto ciclo funcional.
  Cuando sea necesario, puede dar al operario instrucciones para un buen uso de la máquina con fines productivos. Puede operar en presencia de tensión en el interior de los cuadros eléctricos, cajas de derivación, equipos de control, etc., únicamente si se trata de una persona cualificada (PEI). (Referencia normativa **EN50110-1**). No realiza programación software de sistemas tales como: PLC (lógica o seguridad), ni puede modificar las contraseñas del sistema.

* - **Técnico experto en software**
  - Técnico cualificado capaz de:
    * realizar actividades preventivas/correctivas en todas las partes software de la máquina;
    * acceder a todas las partes de la máquina para análisis visual, control del estado de los equipos, ajustes y calibraciones.
  Técnico cualificado del Fabricante con experiencia y formación demostradas en sistemas basados en: PLC/PC accionamientos, etc. (conocimiento de programación, funciones de la máquina, etc.) para operaciones complejas tales como:
    * modificación de datos de la máquina;
    * creación de programas de trabajo;
    * ajuste de parámetros del drive, etc., en tanto en cuanto conoce el ciclo productivo, tecnológico y de construcción de la máquina suministrada.
  Puede operar en el interior de los cuadros eléctricos, cajas de derivación, equipos de control, etc., en presencia de tensión únicamente si se trata de una persona cualificada (PEI) (Referencia normativa **EN50110-1**). Las competencias son de tipo electrónico y/o software.

* - **Técnico del Fabricante**
  - Técnico cualificado por el Fabricante y/o su distribuidor para operaciones complejas, en tanto en cuanto conoce el ciclo productivo de construcción de la máquina. Esta persona interviene de acuerdo con las solicitudes del usuario. Las competencias son de tipo mecánico.

* - **Persona Adiestrada**
  - Agrupa todas las cualificaciones recogidas en esta tabla: se trata de aquella persona que ha sido informada, instruida y adiestrada sobre el trabajo y los posibles peligros derivados de un uso incorrecto. Conoce además la importancia de los dispositivos de seguridad, las normas de prevención de accidentes y las condiciones de trabajo en condiciones de seguridad.

:::

---

## Notas sobre la documentación

### **Versión y actualizaciones**

```{note}

- **Idioma de referencia**: la versión italiana de este documento es la oficial y prevalece en caso de discrepancias con otras traducciones
- **Actualizaciones**: la información contenida está sujeta a modificaciones sin previo aviso por mejoras del producto
- **Unidades de medida**: salvo indicación contraria, todas las dimensiones están expresadas en milímetros (mm)
- **Versión del documento**: comprobar siempre que se dispone de la versión más reciente consultando el sitio [www.flexibowl.it](https://www.flexibowl.it)
```
### **Cómo sacar el máximo partido a este manual**

```{tip}

Para una experiencia óptima:
- Utilice el menú de navegación lateral para pasar rápidamente entre las secciones
- Consulte el índice inicial para identificar de inmediato la sección de su interés
- Preste especial atención a los banners de advertencia, nota y sugerencia
- Siga los procedimientos en el orden indicado, especialmente durante la instalación inicial
- Conserve este manual en formato digital para facilitar búsquedas rápidas mediante palabras clave
```

---


## Derechos de reproducción y notas legales

```{important}
**Copyright © ARS S.r.l. - Todos los derechos reservados**

Ninguna parte de esta publicación puede ser reproducida, distribuida, traducida o transmitida por ningún medio (electrónico, mecánico, fotocopia, grabación u otro sistema de almacenamiento) para fines distintos del uso personal, sin autorización escrita previa de ARS S.r.l.

ARS S.r.l. declina toda responsabilidad por las consecuencias derivadas de operaciones incorrectas realizadas por el usuario o del uso indebido del producto.

**Marcas registradas**: FlexiBowl® es una marca registrada de ARS S.r.l. Todas las demás marcas, nombres comerciales y logotipos mencionados en este documento pertenecen a sus respectivos propietarios y se utilizan exclusivamente con fines identificativos.
```
---
