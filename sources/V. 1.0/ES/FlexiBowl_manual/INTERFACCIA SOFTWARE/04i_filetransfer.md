# **File Transfer**

## Descripción general

La página **File Transfer** permite exportar e importar la configuración completa de los parámetros del FlexiBowl®, transfiriendo los datos entre el sistema y un PC. Es la función dedicada a la copia de seguridad y la restauración de la configuración operativa.

![página file transfer](../../../../_shared/media/images/file_transfer.png)

---

## Funciones disponibles

### DOWNLOAD FILE — Guardado de parámetros (FlexiBowl® → PC)

El panel superior, etiquetado **«Save the Current Parameters, from FlexiBowl® to PC»**, permite exportar a un archivo todos los parámetros configurados actualmente en el sistema.

Al pulsar el botón **DOWNLOAD FILE**, el software genera un archivo de configuración y lo pone a disposición para guardarlo en el PC conectado.

:::{tip}
Realice un **DOWNLOAD FILE** antes de cualquier modificación significativa de los parámetros operativos. El archivo descargado constituye una copia de seguridad completa de la configuración y permite restablecer rápidamente el estado anterior en caso de error.
:::

---

### UPLOAD FILE — Carga de parámetros (PC → FlexiBowl®)

El panel inferior, etiquetado **«Load in the Current Parameters, from PC to FlexiBowl®»**, permite importar al sistema un archivo de configuración guardado previamente.

Al pulsar el botón **UPLOAD FILE** se abre el selector de archivos del sistema operativo. Una vez seleccionado el archivo, los parámetros se cargan en el FlexiBowl® y se aplican inmediatamente.

:::{warning}
La carga de un archivo de configuración **sobrescribe todos los parámetros actuales** del sistema. Antes de continuar, asegúrese de que el archivo seleccionado sea compatible con el modelo de FlexiBowl® en uso y con la versión de software instalada.
:::

:::{warning}
No apague el sistema ni interrumpa la conexión durante la transferencia del archivo. Una interrupción durante la carga podría provocar una configuración incompleta o dañada.
:::

---

## Indicadores de estado de la transferencia

En la parte inferior de la página hay tres indicadores luminosos (LED virtuales) que señalan el resultado de la operación de transferencia.

| Indicador | Color activo | Descripción |
|---|---|---|
| **Active** | 🟡 Amarillo | La transferencia está en curso |
| **Successful** | 🟢 Verde | La transferencia se ha completado correctamente |
| **Error** | 🔴 Rojo | Se ha producido un error durante la transferencia |

:::{note}
Durante una operación de descarga o carga, espere a que se encienda el LED **Successful** antes de continuar con otras operaciones. Si se enciende el LED **Error**, compruebe la conexión con el PC y repita la operación.
:::
