# [SOF] **Home**

## Panoramica

La pagina **Home** è la schermata principale dell'interfaccia software FlexiBowl®. Viene visualizzata all'avvio del sistema e fornisce all'operatore una panoramica immediata dello stato del dispositivo, oltre a consentire l'accesso alle funzioni principali.
![pagina home](../../../../_shared/media/images/home.png)

| Elemento | Posizione | Descrizione |
|---|---|---|
| **Menu** (☰) | In alto a sinistra | Apre il menu laterale di navigazione principale, che consente di accedere a tutte le sezioni del software (parametri, diagnostica, storico, impostazioni, ecc.) |
| **Icona di stato** (READY ✓) | Centro-sinistra | Indica lo stato operativo corrente del sistema. L'icona verde con la spunta e la scritta **READY** segnala che il sistema è pronto per l'operazione |
| **Icona utente** | Centro-destra | Consente di gestire il profilo utente attivo (login, logout, cambio utente) |
| **Pulsante ENABLE MOTOR** | In alto a destra | Abilita il motore del FlexiBowl®. |
| **Selettore lingua** | Sotto ENABLE MOTOR | Menu a tendina per selezionare la lingua dell'interfaccia. Mostra la bandiera della lingua attiva (es. 🇺🇸 English) |

---

## Menù

<style>
.home-menu-wrap {
  display: flex;
  gap: 1.5rem;
  align-items: flex-start;
  margin: 1rem 0 1.5rem;
  flex-wrap: wrap;
}
.home-menu-img {
  flex: 0 0 auto;
  width: 200px;
  border: 1px solid #e2eef6;
  border-radius: 10px;
  overflow: hidden;
}
.home-menu-img img { display: block; width: 100%; }
.home-menu-cards {
  flex: 1 1 420px;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0.75rem;
}
@media (max-width: 560px) {
  .home-menu-cards { grid-template-columns: 1fr; }
}
.home-menu-card {
  display: block;
  padding: 0.7rem 0.9rem;
  border: 1.5px solid #d0e4f0;
  border-radius: 8px;
  background: #fff;
  text-decoration: none;
  color: inherit;
  transition: border-color 0.18s, background 0.18s;
}
.home-menu-card:hover {
  border-color: #2980b9;
  background: #f0f7ff;
  text-decoration: none;
}
.home-menu-card-title {
  font-weight: 700;
  font-size: 0.88rem;
  color: #1a3a52;
}
.home-menu-card-sub {
  font-size: 0.78rem;
  color: #556b7d;
  margin-top: 0.2rem;
  line-height: 1.35;
}
</style>

Il menu laterale, richiamabile dall'icona ☰, dà accesso a tutte le pagine dell'interfaccia:

<div class="home-menu-wrap">
<div class="home-menu-img">

```{image} ../../../../_shared/media/images/menu_laterale.png
:alt: Menu laterale di navigazione
```

</div>
<div class="home-menu-cards">

<a class="home-menu-card" href="04_home.html">
<div class="home-menu-card-title">Home</div>
<div class="home-menu-card-sub">Schermata principale con stato del sistema e accesso rapido alle funzioni</div>
</a>

<a class="home-menu-card" href="04b_maincommand.html">
<div class="home-menu-card-title">Main Command</div>
<div class="home-menu-card-sub">Configura le opzioni generali dell'unità e i movimenti Move e Shake (tab Option, Move, Shake)</div>
</a>

<a class="home-menu-card" href="04c_sequence.html">
<div class="home-menu-card-title">Sequence</div>
<div class="home-menu-card-sub">Crea e modifica le sequenze di alimentazione direttamente dall'interfaccia</div>
</a>

<a class="home-menu-card" href="04d_monitor.html">
<div class="home-menu-card-title">Monitor</div>
<div class="home-menu-card-sub">Vista in tempo reale dello stato del FlexiBowl®, con log eventi con marcatura temporale</div>
</a>

<a class="home-menu-card" href="04e_jogmotor.html">
<div class="home-menu-card-title">Jog Motor</div>
<div class="home-menu-card-sub">Movimentazione manuale del motore, utile in fase di setup, test o troubleshooting</div>
</a>

<a class="home-menu-card" href="04f_wizard.html">
<div class="home-menu-card-title">Wizard Param</div>
<div class="home-menu-card-sub">Procedura guidata passo-passo per la configurazione del FlexiBowl®</div>
</a>

<a class="home-menu-card" href="manual.html">
<div class="home-menu-card-title">Manual</div>
<div class="home-menu-card-sub">Consente di consultare la documentazione del dispositivo direttamente dall'interfaccia</div>
</a>

<a class="home-menu-card" href="04h_graphs.html">
<div class="home-menu-card-title">Graphs</div>
<div class="home-menu-card-sub">Dashboard con i grafici in tempo reale delle grandezze elettriche e termiche del driver motore</div>
</a>

<a class="home-menu-card" href="04i_filetransfer.html">
<div class="home-menu-card-title">File Transfer</div>
<div class="home-menu-card-sub">Trasferimento di parametri e ricette da e verso backup dell'unità</div>
</a>

<a class="home-menu-card" href="04l_setup.html">
<div class="home-menu-card-title">Setup</div>
<div class="home-menu-card-sub">Configurazione di rete, selezione del protocollo di comunicazione e altre impostazioni di sistema</div>
</a>

<a class="home-menu-card" href="04m_hopper.html">
<div class="home-menu-card-title">Hopper</div>
<div class="home-menu-card-sub">Configurazione e controllo delle tramogge collegate (ID, ampiezza, frequenza, tempo di attivazione)</div>
</a>

<a class="home-menu-card" href="04n_emptying.html">
<div class="home-menu-card-title">Emptying</div>
<div class="home-menu-card-sub">Svuotamento automatico del piatto concatenando fino a 4 sequenze con loop configurabili</div>
</a>

</div>
</div>



---
## Note operative

:::{attention}   
Prima di abilitare il motore, verificare che lo stato del sistema sia **READY** (icona verde visibile nella barra superiore). Se l'icona non è verde, controllare i messaggi di errore nelle sezioni di diagnostica.
:::

:::{note}  
La lingua selezionata dalla Home viene applicata a tutta l'interfaccia software. La modifica è immediata e non richiede il riavvio del sistema.
:::
