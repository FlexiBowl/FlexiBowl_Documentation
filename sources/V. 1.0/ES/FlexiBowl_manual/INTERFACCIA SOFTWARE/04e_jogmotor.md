(jog)=
# **Jog Motor**

## Descripción general

La página **Jog Motor** permite accionar el FlexiBowl® en modo manual continuo (jog), sin utilizar secuencias programadas. Se utiliza principalmente durante las fases de configuración, puesta en servicio y prueba del sistema, permitiendo al operador controlar directamente la rotación del FlexiBowl® y las funciones accesorias.
![página jog motor](../../../../_shared/media/images/jog_motor.png)

---

## Parámetros de movimiento

Los tres deslizadores de la parte superior definen el comportamiento del motor durante el jog.

| Parámetro | Unidad | Valor de ejemplo | Descripción |
|---|---|---|---|
| **Acceleration** | % | 50 | Rampa de aceleración al inicio del jog |
| **Deceleration** | % | 50 | Rampa de deceleración al detener el jog |
| **Speed** | % | -30 | Velocidad de rotación del FlexiBowl®. Un valor **negativo** indica rotación en sentido **antihorario**; un valor **positivo** indica rotación en sentido **horario** |

:::{tip}
Para invertir el sentido de rotación del FlexiBowl® durante el jog, basta con poner el deslizador **Speed** en un valor negativo. No es necesario detener el jog para modificar el parámetro.
:::

---

## Panel FLIP

El panel **Flip Enable** gestiona la activación y los parámetros del sistema de vuelco durante el jog.

| Control | Valor de ejemplo | Descripción |
|---|---|---|
| **Flip Enable** (interruptor) | Activo (rojo) | Activa el flip automático durante el jog |
| **Flip Duration** | 200 ms | Duración del impulso de accionamiento del flip |
| **Flip Pression** | 3,00 Bar | Presión de aire utilizada para el flip |
| **Flip Pause** | 200 ms | Pausa entre un flip y el siguiente durante el jog |

:::{note}
El flip se ejecuta cíclicamente durante el jog, con la cadencia definida por **Flip Pause**, solo si el interruptor **Flip Enable** está activo.
:::

---

## Panel BLOW

El panel **Blow Enable** gestiona la activación y los parámetros del sistema de soplado durante el jog.

| Control | Valor de ejemplo | Descripción |
|---|---|---|
| **Blow Enable** (interruptor) | Activo (rojo) | Activa el soplado automático durante el jog |
| **Blow Duration** | 200 ms | Duración del impulso de soplado |
| **Blow Pression** | 3,00 Bar | Presión de aire utilizada para el soplado |
| **Blow Pause** | 200 ms | Pausa entre un impulso de soplado y el siguiente durante el jog |
| **Blow Type** | BLOWc + BLOWe | Tipo de soplado activado. Las opciones combinan soplado central (BLOWc) y/o soplado externo (BLOWe) |

### Opciones de Blow Type

| Valor | Descripción |
|---|---|
| **BLOWc** | Solo soplado central |
| **BLOWe** | Solo soplado externo |
| **BLOWc + BLOWe** | Ambos soplados activados simultáneamente |

---

## Panel BACKLIGHT

El panel **Backlight** gestiona el estado de las retroiluminaciones independientemente del jog.

| Control | Descripción |
|---|---|
| **Backlight 1** (interruptor) | Activa/desactiva la retroiluminación 1 |
| **Backlight 2** (interruptor) | Activa/desactiva la retroiluminación 2 |

Los interruptores se muestran en rojo cuando la retroiluminación está **activa**.

---

## Inicio y parada del jog

| Botón | Función |
|---|---|
| **START JOG** | Inicia la rotación continua del FlexiBowl® con los parámetros establecidos, activando simultáneamente flip y blow si los interruptores respectivos están habilitados |
| **STOP JOG** | Interrumpe el jog y detiene el FlexiBowl® |

:::{important}
Antes de pulsar **START JOG**, comprobar que:
- el motor está habilitado (**ENABLE MOTOR** activo)
- el estado del sistema es **READY**
- los parámetros Speed, Flip y Blow estén correctamente configurados para evitar movimientos no deseados
:::

:::{warning}
Durante el jog el FlexiBowl® gira de forma continua. Antes de iniciar el jog, asegúrese de que la zona alrededor del FlexiBowl® esté libre de obstáculos y de que el personal no esté en contacto con las partes en movimiento.
:::
