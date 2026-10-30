# **Home**

Die neue FlexiBowl®-Oberfläche ist vollständig webbasiert. Für den Zugriff genügt es, die Standard-IP-Adresse des FlexiBowl® `192.168.1.10` in die Adressleiste Ihres Browsers einzugeben.

## Übersicht

Die Seite **Home** ist der Hauptbildschirm der FlexiBowl®-Software-Oberfläche. Sie wird beim Systemstart angezeigt und gibt dem Bediener einen sofortigen Überblick über den Gerätezustand sowie Zugriff auf die wichtigsten Funktionen.
![Startseite](../../../../_shared/media/images/home.png)

| Element | Position | Beschreibung |
|---|---|---|
| **Menü** (☰) | Oben links | Öffnet das seitliche Hauptnavigationsmenü, über das alle Bereiche der Software erreichbar sind (Parameter, Diagnose, Verlauf, Einstellungen usw.) |
| **Statussymbol** (READY ✓) | Mitte links | Zeigt den aktuellen Betriebszustand des Systems an. Das grüne Symbol mit Häkchen und der Schriftzug **READY** signalisieren, dass das System betriebsbereit ist |
| **Benutzersymbol** | Mitte rechts | Ermöglicht die Verwaltung des aktiven Benutzerprofils (Anmelden, Abmelden, Benutzerwechsel) |
| **Pulsante ENABLE MOTOR** | Oben rechts | Aktiviert den Motor des FlexiBowl®. |
| **Sprachauswahl** | Unterhalb von ENABLE MOTOR | Dropdown-Menü zur Auswahl der Sprache der Oberfläche. Es zeigt die Flagge der aktiven Sprache an (z. B. 🇺🇸 English) |

---

## Menü

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

Das Seitenmenü, das über das Symbol ☰ aufgerufen werden kann, gibt Zugriff auf alle Seiten der Oberfläche:

<div class="home-menu-wrap">
<div class="home-menu-img">

```{image} ../../../../_shared/media/images/menu_laterale.png
:alt: Seitliches Navigationsmenü
```

</div>
<div class="home-menu-cards">

<a class="home-menu-card" href="04_home.html">
<div class="home-menu-card-title">Home</div>
<div class="home-menu-card-sub">Hauptbildschirm mit Systemstatus und Schnellzugriff auf die Funktionen</div>
</a>

<a class="home-menu-card" href="04b_maincommand.html">
<div class="home-menu-card-title">Main Command</div>
<div class="home-menu-card-sub">Konfiguriert die allgemeinen Optionen der Einheit sowie die Bewegungen Move und Shake (Tabs Option, Move, Shake)</div>
</a>

<a class="home-menu-card" href="04c_sequence.html">
<div class="home-menu-card-title">Sequence</div>
<div class="home-menu-card-sub">Erstellt und bearbeitet Zuführsequenzen direkt über die Oberfläche</div>
</a>

<a class="home-menu-card" href="04d_monitor.html">
<div class="home-menu-card-title">Monitor</div>
<div class="home-menu-card-sub">Echtzeitansicht des FlexiBowl®-Zustands mit zeitgestempeltem Ereignisprotokoll</div>
</a>

<a class="home-menu-card" href="04e_jogmotor.html">
<div class="home-menu-card-title">Jog Motor</div>
<div class="home-menu-card-sub">Manuelle Motorbewegung, nützlich bei Einrichtung, Test oder Fehlersuche</div>
</a>

<a class="home-menu-card" href="04f_wizard.html">
<div class="home-menu-card-title">Wizard Param</div>
<div class="home-menu-card-sub">Schrittweise geführtes Verfahren zur Konfiguration des FlexiBowl®</div>
</a>

<a class="home-menu-card" href="manual.html">
<div class="home-menu-card-title">Manual</div>
<div class="home-menu-card-sub">Ermöglicht den Zugriff auf die Dokumentation des Geräts direkt über die Oberfläche</div>
</a>

<a class="home-menu-card" href="04h_graphs.html">
<div class="home-menu-card-title">Graphs</div>
<div class="home-menu-card-sub">Dashboard mit Echtzeitdiagrammen der elektrischen und thermischen Größen des Motortreibers</div>
</a>

<a class="home-menu-card" href="04i_filetransfer.html">
<div class="home-menu-card-title">File Transfer</div>
<div class="home-menu-card-sub">Übertragung von Parametern und Rezepten von und zu Sicherungen der Einheit</div>
</a>

<a class="home-menu-card" href="04l_setup.html">
<div class="home-menu-card-title">Setup</div>
<div class="home-menu-card-sub">Netzwerkkonfiguration, Auswahl des Kommunikationsprotokolls und weitere Systemeinstellungen</div>
</a>

<a class="home-menu-card" href="04m_hopper.html">
<div class="home-menu-card-title">Hopper</div>
<div class="home-menu-card-sub">Konfiguration und Steuerung der angeschlossenen Bulk Feeder (ID, Amplitude, Frequenz, Aktivierungszeit)</div>
</a>

<a class="home-menu-card" href="04n_emptying.html">
<div class="home-menu-card-title">Emptying</div>
<div class="home-menu-card-sub">Automatisches Entleeren des Tellers durch Verketten von bis zu 4 Sequenzen mit konfigurierbaren Schleifen</div>
</a>

</div>
</div>



---
## Betriebshinweise

:::{attention}   
Vor der Aktivierung des Motors prüfen, ob der Systemzustand **READY** ist (grünes Symbol in der oberen Leiste sichtbar). Ist das Symbol nicht grün, die Fehlermeldungen in den Diagnosebereichen prüfen.
:::

:::{note}  
Die auf der Startseite gewählte Sprache wird auf die gesamte Software-Oberfläche angewendet. Die Änderung erfolgt sofort und erfordert keinen Neustart des Systems.
:::
