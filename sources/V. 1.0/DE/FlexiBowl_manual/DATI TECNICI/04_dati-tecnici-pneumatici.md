(datipneum)=
# **Technische Daten Pneumatik**

## Pneumatische Eigenschaften des FlexiBowl®

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
         <th>Modell</th>
         <th>FB200</th>
         <th>FB350</th>
         <th>FB500</th>
         <th>FB500E</th>
         <th>FB650</th>
         <th>FB800</th>
         <th>FB1200</th>
       </tr>
     </thead>
     <tbody>
       <tr>
         <td><strong>Eigenschaften der Luft</strong></td>
         <td colspan="7">Saubere Druckluft gemäß ISO 8573-1:2010, Klasse 1.3.2</td>
       </tr>
       <tr>
         <td><strong>Minimaler Versorgungsluftdruck</strong></td>
         <td colspan="6">2 Bar</td><td>2 Bar*</td>
       </tr>
       <tr>
         <td><strong>Maximaler Versorgungsluftdruck</strong></td>
         <td colspan="7">7 Bar</td>
       </tr>       
       <tr>
         <td><strong>Luftverbrauch [l/min]**</strong></td>
         <td>25</td><td>15</td><td>35</td><td>55</td><td>30</td><td>45</td><td>135</td>
       </tr>
       <tr>
         <td><strong>Ø Druckluft-Versorgungsschlauch</strong></td>
         <td colspan="2">Ø6 mm</td>
         <td colspan="5">Ø8 mm</td>
       </tr>
     </tbody>
   </table>
:::

:::{important}
Für seine pneumatische Versorgung benötigt der FlexiBowl® saubere Druckluft gemäß **ISO 8573-1:2010 Klasse 1.3.2**, d. h.:

* Feststoffpartikel müssen eine Größe von ≤0,1 μm haben;

* Drucktaupunkt ≤-20 °C (keine Kondensation oder Reif);

* Ölkonzentration (einschließlich Aerosole und Dämpfe) ≤0,1 mg/m³.
:::

:::{note}
*Der minimale Versorgungsdruck für den FlexiBowl® 1200 beträgt 3 bar, wenn dieser mit Entleerung ausgestattet ist.
:::

:::{note}
**Durchschnittlicher Verbrauch bei ausschließlicher Verwendung des Flips. Die Installation der Blasdüsen kann den Verbrauch um bis zu 75 % erhöhen.
:::

:::{warning}
Die Verwendung von nicht konformer Luft kann zu Fehlfunktionen, Leistungsminderung und vorzeitigem Verschleiß der pneumatischen Komponenten führen.
:::

Auf Anfrage ist optional ein **{ref}`externes Luftfilterset <airfilter>`** erhältlich. Das Set wird empfohlen, wenn die Qualität der Druckluft in der Kundenanlage nicht bekannt oder nicht gewährleistet ist, und ermöglicht das Erreichen der geforderten Qualitätsklasse.

% (sc-pneum)=
% ## Schemi pneumatici

% Seguono gli schemi pneumatici di tutti i modelli a listino, comprensivi di eventuali accessori svuotamento e soffi:

% ::::{grid} 2
% :gutter: 3

% :::{grid-item-card}
% :shadow: md
% :class-card: pneum-card
% :class-header: pneum-card-header
% **FlexiBowl® 200 C**
% ^^^
% {download}`⬇ Scarica PDF <../../../../_shared/media/documents/AS000001-pneum.pdf>`
% :::

% :::{grid-item-card}
% :shadow: md
% :class-card: pneum-card
% :class-header: pneum-card-header
% **FlexiBowl® 200 CC**
% ^^^
% {download}`⬇ Scarica PDF <../../../../_shared/media/documents/AS000019-pneum.pdf>`
% :::

% :::{grid-item-card}
% :shadow: md
% :class-card: pneum-card
% :class-header: pneum-card-header
% **FlexiBowl® 350 C**
% ^^^
% {download}`⬇ Scarica PDF <../../../../_shared/media/documents/AS000010-pneum.pdf>`
% :::

% :::{grid-item-card}
% :shadow: md
% :class-card: pneum-card
% :class-header: pneum-card-header
% **FlexiBowl® 350 CC**
% ^^^
% {download}`⬇ Scarica PDF <../../../../_shared/media/documents/AS000020-pneum.pdf>`
% :::

% :::{grid-item-card}
% :shadow: md
% :class-card: pneum-card
% :class-header: pneum-card-header
% **FlexiBowl® 500 C**
% ^^^
% {download}`⬇ Scarica PDF <../../../../_shared/media/documents/AS000004-pneum.pdf>`
% :::
% 
% :::{grid-item-card}
% :shadow: md
% :class-card: pneum-card
% :class-header: pneum-card-header
% **FlexiBowl® 500 CC**
% ^^^
% {download}`⬇ Scarica PDF <../../../../_shared/media/documents/AS000021-pneum.pdf>`
% :::
% 
% :::{grid-item-card}
% :shadow: md
% :class-card: pneum-card
% :class-header: pneum-card-header
% **FlexiBowl® 500 C/E**
% ^^^
% {download}`⬇ Scarica PDF <../../../../_shared/media/documents/AS000005-pneum.pdf>`
% :::
% 
% :::{grid-item-card}
% :shadow: md
% :class-card: pneum-card
% class-header: pneum-card-header
% **FlexiBowl® 500 CC/E**
% ^^^
% {download}`⬇ Scarica PDF <../../../../_shared/media/documents/AS000022-pneum.pdf>`
% :::
% 
% :::{grid-item-card}
% shadow: md
% :class-card: pneum-card
% :class-header: pneum-card-header
% **FlexiBowl® 650 C**
% ^^^
% {download}`⬇ Scarica PDF <../../../../_shared/media/documents/AS000008-pneum.pdf>`
% :::
% 
% :::{grid-item-card}
% :shadow: md
% :class-card: pneum-card
% :class-header: pneum-card-header
% **FlexiBowl® 650 CC**
% ^^^
%  {download}`⬇ Scarica PDF <../../../../_shared/media/documents/AS000024-pneum.pdf>`
% :::
% 
% :::{grid-item-card}
% % :shadow: md
% :class-card: pneum-card
% :class-header: pneum-card-header
% **FlexiBowl® 800 C**
% ^^^
% {download}`⬇ Scarica PDF <../../../../_shared/media/documents/AS000006-pneum.pdf>`
% :::
% 
% :::{grid-item-card}
% :shadow: md
% :class-card: pneum-card
% :class-header: pneum-card-header
% **FlexiBowl® 800 CC**
% ^^^
% {download}`⬇ Scarica PDF <../../../../_shared/media/documents/AS000023-pneum.pdf>`
% :::
% 
% :::{grid-item-card}
% :shadow: md
% :class-card: pneum-card
% :class-header: pneum-card-header
% **FlexiBowl® 1200 C**
% ^^^
% {download}`⬇ Scarica PDF <../../../../_shared/media/documents/AS000012-pneum.pdf>`
% :::
% 
% :::{grid-item-card}
% :shadow: md
% :class-card: pneum-card
% :class-header: pneum-card-header
% **FlexiBowl® 1200 CC**
% ^^^
% {download}`⬇ Scarica PDF <../../../../_shared/media/documents/AS000025-pneum.pdf>`
% :::
% 
% ::::
% 
% (pneucr)=
% ## Clean Room
% 
% Il Clean Room comporta una modifica sostanziale dei collegamenti pneumatici e dei componenti utilizzati; qua sotto sono disponibili gli schemi pneumatici riadattati (sempre comprensivi di eventuali svuotamenti e soffi) :

% :::{list-table}
% :widths: 30 30
% :class: pneum

% * - {download}`FlexiBowl® 200 C <../../../../_shared/media/documents/AS000001-pneum.pdf>`
%   - {download}`FlexiBowl® 200 CC <../../../../_shared/media/documents/AS000019-pneum.pdf>`

% * - {download}`FlexiBowl® 350 C <../../../../_shared/media/documents/AS000010-pneum.pdf>`
%   - {download}`FlexiBowl® 350 CC <../../../../_shared/media/documents/AS000020-pneum.pdf>`

% * - {download}`FlexiBowl® 500 C <../../../../_shared/media/documents/AS000004-pneum.pdf>`
%   - {download}`FlexiBowl® 500 CC <../../../../_shared/media/documents/AS000021-pneum.pdf>`

% * - {download}`FlexiBowl® 500 C/E <../../../../_shared/media/documents/AS000005-pneum.pdf>`
%   - {download}`FlexiBowl® 500 CC/E <../../../../_shared/media/documents/AS000022-pneum.pdf>`

% * - {download}`FlexiBowl® 650 C <../../../../_shared/media/documents/AS000008-pneum.pdf>`
%   - {download}`FlexiBowl® 650 CC <../../../../_shared/media/documents/AS000024-pneum.pdf>`

% * - {download}`FlexiBowl® 800 C <../../../../_shared/media/documents/AS000006-pneum.pdf>`
%   - {download}`FlexiBowl® 800 CC <../../../../_shared/media/documents/AS000023-pneum.pdf>`

% * - {download}`FlexiBowl® 1200 C <../../../../_shared/media/documents/AS000012-pneum.pdf>`
%   - {download}`FlexiBowl® 1200 CC <../../../../_shared/media/documents/AS000025-pneum.pdf>`

% :::