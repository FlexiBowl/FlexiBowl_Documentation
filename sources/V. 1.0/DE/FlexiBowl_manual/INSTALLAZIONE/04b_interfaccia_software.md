(tcp)=
# **TCP Server**

Bei Verwendung der **TCP-Server**-Kommunikation werden die Befehle nicht als binäre Variablen, sondern als **Textzeichenfolgen** über eine Socket-Verbindung auf dem konfigurierten Port (Standard: 8123) gesendet.


Jede Nachricht hat folgende Form:

```
NomeVariabile[Valore]%
```

Das Zeichen `%` ist der **Nachrichtenabschluss** und muss am Ende immer vorhanden sein. Das Feld `[Valore]` enthält die zugehörigen numerischen Daten (ControlWord, Status usw.).

## TCP-Syntaxtabelle

| Vorgang | Zu sendende Nachricht | Antwort bei OK | Antwort bei Fehler |
|---|---|---|---|
| Alle EXE-Befehle | `10[0]%` | `10[0]%` | `1[0]%` |
| Alle WRITE-Befehle | `100[56]%` | `100[0]%` | `2[0]%` |
| Alle READ-Befehle | `10100[0]%` | `10100[valore]%` | `2[0]%` |
| Fehler-Reset | `Reset%` | `Reset%` | — |
| Busy-Status lesen | `Busy%` | `Busy[1]%` | `Busy[0]%` |
| Ready-Status lesen | `Ready%` | `Ready[1]%` | `Ready[0]%` |
| InError-Status lesen | `InError%` | `InError[1]%` | `InError[0]%` |
| InPowerOn-Status lesen | `InPowerOn%` | `InPowerOn[1]%` | `InPowerOn[0]%` |
| ErrorCode lesen | `ErrorCode%` | `ErrorCode[56]%` | `ErrorCode[0]%` |

:::{note}
Bei Antworten vom Typ READ wird der Text `[valore]` durch den tatsächlich vom System gelesenen numerischen Wert ersetzt. Um z. B. die Geschwindigkeit von SEQ 1 (ControlWord 10102) zu lesen, wird `10102[0]%` gesendet und `10102[35]%` empfangen, wenn die Geschwindigkeit auf 35 % eingestellt ist.
:::

:::{warning}
Hopper-Befehle über TCP (`Hopper1Start%` usw.) funktionieren **nur, wenn die Kommunikation aktiv ist und sich der FlexiBowl® nicht bewegt**. Der korrekte Betrieb ist nicht gewährleistet, wenn der FlexiBowl® eine Sequenz ausführt oder sich im Jog-Modus befindet.
:::

## Bedeutung von ReturnData_1 (oder TCP-Antwort)

| Wert | Bedeutung |
|---|---|
| `0` | NULL — kein Befehl in Bearbeitung (Anfangszustand) |
| `1` | Befehl nicht interpretierbar (unbekanntes ControlWord) |
| `2` | Data_1 außerhalb des Bereichs, der Befehl wurde jedoch erkannt |
| `3` | System belegt (Busy) — erneut versuchen, nachdem Busy wieder auf 0 zurückgekehrt ist |
| Wert = ControlWord | Befehl korrekt ausgeführt |

---

## Befehlsprotokoll

Das Befehlsprotokoll definiert alle über das ControlWord verfügbaren Aktionen. Die ControlWords sind **für alle Protokolle gleich**; es ändert sich nur der Transport (siehe [Fieldbus-Transport](#sec-fieldbus) und [TCP-Syntax](#sec-tcp)). Die Befehle sind in Kategorien gruppiert:

<div style="display:grid; grid-template-columns:repeat(3, 1fr); gap:1rem; margin:1.5rem 0 2.5rem;">

  <a href="#sec-exe" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-play-circle" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">EXE-Befehle</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Ausführungsbefehle (Sequenzen starten, Jog, Reset)</span>
  </a>

  <a href="#sec-write" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-pencil-simple" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">WRITE-Befehle</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Schreiben von Parametern (Geschwindigkeit, Winkel, Zeiten usw.)</span>
  </a>

  <a href="#sec-read" style="display:flex; flex-direction:column; gap:0.6rem; padding:1.1rem 1.2rem; border:1.5px solid #d0e4f0; border-radius:10px; background:#fff; text-decoration:none; color:inherit;">
    <i class="ph ph-eye" style="font-size:1.6rem; color:#2980b9;"></i>
    <span style="font-weight:700; font-size:0.95rem; color:#1a3a52; line-height:1.3;">READ-Befehle</span>
    <span style="font-size:0.82rem; color:#7a9ab0;">Lesen der aktuell konfigurierten Parameter</span>
  </a>

</div>

(sec-exe)=
### Befehle <span class="isw-section-badge isw-badge-exe"><i class="ph ph-play-circle"></i> EXE</span>

EXE-Befehle starten eine sofortige Aktion am FlexiBowl®. Während der Ausführung bleibt **Busy** auf `1`.

| Befehl | ControlWord | Busy während der Ausführung | ReturnData_1 | Erläuterung | 
|---|---|---|---|---|
| Exe Seq 1 | 10 | JA | 10 | Sequenz 1 ausführen |
| Exe Seq 2 | 11 | JA | 11 | Sequenz 2 ausführen |
| Exe Seq 3 | 12 | JA | 12 | Sequenz 3 ausführen |
| Exe Seq 4 | 13 | JA | 13 | Sequenz 4 ausführen |
| Exe Seq 5 | 14 | JA | 14 | Sequenz 5 ausführen |
| Exe Seq 6 | 15 | JA | 15 | Sequenz 6 ausführen |
| Exe Seq 7 | 16 | JA | 16 | Sequenz 7 ausführen |
| Exe Seq 8 | 17 | JA | 17 | Sequenz 8 ausführen |
| Exe Seq 9 | 18 | JA | 18 | Sequenz 9 ausführen |
| Exe Seq 10 | 19 | JA | 19 | Sequenz 10 ausführen |
| Exe Seq 11 | 20 | JA | 20 | Sequenz 11 ausführen |
| Exe Seq 12 | 21 | JA | 21 | Sequenz 12 ausführen |
| Exe Seq 13 | 22 | JA | 22 | Sequenz 13 ausführen |
| Exe Seq 14 | 23 | JA | 23 | Sequenz 14 ausführen |
| Exe Seq 15 | 24 | JA | 24 | Sequenz 15 ausführen |
| Exe Seq 16 | 25 | JA | 25 | Sequenz 16 ausführen |
| Exe Seq 17 | 26 | JA | 26 | Sequenz 17 ausführen |
| Exe Seq 18 | 27 | JA | 27 | Sequenz 18 ausführen |
| Exe Seq 19 | 28 | JA | 28 | Sequenz 19 ausführen |
| Exe Seq 20 | 29 | JA | 29 | Sequenz 20 ausführen |
| Start Jog Seq | 40 | JA | 40 | Jog starten |
| Stop Jog Seq | 41 | JA | 41 | Jog stoppen |
| Reset Return Data | 50 | NEIN | 0 | Setzt den Wert von ReturnData_1 und ReturnData_2 zurück und bringt sie in den Anfangszustand `0` |

:::{note}
Der Befehl **Reset Return Data** (ControlWord 50) setzt den Wert von ReturnData_1 und ReturnData_2 zurück und bringt sie in den Anfangszustand `0`. Er ist nützlich, um zu überprüfen, dass ein neuer Befehl tatsächlich empfangen und verarbeitet wird.
:::

(TCP_EXE)=
#### Praxisbeispiel — „Sequenz 3 ausführen“

<div class="isw-example">
<div class="isw-example-title">Sequenz 3 ausführen → ControlWord 12</div>
<div class="isw-example-body">
<div>

<div>
<div class="isw-example-col-title">TCP Server</div>

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>12[0]%</code><br> RETURN BEI OK:&nbsp;&nbsp;&nbsp;<span class="ok">12[0]</span>
</div>

Beispiel für einen **ungültigen** Befehl (z. B. Sequenz 9 existiert am Gerät nicht):

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>9[0]%</code><br> RETURN BEI NICHT OK:&nbsp;&nbsp;&nbsp;<span class="ko">1[0]</span>
</div>

</div>
</div>
</div>

(sec-write)=
### Befehle <span class="isw-section-badge isw-badge-write"><i class="ph ph-pencil-simple"></i> WRITE</span>

Mit den WRITE-Befehlen können die Betriebsparameter des FlexiBowl® (Geschwindigkeit, Winkel, Zeiten usw.) direkt vom externen System aus geändert werden, ohne die grafische Oberfläche aufrufen zu müssen.

#### Adressierungslogik der Sequenzen

Jede Sequenz (von 1 bis 20) hat einen eigenen Parameterblock. Das ControlWord wird mit folgender Formel berechnet:

> **ControlWord = N × 100 + parameter_offset**

wobei `N` die Sequenznummer (1–20) ist und `offset_parametro` den jeweiligen Parameter kennzeichnet.

#### Beschreibbare Parameter für jede Sequenz

| Parameter | Offset | Range Data_1 | Hinweise |
|---|---|---|---|
| AccelerationMove | 00 | 1–100 | Beschleunigungsrampe der Drehbewegung (%) |
| DecelerationMove | 01 | 1–100 | Verzögerungsrampe der Drehbewegung (%) |
| SpeedMove | 02 | 1–100 | Geschwindigkeit der Drehbewegung (%) |
| AngleMove | 03 | 0–720 | Drehwinkel in Grad. Werte 1000–1720 = negativer Winkel (entgegengesetzte Richtung) |
| AccelerationShake | 04 | 1–100 | Beschleunigungsrampe des Shake (%) |
| DecelerationShake | 05 | 1–100 | Verzögerungsrampe des Shake (%) |
| CountShake | 06 | 2–20 | Anzahl der Schwingungen pro Shake-Zyklus |
| CwAngleShake | 07 | 0–360 | Drehwinkel im Uhrzeigersinn während des Shake. Werte 1000–1360 = negativer Winkel |
| CcwAngleShake | 08 | 0–360 | Drehwinkel gegen den Uhrzeigersinn während des Shake. Werte 1000–1360 = negativer Winkel |
| SpeedShake | 09 | 1–100 | Geschwindigkeit des Shake (%) |
| FlipCount | 10 | 0–20 | Anzahl der Flips pro Zyklus |
| FlipDelay | 11 | 0–500 | Pause zwischen einem Flip und dem nächsten (ms) |
| BlowDelay | 12 | 0–500 | Pause zwischen einem Blasimpuls und dem nächsten (ms) |
| ProportionalValve_Flip | 13 | 0–600 | Druck des Proportionalventils Flip (Wert /100 = Bar) |
| ProportionalValve_Blow | 14 | 0–600 | Druck des Proportionalventils Blow (Wert /100 = Bar) |
| Delete all sequence | 30 | — | Löscht alle Befehle aus der Sequenzliste |
| Emptying Sequence | 40 | 0–1 | 0 = Normalmodus, 1 = Modus Quick Emptying |
| Seq Add Cmd | 50 | FLB-BEFEHL | Fügt der Sequenzliste einen Befehl hinzu |

#### Beispiele für WRITE-ControlWords

| Sequenz | Parameter | Dem Parameter zugeordneter Offset | Formel (N x 100 + Offset) | ControlWord |
|---|---|---|---|---|
| SEQ 1 (N=1) | AccelerationMove | 00 | 1 x 100 + 00 | 100 |
| SEQ 1 (N=1) | SpeedMove | 02 | 1 x 100 + 02 | 102 |
| SEQ 1 (N=1) | FlipCount | 10 | 1 x 100 + 10 | 110 |
| SEQ 1 (N=1) | Emptying Sequence | 40 | 1 x 100 + 40 | 140 |
| SEQ 1 (N=1) | Seq Add Cmd | 50 | 1 x 100 + 50 | 150 |
| SEQ 2 (N=2) | AccelerationMove | 00 | 2 x 100 + 00 | 200 |
| SEQ 2 (N=2) | SpeedMove | 02 | 2 x 100 + 02 | 202 |
| SEQ 5 (N=5) | AngleMove | 03 | 5 x 100 + 03 | 503 |
| SEQ 10 (N=10) | FlipDelay | 11 | 10 x 100 + 11 |1011 |
| SEQ 20 (N=20) | SpeedMove | 02 | 20 x 100 + 02 | 2002 |

:::{tip}
Die Formel ist einfach:
- Um die Geschwindigkeit (Offset 02) der Sequenz 7 zu schreiben, lautet das ControlWord `7 × 100 + 2 = 702`.
- Um den FlipCount (Offset 10) der Sequenz 15 zu schreiben, lautet das ControlWord `15 × 100 + 10 = 1510`.
:::

(TCP_write)=
#### Praxisbeispiel — „Die Move-Beschleunigung in Sequenz 7 auf 80 setzen“

<div class="isw-example">
<div class="isw-example-title">SpeedMove Seq 7 → ControlWord 700, Data_1 = 80</div>
<div class="isw-example-body">
<div>

<div>
<div class="isw-example-col-title">TCP Server</div>

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>700[80]%</code><br> RETURN BEI OK:&nbsp;&nbsp;&nbsp;<span class="ok">700[0]</span>
</div>

Beispiel für einen **Wert außerhalb des Bereichs** (Beschleunigung 1000 nicht zulässig, Bereich 1–100):

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>700[1000]%</code><br> RETURN BEI NICHT OK:&nbsp;&nbsp;&nbsp;<span class="ko">2[0]</span>
</div>

</div>
</div>
</div>

#### WRITE-JOG-Parameter

Die Jog-Parameter (kontinuierlicher Handbetrieb) sind separat über ControlWord im Block 20000 konfigurierbar.

| Parameter | ControlWord | Range Data_1 | Hinweise |
|---|---|---|---|
| AccelerationJog | 20001 | 0–100 | Jog-Beschleunigungsrampe (%) |
| DecelerationJog | 20002 | 0–100 | Jog-Verzögerungsrampe (%) |
| SpeedJog | 20003 | 0–100 | Jog-Geschwindigkeit (%). Werte 1000–1100 = negative Geschwindigkeit (Drehrichtungsumkehr) |
| FlipJog_Enable | 20004 | 0–1 | 0 = Flip deaktiviert, 1 = Flip während des Jog aktiviert |
| FlipJog_Duration | 20005 | 0–1000 | Dauer des Flip-Impulses (ms) |
| FlipJog_Pressure | 20006 | 0–600 | Flip-Druck (/100 = Bar) |
| FlipJog_Pause | 20007 | 0–1000 | Pause zwischen aufeinanderfolgenden Flips (ms) |
| BlowJog_Enable | 20008 | 0–1 | 0 = Blow deaktiviert, 1 = Blow während des Jog aktiviert |
| BlowJog_Duration | 20009 | 0–1000 | Dauer des Blow-Impulses (ms) |
| BlowJog_Pressure | 20010 | 0–600 | Blow-Druck (/100 = Bar) |
| BlowJog_Pause | 20011 | 0–1000 | Pause zwischen aufeinanderfolgenden Blows (ms) |
| BlowJog_Type | 20012 | 0–2 | Blow-Typ: 0 = BLOWc, 1 = BLOWe, 2 = BLOWc+BLOWe |
| Backlight_1 | 20013 | 0–1 | 0 = aus, 1 = ein |
| Backlight_2 | 20014 | 0–1 | 0 = aus, 1 = ein |

---

(sec-read)=
### Befehle <span class="isw-section-badge isw-badge-read"><i class="ph ph-eye"></i> READ</span>

Mit den READ-Befehlen können die aktuell im FlexiBowl® konfigurierten Parameter gelesen werden. Der gelesene Wert wird in **ReturnData_2** zurückgegeben.

#### READ-Adressierungslogik für Sequenzen

Das ControlWord für das Lesen wird mit folgender Formel berechnet:

> **ControlWord = 10000 + N × 100 + parameter_offset**

wobei `N` die Sequenznummer (1–20) ist und `offset_parametro` derselbe ist wie bei den WRITE-Befehlen.

Die lesbaren Parameter sind dieselben wie im WRITE-Block, ergänzt um die 10 Slots der Befehlsliste:

| Zusätzlicher Parameter | Offset | Beschreibung |
|---|---|---|
| Seq Slot 1 Cmd | 50 | Befehl an Position 1 in der Sequenzliste |
| Seq Slot 2 Cmd | 51 | Befehl an Position 2 |
| … | … | … |
| Seq Slot 10 Cmd | 59 | Befehl an Position 10 |

#### Beispiele für READ-ControlWords

| Sequenz | Parameter | ControlWord |
|---|---|---|
| SEQ 1 | AccelerationMove | 10100 |
| SEQ 1 | SpeedMove | 10102 |
| SEQ 1 | FlipCount | 10110 |
| SEQ 1 | Emptying Sequence | 10140 |
| SEQ 1 | Slot 1 Cmd | 10150 |
| SEQ 1 | Slot 10 Cmd | 10159 |
| SEQ 5 | AngleMove | 10503 |
| SEQ 10 | SpeedMove | 11002 |
| SEQ 20 | Emptying Sequence | 12040 |

:::{tip}
Schnellformel:
 Um die Geschwindigkeit (Offset 02) der Sequenz 12 zu lesen, lautet das ControlWord `10000 + 12 × 100 + 2 = 11202`.
:::

(TCP_read)=
#### Praxisbeispiel — „Den Winkel der Sequenz 16 lesen“

<div class="isw-example">
<div class="isw-example-title">AngleMove Seq 16 → ControlWord 11603</div>
<div class="isw-example-body">
<div>

<div>
<div class="isw-example-col-title">TCP Server</div>

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>11603[0]%</code><br> RETURN BEI OK:&nbsp;&nbsp;&nbsp;<span class="ok">11603[45]</span>
</div>

Beispiel für einen **Wert außerhalb des Bereichs** beim Schreiben desselben Parameters (maximaler Winkel 720°):

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>11603[6799]%</code><br> RETURN BEI NICHT OK:&nbsp;&nbsp;&nbsp;<span class="ko">1[0]</span>
</div>

</div>
</div>
</div>

#### READ-JOG-Parameter

Dieselben beschreibbaren JOG-Parameter (Block 20000) können im Block 20100 gelesen werden:

| Parameter | READ-ControlWord | Bereich ReturnData_2 |
|---|---|---|
| AccelerationJog | 20101 | 0–100 |
| DecelerationJog | 20102 | 0–100 |
| SpeedJog | 20103 | 0–100 (1000–1100 = negativ) |
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

---

(sec-hopper)=
## Befehle <span class="isw-section-badge isw-badge-hop"><i class="ph ph-funnel"></i> HOPPER</span>

Die Hopper-Befehle steuern die an das System angeschlossenen Bulk Feeder (bis zu 4). Sie folgen derselben oben beschriebenen ControlWord-/WRITE-/READ-Logik, die für alle Protokolle gilt, sowie einer dedizierten TCP-Syntax für den Schnellstart.

### Schnellstart über TCP

Zusätzlich zur allgemeinen ControlWord-Syntax bietet das Protokoll **TCP Server** dedizierte Nachrichten, um einen Hopper direkt zu starten:

| Vorgang | Zu sendende Nachricht | Antwort |
|---|---|---|
| Hopper 1 starten | `Hopper1Start%` | `Hopper1Start *` |
| Hopper 2 starten | `Hopper2Start%` | `Hopper2Start *` |
| Hopper 3 starten | `Hopper3Start%` | `Hopper3Start *` |
| Hopper 4 starten | `Hopper4Start%` | `Hopper4Start *` |

Bei den Fieldbus-Protokollen (EtherNet/IP, Profinet, Modbus) wird derselbe sofortige Start erreicht, indem das Bit **Hopper_1**...**Hopper_4** des [I/O-Pakets](#sec-fieldbus) direkt auf `1` gesetzt wird, ohne das ControlWord zu verwenden.

### Hopper-WRITE-Befehle

| Parameter | ControlWord | Range Data_1 | Beschreibung |
|---|---|---|---|
| Hopper_1_Id | 30001 | 1–100 | Eindeutige ID des Hoppers 1 im Netzwerk |
| Hopper_1_Amplitude | 30002 | 50–220 | Schwingungsamplitude von Hopper 1 |
| Hopper_1_Frequency | 30003 | 40–70 | Schwingungsfrequenz von Hopper 1 |
| Hopper_1_Activation_Time | 30004 | 400–60000 | Aktivierungszeit von Hopper 1 (ms) |
| Hopper_2_Id | 30005 | 1–100 | Eindeutige ID des Hoppers 2 |
| Hopper_2_Amplitude | 30006 | 50–220 | Schwingungsamplitude von Hopper 2 |
| Hopper_2_Frequency | 30007 | 40–70 | Schwingungsfrequenz von Hopper 2 |
| Hopper_2_Activation_Time | 30008 | 400–60000 | Aktivierungszeit von Hopper 2 (ms) |
| Hopper_3_Id | 30009 | 1–100 | Eindeutige ID des Hoppers 3 |
| Hopper_3_Amplitude | 30010 | 50–220 | Schwingungsamplitude von Hopper 3 |
| Hopper_3_Frequency | 30011 | 40–70 | Schwingungsfrequenz von Hopper 3 |
| Hopper_3_Activation_Time | 30012 | 400–60000 | Aktivierungszeit von Hopper 3 (ms) |
| Hopper_4_Id | 30013 | 1–100 | Eindeutige ID des Hoppers 4 |
| Hopper_4_Amplitude | 30014 | 50–220 | Schwingungsamplitude von Hopper 4 |
| Hopper_4_Frequency | 30015 | 40–70 | Schwingungsfrequenz von Hopper 4 |
| Hopper_4_Activation_Time | 30016 | 400–60000 | Aktivierungszeit von Hopper 4 (ms) |
| Hopper_1_Enable | 30017 | — | Hopper 1 aktivieren (sofortige Aktion) |
| Hopper_1_Disable | 30018 | — | Hopper 1 deaktivieren (sofortige Aktion) |
| Hopper_2_Enable | 30019 | — | Hopper 2 aktivieren |
| Hopper_2_Disable | 30020 | — | Hopper 2 deaktivieren |
| Hopper_3_Enable | 30021 | — | Hopper 3 aktivieren |
| Hopper_3_Disable | 30022 | — | Hopper 3 deaktivieren |
| Hopper_4_Enable | 30023 | — | Hopper 4 aktivieren |
| Hopper_4_Disable | 30024 | — | Hopper 4 deaktivieren |

:::{note}
Im Schulungsmaterial wies das ControlWord `30005` (Hopper_2_Id) irrtümlich denselben Bereich wie die Amplitude auf (50–220). In dieser Tabelle wurde er auf **1–100** korrigiert, konsistent mit Hopper_1_Id, Hopper_3_Id und Hopper_4_Id. Diesen Wert vor der Veröffentlichung der Seite anhand von Firmware/Datenblatt überprüfen.
:::

(TCP_WRITEHOPPER)=
#### Praxisbeispiel — „Hopper 1 aktivieren“

<div class="isw-example">
<div class="isw-example-title">Hopper_1_Enable → ControlWord 30017</div>
<div class="isw-example-body">
<div>

<div>
<div class="isw-example-col-title">TCP Server</div>

Über generisches ControlWord:

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>30017[0]%</code><br> RETURN BEI OK:&nbsp;&nbsp;&nbsp;<span class="ok">30017[0]</span>
</div>

Oder, nur für den Start, mit der dedizierten Nachricht:

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>Hopper1Start%</code><br> RETURN:&nbsp;&nbsp;&nbsp;<span class="ok">Hopper1Start *</span>
</div>

</div>
</div>
</div>

#### Praxisbeispiel — „Die Amplitude von Hopper 2 auf 220 setzen“

<div class="isw-example">
<div class="isw-example-title">Hopper_2_Amplitude → ControlWord 30006, Data_1 = 220</div>
<div class="isw-example-body">
<div>

<div>
<div class="isw-example-col-title">TCP Server</div>

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>30006[220]%</code><br> RETURN BEI OK:&nbsp;&nbsp;&nbsp;<span class="ok">30006[0]</span>
</div>

Beispiel für einen **Wert außerhalb des Bereichs** (Amplitude 2200 nicht zulässig, Bereich 50–220):

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>30006[2200]%</code><br> RETURN BEI NICHT OK:&nbsp;&nbsp;&nbsp;<span class="ko">2[0]</span>
</div>

</div>
</div>
</div>

### Hopper-READ-Befehle

| Parameter | READ-ControlWord | Range ReturnData_2 | Hinweise |
|---|---|---|---|
| Hopper_1_Id | 30101 | 1–100 | |
| Hopper_1_Amplitude | 30102 | 50–220 | |
| Hopper_1_Frequency | 30103 | 40–70 | |
| Hopper_1_Activation_Time | 30104 | 400–60000 | |
| Hopper_2_Id | 30105 | 1–100 | |
| Hopper_2_Amplitude | 30106 | 50–220 | |
| Hopper_2_Frequency | 30107 | 40–70 | |
| Hopper_2_Activation_Time | 30108 | 400–60000 | |
| Hopper_3_Id | 30109 | 1–100 | |
| Hopper_3_Amplitude | 30110 | 50–220 | |
| Hopper_3_Frequency | 30111 | 40–70 | |
| Hopper_3_Activation_Time | 30112 | 400–60000 | |
| Hopper_4_Id | 30113 | 1–100 | |
| Hopper_4_Amplitude | 30114 | 50–220 | |
| Hopper_4_Frequency | 30115 | 40–70 | |
| Hopper_4_Activation_Time | 30116 | 400–60000 | |
| Hopper_1_Ready | 30117 | 0–1 | 0 = nicht bereit, 1 = bereit |
| Hopper_2_Ready | 30118 | 0–1 | 0 = nicht bereit, 1 = bereit |
| Hopper_3_Ready | 30119 | 0–1 | 0 = nicht bereit, 1 = bereit |
| Hopper_4_Ready | 30120 | 0–1 | 0 = nicht bereit, 1 = bereit |
| Hopper_1_InVibration | 30121 | 0–1 | 0 = steht still, 1 = vibriert |
| Hopper_2_InVibration | 30122 | 0–1 | 0 = steht still, 1 = vibriert |
| Hopper_3_InVibration | 30123 | 0–1 | 0 = steht still, 1 = vibriert |
| Hopper_4_InVibration | 30124 | 0–1 | 0 = steht still, 1 = vibriert |
| Hopper_1_Enabled | 30125 | 0–1 | 0 = deaktiviert, 1 = aktiviert |
| Hopper_2_Enabled | 30126 | 0–1 | 0 = deaktiviert, 1 = aktiviert |
| Hopper_3_Enabled | 30127 | 0–1 | 0 = deaktiviert, 1 = aktiviert |
| Hopper_4_Enabled | 30128 | 0–1 | 0 = deaktiviert, 1 = aktiviert |

(TCP_READHOPPER)=
#### Praxisbeispiel — „Die Frequenz von Hopper 4 lesen“

<div class="isw-example">
<div class="isw-example-title">Hopper_4_Frequency → ControlWord 30115</div>
<div class="isw-example-body">
<div>

<div>
<div class="isw-example-col-title">TCP Server</div>

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>30115[0]%</code><br> RETURN BEI OK:&nbsp;&nbsp;&nbsp;<span class="ok">30115[40]</span>
</div>

Beispiel für einen **nicht interpretierbaren Befehl** (nicht vorhandenes READ-ControlWord):

<div class="isw-example-tcp">
INPUT:&nbsp;&nbsp;&nbsp;<code>30199[0]%</code><br> RETURN BEI NICHT OK:&nbsp;&nbsp;&nbsp;<span class="ko">1[0]</span>
</div>

</div>
</div>
</div>

:::{note}
Zu den Quick-Emptying-Befehlen siehe den Abschnitt [Quick-Emptying-Befehle](sec-empty)
:::

:::{important}
Zu den Fehlercodes siehe den Abschnitt [Fehlercodes](sec-err)
:::