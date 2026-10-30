# **Configuration de l'interface**


:::{note}
Si le système utilisé est **FlexiVision One**, la configuration est gérée entièrement par son interface dédiée. Il n'est pas nécessaire d'utiliser l'interface logicielle FlexiBowl® décrite dans cette section. Reportez-vous au {ref}`Manuel FlexiVision One <flexivision_one>`.
:::

## Premier démarrage

Au premier démarrage du système, suivez la procédure guidée ci-dessous pour configurer la communication et préparer le FlexiBowl® à l'utilisation.

::::{list-table}
:widths: 10 90
:header-rows: 1

* - Étape
  - Opération

* - 1
  - Saisissez l'**adresse IP** du FlexiBowl® dans la barre d'adresse du navigateur pour accéder à l'interface logicielle. L'adresse IP par défaut du FlexiBowl® est `192.168.1.10`.

* - 2
  - La **page d'accueil** s'ouvre. Sélectionnez la **langue** souhaitée dans le menu déroulant en haut à droite.

* - 3
  - Ouvrez la page **Setup** depuis le menu latéral.

* - 4
  - Cliquez sur **Get IP** pour lire les paramètres réseau actuels de l'appareil.

* - 5
  - Saisissez dans les champs prévus la **nouvelle adresse IP** que vous souhaitez attribuer au FlexiBowl®, puis cliquez sur **Set IP**.

* - 6
  - Sélectionnez le **type de communication** souhaité dans le menu déroulant. L'option par défaut est **TCP Server**.

    :::{note}
    Le mode **Digital I/O** n'est pas inclus dans la configuration standard, mais est disponible en option, à acheter séparément.
    :::

* - 7
  - Cliquez sur **Apply** pour confirmer les paramètres de communication.

* - 8
  - Cliquez sur **Reboot** pour redémarrer le logiciel et rendre les modifications effectives.

::::

:::{important}
Après le redémarrage, reconnectez-vous au FlexiBowl® en utilisant la nouvelle adresse IP définie à l'étape 5.
:::

## Activation du Backlight (si nécessaire)

Si l'étalonnage du système de vision est requis, activez le rétroéclairage avant de poursuivre :

::::{list-table}
:widths: 10 90
:header-rows: 0

* - 1
  - Ouvrez la page **Main Command** depuis le menu latéral.

* - 2
  - Sélectionnez **OPTION** dans le menu déroulant **« Chose Visualization Page »**.

* - 3
  - Activez l'interrupteur **Backlight 1** et/ou **Backlight 2** selon les besoins.

::::