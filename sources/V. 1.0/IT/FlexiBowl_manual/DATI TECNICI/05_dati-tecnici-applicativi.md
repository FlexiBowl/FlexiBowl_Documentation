# **Dati Tecnici Applicativi**

## Caratteristiche dei componenti ammessi sul FlexiBowl®

:::{raw} html
   <style>
     .ars-components td, .ars-components th { text-align: center; vertical-align: middle; }
     .ars-components td:first-child, .ars-components th:first-child { text-align: left; }
   </style>
:::

:::{list-table}
:class: ars-components
:header-rows: 1
:align: center
:widths: 40 25 25 25 25 25 25

* - Specifiche componenti
  - FlexiBowl® 200
  - FlexiBowl® 350
  - FlexiBowl® 500
  - FlexiBowl® 650
  - FlexiBowl® 800
  - FlexiBowl® 1200

* - Dimensione massima del singolo componente
  - 20 mm
  - 50 mm
  - 100 mm
  - 150 mm
  - 250 mm
  - 400 mm

* - Altezza massima del singolo componente¹
  - 10 mm
  - 20 mm
  - 40 mm
  - 45 mm
  - 60 mm
  - 70 mm

* - Peso massimo del singolo componente
  - 20 g
  - 40 g
  - 100 g
  - 170 g
  - 250 g
  - 300 g

* - Capacità di carico massiima su superficie
  - N.A.
  - N.A.
  - 7 kg
  - 7 kg
  - 7 kg
  - 7 kg

* - Capacità di carico massima su disco rigido
  - 1 kg
  - 3 kg
  - 7 kg
  - N.A.
  - N.A.
  - N.A.

:::

1) L'altezza massima del componente è quella che lascia lo spazio necessario tra esso e la superficie superiore dello schemro flip per consentirne il ribalto

:::{note}
Il valore della dimensione massima del componente è ricavato da test eseguiti internamente ed è da considerarsi puramente indicativo in quanto ci possono essere altri fattori che lo influenzano (dimensioni della Bulk Feeder, tool del robot utilizzato per il *picking*, ecc...); per delle indicazioni puù precise non esitare a [contattare il nostro team](https://www.arsautomation.com/contact) o richiedere un [*free test*](https://www.flexibowl.it/free-test).
:::

:::{note}
L'altezza massima del componente viene calcolata tenendo conto dello spazio necessario per ribaltarlo tramite l'uso del flip, ed è da considerarsi puramente indicativo in quanto la possibilità di ribaltamento dipende anche dal rapporto tra le sue dimensioni. Per una valutazione più precisa della taglia di FlexiBowl® più adatta al pezzo da movimentare o della compatibilità del componente con il FLexiBowl® desiderato è possibile [contattare il nostro team](https://www.arsautomation.com/contact) o richiedere un [*free test*](https://www.flexibowl.it/free-test).
:::

(calcolo-pressione-flip)=
## Come valutare la ribaltabilità del componente

Inserire i dati del componente nel calcolatore: il sistema verifica automaticamente la compatibilità con la taglia di FlexiBowl® scelta e restituisce la **pressione del flip consigliata**.

:::{tip}
Misurare il pezzo appoggiato nella sua **posizione più stabile**: l'**altezza** è la distanza dal piano di appoggio al punto più alto, la **larghezza minima** è il lato più stretto del rettangolo d'ingombro della base d'appoggio.
:::

:::{raw} html
<div class="fc" id="fc-flip">
<style>
.fc{
  --fc-acc:#2980b9; --fc-acc-soft:rgba(41,128,185,.10); --fc-head:#1a3a52;
  --fc-bg:var(--pst-color-surface,#f7f9fb); --fc-card:var(--pst-color-background,#fff);
  --fc-bd:var(--pst-color-border,#d0e4f0); --fc-tx:var(--pst-color-text-base,#1f2d3a);
  --fc-mut:var(--pst-color-text-muted,#5b6b7a);
  --fc-ok:#1e8449; --fc-ok-soft:rgba(30,132,73,.10);
  --fc-warn:#b9770e; --fc-warn-soft:rgba(185,119,14,.12);
  --fc-err:#c0392b; --fc-err-soft:rgba(192,57,43,.10);
}
html[data-theme="dark"] .fc{
  --fc-acc:#5dade2; --fc-acc-soft:rgba(93,173,226,.14); --fc-head:#d6e6f2;
  --fc-ok:#52be80; --fc-ok-soft:rgba(82,190,128,.14);
  --fc-warn:#f0b04a; --fc-warn-soft:rgba(240,176,74,.14);
  --fc-err:#ec7063; --fc-err-soft:rgba(236,112,99,.14);
}
.fc{container-type:inline-size;font-family:inherit;color:var(--fc-tx);border:1px solid var(--fc-bd);border-radius:12px;background:var(--fc-bg);margin:1.5rem 0;overflow:hidden}
.fc *{box-sizing:border-box}
.fc-head{display:flex;align-items:center;gap:.6rem;padding:.9rem 1.2rem;border-bottom:1px solid var(--fc-bd);background:var(--fc-card)}
.fc-head i{font-size:1.4rem;color:var(--fc-acc)}
.fc-head b{font-size:1.05rem;color:var(--fc-head)}
.fc-head span{margin-left:auto;font-size:.8rem;color:var(--fc-mut)}
.fc-grid{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,1fr)}
@container (max-width:860px){.fc-grid{grid-template-columns:1fr}}
.fc-in{padding:1.1rem 1.2rem;display:flex;flex-direction:column;gap:1.1rem}
.fc-out{padding:1.1rem 1.2rem;border-left:1px solid var(--fc-bd);background:var(--fc-card)}
@container (max-width:860px){.fc-out{border-left:none;border-top:1px solid var(--fc-bd)}}
.fc-step{display:flex;align-items:center;gap:.5rem;font-weight:700;font-size:.85rem;color:var(--fc-head);margin-bottom:.5rem;text-transform:uppercase;letter-spacing:.03em}
.fc-step em{font-style:normal;display:inline-flex;align-items:center;justify-content:center;width:1.4rem;height:1.4rem;border-radius:50%;background:var(--fc-acc);color:#fff;font-size:.75rem}
.fc-seg{display:flex;flex-wrap:wrap;gap:.4rem}
.fc-seg button{font:inherit;font-size:.88rem;font-weight:600;padding:.45rem .8rem;border-radius:8px;border:1.5px solid var(--fc-bd);background:var(--fc-card);color:var(--fc-tx);cursor:pointer;transition:border-color .15s,background .15s}
.fc-seg button:hover:not(:disabled){border-color:var(--fc-acc)}
.fc-seg button[aria-pressed="true"]{border-color:var(--fc-acc);background:var(--fc-acc-soft);color:var(--fc-acc)}
.fc-seg button:disabled{opacity:.45;cursor:not-allowed;text-decoration:line-through}
.fc-fields{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:.7rem}
@container (max-width:480px){.fc-fields{grid-template-columns:1fr}}
.fc-f label{display:block;font-size:.82rem;font-weight:600;margin-bottom:.25rem}
.fc-unit{display:flex;align-items:stretch;border:1.5px solid var(--fc-bd);border-radius:8px;background:var(--fc-card);overflow:hidden}
.fc-unit:focus-within{border-color:var(--fc-acc)}
.fc-unit.fc-bad{border-color:var(--fc-err)}
.fc-unit input{flex:1;min-width:0;border:none;background:transparent;color:var(--fc-tx);font:inherit;font-size:.95rem;padding:.45rem .6rem;outline:none}
.fc-unit span{display:flex;align-items:center;padding:0 .6rem;font-size:.8rem;color:var(--fc-mut);border-left:1px solid var(--fc-bd)}
.fc-hint{font-size:.75rem;color:var(--fc-mut);margin-top:.2rem;min-height:1em}
.fc-hint.fc-bad{color:var(--fc-err);font-weight:600}
.fc-mat{display:grid;grid-template-columns:1fr;gap:.5rem}
.fc-mat button{font:inherit;text-align:left;padding:.6rem .7rem;border-radius:8px;border:1.5px solid var(--fc-bd);background:var(--fc-card);color:var(--fc-tx);cursor:pointer;transition:border-color .15s,background .15s}
.fc-mat button:hover{border-color:var(--fc-acc)}
.fc-mat button[aria-pressed="true"]{border-color:var(--fc-acc);background:var(--fc-acc-soft)}
.fc-mat b{display:block;font-size:.88rem}
.fc-mat small{display:block;font-size:.73rem;color:var(--fc-mut);line-height:1.35;margin-top:.2rem}
.fc-empty{display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:.5rem;min-height:260px;color:var(--fc-mut);font-size:.9rem}
.fc-empty i{font-size:2.2rem;color:var(--fc-acc);opacity:.6}
.fc-empty.fc-bad i{color:var(--fc-err);opacity:.8}
.fc-lbl{font-size:.78rem;font-weight:600;text-transform:uppercase;letter-spacing:.04em;color:var(--fc-mut)}
.fc-big{font-size:2.6rem;font-weight:800;line-height:1.1;color:var(--fc-head);font-variant-numeric:tabular-nums}
.fc-big small{font-size:1rem;font-weight:600;color:var(--fc-mut);margin-left:.25rem}
.fc-gauge{position:relative;height:8px;border-radius:4px;background:var(--fc-bd);margin:.7rem 0 .25rem}
.fc-gauge div{position:absolute;left:0;top:0;bottom:0;border-radius:4px;background:var(--fc-acc);transition:width .3s}
.fc-scale{display:flex;justify-content:space-between;font-size:.7rem;color:var(--fc-mut);margin-bottom:1rem}
.fc-checks{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:.4rem}
.fc-checks li{display:flex;gap:.5rem;align-items:flex-start;font-size:.82rem;line-height:1.4;padding:.45rem .6rem;border-radius:6px;margin:0}
.fc-checks li i{font-size:1rem;flex-shrink:0;margin-top:.05rem}
.fc-ok{background:var(--fc-ok-soft)} .fc-ok i{color:var(--fc-ok)}
.fc-warn{background:var(--fc-warn-soft)} .fc-warn i{color:var(--fc-warn)}
.fc-err{background:var(--fc-err-soft)} .fc-err i{color:var(--fc-err)}
.fc-info{background:var(--fc-acc-soft)} .fc-info i{color:var(--fc-acc)}
.fc-reset{font:inherit;font-size:.8rem;margin-top:.9rem;background:none;border:none;color:var(--fc-acc);cursor:pointer;padding:0;text-decoration:underline}
</style>
<script src="https://unpkg.com/@phosphor-icons/web@2.1.1"></script>

<div class="fc-head"><i class="ph ph-calculator"></i><b>Calcolatore pressione flip</b><span>Risultato indicativo da validare</span></div>
<div class="fc-grid">
  <div class="fc-in">
    <div>
      <div class="fc-step"><em>1</em>Taglia FlexiBowl®</div>
      <div class="fc-seg" id="fc-size" role="group" aria-label="Taglia FlexiBowl"></div>
    </div>
    <div>
      <div class="fc-step"><em>2</em>Dimensioni e peso del componente</div>
      <div class="fc-fields">
        <div class="fc-f"><label for="fc-h">Altezza massima</label>
          <div class="fc-unit" id="fc-h-w"><input id="fc-h" type="number" inputmode="decimal" min="0" step="0.1" placeholder="es. 12"><span>mm</span></div>
          <div class="fc-hint" id="fc-h-msg"></div></div>
        <div class="fc-f"><label for="fc-b">Larghezza minima della base</label>
          <div class="fc-unit" id="fc-b-w"><input id="fc-b" type="number" inputmode="decimal" min="0" step="0.1" placeholder="es. 8"><span>mm</span></div>
          <div class="fc-hint" id="fc-b-msg"></div></div>
        <div class="fc-f"><label for="fc-m">Peso del singolo componente</label>
          <div class="fc-unit" id="fc-m-w"><input id="fc-m" type="number" inputmode="decimal" min="0" step="0.1" placeholder="es. 25"><span>g</span></div>
          <div class="fc-hint" id="fc-m-msg"></div></div>
      </div>
    </div>
    <div>
      <div class="fc-step"><em>3</em>Materiale</div>
      <div class="fc-mat" id="fc-mat" role="group" aria-label="Materiale"></div>
    </div>
    <div>
      <div class="fc-step"><em>4</em>Piano di lavoro</div>
      <div class="fc-seg" id="fc-surf" role="group" aria-label="Piano di lavoro"></div>
      <div class="fc-hint" id="fc-surf-hint"></div>
    </div>
  </div>
  <div class="fc-out" id="fc-out" aria-live="polite"></div>
</div>

<script>
(function(){
  /* Dati interni: non vengono mai mostrati all'utente */
  var SIZES = {
    200: {grp:'200-350',  wGrp:'small', maxH:10, maxM:20,  surf:false, disc:true},
    350: {grp:'200-350',  wGrp:'small', maxH:20, maxM:40,  surf:false, disc:true},
    500: {grp:'500-650',  wGrp:'small', maxH:40, maxM:100, surf:true,  disc:true},
    650: {grp:'500-650',  wGrp:'large', maxH:45, maxM:170, surf:true,  disc:false},
    800: {grp:'800-1200', wGrp:'large', maxH:60, maxM:250, surf:true,  disc:false},
    1200:{grp:'800-1200', wGrp:'large', maxH:70, maxM:300, surf:true,  disc:false}
  };
  var PBASE = {
    '200-350': {flat:[2.5,'Se i pezzi tendono a sovrapporsi, aumentare il numero di colpi (Flip Count).'],
                slim:[2.0,'Geometria molto favorevole al ribaltamento. Prestare attenzione se il pezzo è molto leggero.']},
    '500-650': {flat:[3.2,'Il pezzo richiede maggiore energia per ribaltarsi.'],
                slim:[2.8,'Configurazione standard bilanciata.']},
    '800-1200':{flat:[4.0,'Pressione necessaria per separare geometrie piatte e pesanti.'],
                slim:[3.5,'Punto di partenza ottimale per componenti ingombranti.']}
  };
  var KW = { small:{lo:10, hi:100}, large:{lo:30, hi:250} };
  var KW_VAL = {light:0.8, std:1.0, heavy:1.3};
  var MAT = [
    {id:'rigid', k:1.0, n:'Rigido',      ex:'Acciaio, alluminio, ottone, POM, PA rigido, ABS, vetro'},
    {id:'semi',  k:1.2, n:'Semi-rigido', ex:'PE, PP, nylon non caricato, cartone denso, compositi'},
    {id:'soft',  k:1.8, n:'Non rigido',  ex:'Gomma, NBR, silicone, poliuretano, TPU morbido'}
  ];
  var SURF = [{id:'surf', k:1.0, n:'Superficie'}, {id:'disc', k:0.9, n:'Disco rigido'}];
  var PMAX = 6.0;

  var st = {size:null, mat:null, surf:null};
  var root = document.getElementById('fc-flip');
  if(!root || root.dataset.fcInit) return;   /* già inizializzato: evita card duplicate */
  root.dataset.fcInit = '1';
  var $ = function(id){ return root.querySelector('#'+id); };
  var f1 = function(x){ return x.toFixed(1).replace('.',','); };

  /* lettura campo: {e:true} se vuoto, altrimenti {v, ok} con ok = numero > 0 */
  function rd(id){
    var s = String($(id).value).trim().replace(',','.');
    if(s==='') return {e:true};
    var v = Number(s);
    return {e:false, v:v, ok:isFinite(v) && v>0};
  }
  function setMsg(id, msg, bad){
    $(id+'-w').classList.toggle('fc-bad', !!bad);
    var m = $(id+'-msg'); m.textContent = msg || ''; m.classList.toggle('fc-bad', !!bad);
  }
  function press(group, val){
    group.querySelectorAll('button').forEach(function(b){ b.setAttribute('aria-pressed', b.dataset.v===String(val)); });
  }

  Object.keys(SIZES).forEach(function(s){
    var b=document.createElement('button'); b.type='button'; b.dataset.v=s; b.textContent=s; b.setAttribute('aria-pressed','false');
    b.onclick=function(){ st.size=+s; press($('fc-size'),s); syncSurf(); calc(); };
    $('fc-size').appendChild(b);
  });
  MAT.forEach(function(m){
    var b=document.createElement('button'); b.type='button'; b.dataset.v=m.id; b.setAttribute('aria-pressed','false');
    b.innerHTML='<b>'+m.n+'</b><small>'+m.ex+'</small>';
    b.onclick=function(){ st.mat=m.id; press($('fc-mat'),m.id); calc(); };
    $('fc-mat').appendChild(b);
  });
  SURF.forEach(function(s){
    var b=document.createElement('button'); b.type='button'; b.dataset.v=s.id; b.textContent=s.n; b.setAttribute('aria-pressed','false');
    b.onclick=function(){ st.surf=s.id; press($('fc-surf'),s.id); calc(); };
    $('fc-surf').appendChild(b);
  });
  function syncSurf(){
    var S=SIZES[st.size], hint=$('fc-surf-hint');
    $('fc-surf').querySelectorAll('button').forEach(function(b){ b.disabled = !S[b.dataset.v]; });
    if(st.surf && !S[st.surf]) st.surf=null;
    if(!S.surf){ st.surf='disc'; hint.textContent='Il FlexiBowl® '+st.size+' lavora solo con disco rigido.'; }
    else if(!S.disc){ st.surf='surf'; hint.textContent='Il FlexiBowl® '+st.size+' lavora solo con superficie.'; }
    else hint.textContent='';
    press($('fc-surf'), st.surf);
  }

  /* niente segni, notazione esponenziale o valori negativi digitati da tastiera */
  ['fc-h','fc-b','fc-m'].forEach(function(id){
    $(id).addEventListener('keydown', function(e){ if(['-','+','e','E'].indexOf(e.key)>-1) e.preventDefault(); });
    $(id).addEventListener('input', calc);
  });

  function li(cls, icon, html){ return '<li class="'+cls+'"><i class="ph-fill ph-'+icon+'"></i><span>'+html+'</span></li>'; }

  function calc(){
    var out=$('fc-out'), S = st.size ? SIZES[st.size] : null;
    var H=rd('fc-h'), B=rd('fc-b'), M=rd('fc-m'), bad=false;

    /* validazione: valori > 0; peso entro il massimo della taglia */
    if(S){ $('fc-m').max = S.maxM; } else { $('fc-m').removeAttribute('max'); }
    var NOTPOS = 'Inserire un valore maggiore di zero';
    if(!H.e && !H.ok){ setMsg('fc-h', NOTPOS, true); bad=true; } else setMsg('fc-h','',false);
    if(!B.e && !B.ok){ setMsg('fc-b', NOTPOS, true); bad=true; } else setMsg('fc-b','',false);
    if(!M.e && !M.ok){ setMsg('fc-m', NOTPOS, true); bad=true; }
    else if(S && !M.e && M.v > S.maxM){ setMsg('fc-m', 'Peso massimo ammesso per FlexiBowl® '+st.size+': '+S.maxM+' g', true); bad=true; }
    else setMsg('fc-m', S ? 'Massimo ammesso per FlexiBowl® '+st.size+': '+S.maxM+' g' : 'Seleziona prima la taglia per vedere il peso massimo ammesso', false);

    if(bad){
      out.innerHTML='<div class="fc-empty fc-bad"><i class="ph ph-warning-circle"></i><div>Correggi i valori evidenziati per ottenere la pressione consigliata.</div></div>';
      return;
    }

    var missing=[];
    if(!st.size) missing.push('taglia'); if(H.e) missing.push('altezza'); if(B.e) missing.push('larghezza minima');
    if(M.e) missing.push('peso'); if(!st.mat) missing.push('materiale'); if(!st.surf) missing.push('piano di lavoro');
    if(missing.length){
      out.innerHTML='<div class="fc-empty"><i class="ph ph-gauge"></i><div>Completa i dati per calcolare la pressione consigliata.</div><div style="font-size:.8rem">Mancano: '+missing.join(', ')+'</div></div>';
      return;
    }

    var h=H.v, b=B.v, m=M.v;
    var ratio=h/b, slim=ratio>=1.0;
    var pb=PBASE[S.grp][slim?'slim':'flat'];
    var th=KW[S.wGrp], wc = m<th.lo?'light':(m>th.hi?'heavy':'std');
    var mat=MAT.filter(function(x){return x.id===st.mat;})[0];
    var Ks=SURF.filter(function(x){return x.id===st.surf;})[0].k;
    var P=pb[0]*mat.k*KW_VAL[wc]*Ks, Pset=Math.min(P,PMAX), capped=P>PMAX;

    var c='';
    if(h>S.maxH) c += li('fc-err','x-circle','Altezza oltre il limite di <b>'+S.maxH+' mm</b> per il FlexiBowl® '+st.size+': il pezzo potrebbe non avere lo spazio per ribaltarsi sotto lo schermo flip.');
    else c += li('fc-ok','check-circle','Il componente è compatibile con il FlexiBowl® '+st.size+'.');
    if(ratio<1.0) c += li('fc-warn','warning','Pezzo largo e basso, difficile da ribaltare: è richiesta la massima energia del flip.');
    else if(ratio<=2.0) c += li('fc-warn','warning','Per la geometria di questo pezzo il comportamento può variare: <b>si consiglia un test pratico di validazione</b>.');
    if(capped) c += li('fc-err','x-circle','Per questo componente servirebbe una pressione superiore al limite del cilindro flip: impostare <b>6,0 bar</b> e aumentare il <b>Flip Count</b> se il pezzo non si ribalta in modo costante.');
    c += li('fc-info','info',pb[1]);
    if(wc==='light') c += li('fc-info','info','Componente leggero: pressione ridotta per un salto controllato, evitando rimbalzi incontrollati.');
    if(wc==='heavy') c += li('fc-info','info','Componente pesante: pressione aumentata per permettere il ribaltamento della massa.');

    out.innerHTML =
      '<div class="fc-lbl">Pressione flip consigliata</div>'+
      '<div class="fc-big">'+f1(Pset)+'<small>bar</small></div>'+
      '<div class="fc-gauge"><div style="width:'+(Pset/PMAX*100)+'%"></div></div>'+
      '<div class="fc-scale"><span>0</span><span>2</span><span>4</span><span>6 bar (max)</span></div>'+
      '<ul class="fc-checks">'+c+'</ul>'+
      '<button type="button" class="fc-reset" id="fc-reset">Azzera i dati</button>';
    $('fc-reset').onclick=reset;
  }
  function reset(){
    st={size:null,mat:null,surf:null};
    ['fc-h','fc-b','fc-m'].forEach(function(id){ $(id).value=''; });
    ['fc-size','fc-mat','fc-surf'].forEach(function(g){ press($(g),'__'); });
    $('fc-surf').querySelectorAll('button').forEach(function(b){ b.disabled=false; });
    $('fc-surf-hint').textContent='';
    calc();
  }
  calc();
})();
</script>
</div>
:::

:::{attention}
Il valore calcolato è un **punto di partenza** da affinare in macchina. Per una valutazione più precisa e dettagliata dei parametri di flip non esitare a [contattare il nostro team](https://www.arsautomation.com/contact) o richiedere un [*free test*](https://www.flexibowl.it/free-test).
:::






