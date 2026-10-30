
# **Información preliminar general**

```{important}
Antes de instalar, utilizar o realizar el mantenimiento de la máquina, lea atentamente todo el manual y toda la documentación adjunta.

El incumplimiento de las instrucciones indicadas puede causar:
- daños a la máquina;
- pérdida de las condiciones de seguridad;
- riesgos para operadores y personal de mantenimiento;
- la pérdida de la garantía.
```

<script src="https://unpkg.com/@phosphor-icons/web"></script>

<style>
/* ── Variabili e Reset ── */
.isw-page {
  --c-primary:    #1a3a52;
  --c-accent:     #2980b9;
  --c-accent-lt:  #d0e4f0;
  --c-bg:         #ffffff;
  --c-bg-alt:     #f7fbfe;
  --c-bg-hover:   #e8f4fc;
  --c-border:     #d0e4f0;
  --c-text:       #334e5e;
  --c-muted:      #7a9ab0;
  --radius:       10px;
  --shadow-sm:    0 1px 4px rgba(41,128,185,.08);
  --shadow-md:    0 3px 10px rgba(41,128,185,.12);
  max-width: 860px;
  margin: 0 auto;
  padding: 0 0 3rem;
}

/* ── Headings ── */
.isw-page h2 {
  color: var(--c-primary);
  font-weight: 700;
  border-bottom: 2px solid var(--c-accent-lt);
  padding-bottom: .4rem;
  margin-top: 2.5rem;
}
.isw-page h3 {
  color: var(--c-primary);
  font-weight: 600;
  margin-top: 1.6rem;
}

/* ── Meta Grid (Identificazione) ── */
.isw-meta-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1rem;
  margin: 1rem 0 2rem;
}
.isw-meta-card {
  padding: 1.2rem 1.4rem;
  border: 1.5px solid var(--c-border);
  border-radius: var(--radius);
  background: var(--c-bg);
  box-shadow: var(--shadow-sm);
  transition: box-shadow .2s;
}
.isw-meta-card:hover { box-shadow: var(--shadow-md); }

.isw-meta-title {
  font-size: .75rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: .06em;
  color: var(--c-accent);
  margin-bottom: .6rem;
  display: flex;
  align-items: center;
  gap: .4rem;
}
.isw-meta-content {
  font-size: .9rem;
  line-height: 1.6;
  color: var(--c-primary);
}
.isw-meta-content small { color: var(--c-muted); display: block; margin-top: .4rem; line-height: 1.3; }

/* ── Badge modelli ── */
.isw-model-badges {
  display: flex;
  flex-wrap: wrap;
  gap: .4rem;
  margin-top: .5rem;
}
.isw-badge {
  background: var(--c-bg-alt);
  border: 1px solid var(--c-border);
  border-radius: 4px;
  padding: .15rem .55rem;
  font-size: .78rem;
  font-weight: 700;
  color: var(--c-accent);
  font-family: monospace;
}

/* ── Tabelle standard ── */
.isw-table {
  width: 100%;
  border-collapse: collapse;
  font-size: .9rem;
  margin: .75rem 0 1.5rem;
  border-radius: var(--radius);
  overflow: hidden;
  box-shadow: var(--shadow-sm);
}
.isw-table thead th {
  background: var(--c-bg-alt);
  color: var(--c-primary);
  border-bottom: 2px solid var(--c-accent);
  padding: .65rem 1rem;
  text-align: left;
  font-weight: 700;
  font-size: .8rem;
  text-transform: uppercase;
  letter-spacing: .05em;
}
.isw-table tbody tr { transition: background .15s; }
.isw-table tbody tr:nth-child(odd)  { background: var(--c-bg); }
.isw-table tbody tr:nth-child(even) { background: var(--c-bg-alt); }
.isw-table tbody tr:hover { background: var(--c-bg-hover); }
.isw-table td {
  padding: .55rem 1rem;
  border-bottom: 1px solid var(--c-border);
  color: var(--c-text);
  vertical-align: top;
}
.isw-table td:first-child {
  font-family: monospace;
  font-weight: 700;
  color: var(--c-accent);
  white-space: nowrap;
  width: 80px;
}

/* ── Dichiarazione CE ── */
.isw-ce-box {
  background: var(--c-bg-alt);
  border: 1px dashed var(--c-accent-lt);
  border-left: 4px solid var(--c-accent);
  border-radius: var(--radius);
  padding: 1.6rem;
  margin: 1.5rem 0;
}
.isw-ce-header {
  text-align: center;
  font-weight: 700;
  font-size: 1.05rem;
  color: var(--c-primary);
  margin-bottom: 1.2rem;
  letter-spacing: .08em;
  text-transform: uppercase;
}
.isw-ce-box ul { margin: .4rem 0 .8rem 1.2rem; }
.isw-ce-box li { margin-bottom: .2rem; font-size: .88rem; }

.isw-ce-footer {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: .4rem 2rem;
  margin-top: 1.2rem;
  padding-top: 1rem;
  border-top: 1px solid var(--c-border);
  font-size: .85rem;
}

/* ── Tabella Operatori / Profili ── */
.isw-profiles { margin: 1rem 0 1.5rem; display: flex; flex-direction: column; gap: .75rem; }
.isw-profile {
  border: 1.5px solid var(--c-border);
  border-radius: var(--radius);
  overflow: hidden;
  box-shadow: var(--shadow-sm);
}
.isw-profile-header {
  display: flex;
  align-items: center;
  gap: .6rem;
  background: var(--c-bg-alt);
  padding: .6rem 1rem;
  border-bottom: 1px solid var(--c-border);
}
.isw-profile-role {
  font-weight: 700;
  font-size: .85rem;
  color: var(--c-primary);
}
.isw-profile-body {
  padding: .8rem 1rem;
  font-size: .88rem;
  line-height: 1.6;
  color: var(--c-text);
}
.isw-profile-note {
  margin-top: .5rem;
  padding: .4rem .7rem;
  background: #fff8e1;
  border-left: 3px solid #f0b429;
  border-radius: 4px;
  font-size: .82rem;
  color: #7a5c00;
}

/* ── Persona Addestrata callout ── */
.isw-trained-person {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  padding: 1rem 1.2rem;
  border: 1.5px solid var(--c-border);
  border-radius: var(--radius);
  background: var(--c-bg);
  margin: 1rem 0 1.5rem;
  box-shadow: var(--shadow-sm);
}
.isw-trained-person-icon { font-size: 2rem; line-height: 1; flex-shrink: 0; }
.isw-trained-person-title { font-weight: 700; color: var(--c-accent); font-size: .8rem; text-transform: uppercase; letter-spacing: .05em; margin-bottom: .3rem; }

/* ── DPI / Simbologia Grid ── */
.isw-symbol-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
  gap: .75rem;
  margin: 1rem 0 1.5rem;
}
.isw-symbol-item {
  display: flex;
  align-items: flex-start;
  gap: .9rem;
  padding: .8rem 1rem;
  border: 1px solid var(--c-border);
  border-radius: var(--radius);
  background: var(--c-bg);
  transition: box-shadow .2s, background .15s;
}
.isw-symbol-item:hover { background: var(--c-bg-hover); box-shadow: var(--shadow-sm); }
.isw-symbol-item img { width: 52px; height: 52px; object-fit: contain; flex-shrink: 0; }
.isw-symbol-label { font-weight: 700; font-size: .88rem; color: var(--c-primary); margin-bottom: .25rem; }
.isw-symbol-desc  { font-size: .82rem; color: var(--c-text); line-height: 1.4; }

/* ── Rischi residui ── */
.isw-risks { display: flex; flex-direction: column; gap: .75rem; margin: 1rem 0 1.5rem; }
.isw-risk {
  display: grid;
  grid-template-columns: 100px 1fr;
  gap: 0;
  border: 1.5px solid var(--c-border);
  border-radius: var(--radius);
  overflow: hidden;
  box-shadow: var(--shadow-sm);
}
.isw-risk-icons {
  background: var(--c-bg-alt);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: .5rem;
  padding: .8rem;
  border-right: 1px solid var(--c-border);
}
.isw-risk-icons img { width: 44px; height: 44px; object-fit: contain; }
.isw-risk-body { padding: .9rem 1.1rem; }
.isw-risk-title { font-weight: 700; color: var(--c-primary); font-size: .9rem; margin-bottom: .4rem; }
.isw-risk-desc { font-size: .87rem; color: var(--c-text); line-height: 1.55; }
.isw-risk-desc ul { margin: .3rem 0 0 1.1rem; }
.isw-risk-desc li { margin-bottom: .15rem; }

/* ── Zone di sicurezza ── */
.isw-zones { display: flex; flex-direction: column; gap: .6rem; margin: 1rem 0 1.5rem; }
.isw-zone {
  display: grid;
  grid-template-columns: 160px 1fr;
  border: 1.5px solid var(--c-border);
  border-radius: var(--radius);
  overflow: hidden;
}
.isw-zone-label {
  background: var(--c-accent);
  color: #fff;
  font-weight: 700;
  font-size: .8rem;
  padding: .7rem .9rem;
  display: flex;
  align-items: center;
}
.isw-zone:nth-child(2) .isw-zone-label { background: #e67e22; }
.isw-zone:nth-child(3) .isw-zone-label { background: #c0392b; }
.isw-zone-desc { padding: .65rem .9rem; font-size: .87rem; color: var(--c-text); line-height: 1.5; background: var(--c-bg); }

/* ── Garanzia: due colonne ── */
.isw-warranty-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  margin: 1rem 0 1.5rem;
}
@media (max-width: 640px) {
  .isw-warranty-grid { grid-template-columns: 1fr; }
  .isw-risk { grid-template-columns: 1fr; }
  .isw-risk-icons { flex-direction: row; border-right: none; border-bottom: 1px solid var(--c-border); }
  .isw-zone { grid-template-columns: 1fr; }
}
.isw-warranty-col {
  border: 1.5px solid var(--c-border);
  border-radius: var(--radius);
  overflow: hidden;
}
.isw-warranty-col-header {
  padding: .55rem 1rem;
  font-weight: 700;
  font-size: .8rem;
  text-transform: uppercase;
  letter-spacing: .05em;
}
.isw-warranty-col.valid   .isw-warranty-col-header { background: #e8f8f0; color: #1a6b3a; border-bottom: 2px solid #27ae60; }
.isw-warranty-col.invalid .isw-warranty-col-header { background: #fdecea; color: #7b1c1c; border-bottom: 2px solid #c0392b; }
.isw-warranty-col ul { margin: .5rem .5rem .7rem 1.4rem; padding: 0; }
.isw-warranty-col li { font-size: .84rem; color: var(--c-text); margin-bottom: .3rem; line-height: 1.4; }

/* ── Sicurezze inline ── */
.isw-safety-cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: .85rem;
  margin: 1rem 0 1.5rem;
}
.isw-safety-card {
  border: 1.5px solid var(--c-border);
  border-radius: var(--radius);
  padding: 1rem 1.1rem;
  background: var(--c-bg);
}
.isw-safety-card-title {
  font-weight: 700;
  color: var(--c-primary);
  font-size: .88rem;
  margin-bottom: .35rem;
  display: flex;
  align-items: center;
  gap: .4rem;
}
.isw-safety-card p { font-size: .85rem; color: var(--c-text); line-height: 1.5; margin: 0; }
</style>

<div class="isw-page">

## Identificación

<div class="isw-meta-grid">
  <div class="isw-meta-card">
    <div class="isw-meta-title"><i class="ph ph-factory"></i> Fabricante</div>
    <div class="isw-meta-content">
      <strong>ARS S.r.l.</strong><br>
      Via Aretina Nord, 157<br> 52041 – Pieve al Toppo (AR), Italia<br> Tel. +39 0575 398611 &nbsp;·&nbsp; Fax +39 0575 398620<br>
      <a href="mailto:info@arsautomation.com">info@arsautomation.com</a><br>
      <a href="https://www.arsautomation.com" target="_blank">www.arsautomation.com</a>
    </div>
  </div>
  <div class="isw-meta-card">
    <div class="isw-meta-title"><i class="ph ph-cpu"></i> Identificación de la máquina</div>
    <div class="isw-meta-content">
      <strong>Máquina:</strong> Bulk Feeder<br>
      <strong>Modelos base:</strong>
      <div class="isw-model-badges">
        <span class="isw-badge">1,5 l</span>
        <span class="isw-badge">3 l</span>
        <span class="isw-badge">5 l</span>
        <span class="isw-badge">10 l</span>
        <span class="isw-badge">20 l</span>
        <span class="isw-badge">40 l</span>
      </div>
      <small>En algunas aplicaciones pueden existir modelos personalizados. La identificación queda definida por el proyecto de referencia.</small>
    </div>
  </div>
</div>

### Placa de identificación

La máquina está dotada de una placa de identificación situada en la **base vibratoria**. Los datos indicados en la placa deben citarse en toda comunicación con ARS S.r.l.

![Etiqueta del Bulk Feeder](../../../../../_shared/media/images/etichetta_tramoggia.jpg)

<table class="isw-table">
  <thead>
    <tr>
      <th>Pos.</th>
      <th>Elemento de la placa</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>1</td><td>Logotipo del fabricante</td></tr>
    <tr><td>2</td><td>N.º de pieza</td></tr>
    <tr><td>3</td><td>Modelo de la máquina</td></tr>
    <tr><td>4</td><td>Potencia</td></tr>
    <tr><td>5</td><td>Tensión de alimentación</td></tr>
    <tr><td>6</td><td>Año de fabricación</td></tr>
    <tr><td>7</td><td>Grado de protección IP</td></tr>
    <tr><td>8</td><td>N.º de serie</td></tr>
  </tbody>
</table>

```{warning}
**ATENCIÓN — Placa de identificación CE**

Está terminantemente prohibido:
- retirar la placa de identificación CE;
- sustituirla por placas no autorizadas.

Si la placa resultara dañada o fuese retirada por causas accidentales, el cliente está **obligado** a informar inmediatamente al Fabricante.
```

---

## Declaración de conformidad CE (copia)

<div class="isw-ce-box">
  <div class="isw-ce-header">"CE" Declaration of Conformity</div>
  <p style="font-size:.88rem; margin:0 0 .6rem;"><strong>We:</strong> ARS S.r.l. – Via Aretina Nord, 157 – 52041 Pieve al Toppo (AR), Italia</p>
  <p style="font-size:.88rem; margin:0 0 .4rem;">Declare under our exclusive responsibility that the product:</p>
  <p style="font-size:.95rem; font-weight:700; color:#1a3a52; margin:0 0 .8rem;">BULK FEEDER &nbsp;1,5 lt / 3 lt / 5 lt / 10 lt / 20 lt / 40 lt</p>
  <p style="font-size:.88rem; margin:0 0 .4rem;">is compliant with the following standards and regulations:</p>
  <ul>
    <li>DLGS 17/2010</li>
    <li>2006/42/EC – <em>"Partly completed machinery"</em></li>
  </ul>
  <p style="font-size:.85rem; margin:0;">The machinery described above is intended to be incorporated into other machinery and must not be put into service until the relevant machinery into which it is to be incorporated has been declared in conformity with the essential health and safety requirements of Directive 2006/42/EC.</p>
  <div class="isw-ce-footer">
    <div><strong>Lugar:</strong> Arezzo</div>
    <div><strong>Firma:</strong> [Firmado]</div>
    <div><strong>Fecha:</strong> 01-FEB-2019</div>
    <div><strong>Nombre:</strong> Marco Mazzini</div>
  </div>
</div>

---

## Directivas de referencia

La máquina suministrada por ARS S.r.l. no se incluye en las categorías enumeradas en el **Anexo IV** de la Directiva de Máquinas; por lo tanto, se aplica el procedimiento de evaluación de la conformidad con **control interno de la fabricación** (Anexo VIII).

El expediente técnico de construcción se redacta conforme al **Anexo VII** de la Directiva 2006/42/CE y está a disposición de los órganos de vigilancia previa solicitud motivada.

La máquina se comercializa acompañada de:
- Marcado CE
- Declaración CE de conformidad
- Manual de instrucciones y advertencias *(punto 1.7.4 de la Directiva de Máquinas 2006/42/CE)*

<table class="isw-table">
  <thead>
    <tr>
      <th>Directiva</th>
      <th>Descripción / Ámbito</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="font-family:inherit; font-weight:700; color:#1a3a52; width:auto;">2006/42/CE</td>
      <td>Directiva de Máquinas</td>
    </tr>
    <tr>
      <td style="font-family:inherit; font-weight:700; color:#1a3a52;">2014/30/UE</td>
      <td>Directiva de Compatibilidad Electromagnética</td>
    </tr>
  </tbody>
</table>

---

## Destinatarios, suministro y conservación

El manual está destinado a los operadores encargados de utilizar y gestionar la máquina en **todas las fases de su vida técnica**. El manual, junto con el certificado CE, es **parte integrante de la máquina** y debe acompañarla en cada traslado o reventa.

| Aspecto | Prescripción |
|---|---|
| **Integridad** | Conservar íntegro. En caso de pérdida, solicitar inmediatamente una copia al Fabricante. |
| **Cambios de propiedad** | Debe acompañar a la máquina hasta su desguace (traslados, venta, alquiler, arrendamiento). |
| **Formato** | Suministrado en formato electrónico, con anexos (esquemas eléctricos, manuales de subproveedores). |
| **Anexos** | Los manuales adjuntos forman parte constitutiva; se aplican las mismas prescripciones. |
| **Idioma original** | Italiano. En caso de incongruencias con las traducciones, prevalece el texto original. |
| **Actualizaciones** | A cargo del Fabricante. El usuario garantiza que solo se utilicen las versiones actualizadas. |

```{attention}
La empresa fabricante declina toda responsabilidad por el uso indebido de la máquina y/o por los daños causados por operaciones no contempladas en la documentación técnica.
```

---

## Perfiles de los operadores y cualificaciones

<div class="isw-profiles">

  <div class="isw-profile">
    <div class="isw-profile-header">
      <i class="ph ph-user" style="color:#2980b9;font-size:1.1rem;"></i>
      <span class="isw-profile-role">Operador</span>
    </div>
    <div class="isw-profile-body">
      Personal del usuario formado y habilitado para la conducción de la máquina con fines productivos. Realiza las operaciones necesarias para el buen funcionamiento y para su propia integridad. Posee experiencia demostrada y formación específica. En caso de duda, comunica las anomalías a su superior.
      <div class="isw-profile-note">⚠ No está autorizado a realizar ninguna actividad de mantenimiento.</div>
    </div>
  </div>

  <div class="isw-profile">
    <div class="isw-profile-header">
      <i class="ph ph-wrench" style="color:#2980b9;font-size:1.1rem;"></i>
      <span class="isw-profile-role">Mantenedor mecánico</span>
    </div>
    <div class="isw-profile-body">
      Técnico cualificado para actividades preventivas/correctivas en partes mecánicas. Accede a todas las partes de la máquina para el análisis visual, el ajuste y la calibración. Lee esquemas neumáticos/oleohidráulicos, planos técnicos y listas de repuestos. En casos extraordinarios puede operar con seguridades reducidas.
      <div class="isw-profile-note">⚠ No está habilitado para intervenir en instalaciones eléctricas bajo tensión.</div>
    </div>
  </div>

  <div class="isw-profile">
    <div class="isw-profile-header">
      <i class="ph ph-lightning" style="color:#2980b9;font-size:1.1rem;"></i>
      <span class="isw-profile-role">Mantenedor eléctrico</span>
    </div>
    <div class="isw-profile-body">
      Técnico cualificado para el mantenimiento preventivo/correctivo de la instalación eléctrica. Lee los esquemas eléctricos y verifica los ciclos funcionales. Puede trabajar bajo tensión en los cuadros eléctricos <strong>solo si posee la idoneidad PEI (norma EN 50110-1)</strong>.
      <div class="isw-profile-note">⚠ No realiza programación de software (PLC o lógicas de seguridad) y no modifica las contraseñas.</div>
    </div>
  </div>

  <div class="isw-profile">
    <div class="isw-profile-header">
      <i class="ph ph-code" style="color:#2980b9;font-size:1.1rem;"></i>
      <span class="isw-profile-role">Técnico experto en software</span>
    </div>
    <div class="isw-profile-body">
      Técnico del Fabricante con experiencia demostrada en sistemas PLC/PC y accionamientos. Realiza modificaciones de los datos de la máquina, crea programas de trabajo y ajusta los parámetros de los drives. Puede trabajar bajo tensión en los cuadros eléctricos solo si es <strong>persona idónea PEI (EN 50110-1)</strong>.
    </div>
  </div>

  <div class="isw-profile">
    <div class="isw-profile-header">
      <i class="ph ph-star" style="color:#2980b9;font-size:1.1rem;"></i>
      <span class="isw-profile-role">Técnico del Fabricante</span>
    </div>
    <div class="isw-profile-body">
      Técnico especializado y cualificado directamente por ARS S.r.l. (o por el distribuidor) para operaciones de elevada complejidad. Conoce en detalle el ciclo constructivo de la máquina e interviene a petición específica del usuario.
    </div>
  </div>

</div>

Todas las cualificaciones anteriores entran obligatoriamente en la categoría de **«Persona formada»**:

<div class="isw-trained-person">
  <div>
    <div class="isw-trained-person-title">Persona formada</div>
    Persona informada, instruida y formada sobre el trabajo y los peligros derivados de un uso indebido. Conoce la importancia de los dispositivos de seguridad, las normas de prevención de accidentes y las condiciones operativas para trabajar con seguridad.
  </div>
</div>

---

## Simbología de seguridad

<div class="isw-symbol-grid">

  <div class="isw-symbol-item">
    <img src="../../../../../_shared/media/images/simbolo_avvertenza.png" alt="Advertencia">
    <div>
      <div class="isw-symbol-label">Advertencia general</div>
      <div class="isw-symbol-desc">Advertencias cruciales para la seguridad del operador y/o la integridad de la máquina.</div>
    </div>
  </div>

  <div class="isw-symbol-item">
    <img src="../../../../../_shared/media/images/simbolo_elettrico.png" alt="Peligro eléctrico">
    <div>
      <div class="isw-symbol-label">Peligro eléctrico</div>
      <div class="isw-symbol-desc">Señala peligros y riesgos de naturaleza eléctrica (presencia de tensión).</div>
    </div>
  </div>

  <div class="isw-symbol-item">
    <img src="../../../../../_shared/media/images/obbligo_info.png" alt="Información importante">
    <div>
      <div class="isw-symbol-label">Información importante</div>
      <div class="isw-symbol-desc">Información de especial importancia relativa a la gestión operativa del sistema.</div>
    </div>
  </div>

</div>

<style>
.isw-symbol-grid {
  display: flex;
  flex-direction: column; /* Mette i tre blocchi uno sotto l'altro */
  gap: 24px;              /* Crea lo spazio vuoto tra un blocco e l'altro */
}

.isw-symbol-item {
  display: flex;          /* Allinea l'immagine e i testi affiancati dentro la riga */
  align-items: center;    /* Centra verticalmente l'immagine rispetto al testo (opzionale) */
  gap: 15px;              /* Crea spazio tra l'immagine e il testo */
}
</style>

---

## Glosario técnico

<table class="isw-table">
  <thead>
    <tr>
      <th style="width:200px;">Término</th>
      <th>Definición técnica</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Accesorios de elevación</td><td>Componentes no conectados a las máquinas que permiten la sujeción de la carga, dispuestos entre la máquina y la carga (incluidas las eslingas y sus componentes).</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Avería</td><td>Fallo que impide el funcionamiento normal de una máquina o instalación.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Cadenas, cables o correas</td><td>Elementos diseñados para la elevación como parte integrante de máquinas o accesorios de elevación.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Daño</td><td>Cualquier consecuencia negativa derivada de la aparición de un evento peligroso.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">EPI</td><td>Equipo de Protección Individual: productos destinados a salvaguardar la salud y la seguridad de los trabajadores que los llevan.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Máquina</td><td>Conjunto equipado con un sistema de accionamiento compuesto por partes (de las cuales al menos una es móvil), conectadas para una aplicación determinada.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Fallo de funcionamiento</td><td>Funcionamiento defectuoso o inadecuado de una máquina o de uno de sus elementos.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Peligro</td><td>Fuente potencial de daño que, si no se evita, supone un riesgo para la seguridad y la salud.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Protección</td><td>Defensa contra lo que puede causar daño. Puede ser <strong>Activa</strong> (accionada por el operador) o <strong>Pasiva</strong> (interviene sin mando humano).</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Resguardo</td><td>Barrera física, diseñada como parte estructural de la máquina, para proporcionar protección.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Riesgo</td><td>Combinación de la probabilidad y la gravedad de una lesión o un daño para la salud en una situación peligrosa.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Riesgo residual</td><td>Riesgo que permanece tras la adopción de las medidas de protección y prevención en la fase de diseño.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Uso previsto</td><td>Uso de la máquina de conformidad con la información facilitada en las instrucciones de uso.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Uso incorrecto previsible</td><td>Uso no previsto por el diseñador, derivado de un comportamiento humano fácilmente previsible.</td></tr>
  </tbody>
</table>

---

## Equipos de protección individual (EPI) obligatorios

En las fases de proximidad a la máquina (montaje, mantenimiento, ajuste) es obligatorio utilizar los siguientes EPI:

<div class="isw-symbol-grid">
  <div class="isw-symbol-item">
    <img src="../../../../../_shared/media/images/obbligo_guanti.png" alt="Guantes de protección">
    <div>
      <div class="isw-symbol-label">Guantes de protección</div>
      <div class="isw-symbol-desc">Es obligatorio llevar guantes de protección o aislantes para proteger las manos.</div>
    </div>
  </div>
  <div class="isw-symbol-item">
    <img src="../../../../../_shared/media/images/obbligo_occhiali.png" alt="Gafas de protección">
    <div>
      <div class="isw-symbol-label">Gafas de protección</div>
      <div class="isw-symbol-desc">Es obligatorio llevar gafas de protección para salvaguardar los ojos.</div>
    </div>
  </div>
  <div class="isw-symbol-item">
    <img src="../../../../../_shared/media/images/obbligo_antiinf.png" alt="Calzado de seguridad">
    <div>
      <div class="isw-symbol-label">Calzado de seguridad</div>
      <div class="isw-symbol-desc">Es obligatorio llevar calzado de seguridad para proteger los pies.</div>
    </div>
  </div>
  <div class="isw-symbol-item">
    <img src="../../../../../_shared/media/images/obbligo_rumore.png" alt="Protección contra el ruido">
    <div>
      <div class="isw-symbol-label">Protección contra el ruido</div>
      <div class="isw-symbol-desc">Es obligatorio llevar orejeras o tapones para proteger el oído.</div>
    </div>
  </div>
  <div class="isw-symbol-item">
    <img src="../../../../../_shared/media/images/obbligo_indumenti.png" alt="Ropa de protección">
    <div>
      <div class="isw-symbol-label">Ropa de protección</div>
      <div class="isw-symbol-desc">Es obligatorio llevar la ropa de trabajo de protección específica.</div>
    </div>
  </div>
  <div class="isw-symbol-item">
    <img src="../../../../../_shared/media/images/obbligo_manuale.png" alt="Consulte el manual">
    <div>
      <div class="isw-symbol-label">Consulte el manual</div>
      <div class="isw-symbol-desc">Es obligatorio leer y comprender las instrucciones de uso antes de cualquier actividad.</div>
    </div>
  </div>
  <div class="isw-symbol-item">
    <img src="../../../../../_shared/media/images/obbligo_casco.png" alt="Casco de protección">
    <div>
      <div class="isw-symbol-label">Casco de protección</div>
      <div class="isw-symbol-desc">Es obligatorio llevar casco para proteger la cabeza.</div>
    </div>
  </div>
</div>

```{warning}
**ROPA DE SEGURIDAD**

La ropa del personal debe cumplir los requisitos esenciales previstos por el **Reglamento UE 2016/425** y las leyes vigentes en el país de instalación. El incumplimiento puede comprometer la seguridad del operador y de las personas expuestas.
```

---

## Mapa de las áreas de seguridad

<div class="isw-zones">
  <div class="isw-zone">
    <div class="isw-zone-label">Zonas de mando</div>
    <div class="isw-zone-desc">Áreas en las que el operador controla las funciones cíclicas (en modo automático o semiautomático) mediante los paneles dedicados.</div>
  </div>
  <div class="isw-zone">
    <div class="isw-zone-label">Zonas de mantenimiento / ajuste</div>
    <div class="isw-zone-desc">Accesibles solo para mantenedores mecánicos y eléctricos cualificados para operaciones de configuración. Permanecen vedadas durante el ciclo de producción estándar.</div>
  </div>
  <div class="isw-zone">
    <div class="isw-zone-label">Zonas peligrosas</div>
    <div class="isw-zone-desc">Áreas internas o perimetrales de la máquina con riesgos residuales. <strong>Está categóricamente prohibido el acceso a cualquier persona cuando la máquina está en funcionamiento.</strong></div>
  </div>
</div>

```{warning}
**ACCESO A ZONAS PELIGROSAS**

Los riesgos en las zonas de la máquina están protegidos mediante resguardos físicos (carcasas, puertas) y dispositivos eléctricos con enclavamiento (sensores, microinterruptores).

Cuando el sistema está activo está terminantemente prohibido:
- saltar por encima de las protecciones;
- puentear los dispositivos de seguridad;
- intervenir dentro de las áreas protegidas.

La retirada o la elusión de los sistemas de seguridad puede causar lesiones graves a las personas y daños a la máquina.
```

---

## Condiciones y límites de la garantía

Las cláusulas completas se establecen en el contrato de venta, cuyas condiciones tienen siempre prioridad sobre este manual.

<div class="isw-warranty-grid">
  <div class="isw-warranty-col valid">
    <div class="isw-warranty-col-header">✔ Condiciones de validez</div>
    <ul>
      <li>Apertura de los embalajes realizada con medios adecuados sin daños a los sistemas.</li>
      <li>Instalación y puesta en marcha realizadas en presencia de técnicos habilitados.</li>
      <li>Uso dentro de los límites nominales declarados en el contrato.</li>
      <li>Mantenimiento en los plazos establecidos con <strong>repuestos originales ARS S.r.l.</strong> encomendado a personal cualificado.</li>
    </ul>
  </div>
  <div class="isw-warranty-col invalid">
    <div class="isw-warranty-col-header">✘ Causas de caducidad inmediata</div>
    <ul>
      <li>Incumplimiento de las normas de seguridad o de las instrucciones.</li>
      <li>Instalación o uso en entornos no adecuados.</li>
      <li>Retirada o manipulación de dispositivos de control y seguridad.</li>
      <li>Retirada o alteración de la placa CE o de los pictogramas.</li>
      <li>Modificaciones no autorizadas del software (PLC, lógicas, contraseñas).</li>
      <li>Uso indebido o encomienda a personal no autorizado.</li>
      <li>Modificaciones mecánicas/eléctricas/neumáticas sin autorización por escrito del Fabricante.</li>
      <li>Anomalías en el suministro de la energía de alimentación.</li>
      <li>Falta de ejecución del plan de mantenimiento programado.</li>
      <li>Eliminación final en infracción de la normativa medioambiental vigente.</li>
    </ul>
  </div>
</div>

---

## Seguridades

<div class="isw-safety-cards">

  <div class="isw-safety-card">
    <div class="isw-safety-card-title"><i class="ph ph-speaker-high"></i> Ruido</div>
    <p>Mediciones realizadas según UNI EN 11200 y UNI EN ISO 3746. La exposición al ruido durante el funcionamiento es igual a <strong>90 dB</strong>. El nivel real en el lugar puede variar en función del tipo de instalación, de las máquinas adyacentes y de las características del entorno.</p>
  </div>

  <div class="isw-safety-card">
    <div class="isw-safety-card-title"><i class="ph ph-wave-sine"></i> Vibraciones</div>
    <p>Las vibraciones producidas por la máquina en condiciones normales de funcionamiento no son peligrosas para la salud de los operadores. Una vibración excesiva es síntoma de una avería mecánica y debe comunicarse y eliminarse inmediatamente.</p>
  </div>

  <div class="isw-safety-card">
    <div class="isw-safety-card-title"><i class="ph ph-broadcast"></i> Compatibilidad electromagnética</div>
    <p>La máquina cumple la Directiva EMC. Los valores de emisión se mantienen dentro de los límites normativos gracias al uso de componentes certificados, conexiones adecuadas y filtros cuando es necesario. Intervenciones de mantenimiento no conformes o sustituciones erróneas de componentes pueden comprometer dicha conformidad.</p>
  </div>

</div>

<style>
.isw-safety-cards {
  display: flex;
  flex-direction: column; 
  gap: 20px;              
}
</style>

```{attention}
**OBLIGACIÓN** — Es obligatorio utilizar los equipos de protección individual durante el funcionamiento de la máquina.
```

### Riesgos residuales

El diseño de la máquina se ha realizado para garantizar los requisitos esenciales de seguridad; sin embargo, permanecen riesgos residuales en las fases de:
- transporte e instalación
- funcionamiento normal
- ajuste y puesta a punto
- mantenimiento y limpieza
- desmontaje y desmantelamiento

<div class="isw-risks">

  <div class="isw-risk">
    <div class="isw-risk-icons">
      <img src="../../../../../_shared/media/images/simbolo_avvertenza.png" alt="">
      <img src="../../../../../_shared/media/images/pericolo_movimento.png" alt="">
      <img src="../../../../../_shared/media/images/pericolo_spazi.png" alt="">
    </div>
    <div class="isw-risk-body">
      <div class="isw-risk-title">Peligros debidos a la manipulación</div>
      <div class="isw-risk-desc">
        Las operaciones de descarga, apertura de embalajes y manipulación de la máquina exponen a los operadores al riesgo de <strong>cargas suspendidas y aplastamiento</strong>. Deben ser realizadas exclusivamente por personal especializado en la conducción de medios de elevación y específicamente formado.
        <br><br>Los procedimientos detallados se describen en el capítulo <em>«Transporte e instalación»</em>.
      </div>
    </div>
  </div>

  <div class="isw-risk">
    <div class="isw-risk-icons">
      <img src="../../../../../_shared/media/images/simbolo_avvertenza.png" alt="">
      <img src="../../../../../_shared/media/images/simbolo_elettrico.png" alt="">
    </div>
    <div class="isw-risk-body">
      <div class="isw-risk-title">Peligro eléctrico</div>
      <div class="isw-risk-desc">
        Las operaciones de acceso y mantenimiento exponen al riesgo eléctrico. Las intervenciones bajo tensión deben ser realizadas exclusivamente por personal experto y cualificado. Medidas de seguridad:
        <ul>
          <li>Respete los pictogramas de seguridad relativos al riesgo eléctrico.</li>
          <li>No realice mantenimiento sin haber seccionado previamente la alimentación.</li>
          <li>Consulte los manuales de los equipos comerciales para obtener recomendaciones específicas.</li>
          <li>Inspeccione periódicamente el circuito de protección equipotencial.</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="isw-risk">
    <div class="isw-risk-icons">
      <img src="../../../../../_shared/media/images/simbolo_avvertenza.png" alt="">
    </div>
    <div class="isw-risk-body">
      <div class="isw-risk-title">Peligro por polvo y astillas</div>
      <div class="isw-risk-desc">
        Al final del ciclo de trabajo pueden quedar en la superficie de la máquina residuos de las piezas alimentadas o acumulaciones de polvo. Limpie a fondo la superficie vibratoria después de cada uso (véase cap. 7).
      </div>
    </div>
  </div>

</div>

```{attention}
No realice actividades de mantenimiento y limpieza sin haber desenergizado previamente todas las fuentes de energía presentes.
```

```{attention}
Está terminantemente prohibido retirar las protecciones de seguridad o abrir los resguardos fijos sin haber seccionado previamente la alimentación eléctrica y neumática de la máquina.
```

El usuario está obligado a:
- analizar los riesgos de manipulación e instalación dentro de sus propias instalaciones;
- sensibilizar e instruir al personal encargado de las operaciones;
- aplicar las señalizaciones visuales de seguridad en el entorno de trabajo.

</div>