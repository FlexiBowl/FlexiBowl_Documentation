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
  - 15 mm
  - 50 mm
  - 105 mm
  - 160 mm
  - 240 mm
  - 460 mm

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

## Come valutare la ribaltabilità del componente

Per capire se un pezzo caricato in tramoggia pu`o essere separato e ribaltato efficacemente dal flip, vanno valutati tre fattori principali: geometria, limiti di massa e materiale.

### Indice di snellezza

Posizionando il pezzo nella sua configurazione più stabile si misurano i seguenti ingombri:

- Altezza massima ***H***: Distanza verticale dal piano di appoggio al punto pi`u alto del pezzo.

- Larghezza minima alla base ***$B_{\min}$***: Il lato più stretto del rettangolo d’ingombro della base d’appoggio.

L'indice ***$I_s$*** si calcola come segue:

$$
I_s = \frac{H}{B_{\min}}
$$

Questo valore ci dice quanto è facile ribaltare il pezzo:

:::{list-table}
:widths: 33 33 33
:header-rows: 1
* - Indice di snellezza $I_s$
  - Stabilità del pezzo
  - Idoneità al ribaltamento
* - $I_s < 1.0$ (largo e basso)
  - **Estremamente Stabile.** Tende a saltare verticalmente senza ruotare o ricade sulla stessa base.
  - **Difficile da ribaltare.** Richiede la massima energia del flip.
* - $1.0 < I_s < 2.0$
  - **Stabilità Moderata.** Il comportamento dinamico dipende dalla simmetria del pezzo.
  - **Zona Critica.** Richiede un test pratico di validazione sulla macchina.
* - $I_s > 2.0$ (snello e alto)
  - **Altamente Instabile.** Il baricentro alto lo rende estremamente sensibile all'urto.
  - **Ottima.** Si ribalta molto facilmente con impostazioni di energia standard.
:::

In base al valore dell'indice di snellezza si parte da un valore di **pressione base** per il flip:

:::{raw} html

<style>
     table.ars-table {
       border-collapse: collapse;
       width: 100%;
       font-family: inherit;
       border: 1px solid #cccccc;
     }
     table.ars-table thead tr {
       background-color: #f5f5f5;
       border-bottom: 2px solid #3366CC;
     }
     table.ars-table thead th {
       font-weight: bold;
       padding: 12px 16px;
       text-align: center;
       border-right: 1px solid #cccccc;
     }
     table.ars-table thead th:first-child {
       text-align: left;
     }
     table.ars-table thead th:last-child {
       border-right: none;
     }
     table.ars-table tbody tr:nth-child(odd)  { background-color: #f5f5f5; }
     table.ars-table tbody tr:nth-child(even) { background-color: #ffffff; }
     table.ars-table tbody tr:hover           { background-color: #ddeeff; }
     table.ars-table td {
       padding: 10px 16px;
       text-align: center;
       border-right: 1px solid #cccccc;
     }
     table.ars-table td:first-child {
       text-align: left;
     }
     table.ars-table td:last-child {
       border-right: none;
     }
/* Struttura principale della tabella */
[data-theme="dark"] table.ars-table {
  border-collapse: collapse;
  border-spacing: 0;
  
  /* Rimuove i bordi verticali esterni (sinistro e destro) */
  border-left: none;
  border-right: none;
  
  /* Mantiene solo i sottili bordi orizzontali esterni (sopra e sotto) */
  border-top: 1px solid #383f4f;
  border-bottom: 1px solid #383f4f;
}

/* Gestione dei bordi interni delle celle (th e td) */
[data-theme="dark"] table.ars-table th,
[data-theme="dark"] table.ars-table td {
  padding: 10px 12px;
  
  /* Linea orizzontale inferiore uguale per tutte le righe */
  border-bottom: 1px solid #383f4f;
  
  /* Linea verticale interna (a destra di ogni cella) */
  border-right: 1px solid #383f4f;
  
  /* Azzera gli altri lati per evitare conflitti */
  border-left: none;
  border-top: none;
}

/* Elimina l'ultima linea verticale a destra per non creare il bordo esterno destro */
[data-theme="dark"] table.ars-table th:last-child,
[data-theme="dark"] table.ars-table td:last-child {
  border-right: none;
}

/* Elimina l'ultima linea orizzontale per non raddoppiarla con il fondo della tabella */
[data-theme="dark"] table.ars-table tbody tr:last-child td {
  border-bottom: none;
}

/* ══════════ SEZIONE COLORI COINCIDENTI ══════════ */

/* Sfondo dell'header */
[data-theme="dark"] table.ars-table thead tr {
  background-color: #29313d;
}

[data-theme="dark"] table.ars-table thead th {
  color: #e0e0e0;
  font-weight: 600;
}

/* Zebra striping identico alla prima tabella */
[data-theme="dark"] table.ars-table tbody tr:nth-child(odd) {
  background-color: #222832; /* Riga scura */
}

[data-theme="dark"] table.ars-table tbody tr:nth-child(even) {
  background-color: #29313d; /* Riga chiara */
}

/* Effetto Hover al passaggio del mouse */
[data-theme="dark"] table.ars-table tbody tr:hover {
  background-color: #282d3a;
}
   </style>
<table class="ars-table">
  <thead>
    <tr>
      <th style="padding:10px 14px; text-align:left;">Taglia FlexiBowl®</th>
      <th style="padding:10px 14px; text-align:left;">Geometria Componente</th>
      <th style="padding:10px 14px; text-align:left;">Pressione Base</th>
      <th style="padding:10px 14px; text-align:left;">Note Operative e Comportamento</th>
    </tr>
  </thead>
  <tbody>
    <!-- Taglie 200 / 350 -->
    <tr>
      <td rowspan="2" style="padding:10px 14px; font-weight:bold; vertical-align:middle;">200-350</td>
      <td style="padding:10px 14px;">I<sub>s</sub> &lt; 1.0 (Piatto/Largo)</td>
      <td style="padding:10px 14px;">2.5 bar</td>
      <td style="padding:10px 14px;">Rischio Overlapping. Aumentare il numero di colpi se i pezzi si sormontano.</td>
    </tr>
    <tr>
      <td style="padding:10px 14px;">I<sub>s</sub> &ge; 1.0 (Snello/Alto)</td>
      <td style="padding:10px 14px;">2.0 bar</td>
      <td style="padding:10px 14px;">Ottima ribaltabilità. Prestare attenzione a pezzi troppo leggeri.</td>
    </tr>
    <!-- Taglie 500 / 650 -->
    <tr>
      <td rowspan="2" style="padding:10px 14px; font-weight:bold; vertical-align:middle;">500-650</td>
      <td style="padding:10px 14px;">I<sub>s</sub> &lt; 1.0 (Piatto/Largo)</td>
      <td style="padding:10px 14px;">3.2 bar</td>
      <td style="padding:10px 14px;">Richiede maggiore energia per vincere la stabilità geometrica.</td>
    </tr>
    <tr>
      <td style="padding:10px 14px;">I<sub>s</sub> &ge; 1.0 (Snello/Alto)</td>
      <td style="padding:10px 14px;">2.8 bar</td>
      <td style="padding:10px 14px;">Configurazione standard bilanciata.</td>
    </tr>
    <!-- Taglie 800 / 1200 -->
    <tr>
      <td rowspan="2" style="padding:10px 14px; font-weight:bold; vertical-align:middle;">800-1200</td>
      <td style="padding:10px 14px;">I<sub>s</sub> &lt; 1.0 (Piatto/Largo)</td>
      <td style="padding:10px 14px;">4.0 bar</td>
      <td style="padding:10px 14px;">Necessaria per separare geometrie piatte e pesanti.</td>
    </tr>
    <tr>
      <td style="padding:10px 14px;">I<sub>s</sub> &ge; 1.0 (Snello/Alto)</td>
      <td style="padding:10px 14px;">3.5 bar</td>
      <td style="padding:10px 14px;">Punto di partenza ottimale per componenti ingombranti.</td>
    </tr>
  </tbody>
</table>

:::

### Fattore correttivo del materiale ($K_m$)

La rigidezza del componente influisce direttamente sull’efficienza di trasmissione dell’impulso del flip. I materiali a comportamento elastico o smorzante assorbono parte dell’energia cinetica durante l’impatto, richiedendo una compensazione della pressione di linea.

- **Materiali rigidi** ($K_m$ = 1.0):

  *Materiali:* acciaio, alluminio, ottone, lamiera, POM, PA (Nylon rigido), ABS, vetro, bachelite.

  *Note:* Urto perfettamente elastico. La totalità dell’energia viene trasferita al pezzo, che scatta istantaneamente. Non è richiesta alcuna correzione sulla pressione base.

- **Materiali semi-rigidi** ($K_m$ = 1.2):

  *Materiali:* polietilene (PE), polipropilene (PP), Nylon non caricato, cartone denso, materiali compositi stratificati.
  
  *Note:* Presenza di micro-smorzamento strutturale. Aumentare la pressione base del 20% per garantire la stessa altezza di salto del pezzo rigido.

- **Materiali rigidi** ($K_m$ = 1.0):

  *Materiali:* gomma naturale, gomma nitrilica (NBR), silicone, poliuretano, TPU morbido.
  
  *Note:* Urto fortemente anelastico. Il componente si deforma momentaneamente sotto l'impulso. Richiede un incremento della pressione base del 50% (fino al raggiungimento del limite massimo di linea di 6.0 bar se necessario).

### Fattore correttivo del peso ($K_w$)

La massa del componente determina la sua inerzia al decollo. Componenti molto leggeri richiedono pressioni ridotte per evitare traiettorie caotiche o fuoriuscite dal piatto, mentre componenti pesanti necessitano di una spinta energetica maggiore per sollevare il baricentro.

:::{raw} html
<style>
  table.ars-table {
    border-collapse: collapse;
    width: 100%;
    font-family: inherit;
    border: 1px solid #cccccc;
  }
  table.ars-table thead tr {
    background-color: #f5f5f5;
    border-bottom: 2px solid #3366CC;
  }
  table.ars-table thead th {
    font-weight: bold;
    padding: 12px 16px;
    text-align: center;
    border-right: 1px solid #cccccc;
  }
  table.ars-table thead th:first-child { text-align: left; }
  table.ars-table thead th:last-child  { border-right: none; }
  table.ars-table tbody tr:nth-child(odd)  { background-color: #f5f5f5; }
  table.ars-table tbody tr:nth-child(even) { background-color: #ffffff; }
  table.ars-table tbody tr:hover           { background-color: #ddeeff; }
  table.ars-table td {
    padding: 10px 16px;
    text-align: center;
    border-right: 1px solid #cccccc;
  }
  table.ars-table td:first-child { text-align: left; }
  table.ars-table td:last-child  { border-right: none; }

/* Struttura principale della tabella */
[data-theme="dark"] table.ars-table {
  border-collapse: collapse;
  border-spacing: 0;
  
  /* Rimuove i bordi verticali esterni (sinistro e destro) */
  border-left: none;
  border-right: none;
  
  /* Mantiene solo i sottili bordi orizzontali esterni (sopra e sotto) */
  border-top: 1px solid #383f4f;
  border-bottom: 1px solid #383f4f;
}

/* Gestione dei bordi interni delle celle (th e td) */
[data-theme="dark"] table.ars-table th,
[data-theme="dark"] table.ars-table td {
  padding: 10px 12px;
  
  /* Linea orizzontale inferiore uguale per tutte le righe */
  border-bottom: 1px solid #383f4f;
  
  /* Linea verticale interna (a destra di ogni cella) */
  border-right: 1px solid #383f4f;
  
  /* Azzera gli altri lati per evitare conflitti */
  border-left: none;
  border-top: none;
}

/* Elimina l'ultima linea verticale a destra per non creare il bordo esterno destro */
[data-theme="dark"] table.ars-table th:last-child,
[data-theme="dark"] table.ars-table td:last-child {
  border-right: none;
}

/* Elimina l'ultima linea orizzontale per non raddoppiarla con il fondo della tabella */
[data-theme="dark"] table.ars-table tbody tr:last-child td {
  border-bottom: none;
}

/* ══════════ SEZIONE COLORI COINCIDENTI ══════════ */

/* Sfondo dell'header */
[data-theme="dark"] table.ars-table thead tr {
  background-color: #29313d;
}

[data-theme="dark"] table.ars-table thead th {
  color: #e0e0e0;
  font-weight: 600;
}

/* Zebra striping identico alla prima tabella */
[data-theme="dark"] table.ars-table tbody tr:nth-child(odd) {
  background-color: #222832; /* Riga scura */
}

[data-theme="dark"] table.ars-table tbody tr:nth-child(even) {
  background-color: #29313d; /* Riga chiara */
}

/* Effetto Hover al passaggio del mouse */
[data-theme="dark"] table.ars-table tbody tr:hover {
  background-color: #282d3a;
}
</style>

<table class="ars-table">
  <thead>
    <tr>
      <th>Categoria</th>
      <th>Massa (FlexiBowl® 200/350/500)</th>
      <th>Massa (FlexiBowl® 650/800/1200)</th>
      <th>K<sub>w</sub></th>
      <th>Note</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Componenti Leggeri</strong></td>
      <td>&lt; 10 g</td>
      <td>&lt; 30 g</td>
      <td>0.8</td>
      <td>Bassa inerzia. Riduce la pressione base del 20% per garantire un salto controllato e smorzato, evitando rimbalzi incontrollati.</td>
    </tr>
    <tr>
      <td><strong>Componenti Standard</strong></td>
      <td>10 &divide; 100 g</td>
      <td>30 &divide; 250 g</td>
      <td>1.0</td>
      <td>Finestra di lavoro ottimale della macchina. Nessuna correzione richiesta.</td>
    </tr>
    <tr>
      <td><strong>Componenti Pesanti</strong></td>
      <td>&gt; 100 g</td>
      <td>&gt; 250 g</td>
      <td>1.3</td>      
      <td>Alta inerzia. Incrementa la pressione base del 30% per vincere la forza di gravità e permettere il ribaltamento della massa.</td>
    </tr>
  </tbody>
</table>
:::

### Calcolo della pressione del flip

La pressione da impostare per il flip si ottiene applicando la formula:

$$
P_{flip} = P_{base} × K_m × K_w
$$

:::{attention}
Se il calcolo matematico restituisce un valore superiore a 6.0 bar, impostare il regolatore sul valore limite di 6.0 bar (massima pressione di esercizio del cilindro flip) e aumentare il parametro Flip Count se il pezzo non si ribalta costantemente. Per una valutazione più precisa e dettagliata dei parametri di flip non esitare a [contattare il nostro team](https://www.arsautomation.com/contact) o richiedere un [*free test*](https://www.flexibowl.it/free-test).
:::