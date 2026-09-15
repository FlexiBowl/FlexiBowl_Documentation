(intpneum)=
# [ELE] **Interfaccia Pneumatica**

La macchina è dotata di azionamento pneumatico.
Prima di effettuare l'**allacciamento pneumatico** verificare che:
- l'impianto di fornitura di aria compressa presente, garantisca alla macchina la quantità di aria alla giusta pressione;
- il serbatoio dell'aria compressa predisposto sia correttamente dimensionato.

L'allacciamento pneumatico deve essere effettuato collegando la linea principale al circuito macchina.
Il cliente deve inoltre garantire un'alimentazione di aria con le caratteristiche elencate nel paragrafo {ref}`"Dati Tecnici Pneumatici" <datipneum>` di questo manuale.

:::{warning}
Non superare mai i 7 bar di pressione nell'impianto pneumatico della macchina.
:::

:::{warning}
Il FlexiBowl® è fornito senza dispositivo manuale di intercettazione e scarico dell'alimentazione pneumatica. L'integratore deve predisporre a monte un dispositivo chiaramente identificato, facilmente accessibile e bloccabile in posizione di chiusura, che consenta di interrompere l'alimentazione, scaricare la pressione residua e prevenire riattivazioni involontarie. Tubazioni e raccordi devono essere adeguati alla pressione di esercizio, correttamente fissati e protetti contro lo sfilamento. Eventuali ulteriori dispositivi pneumatici di sicurezza devono essere definiti mediante la valutazione dei rischi della macchina finale.
:::

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

* - **Manutentore meccanico**
  - :::{raw} html
       <div class="ars-img-row">
         <img src="../../../../_shared/media/images/guanti.png" alt="guanti">
         <img src="../../../../_shared/media/images/scarpe.png" alt="scarpe">
         <img src="../../../../_shared/media/images/tuta.png" alt="tuta">
       </div>
    :::
::::
:::::

Per l'allacciamento alla rete pneumatica, collegare un tubo dell'aria {ref}`della giusta misura <datipneum>` all'ingresso "Air Supply" presente nel {ref}`pannello comandi <intele>`.

:::{raw} html
<style>
.img-zoom-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 16px;
  padding: 1rem 0;
}
.img-zoom-wrap {
  flex: 1 1 0;
  min-width: 0;
  overflow: visible;
  display: flex;
  align-items: center;
  justify-content: center;
}
.img-zoom-wrap img {
  width: 100%;
  border-radius: 8px;
  transition: transform 0.35s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.35s ease;
  cursor: zoom-in;
  position: relative;
  transform: scale(1);
}
.img-zoom-wrap img:hover {
  transform: scale(1.85);
  box-shadow: 0 12px 40px rgba(0,0,0,0.22);
  z-index: 10;
}
</style>

<div class="img-zoom-grid">
  <div class="img-zoom-wrap">
    <img src="../../../../_shared/media/images/smallpanel5.PNG" alt="Pannello small" />
  </div>
  <div class="img-zoom-wrap">
    <img src="../../../../_shared/media/images/stpanel2.PNG" alt="Pannello ST" />
  </div>
  <div class="img-zoom-wrap">
    <img src="../../../../_shared/media/images/encpanel7.PNG" alt="Pannello ENC" />
  </div>
</div>
:::

<style>
.ars-dropdown {
  margin: 0.9rem 0 0.4rem 0;
  border: 2px solid #7fb3dd;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 6px rgba(26,111,196,0.10);
}
.ars-dropdown summary {
  cursor: pointer;
  color: #2980b9;
  font-weight: 600;
  font-size: 0.83rem;
  padding: 0.5rem 0.9rem;
  display: block;
  background: #eaf3fb;
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
  border-bottom: 2px solid #7fb3dd;
}
.ars-dropdown .ars-dropdown-body {
  padding: 0.9rem 1rem;
  background: #fff;
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

---

## Caratteristiche Aria Richieste

| Parametro | Valore |
|---|---|
| Qualità aria | Aria compressa pulita e secca, secondo **ISO 8573-1:2010, classe 1.3.2** |
| Pressione di alimentazione consigliata | **7 bar** (da non superare mai) |
| Diametro tubo — FB200 / FB350 | **Ø 6 mm** |
| Diametro tubo — FB500E / FB500 / FB650 / FB800 / FB1200 | **Ø 8 mm** |

<details class="ars-dropdown"><summary>Consumo aria indicativo per modello (azione Flip)</summary><div class="ars-dropdown-body">

| Modello | Consumo medio | Consumo di picco |
|---|---|---|
| FB200 | 25 l/min | 45 l/min |
| FB350 | 15 l/min | 24 l/min |
| FB500E | 55 l/min | 74 l/min |
| FB500 | 35 l/min | 48 l/min |
| FB650 | 30 l/min | 45 l/min |
| FB800 | 45 l/min | 60 l/min |
| FB1200 | 135 l/min | 176 l/min |

I valori riportati si riferiscono alla sola azione di Flip; per i dettagli completi sui consumi fare riferimento al paragrafo {ref}`"Dati Tecnici Pneumatici" <datipneum>`.

</div></details>

:::{note}
Su FlexiBowl® 3.0 la regolazione della pressione e la lettura del manometro avvengono tramite **interfaccia software**, e non più con regolatore e manometro fisici sul pannello come nella precedente generazione 2.0.
:::

---

## Procedura Guidata — Collegamento Pneumatico

Anche per l'allacciamento pneumatico la procedura cambia leggermente in base alla taglia della macchina, in particolare per il diametro del tubo e la posizione del connettore **AIR SUPPLY**.

:::{attention}
Prima di iniziare qualsiasi collegamento pneumatico, assicurarsi che l'alimentazione dell'aria compressa sia **disinserita** e che la pressione residua nel circuito sia stata **scaricata**.
:::

### FlexiBowl® 500 – 1200 — Pannello Elettrico Standard

```{list-table}
:widths: 8 52 40
:header-rows: 1

* - #
  - Azione
  - Immagine
* - 1
  - **Verifiche preliminari.**

    Controllare che l'impianto di fornitura garantisca la pressione e la portata richieste, e che il serbatoio di aria compressa sia correttamente dimensionato per il modello installato.

    <div class="ars-step-note">
    Aria pulita e secca secondo ISO 8573-1:2010, classe 1.3.2. Pressione consigliata: 7 bar.
    </div>
  -

* - 2
  - **Disinserire l'alimentazione dell'aria** a monte dell'impianto, prima di collegare il tubo.

    <div class="ars-step-attn">
    Non collegare o scollegare mai il tubo aria con l'impianto ancora in pressione.
    </div>
  -

* - 3
  - **Collegare il tubo dell'aria** all'ingresso **AIR SUPPLY** sul pannello elettrico standard, utilizzando un tubo con diametro esterno **Ø 8 mm**.
  -
    ```{image} ../../../../_shared/media/images/connectAir.png
    :alt: Collegare l'aria compressa Ø8mm
    :class: ars-zoom-img
    ```

* - 4
  - **Verificare la tenuta del collegamento**: controllare che il raccordo sia correttamente inserito e che non vi siano perdite udibili o percepibili al tatto lungo il tubo e il raccordo.
  -

* - 5
  - **Ripristinare l'alimentazione dell'aria** e verificare che la pressione a valle rientri nei parametri previsti.

    <div class="ars-step-note">
    Su FlexiBowl® 3.0 la pressione può essere letta e regolata direttamente da interfaccia software.
    </div>
  -
```

### FlexiBowl® 200 / 350

Su queste taglie, il connettore **AIR SUPPLY** si trova direttamente sul pannello della macchina (non sul rack esterno), a valle di tutti gli altri cablaggi.

```{list-table}
:widths: 8 52 40
:header-rows: 1

* - #
  - Azione
  - Immagine
* - 1
  - **Verifiche preliminari.**

    Controllare che l'impianto di fornitura garantisca la pressione e la portata richieste, e che il serbatoio di aria compressa sia correttamente dimensionato per il modello installato.

    <div class="ars-step-note">
    Aria pulita e secca secondo ISO 8573-1:2010, classe 1.3.2. Pressione consigliata: 7 bar.
    </div>
  -

* - 2
  - **Disinserire l'alimentazione dell'aria** a monte dell'impianto, prima di collegare il tubo.

    <div class="ars-step-attn">
    Non collegare o scollegare mai il tubo aria con l'impianto ancora in pressione.
    </div>
  -

* - 3
  - **Collegare il tubo dell'aria** direttamente sul pannello della macchina, utilizzando un tubo con diametro esterno **Ø 6 mm**.
  -
    ```{image} ../../../../_shared/media/images/connectAir200.png
    :width: 110%
    :alt: Collegare l'aria compressa Ø6mm
    :class: ars-zoom-img
    ```

* - 4
  - **Verificare la tenuta del collegamento**: controllare che il raccordo sia correttamente inserito e che non vi siano perdite udibili o percepibili al tatto lungo il tubo e il raccordo.
  -

* - 5
  - **Ripristinare l'alimentazione dell'aria** e verificare che la pressione a valle rientri nei parametri previsti.

    <div class="ars-step-note">
    Su FlexiBowl® 3.0 la pressione può essere letta e regolata direttamente da interfaccia software.
    </div>
  -
```

---

## Note e Avvertenze Generali

:::{attention}
Tutte le operazioni di collegamento e scollegamento pneumatico devono essere eseguite con impianto **disinserito** e **pressione residua scaricata**.
:::

:::{attention}
Non superare mai i **7 bar** di pressione nell'impianto pneumatico della macchina.
:::

:::{attention}
Il FlexiBowl® non è dotato di dispositivo manuale di intercettazione e scarico: è responsabilità dell'integratore predisporne uno a monte, chiaramente identificato, accessibile e bloccabile in posizione di chiusura.
:::

:::{attention}
Utilizzare esclusivamente tubi e raccordi adeguati alla pressione di esercizio, correttamente fissati e protetti contro lo sfilamento.
:::

:::{attention}
Per ulteriori informazioni tecniche o assistenza, contattare ARS s.r.l. – FlexiBowl® Division.
:::
