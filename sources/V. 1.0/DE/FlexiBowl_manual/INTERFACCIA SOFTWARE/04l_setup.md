# **Setup**
## Übersicht

Die Seite **Setup** fasst die Netzwerk- und Kommunikationseinstellungen des FlexiBowl® zusammen. Sie ermöglicht die Konfiguration der IP-Adresse des Geräts und des Kommunikationsprotokolls mit dem externen System (z. B. SPS oder übergeordneter PC) sowie die Überwachung des Verbindungsstatus in Echtzeit.

Oben rechts wird die **Firmware-Version** der installierten Firmware angezeigt (im Beispiel: `1.0.2`).

![Seite Setup](../../../../_shared/media/images/setup.png)

---

## Obere Leiste

| Element | Beschreibung |
|---|---|
| **Menu** (Symbol ☰) | Öffnet das Navigationsmenü zwischen den Softwareseiten |
| **READY** | Statusanzeige des Geräts: Zeigt an, dass der FlexiBowl® einsatzbereit ist |
| **USER** | Zeigt den aktuell mit der Softwareoberfläche verbundenen Benutzer an |
| **REBOOT** | Startet die FlexiBowl®-Software neu, ohne das System auszuschalten |
| **Version** | Version der aktuell auf dem Gerät installierten Firmware |
| **ENABLE MOTOR** | Aktiviert die Stromversorgung des FlexiBowl®-Motors. Bei deaktiviertem Motor führt das Gerät keine Bewegung aus |

:::{warning}
Die Schaltfläche **REBOOT** unterbricht vorübergehend alle laufenden Vorgänge. Keinen Neustart während einer aktiven Sequenz oder während einer Dateiübertragung durchführen.
:::

:::{warning}
Vor dem Drücken von **ENABLE MOTOR** sicherstellen, dass der Bereich um den FlexiBowl® frei ist: Mit der Aktivierung des Motors ist das Gerät bewegungsbereit.
:::

---

## Bereich GET IP

Der linke Bereich zeigt die dem FlexiBowl® aktuell zugewiesenen Netzwerkparameter an.

| Feld | Beispielwert | Beschreibung |
|---|---|---|
| **IP** | 192.168.1.90 | Aktuelle IP-Adresse des Geräts |
| **SUBNET** | 255.255.255.0 | Aktuelle Subnetzmaske |
| **MAC** | 00:30:de:77:fe:74 | MAC-Adresse der Netzwerkkarte des Geräts |
| **Info** | Done | Ergebnis des letzten Lesevorgangs |

Die Schaltfläche **GET IP** aktualisiert die Felder, indem sie die aktuell auf dem Gerät konfigurierten Netzwerkparameter ausliest.

---

## Bereich SET IP

Im mittleren Bereich können die IP-Adresse und die Subnetzmaske des FlexiBowl® geändert werden.

| Feld | Beispielwert | Beschreibung |
|---|---|---|
| **IP** | 192.168.1.90 | Neue IP-Adresse, die dem Gerät zugewiesen werden soll (oktettweise eingebbar) |
| **SUBNET** | 255.255.255.0 | Neue Subnetzmaske, die zugewiesen werden soll |
| **Info** | All Done. | Ergebnis des letzten Einstellvorgangs |

Die Schaltfläche **SET IP** übernimmt die eingegebenen Werte und speichert sie in der Netzwerkkonfiguration des Geräts.

:::{important}
Nach dem Ändern der IP-Adresse mit **SET IP** muss das System mit **REBOOT** neu gestartet werden, damit die Änderungen wirksam werden. Die Software muss anschließend mit der neuen IP-Adresse neu verbunden werden.
:::

:::{warning}
Sicherstellen, dass die neue IP-Adresse nicht bereits von einem anderen Gerät im selben Netzwerk verwendet wird, um Adresskonflikte zu vermeiden, die den FlexiBowl® unerreichbar machen könnten.
:::

---

## Bereich SELECT THE COMMUNICATION TYPE

Im rechten Bereich kann das Kommunikationsprotokoll zwischen dem FlexiBowl® und dem externen System (SPS, übergeordneter PC, Bildverarbeitungssystem) konfiguriert werden.

![Kommunikationsbereich](../../../../_shared/media/images/comm_type.png)

| Feld |  Beschreibung |
|---|---|
| **Kommunikationstyp** |  Ausgewähltes Kommunikationsprotokoll. Auswählbar über das Dropdown-Menü |
| **Port** |  TCP-Port, auf dem der FlexiBowl® als Server lauscht |
| **Abschlusszeichenfolge** | Zeichen oder Zeichenfolge, die die ausgetauschten Nachrichten begrenzt. Auswählbar über das Dropdown-Menü |

Die Schaltfläche **APPLY** bestätigt und übernimmt die ausgewählten Kommunikationseinstellungen.

:::{note}
Der Modus **TCP Server** bedeutet, dass der FlexiBowl® als Server fungiert: Das externe System (Client) muss die Verbindung zur konfigurierten IP-Adresse und zum konfigurierten Port aufbauen.
:::

:::{tip}
Prüfen, dass der konfigurierte Port (z. B. 8123) nicht durch eine Firewall auf dem PC oder im Firmennetzwerk blockiert wird. Bei Verbindungsproblemen den IT-Verantwortlichen konsultieren.
:::

---

## Auswahl der Abschlusszeichenfolge

Mit dem dritten Dropdown-Menü des Bereichs **SELECT THE COMMUNICATION TYPE** wird das **Abschlusszeichen** der mit dem externen System ausgetauschten Nachrichten gewählt, d. h. die Zeichenfolge, die das Ende jedes gesendeten Befehls und jeder empfangenen Antwort kennzeichnet.

![Dropdown-Menü der Abschlusszeichenfolge](../../../../_shared/media/images/tendina_stringa.png)

| Option | Abschlusszeichen | Beschreibung |
|---|---|---|
| **% only** | `%` | Nur das Zeichen `%`, ohne Zeilenende-Zeichen |
| **% + CR** | `%` + `\r` | Zeichen `%` gefolgt von Carriage Return (0x0D) |
| **% + LF** | `%` + `\n` | Zeichen `%` gefolgt von Line Feed (0x0A) |
| **% + CR/LF** | `%` + `\r\n` | Zeichen `%` gefolgt von Carriage Return und Line Feed (0x0D 0x0A) |

Nach der Auswahl der gewünschten Option **APPLY** drücken, damit die Einstellung wirksam wird.

:::{important}
Die gewählte Abschlusszeichenfolge muss mit der vom externen System (SPS, übergeordneter PC oder Bildverarbeitungssystem) erwarteten übereinstimmen. Stimmen die beiden Einstellungen nicht überein, werden die gesendeten Befehle nicht erkannt und die Kommunikation schlägt fehl, selbst wenn der Server online und der Client verbunden ist.
:::

:::{tip}
Wenn Befehle scheinbar gesendet werden, aber keine Antwort erfolgt, im Statusbereich das Feld **Last message received** prüfen: Kommt die Nachricht an, bleibt aber ohne Wirkung, liegt die Ursache häufig an einer falschen Abschlusszeichenfolge.
:::

---

## Statusbereich der Kommunikation

Der untere Bereich zeigt in Echtzeit den Status der Verbindung zwischen dem FlexiBowl® und dem externen Client.

### Statusanzeigen

| Anzeige | Aktive Farbe |  Beschreibung |
|---|---|---|
| **SERVER ONLINE** | 🟢 Grün |  Der TCP-Server des FlexiBowl® ist aktiv und lauscht |
| **CLIENT CONNECTED** | 🟢 Grün |  Ein externer Client ist derzeit mit dem Server verbunden |
| **CLIENT IP** | — | IP-Adresse des aktuell verbundenen Clients |

:::{note}
Ist eine Anzeige grau, ist die entsprechende Bedingung nicht erfüllt: Im Beispiel ist der Server online, aber noch kein Client verbunden.
:::

### Nachrichtenmonitor

| Feld |  Beschreibung |
|---|---|
| **Last message received** | Zuletzt vom externen Client empfangene Nachricht |
| **Last message sent** | Zuletzt vom FlexiBowl® an den Client gesendete Nachricht |

:::{note}
Der Nachrichtenmonitor ist bei der Integration und beim Debuggen der Kommunikation mit dem externen System nützlich. Die angezeigten Nachrichten folgen dem Kommunikationsprotokoll des FlexiBowl®; die vollständige Liste der verfügbaren Befehle ist der Protokolldokumentation zu entnehmen.
:::

### Schaltfläche RESTART SERVER

Die Schaltfläche **RESTART SERVER** startet den TCP-Dienst des FlexiBowl® neu, ohne einen vollständigen Neustart des Systems durchzuführen. Sie ist nützlich, um die Verbindung bei einer unerwarteten Trennung des Clients oder bei einem Hängen des Servers wiederherzustellen.

:::{warning}
**RESTART SERVER** unterbricht die aktuelle TCP-Verbindung. Führt der FlexiBowl® gerade eine ferngesteuerte Sequenz aus, wird diese unterbrochen. Diese Funktion nur verwenden, wenn sich das System im Stand-by befindet.
:::
