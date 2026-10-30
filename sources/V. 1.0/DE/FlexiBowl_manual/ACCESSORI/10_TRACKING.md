(tracking)=
# **Flexitracking**

## Betrieb im Tracking-Modus

Die Option Flexitracking maximiert die Produktivität des FlexiBowl®, indem sie ihn kontinuierlich und ohne Unterbrechung rotieren lässt. Anstatt in jedem Zyklus anzuhalten, um das Bild aufzunehmen und dem Roboter Zeit zu geben, die im Sichtbereich befindlichen Teile zu greifen, erfasst ein Encoder den Drehwinkel, den die Oberfläche bzw. die starre Scheibe zwischen der Bildaufnahme und dem Greifen des Teils durch den Roboter zurückgelegt hat.

::::{tip}
Der Tracking-Betrieb verschiebt den Greifbereich, der normalerweise mit dem Sichtbereich übereinstimmt und in diesem Fall nach unten (in Drehrichtung) verlagert wird. Weitere Informationen zur empfohlenen Platzierung des Roboters und der übrigen Zubehörteile im Standardbetrieb und bei Flexitracking finden Sie im Kapitel {ref}`Layout Best Practice <layoutbp>`.

:::{figure} ../../../../_shared/media/images/TrackingLayout.PNG
:width: 80%
:align: center
:::

::::

Das Flexitracking besteht aus einer modifizierten Motoreinheit mit einer Halterung für einen Riementrieb, der den Encoder antreibt:

:::{figure} ../../../../_shared/media/images/GM001788.PNG
:width: 80%
:align: center
:::

