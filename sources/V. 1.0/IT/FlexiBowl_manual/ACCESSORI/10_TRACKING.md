(tracking)=
# **Flexitracking**

## Funzionamento in tracking

L'opzione Flexitracking consente di massimizzare la produttività del FlexiBowl® facendolo girare in maniera continua e senza interruzioni. Invece di fermarsi a ogni ciclo per scattare la foto e dare al robot il tempo di raccogliere i pezzi presenti sull'area di visione, un encoder tiene traccia dell'angolo di rotazione che ha effettuato la superficie o dico rigido dal momento dello scatto della foto e quello della presa del pezzo da parte del robot.

::::{tip}
Il funzionamento in tracking sposta l'area di presa che, se normalmente coincide con quella di visione, in questo caso sarà spostata a valle. Fare riferimento al capitolo di {ref}`Layout Best Practice <layoutbp>` per maggiori informazioni sul piazzamento consigliato del robot e degli altri accessori in caso di funzionamento standard e Flexitracking.

:::{figure} ../../../../_shared/media/images/TrackingLayout.PNG
:width: 80%
:align: center
:::

::::

Il Flexitracking consiste in un gruppo motore modificato con un supporto per una trasmissoine a cinghia che alimenta l'encoder:

:::{figure} ../../../../_shared/media/images/GM001788.PNG
:width: 80%
:align: center
:::

