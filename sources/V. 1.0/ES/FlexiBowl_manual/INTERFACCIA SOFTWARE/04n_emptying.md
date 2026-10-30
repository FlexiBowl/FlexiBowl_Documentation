(emptying)=
# **Emptying**

La página Emptying se pone a disposición automáticamente cuando se adquiere la opción de Vaciado.

## Descripción general

La función **Emptying** permite vaciar automáticamente el FlexiBowl® encadenando hasta **4 secuencias** dedicadas, cada una repetida un número de veces (loop) configurable. Está pensada para liberar rápidamente el disco de las piezas residuales, por ejemplo al final del turno o durante un cambio de producción, sin tener que llamar manualmente a las secuencias una por una.

![Página Emptying](../../../../_shared/media/images/pagina_Emptying.png)

---

## Configuración mediante la interfaz web

La página está organizada en **4 columnas**, una por cada una de las secuencias que componen el ciclo de vaciado («Select the first/second/third/fourth sequence»), además de los comandos de inicio/parada en la parte inferior de la página.

### AUTO CONFIG

El botón **AUTO CONFIG**, en la parte superior, inserta automáticamente una configuración predeterminada que ocupa las **secuencias 17, 18, 19 y 20**. Como alternativa, es posible personalizar libremente estas secuencias o seleccionar otras entre las 20 disponibles.

:::{note}
En la configuración predeterminada, la primera secuencia baja la barrera (**FLB_BARRIER_DOWN**), las dos secuencias centrales repiten varias veces un movimiento combinado de rotación y soplado seguido de un shake (**FLB_MOVE_BLOWc** + **FLB_SHAKE**), y la última vuelve a subir la barrera (**FLB_BARRIER_UP**) al final del ciclo.
:::

### Elementos de cada columna

| Elemento | Función |
|---|---|
| **Select the first/second/third/fourth sequence** | Menú desplegable para seleccionar cuál de las 20 secuencias programadas se ejecuta en ese paso del ciclo de vaciado |
| **Active Command** | Lista de los comandos activos de la secuencia seleccionada (hasta 10 posiciones, misma estructura que la página Main Command) |
| **N° Loop** | Número de veces que se repite la secuencia seleccionada durante ese paso |
| **EDIT SEQUENCE** | Abre la secuencia seleccionada para modificar los comandos que la componen |

### Inicio y parada

| Comando | Función |
|---|---|
| **START EMPTYING** | Inicia el ciclo de vaciado: ejecuta en orden las 4 secuencias configuradas, cada una durante el número de loops establecido |
| **STOP EMPTYING** | Interrumpe el ciclo de vaciado en curso |

---
## Página Option

Si la función Emptying está presente, en la sección OPTION de la página «Main Command» se mostrará el siguiente recuadro:

![Emptying OPTION](../../../../_shared/media/images/emptying_option.png)

Este recuadro, que contiene los dos botones «Raise Barrier» y «Lower Barrier», permite subir y bajar la barrera de vaciado y, por tanto, comprobar su correcto funcionamiento. Cuando la barrera se baja, se activa el sensor presente en este recuadro.

## Página Sequence 

:::{image} ../../../../_shared/media/images/box_emptying.png
:width: 50% 
:align: center
:::

En la página Sequence, la marca en la casilla «Emptying Sequence» permite mover el FlexiBowl incluso con la barrera de vaciado bajada. De hecho, si la barrera está bajada y la casilla de la página Sequence no está marcada, no será posible realizar el movimiento asociado a la secuencia actual.

## Comandos por protocolo

Al igual que el resto de la interfaz de software, el ciclo de Emptying también puede iniciarse, configurarse y verificarse por protocolo (TCP Server, EtherNet/IP, Profinet, Modbus), con las mismas ControlWords independientemente del protocolo utilizado — solo cambia el transporte, como se describe en la página [Interfaz de software](int_software).

### Comandos EXE

| Comando | ControlWord | Busy durante la ejecución | ReturnData_1 | Explicación |
|---|---|---|---|---|
| Start Emptying | 45 | SÍ (Emptying activo) | 45 | Inicia el vaciado |
| Stop Emptying | 46 | SÍ (Emptying activo) | 46 | Detiene el vaciado |
| Emptying Active | 47 | NO | 47 | Comprueba si el vaciado está activo |

### Comandos WRITE

Cada par Secuencia/Loop corresponde a una de las 4 columnas de la página web:

| Comando | ControlWord | Range Data_1 | Busy durante la ejecución | ReturnData_1 |
|---|---|---|---|---|
| FirstSequence | 20200 | 1–20 | NO | 20200 |
| FirstLoop | 20201 | 0–500 | NO | 20201 |
| SecondSequence | 20202 | 1–20 | NO | 20202 |
| SecondLoop | 20203 | 0–500 | NO | 20203 |
| ThirdSequence | 20204 | 1–20 | NO | 20204 |
| ThirdLoop | 20205 | 0–500 | NO | 20205 |
| FourthSequence | 20206 | 1–20 | NO | 20206 |
| FourthLoop | 20207 | 0–500 | NO | 20207 |

### Comandos READ

| Comando | ControlWord | Busy durante la ejecución | ReturnData_1 | Range ReturnData_2 |
|---|---|---|---|---|
| FirstSequence | 20300 | NO | 20300 | 1–20 |
| FirstLoop | 20301 | NO | 20301 | 0–500 |
| SecondSequence | 20302 | NO | 20302 | 1–20 |
| SecondLoop | 20303 | NO | 20303 | 0–500 |
| ThirdSequence | 20304 | NO | 20304 | 1–20 |
| ThirdLoop | 20305 | NO | 20305 | 0–500 |
| FourthSequence | 20306 | NO | 20306 | 1–20 |
| FourthLoop | 20307 | NO | 20307 | 0–500 |

:::{tip}
Para la explicación completa de la lógica de las ControlWord, del funcionamiento en 4 pasos y de ejemplos prácticos mediante bus de campo/TCP, consulte la sección [Comandos de vaciado](int_software.html#sec-empty) de la página Interfaz de software.
:::

---

## Notas de uso

:::{note}
Las 4 secuencias llamadas por Emptying (por defecto 17–20, o personalizadas) siguen siendo secuencias programables normales: pueden modificarse desde la página **Main Command** exactamente igual que cualquier otra secuencia, además de con el botón **EDIT SEQUENCE** de esta página.
:::

:::{warning}
No envíe un nuevo comando **Start Emptying** mientras ya haya un ciclo de vaciado en curso (**Emptying Active** = 1). Compruebe que el ciclo anterior haya terminado, o envíe **Stop Emptying**, antes de iniciar uno nuevo.
:::
