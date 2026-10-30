# **Air Blow Kit**

:::{note}
La implementación de los soplados implica una modificación del sistema neumático del FlexiBowl®; para más información, consulte los {ref}`esquemas neumáticos <sc-pneum>`.
:::

El kit de soplado (o *Air Blow Kit*) se compone de las siguientes partes:

## Soplado radial

El soplado radial consiste en un cartucho que se puede montar en lugar del desviador estándar y que presenta dos orificios radiales a alturas diferentes: por uno de ellos, a elección del operador según las dimensiones de las piezas que se vayan a manipular, sale un chorro de aire que aleja los componentes del anillo de contención.

:::{figure} ../../../../_shared/media/images/sofrad500.PNG
:width: 100%
:align: center
:::

### Procedimiento de montaje

:::{warning}
Desconectar la alimentación eléctrica antes de proceder con el montaje de los soplados.
:::

| Paso | Operación |
|:----:|-----------|
| 1 | Retirar los tornillos de fijación del desviador |
| 2 | Desenroscar los tornillos de regulación para retirar el desviador |
| 3 | Colocar la junta maciza y la perforada en sus alojamientos según la altura de soplado deseada |
| 4 | Colocar el cartucho de soplado radial y fijarlo con los tornillos correspondientes |

### Procedimiento de regulación

El soplado radial se puede regular tanto mediante software como mecánicamente, actuando sobre el prisionero situado dentro del cartucho con una llave Allen de 1,5 mm, procurando fijar su posición apretando el empujador con un destornillador plano.

::::{raw} html
<figure style="text-align: center;">
  <video id="regsof500" width="100%" height="auto" controls>
    <source src="../../../../_shared/media/videos/FB500regsof.mp4" type="video/mp4">
    Su navegador no admite el vídeo.
  </video>
  <br>
  <label for="Velsof500">Velocidad:</label>
  <select id="Velsof500" onchange="document.getElementById('regsof500').playbackRate = this.value">
    <option value="0.5">0.5x</option>
    <option value="1" selected>1x</option>
    <option value="1.5">1.5x</option>
    <option value="2">2x</option>
  </select> 
  <figcaption><i>Procedimiento de regulación mecánica del soplado radial ilustrado en un FlexiBowl® 500</i></figcaption>
</figure>
::::

También se puede elegir la altura del soplado intercambiando la junta con el tapón situado bajo el cartucho:

:::{figure} ../../../../_shared/media/images/sofrad500-sm.PNG
:width: 100%
:align: center
:::

## Soplado central

El soplado central consiste en una boquilla montada en la punta de la pantalla flip cuyo chorro de aire está orientado de modo que aleje los componentes de la cubierta de sujeción del disco. Su finalidad es doble:

- Llevar los componentes sobre el flip para maximizar su eficacia;
- Evitar que los componentes se consideren no recogibles por una excesiva cercanía a la cubierta de sujeción del disco, lo que provocaría una colisión del robot.

:::{figure} ../../../../_shared/media/images/sofcen500.PNG
:width: 100%
:align: center
:::

### Procedimiento de montaje

| Paso | Operación |
|:----:|-----------|
| 1 | Retirar todo el conjunto pantalla-barrera flip desenroscando los cuatro tornillos de fijación |
| 2 | Sustituir la pantalla por el conjunto de soplado central |
| 3 | Fijar el nuevo conjunto soplado central-barrera flip |

### Procedimiento de regulación 

La regulación de la intensidad del soplado se realiza mediante software. Además, apretando o aflojando la misma cantidad los prisioneros de regulación de los soplados radiales, es posible estrangular o relajar el flujo de aire que llega al soplado central.

## Aplicaciones recomendadas

Son preferibles al desviador estándar cuando:
- es necesario manipular componentes que presentan detalles o salientes de tamaño reducido que podrían quedar atrapados en el hueco entre el desviador y la superficie o el disco rígido;
- se utiliza una superficie o un disco rígido anti-roll.

## Comprobación del correcto funcionamiento

Unos soplados radiales bien regulados se comportan del siguiente modo:

* El soplado situado antes del flip lleva los componentes a aproximadamente la mitad del radio del FlexiBowl®, donde el flip es más eficaz para voltear y separar las piezas;

* El soplado central aleja las piezas de la cubierta de sujeción del disco para evitar colisiones con la herramienta de agarre;

* El soplado situado después del flip aleja ligeramente los componentes del borde del FlexiBowl®, de modo que se eviten posibles colisiones con la herramienta de agarre.