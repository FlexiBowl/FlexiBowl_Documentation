# **FlexiBowl® Wizard**


Die Oberfläche **FlexiBowl® Wizard** ist ein interaktives Werkzeug, das den Benutzer bei der Konfiguration der Zuführparameter entsprechend der jeweiligen zu handhabenden Produktfamilie anleitet.

![Seite Wizard](../../../../_shared/media/images/wizard_home_page.png)

## Schritt 0: Zugriff auf den Wizard

:::{list-table}
* - **1**
  - Um auf die geführte Konfiguration der FlexiBowl®-Parameter zuzugreifen, genügt es, im Seitenmenü auf die Seite **Wizard** zu klicken.
:::

:::{note}
Das FlexiBowl®-Modell und die Drehrichtung werden von der Software automatisch erkannt.
:::

## Schritt 1: Charakterisierung des Bauteils

Das System fragt Informationen zur Morphologie der Teile ab, um die Vereinzelung zu optimieren.
````{list-table}
* - **2**
  - Die Größe des Bauteils auswählen:

    **Für die Modelle FlexiBowl 200, 350, 500, 650:**

    :::{card}
    <= 150mm
    :::

    :::{card}
    &gt; 150mm
    :::

    **Für die Modelle FlexiBowl 800 und 1200:**

    :::{card}
    <= 250mm
    :::

    :::{card}
    &gt; 250mm
    :::

* - **3**
  - Die Geometrie auswählen, die das Bauteil am besten beschreibt:
      * **FLAT**: Flache Bauteile.
      * **CYLINDRICAL**: Zylindrische Bauteile.
      * **COMPLEX**: Komplexe oder unregelmäßige Geometrien

      ![Flat, Cylindrical oder Complex](../../../../_shared/media/images/flatorcomplex.png)

      *Beispiele für Geometrien: Flat, Cylindrical und Complex.*

* - **4**
  - Festlegen, wie die Bauteile auf der Oberfläche miteinander interagieren:
      * **Overlapping**: Die Teile neigen dazu, sich zu überlappen.
      * **Not Overlapping**: Die Teile überlappen sich nicht.
      * **Tangling / Stacking**: Die Teile neigen dazu, sich zu verhaken oder zu stapeln.
      * **Not Tangling / Not Stacking**: Die Teile bleiben getrennt und verhaken sich nicht.

      ![Overlapping](../../../../_shared/media/videos/overlapping.gif)

      *Not Overlapping: Die Teile überlappen sich auf der Oberfläche nicht.*

      ::::{grid} 2
      :::{grid-item}
      ![Stacking](../../../../_shared/media/videos/stacking.gif)

      *Stacking: Die Teile stapeln sich.*
      :::
      :::{grid-item}
      ![Tangling](../../../../_shared/media/videos/tangling.gif)

      *Tangling: Die Teile verhaken sich ineinander.*
      :::
      ::::
````

## Schritt 2: Test der Zubehörteile

```{list-table}
* - **5**
  - Im Dropdown-Menü auswählen, ob der FlexiBowl® mit dem Modul **Air-blow** ausgestattet ist.
* - **6**
  - Auf **TEST Air-blow** klicken, um die Funktion zu überprüfen.
* - **7**
  - **USE** auswählen, um es in der aktuellen Anwendung zu aktivieren, andernfalls auf **DON'T USE** klicken.
* - **8**
  - Klicken Sie auf **TEST FLIP**, um zu prüfen, ob der Schlagbolzen tatsächlich aktiviert wird. Der „Flip“ ist die Einheit, die den mechanischen Impuls zum Wenden der Teile erzeugt, und ist entscheidend, um die Bauteile während des Zuführzyklus zu vereinzeln, zu entwirren oder zu wenden.
 
      :::{important}
      Ist der Impuls nicht spürbar, prüfen, ob die Druckluft angeschlossen ist, und den mechanischen Druckregler am Bedienfeld einstellen.
      :::
* - **9**
  - Klicken Sie am Ende des Wizards auf **FINISH**: Das System berechnet die Parameter automatisch:
    - Bewegungsparameter (Geschwindigkeit, Beschleunigung, Winkel)
    - Shake-Parameter
    - Zeitsteuerungen der Zubehörteile (Flip, Blow)
* - **10**
  - Wählen Sie im Dropdown-Menü die **Sequenz** aus, in der die berechneten Parameter gespeichert werden sollen.
* - **11**
  - Klicken Sie auf **UPDATE SEQUENCE**, um die Parameter in der ausgewählten Sequenz zu speichern.
* - **12**
  - Anschließend können Sie die Parameter auf der Seite **Sequence** feinabstimmen.
```

```{list-table} Parameterübersicht
   :widths: 20 30 50
   :header-rows: 1

   * - Gruppe
     - Parameter
     - Beschreibung
   * - **Move**
     - Accel, Decel, Speed, Angle
     - Parameter der Hauptbewegung der Scheibe.
   * - **Option**
     - Flip Count, Flip Delay, Blow Time
     - Steuerung der Aktivierungszeiten der Zubehörteile.
   * - **Shake**
     - Accel, Speed, Angle CW/CCW
     - Parameter der Schüttelschwingung (Vereinzelung).
```

## Schritt 3: Validierung der Sequenz

Öffnen Sie die Seite **Sequence** und prüfen Sie mit der Schaltfläche **TEST SEQUENCE**, ob der Zyklus die folgenden Effizienzkriterien erfüllt:

```{list-table}
:widths: 5 95
:header-rows: 0

* - **Synchronisierung**
  - Der Flip-Impuls muss genau im selben Moment enden wie die Bewegung (*Move*). Die Werte *Flip Count* und *Delay* anpassen, um beide aufeinander abzustimmen.

* - **Bildstabilität**
  - Die Bauteile müssen im Moment der Kameraaufnahme stillstehen.
    - Wenn sich die Teile bewegen, Geschwindigkeit/Beschleunigung verringern oder eine Pause einfügen (z. B. `pause 200ms`).

* - **Positionierung der Teile während der Sequenz**
  - Während der Bewegung müssen die Teile zur Mitte des Radius des FlexiBowl® befördert werden, um die Wirksamkeit des Flips zu maximieren. Am Ende der Sequenz müssen die Teile ungefähr in der Mitte des Sichtbereichs angeordnet sein.
```

:::{warning}
Nach jeder manuellen Änderung immer auf **Synchronize Parameters** klicken, damit die Änderungen im Controller wirksam werden.
:::
