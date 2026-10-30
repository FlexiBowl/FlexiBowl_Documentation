# **Technische Daten Anwendung**

## Eigenschaften der auf dem FlexiBowl® zulässigen Bauteile

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

* - Bauteilspezifikationen
  - FlexiBowl® 200
  - FlexiBowl® 350
  - FlexiBowl® 500
  - FlexiBowl® 650
  - FlexiBowl® 800
  - FlexiBowl® 1200

* - Maximale Größe des einzelnen Bauteils
  - 20 mm
  - 50 mm
  - 100 mm
  - 150 mm
  - 250 mm
  - 400 mm

* - Maximale Höhe des einzelnen Bauteils¹
  - 10 mm
  - 20 mm
  - 40 mm
  - 45 mm
  - 60 mm
  - 70 mm

* - Maximales Gewicht des einzelnen Bauteils
  - 20 g
  - 40 g
  - 100 g
  - 170 g
  - 250 g
  - 300 g

* - Maximale Tragfähigkeit auf der Fläche
  - N. V.
  - N. V.
  - 7 kg
  - 7 kg
  - 7 kg
  - 7 kg

* - Maximale Tragfähigkeit auf der starren Scheibe
  - 1 kg
  - 3 kg
  - 7 kg
  - N. V.
  - N. V.
  - N. V.

:::

1) Die maximale Bauteilhöhe ist diejenige, die zwischen dem Bauteil und der Oberseite des Flip-Schirms den nötigen Freiraum lässt, damit es umgekippt werden kann

:::{note}
Der Wert für die maximale Bauteilgröße stammt aus intern durchgeführten Tests und ist als rein indikativ zu betrachten, da weitere Faktoren Einfluss haben können (Abmessungen des Bulk Feeders, für das *Picking* verwendetes Roboterwerkzeug usw.); für genauere Angaben zögern Sie nicht, [unser Team zu kontaktieren](https://www.arsautomation.com/contact) oder einen [*Free Test*](https://www.flexibowl.it/free-test) anzufordern.
:::

:::{note}
Die maximale Bauteilhöhe wird unter Berücksichtigung des Platzes berechnet, der zum Umkippen mittels Flip erforderlich ist, und ist als rein indikativ zu betrachten, da die Möglichkeit des Umkippens auch vom Verhältnis seiner Abmessungen abhängt. Für eine genauere Beurteilung der am besten zum zu handhabenden Teil passenden FlexiBowl®-Baugröße oder der Kompatibilität des Bauteils mit dem gewünschten FlexiBowl® können Sie [unser Team kontaktieren](https://www.arsautomation.com/contact) oder einen [*Free Test*](https://www.flexibowl.it/free-test) anfordern.
:::

(calcolo-pressione-flip)=
## So beurteilen Sie die Kippbarkeit des Bauteils

Die Bauteildaten in den Rechner eingeben: Das System prüft automatisch die Kompatibilität mit der gewählten FlexiBowl®-Baugröße und liefert den **empfohlenen Flip-Druck**.

:::{tip}
Das Teil in seiner **stabilsten Lage** aufliegend messen: Die **Höhe** ist der Abstand von der Auflagefläche bis zum höchsten Punkt, die **minimale Breite** ist die schmalste Seite des umschließenden Rechtecks der Auflagebasis.
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

<div class="fc-head"><i class="ph ph-calculator"></i><b>Flip-Druck-Rechner</b><span>Richtwert, der zu validieren ist</span></div>
<div class="fc-grid">
  <div class="fc-in">
    <div>
      <div class="fc-step"><em>1</em>FlexiBowl®-Baugröße</div>
      <div class="fc-seg" id="fc-size" role="group" aria-label="FlexiBowl-Baugröße"></div>
    </div>
    <div>
      <div class="fc-step"><em>2</em>Abmessungen und Gewicht des Bauteils</div>
      <div class="fc-fields">
        <div class="fc-f"><label for="fc-h">Maximale Höhe</label>
          <div class="fc-unit" id="fc-h-w"><input id="fc-h" type="number" inputmode="decimal" min="0" step="0.1" placeholder="z. B. 12"><span>mm</span></div>
          <div class="fc-hint" id="fc-h-msg"></div></div>
        <div class="fc-f"><label for="fc-b">Minimale Breite der Basis</label>
          <div class="fc-unit" id="fc-b-w"><input id="fc-b" type="number" inputmode="decimal" min="0" step="0.1" placeholder="z. B. 8"><span>mm</span></div>
          <div class="fc-hint" id="fc-b-msg"></div></div>
        <div class="fc-f"><label for="fc-m">Gewicht des einzelnen Bauteils</label>
          <div class="fc-unit" id="fc-m-w"><input id="fc-m" type="number" inputmode="decimal" min="0" step="0.1" placeholder="z. B. 25"><span>g</span></div>
          <div class="fc-hint" id="fc-m-msg"></div></div>
      </div>
    </div>
    <div>
      <div class="fc-step"><em>3</em>Material</div>
      <div class="fc-mat" id="fc-mat" role="group" aria-label="Material"></div>
    </div>
    <div>
      <div class="fc-step"><em>4</em>Arbeitsfläche</div>
      <div class="fc-seg" id="fc-surf" role="group" aria-label="Arbeitsfläche"></div>
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
    '200-350': {flat:[2.5,'Wenn sich die Teile tendenziell überlappen, die Anzahl der Schläge (Flip Count) erhöhen.'],
                slim:[2.0,'Sehr günstige Geometrie für das Wenden. Vorsicht, wenn das Teil sehr leicht ist.']},
    '500-650': {flat:[3.2,'Das Teil benötigt mehr Energie zum Wenden.'],
                slim:[2.8,'Ausgewogene Standardkonfiguration.']},
    '800-1200':{flat:[4.0,'Erforderlicher Druck, um flache und schwere Geometrien zu trennen.'],
                slim:[3.5,'Optimaler Ausgangspunkt für sperrige Komponenten.']}
  };
  var KW = { small:{lo:10, hi:100}, large:{lo:30, hi:250} };
  var KW_VAL = {light:0.8, std:1.0, heavy:1.3};
  var MAT = [
    {id:'rigid', k:1.0, n:'Rigido',      ex:'Stahl, Aluminium, Messing, POM, steifes PA, ABS, Glas'},
    {id:'semi',  k:1.2, n:'Semi-rigido', ex:'PE, PP, unverstärktes Nylon, dichter Karton, Verbundwerkstoffe'},
    {id:'soft',  k:1.8, n:'Non rigido',  ex:'Gummi, NBR, Silikon, Polyurethan, weiches TPU'}
  ];
  var SURF = [{id:'surf', k:1.0, n:'Oberfläche'}, {id:'disc', k:0.9, n:'Starre Scheibe'}];
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
    if(!S.surf){ st.surf='disc'; hint.textContent='Der FlexiBowl® '+st.size+' arbeitet nur mit starrer Scheibe.'; }
    else if(!S.disc){ st.surf='surf'; hint.textContent='Der FlexiBowl® '+st.size+' arbeitet nur mit Oberfläche.'; }
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
    var NOTPOS = 'Wert größer als null eingeben';
    if(!H.e && !H.ok){ setMsg('fc-h', NOTPOS, true); bad=true; } else setMsg('fc-h','',false);
    if(!B.e && !B.ok){ setMsg('fc-b', NOTPOS, true); bad=true; } else setMsg('fc-b','',false);
    if(!M.e && !M.ok){ setMsg('fc-m', NOTPOS, true); bad=true; }
    else if(S && !M.e && M.v > S.maxM){ setMsg('fc-m', 'Maximal zulässiges Gewicht für FlexiBowl® '+st.size+': '+S.maxM+' g', true); bad=true; }
    else setMsg('fc-m', S ? 'Maximal zulässig für FlexiBowl® '+st.size+': '+S.maxM+' g' : 'Zuerst die Größe wählen, um das maximal zulässige Gewicht zu sehen', false);

    if(bad){
      out.innerHTML='<div class="fc-empty fc-bad"><i class="ph ph-warning-circle"></i><div>Markierte Werte korrigieren, um den empfohlenen Druck zu erhalten.</div></div>';
      return;
    }

    var missing=[];
    if(!st.size) missing.push('Größe'); if(H.e) missing.push('Höhe'); if(B.e) missing.push('Mindestbreite');
    if(M.e) missing.push('Gewicht'); if(!st.mat) missing.push('Material'); if(!st.surf) missing.push('Arbeitsfläche');
    if(missing.length){
      out.innerHTML='<div class="fc-empty"><i class="ph ph-gauge"></i><div>Daten ausfüllen, um den empfohlenen Druck zu berechnen.</div><div style="font-size:.8rem">Fehlend: '+missing.join(', ')+'</div></div>';
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
    if(h>S.maxH) c += li('fc-err','x-circle','Höhe überschreitet den Grenzwert von <b>'+S.maxH+' mm</b> für den FlexiBowl® '+st.size+': Das Teil hat möglicherweise nicht genug Platz, um sich unter dem Flip-Schirm zu wenden.');
    else c += li('fc-ok','check-circle','Das Bauteil ist kompatibel mit dem FlexiBowl® '+st.size+'.');
    if(ratio<1.0) c += li('fc-warn','warning','Breites, flaches Teil, schwer zu wenden: Es ist die maximale Flip-Energie erforderlich.');
    else if(ratio<=2.0) c += li('fc-warn','warning','Bei der Geometrie dieses Teils kann das Verhalten variieren: <b>Ein praktischer Validierungstest wird empfohlen</b>.');
    if(capped) c += li('fc-err','x-circle','Für dieses Bauteil wäre ein Druck über dem Grenzwert des Flip-Zylinders nötig: <b>6,0 bar</b> einstellen und den <b>Flip Count</b> erhöhen, wenn sich das Teil nicht zuverlässig wendet.');
    c += li('fc-info','info',pb[1]);
    if(wc==='light') c += li('fc-info','info','Leichtes Bauteil: reduzierter Druck für einen kontrollierten Sprung, um unkontrolliertes Abprallen zu vermeiden.');
    if(wc==='heavy') c += li('fc-info','info','Schweres Bauteil: erhöhter Druck, damit sich die Masse wenden kann.');

    out.innerHTML =
      '<div class="fc-lbl">Empfohlener Flip-Druck</div>'+
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
Der berechnete Wert ist ein **Ausgangspunkt**, der an der Maschine zu verfeinern ist. Für eine genauere und detailliertere Beurteilung der Flip-Parameter zögern Sie nicht, [unser Team zu kontaktieren](https://www.arsautomation.com/contact) oder einen [*Free Test*](https://www.flexibowl.it/free-test) anzufordern.
:::






