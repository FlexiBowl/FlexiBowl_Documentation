<style>
.compare-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  margin: 1rem 0 1.5rem;
}
@media (max-width: 680px) {
  .compare-grid { grid-template-columns: 1fr; }
}
.compare-card {
  border: 1px solid #5a9fd4;
  border-radius: 7px;
  overflow: hidden;
  font-size: 0.92rem;
}
.compare-card-header {
  padding: 0.5rem 1rem;
  font-weight: 700;
  font-size: 0.82rem;
  letter-spacing: 0.05em;
  color: #ffffff;
}
.v20 .compare-card-header { background: #1a4a7a; }
.v30 .compare-card-header { background: #1e6fbf; }
.compare-card-body {
  padding: 0.85rem 1rem;
}
.compare-card-body p, .compare-card-body li { margin: 0.25rem 0; }
.compare-card-body ul, .compare-card-body ol { padding-left: 1.2rem; margin: 0.4rem 0; }
.compare-card-body table {
  width: 100%;
  border-collapse: collapse;
  margin: 0.5rem 0;
  font-size: 0.88rem;
}
.compare-card-body table th {
  padding: 0.35rem 0.6rem;
  text-align: left;
  font-size: 0.78rem;
  font-weight: 700;
  border-bottom: 2px solid #5a9fd4;
  opacity: 0.75;
}
.compare-card-body table td {
  padding: 0.35rem 0.6rem;
  border-bottom: 1px solid rgba(90, 159, 212, 0.3);
}
.compare-card-body table tr:last-child td { border-bottom: none; }
</style>

# **Comparativa eléctrica**

Esta página compara las principales diferencias eléctricas entre el **FlexiBowl® 2.0** y el **FlexiBowl® 3.0**, en términos de alimentación, conectividad y seguridad.

:::{important}
Antes de leer el contenido de esta página, es recomendable tener claras las informaciones recogidas en la página [Especificaciones eléctricas y neumáticas](dati_elettrici)
:::

---

## 1. Alimentación

```{list-table}
:header-rows: 1
:widths: 25 37 38

* -
  - FlexiBowl® 2.0
  - FlexiBowl® 3.0
* - **Alimentación AC**
  - 110-220 Vac ±5%
  - 110-230 Vac ±5%
* - **Frecuencia**
  - 50/60 Hz
  - 50/60 Hz
* - **Potencia nominal**
  - 150 W
  - 345-920 W *(según el tamaño del FlexiBowl®)*
* - **Alimentación DC**
  - Generada internamente
  - Generada internamente
```

:::{note}
El FlexiBowl® 3.0 absorbe una potencia nominal superior a la de la generación anterior, ya que la electrónica de accionamiento (drive) está integrada directamente en la unidad.
:::

---

## 2. Conectividad Ethernet

<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0</div>
<div class="compare-card-body">

Conector **RJ45** estándar.

</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0</div>
<div class="compare-card-body">

Conector **M12 codificación D**.

</div>
</div>
</div>

---

## 3. Seguridad

<div class="compare-grid">
<div class="compare-card v20">
<div class="compare-card-header">FlexiBowl® 2.0</div>
<div class="compare-card-body">

Para detener la unidad de forma segura es necesario **desconectar por completo la alimentación de 230 Vac**.

</div>
</div>
<div class="compare-card v30">
<div class="compare-card-header">FlexiBowl® 3.0</div>
<div class="compare-card-body">

<img src="../../../../_shared/media/images/connettore_STO.png" width="110"/>

Función **Safe Torque Off (STO)** integrada, que permite la parada segura sin tener que desconectar la alimentación.

</div>
</div>
</div>

:::{note}
Para los detalles sobre los canales STO y su cableado, consulte la página [Interfaz eléctrica](dati_elettrici).
:::

---

## 4. Resumen

El FlexiBowl® 3.0 absorbe más potencia que la generación anterior debido a la electrónica de accionamiento integrada, pero introduce un conector Ethernet más robusto (M12 codificación D) y una función de seguridad STO integrada, que evita la necesidad de desconectar la alimentación para detener la unidad de forma segura.
