(emptying)=
# **Emptying**

Die Seite Emptying wird automatisch verfügbar, wenn die Option Entleerung erworben wird.

## Übersicht

Die Funktion **Emptying** ermöglicht es, den FlexiBowl® automatisch zu entleeren, indem bis zu **4 dedizierte Sequenzen** verkettet werden, die jeweils eine konfigurierbare Anzahl von Malen (Loop) wiederholt werden. Sie dient dazu, die Scheibe schnell von Restteilen zu befreien, zum Beispiel am Schichtende oder beim Produktionswechsel, ohne die Sequenzen einzeln manuell aufrufen zu müssen.

![Seite Emptying](../../../../_shared/media/images/pagina_Emptying.png)

---

## Konfiguration über die Weboberfläche

Die Seite ist in **4 Spalten** gegliedert, eine für jede der Sequenzen, aus denen sich der Entleerungszyklus zusammensetzt („Select the first/second/third/fourth sequence“), sowie die Start-/Stopp-Befehle am Seitenende.

### AUTO CONFIG

Die Schaltfläche **AUTO CONFIG** oben fügt automatisch eine Standardkonfiguration ein, die die **Sequenzen 17, 18, 19 und 20** belegt. Alternativ können diese Sequenzen frei angepasst oder andere aus den 20 verfügbaren ausgewählt werden.

:::{note}
In der Standardkonfiguration senkt die erste Sequenz die Barriere (**FLB_BARRIER_DOWN**), die beiden mittleren Sequenzen wiederholen mehrfach eine kombinierte Dreh- und Blasbewegung gefolgt von einem Shake (**FLB_MOVE_BLOWc** + **FLB_SHAKE**), und die letzte hebt die Barriere am Ende des Zyklus wieder an (**FLB_BARRIER_UP**).
:::

### Elemente jeder Spalte

| Element | Funktion |
|---|---|
| **Select the first/second/third/fourth sequence** | Dropdown-Menü zur Auswahl, welche der 20 programmierten Sequenzen in diesem Schritt des Entleerungszyklus ausgeführt wird |
| **Active Command** | Liste der aktiven Befehle der ausgewählten Sequenz (bis zu 10 Plätze, gleicher Aufbau wie auf der Seite Main Command) |
| **N° Loop** | Anzahl der Wiederholungen der ausgewählten Sequenz in diesem Schritt |
| **EDIT SEQUENCE** | Öffnet die ausgewählte Sequenz zur Bearbeitung der enthaltenen Befehle |

### Start und Stopp

| Befehl | Funktion |
|---|---|
| **START EMPTYING** | Startet den Entleerungszyklus: Führt die 4 konfigurierten Sequenzen der Reihe nach aus, jede für die eingestellte Anzahl von Loops |
| **STOP EMPTYING** | Unterbricht den laufenden Entleerungszyklus |

---
## Seite Option

Ist die Funktion Emptying vorhanden, wird im Abschnitt OPTION der Seite „Main Command“ der folgende Kasten angezeigt:

![Emptying OPTION](../../../../_shared/media/images/emptying_option.png)

Dieser Kasten mit den beiden Schaltflächen „Raise Barrier“ und „Lower Barrier“ ermöglicht es, die Entleerungsbarriere anzuheben und abzusenken und so ihre korrekte Funktion zu überprüfen. Wenn die Barriere abgesenkt wird, wird der Sensor in diesem Kasten aktiviert.

## Seite Sequence 

:::{image} ../../../../_shared/media/images/box_emptying.png
:width: 50% 
:align: center
:::

Auf der Seite Sequence ermöglicht das Häkchen im Feld „Emptying Sequence“ die Bewegung des FlexiBowl auch bei abgesenkter Entleerungsbarriere. Ist die Barriere nämlich abgesenkt und das Feld auf der Seite Sequence nicht angehakt, ist die der aktuellen Sequenz zugeordnete Bewegung nicht möglich.

## Befehle über das Protokoll

Wie beim Rest der Softwareoberfläche kann der Emptying-Zyklus auch über das Protokoll (TCP Server, EtherNet/IP, Profinet, Modbus) gestartet, konfiguriert und überprüft werden, mit denselben ControlWords unabhängig vom verwendeten Protokoll – nur der Transport ändert sich, wie auf der Seite [Softwareschnittstelle](int_software) beschrieben.

### EXE-Befehle

| Befehl | ControlWord | Busy während der Ausführung | ReturnData_1 | Erläuterung |
|---|---|---|---|---|
| Start Emptying | 45 | JA (Emptying aktiv) | 45 | Startet die Entleerung |
| Stop Emptying | 46 | JA (Emptying aktiv) | 46 | Stoppt die Entleerung |
| Emptying Active | 47 | NEIN | 47 | Prüft, ob die Entleerung aktiv ist |

### WRITE-Befehle

Jedes Paar Sequenz/Loop entspricht einer der 4 Spalten der Webseite:

| Befehl | ControlWord | Range Data_1 | Busy während der Ausführung | ReturnData_1 |
|---|---|---|---|---|
| FirstSequence | 20200 | 1–20 | NEIN | 20200 |
| FirstLoop | 20201 | 0–500 | NEIN | 20201 |
| SecondSequence | 20202 | 1–20 | NEIN | 20202 |
| SecondLoop | 20203 | 0–500 | NEIN | 20203 |
| ThirdSequence | 20204 | 1–20 | NEIN | 20204 |
| ThirdLoop | 20205 | 0–500 | NEIN | 20205 |
| FourthSequence | 20206 | 1–20 | NEIN | 20206 |
| FourthLoop | 20207 | 0–500 | NEIN | 20207 |

### READ-Befehle

| Befehl | ControlWord | Busy während der Ausführung | ReturnData_1 | Range ReturnData_2 |
|---|---|---|---|---|
| FirstSequence | 20300 | NEIN | 20300 | 1–20 |
| FirstLoop | 20301 | NEIN | 20301 | 0–500 |
| SecondSequence | 20302 | NEIN | 20302 | 1–20 |
| SecondLoop | 20303 | NEIN | 20303 | 0–500 |
| ThirdSequence | 20304 | NEIN | 20304 | 1–20 |
| ThirdLoop | 20305 | NEIN | 20305 | 0–500 |
| FourthSequence | 20306 | NEIN | 20306 | 1–20 |
| FourthLoop | 20307 | NEIN | 20307 | 0–500 |

:::{tip}
Für die vollständige Erläuterung der ControlWord-Logik, des 4-Schritte-Ablaufs und praktischer Beispiele über Feldbus/TCP siehe den Abschnitt [Entleerungsbefehle](int_software.html#sec-empty) der Seite Softwareschnittstelle.
:::

---

## Hinweise zur Verwendung

:::{note}
Die 4 von Emptying aufgerufenen Sequenzen (standardmäßig 17–20 oder angepasst) bleiben normale programmierbare Sequenzen: Sie können auf der Seite **Main Command** genau wie jede andere Sequenz bearbeitet werden, ebenso über die Schaltfläche **EDIT SEQUENCE** auf dieser Seite.
:::

:::{warning}
Keinen neuen Befehl **Start Emptying** senden, während bereits ein Entleerungszyklus läuft (**Emptying Active** = 1). Vor dem Start eines neuen Zyklus prüfen, ob der vorherige beendet ist, oder **Stop Emptying** senden.
:::
