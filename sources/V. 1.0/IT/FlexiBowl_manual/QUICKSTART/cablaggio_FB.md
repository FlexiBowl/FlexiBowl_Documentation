# **[ELE]** Cablaggio del FlexiBowl®

<style>
.ars-dropdown {
  margin-top: 0.35rem;
}
.ars-dropdown summary {
  cursor: pointer;
  color: #2980b9;
  font-weight: 600;
  font-size: 0.82rem;
  padding: 0.35rem 0.7rem;
  border: 1px solid #d0e4f0;
  border-radius: 6px;
  display: inline-block;
  background: #f0f7ff;
  list-style: none;
  user-select: none;
}
.ars-dropdown summary::-webkit-details-marker { display: none; }
.ars-dropdown summary::before {
  content: "▸ ";
}
.ars-dropdown[open] summary::before {
  content: "▾ ";
}
.ars-dropdown[open] summary {
  border-radius: 6px 6px 0 0;
}
.ars-dropdown .ars-dropdown-body {
  border: 1px solid #d0e4f0;
  border-top: none;
  border-radius: 0 0 6px 6px;
  padding: 0.6rem;
  background: #fff;
}
.ars-dropdown img {
  display: block;
  max-width: 100%;
  width: 360px;
  border-radius: 4px;
}
.ars-step-warn, .ars-step-attn, .ars-step-note {
  border-radius: 5px;
  padding: 0.5rem 0.75rem;
  font-size: 0.83rem;
  margin-top: 0.55rem;
  line-height: 1.4;
}
.ars-step-warn { background:#fff3cd; border-left:4px solid #f0ad4e; color:#7a5b00; }
.ars-step-attn { background:#fee2e2; border-left:4px solid #dc2626; color:#8a1c1c; }
.ars-step-note { background:#eef6fc; border-left:4px solid #2980b9; color:#1a3a52; }
.ars-pin-table { width:100%; border-collapse:collapse; font-size:0.8rem; margin-top:0.4rem; }
.ars-pin-table th { background:#f0f4f8; padding:0.3rem 0.5rem; text-align:left; border:1px solid #d0e4f0; }
.ars-pin-table td { padding:0.3rem 0.5rem; border:1px solid #d0e4f0; }


.ars-zoom-img {
  transition: transform 0.35s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.35s ease;
  cursor: zoom-in;
  position: relative;
}
.ars-zoom-img:hover {
  transform: scale(1.8);
  box-shadow: 0 12px 40px rgba(0,0,0,0.22);
  z-index: 10;
}
</style>

:::::{important}

:::{raw} html
   <style>
     .ars-img-row { display: flex; gap: 12px; align-items: center; justify-content: center; }
     .ars-img-row img { width: 25%; }
   </style>
:::

::::{list-table}
:widths: 30 60
:header-rows: 1
* - {ref}`Qualifica operatore <operatori>`
  - {ref}`D.P.I. Necessari <dpi>`

* - **Manutentore elettrico**
  - :::{raw} html
       <div class="ars-img-row">
         <img src="../../../../_shared/media/images/guanti.png" alt="guanti">
         <img src="../../../../_shared/media/images/scarpe.png" alt="scarpe">
         <img src="../../../../_shared/media/images/tuta.png" alt="tuta">
       </div>
    :::
::::
:::::

:::{warning}
Prima di effettuare qualsiasi connessione elettrica, assicurarsi che l'alimentazione sia disinserita e che il sistema sia in stato di sicurezza. 
:::

Il cablaggio del FlexiBowl® cambia in base alla taglia della macchina:

- **FlexiBowl® 500 – 1200**: tutti i collegamenti (STO, Ethernet, Hopper, alimentazione, aria) si trovano su un unico **pannello elettrico standard**, montato direttamente sulla macchina.
- **FlexiBowl® 200 / 350**: i collegamenti principali si trovano su un **rack** esterno; il rack viene poi collegato alla macchina tramite 4 cavi dedicati (Ethernet, Motore+STO, segnale A, segnale B). Sulla macchina resta da collegare solo l'aria compressa.

---

## FlexiBowl® 500 – 1200 — Pannello Elettrico Standard

```{list-table}
:widths: 8 52 40
:header-rows: 1

* - #
  - Azione
  - Immagine
* - 1
  - **Collegare lo STO.**

    <div class="ars-step-note">
    Connettore a 10 pin. Gli ingressi <strong>+STO1</strong> e <strong>+STO2</strong> devono ricevere <strong>+24 Vdc</strong> dal circuito di sicurezza; <strong>−STO1</strong> e <strong>−STO2</strong> vanno collegati al riferimento −24 Vdc.
    </div>

    <details class="ars-dropdown"><summary>Pinout connettore 10 pin</summary><div class="ars-dropdown-body">

    | Pin | Descrizione |
    |---|---|
    | 1 | +24 Vdc |
    | 2 | −24 Vdc |
    | 3 | +STO1 |
    | 4 | −STO1 |
    | 5 | +STO2 |
    | 6 | −STO2 |
    | 7–10 | NC |

    </div></details>
  - 
    ```{image} ../../../../_shared/media/images/connectSTO.png
    :alt: Collegare lo STO
    :class: ars-zoom-img
    ```

* - 2
  - **Collegare l'Ethernet (C-ETH).**

    <div class="ars-step-attn">
    Quando il FlexiBowl® è alimentato, il collegamento Ethernet è <strong>obbligatorio</strong>: se assente, la macchina entra in stato di <strong>ERROR</strong> (LED Ready/Fault rosso).
    </div>

    <details class="ars-dropdown"><summary>Pinout M12 → RJ45</summary><div class="ars-dropdown-body">

    Adattatore M12 8 poli → RJ45:

    | Pin | Colore |
    |---|---|
    | 1 | Giallo |
    | 2 | Arancione |
    | 3 | Bianco |
    | 4 | Non assegnato |
    | 5 | Non assegnato |
    | 6 | Blu |
    | 7 | Non assegnato |
    | 8 | Non assegnato |

    Connettore M12 D-code 4 poli:

    | Pin | Colore |
    |---|---|
    | 1 | Giallo |
    | 2 | Bianco |
    | 3 | Arancione |
    | 4 | Blu |

    </div></details>
  - 
    ```{image} ../../../../_shared/media/images/connectEthernet.png
    :alt: Collegare l'Ethernet
    :class: ars-zoom-img
    ```

* - 3
  - **Collegare l'Hopper.**

    <div class="ars-step-note">
    Connettore M12 A-code, utilizzato per comunicare con i controller hopper ARS tramite protocollo <strong>Modbus RTU</strong>.
    </div>

    <details class="ars-dropdown"><summary>Pinout M12 A-code</summary><div class="ars-dropdown-body">

    | Pin | Colore |
    |---|---|
    | 1 | Marrone |
    | 2 | Bianco |
    | 3 | Blu |
    | 4 | Nero |
    | 5 | Grigio |

    </div></details>
  - 
    ```{image} ../../../../_shared/media/images/connectHopper.png
    :alt: Collegare l'Hopper
    :class: ars-zoom-img
    ```

* - 4
  - **Collegare l'alimentazione (Power Supply).**

    <div class="ars-step-attn">
    Assicurarsi che il FlexiBowl® sia <strong>spento</strong> prima di collegare l'alimentazione.
    </div>

    <div class="ars-step-warn">
    Tensione ammessa: <strong>120–230 Vac, 50/60 Hz</strong>.
    </div>

    <div class="ars-step-note">
    Al primo avvio, verificare lo stato dei fusibili. Dopo l'accensione, attendere che il LED di stato (Ready/Fault) si accenda: se Hopper e C-ETH sono collegati correttamente, il LED sarà <strong>verde</strong>.
    </div>

    <details class="ars-dropdown"><summary>Schema pinout cavo alimentazione</summary><div class="ars-dropdown-body">

    | Colore | Tipo | Etichetta |
    |---|---|---|
    | Marrone | Fase | L1 |
    | Blu | Neutro | N1 |
    | Giallo/Verde | Terra | PE1 |

    </div></details>
  - 
    ```{image} ../../../../_shared/media/images/connectSupply.png
    :alt: Collegare l'alimentazione
    :class: ars-zoom-img
    ```

* - 5
  - **Collegare l'aria compressa** con tubo **Ø 8 mm**.

    :::{note}
    Per le caratteristiche dell'aria richieste (pressione, classe di pulizia ISO) fare riferimento ai [Dati Tecnici Pneumatici](datipneum).
    :::
  - 
    ```{image} ../../../../_shared/media/images/connectAir.png
    :alt: Collegare l'aria compressa Ø8mm
    :class: ars-zoom-img
    ```
```

---

## FlexiBowl® 200 / 350 — Rack Esterno

Per queste taglie, i collegamenti verso gli impianti del cliente si trovano sul **rack** esterno (non sulla macchina). Il rack va poi collegato alla macchina tramite 4 cavi dedicati.

### Collegamenti sul rack

I connettori del rack sono gli stessi del pannello standard (stessa piedinatura), semplicemente posizionati su un box esterno anziché sulla macchina.

```{list-table}
:header-rows: 1

* - #
  - Azione

* - 1
  - **Collegare lo STO** sul rack — stesso connettore a 10 pin del pannello standard (vedi tabella pinout sopra).

* - 2
  - **Collegare il C-ETH IN** sul rack — stesso connettore M12 D-code del pannello standard. Vale la stessa regola: collegamento obbligatorio, altrimenti la macchina va in ERROR.

* - 3
  - **Collegare l'Hopper** sul rack — stesso connettore M12 A-code (Modbus RTU) del pannello standard.

* - 4
  - **Collegare l'alimentazione** sul rack — 120–230 Vac.

    <div class="ars-step-attn">
    Assicurarsi che il FlexiBowl® sia <strong>spento</strong> prima di collegare l'alimentazione.
    </div>
```

### Collegamento tra Rack e FlexiBowl®

Il rack comunica con il FlexiBowl® tramite 4 cavi dedicati, ciascuno da collegare **esclusivamente** alla porta con l'etichetta corrispondente sul pannello.

:::{attention}
Collegare ogni cavo alla porta con l'**etichetta corrispondente** (es. MOTOR ↔ MOTOR, C-A SIGNAL ↔ C-A SIGNAL). Un collegamento incrociato può danneggiare il sistema.
:::

```{list-table}
:widths: 8 52 40
:header-rows: 1

* - #
  - Azione
  - Immagine
* - 5
  - **Collegare il cavo Ethernet (C-ETH FB)** tra Rack e FlexiBowl® — connettore M12 D-code.
  - 
    ```{image} ../../../../_shared/media/images/connectEthernet200.png
    :width: 110%
    :alt: Collegare il cavo C-ETH FB
    :class: ars-zoom-img
    ```
* - 6
  - **Collegare il cavo MOTOR.**

    <div class="ars-step-note">
    Connettore a 9 poli: veicola sia l'alimentazione del motore sia i segnali <strong>STO</strong> verso il FlexiBowl® (sul rack, STO e Motore sono connettori separati; sul cavo verso la macchina sono combinati in un unico connettore a 9 poli).
    </div>
  - 
    ```{image} ../../../../_shared/media/images/connectMotor.png
    :width:110%
    :alt: Collegare il cavo Motor
    :class: ars-zoom-img
    ```
* - 7
  - **Collegare il cavo C-A SIGNAL** — connettore a 19 poli per i segnali analogici.
  - 
    ```{image} ../../../../_shared/media/images/connectASignal.png
    :width:110%
    :alt: Collegare il cavo C-A Signal
    :class: ars-zoom-img
    ```
* - 8
  - **Collegare il cavo C-B SIGNAL** — connettore a 19 poli per i segnali digitali.
  - 
    ```{image} ../../../../_shared/media/images/connectBSignal.png
    :width:110%
    :alt: Collegare il cavo C-B Signal
    :class: ars-zoom-img
    ```
* - 9
  - **Collegare l'aria compressa** con tubo **Ø 6 mm**, direttamente sul pannello della macchina.

    :::{note}
    Per le caratteristiche dell'aria richieste (pressione, classe di pulizia ISO) fare riferimento ai [Dati Tecnici Pneumatici](datipneum).
    :::
  - 
    ```{image} ../../../../_shared/media/images/connectAir200.png
    :width:110%
    :alt: Collegare l'aria compressa Ø6mm
    :class: ars-zoom-img
    ```
```
