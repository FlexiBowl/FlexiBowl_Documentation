# **Configuración de la interfaz**


:::{note}
Si el sistema utilizado es **FlexiVision One**, la configuración se gestiona íntegramente desde su interfaz dedicada. No es necesario utilizar la interfaz de software FlexiBowl® descrita en esta sección. Consulte el {ref}`Manual de FlexiVision One <flexivision_one>`.
:::

## Primer arranque

En el primer arranque del sistema, siga el procedimiento guiado que se indica a continuación para configurar la comunicación y preparar el FlexiBowl® para su uso.

::::{list-table}
:widths: 10 90
:header-rows: 1

* - Paso
  - Operación

* - 1
  - Introduzca la **dirección IP** del FlexiBowl® en la barra de direcciones del navegador para acceder a la interfaz de software. La dirección IP predeterminada del FlexiBowl® es `192.168.1.10`.

* - 2
  - Se abre la **página de inicio**. Seleccione el **idioma** deseado en el menú desplegable de la parte superior derecha.

* - 3
  - Abra la página **Setup** desde el menú lateral.

* - 4
  - Haga clic en **Get IP** para leer los parámetros de red actuales del dispositivo.

* - 5
  - Introduzca en los campos correspondientes la **nueva dirección IP** que desea asignar al FlexiBowl® y haga clic en **Set IP**.

* - 6
  - Seleccione el **tipo de comunicación** deseado en el menú desplegable. La opción predeterminada es **TCP Server**.

    :::{note}
    El modo **Digital I/O** no está incluido en la configuración estándar, pero está disponible como opción que se adquiere por separado.
    :::

* - 7
  - Haga clic en **Apply** para confirmar los ajustes de comunicación.

* - 8
  - Haga clic en **Reboot** para reiniciar el software y que los cambios surtan efecto.

::::

:::{important}
Tras el reinicio, vuelva a conectarse al FlexiBowl® utilizando la nueva dirección IP establecida en el paso 5.
:::

## Activación del Backlight (si es necesario)

Si se requiere la calibración del sistema de visión, active la retroiluminación antes de continuar:

::::{list-table}
:widths: 10 90
:header-rows: 0

* - 1
  - Abra la página **Main Command** desde el menú lateral.

* - 2
  - Seleccione **OPTION** en el menú desplegable **«Chose Visualization Page»**.

* - 3
  - Active el interruptor **Backlight 1** y/o **Backlight 2** según sea necesario.

::::