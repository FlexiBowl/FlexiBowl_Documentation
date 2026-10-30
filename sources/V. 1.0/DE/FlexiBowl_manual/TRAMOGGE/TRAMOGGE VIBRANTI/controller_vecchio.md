# **Altes Steuergerät**
## Standardsteuerung

#### Elektrische Anschlüsse und Einrichtung der Steuerung

:::{attention}
Stecken Sie vor dem Einschalten der Steuerung den Schuko-Stecker in die Steckdose und prüfen Sie, dass die Anlage über ein geeignetes Erdungssystem verfügt.
:::

Gehen Sie zum Starten wie beschrieben vor:

<div style="display: flex; flex-direction: column; gap: 12px; margin: 20px 0;">
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #34495e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">1</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Schließen Sie das Kabel des Linearsockels an den Ausgangsanschluss der Steuerung an (d. h. den Vibrator an den Ausgangsanschluss <strong>(1)</strong>).
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #34495e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">2</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Drehen Sie den Frequenz-Einstellknopf <strong>(2)</strong> und den Amplituden-Einstellknopf <strong>(3)</strong> der Steuerung auf die Position „•“.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #34495e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">3</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Schalten Sie die Steuerung mit der Taste ON/OFF ein (Taste in Stellung 1 <strong>(4)</strong>).
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #34495e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">4</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Drehen Sie die Einstellknöpfe <strong>(2 und 3)</strong> langsam. Bevor die Vibration auf das Maximum gebracht wird (Potentiometer Amplitude <strong>(3)</strong>), empfiehlt es sich, mit dem Potentiometer Frequency <strong>(2)</strong> die richtige Resonanzfrequenz (50 Hertz) zu suchen.
    </div>
  </div>
</div>

![Steuerung mit Markierungen](../../../../../_shared/media/images/controller_puntatori.png)

Zur Einhaltung der EMV-Vorschriften ist die Schaltung mit einem Filter mit Erdableitströmen unter 1 mA ausgestattet.
 Die Schaltung versorgt den Vibrator mit einem in Amplitude und Frequenz einstellbaren PWM-Signal (Pulsweitenmodulation), das gegenüber Schwankungen der Netzspannung kompensiert ist.
  Der Steuerteil ist vom Leistungsteil galvanisch getrennt.
   Beim Einschalten wartet die Schaltung einige Sekunden, bevor sie den Vibrator freigibt.

Die Schaltung ist mikroprozessorgesteuert und verfügt über eine Begrenzung des Ausgangsstroms über die Sicherung F4 (4 A).

**Absicherung durch Sicherungen**

| Sicherung | Wert | Position |
| :--- | :--- | :--- |
| **F1** | 6,3 A | Netzeingang |
| **F3** | 250 mA | Eingang ON/OFF — begrenzt den für den NPN/PNP-Sensor und ein eventuelles Magnetventil verfügbaren Strom |
| **F4** | 4 A | Vibratorausgang |

**LED-Anzeigen auf der Platine**

| LED | Farbe | Status: leuchtet |
| :--- | :--- | :--- |
| **LD1** | Rot | Hochspannung an den Filterkondensatoren vorhanden (bis über 300 V bei 230 V Netzspannung) |
| **LD2** | Grün | Spannung im Steuerkreis vorhanden. Aus, wenn F1, F2 oder F3 durchgebrannt sind |
| **LD3** | Grün | Relais ON/OFF geschaltet — Vibrator in Betrieb oder gestoppt |
| **LD4** | Gelb | Relais geschaltet, weil die Zeit ohne Teile überschritten wurde |

:::{attention}
Berühren Sie die Schaltung unbedingt nicht, solange die rote LED (LD1) leuchtet.
:::

Die den LEDs LD3 und LD4 zugeordneten Relais stellen einen Wechslerkontakt an den Steckverbindern **CONN4** und **CONN5** bereit: **CONN4** ermöglicht die Kaskadenansteuerung eines zusätzlichen Moduls, **CONN5** die Aktivierung eines Teilefluss-Alarms.

**Verfügbare Einstellungen**

Mit den Trimmern auf der Platine kann das Verhalten des Vibrators an die Anwendung angepasst werden:

- **TR2** — Verzögerung beim Stopp des Vibrators (0 ÷ 10 s)
- **TR3** — Verzögerung beim Start des Vibrators (0 ÷ 10 s)
- **TR4** — maximale Amplitude
- **TR5** — zusätzliche Startverzögerung
- **TR6** — minimale Amplitude

Der Vibrator kann über einen externen Befehl an **CONN3** angehalten und neu gestartet werden, kompatibel mit potentialfreiem Kontakt, NPN/PNP-Sensor oder 0–24-V-Ausgang, mit oder ohne die konfigurierten Verzögerungen.
 Mit **DP1** lässt sich die direkte oder invertierte Logik des ON/OFF-Signals auswählen.

**Von ARS empfohlene Standardkonfiguration**

| Komponente | Einstellung |
| :--- | :--- |
| **DP1** | Beide Schalter in Stellung ON |
| **DP2** | Schalter 2 ON — Schalter 1 OFF |
| **TR2 e TR3** | Einstellschraube bis zum Anschlag gegen den Uhrzeigersinn gedreht |
| **CONN3** | Start eines Bulk Feeders mit potentialfreiem Kontakt |

![Zeichnung der Steuerung](../../../../../_shared/media/images/disegno_controller.jpg)

---

### Analogsteuerung

![Analogsteuerung](../../../../../_shared/media/images/controller_analogico.png)

#### Elektrische Anschlüsse und Einrichtung der Steuerung

Gehen Sie zum Starten wie beschrieben vor und beachten Sie das Bild am Ende des Absatzes:

<div style="display: flex; flex-direction: column; gap: 12px; margin: 20px 0;">
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">1</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Schließen Sie die 80/250-V-AC-Versorgung an den Steckverbinder <strong>CONN 1</strong> an.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">2</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Schließen Sie das vom Vibrationssockel kommende Kabel an den Steckverbinder <strong>CONN 2</strong> an.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">3</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Schließen Sie den Ansteuerbefehl an den Steckverbinder <strong>CONN 3</strong> an.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">4</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Schließen Sie den Analogeingang an den Steckverbinder <strong>CONN 7</strong> an.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">5</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Stellen Sie den Trimmer <strong>TR1</strong> so ein, dass die Frequenz 50 Hertz beträgt.
    </div>
  </div>
</div>

Zur Einhaltung der EMV-Vorschriften ist die Schaltung mit einem Filter mit Erdableitströmen unter 1 mA ausgestattet.
 Die Schaltung versorgt den Vibrator mit einem PWM-Signal, dessen Amplitude über ein Analogsignal und dessen Frequenz über den Trimmer **TR1** einstellbar ist.
  Das Signal ist gegenüber Schwankungen der Netzspannung kompensiert. Der Steuerteil ist vom Leistungsteil galvanisch getrennt.
   Beim Einschalten wartet die Schaltung einige Sekunden, bevor sie den Vibrator freigibt.

Die Schaltung ist mikroprozessorgesteuert und verfügt über eine Begrenzung des Ausgangsstroms über die Sicherung F4 (4 A).

**Absicherung durch Sicherungen**

| Sicherung | Wert | Position |
| :--- | :--- | :--- |
| **F1–F2** | 6,3 A | Netzeingang |
| **F3** | 250 mA | Eingang ON/OFF — begrenzt den für den NPN/PNP-Sensor und ein eventuelles Magnetventil verfügbaren Strom |
| **F4** | 4 A | Vibratorausgang |

**LED-Anzeigen auf der Platine**

| LED | Farbe | Status: leuchtet |
| :--- | :--- | :--- |
| **LD1** | Rot | Hochspannung an den Filterkondensatoren vorhanden (bis über 300 V bei 230 V Netzspannung) |
| **LD2** | Grün | Spannung im Steuerkreis vorhanden. Aus, wenn F1, F2 oder F3 durchgebrannt sind |
| **LD3** | Grün | Relais ON/OFF geschaltet — Vibrator in Betrieb oder gestoppt |
| **LD4** | Gelb | Relais geschaltet, weil die Zeit ohne Teile überschritten wurde |

:::{attention}
Berühren Sie die Schaltung unbedingt nicht, solange die rote LED (LD1) leuchtet.
:::

Die den LEDs LD3 und LD4 zugeordneten Relais stellen einen Wechslerkontakt an den Steckverbindern **CONN4** und **CONN5** bereit: **CONN4** ermöglicht die Kaskadenansteuerung eines zusätzlichen Moduls, **CONN5** die Aktivierung eines Teilefluss-Alarms.

**Verfügbare Einstellungen**

Mit den Trimmern auf der Platine kann das Verhalten des Vibrators an die Anwendung angepasst werden:

- **TR2** — Verzögerung beim Stopp des Vibrators (0 ÷ 10 s)
- **TR3** — Verzögerung beim Start des Vibrators (0 ÷ 10 s)
- **TR4** — Verzögerung, nach der der Alarm „Teile fehlen“ ausgelöst wird (0 ÷ 10 s)
- **TR5** — zusätzliche Aktivierungszeit des Blasluft-Magnetventils nach dem Stopp des Vibrators (0 ÷ 3 s)
- **TR6** — Rampe beim Einschalten des Vibrators (0 ÷ 3 s)
- **TR7** — maximale Amplitude am Vibrator

Der Vibrator kann über einen externen Befehl an **CONN3** angehalten und neu gestartet werden, kompatibel mit potentialfreiem Kontakt, NPN/PNP-Sensor oder 0–24-V-Ausgang, mit oder ohne die konfigurierten Verzögerungen.
 Mit **DP1** lässt sich die NC- oder NO-Logik des ON/OFF-Signals auswählen.
 Die Vibrationsamplitude wird durch Einstellen der geeigneten Analogspannung an **CONN7** geregelt.

**Von ARS empfohlene Standardkonfiguration**

| Komponente | Einstellung |
| :--- | :--- |
| **DP1** | Beide Schalter in Stellung ON |
| **DP2** | Schalter 1 ON — Schalter 2 OFF |
| **TR2 e TR3** | Einstellschraube bis zum Anschlag gegen den Uhrzeigersinn gedreht |
| **CONN3** | Start eines Bulk Feeders mit potentialfreiem Kontakt |


![Schaltplan der Steuerung](../../../../../_shared/media/images/controller_schema.png)