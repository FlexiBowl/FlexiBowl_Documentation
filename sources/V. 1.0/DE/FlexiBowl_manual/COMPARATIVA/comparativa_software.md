<style>
.compare-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  margin: 1rem 0 1.5rem;
}
@media (max-width: 680px) {
  .compare-grid { grid-template-columns: 1fr; }
}
.compare-card {
  border: 1px solid #5a9fd4;
  border-radius: 7px;
  overflow: hidden;
  font-size: 0.92rem;
}
.compare-card-header {
  padding: 0.5rem 1rem;
  font-weight: 700;
  font-size: 0.82rem;
  letter-spacing: 0.05em;
  color: #ffffff;
}
.v20 .compare-card-header { background: #1a4a7a; }
.v30 .compare-card-header { background: #1e6fbf; }
.compare-card-body {
  padding: 0.85rem 1rem;
}
.compare-card-body p, .compare-card-body li { margin: 0.25rem 0; }
.compare-card-body ul, .compare-card-body ol { padding-left: 1.2rem; margin: 0.4rem 0; }
.compare-card-body table {
  width: 100%;
  border-collapse: collapse;
  margin: 0.5rem 0;
  font-size: 0.88rem;
}
.compare-card-body table th {
  padding: 0.35rem 0.6rem;
  text-align: left;
  font-size: 0.78rem;
  font-weight: 700;
  border-bottom: 2px solid #5a9fd4;
  opacity: 0.75;
}
.compare-card-body table td {
  padding: 0.35rem 0.6rem;
  border-bottom: 1px solid rgba(90, 159, 212, 0.3);
}
.compare-card-body table tr:last-child td { border-bottom: none; }
.compare-card-body pre {
  border: 1px solid rgba(90, 159, 212, 0.4);
  border-radius: 5px;
  padding: 0.7rem 0.9rem;
  font-size: 0.8rem;
  overflow-x: auto;
  margin: 0.5rem 0 0;
}
</style>
 
# **Software-Vergleich**
 
Diese Seite vergleicht die wichtigsten Software-Unterschiede zwischen **FlexiBowl® 2.0** und **FlexiBowl® 3.0**, um dem Benutzer das Verständnis der neuen Funktionen und der betrieblichen Änderungen der neuen Generation zu erleichtern.
 
:::{important}
Bevor Sie den Inhalt dieser Seite lesen, empfiehlt es sich, die Informationen auf der Seite [Software-Schnittstelle](int_software) zu kennen
:::
---
 
## 1. Verfügbare Kommunikationsprotokolle
 
| Protokoll | FlexiBowl® 2.0 | FlexiBowl® 3.0 |
|---|---|---|
| TCP/IP – UDP | ✓ | ✓ (TCP Server) |
| EtherNet/IP | ✓ | ✓ |
| Profinet | ✗ | ✓ |
| Modbus | ✗ | ✓ |
| Digital I/O | ✓ | ✓ (optional) |
 
---
 
## 2. Benutzeroberfläche: Aufbau und Zugriff
 
<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0 — Software Parameters</div>
<div class="compare-card-body">
 
**Desktop**-Oberfläche namens **FlexiBowl® Parameters**, die auf dem Steuerungs-PC zu installieren ist.
 
**Installation und Zugriff:**
 
1. Das Programm **FlexiBowl® Parameters** auf dem PC installieren (von ARS bereitgestellt).
2. Den PC über ein **Ethernet-Kabel** mit dem FlexiBowl® verbinden (direktes LAN oder über einen Switch).
3. Das Programm starten und die **IP-Adresse** des FlexiBowl® eingeben, um die Verbindung herzustellen.
 
Über den Bildschirm **Main Commands** sind die Bereiche **Move**, **Shake** und **Option** über Tabs im oberen Bereich erreichbar.
 
</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0 — Weboberfläche</div>
<div class="compare-card-body">
 
**Vollständig webbasierte** Oberfläche: Es ist keine Installation erforderlich. Ein moderner Browser genügt.
 
**Zugriff:**
 
1. Den PC über Ethernet mit dem FlexiBowl® verbinden.
2. Den Browser öffnen und die **IP-Adresse** des FlexiBowl® in die Adressleiste eingeben.
3. Die **Startseite** der Oberfläche wird geöffnet.
 
**Aufbau der Oberfläche:**
 
Das Seitenmenü enthält Seiten für jede Betriebsfunktion (Main Command, Jog Motor, Setup, Monitor usw.), die direkt im Browser aufgerufen werden können.
 
</div>
</div>
</div>
 
:::{note}
Wenn das verwendete System **FlexiVision One** ist, wird die Konfiguration über die zugehörige Oberfläche verwaltet. Die in diesem Abschnitt beschriebene Software-Oberfläche des FlexiBowl® muss nicht verwendet werden.
:::
 
---
 
## 3. So ändern Sie die IP-Adresse
 
<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0</div>
<div class="compare-card-body">
 
1. Das auf dem USB-Stick mitgelieferte Programm verwenden.
2. Den FlexiBowl® über ein Ethernet-Kabel verbinden.
3. Das Gerät einschalten.
4. Das Programm starten.
5. Im Feld **IP Address** die Adresse eingeben: `192.168.1.10`
   *(Der angeschlossene PC muss sich in derselben Subnetzmaske der Klasse B befinden — 255.255.0.0)*
6. **Ping** drücken → Pop-up **„FlexiBowl® found“**.
7. **Ok** drücken, um **CONNECT** zu aktivieren und die Verbindung herzustellen.
8. Nach dem Verbinden wird der Startbildschirm angezeigt.
 
</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0</div>
<div class="compare-card-body">
 
1. Den Browser öffnen und über die aktuelle IP auf die Oberfläche zugreifen.
2. Im Seitenmenü die Seite **Setup** öffnen.
3. Auf **Get IP** klicken, um die aktuellen Netzwerkparameter auszulesen.
4. Die neue IP-Adresse in die dafür vorgesehenen Felder eingeben und auf **Set IP** klicken.
5. Auf **Apply** klicken, um zu bestätigen, dann auf **Reboot**, damit die Änderungen wirksam werden.
 
</div>
</div>
</div>
 
:::{note}
**FlexiBowl® 2.0** — Ist eine frühere Version des Programms installiert, muss diese zuvor deinstalliert werden.
:::
 
:::{important}
**FlexiBowl® 3.0** — Nach dem Neustart wieder mit dem FlexiBowl® verbinden und dabei die neu eingestellte IP-Adresse verwenden.
:::
 
---
 
## 4. So verwalten Sie die Bewegungen
 
<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0</div>
<div class="compare-card-body">
 
Die Bewegungen werden über **Main Commands** konfiguriert und getestet, mit drei Bereichen:
 
- **Move**: stellt Acceleration, Deceleration, Speed und Angle per Schieberegler oder Zahlenfeld ein. **Test Move** führt die Bewegung mit den eingestellten Werten aus.
- **Shake**: Parameter CCW Angle, CW Angle, Count, Acceleration, Deceleration und Speed. **Test Shake** führt den Shake aus.
- **Try Commands**: kombiniert mehrere Befehle zu einer Sequenz mit konfigurierbarer Schleife, indem sie aus **All Commands** ausgewählt und zu **Selected Commands** hinzugefügt werden.
 
Für den Produktivbetrieb über Protokoll werden ASCII-Befehle (z. B. `QX2` für Move, `QX6` für Shake) über den konfigurierten TCP/UDP-Kanal gesendet.
 
</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0</div>
<div class="compare-card-body">
 
Die Bewegungen sind in **Sequenzen** (bis zu 20) organisiert, die auf der Seite **Main Command** konfiguriert werden können. Jede Sequenz enthält bis zu 10 Befehlsplätze (Move, Shake, Flip, Blow).
 
Auf der Seite **Main Command** ist Folgendes möglich:
 
- Die Sequenz über **Select the sequence** auswählen.
- Alle Parameter in den Zahlenfeldern einstellen.
- Befehle mit **Command Available** + **ADD** hinzufügen; mit **UP/DOWN** neu anordnen; mit **DELETE** entfernen oder mit **CLEAR** die Liste leeren.
- Mit **TEST SEQUENCE** testen oder mit **RUN** in den Produktivbetrieb starten.
 
Die Seite **Jog Motor** ermöglicht kontinuierliche Rotation (positive Speed = im Uhrzeigersinn, negativ = gegen den Uhrzeigersinn) mit integriertem Flip und Blow.
 
Für den Produktivbetrieb über Protokoll: `10[0]%` für Sequenz 1 über TCP oder ControlWord `10` über EtherNet/IP oder Profinet.
 
</div>
</div>
</div>
 
---
 
## 5. So ändern Sie die Parameter
 
<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0</div>
<div class="compare-card-body">
 
Die Betriebsparameter werden auf zwei Arten geändert:
 
- **Grafische Oberfläche**: Schieberegler oder Zahlenfelder in den Bildschirmen Move und Shake von **Main Commands**.
- **Über Protokoll (Laufzeit)**: Befehle `RW` (Write) und `RL` (Read) über TCP/UDP. Die Werte müssen mit dem **Untersetzungsfaktor** der Maschine multipliziert werden (mit dem Befehl `RR114` ermittelt), da die Parameter in internen Treibereinheiten angegeben sind.
 
</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0</div>
<div class="compare-card-body">
 
Die Parameter werden auf drei Arten geändert:
 
- **Weboberfläche**: direkt in den Zahlenfeldern der Seite **Main Command** für jede Sequenz.
- **Über WRITE-Protokoll**: ControlWord-Block WRITE mit der Formel `N × 100 + offset_parametro`
- **Über READ-Protokoll**: ControlWord-Block READ mit der Formel `10000 + N × 100 + offset_parametro`
 
</div>
</div>
</div>
 
---
 
### Praxisbeispiel: Move + Shake am FlexiBowl® 800
 
Das Szenario lautet wie folgt: einen **Move** von 360° ausführen, dann einen **Shake**, dann eine Wartezeit von 200 ms.
 
<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0 — TCP-Befehlssequenz</div>
<div class="compare-card-body">
 
Die Parameter müssen mit dem **Untersetzungsfaktor** der Maschine skaliert werden:
 
<pre>QX7                     → Backlight einschalten
RR114                   → Untersetzungsfaktor lesen
reduction_factor = RX 1
 
RL1 (50 × reduction_factor), RW11   → Acceleration Move = 50 %
RL1 (50 × reduction_factor), RW12   → Deceleration Move = 50 %
RL1 (35 × reduction_factor), RW13   → Speed Move = 35 %
RL1 (360 × reduction_factor), RW14  → Angle Move = 360°
QX2                     → Move ausführen
 
RL1 (50 × reduction_factor), RW15  → Acceleration Shake = 50 %
RL1 (50 × reduction_factor), RW16  → Deceleration Shake = 50 %
RL1 (50 × reduction_factor), RW110 → Speed Shake = 50 %
RL1 (30 × reduction_factor), RW18  → Angle CW Shake = -30°
RL1 (30 × reduction_factor), RW19  → Angle CCW Shake = -45°
RL1 2, RW17                           → Count Shake = 2
QX6                     → Shake ausführen</pre>
 
Die Wartezeit von 200 ms wird vom aufrufenden System (Roboter oder SPS) verwaltet.
 
</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0 — Konfiguration der Weboberfläche</div>
<div class="compare-card-body">
 
Auf der Seite **Main Command** **SEQUENCE 1** auswählen und einstellen:
 
| Parameter | Wert |
|---|---|
| Acceleration Move | 50 % |
| Deceleration Move | 50 % |
| Speed Move | 35 % |
| Angle Move | 360° |
| Acceleration Shake | 50 % |
| Deceleration Shake | 50 % |
| Speed Shake | 50 % |
| Ccw Angle Shake | −45° |
| Cw Angle Shake | −30° |
| Count Shake | 2 |
 
Zur Liste hinzufügen: `FLB_MOVE` → `FLB_SHAKE`. Backlight auf der Seite **Option** prüfen. Die Wartezeit von 200 ms wird durch Hinzufügen von `FLB_WAIT` zur Liste oder auf Seiten des aufrufenden Systems verwaltet.
 
Um die Sequenz über TCP auszuführen:
 
<pre>10[0]%    → Sequenz 1 ausführen</pre>
 
Das System antwortet zur Bestätigung mit `10[0]`.
 
</div>
</div>
</div>
 
---
 
## 6. So lesen Sie Alarme
 
<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0</div>
<div class="compare-card-body">
 
Die Alarme werden unter **Monitor → Alarm Status** des Programms **FlexiBowl® Parameters** abgerufen. Der Bildschirm zeigt die Treiberzustände mit LED-Anzeigen (grün = OK, rot = Fehler). Der Bildschirm **Driver Status** zeigt in Echtzeit alle Betriebsvariablen.
 
Alarm-Reset über Protokoll:
 
<pre>Chr(0)Chr(7)QX12Chr(13)    → Alarm zurücksetzen und Motor wieder freigeben</pre>
 
</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0</div>
<div class="compare-card-body">
 
Die Alarme werden auf der Seite **Monitor** abgerufen (Tabs: **I/O Status**, **Driver Status**, **Alarm Status**).
 
Über das Protokoll wird das Alarmsignal durch **In_Error** (BOOL) und der aktive Code durch **ErrorCode** (UDINT) bereitgestellt:
 
<pre>InError%         → InError[1]% bei Fehler, InError[0]% wenn OK
ErrorCode%       → ErrorCode[N]% mit dem Code des aktiven Fehlers</pre>
 
Alarm-Reset:
- Über TCP-Protokoll: `Reset%`
- Über digitale Variable: steigende Flanke am Eingangssignal **Reset** (BOOL)
 
</div>
</div>
</div>
 
:::{warning}
Vor dem Zurücksetzen die Fehlerursache identifizieren und beheben. Das System führt keine neuen Bewegungsbefehle aus, solange ein aktiver Fehler vorliegt.
:::
 
:::{note}
Die vollständige Liste der Fehlercodes finden Sie im Abschnitt [Fehlercodes](sec-err)
:::
 
---
 
## 7. Tracking-Modus (FlexiTrack)
 
<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0</div>
<div class="compare-card-body">
 
Der Modus **FlexiTrack** ist eine separat erhältliche Option, mit der der FlexiBowl® in **kontinuierlicher Rotation** (Jog) gehalten werden kann, indem das Encodersignal mit dem Pick-Roboter synchronisiert wird.
 
**Erforderliche Hardware:**
 
- Anschluss an den **internen Encoder** über den Stecker des Bedienfelds (TTL-Quadratursignal, 4000 Impulse/Umdrehung am Motor; bei FlexiBowl® 500/650/800 mit Untersetzung 1:3 → 12000 Impulse/Umdrehung an der Scheibe).
- Alternativ **externer Encoder** (inkremental, TTL RS422, ≥ 12000 ppr) auf der mit der angetriebenen Riemenscheibe verbundenen Welle.
 
**Wichtigste FlexiTrack-Befehle (über TCP/UDP):**
 
| Befehl | Beschreibung |
|---|---|
| `JA<valore>` | Beschleunigung/Verzögerung in U/s² |
| `JL<valore>` | Verzögerung (falls abweichend von JA, nach JA senden) |
| `JS<valore>` | Drehgeschwindigkeit in U/s |
| `CC<valore>` | Dem Motor zugeführter Strom |
| `DI1` | Richtung im Uhrzeigersinn |
| `DI-1` | Richtung gegen den Uhrzeigersinn |
| `CJ` | Jog starten (kontinuierliche Rotation) |
| `SJ` | Jog stoppen (mit JL-Rampe) |
| `IL2` / `IH2` | Flip aktivieren / deaktivieren |
| `IL3` / `IH3` | Blow aktivieren / deaktivieren |
 
**Empfohlene Parameter:**
 
<pre>JA0.2    → Beschleunigung 0.2 U/s²
JL0.2    → Verzögerung 0.2 U/s²
JS0.2    → Geschwindigkeit 0.2 U/s
CC1.3    → Motorstrom
DI1      → Rotation im Uhrzeigersinn</pre>
 
Flip und Blow müssen über ein **Hintergrundprogramm** mit einer Iterationsschleife implementiert werden, die den Zustand der Ventile umschaltet.
 
</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0</div>
<div class="compare-card-body">
 
Der Jog-Modus ist **nativ** in die Seite **Jog Motor** integriert — ohne zusätzliche Hardware-Optionen.
 
**Jog-Bewegungsparameter:**
 
| Parameter | Einheit | Beschreibung |
|---|---|---|
| Acceleration | % | Beschleunigungsrampe beim Start |
| Deceleration | % | Verzögerungsrampe beim Stopp |
| Speed | % | Geschwindigkeit — positiv = im Uhrzeigersinn; negativ = gegen den Uhrzeigersinn |
 
**Zusatzfunktionen während des Jog:**
 
- **Flip Enable**: automatischer zyklischer Flip mit Flip Duration, Flip Pression, Flip Pause.
- **Blow Enable**: automatische zyklische Blasluft mit Blow Duration, Blow Pression, Blow Pause, Blow Type (BLOWc, BLOWe, BLOWc+BLOWe).
- **Backlight 1 / 2**: Umschalter der Hintergrundbeleuchtung, unabhängig vom Jog-Zustand.
 
**Start und Stopp:**
 
- **START JOG**: startet die kontinuierliche Rotation.
- **STOP JOG**: stoppt mit Verzögerungsrampe.
 
Steuerung über Protokoll:
 
<pre>40[0]%    → Start Jog Seq (via TCP)
41[0]%    → Stop Jog Seq (via TCP)</pre>
 
</div>
</div>
</div>
 
:::{important}
Vor dem Start des Jog sicherstellen, dass der Motor freigegeben ist (**ENABLE MOTOR** aktiv) und der Systemzustand **READY** lautet.
:::
 
:::{important}
Mit FlexiTrack **(FlexiBowl® 2.0)** ist die Bewegungssteuerung **nur über das Ethernet-Protokoll** (TCP/UDP) möglich. Das Digital-I/O-Protokoll wird nicht unterstützt.
:::