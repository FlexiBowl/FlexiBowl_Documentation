# **Modo Estándar**

El **modo Estándar** es la configuración operativa predeterminada del FlexiBowl® y se adapta a cualquier tipo de aplicación de alimentación robotizada. En este modo, el robot y el sistema de visión comparten la misma área de trabajo, operando de forma coordinada y secuencial para garantizar un alto rendimiento de ciclo.

---

## Principio de funcionamiento

En modo Estándar, el FlexiBowl® ejecuta un ciclo continuo compuesto por tres fases principales, que se repiten en secuencia:

```{figure} ../../../../_shared/media/images/flexibowl_standard_cycle.jpg
:align: center
:width: 50%
:alt: *Ciclo operativo en modo Estándar: Detect → Pick-Drop → Move-Flip*
```
```{image} ../../../../_shared/media/videos/STANDARD_MODE.gif
:align: center
:width: 100%
:alt: *Ciclo operativo en modo Estándar: Detect → Pick-Drop → Move-Flip*
```

### 1. Detect (Detección)

El sistema de visión captura una imagen de la superficie del FlexiBowl® e identifica la posición, la orientación y el tipo de los componentes presentes. La información se transmite al robot para planificar las operaciones de recogida.

### 2. Pick-Drop (Recogida y depósito)

El robot toma los componentes correctamente orientados del FlexiBowl® y los deposita en la posición de destino (p. ej. bandeja, cinta transportadora, estación de montaje). Las actividades de visión y recogida se ejecutan **de forma secuencial**: primero el sistema de visión escanea la escena y después interviene el robot.

### 3. Move-Flip (Movimiento y vuelco)

Al finalizar la recogida, el FlexiBowl® realiza un movimiento combinado de rotación y vibración (**flip**) para remezclar los componentes restantes y favorecer la correcta presentación de nuevas piezas. Al mismo tiempo, la **descarga del hopper** y el **movimiento del bowl** se ejecutan **de forma simultánea**, optimizando los tiempos de ciclo.

---

## Características principales

| Característica | Descripción |
|---|---|
| **Área de trabajo compartida** | El robot y el sistema de visión operan en la misma zona del FlexiBowl® |
| **Aplicabilidad** | Adecuado para todo tipo de aplicación |
| **Descarga del hopper** | Se ejecuta simultáneamente con el movimiento/impulso del FlexiBowl® |
| **Visión y recogida** | Se ejecutan en secuencia |
| **Medición del ciclo** | El tiempo de ciclo se mide por minuto |

---

## Esquema del ciclo operativo

El ciclo se desarrolla según el siguiente esquema de lazo cerrado:

1. **Detect** — El sistema de visión escanea el FlexiBowl® y localiza los componentes.
2. **Pick-Drop** — El robot toma las piezas identificadas y las deposita en el destino.
3. **Move-Flip** — El FlexiBowl® remezcla los componentes para el siguiente ciclo.
4. El ciclo vuelve a comenzar desde el punto 1.

:::{note} 
Durante la fase Move-Flip, la descarga del hopper se realiza en paralelo al movimiento del FlexiBowl®, reduciendo los tiempos muertos y maximizando la productividad.
:::

---
## Ejemplo de disposición

:::{figure} ../../../../_shared/media/images/Funz-standard.PNG
:align: center
:width: 60%

Ejemplo de disposición en modo Estándar: el Bulk Feeder descarga en el sector de liberación, el flip separa los componentes, el robot toma en el área de visión y las piezas no tomadas recirculan.
:::

El área de trabajo del robot debe cubrir por completo el área de visión, de modo que el robot pueda alcanzar todos los componentes reconocidos como tomables. Para el posicionamiento del robot, el Bulk Feeder, los puntos de depósito, la cámara y la iluminación, consulte {ref}`Layout Best Practice <layoutbp-traditional>`.


---

## Ventajas 


:::{grid-item-card} Ventajas
- **Precisión**: .
- **Separación**: .
- **Velocidad**: .
:::
