# **Modalità Standard**

La **Modalità Standard** è la configurazione operativa predefinita del FlexiBowl® e si adatta a qualsiasi tipo di applicazione di alimentazione robotizzata. In questa modalità, il robot e il sistema di visione condividono la stessa area di lavoro, operando in modo coordinato e sequenziale per garantire elevate prestazioni di ciclo.

---

## Principio di funzionamento

Il FlexiBowl® in Modalità Standard esegue un ciclo continuo composto da tre fasi principali, che si ripetono in sequenza:

```{figure} ../../../../_shared/media/images/flexibowl_standard_cycle.jpg
:align: center
:width: 80%
:alt: *Ciclo operativo in Modalità Standard: Detect → Pick-Drop → Move-Flip*
```

### 1. Detect (Rilevamento)

Il sistema di visione acquisisce un'immagine della superficie del FlexiBowl® e identifica la posizione, l'orientamento e la tipologia dei componenti presenti. Le informazioni vengono trasmesse al robot per pianificare le operazioni di prelievo.

### 2. Pick-Drop (Prelievo e Deposito)

Il robot preleva i componenti correttamente orientati dal FlexiBowl® e li deposita nella posizione di destinazione (es. vassoio, nastro trasportatore, stazione di assemblaggio). Le attività di visione e prelievo vengono eseguite **in modo sequenziale**: prima il sistema di visione scansiona la scena, poi il robot interviene.

### 3. Move-Flip (Movimento e Ribaltamento)

Al termine del prelievo, il FlexiBowl® esegue un movimento combinato di rotazione e vibrazione (**flip**) per rimescolare i componenti rimanenti e favorire la corretta presentazione di nuovi pezzi. Contestualmente, lo **scarico dell'hopper** e il **movimento del bowl** vengono eseguiti **in modo simultaneo**, ottimizzando i tempi di ciclo.

---

## Caratteristiche principali

| Caratteristica | Descrizione |
|---|---|
| **Area di lavoro condivisa** | Il robot e il sistema di visione operano nella stessa zona del FlexiBowl® |
| **Applicabilità** | Adatta a tutte le tipologie di applicazione |
| **Scarico hopper** | Eseguito simultaneamente al movimento/impulso del FlexiBowl® |
| **Visione e prelievo** | Eseguiti in sequenza |
| **Misurazione del ciclo** | Il tempo di ciclo è misurato su base al minuto |

---

## Schema del ciclo operativo

Il ciclo si svolge secondo il seguente schema ad anello chiuso:

1. **Detect** — Il sistema di visione scansiona il FlexiBowl® e localizza i componenti.  
2. **Pick-Drop** — Il robot preleva i pezzi identificati e li deposita nella destinazione.  
3. **Move-Flip** — Il FlexiBowl® rimescola i componenti per il ciclo successivo.  
4. Il ciclo ricomincia dal punto 1.

:::{note} 
Durante la fase Move-Flip, lo scarico dell'hopper avviene in parallelo al movimento del FlexiBowl®, riducendo i tempi morti e massimizzando la produttività.
:::

---

## Vantaggi della Modalità Standard

- **Semplicità di integrazione**: la configurazione è immediata e non richiede parametri avanzati.
- **Versatilità**: compatibile con una vasta gamma di componenti e settori industriali.
- **Efficienza**: la simultaneità tra scarico hopper e movimento FlexiBowl® riduce i tempi di attesa.
- **Affidabilità**: il ciclo sequenziale visione–prelievo minimizza gli errori di presa.
