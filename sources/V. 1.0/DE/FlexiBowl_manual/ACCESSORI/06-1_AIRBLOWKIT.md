# **Air Blow Kit**

:::{note}
Die Implementierung der Blasluft erfordert eine Änderung der Pneumatikanlage des FlexiBowl®; weitere Informationen finden Sie in den {ref}`Pneumatikplänen <sc-pneum>`.
:::

Das Blasluft-Kit (oder *Air Blow Kit*) besteht aus den folgenden Teilen:

## Radiale Blasluft

Die radiale Blasluft besteht aus einer Kartusche, die anstelle des Standard-Abweisers montiert werden kann und zwei radiale Bohrungen in unterschiedlichen Höhen aufweist: Aus einer der beiden, vom Bediener je nach Größe der zu handhabenden Teile gewählt, tritt ein Luftstrahl aus, der die Bauteile vom Rückhaltering entfernt.

:::{figure} ../../../../_shared/media/images/sofrad500.PNG
:width: 100%
:align: center
:::

### Montageverfahren

:::{warning}
Vor der Montage der Blasluft die elektrische Versorgung trennen.
:::

| Schritt | Vorgang |
|:----:|-----------|
| 1 | Die Befestigungsschrauben des Abweisers entfernen |
| 2 | Die Einstellschrauben herausdrehen, um den Abweiser zu entfernen |
| 3 | Die Vollgummidichtung und die gelochte Dichtung entsprechend der gewünschten Blashöhe in die vorgesehenen Aufnahmen einsetzen |
| 4 | Die Kartusche der radialen Blasluft einsetzen und mit den vorgesehenen Schrauben befestigen |

### Einstellverfahren

Die radiale Blasluft lässt sich sowohl per Software als auch mechanisch einstellen, indem mit einem 1,5-mm-Sechskantschlüssel an der dafür vorgesehenen Gewindestift in der Kartusche gedreht wird; dabei ist darauf zu achten, die Position durch Anziehen des Druckstücks mit einem Schlitzschraubendreher zu fixieren.

::::{raw} html
<figure style="text-align: center;">
  <video id="regsof500" width="100%" height="auto" controls>
    <source src="../../../../_shared/media/videos/FB500regsof.mp4" type="video/mp4">
    Ihr Browser unterstützt das Video nicht.
  </video>
  <br>
  <label for="Velsof500">Geschwindigkeit:</label>
  <select id="Velsof500" onchange="document.getElementById('regsof500').playbackRate = this.value">
    <option value="0.5">0.5x</option>
    <option value="1" selected>1x</option>
    <option value="1.5">1.5x</option>
    <option value="2">2x</option>
  </select> 
  <figcaption><i>Mechanisches Einstellverfahren der radialen Blasluft, dargestellt an einem FlexiBowl® 500</i></figcaption>
</figure>
::::

Die Blashöhe kann außerdem gewählt werden, indem die Dichtung mit dem Stopfen unter der Kartusche vertauscht wird:

:::{figure} ../../../../_shared/media/images/sofrad500-sm.PNG
:width: 100%
:align: center
:::

## Zentrale Blasluft

Die zentrale Blasluft besteht aus einer Düse, die an der Spitze des Flip-Schirms montiert ist und deren Luftstrahl so ausgerichtet ist, dass die Bauteile von der Scheibenspannkappe entfernt werden. Sie hat einen doppelten Zweck:

- Die Bauteile über den Flip bringen, um dessen Effizienz zu maximieren;
- Verhindern, dass Bauteile wegen zu großer Nähe zur Scheibenspannkappe als nicht greifbar eingestuft werden, was zu einer Kollision des Roboters führen würde.

:::{figure} ../../../../_shared/media/images/sofcen500.PNG
:width: 100%
:align: center
:::

### Montageverfahren

| Schritt | Vorgang |
|:----:|-----------|
| 1 | Die gesamte Einheit aus Flip-Schirm und Barriere durch Lösen der vier Befestigungsschrauben entfernen |
| 2 | Den Schirm durch die Einheit der zentralen Blasluft ersetzen |
| 3 | Die neue Einheit aus zentraler Blasluft und Flip-Barriere befestigen |

### Einstellverfahren 

Die Intensität der Blasluft wird per Software eingestellt. Außerdem lässt sich durch gleichmäßiges Eindrehen oder Herausdrehen der Einstellgewindestifte der radialen Blasluft der zur zentralen Blasluft gelangende Luftstrom drosseln oder erhöhen.

## Empfohlene Anwendungen

Sie sind dem Standard-Abweiser vorzuziehen, wenn:
- Bauteile gehandhabt werden müssen, die kleine Merkmale oder Vorsprünge aufweisen, die sich im Spalt zwischen Abweiser und Oberfläche bzw. starrer Scheibe verklemmen könnten;
- eine Anti-Roll-Oberfläche oder starre Anti-Roll-Scheibe verwendet wird.

## Überprüfung der korrekten Funktion

Gut eingestellte radiale Blasluft verhält sich wie folgt:

* Die Blasluft vor dem Flip bringt die Bauteile auf etwa die Hälfte des Radius des FlexiBowl®, wo der Flip beim Wenden und Vereinzeln der Teile am wirksamsten ist;

* Die zentrale Blasluft entfernt die Teile von der Scheibenspannkappe, sodass Kollisionen mit dem Greifwerkzeug vermieden werden;

* Die Blasluft nach dem Flip entfernt die Bauteile geringfügig vom Rand des FlexiBowl®, um mögliche Kollisionen mit dem Greifwerkzeug zu verhindern.