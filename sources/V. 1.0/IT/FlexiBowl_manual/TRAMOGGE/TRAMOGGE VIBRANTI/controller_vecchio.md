# Vecchio Controller
## Controller standard

#### Connessioni elettriche e setup controller

:::{attention}
Prima di accendere il controller collegare la spina Schuko nella presa di corrente verificando che l'impianto abbia un adeguato sistema di messa a terra.
:::

Per eseguire l'avviamento, procedere come descritto:

<div style="display: flex; flex-direction: column; gap: 12px; margin: 20px 0;">
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #34495e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">1</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Collegare il cavo della base lineare al connettore di uscita del controller (collegare quindi il vibratore al connettore di uscita <strong>(1)</strong>).
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #34495e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">2</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Ruotare la manopola di regolazione frequenza <strong>(2)</strong> e di regolazione di ampiezza <strong>(3)</strong> del controller sulla posizione "•".
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #34495e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">3</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Accendere il controller con il pulsante ON/OFF (pulsante su posizione 1 <strong>(4)</strong>).
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #34495e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">4</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Ruotare lentamente le manopole di regolazione <strong>(2 e 3)</strong>. Prima di portare la vibrazione al massimo (Potenziometro Amplitude <strong>(3)</strong>) si consiglia di cercare con il potenziometro Frequency <strong>(2)</strong>, la frequenza di risonanza corretta (50 Hertz).
    </div>
  </div>
</div>

![Controller con Puntatori](../../../../../_shared/media/images/controller_puntatori.png)

Per rispetto della normativa EMC il circuito è dotato di filtro con correnti di perdita verso terra inferiore a 1 mA.  
 Il circuito fornisce al vibratore un segnale PWM (modulazione in larghezza di impulso) regolabile in ampiezza e in frequenza, compensato rispetto alle variazioni della tensione di linea.  
  La sezione di controllo è isolata galvanicamente dalla sezione di potenza.  
   All'accensione il circuito attende qualche secondo prima di abilitare il vibratore.

Il circuito è controllato da microprocessore ed è dotato di limitazione della corrente in uscita tramite fusibile F4 (4 A).

**Protezioni tramite fusibili**

| Fusibile | Valore | Posizione |
| :--- | :--- | :--- |
| **F1** | 6,3 A | Ingresso di linea |
| **F3** | 250 mA | Ingresso ON/OFF — limita la corrente disponibile per il sensore NPN/PNP e l'eventuale elettrovalvola |
| **F4** | 4 A | Uscita vibratore |

**Indicatori LED interni alla scheda**

| LED | Colore | Stato: acceso |
| :--- | :--- | :--- |
| **LD1** | Rosso | Alta tensione presente sui condensatori di filtraggio (fino a oltre 300 V con 230 V di linea) |
| **LD2** | Verde | Tensione presente nel circuito di controllo. Spento se F1, F2 o F3 sono interrotti |
| **LD3** | Verde | Relè ON/OFF commutato — vibratore in marcia o in arresto |
| **LD4** | Giallo | Relè commutato per superamento del tempo di mancanza pezzi |

:::{attention}
Evitare assolutamente di toccare il circuito con il LED rosso (LD1) acceso.
:::

I relè associati a LD3 e LD4 espongono un contatto in scambio sui connettori **CONN4** e **CONN5**: **CONN4** consente il pilotaggio in cascata di un modulo aggiuntivo, **CONN5** l'attivazione di un allarme di flusso pezzi.

**Regolazioni disponibili**

I trimmer sulla scheda permettono di adattare il comportamento del vibratore all'applicazione:

- **TR2** — ritardo al fermo del vibratore (0 ÷ 10 sec)
- **TR3** — ritardo alla partenza del vibratore (0 ÷ 10 sec)
- **TR4** — ampiezza massima
- **TR5** — ritardo aggiuntivo in avvio
- **TR6** — ampiezza minima

Il vibratore può essere bloccato e riavviato tramite comando esterno su **CONN3**, compatibile con contatto pulito, sensore NPN/PNP o uscita 0–24 V, con o senza i ritardi configurati.  
 Tramite **DP1** è possibile selezionare la logica diritta o negata del segnale ON/OFF.

**Configurazione standard consigliata da ARS**

| Componente | Impostazione |
| :--- | :--- |
| **DP1** | Entrambi gli switch in posizione ON |
| **DP2** | Switch 2 ON — Switch 1 OFF |
| **TR2 e TR3** | Vite di regolazione in senso antiorario fino a fine corsa |
| **CONN3** | Start a tramoggia con contatto pulito |

![Disegno Controller](../../../../../_shared/media/images/disegno_controller.jpg)

---

### Controller analogico

![Controller Analogico](../../../../../_shared/media/images/controller_analogico.png)

#### Connessioni elettriche e setup controller

Per eseguire l'avviamento, procedere come descritto e fare riferimento all'immagine a fine paragrafo:

<div style="display: flex; flex-direction: column; gap: 12px; margin: 20px 0;">
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">1</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Collegare l'alimentazione 80/250 Vac al connettore <strong>CONN 1</strong>.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">2</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Collegare il cavo proveniente dalla base vibrante al connettore <strong>CONN 2</strong>.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">3</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Collegare il comando di azionamento sul connettore <strong>CONN 3</strong>.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">4</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Collegare l'ingresso analogico al connettore <strong>CONN 7</strong>.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">5</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Regolare il trimmer <strong>TR1</strong> affinché la frequenza sia pari a 50 Hertz.
    </div>
  </div>
</div>

Per rispetto della normativa EMC il circuito è dotato di filtro con correnti di perdita verso terra inferiore a 1 mA.  
 Il circuito fornisce al vibratore un segnale PWM regolabile in ampiezza tramite segnale analogico e in frequenza tramite il trimmer **TR1**.  
  Il segnale è compensato rispetto alle variazioni della tensione di linea. La sezione di controllo è isolata galvanicamente dalla sezione di potenza.  
   All'accensione il circuito attende qualche secondo prima di abilitare il vibratore.

Il circuito è controllato da microprocessore ed è dotato di limitazione della corrente in uscita tramite fusibile F4 (4 A).

**Protezioni tramite fusibili**

| Fusibile | Valore | Posizione |
| :--- | :--- | :--- |
| **F1–F2** | 6,3 A | Ingresso di linea |
| **F3** | 250 mA | Ingresso ON/OFF — limita la corrente disponibile per il sensore NPN/PNP e l'eventuale elettrovalvola |
| **F4** | 4 A | Uscita vibratore |

**Indicatori LED interni alla scheda**

| LED | Colore | Stato: acceso |
| :--- | :--- | :--- |
| **LD1** | Rosso | Alta tensione presente sui condensatori di filtraggio (fino a oltre 300 V con 230 V di linea) |
| **LD2** | Verde | Tensione presente nel circuito di controllo. Spento se F1, F2 o F3 sono interrotti |
| **LD3** | Verde | Relè ON/OFF commutato — vibratore in marcia o in arresto |
| **LD4** | Giallo | Relè commutato per superamento del tempo di mancanza pezzi |

:::{attention}
Evitare assolutamente di toccare il circuito con il LED rosso (LD1) acceso.
:::

I relè associati a LD3 e LD4 espongono un contatto in scambio sui connettori **CONN4** e **CONN5**: **CONN4** consente il pilotaggio in cascata di un modulo aggiuntivo, **CONN5** l'attivazione di un allarme di flusso pezzi.

**Regolazioni disponibili**

I trimmer sulla scheda permettono di adattare il comportamento del vibratore all'applicazione:

- **TR2** — ritardo al fermo del vibratore (0 ÷ 10 sec)
- **TR3** — ritardo alla partenza del vibratore (0 ÷ 10 sec)
- **TR4** — ritardo oltre il quale scatta l'allarme mancanza pezzi (0 ÷ 10 sec)
- **TR5** — tempo aggiuntivo di attivazione dell'elettrovalvola di soffio aria dopo l'arresto del vibratore (0 ÷ 3 sec)
- **TR6** — rampa all'accensione del vibratore (0 ÷ 3 sec)
- **TR7** — ampiezza massima sul vibratore

Il vibratore può essere bloccato e riavviato tramite comando esterno su **CONN3**, compatibile con contatto pulito, sensore NPN/PNP o uscita 0–24 V, con o senza i ritardi configurati.  
 Tramite **DP1** è possibile selezionare la logica NC o NO del segnale ON/OFF.    
 L'ampiezza di vibrazione si regola impostando la tensione analogica appropriata su **CONN7**.

**Configurazione standard consigliata da ARS**

| Componente | Impostazione |
| :--- | :--- |
| **DP1** | Entrambi gli switch in posizione ON |
| **DP2** | Switch 1 ON — Switch 2 OFF |
| **TR2 e TR3** | Vite di regolazione in senso antiorario fino a fine corsa |
| **CONN3** | Start a tramoggia con contatto pulito |


![Schema Controller](../../../../../_shared/media/images/controller_schema.png)