# **Mantenimiento y resolución de problemas**

:::{warning}
Realice las operaciones de mantenimiento con la máquina apagada.
:::

:::{warning}
Las operaciones de mantenimiento deben ser realizadas por personal cualificado y autorizado.
::: 

El mantenimiento de la máquina comprende las intervenciones (inspección, verificación, control, ajuste y sustitución) que resulten necesarias como consecuencia del uso normal.

**Directrices para un mantenimiento correcto:**

<style>
  .isw-timeline-custom {
    display: flex !important;
    flex-direction: column !important;
    position: relative !important;
    padding-left: 45px !important;
    margin: 2.5rem 0 !important;
    list-style: none !important;
  }

  .isw-timeline-custom .isw-timeline-item-fixed {
    display: block !important;
    position: relative !important;
    padding-bottom: 2.5rem !important;
  }

  .isw-timeline-custom .isw-timeline-item-fixed:last-child {
    padding-bottom: 0 !important;
  }

  /* Forza la card con il tuo bordo azzurro e sfondo alternativo */
  .isw-timeline-custom .isw-card-fixed {
    display: block !important;
    padding: 1.4rem !important;
    border: 2px solid var(--c-accent, #2980b9) !important;
    border-radius: var(--radius, 10px) !important;
    background: var(--c-bg-alt, #f7fbfe) !important;
    box-shadow: var(--shadow-sm, 0 1px 4px rgba(41,128,185,.08)) !important;
  }

  /* Forza lo stile del titolo */
  .isw-timeline-custom .isw-card-fixed .isw-symbol-label {
    color: var(--c-accent, #2980b9) !important;
    font-size: 19px !important;
    font-weight: 700 !important;
    margin-bottom: 0.5rem !important;
    display: block !important;
    text-transform: none !important;
  }

  /* Linea verticale tratteggiata */
  .isw-timeline-custom .isw-timeline-item-fixed::before {
    content: '' !important;
    position: absolute !important;
    left: -24px !important;
    top: 25px !important;
    bottom: -15px !important;
    width: 2px !important;
    border-left: 2px dashed var(--c-accent, #2980b9) !important;
    z-index: 1 !important;
  }

  .isw-timeline-custom .isw-timeline-item-fixed:last-child::before {
    display: none !important;
  }

  /* Punta della freccia a V minimale */
  .isw-timeline-custom .isw-timeline-arrow-fixed {
    display: block !important;
    content: '' !important;
    position: absolute !important;
    left: -28px !important;
    bottom: 8px !important;
    width: 8px !important;
    height: 8px !important;
    border-right: 2px solid var(--c-accent, #2980b9) !important;
    border-bottom: 2px solid var(--c-accent, #2980b9) !important;
    transform: rotate(45deg) !important;
    z-index: 2 !important;
    background: var(--c-bg, #ffffff) !important;
  }
</style>

<div class="isw-timeline-custom">
  
  <div class="isw-timeline-item-fixed">
    <div class="isw-timeline-arrow-fixed"></div>
    <div class="isw-card-fixed">
      <span class="isw-symbol-label">Componentes</span>
      <div class="isw-symbol-desc">Utilice únicamente repuestos originales y herramientas adecuadas para el fin previsto y en buen estado.</div>
    </div>
  </div>

  <div class="isw-timeline-item-fixed">
    <div class="isw-timeline-arrow-fixed"></div>
    <div class="isw-card-fixed">
      <span class="isw-symbol-label">Frecuencias de intervención</span>
      <div class="isw-symbol-desc">Respete los plazos indicados en el manual para el mantenimiento programado (preventivo y periódico). El intervalo de tiempo o los ciclos de trabajo entre una intervención y la siguiente deben entenderse como el valor máximo aceptable y no deben superarse.</div>
    </div>
  </div>

  <div class="isw-timeline-item-fixed">
    <div class="isw-timeline-arrow-fixed"></div>
    <div class="isw-card-fixed">
      <span class="isw-symbol-label">Supervisión preventiva</span>
      <div class="isw-symbol-desc">Verifique con prontitud la causa de posibles anomalías como ruido excesivo, sobrecalentamientos, fugas de fluidos, etc.</div>
    </div>
  </div>

  <div class="isw-timeline-item-fixed">
    <div class="isw-card-fixed">
      <span class="isw-symbol-label">Prontitud</span>
      <div class="isw-symbol-desc">
        La eliminación inmediata de las causas de una anomalía o un fallo de funcionamiento evita nuevos daños en los equipos y garantiza la seguridad de los operadores.
      </div>
    </div>
  </div>

</div>

El personal encargado debe estar bien formado y tener un conocimiento profundo de las normas de prevención de accidentes. El personal no autorizado debe permanecer fuera del área de trabajo durante las operaciones.

Las actividades de limpieza y ajuste se realizan única y exclusivamente durante el mantenimiento, con la máquina parada, desenergizada y con el cuadro eléctrico seccionado.

:::{important}
En caso de duda, está prohibido intervenir. Consulte al Fabricante para obtener las aclaraciones necesarias.
:::

:::{attention}
Las intervenciones de reparación o de mantenimiento no contenidas en este manual solo pueden realizarse con la autorización previa de ARS S.r.l. No puede atribuirse a ARS S.r.l. ninguna responsabilidad por daños a personas o bienes derivados de intervenciones distintas de las descritas o realizadas de modos distintos de los indicados.
:::

### Clasificación operativa del mantenimiento

| Tipo de mantenimiento | Descripción |
| :--- | :--- |
| **Mantenimiento ordinario** | Operaciones preventivas para garantizar el buen funcionamiento de la máquina a lo largo del tiempo (inspección, control, ajuste, limpieza y lubricación). |
| **Mantenimiento extraordinario** | Intervenciones correctivas según las necesidades (revisión, reparación, restablecimiento de las condiciones nominales o sustitución de un grupo averiado, defectuoso o desgastado). |

---

## Advertencias de seguridad 

:::{attention} 
Antes de iniciar cualquier intervención de mantenimiento en la máquina, seccione y bloquee con candado todas las fuentes de energía y ponga en condición de bloqueo seguro los grupos móviles que la componen. Coloque el cartel «Máquina en mantenimiento - no conectar la alimentación» junto al interruptor general.
:::

:::{attention}
Cuando la máquina esté en mantenimiento, para evitar que pueda ponerse en funcionamiento accidentalmente, coloque carteles con la leyenda: «¡ATENCIÓN! Máquina en mantenimiento».
:::

<div class="isw-page">
  <div class="isw-timeline-container">
    <div class="isw-timeline-item">
      <div class="isw-timeline-arrow"></div>
      <div class="isw-timeline-card">
        <span class="isw-symbol-label">EPI</span>
        <div class="isw-symbol-desc">Los mantenedores deben llevar obligatoriamente todos los equipos de protección individual necesarios (guantes, gafas, monos) para la actividad que se vaya a realizar.</div>
      </div>
    </div>
    <div class="isw-timeline-item">
      <div class="isw-timeline-arrow"></div>
      <div class="isw-timeline-card">
        <span class="isw-symbol-label">Señalización</span>
        <div class="isw-symbol-desc">Si la operación prevé la retirada de protecciones, balice la zona de intervención y señalice la prohibición de acceso a personas ajenas.</div>
      </div>
    </div>
    <div class="isw-timeline-item">
      <div class="isw-timeline-arrow"></div>
      <div class="isw-timeline-card">
        <span class="isw-symbol-label">Verificación de la desconexión</span>
        <div class="isw-symbol-desc">Antes de proceder a cualquier actividad, verifique la desconexión efectiva de las fuentes de energía (corriente eléctrica, aire comprimido, energía hidráulica, etc.).</div>
      </div>
    </div>
    <div class="isw-timeline-item">
      <div class="isw-timeline-card">
        <span class="isw-symbol-label">Competencia</span>
        <div class="isw-symbol-desc">El mantenedor debe realizar solo las operaciones de su competencia (Mecánica, Eléctrica, Fluídica) para las que esté expresamente autorizado, utilizando la instrumentación adecuada para la búsqueda de averías.</div>
      </div>
    </div>
  </div>
</div>

---

## Mantenimiento ordinario 

El mantenimiento ordinario mantiene bajo control las condiciones mecánicas y la limpieza de la máquina. Las periodicidades indicadas se refieren a condiciones de funcionamiento normales.

:::{important}
Para el mantenimiento ordinario de las máquinas procedentes de proveedores externos, consulte los manuales de los subproveedores adjuntos.
::: 

:::{important}
Al fijar los tornillos utilice siempre LOCTITE 243 para garantizar un apriete antivibratorio perfecto.
:::

### Controles y verificaciones

#### Tabla de mantenimiento ordinario – Controles

| Operación | Diaria | Semanal | Mensual | Semestral | Anual |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Control del estado de la cubeta antes de cada arranque | ◈ | | | | |
| Control del estado de desgaste de los relés | | | |  | ◈ |
| Control del correcto funcionamiento de los fusibles | | | |  | ◈ |
| Control del estado de desgaste de las ballestas | | | | ◈ |  |
| Control del correcto funcionamiento del electroimán | | | | ◈ |  |
| Control del desgaste del recubrimiento de poliuretano *(si lo hay)* | | | ◈ | |  |

#### Verificación de los dispositivos de seguridad

Para verificar la integridad de los sistemas de protección, realice los siguientes pasos:

<div style="display: flex; flex-direction: column; gap: 12px; margin: 20px 0;">
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #34495e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">1</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Compruebe que todas las cubiertas y carcasas de la máquina estén presentes y correctamente fijadas.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #34495e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">2</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Compruebe que el cable de alimentación eléctrica no presente daños, cortes ni signos de desgaste superficial.
    </div>
  </div>
</div>

#### Limpieza

:::{attention} 
Las operaciones de limpieza deben ser realizadas únicamente por personal cualificado y autorizado.
:::

:::{attention} 
Para limpiar la máquina, no utilice trozos de esponja, paños húmedos y/o abrasivos, trapos que suelten pelusa, gasolina ni disolventes inflamables como detergente.
:::

:::{attention} 
No utilice ácidos ni disolventes químicos agresivos para limpiar la base del Bulk Feeder.
:::

:::{important}
Utilice productos suaves y no abrasivos, como desengrasantes neutros o jabón doméstico común. Para eliminar fragmentos y polvo, use un pincel procurando llevar gafas de protección.
:::

#### Tabla de mantenimiento ordinario – Limpieza

| Operación | Diaria | Semanal | Mensual | Semestral | Anual |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Eliminación de residuos y desechos del proceso de la superficie de la cubeta | ◈ | | | | |
| Eliminación de grasa y aceite con productos o disolventes neutros | ◈ |  | | | |
| Limpieza general de la máquina | | ◈ |  | | |

#### Procedimiento de limpieza general

<div style="display: flex; flex-direction: column; gap: 12px; margin: 20px 0;">
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #7f8c8d; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">1</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Desconecte completamente la alimentación eléctrica de la máquina.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #7f8c8d; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">2</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Retire manualmente los posibles residuos de producto acumulados.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #7f8c8d; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">3</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Elimine la suciedad localizada utilizando disolventes comerciales no inflamables y no tóxicos.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #7f8c8d; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">4</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Si es necesario, utilice un aspirador para eliminar los residuos diminutos presentes en la superficie giratoria.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #7f8c8d; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">5</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Una vez terminada la limpieza, restablezca las conexiones de la máquina.
    </div>
  </div>
</div>

:::{important}
La limpieza general de la máquina debe realizarse cada vez que se cambie el tipo de componente que se va a procesar, para eliminar los residuos contaminantes del procesamiento anterior.
:::

---

## Mantenimiento extraordinario

:::{attention} 
El mantenimiento extraordinario y la reparación de la máquina están reservados a técnicos cualificados, instruidos y autorizados, empleados del Fabricante o del centro de asistencia autorizado.
:::

Si se producen eventos excepcionales que requieran intervenciones extraordinarias, los mantenedores internos del usuario deben:
1. Verificar con precisión el estado de los grupos dañados o desfasados.
2. Realizar exclusivamente las operaciones descritas en este apartado, si están autorizados.
3. Si las operaciones no están contempladas en este manual, remitir al Fabricante un informe detallado de los hechos, el resultado de la inspección y las observaciones detectadas.

:::{attention} 
Los repuestos que se deban sustituir deben pedirse directamente a ARS S.r.l. Si no se utilizan repuestos originales o autorizados por escrito, el Fabricante declina toda responsabilidad sobre el funcionamiento de la máquina y la seguridad de los operadores.
:::

:::{attention} 
Desconecte la alimentación eléctrica y neumática antes de proceder a cualquier operación de mantenimiento extraordinario o antes de retirar las cubiertas de protección.
:::

:::{important}
Al apretar los tornillos utilice siempre fijador de roscas LOCTITE 243 para garantizar la sujeción mecánica.
:::

### Ajuste del entrehierro

El entrehierro es la distancia física entre el núcleo y el contranúcleo; un ajuste milimétrico es fundamental:
* **Entrehierro demasiado estrecho:** Las superficies del núcleo y del contranúcleo entran en contacto mecánico durante el funcionamiento, provocando el «golpeteo».
* **Entrehierro demasiado ancho:** La corriente eléctrica del vibrador puede alcanzar niveles críticos, provocando la quema del bobinado y daños en los componentes internos del controlador.

:::{attention}
No haga funcionar en ningún caso el vibrador si se produce una de las dos condiciones descritas anteriormente.
:::

:::{important}
El entrehierro viene calibrado adecuadamente de fábrica; los ajustes solo son necesarios en caso de manipulaciones indebidas o de aplicación de sobretensiones.
:::

| Datos operativos | Especificaciones de la intervención |
| :--- | :--- |
| **Cualificación del operador** | Mantenedor mecánico |
| **Herramientas que se deben utilizar** | Llave de boca |

#### Procedimiento de ajuste del entrehierro

![Ajuste del entrehierro](../../../../../_shared/media/images/regolazione_traferro.png)

<div style="display: flex; flex-direction: column; gap: 12px; margin: 20px 0;">
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">1</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Afloje la contratuerca de bloqueo <strong>(Tuerca 2)</strong>.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">2</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Enrosque el <strong>Tornillo 1</strong> en sentido horario hasta llevarlo al final de su recorrido, es decir, hasta el tope mecánico contra el contranúcleo.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">3</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Desenrosque el <strong>Tornillo 1</strong> en sentido antihorario: consulte la tabla siguiente para identificar el valor correcto y haga girar el tornillo el número de vueltas y fracciones necesarias para establecer la distancia correcta.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">4</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Apriete a fondo la <strong>Tuerca 2</strong> para asegurar la estabilidad del tornillo de ajuste 1.
    </div>
  </div>
</div>

:::{note} 
 El ajuste del entrehierro es una operación de precisión que puede requerir comprobaciones repetidas para obtener el ajuste ideal.
:::
![Ajuste del entrehierro](../../../../../_shared/media/images/disegno_tecnico.png)

#### Tabla técnica de referencia del entrehierro

| Modelo | Tamaño del imán | Entrehierro requerido | Giro del tornillo de ajuste |
| :---: | :---: | :---: | :---: |
| **1,5 l** | Ø21 | 1,5 mm | 360° (1 vuelta completa) |
| **3 l** | Ø24 | 2 mm | 480° (1 vuelta + 1/3) |
| **5 l** | Ø28 | 3 mm | 720° (2 vueltas completas) |
| **10 l** | Ø28 | 3 mm | 720° (2 vueltas completas) |
| **20 l** | Ø28 | 3 mm | 720° (2 vueltas completas) |
| **40 l** | 32x30 | 3 mm | 720° (2 vueltas completas) |

### Sustitución de las ballestas

| Datos operativos | Especificaciones de la intervención |
| :--- | :--- |
| **Cualificación del operador** | Mantenedor mecánico |
| **Herramientas que se deben utilizar** | Llave de boca |

La modificación del dimensionamiento del paquete de ballestas (número y espesor de las hojas) sirve para variar y adecuar la capacidad útil del vibrador.

#### Procedimiento de sustitución de las ballestas

<div style="display: flex; flex-direction: column; gap: 12px; margin: 20px 0;">
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">1</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Trabaje en un solo paquete de ballestas cada vez, comenzando obligatoriamente por el situado en la parte posterior.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">2</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Anote o fotografíe la posición exacta y el orden de secuencia de cada ballesta, separador y abrazadera de retención.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">3</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Retire los pernos de anclaje mecánico a la base y, a continuación, los pernos de fijación al puente del canal vibratorio.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">4</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Sustituya los elementos desgastados o agrietados por repuestos originales.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">5</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Vuelva a montar el paquete de ballestas siguiendo exactamente el orden inverso al del desmontaje.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">6</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Apriete todos los tornillos aplicando el par de apriete indicado en la tabla siguiente.
    </div>
  </div>
</div>

#### Tabla técnica de ballestas y pares de apriete

| Modelo | Tamaño de las ballestas | Espesor de las hojas | Par de apriete y rosca |
| :---: | :---: | :---: | :--- |
| **1,5 l** | 40x48 mm | 1 - 1,5 - 2 mm | 7,5 N·m – M5 |
| **3 l** | 40x48 mm | 1 - 1,5 - 2 mm | 7,5 N·m – M5 |
| **5 l** | 70x82 mm | 1,5 - 2 mm | 30 N·m – M8 |
| **10 l** | 70x82 mm | 1,5 - 2 mm | 30 N·m – M8 |
| **20 l** | 70x82 mm | 1,5 - 2 mm | 30 N·m – M8 |
| **40 l** | 80x91 mm | 1,5 - 2 - 2,5 mm | 70 N·m – M10 |

### Sustitución de la cubeta

| Datos operativos | Especificaciones de la intervención |
| :--- | :--- |
| **Cualificación del operador** | Mantenedor mecánico |
| **Herramientas que se deben utilizar** | Llave de boca |

#### Procedimiento de desmontaje y montaje de la cubeta

<div style="display: flex; flex-direction: column; gap: 12px; margin: 20px 0;">
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">1</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Sujete firmemente la cubeta para evitar su caída accidental durante la retirada.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">2</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Afloje los cuatro tornillos de fijación presentes en la placa base de la cubeta.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">3</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Levante con cuidado la cubeta original y extráigala de su alojamiento.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">4</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Retire la junta de la placa base.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">5</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Coloque la junta en la nueva cubeta, comprobando que quede correctamente alojada.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">6</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Introduzca la nueva cubeta en su alojamiento, comprobando que quede correctamente encajada en los pasadores de fijación y que la junta esté bien colocada.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">7</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Apriete los cuatro tornillos presentes en la placa base para fijar la nueva cubeta.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">8</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Compruebe que la nueva cubeta esté correctamente colocada y firmemente fijada.
    </div>
  </div>
</div>

![Desmontaje y montaje de la cubeta](../../../../../_shared/media/images/vasca.jpg)

:::{attention}
En el caso de modelos personalizados, los componentes pueden diferir, parcial o totalmente, de los indicados. Para este tipo de modelos es necesario consultar el expediente técnico del proyecto.
:::

---

## Resolución de problemas

:::{attention}
Durante el funcionamiento normal, el vibrador debe funcionar silenciosamente. Si se produjera un ruido sordo causado por un golpeteo interno, apague inmediatamente el sistema.
:::

En caso de golpeteo, compruebe y restablezca el entrehierro óptimo: si las superficies están demasiado cerca, chocarán mecánicamente; si están demasiado lejos, el aumento anómalo de corriente quemará los bobinados del estátor.

| Síntoma observado | Posible causa raíz | Acción correctiva requerida |
| :--- | :--- | :--- |
| **El vibrador funciona demasiado despacio** | La tensión de alimentación está por debajo del umbral nominal. | Aumente la tensión eléctrica hasta el valor correcto de placa. |
| | La unidad entra en contacto con objetos rígidos externos o estructuras adyacentes. | Restablezca las holguras físicas aislando la unidad vibratoria (3-5 cm). |
| | La oscilación de los paquetes de ballestas está obstaculizada o frenada por acumulaciones. | Desmonte, limpie a fondo y elimine los residuos de los paquetes de ballestas. |
| | Las ballestas presentan grietas, defectos o fluencia estructural. | Proceda a la sustitución inmediata del juego de ballestas. |
| | El canal vibratorio está agrietado o mecánicamente desgastado. | Sustituya el canal. |
| **El vibrador funciona demasiado rápido** | La tensión de alimentación supera los límites nominales *(causa principal del golpeteo)*. | Estabilice y reduzca la tensión de alimentación al valor de placa. |
| **La unidad emite ruido (zumbido) pero no vibra** | La placa electrónica de regulación del interior de la caja está defectuosa. | Sustituya la placa electrónica del controlador. |
| **La unidad no se activa y no responde** | Falta total de alimentación eléctrica en la entrada del controlador. | Inspeccione la línea y elimine las posibles interrupciones eléctricas. |
| | El interruptor magnetotérmico o el fusible de protección está disparado/fundido. | Sustituya los fusibles o rearme el interruptor. |
| | La placa electrónica del interior de la caja de control está dañada. | Sustituya la placa electrónica. |
| | El bobinado interno del vibrador está quemado o descarga a masa. | Sustituya el grupo del electroimán. |
| | El bobinado presenta un cortocircuito interno. | Sustituya el bobinado. |
| | El bobinado del reóstato de regulación está abierto. | Sustituya el componente averiado. |


