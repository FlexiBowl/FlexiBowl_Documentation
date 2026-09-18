(tracking)=
# [SOF] **Modalità Tracking**

## Funzionamento in Tracking

L'opzione **Flexitracking** consente di massimizzare la produttività del FlexiBowl® facendolo girare in maniera continua e senza interruzioni.  
 Invece di fermarsi a ogni ciclo per scattare la foto e dare al robot il tempo di raccogliere i pezzi presenti sull'area di visione, un encoder tiene traccia dell'angolo di rotazione effettuato dalla superficie del disco rigido dal momento dello scatto della foto a quello della presa del pezzo da parte del robot.  

:::{figure} ../../../../_shared/media/images/Tracking.png
:width: 50%
:align: center
:::

:::{image} ../../../../_shared/media/videos/TRACKING_MODE.GIF
:width: 100%
:align: center
:::

::::{tip}
Il funzionamento in tracking sposta l'area di presa che, se normalmente coincide con quella di visione, in questo caso sarà spostata a valle.  
 Fare riferimento al capitolo di {ref}`Layout Best Practice <layoutbp>` per maggiori informazioni sul piazzamento consigliato del robot e degli altri accessori in caso di funzionamento standard e Flexitracking.  

:::{figure} ../../../../_shared/media/images/TrackingLayout.PNG
:width: 80%
:align: center
:::

::::
---

## Caratteristiche principali

<div class="tracking-features">

| Caratteristica | Descrizione |
|---|---|
| **Prestazioni** | Ideale per massimizzare le performance (fino al 100%) |
| **Area di visione** | Un settore avanti rispetto all'area di presa |
| **Parallelismo** | Scarico hopper, movimento/impulso FlexiBowl®, visione e picking in esecuzione simultanea |
| **Stabilità** | Maggiore stabilità del tempo di ciclo istantaneo |
| **Precisione** | Accuratezza inferiore rispetto alla modalità standard |

</div>

---

## Ciclo operativo

Il funzionamento in tracking si basa su un ciclo continuo suddiviso in quattro fasi che si
svolgono in parallelo:

```{list-table}
:header-rows: 1
:widths: 20 80

* - Fase
  - Descrizione
* - **Detect**
  - La telecamera acquisisce l'immagine di un settore del FlexiBowl®, anticipando l'area di presa.
* - **Move**
  - La bowl ruota in modo continuo, senza fermarsi; l'encoder registra lo spostamento angolare
    in tempo reale.
* - **Flip / Drop**
  - I pezzi non correttamente orientati vengono ribaltati o scaricati nella posizione corretta.
* - **Pick**
  - Il robot preleva i pezzi compensando il movimento del FlexiBowl® grazie ai dati dell'encoder.
```

---

## Hardware e software richiesti

Per abilitare il Flexitracking sono necessari i seguenti componenti:

- **Opzione encoder** sul FlexiBowl®
- **Opzione tracking** sul robot

### Schema di collegamento

Il Flexitracking si basa su un gruppo motore modificato con un supporto per una trasmissione
a cinghia che alimenta l'encoder esterno.

:::{figure} ../../../../_shared/media/images/GM001788.PNG
:width: 80%
:align: center
:::

Il segnale dell'encoder viene distribuito tramite uno **splitter interno**, che lo invia sia
al driver del motore sia al robot:

<div class="hw-schema">

```{list-table}
:header-rows: 1
:widths: 35 65

* - Componente
  - Funzione
* - **Internal encoder splitter**
  - Sdoppia il segnale encoder verso il driver e verso il robot.
* - **External encoder**
  - Montato su un albero collegato alla puleggia condotta tramite una staffa di supporto;
    misura la rotazione effettiva della superficie del disco.
```

</div>

---
## Pagina JOG 

La pagina **Jog Motor** consente di azionare il FlexiBowl® in modalità tracking, senza l'utilizzo di sequenze programmate. È utilizzata principalmente durante le fasi di setup, messa in servizio e test del sistema, permettendo all'operatore di controllare direttamente la rotazione del FlexiBowl® e le funzioni accessorie.
![pagina jog monitor](../../../../_shared/media/images/jog_motor.png)

Per maggiori informazioni, consultare la [Pagina JOG](jog)

#### Comandi EXE JOG

| Comando | ControlWord | Busy durante esecuzione | ReturnData_1 | Spiegazione | 
|---|---|---|---|---|
| Start Jog Seq | 40 | SI | 40 | Avvia Jog |
| Stop Jog Seq | 41 | SI | 41 | Ferma Jog |

#### Comandi WRITE JOG

I comandi del Jog (funzionamento manuale continuo) sono configurabili separatamente tramite ControlWord nel blocco 20000.

| Comando | ControlWord | Range Data_1 | Note |
|---|---|---|---|
| AccelerationJog | 20001 | 0–100 | Rampa di accelerazione del jog (%) |
| DecelerationJog | 20002 | 0–100 | Rampa di decelerazione del jog (%) |
| SpeedJog | 20003 | 0–100 | Velocità jog (%). Valori 1000–1100 = velocità negativa (rotazione inversa) |
| FlipJog_Enable | 20004 | 0–1 | 0 = flip disabilitato, 1 = flip abilitato durante jog |
| FlipJog_Duration | 20005 | 0–1000 | Durata impulso flip (ms) |
| FlipJog_Pressure | 20006 | 0–600 | Pressione flip (/100 = Bar) |
| FlipJog_Pause | 20007 | 0–1000 | Pausa tra flip consecutivi (ms) |
| BlowJog_Enable | 20008 | 0–1 | 0 = blow disabilitato, 1 = blow abilitato durante jog |
| BlowJog_Duration | 20009 | 0–1000 | Durata impulso blow (ms) |
| BlowJog_Pressure | 20010 | 0–600 | Pressione blow (/100 = Bar) |
| BlowJog_Pause | 20011 | 0–1000 | Pausa tra blow consecutivi (ms) |
| BlowJog_Type | 20012 | 0–2 | Tipo di blow: 0 = BLOWc, 1 = BLOWe, 2 = BLOWc+BLOWe |
| Backlight_1 | 20013 | 0–1 | 0 = spento, 1 = acceso |
| Backlight_2 | 20014 | 0–1 | 0 = spento, 1 = acceso |

#### Comandi READ JOG

Gli stessi comandi scrivibili del JOG (blocco 20000) sono leggibili nel blocco 20100:

| Comando | ControlWord READ | Range RestituData_2 |
|---|---|---|
| AccelerationJog | 20101 | 0–100 |
| DecelerationJog | 20102 | 0–100 |
| SpeedJog | 20103 | 0–100 (1000–1100 = negativo) |
| FlipJog_Enable | 20104 | 0–1 |
| FlipJog_Duration | 20105 | 0–1000 |
| FlipJog_Pressure | 20106 | 0–600 (/100) |
| FlipJog_Pause | 20107 | 0–1000 |
| BlowJog_Enable | 20108 | 0–1 |
| BlowJog_Duration | 20109 | 0–1000 |
| BlowJog_Pressure | 20110 | 0–600 (/100) |
| BlowJog_Pause | 20111 | 0–1000 |
| BlowJog_Type | 20112 | 0–2 |
| Backlight_1 | 20113 | 0–1 |
| Backlight_2 | 20114 | 0–1 |

::::{tip}
Per i Codici di Errore, consultare la pagina dedicata. 
:::{card} VAI ALLA PAGINA DEDICATA
:link: sec-err
:link-type: ref
:class-card: isw-card-field
:class-body: isw-card-body
:::
::::
---

## Note operative

:::{warning}
La modalità Tracking offre prestazioni massime ma con una **precisione leggermente inferiore**
rispetto alla modalità standard. Valutare l'adeguatezza in base ai requisiti di tolleranza
del componente da manipolare.
:::

:::{note}
Per la configurazione del parametro di offset tra area di visione e area di presa, fare
riferimento alla sezione di configurazione software del sistema.
:::

