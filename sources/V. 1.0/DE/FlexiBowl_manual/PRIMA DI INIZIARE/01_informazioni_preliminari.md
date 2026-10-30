(info)=
# **Vorbemerkungen**

Dieser Abschnitt enthält rechtliche Informationen und wichtige Warnhinweise zur Verwendung des FlexiBowl® und dieser Dokumentation.   Bitte sorgfältig lesen, bevor mit der Installation und der Nutzung des Systems begonnen wird.

---

## Adressaten und Zielgruppe

```{note}
**Für wen dieses Handbuch bestimmt ist**

Diese Dokumentation richtet sich an qualifizierte Techniker mit Kenntnissen in:
- Integration robotergestützter Systeme
- Konfiguration industrieller Bildverarbeitungssysteme
- Installation und Wartung elektromechanischer Anlagen

Es wird vorausgesetzt, dass der Leser über die technischen Grundkenntnisse verfügt, die zum Verständnis der enthaltenen Informationen erforderlich sind.   Informationen, die sich leicht aus technischen Zeichnungen oder Diagrammen ableiten lassen, werden möglicherweise nicht weiter ausgeführt.
```

---

## Wichtige Warnhinweise

### **Vor Gebrauch lesen**
```{warning}

Vor der Verwendung des FlexiBowl® ist es zwingend erforderlich:
- Dieses Handbuch vollständig zu lesen, um eine korrekte Nutzung des Systems sicherzustellen
- Die Betriebsanweisungen und Empfehlungen zu beachten
- Das mit der Nutzung beauftragte Personal angemessen zu schulen
- Die Betriebsanleitungen aller angeschlossenen Hardwarekomponenten zu konsultieren (FlexiVision One, Bulk Feeder, VisionController, Kamera, Roboter usw.)

Die Nichtbeachtung dieser Hinweise kann zu Fehlfunktionen, Schäden an den Geräten oder gefährlichen Situationen führen.
```
### **Betriebskontext und Haftungsbeschränkungen**

Der FlexiBowl® ist ein flexibles Zuführsystem mit rotierender Vibrationsscheibe zur zufälligen Positionierung und Ausrichtung von Bauteilen für die robotergestützte Entnahme.

```{warning}
Während der Nutzung muss der Bediener:
- die physischen Abmessungen des Systems berücksichtigen
- die Bewegungen des Roboters und des Zuführers überwachen
- unvorhergesehene Betriebssituationen vorhersehen und bewältigen
- die für Industrieroboter und Maschinen geltenden Sicherheitsnormen einhalten
```
```{warning}
**ARS S.r.l. lehnt jede Haftung für Personen- oder Sachschäden ab, die aus der Bewegung von Maschinen und Systemen entstehen, die an die FlexiVision-One-Software angeschlossen sind.**

Die Integration des Systems in die Arbeitsumgebung und die Risikobewertung liegen in der Verantwortung des Systemintegrators und des Endanwenders.
```

(operatori)=
## Bediener

Um die Kompetenzen und Qualifikationen der mit den verschiedenen Aufgaben (Inbetriebnahme, Reinigung, regelmäßige Wartung) betrauten Bediener eindeutig festzulegen, die folgende Tabelle konsultieren:

:::{list-table}
:header-rows: 1
:widths: 30 70

* - Qualifikation
  - Definition

* - **Systemintegrator**
  - Personal, das mit der Planung der Layouts, der Dimensionierung der Komponenten und der Prüfung der technischen Anforderungen für die Installation des FlexiBowl® betraut ist.

* - **Installationstechniker**
  - Personal, das mit der mechanischen Montage, dem elektrischen und pneumatischen Anschluss sowie der Netzwerkkonfiguration betraut ist.

* - **Bediener**
  - Geschultes und befugtes Personal des Anwenders für die Nutzung und den Betrieb der Maschine zu Produktionszwecken, für die Tätigkeiten, für die sie gebaut und geliefert wurde. Es muss in der Lage sein, alle für den einwandfreien Betrieb der Maschine und für die Unversehrtheit der eigenen Person und eventueller Mitarbeiter erforderlichen Arbeiten auszuführen. Es muss nachweisliche Erfahrung im korrekten Umgang mit derartigen Maschinen haben und diesbezüglich geschult, informiert und unterwiesen sein. Im Zweifelsfall muss es jede Anomalie seinem Vorgesetzten melden.

    **Hinweis:** Nicht befugt, Wartungstätigkeiten jeglicher Art durchzuführen.
    
* - **Mechanischer Instandhalter**
  - Qualifizierter Techniker, der in der Lage ist:

    * vorbeugende/korrektive Wartungsarbeiten an allen mechanischen Teilen der Maschine durchzuführen, die gewartet oder repariert werden müssen;
    * zu allen Teilen der Maschine Zugang zu haben für Sichtprüfung, Kontrolle des Gerätezustands, Einstellungen und Kalibrierungen;
    * an den mechanischen Bauteilen Einstellungen, Wartungs- und Reparaturarbeiten vorzunehmen;
    * pneumatische und hydraulische Schaltpläne, technische Zeichnungen und Ersatzteillisten zu lesen.

    In außergewöhnlichen Fällen ist er befugt, die Maschine mit reduzierten Sicherheitseinrichtungen zu betreiben. Wo erforderlich, kann er dem Bediener Anweisungen für die ordnungsgemäße Nutzung der Maschine zu Produktionszwecken geben.

    **Hinweis:** Nicht befugt, an unter Spannung stehenden elektrischen Anlagen zu arbeiten (falls vorhanden).

* - **Elektrofachkraft für die Wartung**
  - Qualifizierter Techniker, der in der Lage ist:
    * vorbeugende/korrektive Wartungsarbeiten an allen mechanischen Teilen der Maschine durchzuführen, die gewartet oder repariert werden müssen;
    * zu allen Teilen der Maschine Zugang zu haben für Sichtprüfung, Kontrolle des Gerätezustands, Einstellungen und Kalibrierungen;
    * die Maschine wie der Bediener zu führen;
    * Einstellungen und elektrische Anlagen für Wartung, Reparatur und Austausch von Verschleißteilen zu bearbeiten;
    * Schaltpläne zu lesen und den korrekten Funktionsablauf zu überprüfen. Wo erforderlich, kann er dem Bediener Anweisungen für die ordnungsgemäße Nutzung der Maschine zu Produktionszwecken geben. Er darf unter Spannung in Schaltschränken, Abzweigdosen, Steuergeräten usw. nur arbeiten, wenn es sich um eine geeignete Person (PEI) handelt. (Siehe Norm **EN50110-1**). Er führt keine Softwareprogrammierung von Systemen wie SPS (Logik oder Sicherheit) durch und darf keine Systempasswörter ändern.

* - **Software-Fachtechniker**
  - Qualifizierter Techniker, der in der Lage ist:
    * vorbeugende/korrektive Tätigkeiten an allen Softwareteilen der Maschine durchzuführen;
    * zu allen Teilen der Maschine Zugang zu haben für Sichtprüfung, Kontrolle des Gerätezustands, Einstellungen und Kalibrierungen. Qualifizierter Techniker des Herstellers mit nachgewiesener Erfahrung und Ausbildung in Systemen auf Basis von: SPS/PC, Antrieben usw. (Kenntnis von Programmierung, Maschinenfunktionen usw.) für komplexe Arbeiten wie zum Beispiel:
    * Änderung von Maschinendaten;
    * Erstellung von Arbeitsprogrammen;
    * Einstellung von Antriebsparametern usw., da er den Produktions-, Technologie- und Konstruktionszyklus der gelieferten Maschine kennt. Er darf unter Spannung in Schaltschränken, Abzweigdosen, Steuergeräten usw. nur arbeiten, wenn es sich um eine geeignete Person (PEI) handelt (siehe Norm **EN50110-1**). Seine Kompetenzen liegen im Bereich Elektronik und/oder Software.

* - **Techniker des Herstellers**
  - Vom Hersteller und/oder seinem Händler qualifizierter Techniker für komplexe Arbeiten, da er den Produktionszyklus beim Bau der Maschine kennt. Diese Person wird entsprechend den Anforderungen des Anwenders tätig. Seine Kompetenzen liegen im mechanischen Bereich.

* - **Unterwiesene Person**
  - Fasst alle in dieser Tabelle aufgeführten Qualifikationen zusammen: Es handelt sich um eine Person, die über die Arbeit und mögliche Gefahren durch unsachgemäße Verwendung informiert, unterwiesen und geschult wurde. Sie kennt außerdem die Bedeutung der Sicherheitseinrichtungen, die Unfallverhütungsvorschriften und die Bedingungen für sicheres Arbeiten.

:::

---

## Hinweise zur Dokumentation

### **Version und Aktualisierungen**

```{note}

- **Referenzsprache**: Die italienische Fassung dieses Dokuments ist die offizielle und hat bei Abweichungen von anderen Übersetzungen Vorrang
- **Aktualisierungen**: Die enthaltenen Informationen können im Zuge von Produktverbesserungen ohne Vorankündigung geändert werden
- **Maßeinheiten**: Sofern nicht anders angegeben, sind alle Abmessungen in Millimetern (mm) angegeben
- **Dokumentversion**: Stets prüfen, ob die aktuellste Version vorliegt, indem die Website [www.flexibowl.it](https://www.flexibowl.it) konsultiert wird
```
### **So nutzen Sie dieses Handbuch optimal**

```{tip}

Für eine optimale Nutzung:
- Das seitliche Navigationsmenü verwenden, um schnell zwischen den Abschnitten zu wechseln
- Das Inhaltsverzeichnis am Anfang konsultieren, um den gewünschten Abschnitt sofort zu finden
- Besondere Aufmerksamkeit den Warn-, Hinweis- und Tipp-Bannern widmen
- Die Verfahren in der angegebenen Reihenfolge befolgen, insbesondere bei der Erstinstallation
- Dieses Handbuch in digitaler Form aufbewahren, um die schnelle Stichwortsuche zu erleichtern
```

---


## Urheberrecht und rechtliche Hinweise

```{important}
**Copyright © ARS S.r.l. - Alle Rechte vorbehalten**

Kein Teil dieser Veröffentlichung darf ohne vorherige schriftliche Genehmigung von ARS S.r.l. für andere Zwecke als den persönlichen Gebrauch auf irgendeine Weise (elektronisch, mechanisch, Fotokopie, Aufzeichnung oder sonstiges Speichersystem) vervielfältigt, verbreitet, übersetzt oder übertragen werden.

ARS S.r.l. lehnt jede Haftung für Folgen ab, die sich aus fehlerhaften Handlungen des Anwenders oder aus unsachgemäßer Verwendung des Produkts ergeben.

**Eingetragene Marken**: FlexiBowl® ist eine eingetragene Marke von ARS S.r.l. Alle anderen in diesem Dokument genannten Marken, Handelsnamen und Logos gehören ihren jeweiligen Eigentümern und werden ausschließlich zu Identifikationszwecken verwendet.
```
---


