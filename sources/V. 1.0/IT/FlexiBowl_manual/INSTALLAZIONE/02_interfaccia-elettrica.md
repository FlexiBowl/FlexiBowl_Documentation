(intele)=
# **[ELE]** Interfaccia Elettrica

Il pannello connettori del FlexiBowl® varia in base alla versione della macchina:

:::{raw} html
<style>
*{box-sizing:border-box;margin:0;padding:0}
:root{
  --acc:#1a6fc4;--acc-dk:#0d4a8a;--acc-bg:#e8f1fb;
  --bd:#e0e0e0;--bg-p:#ffffff;--bg-s:#f7f8f9;--bg-h:#f0f4fa;
  --tx1:#1a1a1a;--tx2:#555;--tx3:#888;
  --r:10px;--tr:0.35s cubic-bezier(.4,0,.2,1);
}
.ie-tabs{display:flex;gap:6px;margin-bottom:12px}
.ie-tab{padding:5px 14px;border-radius:6px;border:1.5px solid var(--bd);background:#fff;font-size:13px;font-weight:600;color:var(--tx2);cursor:pointer;transition:background var(--tr),color var(--tr),border-color var(--tr)}
.ie-tab:hover{background:var(--bg-h)}
.ie-tab.on{background:var(--acc-bg);color:var(--acc-dk);border-color:var(--acc)}
.ie-panel{display:none}
.ie-panel.on{display:block}
.ie-wrap{border:1px solid var(--bd);border-radius:var(--r);overflow:hidden;background:var(--bg-p);box-shadow:0 2px 12px rgba(0,0,0,0.07)}
.ie-img-outer{position:relative;width:100%;padding-top:70.71%}
.ie-img-outer img{position:absolute;inset:0;width:100%;height:100%;object-fit:contain;padding:0;transition:opacity var(--tr)}
.ie-img-base{opacity:1;z-index:1}
.ie-img-hl{opacity:0;z-index:2}
.ie-badge{position:absolute;top:12px;left:14px;z-index:3;background:var(--acc);color:#fff;font-size:12px;font-weight:600;padding:4px 10px;border-radius:20px;opacity:0;transform:translateY(-4px);transition:opacity var(--tr),transform var(--tr);pointer-events:none;white-space:nowrap}
.ie-badge.on{opacity:1;transform:translateY(0)}
.ie-hint{position:absolute;bottom:14px;left:50%;z-index:3;transform:translateX(-50%);font-size:13px;color:#fff;background:rgba(0,0,0,0.38);padding:6px 16px;border-radius:20px;pointer-events:none;transition:opacity var(--tr);white-space:nowrap}
.ie-list-panel{border-top:1px solid var(--bd);background:var(--bg-p)}
.ie-list-head{display:grid;grid-template-columns:40px 1fr;gap:8px;padding:8px 14px;background:var(--bg-s);border-bottom:1px solid var(--bd);font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:.05em;color:var(--tx3)}
.ie-row{display:grid;grid-template-columns:40px 1fr;gap:8px;align-items:center;padding:9px 14px;border-bottom:1px solid var(--bd);cursor:pointer;transition:background var(--tr);user-select:none}
.ie-row:last-child{border-bottom:none}
.ie-row:hover{background:var(--bg-h)}
.ie-row.on{background:var(--acc-bg)}
.ie-bubble{width:26px;height:26px;border-radius:50%;border:1.5px solid var(--bd);background:#fff;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:600;color:var(--tx2);flex-shrink:0;transition:background var(--tr),color var(--tr),border-color var(--tr)}
.ie-row.on .ie-bubble{background:var(--acc);color:#fff;border-color:var(--acc)}
.ie-name{font-size:13px;font-weight:500;color:var(--tx1);transition:color var(--tr)}
.ie-row.on .ie-name{color:var(--acc-dk)}
</style>

<!-- Tab bar -->
<div class="ie-tabs">
  <button class="ie-tab on" onclick="ieSwitchTab('rack',this)">Rack</button>
  <button class="ie-tab"    onclick="ieSwitchTab('stpanel',this)">Pannello Standard</button>
  <button class="ie-tab"    onclick="ieSwitchTab('encpanel',this)">Pannello Flexitracking</button>
</div>

<!-- ══════════ RACK ══════════ -->
<div class="ie-panel on" id="ie-panel-rack">
  <div class="ie-wrap">
    <div class="ie-img-outer">
      <img class="ie-img-base" id="rack-img-base" src="../../../../_shared/media/images/rack0.PNG" alt="Rack FlexiBowl®" />
      <img class="ie-img-hl"   id="rack-img-hl"   src="" alt="" aria-hidden="true" />
      <div class="ie-badge" id="rack-badge"></div>
      <div class="ie-hint"  id="rack-hint">Seleziona un connettore dalla lista</div>
    </div>
    <div class="ie-list-panel">
      <div class="ie-list-head"><span>N.</span><span>Connettore</span></div>
      <div id="rack-list"></div>
    </div>
  </div>
</div>

<!-- ══════════ PANNELLO STANDARD ══════════ -->
<div class="ie-panel" id="ie-panel-stpanel">
  <div class="ie-wrap">
    <div class="ie-img-outer">
      <img class="ie-img-base" id="stpanel-img-base" src="../../../../_shared/media/images/stpanel0.PNG" alt="Pannello Standard FlexiBowl®" />
      <img class="ie-img-hl"   id="stpanel-img-hl"   src="" alt="" aria-hidden="true" />
      <div class="ie-badge" id="stpanel-badge"></div>
      <div class="ie-hint"  id="stpanel-hint">Seleziona un connettore dalla lista</div>
    </div>
    <div class="ie-list-panel">
      <div class="ie-list-head"><span>N.</span><span>Connettore</span></div>
      <div id="stpanel-list"></div>
    </div>
  </div>
</div>

<!-- ══════════ PANNELLO FLEXITRACKING ══════════ -->
<div class="ie-panel" id="ie-panel-encpanel">
  <div class="ie-wrap">
    <div class="ie-img-outer">
      <img class="ie-img-base" id="encpanel-img-base" src="../../../../_shared/media/images/encpanel0.PNG" alt="Pannello Flexitracking FlexiBowl®" />
      <img class="ie-img-hl"   id="encpanel-img-hl"   src="" alt="" aria-hidden="true" />
      <div class="ie-badge" id="encpanel-badge"></div>
      <div class="ie-hint"  id="encpanel-hint">Seleziona un connettore dalla lista</div>
    </div>
    <div class="ie-list-panel">
      <div class="ie-list-head"><span>N.</span><span>Connettore</span></div>
      <div id="encpanel-list"></div>
    </div>
  </div>
</div>

<script>
(function(){

  var models = {
    rack: {
      imgPath: '../../../../_shared/media/images/rack',
      imgExt: '.PNG',
      comps: [
        {n:1, name:'Presa di corrente e interruttore'},
        {n:2, name:'Connettore STO'},
        {n:3, name:'Connettore cavo motore'},
        {n:4, name:'Connettore C-A signal'},
        {n:5, name:'Connettore C-B Signal'},
        {n:6, name:'Ingresso Ethernet'},
        {n:7, name:'Connettore tramoggia'},
        {n:8, name:'Collegamento Ethernet al FlexiBowl\u00ae'}
      ]
    },
    stpanel: {
      imgPath: '../../../../_shared/media/images/stpanel',
      imgExt: '.PNG',
      comps: [
        {n:1, name:'Presa di corrente e interruttore'},
        {n:2, name:'Ingresso aria'},
        {n:3, name:'LED di stato backlight'},
        {n:4, name:'LED di stato Ready/Fault'},
        {n:5, name:'Connettore tramoggia'},
        {n:6, name:'Ingresso Ethernet'},
        {n:7, name:'Connettore STO'}
      ]
    },
    encpanel: {
      imgPath: '../../../../_shared/media/images/encpanel',
      imgExt: '.PNG',
      comps: [
        {n:1, name:'Presa di corrente e interruttore'},
        {n:2, name:'LED di stato backlight'},
        {n:3, name:'LED di stato Ready/Fault'},
        {n:4, name:'Connettore tramoggia'},
        {n:5, name:'Ingresso Ethernet'},
        {n:6, name:'Passaggio cavo encoder'},
        {n:7, name:'Ingresso aria'},
        {n:8, name:'Connettore I/O'},
        {n:9, name:'Connettore STO'}
      ]
    }
  };

  var state = {};
  Object.keys(models).forEach(function(id){ state[id]={activeN:null,activeRow:null}; });

  Object.keys(models).forEach(function(id){
    var m  = models[id];
    var el = document.getElementById(id+'-list');
    m.comps.forEach(function(c){
      var row = document.createElement('div');
      row.className = 'ie-row';
      row.innerHTML = '<div class="ie-bubble">'+c.n+'</div>'
                    + '<div class="ie-name">'+c.name+'</div>';
      row.addEventListener('click', function(){ toggle(id, c, row); });
      el.appendChild(row);
    });
  });

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

  function reset(id){
    var s       = state[id];
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

  window.ieSwitchTab = function(id, btn){
    document.querySelectorAll('.ie-panel.on').forEach(function(p){
      var oldId = p.id.replace('ie-panel-','');
      reset(oldId);
    });
    document.querySelectorAll('.ie-tab').forEach(function(b){ b.classList.remove('on'); });
    document.querySelectorAll('.ie-panel').forEach(function(p){ p.classList.remove('on'); });
    btn.classList.add('on');
    document.getElementById('ie-panel-'+id).classList.add('on');
  };

})();
</script>
:::