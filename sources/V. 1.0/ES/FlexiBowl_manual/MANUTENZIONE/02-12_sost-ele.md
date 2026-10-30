# **Sustitución de los componentes electrónicos**

:::::{important}

:::{raw} html
   <style>
     .ars-img-row { display: flex; gap: 12px; align-items: center; justify-content: center; }
     .ars-img-row img { width: 25%; }
   </style>
:::

::::{list-table}
:widths: 30 60
:header-rows: 1
* - {ref}`Cualificación del operario <operatori>`
  - {ref}`EPI necesarios <dpi>`

* - **Técnico de mantenimiento eléctrico**
  - :::{raw} html
       <div class="ars-img-row">
         <img src="../../../../_shared/media/images/guanti.png" alt="guantes">
         <img src="../../../../_shared/media/images/scarpe.png" alt="calzado">
         <img src="../../../../_shared/media/images/tuta.png" alt="mono">
       </div>
    :::
::::
:::::

::::{warning}
<table style="width: 100%; border: none; background: transparent;">
  <tr style="background: transparent !important; border: none !important;">
    <td style="width: 10%; border: none; vertical-align: middle; text-align: center; background: transparent !important;">
      <img src="../../../../_shared/media/images/corrente.png" style="width: 50px; height: auto;">
    </td>
    <td style="width: 90%; border: none; vertical-align: middle; background: transparent !important; padding-left: 15px;">
      Desconecte la alimentación eléctrica antes de realizar cualquier operación en el interior del FlexiBowl®.
    </td>
  </tr>
</table>
::::

## Sustitución de las principales partes electrónicas

En los tamaños más pequeños toda la electrónica está contenida en el rack, por lo que basta con desmontar el panel superior para acceder a todos los componentes. En los FlexiBowl® de tamaño 500 o superior, en cambio, todas las partes están alojadas en la máquina.

:::{raw} html
<style>
*{box-sizing:border-box;margin:0;padding:0}
:root{
  --acc:#1a6fc4;--acc-dk:#0d4a8a;--acc-bg:#e8f1fb;
  --bd:#e0e0e0;--bg-p:#ffffff;--bg-s:#f7f8f9;--bg-h:#f0f4fa;
  --tx1:#1a1a1a;--tx2:#555;--tx3:#888;
  --r:10px;--tr:0.35s cubic-bezier(.4,0,.2,1);
}

/* ── Tab bar ── */
.fb-tabs{display:flex;gap:6px;margin-bottom:12px}
.fb-tab{padding:5px 14px;border-radius:6px;border:1.5px solid var(--bd);background:#fff;font-size:13px;font-weight:600;color:var(--tx2);cursor:pointer;transition:background var(--tr),color var(--tr),border-color var(--tr)}
.fb-tab:hover{background:var(--bg-h)}
.fb-tab.on{background:var(--acc-bg);color:var(--acc-dk);border-color:var(--acc)}

/* ── Panel ── */
.fb-panel{display:none}
.fb-panel.on{display:block}
.fb-wrap{border:1px solid var(--bd);border-radius:var(--r);overflow:hidden;background:var(--bg-p);box-shadow:0 2px 12px rgba(0,0,0,0.07)}
.fb-img-outer{position:relative;width:100%;padding-top:70.71%}
.fb-img-outer img{position:absolute;inset:0;width:100%;height:100%;object-fit:contain;padding:0;transition:opacity var(--tr)}
.fb-img-base{opacity:1;z-index:1}
.fb-img-hl{opacity:0;z-index:2}
.fb-badge{position:absolute;top:12px;left:14px;z-index:3;background:var(--acc);color:#fff;font-size:12px;font-weight:600;padding:4px 10px;border-radius:20px;opacity:0;transform:translateY(-4px);transition:opacity var(--tr),transform var(--tr);pointer-events:none;white-space:nowrap}
.fb-badge.on{opacity:1;transform:translateY(0)}
.fb-hint{position:absolute;bottom:14px;left:50%;z-index:3;transform:translateX(-50%);font-size:13px;color:#fff;background:rgba(0,0,0,0.38);padding:6px 16px;border-radius:20px;pointer-events:none;transition:opacity var(--tr);white-space:nowrap}
.fb-list-panel{border-top:1px solid var(--bd);background:var(--bg-p)}
.fb-list-head{display:grid;grid-template-columns:40px 160px 1fr;gap:8px;padding:8px 14px;background:var(--bg-s);border-bottom:1px solid var(--bd);font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:.05em;color:var(--tx3)}
.fb-row{display:grid;grid-template-columns:40px 160px 1fr;gap:8px;align-items:center;padding:9px 14px;border-bottom:1px solid var(--bd);cursor:pointer;transition:background var(--tr);user-select:none}
.fb-row:last-child{border-bottom:none}
.fb-row:hover{background:var(--bg-h)}
.fb-row.on{background:var(--acc-bg)}
.fb-bubble{width:26px;height:26px;border-radius:50%;border:1.5px solid var(--bd);background:#fff;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:600;color:var(--tx2);flex-shrink:0;transition:background var(--tr),color var(--tr),border-color var(--tr)}
.fb-row.on .fb-bubble{background:var(--acc);color:#fff;border-color:var(--acc)}
.fb-name{font-size:13px;font-weight:500;color:var(--tx1);transition:color var(--tr)}
.fb-row.on .fb-name{color:var(--acc-dk)}
.fb-desc{font-size:12px;color:var(--tx2);line-height:1.55}
.fb-desc a{color:var(--acc);text-decoration:underline}
</style>

<!-- Tab bar -->
<div class="fb-tabs">
  <button class="fb-tab on"    onclick="fbSwitchTab('rack',this)">Electrónica en el rack</button>
  <button class="fb-tab"    onclick="fbSwitchTab('fb',this)">Electrónica en el FlexiBowl®</button>
</div>

<!-- ══════════ rack ══════════ -->
<div class="fb-panel on" id="fb-panel-rack">
  <div class="fb-wrap">
    <div class="fb-img-outer">
      <img class="fb-img-base" id="rack-img-base" src="../../../../_shared/media/images/inrack0.PNG" alt="Electrónica en el rack" />
      <img class="fb-img-hl"   id="rack-img-hl"   src="" alt="" aria-hidden="true" />
      <div class="fb-badge" id="rack-badge"></div>
      <div class="fb-hint"  id="rack-hint">Seleccione un componente de la lista</div>
    </div>
    <div class="fb-list-panel">
      <div class="fb-list-head"><span>N.º</span><span>Componente</span><span>Descripción</span></div>
      <div id="rack-list"></div>
    </div>
  </div>
</div>

<!-- ══════════ fb ══════════ -->
<div class="fb-panel" id="fb-panel-fb">
  <div class="fb-wrap">
    <div class="fb-img-outer">
      <img class="fb-img-base" id="fb-img-base" src="../../../../_shared/media/images/fbele0.PNG" alt="Electrónica en el FlexiBowl®" />
      <img class="fb-img-hl"   id="fb-img-hl"   src="" alt="" aria-hidden="true" />
      <div class="fb-badge" id="fb-badge"></div>
      <div class="fb-hint"  id="fb-hint">Seleccione un componente de la lista</div>
    </div>
    <div class="fb-list-panel">
      <div class="fb-list-head"><span>N.º</span><span>Componente</span><span>Descripción</span></div>
      <div id="fb-list"></div>
    </div>
  </div>
</div>

<script>
(function(){

  /* ── dati componenti ── */
  var models = {
    rack: {
      imgPath: '../../../../_shared/media/images/inrack',
      imgDefault: '../../../../_shared/media/images/inrack0.PNG',
      imgExt: '.PNG',
      comps: [
        {n:1,  name:'Grupo PLC y fuente de alimentación 24V',     desc:'Están fijados a un carril DIN; los módulos del PLC se pueden retirar individualmente'},
        {n:2,  name:'Fuente de alimentación 48V',                  desc:'Fijado a un carril DIN'},
        {n:3,  name:'Tarjeta',                            desc:'Su soporte está fijado a la bandeja inferior mediante dos separadores; contiene también los fusibles'},
        {n:4,  name:'Resistencia de frenado',           desc:'Fijada a la bandeja inferior con dos tornillos M4'},
      ]
    },
    fb: {
      imgPath: '../../../../_shared/media/images/fbele',
      imgDefault: '../../../../_shared/media/images/fbele0.PNG',
      imgExt: '.PNG',
      comps: [
        {n:1,  name:'Grupo PLC y fuente de alimentación 24V',     desc:'Están fijados a un carril DIN; los módulos del PLC se pueden retirar individualmente'},
        {n:2,  name:'Fuente de alimentación 48V',                  desc:'Fijado a un carril DIN'},
        {n:3,  name:'Resistencia de frenado',           desc:'Fijada a la bandeja inferior con dos tornillos M4 en el FlexiBowl® 500 y con cuatro tornillos M4 en los demás tamaños'},
      ]
    },
  };

  /* ── stato per modello ── */
  var state = {};
  Object.keys(models).forEach(function(id){ state[id]={activeN:null,activeRow:null}; });

  /* ── costruisce le liste ── */
  Object.keys(models).forEach(function(id){
    var m   = models[id];
    var el  = document.getElementById(id+'-list');
    m.comps.forEach(function(c){
      var row = document.createElement('div');
      row.className = 'fb-row';
      row.innerHTML = '<div class="fb-bubble">'+c.n+'</div>'
                    + '<div class="fb-name">'+c.name+'</div>'
                    + '<div class="fb-desc">'+c.desc+'</div>';
      row.addEventListener('click', function(){ toggle(id, c, row); });
      el.appendChild(row);
    });
  });

  /* ── toggle componente ── */
  function toggle(id, c, row){
    var s       = state[id];
    var m       = models[id];
    var imgBase = document.getElementById(id+'-img-base');
    var imgHl   = document.getElementById(id+'-img-hl');
    var badge   = document.getElementById(id+'-badge');
    var hint    = document.getElementById(id+'-hint');

    if(s.activeN === c.n){ reset(id); return; }
    if(s.activeRow) s.activeRow.classList.remove('on');
    row.classList.add('on');
    s.activeRow = row; s.activeN = c.n;

    badge.textContent = c.n + ' \u2014 ' + c.name;
    badge.classList.add('on');
    hint.style.opacity = '0';

    var newImg = new Image();
    newImg.onload = function(){
      imgHl.src = newImg.src;
      imgHl.style.opacity = '1';
      imgBase.style.opacity = '0';
    };
    newImg.onerror = function(){
      imgBase.style.opacity = '1';
      imgHl.style.opacity = '0';
    };
    newImg.src = m.imgPath + c.n + m.imgExt;
  }

  /* ── reset ── */
  function reset(id){
    var s       = state[id];
    var m       = models[id];
    var imgBase = document.getElementById(id+'-img-base');
    var imgHl   = document.getElementById(id+'-img-hl');
    var badge   = document.getElementById(id+'-badge');
    var hint    = document.getElementById(id+'-hint');

    if(s.activeRow) s.activeRow.classList.remove('on');
    s.activeRow = null; s.activeN = null;
    imgBase.style.opacity = '1';
    imgHl.style.opacity = '0';
    setTimeout(function(){ imgHl.src = ''; }, 350);
    badge.classList.remove('on');
    hint.style.opacity = '1';
  }

  /* ── switch tab ── */
  window.fbSwitchTab = function(id, btn){
    /* resetta il pannello attualmente attivo prima di cambiare */
    document.querySelectorAll('.fb-panel.on').forEach(function(p){
      var oldId = p.id.replace('fb-panel-','');
      reset(oldId);
    });
    document.querySelectorAll('.fb-tab').forEach(function(b){ b.classList.remove('on'); });
    document.querySelectorAll('.fb-panel').forEach(function(p){ p.classList.remove('on'); });
    btn.classList.add('on');
    document.getElementById('fb-panel-'+id).classList.add('on');
  };

})();
</script>
:::

En los FlexiBowl® de tamaño 500 o superior, la placa está anclada a un soporte fijado en la columna junto al backlight, en el lado del flip.

::: {figure} ../../../../_shared/media/images/schedapos.png
:align: center
:width: 90%
:::

:::{note}
En los FlexiBowl® de tamaño 650 o superior, toda la electrónica es accesible desde arriba retirando el iluminador del backlight y la tapa central de la plataforma superior. En el FlexiBowl® 500 puede ser más conveniente desmontar los cárteres para acceder lateralmente al grupo PLC/fuente de alimentación de 24 V y a la resistencia de frenado.
:::


(scheda-interfaccia)=
## Mantenimiento de la placa de interfaz

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
