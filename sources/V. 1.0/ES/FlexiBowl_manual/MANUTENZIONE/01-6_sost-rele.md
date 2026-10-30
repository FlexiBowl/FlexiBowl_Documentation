# **Sustitución de relés y fusibles**


Esta sección describe el funcionamiento y el procedimiento de sustitución de los **relés de interfaz** y de los **fusibles de protección** presentes en la placa de interfaz.

La siguiente figura muestra la placa con la indicación de la posición de los relés y los fusibles.

::: {figure} ../../../../_shared/media/images/schedafronte.png
:align: center
:width: 80%

Vista frontal de la placa de interfaz
:::

En la parte trasera de la placa figuran el amperaje de cada fusible y la referencia de cada relé de interfaz.

(scheda-interfaccia-retro)=
::: {figure} ../../../../_shared/media/images/schedaretro.png
:align: center
:width: 80%

Vista trasera: referencias de los relés y calibres de los fusibles
:::

### Advertencias de seguridad

:::{danger}
**Riesgo eléctrico.** Antes de intervenir en la placa de interfaz, desconecte la tensión de la máquina mediante el interruptor general y espere a que se descarguen los condensadores. Compruebe la ausencia de tensión con un instrumento de medida adecuado antes de tocar cualquier componente.
:::

Durante las operaciones de mantenimiento, respete escrupulosamente las siguientes indicaciones:

- la intervención debe ser realizada exclusivamente por personal técnico cualificado y formado;
- utilice equipos de protección individual (EPI) adecuados, incluidos guantes antiestáticos;
- evite que caigan herramientas o cuerpos extraños sobre la placa durante la intervención;
- no sustituya un fusible por otro de amperaje distinto al original;
- no fuerce los relés durante la extracción: si un componente está atascado, compruebe que esté correctamente encajado antes de continuar;
- al terminar la intervención, cierre correctamente la puerta/ranura de acceso antes de restablecer la alimentación.

### Descripción de la placa

(scheda-relè)=
#### Relés de interfaz

La placa dispone de cinco relés de interfaz, identificados con las siglas K1–K5. El relé K1 es un relé electromecánico de doble conmutación; todos los demás relés (K2–K5) son relés de estado sólido.

:::{list-table}
:widths: 10 55 35
:header-rows: 1

* - Ref.
  - Función
  - Tipo
* - K1
  - Relé de interfaz para backlight
  - Electromecánico de doble conmutación
* - K2
  - Relé de interfaz para electroválvula del flip
  - Estado sólido
* - K3
  - Relé de interfaz para electroválvula de soplado central
  - Estado sólido
* - K4
  - Relé de interfaz para electroválvula de soplado radial
  - Estado sólido
* - K5
  - Relé de interfaz para electroválvula de vaciado (opcional)
  - Estado sólido
:::

(scheda-fusibili)=
#### Fusibles de protección

La placa dispone de nueve fusibles de protección de tipo *automotive mini*. El kit de fusibles de repuesto se suministra con el FlexiBowl®.

:::{list-table}
:widths: 10 70 20
:header-rows: 1

* - Ref.
  - Función
  - Calibre
* - F1
  - Alimentación principal
  - 10 A
* - F2
  - Alimentación de 24 V — electroválvulas de flip, soplado central/radial y vaciado
  - 7.5 A
* - F3
  - Alimentación del conector STO
  - 2 A
* - F4
  - Alimentación hacia el cliente
  - 5 A
* - F5
  - Sensor de vaciado
  - 2 A
* - F6
  - Alimentación del backlight
  - 7.5 A
* - F7
  - Alimentación del backlight
  - 7.5 A
* - F8
  - Alimentación del motor y del driver
  - 5 A
* - F9
  - Alimentación del PLC
  - 7.5 A
:::

### Equipo necesario

- Extractor de fusibles *automotive mini* (o pinzas de punta plana)
- Kit de fusibles de repuesto suministrado con el FlexiBowl®
- Relés de repuesto conformes con la referencia original (K1–K5)

### Sustitución de los relés de interfaz

El procedimiento se aplica a la sustitución de uno o varios relés de interfaz (K1–K5).

1. Desconecte la tensión de la máquina y compruebe su ausencia con el multímetro, como se indica en las advertencias de seguridad.
2. Acceda a la placa de interfaz a través de la abertura prevista.
3. Localice el relé que se va a sustituir consultando la {ref}`vista trasera <scheda-interfaccia-retro>` y la {ref}`tabla de relés <scheda-relè>`.
4. Si el relé que se va a sustituir es **K1** (electromecánico), extráigalo con cuidado de su zócalo tirando hacia arriba sin forzar los terminales.
5. Si el relé que se va a sustituir es **K2, K3, K4 o K5** (estado sólido), extráigalo con el mismo cuidado, evitando doblar los pines de contacto.
6. Inserte el relé de repuesto en el zócalo, comprobando que la referencia y la orientación coincidan exactamente con las del componente retirado.
7. Compruebe que el relé esté correctamente insertado y estable en el zócalo.
8. Vuelva a cerrar la abertura de acceso a la placa.
9. Restablezca la alimentación y compruebe el correcto funcionamiento de la función asociada al relé sustituido.

### Sustitución de los fusibles de protección

El procedimiento se aplica a la sustitución de uno o varios fusibles de protección (F1–F9).

1. Desconecte la tensión de la máquina y compruebe su ausencia con el multímetro, como se indica en las advertencias de seguridad.
2. Abra la ranura de acceso a los fusibles de protección prevista para ello.
3. Localice el fusible que se va a sustituir consultando la {ref}`vista trasera <scheda-interfaccia-retro>` y la {ref}`tabla de fusibles <scheda-fusibili>`.
4. Extraiga el fusible con el extractor específico (o unas pinzas), sujetándolo sin tocar las partes metálicas.
5. Si es posible, compruebe la causa de la actuación del fusible antes de proceder a la sustitución.
6. Tome del kit de repuesto un fusible *automotive mini* del mismo calibre (amperaje) indicado en la tabla.
7. Inserte el nuevo fusible en su alojamiento, comprobando que quede correctamente colocado.
8. Vuelva a cerrar la ranura de acceso.
9. Restablezca la alimentación y compruebe el correcto funcionamiento del circuito protegido por el fusible sustituido.

:::{caution}
No utilice nunca un fusible de calibre distinto al original.
:::

### Controles periódicos y mantenimiento preventivo

- Compruebe periódicamente la ausencia de signos de sobrecalentamiento o ennegrecimiento en relés, fusibles y zócalos.
- Compruebe que los conectores de la placa estén correctamente enchufados.
- Mantenga siempre disponible una reserva del kit de fusibles de repuesto.
- Anote cada sustitución realizada (fecha, referencia del componente, causa) en un registro de mantenimiento.
