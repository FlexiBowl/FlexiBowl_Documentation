(panoramica)=
# **Panoramica e Unboxing**

## Componenti principali del FlexiBowl®

Il FlexiBowl® è composto dalle seguenti parti fondamentali:

:::{raw} html
<style>
*{box-sizing:border-box;margin:0;padding:0}
:root{
  --acc:#1a6fc4;--acc-dk:#0d4a8a;--acc-bg:#e8f1fb;
  --bd:#e0e0e0;--bg-p:#ffffff;--bg-s:#f7f8f9;--bg-h:#f0f4fa;
  --tx1:#1a1a1a;--tx2:#555;--tx3:#888;
  --r:10px;--tr:0.35s cubic-bezier(.4,0,.2,1);
}
.fb-wrap{border:1px solid var(--bd);border-radius:var(--r);overflow:hidden;background:var(--bg-p);box-shadow:0 2px 12px rgba(0,0,0,0.07)}
.fb-img-outer{position:relative;width:100%;padding-top:70.71%}
.fb-img-outer img{position:absolute;inset:0;width:100%;height:100%;object-fit:contain;padding:0;transition:opacity var(--tr)}
#fb-img-base{opacity:1;z-index:1}
#fb-img-hl{opacity:0;z-index:2}
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
.fb-name{font-size:15px;font-weight:500;color:var(--tx1);transition:color var(--tr)}
.fb-row.on .fb-name{color:var(--acc-dk)}
.fb-desc{font-size:15px;color:var(--tx2);line-height:1.55}
</style>

<div class="fb-wrap">
  <div class="fb-img-outer">
    <img id="fb-img-base" src="../../../../_shared/media/images/component_default.PNG" alt="Vista esplosa FlexiBowl®" />
    <img id="fb-img-hl" src="" alt="" aria-hidden="true" />
    <div class="fb-badge" id="fb-badge"></div>
    <div class="fb-hint" id="fb-hint">Seleziona un componente dalla lista</div>
  </div>
  <div class="fb-list-panel">
    <div class="fb-list-head"><span>N.</span><span>Componente</span><span>Descrizione</span></div>
    <div id="fb-list"></div>
  </div>
</div>

<script>
(function(){
  var comps=[
    {n:1,name:"Cavi",desc:"Collegamenti elettrici tra le varie parti funzionali del FlexiBowl\u00ae."},
    {n:2,name:"Gruppo pneumatico",desc:"Alimentano il gruppo flip e gli eventuali soffi."},
    {n:3,name:"Gruppo motore",desc:"Consente la rotazione della superficie o disco rigido."},
    {n:4,name:"Anello di contenimento",desc:"Composto da diversi settori, impedisce la fuoriuscita dei pezzi durante il funzionamento. Contiene anche i deviatori in assenza di altri accessori."},
    {n:5,name:"Backlight",desc:"Retroillumina l\u2019area di visione per evidenziare i contorni dei pezzi."},
    {n:6,name:"Schermo flip",desc:"Impedisce la fuoriuscita dei pezzi durante il ribaltamento."},
    {n:7,name:"Carter",desc:"Contiene e protegge gli elementi interni. Protegge l\u2019utente da esposizioni a voltaggio elettrico e componenti in movimento."},
    {n:8,name:"Flip",desc:"Percussore azionato da semi slitta pneumatica (350\u20131200) o cilindro pneumatico (200). Genera un impulso per far ribaltare gli oggetti prima della finestra di visione."},
    {n:9,name:"Telaio",desc:"\u00c8 la struttura portante del FlexiBowl\u00ae."},
    {n:10,name:"Gruppo elettronico",desc:"Comprende tutta l\u2019elettronica di comando del FlexiBowl\u00ae."},
    {n:11,name:"Pannello connettori",desc:"Comprende tutti gli allacciamenti elettrici e pneumatici."},
    {n:12,name:"Supporto superficie / disco",desc:"Tiene la superficie o disco rigido saldamente fissati al gruppo motore."},
    {n:13,name:"Piastre di copertura",desc:"Consentono un facile accesso ai componenti interni per la manutenzione."}
  ];
  var imgBase=document.getElementById('fb-img-base');
  var imgHl=document.getElementById('fb-img-hl');
  var badge=document.getElementById('fb-badge');
  var hint=document.getElementById('fb-hint');
  var list=document.getElementById('fb-list');
  var activeN=null,activeRow=null;

  comps.forEach(function(c){
    var row=document.createElement('div');
    row.className='fb-row';
    row.innerHTML='<div class="fb-bubble">'+c.n+'</div><div class="fb-name">'+c.name+'</div><div class="fb-desc">'+c.desc+'</div>';
    row.addEventListener('click',function(){toggle(c,row);});
    list.appendChild(row);
  });

  function toggle(c,row){
    if(activeN===c.n){reset();return;}
    if(activeRow)activeRow.classList.remove('on');
    row.classList.add('on');
    activeRow=row;activeN=c.n;
    badge.textContent=c.n+' \u2014 '+c.name;
    badge.classList.add('on');
    hint.style.opacity='0';
    var newImg=new Image();
    newImg.onload=function(){
      imgHl.src=newImg.src;
      imgHl.style.opacity='1';
      imgBase.style.opacity='0';
    };
    newImg.onerror=function(){
      imgBase.style.opacity='1';
      imgHl.style.opacity='0';
    };
    newImg.src='../../../../_shared/media/images/component_'+c.n+'.PNG';
  }

  function reset(){
    if(activeRow)activeRow.classList.remove('on');
    activeRow=null;activeN=null;
    imgBase.style.opacity='1';
    imgHl.style.opacity='0';
    setTimeout(function(){imgHl.src='';},350);
    badge.classList.remove('on');
    hint.style.opacity='1';
  }
})();
</script>
:::

## What is in the box?