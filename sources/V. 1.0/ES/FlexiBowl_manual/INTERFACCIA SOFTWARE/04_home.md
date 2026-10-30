# **Home**

La nueva interfaz del FlexiBowl® está totalmente basada en web. Para acceder a ella basta con introducir la dirección IP por defecto del FlexiBowl® `192.168.1.10` en la barra de direcciones de su navegador.

## Descripción general

La página **Home** es la pantalla principal de la interfaz de software del FlexiBowl®. Se muestra al arrancar el sistema y ofrece al operador una visión general inmediata del estado del dispositivo, además de permitir el acceso a las funciones principales.
![página de inicio](../../../../_shared/media/images/home.png)

| Elemento | Posición | Descripción |
|---|---|---|
| **Menú** (☰) | Arriba a la izquierda | Abre el menú lateral de navegación principal, que permite acceder a todas las secciones del software (parámetros, diagnóstico, historial, ajustes, etc.) |
| **Icono de estado** (READY ✓) | Centro izquierda | Indica el estado operativo actual del sistema. El icono verde con la marca de verificación y el rótulo **READY** señala que el sistema está listo para funcionar |
| **Icono de usuario** | Centro derecha | Permite gestionar el perfil de usuario activo (inicio de sesión, cierre de sesión, cambio de usuario) |
| **Pulsante ENABLE MOTOR** | Arriba a la derecha | Habilita el motor del FlexiBowl®. |
| **Selector de idioma** | Debajo de ENABLE MOTOR | Menú desplegable para seleccionar el idioma de la interfaz. Muestra la bandera del idioma activo (p. ej. 🇺🇸 English) |

---

## Menú

<style>
.home-menu-wrap {
  display: flex;
  gap: 1.5rem;
  align-items: flex-start;
  margin: 1rem 0 1.5rem;
  flex-wrap: wrap;
}
.home-menu-img {
  flex: 0 0 auto;
  width: 200px;
  border: 1px solid #e2eef6;
  border-radius: 10px;
  overflow: hidden;
}
.home-menu-img img { display: block; width: 100%; }
.home-menu-cards {
  flex: 1 1 420px;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0.75rem;
}
@media (max-width: 560px) {
  .home-menu-cards { grid-template-columns: 1fr; }
}
.home-menu-card {
  display: block;
  padding: 0.7rem 0.9rem;
  border: 1.5px solid #d0e4f0;
  border-radius: 8px;
  background: #fff;
  text-decoration: none;
  color: inherit;
  transition: border-color 0.18s, background 0.18s;
}
.home-menu-card:hover {
  border-color: #2980b9;
  background: #f0f7ff;
  text-decoration: none;
}
.home-menu-card-title {
  font-weight: 700;
  font-size: 0.88rem;
  color: #1a3a52;
}
.home-menu-card-sub {
  font-size: 0.78rem;
  color: #556b7d;
  margin-top: 0.2rem;
  line-height: 1.35;
}
</style>

El menú lateral, que se abre con el icono ☰, da acceso a todas las páginas de la interfaz:

<div class="home-menu-wrap">
<div class="home-menu-img">

```{image} ../../../../_shared/media/images/menu_laterale.png
:alt: Menú lateral de navegación
```

</div>
<div class="home-menu-cards">

<a class="home-menu-card" href="04_home.html">
<div class="home-menu-card-title">Home</div>
<div class="home-menu-card-sub">Pantalla principal con el estado del sistema y acceso rápido a las funciones</div>
</a>

<a class="home-menu-card" href="04b_maincommand.html">
<div class="home-menu-card-title">Main Command</div>
<div class="home-menu-card-sub">Configura las opciones generales de la unidad y los movimientos Move y Shake (pestañas Option, Move, Shake)</div>
</a>

<a class="home-menu-card" href="04c_sequence.html">
<div class="home-menu-card-title">Sequence</div>
<div class="home-menu-card-sub">Crea y edita secuencias de alimentación directamente desde la interfaz</div>
</a>

<a class="home-menu-card" href="04d_monitor.html">
<div class="home-menu-card-title">Monitor</div>
<div class="home-menu-card-sub">Vista en tiempo real del estado del FlexiBowl®, con registro de eventos con marca de tiempo</div>
</a>

<a class="home-menu-card" href="04e_jogmotor.html">
<div class="home-menu-card-title">Jog Motor</div>
<div class="home-menu-card-sub">Movimiento manual del motor, útil durante la puesta a punto, las pruebas o la resolución de problemas</div>
</a>

<a class="home-menu-card" href="04f_wizard.html">
<div class="home-menu-card-title">Wizard Param</div>
<div class="home-menu-card-sub">Procedimiento guiado paso a paso para la configuración del FlexiBowl®</div>
</a>

<a class="home-menu-card" href="manual.html">
<div class="home-menu-card-title">Manual</div>
<div class="home-menu-card-sub">Permite consultar la documentación del dispositivo directamente desde la interfaz</div>
</a>

<a class="home-menu-card" href="04h_graphs.html">
<div class="home-menu-card-title">Graphs</div>
<div class="home-menu-card-sub">Panel con los gráficos en tiempo real de las magnitudes eléctricas y térmicas del driver del motor</div>
</a>

<a class="home-menu-card" href="04i_filetransfer.html">
<div class="home-menu-card-title">File Transfer</div>
<div class="home-menu-card-sub">Transferencia de parámetros y recetas desde y hacia copias de seguridad de la unidad</div>
</a>

<a class="home-menu-card" href="04l_setup.html">
<div class="home-menu-card-title">Setup</div>
<div class="home-menu-card-sub">Configuración de red, selección del protocolo de comunicación y otros ajustes del sistema</div>
</a>

<a class="home-menu-card" href="04m_hopper.html">
<div class="home-menu-card-title">Hopper</div>
<div class="home-menu-card-sub">Configuración y control de los Bulk Feeders conectados (ID, amplitud, frecuencia, tiempo de activación)</div>
</a>

<a class="home-menu-card" href="04n_emptying.html">
<div class="home-menu-card-title">Emptying</div>
<div class="home-menu-card-sub">Vaciado automático del plato encadenando hasta 4 secuencias con bucles configurables</div>
</a>

</div>
</div>



---
## Notas operativas

:::{attention}   
Antes de habilitar el motor, comprobar que el estado del sistema sea **READY** (icono verde visible en la barra superior). Si el icono no es verde, revisar los mensajes de error en las secciones de diagnóstico.
:::

:::{note}  
El idioma seleccionado desde la página Home se aplica a toda la interfaz de software. El cambio es inmediato y no requiere reiniciar el sistema.
:::
