(info)=
# **Vorabinformationen**

Dieser Abschnitt enthält rechtliche Hinweise und wichtige Warnungen zur Verwendung des FlexiBowl® und dieser Dokumentation. Bitte lesen Sie diesen Abschnitt sorgfältig, bevor Sie mit der Installation und dem Betrieb des Systems beginnen.

---

## Zielgruppe

```{note}
**An wen richtet sich dieses Handbuch**

Diese Dokumentation richtet sich an qualifizierte Fachkräfte mit Kenntnissen in:
- Integration von Robotersystemen
- Konfiguration industrieller Bildverarbeitungssysteme
- Installation und Wartung elektromechanischer Geräte

Es wird vorausgesetzt, dass der Leser über die erforderlichen technischen Grundkenntnisse verfügt, um die enthaltenen Informationen zu verstehen. Informationen, die aus technischen Zeichnungen oder Diagrammen leicht abgeleitet werden können, werden möglicherweise nicht weiter ausgeführt.
```

---

## Wichtige Hinweise

### **Vor der Verwendung lesen**
```{warning}

Vor der Verwendung des FlexiBowl® ist Folgendes obligatorisch:
- Dieses Handbuch vollständig lesen, um einen korrekten Betrieb des Systems zu gewährleisten
- Die Betriebsanweisungen und Empfehlungen einhalten
- Das mit der Bedienung betraute Personal angemessen schulen
- Die Bedienungsanleitungen aller angeschlossenen Hardwarekomponenten konsultieren (FlexiVision One, Zuführeinheit, VisionController, Kamera, Roboter usw.)

Die Nichtbeachtung dieser Anweisungen kann zu Fehlfunktionen, Geräteschäden oder gefährlichen Situationen führen.
```
### **Betriebskontext und Haftungsbeschränkung**

Der FlexiBowl® ist ein flexibles Zuführsystem mit rotierender Vibrationsscheibe zur zufälligen Positionierung und Ausrichtung von Bauteilen für die Robotergreifung.

```{warning}
Während des Betriebs muss der Bediener:
- Die physischen Abmessungen des Systems berücksichtigen
- Die Bewegungen des Roboters und der Zuführeinheit überwachen
- Unvorhergesehene Betriebssituationen vorhersehen und handhaben
- Die für Roboter und Industriemaschinen geltenden Sicherheitsvorschriften einhalten
```
```{warning}
**ARS S.r.l. übernimmt keine Haftung für Personen- oder Sachschäden, die durch die Bewegung von Maschinen und Systemen entstehen, die mit der FlexiVision One-Software verbunden sind.**

Die Integration des Systems in die Arbeitsumgebung und die Risikobewertung liegen in der Verantwortung des Systemintegrators und des Endanwenders.
```

(operatori)=
## Bedienpersonal

Um eindeutig festzulegen, welche Kompetenzen und Qualifikationen das für die verschiedenen Aufgaben zuständige Personal (Inbetriebnahme, Reinigung, ordentliche Wartung) besitzen muss, ist die folgende Tabelle zu konsultieren:

:::{list-table}
:header-rows: 1
:widths: 30 70

* - Qualifikation
  - Definition

* - **Systemintegrator**
  - Personal, das für die Planung von Layouts, die Dimensionierung von Komponenten und die Überprüfung der technischen Anforderungen für die Installation des FlexiBowl® zuständig ist.

* - **Installationstechniker**
  - Personal, das für die mechanische Montage, den elektrischen und pneumatischen Anschluss sowie die Netzwerkkonfiguration zuständig ist.

* - **Bediener**
  - Personal des Anwenders, das für die Bedienung und den Betrieb der Maschine
    zu Produktionszwecken für die Tätigkeiten, für die sie gebaut und geliefert
    wurde, geschult und berechtigt ist. Er muss in der Lage sein, alle für den
    ordnungsgemäßen Betrieb der Maschine und für seine eigene Sicherheit sowie
    die etwaiger Mitarbeiter erforderlichen Maßnahmen durchzuführen. Er muss
    nachgewiesene Erfahrung im korrekten Umgang mit diesen Maschinentypen haben
    und diesbezüglich geschult, informiert und unterwiesen sein. Im Zweifelsfall
    muss er jede Anomalie seinem Vorgesetzten melden.

    **Hinweis:** Er ist nicht berechtigt, Wartungsarbeiten durchzuführen.
    
* - **Mechanischer Wartungstechniker**
  - Qualifizierter Techniker, der in der Lage ist:

    * vorbeugende/korrektive Wartungsarbeiten an allen wartungs- oder
      reparaturbedürftigen mechanischen Teilen der Maschine durchzuführen;
    * auf alle Maschinenteile zur Sichtprüfung, Zustandskontrolle der
      Geräte, Einstellungen und Kalibrierungen zuzugreifen;
    * an mechanischen Bauteilen für Einstellungen, Wartung und Reparaturen
      einzugreifen;
    * Pneumatik-, Hydraulikpläne, technische Zeichnungen und
      Ersatzteillisten zu lesen.

    In außergewöhnlichen Fällen ist er berechtigt, die Maschine mit
    reduzierten Sicherheitsvorkehrungen zu betreiben. Bei Bedarf kann er dem
    Bediener Anweisungen für einen ordnungsgemäßen Produktionsbetrieb geben.

    **Hinweis:** Er ist nicht berechtigt, an unter Spannung stehenden
    Elektroanlagen einzugreifen (sofern vorhanden).

* - **Elektrischer Wartungstechniker**
  - Qualifizierter Techniker, der in der Lage ist:
    * vorbeugende/korrektive Wartungsarbeiten an allen wartungs- oder reparaturbedürftigen mechanischen Teilen der Maschine durchzuführen;
    * auf alle Maschinenteile zur Sichtprüfung, Zustandskontrolle der Geräte, Einstellungen und Kalibrierungen zuzugreifen;
    * die Maschine wie der Bediener zu führen;
    * an Einstellungen und Elektroanlagen für Wartung, Reparatur und Austausch verschlissener Teile einzugreifen;
    * Elektropläne zu lesen und den korrekten Funktionszyklus zu überprüfen.
  Bei Bedarf kann er dem Bediener Anweisungen für einen ordnungsgemäßen Produktionsbetrieb geben. Er darf unter Spannung in Schaltkästen, Abzweigdosen, Steuergeräten usw. arbeiten, sofern er eine geeignete Person (PEI) ist. (Siehe Norm **EN50110-1**). Er führt keine Software-Programmierung von Systemen wie PLC (Logik oder Sicherheit) durch und darf keine Systempasswörter ändern.

* - **Software-Experte**
  - Qualifizierter Techniker, der in der Lage ist:
    * vorbeugende/korrektive Maßnahmen an allen Software-Teilen der Maschine durchzuführen;
    * auf alle Maschinenteile zur Sichtprüfung, Zustandskontrolle der Geräte, Einstellungen und Kalibrierungen zuzugreifen.
  Qualifizierter Techniker des Herstellers mit nachgewiesener Erfahrung und Ausbildung in Systemen basierend auf: SPS/PC-Antrieben usw. (Kenntnisse der Programmierung, Maschinenfunktionen usw.) für komplexe Vorgänge wie zum Beispiel:
    * Änderung von Maschinendaten; 
    * Erstellung von Arbeitsprogrammen; 
    * Einstellung von Antriebsparametern usw. aufgrund der Kenntnisse des Produktions-, Technologie- und Konstruktionszyklus der gelieferten Maschine. 
  Er darf unter Spannung in Schaltkästen, Abzweigdosen, Steuergeräten usw. arbeiten, sofern er eine geeignete Person (PEI) ist (Siehe Norm **EN50110-1**). Die Kompetenzen sind elektronischer und/oder softwaretechnischer Art.

* - **Herstellertechniker**
  - Vom Hersteller und/oder seinem Händler qualifizierter Techniker für komplexe Vorgänge, aufgrund der Kenntnisse des Produktionsfertigungszyklus der Maschine. Diese Person greift in Übereinstimmung mit den Anforderungen des Anwenders ein. Die Kompetenzen sind mechanischer Art.

* - **Ausgebildete Person**
  - Umfasst alle in dieser Tabelle aufgeführten Qualifikationen: Es handelt sich um eine Person, die über die Arbeit und mögliche Gefahren bei unsachgemäßem Gebrauch informiert, unterwiesen und geschult wurde. Sie kennt außerdem die Bedeutung der Sicherheitsvorrichtungen, die Unfallverhütungsvorschriften und die sicheren Arbeitsbedingungen.

:::

---

## Hinweise zur Dokumentation

### **Version und Aktualisierungen**

```{note}

- **Referenzsprache**: Die italienische Version dieses Dokuments ist die offizielle Version und hat bei Abweichungen von anderen Übersetzungen Vorrang
- **Aktualisierungen**: Die enthaltenen Informationen können zur Produktverbesserung ohne vorherige Ankündigung geändert werden
- **Maßeinheiten**: Sofern nicht anders angegeben, sind alle Maße in Millimetern (mm) ausgedrückt
- **Dokumentversion**: Stellen Sie stets sicher, dass Sie über die neueste Version verfügen, indem Sie die Website [www.flexibowl.it](https://www.flexibowl.it) konsultieren
```
### **So nutzen Sie dieses Handbuch optimal**

```{tip}

Für ein optimales Erlebnis:
- Verwenden Sie das seitliche Navigationsmenü, um schnell zwischen den Abschnitten zu wechseln
- Konsultieren Sie das Ausgangsverzeichnis, um sofort den für Sie relevanten Abschnitt zu identifizieren
- Achten Sie besonders auf die Warn-, Hinweis- und Tipp-Banner
- Befolgen Sie die Verfahren in der angegebenen Reihenfolge, insbesondere bei der Erstinstallation
- Bewahren Sie dieses Handbuch im digitalen Format auf, um schnelle Stichwortsuchen zu erleichtern
```

---


## Vervielfältigungsrechte und rechtliche Hinweise

```{important}
**Copyright © ARS S.r.l. - Alle Rechte vorbehalten**

Kein Teil dieser Veröffentlichung darf ohne vorherige schriftliche Genehmigung von ARS S.r.l. für andere Zwecke als den persönlichen Gebrauch reproduziert, verteilt, übersetzt oder mit irgendwelchen Mitteln (elektronisch, mechanisch, Fotokopie, Aufzeichnung oder andere Speichersysteme) übertragen werden.

ARS S.r.l. übernimmt keine Haftung für Folgen, die aus fehlerhaften Bedienungen durch den Benutzer oder aus unsachgemäßem Gebrauch des Produkts entstehen.

**Eingetragene Marken**: FlexiBowl® ist eine eingetragene Marke von ARS S.r.l. Alle anderen in diesem Dokument genannten Marken, Handelsnamen und Logos gehören ihren jeweiligen Eigentümern und werden ausschließlich zu Identifikationszwecken verwendet.
```
---

