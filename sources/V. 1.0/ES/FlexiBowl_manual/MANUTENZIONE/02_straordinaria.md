# **Mantenimiento extraordinario**

:::{warning}
El mantenimiento extraordinario y la reparación de la máquina están reservados a técnicos cualificados, formados y autorizados, empleados del Fabricante o del centro de servicio autorizado. Estas intervenciones requieren un conocimiento profundo y especializado de las máquinas, de las operaciones necesarias, de los riesgos asociados y de los procedimientos correctos para trabajar con seguridad.
:::

Si se producen eventos excepcionales que requieran intervenciones de mantenimiento extraordinario, el personal de mantenimiento ordinario del usuario debe seguir estos procedimientos:
- comprobar el estado de los grupos dañados o desfasados;
- realizar las operaciones descritas en este apartado;
- si las operaciones que se deben realizar no están contempladas en este manual, enviar al Fabricante el informe de los hechos ocurridos, el resultado de la inspección y las posibles observaciones.

El Fabricante o el centro de servicio autorizado evaluará la situación caso por caso. A continuación acordará con el personal de mantenimiento ordinario el tipo de intervención que se debe realizar, eligiendo la solución más adecuada entre las que se enumeran a continuación:
- el Fabricante envía a un técnico autorizado, formado y cualificado para realizar las intervenciones necesarias;
- o bien el Fabricante autoriza al personal de mantenimiento ordinario del usuario a realizar las intervenciones, enviando las instrucciones adicionales que correspondan.

:::{warning}
Los repuestos que se deben sustituir deben pedirse a ARS S.r.l.

Si el cliente no utiliza repuestos originales o autorizados por escrito por el Fabricante, este queda exento de toda responsabilidad sobre el funcionamiento de la máquina y la seguridad de los operarios. La autorización y/o las instrucciones deben comunicarse siempre por escrito. A falta de autorización escrita, está prohibido operar y el Fabricante declina toda responsabilidad.
:::

:::{warning}
Las operaciones de mantenimiento deben ser realizadas únicamente por personal cualificado y autorizado.
:::

::::{warning}
<table style="width: 100%; border: none; background: transparent;">
  <tr style="background: transparent !important; border: none !important;">
    <td style="width: 10%; border: none; vertical-align: middle; text-align: center; background: transparent !important;">
      <img src="../../../../_shared/media/images/corrente.png" style="width: 50px; height: auto;">
    </td>
    <td style="width: 90%; border: none; vertical-align: middle; background: transparent !important; padding-left: 15px;">
      Desconecte la alimentación eléctrica antes de retirar la cubierta.
    </td>
  </tr>
</table>
::::

:::{warning}
Desconecte la alimentación eléctrica y neumática antes de proceder con las operaciones de mantenimiento.
:::

:::{note}
Al fijar los tornillos, utilice siempre LOCTITE 243 para lograr un apriete perfecto (salvo en los tornillos de la brida de la superficie o del disco rígido del FlexiBowl®).
:::

## Grupos de intervención potenciales

Los grupos que componen el FlexiBowl® son los siguientes:

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
  <button class="fb-tab on"    onclick="fbSwitchTab('fb200',this)">FB200</button>
  <button class="fb-tab"    onclick="fbSwitchTab('fb350',this)">FB350</button>
  <button class="fb-tab" onclick="fbSwitchTab('fb650',this)">FB500-650-800-1200</button>
</div>

<!-- ══════════ FB650 ══════════ -->
<div class="fb-panel" id="fb-panel-fb650">
  <div class="fb-wrap">
    <div class="fb-img-outer">
      <img class="fb-img-base" id="fb650-img-base" src="../../../../_shared/media/images/component_default.PNG" alt="Vista del FlexiBowl® 650" />
      <img class="fb-img-hl"   id="fb650-img-hl"   src="" alt="" aria-hidden="true" />
      <div class="fb-badge" id="fb650-badge"></div>
      <div class="fb-hint"  id="fb650-hint">Seleccione un componente de la lista</div>
    </div>
    <div class="fb-list-panel">
      <div class="fb-list-head"><span>N.º</span><span>Componente</span><span>Descripción</span></div>
      <div id="fb650-list"></div>
    </div>
  </div>
</div>

<!-- ══════════ FB350 ══════════ -->
<div class="fb-panel" id="fb-panel-fb350">
  <div class="fb-wrap">
    <div class="fb-img-outer">
      <img class="fb-img-base" id="fb350-img-base" src="../../../../_shared/media/images/FB350-0.PNG" alt="Vista del FlexiBowl® 350" />
      <img class="fb-img-hl"   id="fb350-img-hl"   src="" alt="" aria-hidden="true" />
      <div class="fb-badge" id="fb350-badge"></div>
      <div class="fb-hint"  id="fb350-hint">Seleccione un componente de la lista</div>
    </div>
    <div class="fb-list-panel">
      <div class="fb-list-head"><span>N.º</span><span>Componente</span><span>Descripción</span></div>
      <div id="fb350-list"></div>
    </div>
  </div>
</div>

<!-- ══════════ FB200 ══════════ -->
<div class="fb-panel on" id="fb-panel-fb200">
  <div class="fb-wrap">
    <div class="fb-img-outer">
      <img class="fb-img-base" id="fb200-img-base" src="../../../../_shared/media/images/FB200-0.PNG" alt="Vista del FlexiBowl® 200" />
      <img class="fb-img-hl"   id="fb200-img-hl"   src="" alt="" aria-hidden="true" />
      <div class="fb-badge" id="fb200-badge"></div>
      <div class="fb-hint"  id="fb200-hint">Seleccione un componente de la lista</div>
    </div>
    <div class="fb-list-panel">
      <div class="fb-list-head"><span>N.º</span><span>Componente</span><span>Descripción</span></div>
      <div id="fb200-list"></div>
    </div>
  </div>
</div>

<script>
(function(){

  /* ── dati componenti ── */
  var models = {
    fb650: {
      imgPath: '../../../../_shared/media/images/component_',
      imgDefault: '../../../../_shared/media/images/component_default.PNG',
      imgExt: '.PNG',
      comps: [
        {n:1,  name:'Grupo neumático',           desc:'Alimentan el grupo flip y los posibles soplos.'},
        {n:2,  name:'Grupo motor',               desc:'Permite la rotación de la superficie o del disco rígido.'},
        {n:3,  name:'Anillo de contención',      desc:'Compuesto por varios sectores, impide la salida de las piezas durante el funcionamiento. Contiene también los desviadores en ausencia de accesorios.'},
        {n:4,  name:'Backlight',                   desc:'Retroilumina el área de visión para resaltar los contornos de las piezas.'},
        {n:5,  name:'Pantalla flip',                desc:'Impide la salida de las piezas durante el volteo.'},
        {n:6,  name:'Carter',                      desc:'Contiene y protege los elementos internos. Protege al usuario de la exposición a tensión eléctrica y a componentes en movimiento.'},
        {n:7,  name:'Grupo flip',                 desc:'Percutor accionado por una semicorredera neumática (350–1200) o un cilindro neumático (200). Genera un impulso para voltear los objetos antes de la ventana de visión.'},
        {n:8,  name:'Bastidor',                      desc:'Es la estructura portante del FlexiBowl®.'},
        {n:9, name:'Grupo electrónico',          desc:'Incluye toda la electrónica de control del FlexiBowl®.'},
        {n:10, name:'Panel de conectores',         desc:'Incluye todas las conexiones eléctricas y neumáticas.'},
        {n:11, name:'Soporte de superficie / disco', desc:'Mantiene la superficie o el disco rígido firmemente sujeto al grupo motor.'},
        {n:12, name:'Placas de cubierta',        desc:'Permiten un fácil acceso a los componentes internos para el mantenimiento.'}
      ]
    },
    fb350: {
      imgPath: '../../../../_shared/media/images/FB350-',
      imgDefault: '../../../../_shared/media/images/FB350-0.PNG',
      imgExt: '.PNG',
      comps: [
        {n:1,  name:'Cables y alargadores',  desc:'Son las conexiones electrónicas entre los distintos componentes internos del FlexiBowl®.'},
        {n:2,  name:'Grupo neumático', desc:'Alimenta el grupo flip y los soplos.'},
        {n:3,  name:'Grupo motor',     desc:'Permite la rotación del disco rígido.'},
        {n:4,  name:'Disco',             desc:'<a href="../ACCESSORI/02_DISCHI_RIGIDI.html">Véase el apartado dedicado</a>.'},
        {n:5,  name:'Backlight',         desc:'Retroilumina el área de visión para resaltar los contornos de las piezas.'},
        {n:6,  name:'Pantalla flip',      desc:'Impide la salida de las piezas durante el volteo. Incluye también los <a href="../ACCESSORI/06-4_INTEGRATI.html">soplos</a>.'},
        {n:7,  name:'Carter',            desc:'Contiene y protege los elementos internos. Protege al usuario de la exposición a tensión eléctrica y a componentes en movimiento.'},
        {n:8,  name:'Grupo flip',       desc:'Percutor accionado por un cilindro neumático (200). Genera un impulso para voltear los objetos antes de la ventana de visión.'},
        {n:9,  name:'Bastidor',            desc:'Es la estructura portante del FlexiBowl®.'},
        {n:10, name:'Soporte de disco',    desc:'Mantiene el disco rígido firmemente sujeto al grupo motor.'},
        {n:11, name:'Rack',              desc:'Contiene toda la electrónica del FlexiBowl®.'}
      ]
    },
    fb200: {
      imgPath: '../../../../_shared/media/images/FB200-',
      imgDefault: '../../../../_shared/media/images/FB200-0.PNG',
      imgExt: '.PNG',
      comps: [
        {n:1,  name:'Cables y alargadores',  desc:'Son las conexiones electrónicas entre los distintos componentes internos del FlexiBowl®.'},
        {n:2,  name:'Grupo neumático', desc:'Alimenta el grupo flip y los soplos.'},
        {n:3,  name:'Grupo motor',     desc:'Permite la rotación del disco rígido.'},
        {n:4,  name:'Disco',             desc:'<a href="../ACCESSORI/02_DISCHI_RIGIDI.html">Véase el apartado dedicado</a>.'},
        {n:5,  name:'Backlight',         desc:'Retroilumina el área de visión para resaltar los contornos de las piezas.'},
        {n:6,  name:'Pantalla flip',      desc:'Impide la salida de las piezas durante el volteo. Incluye también los <a href="../ACCESSORI/06-4_INTEGRATI.html">soplos</a>.'},
        {n:7,  name:'Carter',            desc:'Contiene y protege los elementos internos. Protege al usuario de la exposición a tensión eléctrica y a componentes en movimiento.'},
        {n:8,  name:'Grupo flip',       desc:'Percutor accionado por un cilindro neumático (200). Genera un impulso para voltear los objetos antes de la ventana de visión.'},
        {n:9,  name:'Bastidor',            desc:'Es la estructura portante del FlexiBowl®.'},
        {n:10, name:'Rack',              desc:'Contiene toda la electrónica del FlexiBowl®.'}
      ]
    }
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

:::{toctree}
:hidden:
02-1_sost-backlight.md
02-2_sost-ev.md
02-3_sost-vp.md
02-4_sost-flip.md
02-11_sost-mot.md
02-12_sost-ele.md
:::