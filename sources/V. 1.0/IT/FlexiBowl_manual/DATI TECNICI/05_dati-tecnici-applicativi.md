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
Il valore della dimensione massima del componente è ricavato da test eseguiti internamente ed è da considerarsi puramente indicativo in quanto ci possono essere altri fattori che lo influenzano (dimensioni della tramoggia, tool del robot utilizzato per il *picking*, ecc...); per delle indicazioni puù precise non esitare a [contattare il nostro team](https://www.arsautomation.com/contact) o richiedere un [*free test*](https://www.flexibowl.it/free-test).
:::

:::{note}
L'altezza massima del componente viene calcolata tenendo conto dello spazio necessario per ribaltarlo tramite l'uso del flip, ed è da considerarsi puramente indicativo in quanto la possibilità di ribaltamento dipende anche dal rapporto tra le sue dimensioni. Per una valutazione più precisa della taglia di FlexiBowl® più adatta al pezzo da movimentare o della compatibilità del componente con il FLexiBowl® desiderato è possibile [contattare il nostro team](https://www.arsautomation.com/contact) o richiedere un [*free test*](https://www.flexibowl.it/free-test).
:::
(calcolo-pressione-flip)=
## Come valutare la ribaltabilità del componente

Per capire se un pezzo caricato in tramoggia può essere separato e ribaltato efficacemente dal flip, vanno valutati quattro fattori: **geometria**, **massa**, **materiale** e **piano di lavoro** (superficie o disco rigido).

Inserire i dati del componente nel calcolatore: il sistema verifica automaticamente la compatibilità con la taglia di FlexiBowl® scelta e restituisce la **pressione del flip consigliata**.

:::{tip}
Misurare il pezzo appoggiato nella sua **posizione più stabile**: l'altezza *H* è la distanza dal piano di appoggio al punto più alto, la larghezza minima *B<sub>min</sub>* è il lato più stretto del rettangolo d'ingombro della base d'appoggio.
:::

:::{raw} html
<div class="fc" id="fc-flip">
<style>
/* ── Token: chiaro (default) e scuro (pydata: html[data-theme="dark"]) ── */
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
@container (max-width:480px){.fc-fields{grid-template-columns:1fr}.fc-chips{grid-template-columns:repeat(2,minmax(0,1fr))}}
.fc-f label{display:block;font-size:.82rem;font-weight:600;margin-bottom:.25rem}
.fc-f label small{font-weight:400;color:var(--fc-mut)}
.fc-unit{display:flex;align-items:stretch;border:1.5px solid var(--fc-bd);border-radius:8px;background:var(--fc-card);overflow:hidden}
.fc-unit:focus-within{border-color:var(--fc-acc)}
.fc-unit input{flex:1;min-width:0;border:none;background:transparent;color:var(--fc-tx);font:inherit;font-size:.95rem;padding:.45rem .6rem;outline:none}
.fc-unit span{display:flex;align-items:center;padding:0 .6rem;font-size:.8rem;color:var(--fc-mut);border-left:1px solid var(--fc-bd)}
.fc-hint{font-size:.75rem;color:var(--fc-mut);margin-top:.2rem}
.fc-mat{display:grid;grid-template-columns:1fr;gap:.5rem}
.fc-mat button{font:inherit;text-align:left;padding:.6rem .7rem;border-radius:8px;border:1.5px solid var(--fc-bd);background:var(--fc-card);color:var(--fc-tx);cursor:pointer;transition:border-color .15s,background .15s}
.fc-mat button:hover{border-color:var(--fc-acc)}
.fc-mat button[aria-pressed="true"]{border-color:var(--fc-acc);background:var(--fc-acc-soft)}
.fc-mat b{display:block;font-size:.88rem}
.fc-mat small{display:block;font-size:.73rem;color:var(--fc-mut);line-height:1.35;margin-top:.2rem}
/* risultato */
.fc-empty{display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:.5rem;min-height:260px;color:var(--fc-mut);font-size:.9rem}
.fc-empty i{font-size:2.2rem;color:var(--fc-acc);opacity:.6}
.fc-lbl{font-size:.78rem;font-weight:600;text-transform:uppercase;letter-spacing:.04em;color:var(--fc-mut)}
.fc-big{font-size:2.6rem;font-weight:800;line-height:1.1;color:var(--fc-head);font-variant-numeric:tabular-nums}
.fc-big small{font-size:1rem;font-weight:600;color:var(--fc-mut);margin-left:.25rem}
.fc-gauge{position:relative;height:8px;border-radius:4px;background:var(--fc-bd);margin:.7rem 0 .25rem}
.fc-gauge div{position:absolute;left:0;top:0;bottom:0;border-radius:4px;background:var(--fc-acc);transition:width .3s}
.fc-scale{display:flex;justify-content:space-between;font-size:.7rem;color:var(--fc-mut)}
.fc-chips{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:.4rem;margin:1rem 0 .6rem}
.fc-chip{border:1px solid var(--fc-bd);border-radius:8px;padding:.4rem .5rem;text-align:center}
.fc-chip span{display:block;font-size:.72rem;color:var(--fc-mut)}
.fc-chip b{font-size:.98rem;font-variant-numeric:tabular-nums}
.fc-formula{font-size:.8rem;color:var(--fc-mut);font-variant-numeric:tabular-nums;margin-bottom:.9rem}
.fc-is{display:flex;align-items:center;gap:.5rem;font-size:.85rem;margin-bottom:.8rem}
.fc-pill{font-size:.72rem;font-weight:700;padding:.15rem .55rem;border-radius:20px}
.fc-checks{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:.4rem}
.fc-checks li{display:flex;gap:.5rem;align-items:flex-start;font-size:.82rem;line-height:1.4;padding:.45rem .6rem;border-radius:6px;margin:0}
.fc-checks li i{font-size:1rem;flex-shrink:0;margin-top:.05rem}
.fc-ok{background:var(--fc-ok-soft)} .fc-ok i,.fc-pill.fc-ok{color:var(--fc-ok)}
.fc-warn{background:var(--fc-warn-soft)} .fc-warn i,.fc-pill.fc-warn{color:var(--fc-warn)}
.fc-err{background:var(--fc-err-soft)} .fc-err i,.fc-pill.fc-err{color:var(--fc-err)}
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
      <div class="fc-step"><em>2</em>Geometria e massa del componente</div>
      <div class="fc-fields">
        <div class="fc-f"><label for="fc-h">Altezza massima <i>H</i></label>
          <div class="fc-unit"><input id="fc-h" type="number" inputmode="decimal" min="0" step="0.1" placeholder="es. 12"><span>mm</span></div></div>
        <div class="fc-f"><label for="fc-b">Larghezza minima base <i>B<sub>min</sub></i></label>
          <div class="fc-unit"><input id="fc-b" type="number" inputmode="decimal" min="0" step="0.1" placeholder="es. 8"><span>mm</span></div></div>
          <div class="fc-hint">*B<sub>min</sub>* è il lato più stretto del rettangolo d'ingombro della base d'appoggio</div></div>
        <div class="fc-f"><label for="fc-m">Massa</label>
          <div class="fc-unit"><input id="fc-m" type="number" inputmode="decimal" min="0" step="0.1" placeholder="es. 25"><span>g</span></div></div>
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
  /* ═════ DATI — allineati alle tabelle di riferimento sotto ═════ */
  var SIZES = {
    200: {grp:'200-350',  wGrp:'small', maxDim:20,  maxH:10, maxM:20,  surf:false, disc:true},
    350: {grp:'200-350',  wGrp:'small', maxDim:50,  maxH:20, maxM:40,  surf:false, disc:true},
    500: {grp:'500-650',  wGrp:'small', maxDim:100, maxH:40, maxM:100, surf:true,  disc:true},
    650: {grp:'500-650',  wGrp:'large', maxDim:150, maxH:45, maxM:170, surf:true,  disc:false},
    800: {grp:'800-1200', wGrp:'large', maxDim:250, maxH:60, maxM:250, surf:true,  disc:false},
    1200:{grp:'800-1200', wGrp:'large', maxDim:400, maxH:70, maxM:300, surf:true,  disc:false}
  };
  var PBASE = {
    '200-350': {flat:[2.5,'Rischio overlapping: aumentare il numero di colpi (Flip Count) se i pezzi si sormontano.'],
                slim:[2.0,'Ottima ribaltabilità. Prestare attenzione a pezzi troppo leggeri.']},
    '500-650': {flat:[3.2,'Richiede maggiore energia per vincere la stabilità geometrica.'],
                slim:[2.8,'Configurazione standard bilanciata.']},
    '800-1200':{flat:[4.0,'Necessaria per separare geometrie piatte e pesanti.'],
                slim:[3.5,'Punto di partenza ottimale per componenti ingombranti.']}
  };
  var KW = { small:{lo:10, hi:100}, large:{lo:30, hi:250} };   /* soglie massa in g */
  var KW_VAL = {light:[0.8,'Leggero'], std:[1.0,'Standard'], heavy:[1.3,'Pesante']};
  var MAT = [
    {id:'rigid', k:1.0, n:'Rigido',      ex:'Acciaio, alluminio, ottone, POM, PA rigido, ABS, vetro'},
    {id:'semi',  k:1.2, n:'Semi-rigido', ex:'PE, PP, nylon non caricato, cartone denso, compositi'},
    {id:'soft',  k:1.8, n:'Non rigido',  ex:'Gomma, NBR, silicone, poliuretano, TPU morbido'}
  ];
  var SURF = [{id:'surf', k:1.0, n:'Superficie'}, {id:'disc', k:0.9, n:'Disco rigido'}];
  var PMAX = 6.0;

  /* ═════ STATO ═════ */
  var st = {size:null, mat:null, surf:null};
  var root = document.getElementById('fc-flip');
  var $ = function(id){ return root.querySelector('#'+id); };
  var f2 = function(x){ return x.toFixed(2).replace('.',','); };
  var f1 = function(x){ return x.toFixed(1).replace('.',','); };
  var num = function(id){ var v=parseFloat(String($(id).value).replace(',','.')); return isFinite(v)&&v>0 ? v : null; };

  function press(group, val){
    group.querySelectorAll('button').forEach(function(b){ b.setAttribute('aria-pressed', b.dataset.v===String(val)); });
  }

  /* taglie */
  Object.keys(SIZES).forEach(function(s){
    var b=document.createElement('button'); b.type='button'; b.dataset.v=s; b.textContent=s; b.setAttribute('aria-pressed','false');
    b.onclick=function(){ st.size=+s; press($('fc-size'),s); syncSurf(); calc(); };
    $('fc-size').appendChild(b);
  });
  /* materiali */
  MAT.forEach(function(m){
    var b=document.createElement('button'); b.type='button'; b.dataset.v=m.id; b.setAttribute('aria-pressed','false');
    b.innerHTML='<b>'+m.n+' · K<sub>m</sub> '+f1(m.k)+'</b><small>'+m.ex+'</small>';
    b.onclick=function(){ st.mat=m.id; press($('fc-mat'),m.id); calc(); };
    $('fc-mat').appendChild(b);
  });
  /* piano di lavoro */
  SURF.forEach(function(s){
    var b=document.createElement('button'); b.type='button'; b.dataset.v=s.id; b.setAttribute('aria-pressed','false');
    b.textContent=s.n+' · Ks '+f1(s.k);
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
  ['fc-h','fc-b','fc-m','fc-l'].forEach(function(id){ $(id).addEventListener('input', calc); });

  function li(cls, icon, html){ return '<li class="'+cls+'"><i class="ph-fill ph-'+icon+'"></i><span>'+html+'</span></li>'; }

  function calc(){
    var H=num('fc-h'), B=num('fc-b'), M=num('fc-m'), L=num('fc-l'), out=$('fc-out');
    var missing=[];
    if(!st.size) missing.push('taglia'); if(!H) missing.push('altezza H'); if(!B) missing.push('larghezza B<sub>min</sub>');
    if(!M) missing.push('massa'); if(!st.mat) missing.push('materiale'); if(!st.surf) missing.push('piano di lavoro');
    if(missing.length){
      out.innerHTML='<div class="fc-empty"><i class="ph ph-gauge"></i><div>Completa i dati per calcolare la pressione consigliata.</div><div style="font-size:.8rem">Mancano: '+missing.join(', ')+'</div></div>';
      return;
    }
    var S=SIZES[st.size], Is=H/B, slim=Is>=1.0;
    var pb=PBASE[S.grp][slim?'slim':'flat'];
    var th=KW[S.wGrp], wc = M<th.lo?'light':(M>th.hi?'heavy':'std');
    var Kw=KW_VAL[wc][0];
    var mat=MAT.filter(function(m){return m.id===st.mat;})[0];
    var Ks=SURF.filter(function(s){return s.id===st.surf;})[0].k;
    var P=pb[0]*mat.k*Kw*Ks, Pset=Math.min(P,PMAX), capped=P>PMAX;

    /* classe di snellezza */
    var isCls, isTxt;
    if(Is<1.0){ isCls='fc-err'; isTxt='Estremamente stabile · difficile da ribaltare'; }
    else if(Is<=2.0){ isCls='fc-warn'; isTxt='Stabilità moderata · zona critica'; }
    else { isCls='fc-ok'; isTxt='Altamente instabile · ribaltamento ottimo'; }

    /* controlli incrociati */
    var c='';
    c += H<=S.maxH ? li('fc-ok','check-circle','Altezza '+f1(H)+' mm entro il limite di '+S.maxH+' mm per il FlexiBowl® '+st.size+'.')
                   : li('fc-err','x-circle','Altezza '+f1(H)+' mm oltre il limite di <b>'+S.maxH+' mm</b>: il pezzo potrebbe non avere lo spazio per ribaltarsi sotto lo schermo flip.');
    c += M<=S.maxM ? li('fc-ok','check-circle','Massa '+f1(M)+' g entro il limite di '+S.maxM+' g.')
                   : li('fc-err','x-circle','Massa '+f1(M)+' g oltre il limite di <b>'+S.maxM+' g</b> per il FlexiBowl® '+st.size+'.');
    if(L) c += L<=S.maxDim ? li('fc-ok','check-circle','Dimensione massima '+f1(L)+' mm entro il limite di '+S.maxDim+' mm.')
                           : li('fc-err','x-circle','Dimensione massima '+f1(L)+' mm oltre il limite di <b>'+S.maxDim+' mm</b>.');
    if(L && L<Math.max(H,B)) c += li('fc-warn','warning','La dimensione massima è inferiore ad H o B<sub>min</sub>: verificare le misure inserite.');
    if(Is<1.0) c += li('fc-warn','warning','Pezzo largo e basso: richiede la massima energia del flip.');
    else if(Is<=2.0) c += li('fc-warn','warning','Indice di snellezza in zona critica: il comportamento dipende dalla simmetria del pezzo, <b>validare con un test pratico</b>.');
    if(capped) c += li('fc-err','x-circle','Il calcolo restituisce '+f2(P)+' bar, oltre la massima pressione di esercizio del cilindro flip: impostare <b>6,0 bar</b> e aumentare il <b>Flip Count</b> se il pezzo non si ribalta costantemente.');
    c += li('fc-info','info',pb[1]);
    if(wc!=='std') c += li('fc-info','info', wc==='light'
        ? 'Componente leggero: pressione ridotta per un salto controllato, evitando rimbalzi incontrollati.'
        : 'Componente pesante: pressione aumentata per vincere la gravità e permettere il ribaltamento della massa.');

    out.innerHTML =
      '<div class="fc-lbl">Pressione flip consigliata</div>'+
      '<div class="fc-big">'+f1(Pset)+'<small>bar</small></div>'+
      '<div class="fc-gauge"><div style="width:'+(Pset/PMAX*100)+'%"></div></div>'+
      '<div class="fc-scale"><span>0</span><span>2</span><span>4</span><span>6 bar (max)</span></div>'+
      '<div class="fc-chips">'+
        '<div class="fc-chip"><span>P<sub>base</sub></span><b>'+f1(pb[0])+'</b></div>'+
        '<div class="fc-chip"><span>K<sub>m</sub> '+mat.n.toLowerCase()+'</span><b>'+f1(mat.k)+'</b></div>'+
        '<div class="fc-chip"><span>K<sub>w</sub> '+KW_VAL[wc][1].toLowerCase()+'</span><b>'+f1(Kw)+'</b></div>'+
        '<div class="fc-chip"><span>K<sub>s</sub></span><b>'+f1(Ks)+'</b></div>'+
      '</div>'+
      '<div class="fc-formula">P<sub>flip</sub> = '+f1(pb[0])+' × '+f1(mat.k)+' × '+f1(Kw)+' × '+f1(Ks)+' = <b>'+f2(P)+' bar</b>'+(capped?' → limitata a 6,0 bar':'')+'</div>'+
      '<div class="fc-is"><span>Indice di snellezza I<sub>s</sub> = '+f2(H)+' / '+f2(B)+' = <b>'+f2(Is)+'</b></span><span class="fc-pill '+isCls+'">'+isTxt+'</span></div>'+
      '<ul class="fc-checks">'+c+'</ul>'+
      '<button type="button" class="fc-reset" id="fc-reset">Azzera i dati</button>';
    $('fc-reset').onclick=reset;
  }
  function reset(){
    st={size:null,mat:null,surf:null};
    ['fc-h','fc-b','fc-m','fc-l'].forEach(function(id){ $(id).value=''; });
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

### Come viene calcolata la pressione

La pressione consigliata si ottiene moltiplicando una **pressione base**, che dipende dalla taglia del FlexiBowl® e dalla geometria del pezzo, per tre fattori correttivi:

$$
P_{flip} = P_{base} \times K_m \times K_w \times K_s
$$

Il risultato è limitato a **6,0 bar**, la massima pressione di esercizio del cilindro flip.

::::{dropdown} Indice di snellezza e pressione base
:icon: graph

L'indice di snellezza descrive quanto è facile ribaltare il pezzo:

$$
I_s = \frac{H}{B_{\min}}
$$

:::{list-table}
:widths: 25 35 40
:header-rows: 1

* - Indice $I_s$
  - Stabilità del pezzo
  - Idoneità al ribaltamento
* - $I_s < 1{,}0$ (largo e basso)
  - **Estremamente stabile.** Tende a saltare verticalmente senza ruotare o ricade sulla stessa base.
  - **Difficile da ribaltare.** Richiede la massima energia del flip.
* - $1{,}0 \le I_s \le 2{,}0$
  - **Stabilità moderata.** Il comportamento dinamico dipende dalla simmetria del pezzo.
  - **Zona critica.** Richiede un test pratico di validazione sulla macchina.
* - $I_s > 2{,}0$ (snello e alto)
  - **Altamente instabile.** Il baricentro alto lo rende estremamente sensibile all'urto.
  - **Ottima.** Si ribalta molto facilmente con impostazioni di energia standard.
:::

:::{list-table}
:widths: 18 27 15 40
:header-rows: 1

* - Taglia FlexiBowl®
  - Geometria
  - $P_{base}$
  - Note operative
* - 200 – 350
  - $I_s < 1{,}0$ (piatto/largo)
  - 2,5 bar
  - Rischio overlapping. Aumentare il numero di colpi se i pezzi si sormontano.
* - 200 – 350
  - $I_s \ge 1{,}0$ (snello/alto)
  - 2,0 bar
  - Ottima ribaltabilità. Prestare attenzione a pezzi troppo leggeri.
* - 500 – 650
  - $I_s < 1{,}0$ (piatto/largo)
  - 3,2 bar
  - Richiede maggiore energia per vincere la stabilità geometrica.
* - 500 – 650
  - $I_s \ge 1{,}0$ (snello/alto)
  - 2,8 bar
  - Configurazione standard bilanciata.
* - 800 – 1200
  - $I_s < 1{,}0$ (piatto/largo)
  - 4,0 bar
  - Necessaria per separare geometrie piatte e pesanti.
* - 800 – 1200
  - $I_s \ge 1{,}0$ (snello/alto)
  - 3,5 bar
  - Punto di partenza ottimale per componenti ingombranti.
:::
::::

::::{dropdown} Fattore correttivo del materiale ($K_m$)
:icon: package

La rigidezza del componente influisce direttamente sull'efficienza di trasmissione dell'impulso del flip. I materiali a comportamento elastico o smorzante assorbono parte dell'energia cinetica durante l'impatto, richiedendo una compensazione della pressione di linea.

:::{list-table}
:widths: 18 10 37 35
:header-rows: 1

* - Categoria
  - $K_m$
  - Materiali
  - Comportamento
* - Rigido
  - 1,0
  - Acciaio, alluminio, ottone, lamiera, POM, PA (nylon rigido), ABS, vetro, bachelite
  - Urto perfettamente elastico: la totalità dell'energia viene trasferita al pezzo, che scatta istantaneamente. Nessuna correzione.
* - Semi-rigido
  - 1,2
  - Polietilene (PE), polipropilene (PP), nylon non caricato, cartone denso, materiali compositi stratificati
  - Presenza di micro-smorzamento strutturale. Pressione base aumentata del 20% per garantire la stessa altezza di salto del pezzo rigido.
* - Non rigido
  - 1,8
  - Gomma naturale, gomma nitrilica (NBR), silicone, poliuretano, TPU morbido
  - Urto fortemente anelastico: il componente si deforma momentaneamente sotto l'impulso. Richiede un forte incremento della pressione base, fino al limite di linea di 6,0 bar se necessario.
:::
::::

::::{dropdown} Fattore correttivo del peso ($K_w$)
:icon: stack

La massa del componente determina la sua inerzia al decollo. Componenti molto leggeri richiedono pressioni ridotte per evitare traiettorie caotiche o fuoriuscite dal piatto, mentre componenti pesanti necessitano di una spinta maggiore per sollevare il baricentro.

:::{list-table}
:widths: 18 20 20 10 32
:header-rows: 1

* - Categoria
  - Massa (FlexiBowl® 200 / 350 / 500)
  - Massa (FlexiBowl® 650 / 800 / 1200)
  - $K_w$
  - Note
* - Leggero
  - < 10 g
  - < 30 g
  - 0,8
  - Bassa inerzia. Pressione ridotta del 20% per un salto controllato e smorzato, evitando rimbalzi incontrollati.
* - Standard
  - 10 – 100 g
  - 30 – 250 g
  - 1,0
  - Finestra di lavoro ottimale della macchina. Nessuna correzione richiesta.
* - Pesante
  - > 100 g
  - > 250 g
  - 1,3
  - Alta inerzia. Pressione aumentata del 30% per vincere la forza di gravità e permettere il ribaltamento della massa.
:::
::::

::::{dropdown} Fattore correttivo del piano di lavoro ($K_s$)
:icon: circle

:::{list-table}
:widths: 50 50
:header-rows: 1

* - Piano di lavoro
  - $K_s$
* - Superficie
  - 1,0
* - Disco rigido
  - 0,9
:::

I FlexiBowl® 200 e 350 lavorano solo con disco rigido; i FlexiBowl® 650, 800 e 1200 solo con superficie (vedi {ref}`dischi-rigidi` e {ref}`superfici`).
::::