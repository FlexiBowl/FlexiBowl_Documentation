(Installazione_Meccanica)=
# **Installazione Meccanica del Sistema**

Questa sezione descrive i requisiti di montaggio e posizionamento dei componenti chiave del sistema di visione FlexiVision One.     L'installazione deve essere eseguita solo dopo aver completato l'installazione meccanica di base del FlexiBowl e dell'eventuale tramoggia.

```{warning}
**Prerequisiti obbligatori**

Prima di procedere con l'installazione dei componenti di visione, assicurarsi che:

- Il FlexiBowl sia stato montato e fissato alla struttura portante (cellula robotica)
- La tramoggia (Hopper) sia stata installata correttamente
- La struttura di supporto per camera e illuminatore sia stata preparata

Per l'installazione del FlexiBowl, consultare il Manuale Dedicato fornito.
```

```{note}
**Competenze richieste**

L'installazione meccanica richiede:
- Competenze di base in assemblaggio meccanico
- Utilizzo di strumenti di misura (calibro, livella, metro)
- Capacità di lettura di disegni tecnici 
```

---

## Montaggio VisionController

Il VisionController (PC Industriale) gestisce l'elaborazione delle immagini e la comunicazione con il robot.   
Essendo un componente elettronico sensibile, richiede un posizionamento attento per garantire ventilazione adeguata e protezione da contaminanti.

### Specifiche tecniche 
```{figure} ../../../../_shared/media/images/Dim_PC.png
:alt: Dimensioni VisionController
:align: center
:width: 80%
```

```{list-table}
:header-rows: 1
:widths: 40 60
* - **Fori Viti**
  - M5
* - **Caratteristica**
  - **Valore**
* - Larghezza (totale con staffe)
  - 245.00 mm
* - Larghezza (corpo)
  - 227.00 mm
* - Larghezza pannello connettori
  - 200.00 mm
* - Altezza (totale con staffe)
  - 123.00 mm
* - Altezza (corpo)
  - 120.00 mm
* - Profondità
  - 61.10 mm
```

### Requisiti di montaggio

```{list-table}
:header-rows: 1
:widths: 35 65

* - Requisito
  - Specifiche
* - **Posizione consigliata**
  - Interno quadro elettrico o su pannello dedicato vicino alla cella robotica
* - **Spazio di ventilazione**
  - Minimo 50 mm su tutti i lati per circolazione aria
* - **Fissaggio**
  - Guida DIN 35 mm o viti M5 su pannello
* - **Temperatura ambiente**
  - 1°C ~ +50°C (verificare specifiche complete nella sezione [Specifiche VisionController](specifiche_VC))
* - **Protezione**
  - IP40 minimo (consigliato montaggio in quadro elettrico IP54)
```

### Procedura di installazione

#### Montaggio con Fori 

```{list-table} 
   :header-rows: 1
   :widths: 35 65

   * - Fase
     - Descrizione Operativa
   * - **1. Preparazione supporto**
     - Praticare i fori secondo le indicazioni riportate nella scheda tecnica 
   * - **2. Disimballaggio**
     - Estrarre il VisionController dalla confezione prestando attenzione a non danneggiare i connettori. Verificare l'integrità del prodotto.
   * - **3. Fissaggio**
     - Fissare il VisionController con viti M5  
```

#### Montaggio con guida DIN

```{list-table} 
   :header-rows: 1
   :widths: 35 65

   * - Fase
     - Descrizione Operativa
   * - **1. Preparazione supporto**
     - verificare che la guida sia pulita e fissata saldamente.
   * - **2. Disimballaggio**
     - Estrarre il VisionController dalla confezione prestando attenzione a non danneggiare i connettori. Verificare l'integrità del prodotto.
   * - **3. Fissaggio**
     - Agganciare il dispositivo facendolo scorrere sulla guida fino allo scatto.  
```

```{warning}
**Ventilazione**

Il VisionController genera calore durante il funzionamento. Garantire sempre almeno 50 mm di spazio libero attorno al dispositivo.
Altrimenti si può avere:
- Surriscaldamento e spegnimenti automatici
- Riduzione delle prestazioni
- Danneggiamento dei componenti interni
```

---

## Montaggio Camera

Il posizionamento preciso e l'allineamento della telecamera sono passaggi critici che influenzano direttamente l'accuratezza della calibrazione e le prestazioni del sistema di picking.


### Distanza di lavoro ottimale

La telecamera deve essere montata in modo che la faccia frontale della lente sia posizionata a una distanza specifica (Working Distance) dalla superficie del piatto FlexiBowl.  
Per il calcolo dettagliato della distanza ottimale per la vostra applicazione, consultare la sezione dedicata: [Calcolo Distanza Ottimale](distanza_lavoro)

```{image} ../../../../_shared/media/images/working_distance.JPG
:alt: Distanza Di Lavoro
:width: 40%
:align: center
```

```{list-table}
:header-rows: 1
:widths: 25 40 35

* - Modello FlexiBowl
  - Distanza di Lavoro Raccomandata (Working Distance)
  - Lente Inclusa nel Kit (Lunghezza Focale)
* - **FB 200**
  - 800 mm 
  - 35 mm
* - **FB 350**
  - 1000 mm
  - 35 mm
* - **FB 500**
  - 1000 mm
  - 25 mm
* - **FB 650**
  - 1000 mm
  - 16 mm
* - **FB 800**
  - 1000 mm
  - 16 mm
* - **FB 1200**
  - 1300 mm
  - 12 mm
```

### Posizionamento e allineamento

Il corretto allineamento della camera è fondamentale per ottenere immagini di qualità e garantire precisione nel picking.

**Configurazioni errate.** Le immagini mostrano esempi di posizionamento non corretto della camera: il campo visivo (indicato in rosso) risulta decentrato rispetto all'area di visone, coprendo solo parzialmente l'area di lavoro o includendo zone esterne ad essa. Queste configurazioni compromettono il riconoscimento dei pezzi e il funzionamento del sistema di visione.    

```{image} ../../../../_shared/media/images/config_sbagliata.png
:alt: Distanza Di Lavoro
:width: 60%
:align: center
```
```{image} ../../../../_shared/media/images/config_sbagliata2.png
:alt: Distanza Di Lavoro
:width: 60%
:align: center
```
**Configurazione corretta.** La camera deve essere posizionata centralmente rispetto all'area di visione del FlexiBowl (zona backlight). In questo modo il campo visivo (indicato in verde) copre simmetricamente l'intera area di lavoro, garantendo il corretto funzionamento del sistema di visione.  

```{image} ../../../../_shared/media/images/config_giusta.JPG
:alt: Distanza Di Lavoro
:width: 70%
:align: center
```

```{list-table}
* - **Centratura:**
  - 
    - La camera deve essere posizionata esattamente al di sopra dell'area di visione del FlexiBowl
    - Tolleranza massima di centratura: ±5 mm
* - **Ortogonalità:**
  - 
    - La camera deve essere montata perfettamente parallela alla superficie del piatto
    - Non sono ammesse inclinazioni laterali (tilt) o rotazioni rispetto alla verticale
    - Tolleranza massima di inclinazione: ±1°
```

```{tip}
Per facilitare la messa a punto e permettere aggiustamenti futuri, si raccomanda fortemente di progettare il supporto meccanico della camera con possibilità di microregolazioni:
- **Asse Z (altezza)**: -10 mm / +30 mm (per adattamento distanza di lavoro)
- **Asse X (sinistra-destra)**: ±10 mm (per centratura fine)
- **Asse Y (avanti-indietro)**: ±10 mm (per centratura fine)
Questa flessibilità è particolarmente utile durante la calibrazione iniziale e per eventuali ricalibrazione future.
```

### Dimensioni Camera 
```{figure} ../../../../_shared/media/images/Dimensioni_Cam.png
:alt: Dimensioni camera CAM-CIC-5000-20G-1
:align: center
:width: 100%

Dimensioni camera CAM-CIC-5000-20G-1 (mm)
```
```{list-table}
:header-rows: 1
:widths: 40 60

* - **Caratteristica**
  - **Valore**
* - Larghezza × Altezza (corpo)
  - 29 × 29 mm
* - Profondità (corpo)
  - 42.0 mm
* - Profondità totale (incluso connettore posteriore)
  - 48.9 mm
* - Sporgenza frontale (attacco obiettivo)
  - 12.60 mm
* - Interasse fori di fissaggio laterali (M2)
  - 20.0 × 23.7 mm
* - Fori di fissaggio frontali
  - 2× M2 profondità 3 mm
* - Fori di fissaggio laterali
  - 4× M2 profondità 3.5 mm + 3× M3 profondità 3.5 mm
* - Peso
  - 88 g
```
```{warning}
**Fissaggio:**
- Utilizzare i 4 fori di montaggio M3 presenti sul corpo camera
- Viti consigliate: Viti consigliate: M3 A2 / M3 8.8
- Coppia di serraggio: 0.5 Nm (non serrare eccessivamente per evitare deformazioni)
```
```{tip}
**Regolazione della posizione della camera**

Per permettere aggiustamenti futuri ed evitare problemi di allineamento, progettare il supporto meccanico con possibilità di microregolazione su tutti gli assi:

- **Asse Z (altezza)**: -10 mm / +30 mm
- **Asse X (sinistra-destra)**: ±10 mm
- **Asse Y (avanti-indietro)**: ±10 mm

Un supporto con viti serrate definitivamente senza possibilità di regolazione rende impossibile correggere la posizione della camera dopo il montaggio iniziale.
```
### Verifica montaggio lente

```{warning}
Prima di procedere con il fissaggio definitivo:
1. Verificare visivamente che la lente sia installata
2. Controllare che la lunghezza focale sia corretta per il vostro modello di FlexiBowl (etichetta sulla lente o documentazione dell'ordine)
3. Assicurarsi che la lente sia avvitata completamente (contatto metal-metal tra lente e corpo camera)
4. NON rimuovere o allentare la lente se già montata correttamente
```
### Installazione Camera
Per garantire il corretto funzionamento del sistema di visione è necessario che la telecamera sia installata su un supporto rigido e stabile.
Il sistema Flexibowl non genera vibrazioni; tuttavia, nelle linee automatizzate sono presenti altre sorgenti di vibrazione,(robot industriali,sistemi di movimentazione,altre macchine della linea)

Se tali vibrazioni vengono trasmesse alla telecamera, l'immagine acquisita può risultare instabile e le coordinate calcolate dal sistema di visione potrebbero non essere affidabili, compromettendo la precisione del prelievo robotizzato.

![Installazione Camera](../../../../_shared/media/images/installazionecamera.png)

:::{tip}
Per questo motivo si raccomanda di:

- installare la telecamera su una struttura rigida e stabile

- evitare supporti soggetti a vibrazioni provenienti da robot o altre macchine

- utilizzare preferibilmente una struttura indipendente dalla macchina
:::

```{warning}
**Viti di fissaggio camera: prevenzione allentamento**

Le viti di fissaggio della camera possono allentarsi nel tempo per le seguenti cause:

- **Coppia di serraggio eccessiva (> 0.5 Nm)**: può causare deformazioni del corpo camera e successivo allentamento. Serrare sempre con coppia massima di **0.5 Nm**.
- **Vibrazioni trasmesse dalla linea**: utilizzare **frenafiletti medio** su tutte le viti di fissaggio.
- **Viti non idonee**: verificare l'utilizzo di viti **M3 × 8 mm inox** come consigliato.
```

### Regolazione della posizione della telecamera:

Il supporto della telecamera deve consentire la regolazione della posizione per permettere il corretto allineamento con l’area di prelievo del Flexibowl.

![Regolazioni Cmera](../../../../_shared/media/images/regolazionicamera.png)

:::{note}
Partendo da un posizionamento nominale con inclinazione, altezza e posizionamento corretto al centro dell'area retroilluminata, si raccomanda di prevedere le seguenti regolazioni:

Regolazione X/Y → ± 50mm
Regolazione Z → ± 50mm
Rotazione θ → ± 10°
:::

```{caution}
**Camera danneggiata durante il montaggio**

Per evitare danni alla telecamera durante le operazioni di installazione e regolazione:

- **Coppia di serraggio eccessiva**: non superare **0.5 Nm** di coppia sulle viti M3. Il superamento di questo valore può deformare il corpo ottico in modo irreversibile.
- **Manipolazione scorretta**: maneggiare sempre la camera con cura, evitando pressioni dirette sul corpo ottico e sul sensore.
- **Urti durante l'installazione**: proteggere la camera durante eventuali lavori meccanici circostanti (foratura, fresatura, serraggio strutture).
```
---

## Montaggio Toplight

Se l'ordine include un Toplight (illuminatore dall'alto), questo deve essere montato sulla stessa struttura di supporto della telecamera per garantire un'illuminazione uniforme della superficie di lavoro.

:::{attention}
Durante il montaggio, l'apparecchio deve essere spento e staccato dalla corrente.
:::
### Dimensioni Toplight 
![Dimensioni Toplight](../../../../_shared/media/images/toplight_dim.JPG)

| Lunghezza x Larghezza (mm) | Altezza (mm) | Altezza con piastra di fissaggio (mm) | Diametro foro centrale | Superficie utile massima [A x B] | Perimetro utile massimo |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **A x B** | **C** | **C + 10 mm** | **D** | **–** | **–** |
| 500x300 | 45 | 55 | 65 | 0,15 m² | 1,6 m |
| 700x300 | 45 | 55 | 65 | 0,21 m² | 2 m |
| 700x500 | 45 | 55 | 65 | 0,35 m² | 2,4 m |
| 900x600 | 45 | 55 | 65 | 0,54 m² | 3 m |

### Posizionamento Toplight 
Il toplight deve essere posizionato centralmente rispetto alla superficie utile del pannello luminoso,
con l'ottica della telecamera montata all'interno del foro centrale, a filo con la superficie superiore del toplight.   
Le frecce rosse indicano le viti di fissaggio delle ghiere dell'obiettivo, una per la regolazione del fuoco e una per la regolazione del diaframma. Come mostrato nella figura, il toplight deve essere montato in modo che le due viti restino accessibili dall'alto. 

![Posizione Toplight e Cam](../../../../_shared/media/images/posizione_cam_TPL_B.png)

Il campo visivo della telecamera e il fascio luminoso del toplight (in verde) devono essere allineati concentricamente e perpendicolarmente rispetto all'area di visione sul FlexiBowl.    
Come mostrato nelle tre viste (frontale, dall'alto e assonometrica), il toplight deve illuminare esattamente l'area inquadrata dalla telecamera, con entrambi i componenti centrati sull'asse ottico verticale del sistema.  

![Posizione Toplight Cam + FB](../../../../_shared/media/images/posizioneTPL_giusta.png)

Un posizionamento errato si verifica quando il toplight e la telecamera non sono centrati sull'area di visione del FlexiBowl.   
Come illustrato (in rosso), due errori tipici sono:  
- spostarsi in avanti o indietro rispetto all'area di visione.  
- ruotare il toplight rispetto ad essa.   
  
In entrambi i casi, l'illuminazione risulta disassata e non perpendicolare, compromettendo la qualità dell'acquisizione.

![Posizione Toplight Cam + FB Sbagliata](../../../../_shared/media/images/posizioneTPL_sbagliata.png)

### Procedura di installazione
```{list-table}
:header-rows: 1
:widths: 35 65

* - **Fase**
  - **Istruzioni operative**
* - **1. Posizionamento**
  - Fissare il Toplight sulla struttura di supporto in posizione concentrica rispetto alla camera.
* - **2. Distanza dalla superficie**
  - Posizionare l'illuminatore a una distanza dalla superficie del FlexiBowl simile a quella della camera per:
    
    * Minimizzare le ombre proiettate dai pezzi
    * Massimizzare l'uniformità luminosa
    * Evitare riflessioni dirette verso la camera
* - **3. Orientamento**
  - Assicurarsi che la superficie emittente del Toplight sia parallela al piatto del FlexiBowl.
* - **4. Angolo di illuminazione**
  - Perpendicolare alla superficie (0° tilt).
* - **5. Fissaggio**
  - Secondo specifiche della modalità scelta (vedi sezione seguente).
```

### Modalità di fissaggio

Il Toplight può essere fissato in due modalità: sull'[angolo](angolo) o sul [lato](lato).

:::{note}
I componenti di fissaggio **non sono inclusi** nella fornitura del Toplight. Il montaggio può quindi essere personalizzato in base alle esigenze dell'installazione.

- Fissaggio sul lato (scanalatura): dadi M4 **forniti**
- Fissaggio sull'angolo: viti CHC M4x20 **non fornite**

In entrambi i casi si raccomanda l'uso di un **frenafiletti** (non fornito) per evitare allentamenti nel tempo. La coppia di serraggio consigliata è compresa tra **0,5 e 1,5 Nm**.
:::

(angolo)=
#### 1. Fissaggio sull'angolo

Il fissaggio sull'angolo utilizza viti CHC M4x20 (non fornite) applicate nei fori posizionati ai quattro angoli del Toplight.
```{figure} ../../../../_shared/media/images/fissaggio_angolo.png
:alt: Fissaggio del Toplight sull'angolo con vite CHC M4x20
:align: center
:width: 60%

Fissaggio sull'angolo tramite vite CHC M4x20 (non fornita).
```

(lato)=
#### 2. Fissaggio sul lato (scanalatura)

Il fissaggio sul lato utilizza 4 dadi M4 (forniti) da inserire nella scanalatura laterale del profilo del Toplight. La profondità massima di inserimento del dado nella scanalatura è di **5 mm**.

```{figure} ../../../../_shared/media/images/fissaggio_lato.JPG
:alt: Fissaggio del Toplight sul lato tramite dadi M4 nella scanalatura
:align: center
:width: 100%

Fissaggio sul lato tramite 4 dadi M4 (forniti) inseriti nella scanalatura del profilo. Profondità massima: 5 mm.
```

##### Fissaggio laterale con staffe 
Nel caso in cui il Toplight venisse fissato con delle staffe: 

:::{error}
![montaggio Laterale](../../../../_shared/media/images/errorimontaggiolaterale.png)
:::

:::{tip}
![montaggio Laterale](../../../../_shared/media/images/montaggiolaterale.png)
:::


### Cablaggio illuminatore


![Pin Toplight](../../../../_shared/media/images/pin_toplight.png)

```{list-table} 
:header-rows: 1
:widths: 30 70

* - Parametro
  - Requisito / Azione
* - **Tensione**
  - 24V DC (±10%). Tensione minima di funzionamento: 20V DC sull'ingresso luce.
* - **Connettore**
  - M12 5 poli (T-coding).
* - **Pinout connettore**
  - Pin 1: +24V (marrone) — Pin 3: GND (blu) — Pin 4: STROBE PNP (nero)
* - **Modalità STROBE (PNP)**
  - Da 5V a 24V per accensione al 100%. Da 0V a 1V per spegnimento al 100%.
* - **Modalità CONTINUA**
  - Pin 1 (+24V) e Pin 3 (GND) collegati; Pin 4 (PNP) collegato a Pin 1.
* - **Caduta di tensione (cavo M12, 10m)**
  - 1.15V @ 5A — 2.3V @ 10A — 3.5V @ 15A — 4.6V @ 20A (max 20A)
* - **Schermatura**
  - Utilizzare cavi schermati per ridurre le interferenze elettromagnetiche (EMI).
```
```{warning}
**Sicurezza elettrica**

- Rispettare le tensioni di alimentazione e i morsetti di connessione indicati.
- Non modificare né smontare il prodotto.
- Non collegare o pulire l'apparecchio quando è sotto tensione.
- Non guardare direttamente la sorgente luminosa.
```
```{note}
Per dettagli sui collegamenti elettrici, consultare la sezione [Cablaggio e Connessioni](10_Cablaggio_Connessioni.md).
```

---

## Schermatura da luce ambientale

La stabilità del sistema di visione dipende fortemente dalla consistenza delle condizioni di illuminazione. La luce ambientale variabile può causare rilevazioni incoerenti.

```{warning}
**Protezione da fonti luminose esterne**

Si raccomanda fortemente di schermare la cella robotica da:
- Luce solare diretta o indiretta
- Illuminazione artificiale variabile (es. lampade con dimmer)
- Riflessi da superfici lucide circostanti
- Flash o luci intermittenti nell'area

```
---

## Riferimenti correlati

Per informazioni complementari all'installazione meccanica:

- **Calcolo della distanza ottimale camera**: [Calcolo Distanza Ottimale](distanza_lavoro)
- **Specifiche tecniche complete**: [Specifiche FlexiVision One](specifiche_tecniche)
- **Passo successivo - Collegamenti elettrici**: [Cablaggio e Connessioni](cablaggio)
- **Calibrazione camera**: [Calibrazione della Camera](calibrazione)




<br>

<!-- Versions and languages set-up -->
<style>
  .fixed-bar {
    position: fixed;
    bottom: 10px;
    right: 10px;
    background: rgba(240, 240, 240, 0.85);
    border: 1px solid rgba(100, 100, 100, 0.3);
    border-radius: 6px;
    box-shadow: 0 1px 6px rgba(0, 0, 0, 0.1);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 0.9rem;
    color: #222;
    display: flex;
    gap: 12px;
    padding: 6px 12px;
    align-items: center;
    z-index: 9999;
    backdrop-filter: saturate(180%) blur(10px);
  }

  @media print {
    .fixed-bar {
      display: none !important;
    }
  }

  .fixed-bar .dropdown {
    position: relative;
    user-select: none;
  }

  .fixed-bar .dropdown-toggle {
    background-color: rgba(200, 200, 200, 0.4);
    color: #222;
    padding: 6px 10px;
    border: 1px solid rgba(100, 100, 100, 0.3);
    border-radius: 4px;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 6px;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
    white-space: nowrap;
    transition: background-color 0.3s ease;
  }

  .fixed-bar .dropdown-toggle::after {
    content: none !important;
    display: none !important;
  }

  .fixed-bar .dropdown-toggle:hover {
    background-color: rgba(100, 150, 220, 0.2);
    color: #1a3e72;
    border-color: rgba(26, 62, 114, 0.6);
  }

  .fixed-bar .dropdown-toggle .fa {
    font-size: 0.9rem;
  }

  .fixed-bar .dropdown-menu {
    position: absolute;
    bottom: 100%;
    left: 0;
    background-color: rgba(250, 250, 250, 0.95);
    border: 1px solid rgba(150, 150, 150, 0.3);
    border-radius: 4px;
    box-shadow: 0 3px 8px rgba(0, 0, 0, 0.1);
    min-width: 140px;
    max-height: 200px;
    overflow-y: auto;
    display: none;
    flex-direction: column;
    z-index: 10000;
    backdrop-filter: saturate(180%) blur(8px);
  }

  .fixed-bar .dropdown-menu.show {
    display: flex;
  }

  .fixed-bar .dropdown-menu a {
    padding: 8px 12px;
    color: #1a3e72;
    text-decoration: none;
    border-bottom: 1px solid rgba(200, 200, 200, 0.5);
    white-space: nowrap;
    transition: background-color 0.25s ease;
  }

  .fixed-bar .dropdown-menu a:last-child {
    border-bottom: none;
  }

  .fixed-bar .dropdown-menu a:hover {
    background-color: rgba(100, 150, 220, 0.15);
  }

  .dropdown-download-buttons .btn__icon-container svg {
    width: 1em;
    height: 1em;
    stroke: currentColor;
    fill: none;
    stroke-width: 1.6;
    stroke-linecap: round;
    stroke-linejoin: round;
    vertical-align: middle;
  }

  a.headerlink.manual-heading-action {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    margin-left: 0.2em;
    text-decoration: none;
    color: #7b8493;
    transition: color 0.2s ease, opacity 0.2s ease;
  }

  a.headerlink.manual-heading-action svg {
    width: 0.8em;
    height: 0.8em;
    stroke: currentColor;
    fill: none;
    stroke-width: 1.6;
    stroke-linecap: round;
    stroke-linejoin: round;
    vertical-align: middle;
  }

  a.headerlink.manual-feedback-link:hover,
  a.headerlink.manual-feedback-link:focus-visible {
    color: #2563eb;
  }

  a.headerlink.manual-service-link:hover,
  a.headerlink.manual-service-link:focus-visible {
    color: #d97706;
  }
</style>

<div class="fixed-bar" role="region" aria-label="Version and language selector">
  <div class="dropdown" data-selector="version">
    <div class="dropdown-toggle" tabindex="0" aria-haspopup="listbox" aria-expanded="false">
      Version: <span class="current-value">V. 1.0</span>
      <span class="caret-icon" aria-hidden="true">&#9662;</span>
    </div>
    <div class="dropdown-menu" role="listbox">
      	<a href="#" role="option">V. 1.0</a>
    </div>
  </div>

  <div class="dropdown" data-selector="language">
    <div class="dropdown-toggle" tabindex="0" aria-haspopup="listbox" aria-expanded="false">
      Language: <span class="current-value">ES</span>
      <span class="caret-icon" aria-hidden="true">&#9662;</span>
    </div>
    <div class="dropdown-menu" role="listbox">
      	<a href="#" role="option">DE</a>
				<a href="#" role="option">EN</a>
				<a href="#" role="option">ES</a>
				<a href="#" role="option">FR</a>
				<a href="#" role="option">IT</a>
    </div>
  </div>
</div>

<script>
  (function () {
    const bar = document.querySelector('.fixed-bar');
    if (!bar) {
      return;
    }

    const inlineVersions = ["V. 1.0"];
    const inlineLanguages = ["DE", "EN", "ES", "FR", "IT"];
    const manifest = window.FV_VERSIONING || null;
    const versions = Array.isArray(manifest && manifest.versions) && manifest.versions.length
      ? manifest.versions
      : inlineVersions;
    const offlineZipEnabled = false;
    const offlineZipFileName = 'Offline manual.zip';
    const americanRegions = new Set([
      'AG', 'AR', 'AW', 'BB', 'BL', 'BM', 'BO', 'BQ', 'BR', 'BS', 'BZ', 'CA', 'CL', 'CO', 'CR',
      'CU', 'CW', 'DM', 'DO', 'EC', 'FK', 'GD', 'GF', 'GL', 'GP', 'GT', 'GY', 'HN', 'HT', 'JM',
      'KN', 'KY', 'LC', 'MF', 'MQ', 'MS', 'MX', 'NI', 'PA', 'PE', 'PM', 'PR', 'PY', 'SR', 'SV',
      'SX', 'TC', 'TT', 'US', 'UY', 'VC', 'VE', 'VG', 'VI', '419'
    ]);
    const additionalAmericanTimeZones = new Set([
      'Atlantic/Bermuda',
      'Pacific/Easter',
      'Pacific/Galapagos',
      'Pacific/Honolulu',
      'Pacific/Pitcairn'
    ]);

    function setCaret(toggle, isOpen) {
      const caret = toggle.querySelector('.caret-icon');
      if (caret) {
        caret.innerHTML = isOpen ? '&#9652;' : '&#9662;';
      }
    }

    function closeAllMenus() {
      bar.querySelectorAll('.dropdown').forEach(dropdown => {
        const menu = dropdown.querySelector('.dropdown-menu');
        const toggle = dropdown.querySelector('.dropdown-toggle');
        menu.classList.remove('show');
        toggle.setAttribute('aria-expanded', 'false');
        setCaret(toggle, false);
      });
    }

    function getLanguagesForVersion(version) {
      const manifestLanguages = manifest &&
        manifest.languagesByVersion &&
        Array.isArray(manifest.languagesByVersion[version]) &&
        manifest.languagesByVersion[version].length
          ? manifest.languagesByVersion[version]
          : null;

      if (manifestLanguages) {
        return manifestLanguages;
      }

      return inlineLanguages;
    }

    function getDefaultLanguageForVersion(version) {
      const manifestDefault = manifest &&
        manifest.defaultLanguageByVersion &&
        typeof manifest.defaultLanguageByVersion[version] === 'string'
          ? manifest.defaultLanguageByVersion[version]
          : '';

      if (manifestDefault) {
        return manifestDefault;
      }

      const availableLanguages = getLanguagesForVersion(version);
      return availableLanguages.length ? availableLanguages[0] : (inlineLanguages[0] || '');
    }

    function populateSelectorMenu(selector, values) {
      const menu = bar.querySelector(`[data-selector="${selector}"] .dropdown-menu`);
      if (!menu) {
        return;
      }

      menu.innerHTML = '';
      values.forEach(value => {
        const link = document.createElement('a');
        link.href = '#';
        link.setAttribute('role', 'option');
        link.textContent = value;
        menu.appendChild(link);
      });
    }

    function getNavigationContext() {
      const currentUrl = new URL(window.location.href);
      const rawSegments = currentUrl.pathname.split('/').filter(Boolean);
      const decodedSegments = rawSegments.map(segment => decodeURIComponent(segment));
      const currentVersionLabel = bar.querySelector('[data-selector="version"] .current-value');
      const currentLanguageLabel = bar.querySelector('[data-selector="language"] .current-value');
      const fallbackVersion = currentVersionLabel ? currentVersionLabel.textContent.trim() : '';
      const versionIndex = decodedSegments.findIndex(segment => versions.includes(segment));
      const currentVersion = versionIndex !== -1 ? decodedSegments[versionIndex] : fallbackVersion;
      const availableLanguages = getLanguagesForVersion(currentVersion);
      const fallbackLanguage = currentLanguageLabel ? currentLanguageLabel.textContent.trim() : '';
      const languageIndex = decodedSegments.findIndex(
        (segment, index) => index > versionIndex && availableLanguages.includes(segment)
      );

      return {
        currentUrl: currentUrl,
        rawSegments: rawSegments,
        versionIndex: versionIndex,
        currentVersion: currentVersion,
        currentLanguage: languageIndex !== -1 ? decodedSegments[languageIndex] : fallbackLanguage
      };
    }

    function refreshNavigationMenus() {
      const context = getNavigationContext();
      const resolvedVersion = versions.includes(context.currentVersion) ? context.currentVersion : (versions[0] || context.currentVersion);
      const availableLanguages = getLanguagesForVersion(resolvedVersion);
      const resolvedLanguage = availableLanguages.includes(context.currentLanguage)
        ? context.currentLanguage
        : (getDefaultLanguageForVersion(resolvedVersion) || context.currentLanguage);

      populateSelectorMenu('version', versions);
      populateSelectorMenu('language', availableLanguages);

      const versionLabel = bar.querySelector('[data-selector="version"] .current-value');
      const languageLabel = bar.querySelector('[data-selector="language"] .current-value');
      if (versionLabel) {
        versionLabel.textContent = resolvedVersion;
      }
      if (languageLabel) {
        languageLabel.textContent = resolvedLanguage;
      }
    }

    function buildScopedUrl(targetVersion, targetLanguage, pageName) {
      const context = getNavigationContext();
      const rootSegments = context.versionIndex !== -1 ? context.rawSegments.slice(0, context.versionIndex) : [];
      const targetPath = '/' + rootSegments.concat([
        encodeURIComponent(targetVersion),
        encodeURIComponent(targetLanguage),
        encodeURIComponent(pageName)
      ]).join('/');

      if (context.currentUrl.protocol === 'file:') {
        return 'file://' + targetPath;
      }

      return context.currentUrl.origin + targetPath;
    }

    function buildTargetUrl(targetVersion, targetLanguage) {
      return buildScopedUrl(targetVersion, targetLanguage, 'index.html');
    }

    function buildSiteRootAssetUrl(fileName) {
      const context = getNavigationContext();
      const rootSegments = context.versionIndex !== -1 ? context.rawSegments.slice(0, context.versionIndex) : [];
      const targetPath = '/' + rootSegments.concat([encodeURIComponent(fileName)]).join('/');

      if (context.currentUrl.protocol === 'file:') {
        return 'file://' + targetPath;
      }

      return context.currentUrl.origin + targetPath;
    }

    function buildClientSiteZipUrl() {
      return buildSiteRootAssetUrl(offlineZipFileName);
    }

    function getHeadingText(heading) {
      const clone = heading.cloneNode(true);
      clone.querySelectorAll('a.headerlink').forEach(link => link.remove());
      return clone.textContent.replace(/\s+/g, ' ').trim();
    }

    function normalizeMailText(text) {
      return String(text || '').replace(/\u00AE/g, '');
    }

    function getTimeZoneAmericaDecision() {
      try {
        const timeZone = String(Intl.DateTimeFormat().resolvedOptions().timeZone || '').trim();
        if (!timeZone) {
          return null;
        }
        return timeZone.startsWith('America/') || additionalAmericanTimeZones.has(timeZone);
      } catch (error) {
        return null;
      }
    }

    function isCoordinateInAmericas(latitude, longitude) {
      if (!Number.isFinite(latitude) || !Number.isFinite(longitude)) {
        return null;
      }

      return latitude >= -60 && latitude <= 85 && longitude >= -170 && longitude <= -25;
    }

    function getCurrentPosition(options) {
      return new Promise((resolve, reject) => {
        if (!navigator.geolocation || typeof navigator.geolocation.getCurrentPosition !== 'function') {
          reject(new Error('Geolocation unavailable'));
          return;
        }

        navigator.geolocation.getCurrentPosition(resolve, reject, options);
      });
    }

    async function resolveServiceAddress() {
      const timeZoneDecision = getTimeZoneAmericaDecision();
      if (timeZoneDecision === false) {
        return 'service@arsautomation.com';
      }

      const canTryGeolocation = Boolean(
        navigator.onLine &&
        window.isSecureContext &&
        navigator.geolocation &&
        typeof navigator.geolocation.getCurrentPosition === 'function'
      );

      if (canTryGeolocation) {
        try {
          const position = await getCurrentPosition({
            enableHighAccuracy: false,
            timeout: 4000,
            maximumAge: 300000
          });
          const inAmericas = isCoordinateInAmericas(position.coords.latitude, position.coords.longitude);
          if (inAmericas !== null) {
            return inAmericas ? 'us.service@arsautomation.com' : 'service@arsautomation.com';
          }
        } catch (error) {
        }
      }

      if (timeZoneDecision === true) {
        return 'us.service@arsautomation.com';
      }

      return 'service@arsautomation.com';
    }

    function buildMailtoUrl(address, subject, body) {
      return 'mailto:' + address +
        '?subject=' + encodeURIComponent(normalizeMailText(subject)) +
        '&body=' + encodeURIComponent(normalizeMailText(body));
    }

    function createHeadingActionLink(className, title, mailtoUrl, svgMarkup) {
      const link = document.createElement('a');
      link.className = 'headerlink manual-heading-action ' + className;
      link.href = mailtoUrl;
      link.title = title;
      link.setAttribute('aria-label', title);
      link.innerHTML = svgMarkup;
      return link;
    }

    function addHeadingActions() {
      const feedbackIcon = [
        '<svg viewBox="0 0 16 16" aria-hidden="true">',
        '<path d="M3 3.5h10v6.5H7.5L4.5 13v-3H3z"></path>',
        '<path d="M6 6.2h4"></path>',
        '<path d="M6 8.2h3"></path>',
        '</svg>'
      ].join('');

        const serviceIcon = [
          '<svg viewBox="0 0 16 16" aria-hidden="true">',
          '<circle cx="8" cy="8" r="5.2"></circle>',
          '<path d="M6.4 6.1A1.9 1.9 0 0 1 8 5.2c1.1 0 1.9.7 1.9 1.7 0 .8-.4 1.3-1.2 1.8-.6.4-.9.8-.9 1.5"></path>',
          '<circle cx="8" cy="11.7" r="0.45" style="fill:currentColor;stroke:none"></circle>',
          '</svg>'
        ].join('');

      document.querySelectorAll('h1 > a.headerlink, h2 > a.headerlink, h3 > a.headerlink, h4 > a.headerlink, h5 > a.headerlink, h6 > a.headerlink').forEach(link => {
        const heading = link.parentElement;
        if (!heading || heading.querySelector('.manual-feedback-link') || heading.querySelector('.manual-service-link')) {
          return;
        }

        const sectionTitle = getHeadingText(heading);
        const sectionUrl = new URL(link.getAttribute('href'), window.location.href).href;
        const pageUrl = window.location.href.split('#')[0];
        const feedbackBody = [
          'Hello Documentation Team,',
          '',
          'I would like to suggest an improvement for this section of the manual.',
          '',
          'Section: ' + sectionTitle,
          'Page: ' + pageUrl,
          'Section link: ' + sectionUrl,
          '',
          'Suggestion:',
          ''
        ].join('\n');
          const serviceBody = [
            'Hello Service Team,',
            '',
            'I need support related to this section of the manual.',
            '',
            'Section: ' + sectionTitle,
            'Page: ' + pageUrl,
            'Section link: ' + sectionUrl,
            '',
            'FlexiBowl serial number:',
            '',
            'Photos or videos of the issue attached:',
            '',
            'Issue description:',
            ''
          ].join('\n');

        const feedbackLink = createHeadingActionLink(
          'manual-feedback-link',
          'Suggest an improvement for this section',
          buildMailtoUrl('documentation@arsautomation.com', 'Documentation suggestion: ' + sectionTitle, feedbackBody),
          feedbackIcon
        );
          const serviceLink = createHeadingActionLink(
            'manual-service-link',
            'Contact service about this section',
            '#',
            serviceIcon
          );
          serviceLink.addEventListener('click', async event => {
            event.preventDefault();
            const serviceAddress = await resolveServiceAddress();
            window.location.href = buildMailtoUrl(serviceAddress, 'Service request: ' + sectionTitle, serviceBody);
          });

          heading.appendChild(feedbackLink);
          heading.appendChild(serviceLink);
        });
    }

    function enhancePrintMenu() {
      const dropdown = document.querySelector('.dropdown-download-buttons');
      if (!dropdown || dropdown.dataset.printMenuEnhanced === 'true') {
        return;
      }

      dropdown.dataset.printMenuEnhanced = 'true';

      const toggleButton = dropdown.querySelector('.dropdown-toggle');
      const hasReleaseDownloads = offlineZipEnabled;

      if (toggleButton) {
        const toggleLabel = hasReleaseDownloads ? 'Export options' : 'Print options';
        toggleButton.setAttribute('aria-label', toggleLabel);
        toggleButton.setAttribute('title', toggleLabel);
        toggleButton.setAttribute('data-bs-original-title', toggleLabel);
        const toggleIcon = toggleButton.querySelector('i');
        if (toggleIcon) {
          toggleIcon.className = hasReleaseDownloads ? 'fas fa-download' : 'fas fa-print';
        }
      }

      dropdown.querySelectorAll('.btn-download-source-button').forEach(sourceButton => {
        const sourceItem = sourceButton.closest('li');
        if (sourceItem) {
          sourceItem.remove();
        }
      });

      const pagePrintButton = dropdown.querySelector('.btn-download-pdf-button');
      if (pagePrintButton) {
        pagePrintButton.setAttribute('title', 'Print this page');
        pagePrintButton.setAttribute('aria-label', 'Print this page');
        pagePrintButton.setAttribute('data-bs-original-title', 'Print this page');
        const textContainer = pagePrintButton.querySelector('.btn__text-container');
        if (textContainer) {
          textContainer.textContent = 'Print this page';
        }
      }

      const menu = dropdown.querySelector('.dropdown-menu');
      if (!menu) {
        return;
      }

      menu.querySelectorAll('.btn-download-client-site-zip-button').forEach(button => {
        const item = button.closest('li');
        if (item) {
          item.remove();
        }
      });

      if (offlineZipEnabled) {
        const siteZipItem = document.createElement('li');
        const siteZipLink = document.createElement('a');
        siteZipLink.className = 'btn btn-sm dropdown-item btn-download-client-site-zip-button';
        siteZipLink.title = 'Download offline manual';
        siteZipLink.setAttribute('aria-label', 'Download offline manual');
        siteZipLink.setAttribute('download', offlineZipFileName);
        siteZipLink.href = buildClientSiteZipUrl();
        siteZipLink.innerHTML = [
          '<span class="btn__icon-container">',
          '<svg viewBox="0 0 16 16" aria-hidden="true">',
          '<path d="M4 3.5h8v2.5H4z"></path>',
          '<path d="M4 6h8v6.5H4z"></path>',
          '<path d="M8 3.5v9"></path>',
          '<path d="M6.3 9.2L8 10.9l1.7-1.7"></path>',
          '</svg>',
          '</span>',
          '<span class="btn__text-container">Download offline manual</span>'
        ].join('');
        siteZipItem.appendChild(siteZipLink);
        menu.appendChild(siteZipItem);
      }
    }

    refreshNavigationMenus();

    bar.querySelectorAll('.dropdown').forEach(dropdown => {
      const toggle = dropdown.querySelector('.dropdown-toggle');
      const menu = dropdown.querySelector('.dropdown-menu');
      const selector = dropdown.getAttribute('data-selector');

      toggle.addEventListener('click', event => {
        event.stopPropagation();
        const willOpen = toggle.getAttribute('aria-expanded') !== 'true';
        closeAllMenus();

        if (willOpen) {
          menu.classList.add('show');
          toggle.setAttribute('aria-expanded', 'true');
          setCaret(toggle, true);
        }
      });

      menu.addEventListener('click', event => {
        const link = event.target.closest('a');
        if (!link) {
          return;
        }

        event.preventDefault();
        const selectedValue = link.textContent.trim();
        const context = getNavigationContext();
        if (!selectedValue) {
          return;
        }

        if (selector === 'version') {
          const targetVersion = selectedValue;
          const availableLanguages = getLanguagesForVersion(targetVersion);
          const targetLanguage = availableLanguages.includes(context.currentLanguage)
            ? context.currentLanguage
            : getDefaultLanguageForVersion(targetVersion);
          if (targetLanguage) {
            window.location.href = buildTargetUrl(targetVersion, targetLanguage);
          }
          return;
        }

        window.location.href = buildTargetUrl(context.currentVersion, selectedValue);
      });
    });

    window.addEventListener('click', closeAllMenus);
    window.addEventListener('keydown', event => {
      if (event.key === 'Escape') {
        closeAllMenus();
      }
    });

    addHeadingActions();
    enhancePrintMenu();
  })();
</script>
