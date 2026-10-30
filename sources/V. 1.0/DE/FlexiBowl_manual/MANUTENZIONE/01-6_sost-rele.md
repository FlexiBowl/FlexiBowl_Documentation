# **Austausch von Relais und Sicherungen**


Dieser Abschnitt beschreibt die Funktion und das Austauschverfahren der **Schnittstellenrelais** und der **Schutzsicherungen** auf der Schnittstellenplatine.

Die folgende Abbildung zeigt die Platine mit der Lage der Relais und Sicherungen.

::: {figure} ../../../../_shared/media/images/schedafronte.png
:align: center
:width: 80%

Vorderansicht der Schnittstellenplatine
:::

Auf der Rückseite der Platine sind die Stromstärke jeder Sicherung und die Bezeichnung jedes Schnittstellenrelais angegeben.

(scheda-interfaccia-retro)=
::: {figure} ../../../../_shared/media/images/schedaretro.png
:align: center
:width: 80%

Rückansicht: Relaisbezeichnungen und Sicherungswerte
:::

### Sicherheitshinweise

:::{danger}
**Elektrische Gefahr.** Vor Arbeiten an der Schnittstellenplatine die Maschine über den Hauptschalter spannungsfrei schalten und die Entladung der Kondensatoren abwarten. Vor dem Berühren jeglicher Komponenten die Spannungsfreiheit mit einem geeigneten Messgerät prüfen.
:::

Bei den Wartungsarbeiten sind die folgenden Anweisungen strikt zu beachten:

- Die Arbeiten dürfen ausschließlich von qualifiziertem und geschultem Fachpersonal durchgeführt werden;
- geeignete persönliche Schutzausrüstung (PSA) verwenden, einschließlich antistatischer Handschuhe;
- während der Arbeiten vermeiden, dass Werkzeuge oder Fremdkörper auf die Platine fallen;
- eine Sicherung nicht durch eine mit anderer Stromstärke als der ursprünglichen ersetzen;
- Relais beim Herausziehen nicht gewaltsam behandeln: Sitzt ein Bauteil fest, vor dem Fortfahren prüfen, ob es korrekt eingerastet ist;
- Nach Abschluss der Arbeiten die Zugangsklappe/den Zugangsschlitz ordnungsgemäß schließen, bevor die Stromversorgung wiederhergestellt wird.

### Beschreibung der Platine

(scheda-relè)=
#### Schnittstellenrelais

Die Platine ist mit fünf Schnittstellenrelais ausgestattet, die mit K1–K5 bezeichnet sind. Das Relais K1 ist ein elektromechanisches Relais mit zwei Wechslern; alle übrigen Relais (K2–K5) sind Halbleiterrelais.

:::{list-table}
:widths: 10 55 35
:header-rows: 1

* - Bez.
  - Funktion
  - Typ
* - K1
  - Schnittstellenrelais für Backlight
  - Elektromechanisch mit zwei Wechslern
* - K2
  - Schnittstellenrelais für Flip-Magnetventil
  - Halbleiter
* - K3
  - Schnittstellenrelais für Magnetventil der zentralen Blasluft
  - Halbleiter
* - K4
  - Schnittstellenrelais für Magnetventil der radialen Blasluft
  - Halbleiter
* - K5
  - Schnittstellenrelais für Entleerungs-Magnetventil (optional)
  - Halbleiter
:::

(scheda-fusibili)=
#### Schutzsicherungen

Die Platine ist mit neun Schutzsicherungen vom Typ *Automotive Mini* ausgestattet. Das Ersatzsicherungs-Set wird mit dem FlexiBowl® geliefert.

:::{list-table}
:widths: 10 70 20
:header-rows: 1

* - Bez.
  - Funktion
  - Wert
* - F1
  - Hauptversorgung
  - 10 A
* - F2
  - 24-V-Versorgung — Magnetventile für Flip, zentrale/radiale Blasluft und Entleerung
  - 7.5 A
* - F3
  - Versorgung des STO-Steckers
  - 2 A
* - F4
  - Versorgung zum Kunden
  - 5 A
* - F5
  - Entleerungssensor
  - 2 A
* - F6
  - Backlight-Versorgung
  - 7.5 A
* - F7
  - Backlight-Versorgung
  - 7.5 A
* - F8
  - Versorgung von Motor und Treiber
  - 5 A
* - F9
  - SPS-Versorgung
  - 7.5 A
:::

### Erforderliche Ausrüstung

- Sicherungszieher für *Automotive-Mini*-Sicherungen (oder Flachzange/Pinzette mit flachen Spitzen)
- Mit dem FlexiBowl® gelieferte Ersatzsicherungs-Set
- Ersatzrelais gemäß der ursprünglichen Bezeichnung (K1–K5)

### Austausch der Schnittstellenrelais

Das Verfahren gilt für den Austausch eines oder mehrerer Schnittstellenrelais (K1–K5).

1. Die Maschine spannungsfrei schalten und die Spannungsfreiheit mit dem Multimeter prüfen, wie in den Sicherheitshinweisen angegeben.
2. Über die vorgesehene Öffnung auf die Schnittstellenplatine zugreifen.
3. Das auszutauschende Relais anhand der {ref}`Rückansicht <scheda-interfaccia-retro>` und der {ref}`Relaistabelle <scheda-relè>` lokalisieren.
4. Ist das auszutauschende Relais **K1** (elektromechanisch), es vorsichtig nach oben aus dem Sockel ziehen, ohne die Anschlüsse zu verbiegen.
5. Ist das auszutauschende Relais **K2, K3, K4 oder K5** (Halbleiter), es mit derselben Sorgfalt herausziehen und dabei die Kontaktstifte nicht verbiegen.
6. Das Ersatzrelais in den Sockel einsetzen und prüfen, dass Bezeichnung und Ausrichtung genau mit denen des entfernten Bauteils übereinstimmen.
7. Prüfen, dass das Relais korrekt eingesetzt ist und fest im Sockel sitzt.
8. Die Zugangsöffnung zur Platine wieder schließen.
9. Die Stromversorgung wiederherstellen und prüfen, ob die dem ausgetauschten Relais zugeordnete Funktion korrekt arbeitet.

### Austausch der Schutzsicherungen

Das Verfahren gilt für den Austausch einer oder mehrerer Schutzsicherungen (F1–F9).

1. Die Maschine spannungsfrei schalten und die Spannungsfreiheit mit dem Multimeter prüfen, wie in den Sicherheitshinweisen angegeben.
2. Den dafür vorgesehenen Zugangsschlitz zu den Schutzsicherungen öffnen.
3. Die auszutauschende Sicherung anhand der {ref}`Rückansicht <scheda-interfaccia-retro>` und der {ref}`Sicherungstabelle <scheda-fusibili>` lokalisieren.
4. Die Sicherung mit dem dafür vorgesehenen Zieher (oder einer Pinzette) herausziehen und dabei die Metallteile nicht berühren.
5. Wenn möglich, vor dem Austausch die Ursache für das Auslösen der Sicherung ermitteln.
6. Aus dem Ersatzset eine Sicherung vom Typ *Automotive Mini* mit demselben in der Tabelle angegebenen Wert (Stromstärke) entnehmen.
7. Die neue Sicherung in ihren Sitz einsetzen und prüfen, dass sie korrekt sitzt.
8. Den Zugangsschlitz wieder schließen.
9. Die Stromversorgung wiederherstellen und prüfen, ob der durch die ausgetauschte Sicherung geschützte Stromkreis korrekt arbeitet.

:::{caution}
Niemals eine Sicherung mit einem anderen Wert als dem ursprünglichen verwenden.
:::

### Regelmäßige Kontrollen und vorbeugende Wartung

- Regelmäßig auf Anzeichen von Überhitzung oder Schwärzung an Relais, Sicherungen und Sockeln prüfen.
- Prüfen, dass die Stecker auf der Platine korrekt eingesteckt sind.
- Stets einen Vorrat des Ersatzsicherungs-Sets vorhalten.
- Jeden durchgeführten Austausch (Datum, Bauteilbezeichnung, Ursache) in einem Wartungsprotokoll festhalten.
