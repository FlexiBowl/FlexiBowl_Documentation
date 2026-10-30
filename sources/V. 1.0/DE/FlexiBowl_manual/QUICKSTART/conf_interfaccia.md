# **Konfiguration der Benutzeroberfläche**


:::{note}
Wenn das verwendete System **FlexiVision One** ist, erfolgt die Konfiguration vollständig über die zugehörige Oberfläche. Die in diesem Abschnitt beschriebene FlexiBowl®-Software-Oberfläche muss nicht verwendet werden. Siehe {ref}`FlexiVision One Handbuch <flexivision_one>`.
:::

## Erste Inbetriebnahme

Befolgen Sie beim ersten Start des Systems die nachstehende geführte Prozedur, um die Kommunikation zu konfigurieren und den FlexiBowl® für den Einsatz vorzubereiten.

::::{list-table}
:widths: 10 90
:header-rows: 1

* - Schritt
  - Vorgang

* - 1
  - Geben Sie die **IP-Adresse** des FlexiBowl® in die Adressleiste des Browsers ein, um die Software-Oberfläche aufzurufen. Die Standard-IP-Adresse des FlexiBowl® lautet `192.168.1.10`.

* - 2
  - Die **Startseite** wird geöffnet. Wählen Sie im Dropdown-Menü oben rechts die gewünschte **Sprache** aus.

* - 3
  - Öffnen Sie im Seitenmenü die Seite **Setup**.

* - 4
  - Klicken Sie auf **Get IP**, um die aktuellen Netzwerkparameter des Geräts auszulesen.

* - 5
  - Geben Sie in den entsprechenden Feldern die **neue IP-Adresse** ein, die dem FlexiBowl® zugewiesen werden soll, und klicken Sie dann auf **Set IP**.

* - 6
  - Wählen Sie im Dropdown-Menü die gewünschte **Kommunikationsart** aus. Die Standardoption ist **TCP Server**.

    :::{note}
    Der Modus **Digital I/O** ist nicht in der Standardkonfiguration enthalten, ist aber als separat erhältliche Option verfügbar.
    :::

* - 7
  - Klicken Sie auf **Apply**, um die Kommunikationseinstellungen zu bestätigen.

* - 8
  - Klicken Sie auf **Reboot**, um die Software neu zu starten und die Änderungen wirksam zu machen.

::::

:::{important}
Verbinden Sie sich nach dem Neustart mit der in Schritt 5 festgelegten neuen IP-Adresse erneut mit dem FlexiBowl®.
:::

## Backlight aktivieren (falls erforderlich)

Wenn eine Kalibrierung des Bildverarbeitungssystems erforderlich ist, aktivieren Sie die Hintergrundbeleuchtung, bevor Sie fortfahren:

::::{list-table}
:widths: 10 90
:header-rows: 0

* - 1
  - Öffnen Sie im Seitenmenü die Seite **Main Command**.

* - 2
  - Wählen Sie im Dropdown-Menü **„Chose Visualization Page“** den Eintrag **OPTION** aus.

* - 3
  - Aktivieren Sie je nach Bedarf den Schalter **Backlight 1** und/oder **Backlight 2**.

::::