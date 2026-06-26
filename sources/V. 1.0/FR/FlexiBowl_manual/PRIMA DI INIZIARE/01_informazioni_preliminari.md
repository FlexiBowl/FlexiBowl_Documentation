(info)=
# **Informations préliminaires**

Questa sezione contiene informazioni legali e avvertenze importanti relative all'uso del FlexiBowl® e della presente documentazione.   Si prega di leggere attentamente prima di procedere con l'installazione e l'utilizzo del sistema.

---

## Destinatari e pubblico target

```{note}
**A chi è rivolto questo manuale**

Questa documentazione è indirizzata a tecnici qualificati con competenze in:
- Integrazione di sistemi robotizzati
- Configurazione di sistemi di visione industriale
- Installazione e manutenzione di apparecchiature elettromeccaniche

Si presuppone che il lettore possieda le conoscenze tecniche di base necessarie per comprendere le informazioni riportate.   Informazioni facilmente deducibili da disegni tecnici o diagrammi potrebbero non essere ulteriormente dettagliate.
```

---

## Avvertenze importanti

### **Leggere prima dell'uso**
```{warning}

Prima di utilizzare il FlexiBowl®, è obbligatorio:
- Leggere integralmente questo manuale per garantire un uso corretto del sistema
- Rispettare le istruzioni operative e le raccomandazioni
- Formare adeguatamente il personale incaricato dell'utilizzo
- Consultare i manuali di istruzioni di tutti i componenti hardware collegati (FlexiVision One, Tramoggia, VisionController, Camera, Robot ecc.)

Il mancato rispetto di queste indicazioni può causare malfunzionamenti, danni alle apparecchiature o situazioni pericolose.
```
### **Contesto operativo e limitazioni di responsabilità**

Il FlexiBowl® è un sistema di alminentazione flessibile a disco rotante vibrante per il posizionamento e orientamento casuale dei componenti ai fini del prelievo robotico.

```{warning}
Durante l'utilizzo, l'operatore deve:
- Tenere conto degli ingombri fisici del sistema
- Monitorare i movimenti del robot e dell'alimentatore
- Prevedere e gestire situazioni operative impreviste
- Rispettare le norme di sicurezza applicabili a robot e macchinari industriali
```
```{warning}
**ARS S.r.l. declina ogni responsabilità per danni a persone o cose derivanti dal movimento di macchine e sistemi collegati al software FlexiVision One.**

L'integrazione del sistema nell'ambiente di lavoro e la valutazione dei rischi sono responsabilità dell'integratore di sistema e dell'utilizzatore finale.
```

(operatori)=
## Operatori

Allo scopo di stabilire con certezza quali sono le competenze e le qualifiche degli operatori addetti alle varie mansioni (messa in marcia, pulizia, manutenzione ordinaria), consultare la seguente tabella:

:::{list-table}
:header-rows: 1
:widths: 30 70

* - Qualifica
  - Definizione

* - **Integratore di sistema**
  - Personale addetto alla progettazione dei layout, del dimensionamento componenti e della verifica requisiti tecnici per l'installazione del FlexiBowl®.

* - **Tecnico installatore**
  - Personale addetto al montaggio meccanico, allacciamento elettrico e pneumatico e alla configurazione della rete.

* - **Operatore**
  - Personale dell'utilizzatore addestrato e abilitato all'utilizzo e conduzione
    della macchina ai fini produttivi per le attività per cui è stata costruita
    e fornita. Dovrà essere in grado di eseguire tutte le operazioni necessarie
    per il buon funzionamento della macchina e per l'incolumità di sé stesso o
    di eventuali collaboratori. Deve avere una comprovata esperienza nel corretto
    utilizzo di tali tipologie di macchine ed essere formato, informato ed
    istruito a riguardo. In caso di dubbi deve segnalare ogni anomalia al suo
    superiore.

    **Nota:** Non è abilitato ad effettuare alcuna attività di manutenzione.
    
* - **Manutentore meccanico**
  - Tecnico qualificato in grado di:

    * svolgere attività di manutenzione preventiva/correttiva su tutte le parti
      meccaniche della macchina soggette a manutenzione o riparazione;
    * avere accesso a tutte le parti di macchina per analisi visiva, controllo
      dello stato delle apparecchiature, regolazioni e tarature;
    * intervenire sugli organi meccanici per regolazioni, manutenzioni e
      riparazioni;
    * leggere schemi pneumatici, oleodinamici, disegni tecnici e listati dei
      pezzi di ricambio.

    In casi straordinari, è autorizzato a far funzionare la macchina con
    sicurezze ridotte. Ove necessario, può dare all'operatore istruzioni per
    un buon utilizzo della macchina ai fini produttivi.

    **Nota:** Non è abilitato ad intervenire su impianti elettrici sotto
    tensione (se presenti).

* - **Manutentore elettrico**
  - Tecnico qualificato in grado di:
    * svolgere attività di manutenzione preventiva/correttiva su tutte le parti meccaniche della macchina soggette a manutenzione o riparazione;
    * avere accesso a tutte le parti di macchina per analisi visiva, controllo dello stato delle apparecchiature, regolazioni e tarature;
    * condurre la macchina come l’operatore;
    * intervenire sulle regolazioni e sugli impianti elettrici per manutenzione, riparazione e sostituzione pezzi usurati;
    * leggere schemi elettrici e verificare il corretto ciclo funzionale.
  Ove necessario, può dare all’operatore istruzioni per un buon utilizzo della macchina ai fini produttivi. Può operare in presenza di tensione all’interno dei quadri elettrici, scatole di derivazione, apparecchiature di controllo etc. solo se trattasi di persona idonea (PEI). (Fare riferimento normativa **EN50110-1**). Non effettua programmazione software di sistemi quali: PLC (logica o sicurezza), non può modificare le password di sistema.

* - **Tecnico esperto software**
  - Tecnico qualificato in grado di:
    * svolgere attività preventiva/correttiva su tutte le parti software della macchina;
    * avere accesso a tutte le parti di macchina per analisi visiva, controllo dello stato delle apparecchiature, regolazioni e tarature.
  Tecnico qualificato del Costruttore con comprovata esperienza e formazione dei sistemi basati su: PLC/PC azionamenti, ecc. (conoscenza programmazione, funzioni macchina etc.) per operazioni complesse quali ad esempio:
    * modifica dati macchina; 
    * creazione programmi di lavoro; 
    * regolazione parametri drive etc. in quanto a conoscenza del ciclo produttivo, tecnologico e di costruzione della macchina fornita. 
  Può operare all’interno dei quadri elettrici, scatole di derivazione, apparecchiature di controllo etc. in presenza di tensione solo se trattasi di persona idonea (PEI) (Fare riferimento normativa **EN50110-1**). Le competenze sono di tipo elettronico e/o software.

* - **Tecnico del Costruttore**
  - Tecnico qualificato dal Costruttore e/o dal suo distributore per operazioni complesse, in quanto a conoscenza del ciclo produttivo di costruzione della macchina. Questa persona interviene in accordo con le richieste dell’utilizzatore. Le competenze sono di tipo meccanico.

* - **Persona Addestrata**
  - Raggruppa tutte le qualifiche riportate in questa tabella: trattasi di colui che è stato informato, istruito ed addestrato sul lavoro e sugli eventuali pericoli derivanti da un uso improprio. Conosce inoltre l’importanza dei dispositivi di sicurezza, le norme antinfortunistiche e le condizioni di lavoro in sicurezza.

:::

---

## Note sulla documentazione

### **Versione e aggiornamenti**

```{note}

- **Lingua di riferimento**: la versione italiana di questo documento è quella ufficiale e prevale in caso di discrepanze con altre traduzioni
- **Aggiornamenti**: le informazioni contenute sono soggette a modifiche senza preavviso per miglioramenti del prodotto
- **Unità di misura**: salvo diversa indicazione, tutte le dimensioni sono espresse in millimetri (mm)
- **Versione documento**: controllare sempre di disporre della versione più recente consultando il sito [www.flexibowl.it](https://www.flexibowl.it)
```
### **Come usare al meglio questo manuale**

```{tip}

Per un'esperienza ottimale:
- Utilizza il menu di navigazione laterale per passare rapidamente tra le sezioni
- Consulta l'indice iniziale per identificare immediatamente la sezione di tuo interesse
- Presta particolare attenzione ai banner di avvertenza, nota  e suggerimento 
- Segui le procedure nell'ordine indicato, soprattutto durante l'installazione iniziale
- Conserva questo manuale in formato digitale per facilitare ricerche rapide tramite parole chiave
```

---


## Diritti di riproduzione e note legali

```{important}
**Copyright © ARS S.r.l. - Tutti i diritti riservati**

Nessuna parte di questa pubblicazione può essere riprodotta, distribuita, tradotta o trasmessa con qualsiasi mezzo (elettronico, meccanico, fotocopia, registrazione o altro sistema di archiviazione) per scopi diversi dall'uso personale, senza previa autorizzazione scritta di ARS S.r.l.

ARS S.r.l. declina ogni responsabilità per conseguenze derivanti da operazioni errate eseguite dall'utente o dall'uso improprio del prodotto.

**Marchi registrati**: FlexiBowl® è un marchio registrati di ARS S.r.l. Tutti gli altri marchi, nomi commerciali e loghi menzionati in questo documento appartengono ai rispettivi proprietari e sono utilizzati esclusivamente a scopo identificativo.
```
---


