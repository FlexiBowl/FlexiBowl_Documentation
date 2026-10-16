
# **General Preliminary Information**

```{important}
Before installing, using or performing maintenance on the machine, carefully read the entire manual and all the attached documentation.

Failure to comply with the instructions given may cause:
- damage to the machine;
- loss of safety conditions;
- risks for operators and maintenance technicians;
- voiding of the warranty.
```

<script src="https://unpkg.com/@phosphor-icons/web"></script>

<style>
/* ── Variables and Reset ── */
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

/* ── Meta Grid (Identification) ── */
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

/* ── Model badges ── */
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

/* ── Standard tables ── */
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

/* ── CE Declaration ── */
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

/* ── Operators / Profiles table ── */
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

/* ── Trained Person callout ── */
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

/* ── PPE / Symbols Grid ── */
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

/* ── Residual risks ── */
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

/* ── Safety zones ── */
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

/* ── Warranty: two columns ── */
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

/* ── Inline safety ── */
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

## Identification

<div class="isw-meta-grid">
  <div class="isw-meta-card">
    <div class="isw-meta-title"><i class="ph ph-factory"></i> Manufacturer</div>
    <div class="isw-meta-content">
      <strong>ARS S.r.l.</strong><br>
      Via Aretina Nord, 157<br>
      52041 – Pieve al Toppo (AR), Italy<br>
      Tel. +39 0575 398611 &nbsp;·&nbsp; Fax +39 0575 398620<br>
      <a href="mailto:info@arsautomation.com">info@arsautomation.com</a><br>
      <a href="https://www.arsautomation.com" target="_blank">www.arsautomation.com</a>
    </div>
  </div>
  <div class="isw-meta-card">
    <div class="isw-meta-title"><i class="ph ph-cpu"></i> Machine Identification</div>
    <div class="isw-meta-content">
      <strong>Machine:</strong> Hopper<br>
      <strong>Base models:</strong>
      <div class="isw-model-badges">
        <span class="isw-badge">1.5 l</span>
        <span class="isw-badge">3 l</span>
        <span class="isw-badge">5 l</span>
        <span class="isw-badge">10 l</span>
        <span class="isw-badge">20 l</span>
        <span class="isw-badge">40 l</span>
      </div>
      <small>In some applications custom models may exist. Identification is defined by the reference project.</small>
    </div>
  </div>
</div>

### Identification Plate

The machine is fitted with an identification plate located on the **vibrating base**. The details shown on the plate must be quoted in every communication with ARS S.r.l.

![Hopper label](../../../../../_shared/media/images/etichetta_tramoggia.jpg)

<table class="isw-table">
  <thead>
    <tr>
      <th>Pos.</th>
      <th>Item on the plate</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>1</td><td>Manufacturer logo</td></tr>
    <tr><td>2</td><td>Part No.</td></tr>
    <tr><td>3</td><td>Machine model</td></tr>
    <tr><td>4</td><td>Power</td></tr>
    <tr><td>5</td><td>Supply voltage</td></tr>
    <tr><td>6</td><td>Year of construction</td></tr>
    <tr><td>7</td><td>IP protection rating</td></tr>
    <tr><td>8</td><td>Serial No.</td></tr>
  </tbody>
</table>

```{warning}
**WARNING — CE identification plate**

It is absolutely forbidden to:
- remove the CE identification plate;
- replace it with unauthorized plates.

If the plate is damaged or removed accidentally, the customer is **obliged** to inform the Manufacturer immediately.
```

---

## CE Declaration of Conformity (Copy)

<div class="isw-ce-box">
  <div class="isw-ce-header">"CE" Declaration of Conformity</div>
  <p style="font-size:.88rem; margin:0 0 .6rem;"><strong>We:</strong> ARS S.r.l. – Via Aretina Nord, 157 – 52041 Pieve al Toppo (AR), Italy</p>
  <p style="font-size:.88rem; margin:0 0 .4rem;">Declare under our exclusive responsibility that the product:</p>
  <p style="font-size:.95rem; font-weight:700; color:#1a3a52; margin:0 0 .8rem;">BULK FEEDER &nbsp;1.5 l / 3 l / 5 l / 10 l / 20 l / 40 l</p>
  <p style="font-size:.88rem; margin:0 0 .4rem;">is compliant with the following standards and regulations:</p>
  <ul>
    <li>DLGS 17/2010</li>
    <li>2006/42/EC – <em>"Partly completed machinery"</em></li>
  </ul>
  <p style="font-size:.85rem; margin:0;">The machinery described above is intended to be incorporated into other machinery and must not be put into service until the relevant machinery into which it is to be incorporated has been declared in conformity with the essential health and safety requirements of Directive 2006/42/EC.</p>
  <div class="isw-ce-footer">
    <div><strong>Place:</strong> Arezzo</div>
    <div><strong>Signature:</strong> [Signed]</div>
    <div><strong>Date:</strong> 01-FEB-2019</div>
    <div><strong>Name:</strong> Marco Mazzini</div>
  </div>
</div>

---

## Reference Directives

The machine supplied by ARS S.r.l. does not fall within the categories listed in **Annex IV** of the Machinery Directive; the conformity assessment procedure with **internal checks on manufacturing** (Annex VIII) therefore applies.

The technical construction file is drawn up in accordance with **Annex VII** of Directive 2006/42/EC and is available to the supervisory authorities upon reasoned request.

The machine is placed on the market accompanied by:
- CE marking
- CE Declaration of Conformity
- Instruction manual and warnings *(point 1.7.4 of the Machinery Directive 2006/42/EC)*

<table class="isw-table">
  <thead>
    <tr>
      <th>Directive</th>
      <th>Description / Scope</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="font-family:inherit; font-weight:700; color:#1a3a52; width:auto;">2006/42/EC</td>
      <td>Machinery Directive</td>
    </tr>
    <tr>
      <td style="font-family:inherit; font-weight:700; color:#1a3a52;">2014/30/EU</td>
      <td>Electromagnetic Compatibility Directive</td>
    </tr>
  </tbody>
</table>

---

## Recipients, Supply and Storage

The manual is intended for the operators in charge of using and managing the machine in **all phases of its technical life**. The manual, together with the CE certificate, is an **integral part of the machine** and must accompany it in every relocation or resale.

| Aspect | Requirement |
|---|---|
| **Integrity** | Keep intact. If lost, immediately request a copy from the Manufacturer. |
| **Changes of ownership** | Must follow the machine until its demolition (relocation, sale, rental, lease). |
| **Format** | Supplied in electronic format, with attachments (electrical diagrams, sub-supplier manuals). |
| **Attachments** | The attached manuals are an integral part; the same requirements apply. |
| **Original language** | Italian. In case of inconsistencies with the translations, the original text prevails. |
| **Updates** | Provided by the Manufacturer. The user ensures that only updated versions are in use. |

```{attention}
The Manufacturer declines all liability for improper use of the machine and/or for damage caused by operations not covered in the technical documentation.
```

---

## Operator Profiles and Qualifications

<div class="isw-profiles">

  <div class="isw-profile">
    <div class="isw-profile-header">
      <i class="ph ph-user" style="color:#2980b9;font-size:1.1rem;"></i>
      <span class="isw-profile-role">Operator</span>
    </div>
    <div class="isw-profile-body">
      User's personnel trained and authorized to operate the machine for production purposes. Performs the operations necessary for proper operation and for their own safety. Has proven experience and specific training. In case of doubt, reports anomalies to their superior.
      <div class="isw-profile-note">⚠ Not authorized to carry out any maintenance activity.</div>
    </div>
  </div>

  <div class="isw-profile">
    <div class="isw-profile-header">
      <i class="ph ph-wrench" style="color:#2980b9;font-size:1.1rem;"></i>
      <span class="isw-profile-role">Mechanical Maintenance Technician</span>
    </div>
    <div class="isw-profile-body">
      Technician qualified for preventive/corrective activities on mechanical parts. Accesses all parts of the machine for visual analysis, adjustment and calibration. Reads pneumatic/hydraulic diagrams, technical drawings and spare parts lists. In extraordinary cases may operate with reduced safety devices.
      <div class="isw-profile-note">⚠ Not authorized to work on live electrical systems.</div>
    </div>
  </div>

  <div class="isw-profile">
    <div class="isw-profile-header">
      <i class="ph ph-lightning" style="color:#2980b9;font-size:1.1rem;"></i>
      <span class="isw-profile-role">Electrical Maintenance Technician</span>
    </div>
    <div class="isw-profile-body">
      Technician qualified for preventive/corrective maintenance on the electrical system. Reads the electrical diagrams and verifies the functional cycles. May work on live electrical panels <strong>only if holding PEI qualification (Standard EN 50110-1)</strong>.
      <div class="isw-profile-note">⚠ Does not perform software programming (PLC or safety logic) and does not change passwords.</div>
    </div>
  </div>

  <div class="isw-profile">
    <div class="isw-profile-header">
      <i class="ph ph-code" style="color:#2980b9;font-size:1.1rem;"></i>
      <span class="isw-profile-role">Software Expert Technician</span>
    </div>
    <div class="isw-profile-body">
      Manufacturer's technician with proven experience on PLC/PC systems and drives. Performs changes to machine data, creation of work programs and adjustment of drive parameters. May work on live electrical panels only if a <strong>PEI-qualified person (EN 50110-1)</strong>.
    </div>
  </div>

  <div class="isw-profile">
    <div class="isw-profile-header">
      <i class="ph ph-star" style="color:#2980b9;font-size:1.1rem;"></i>
      <span class="isw-profile-role">Manufacturer's Technician</span>
    </div>
    <div class="isw-profile-body">
      Technician specialized and qualified directly by ARS S.r.l. (or by the distributor) for highly complex operations. Knows the construction cycle of the machine in detail and intervenes at the specific request of the user.
    </div>
  </div>

</div>

All the above qualifications necessarily fall within the category of **"Trained Person"**:

<div class="isw-trained-person">
  <div>
    <div class="isw-trained-person-title">Trained Person</div>
    A person informed, instructed and trained on the work and on the hazards arising from improper use. Knows the importance of safety devices, accident-prevention rules and the operating conditions for working safely.
  </div>
</div>

---

## Safety Symbols

<div class="isw-symbol-grid">

  <div class="isw-symbol-item">
    <img src="../../../../../_shared/media/images/simbolo_avvertenza.png" alt="Warning">
    <div>
      <div class="isw-symbol-label">General warning</div>
      <div class="isw-symbol-desc">Crucial warnings for operator safety and/or machine integrity.</div>
    </div>
  </div>

  <div class="isw-symbol-item">
    <img src="../../../../../_shared/media/images/simbolo_elettrico.png" alt="Electrical hazard">
    <div>
      <div class="isw-symbol-label">Electrical hazard</div>
      <div class="isw-symbol-desc">Indicates hazards and risks of an electrical nature (presence of voltage).</div>
    </div>
  </div>

  <div class="isw-symbol-item">
    <img src="../../../../../_shared/media/images/obbligo_info.png" alt="Important information">
    <div>
      <div class="isw-symbol-label">Important information</div>
      <div class="isw-symbol-desc">Information of particular importance relating to the operational management of the system.</div>
    </div>
  </div>

</div>

<style>
.isw-symbol-grid {
  display: flex;
  flex-direction: column; /* Stacks the three blocks one below the other */
  gap: 24px;              /* Creates the empty space between one block and the next */
}

.isw-symbol-item {
  display: flex;          /* Aligns the image and the texts side by side inside the row */
  align-items: center;    /* Vertically centers the image relative to the text (optional) */
  gap: 15px;              /* Creates space between the image and the text */
}
</style>

---

## Technical Glossary

<table class="isw-table">
  <thead>
    <tr>
      <th style="width:200px;">Term</th>
      <th>Technical Definition</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Lifting accessories</td><td>Components not connected to machines that allow the load to be gripped, placed between the machine and the load (including slings and their components).</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Breakdown</td><td>Failure that prevents the normal operation of a machine or a plant.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Chains, ropes or belts</td><td>Elements designed for lifting as an integral part of machines or lifting accessories.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Damage</td><td>Any negative consequence arising from the occurrence of a hazardous event.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">PPE</td><td>Personal Protective Equipment: products designed to safeguard the health and safety of the workers who wear them.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Machine</td><td>Assembly equipped with a drive system, made up of parts (at least one of which is movable), connected for a specific application.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Malfunction</td><td>Defective or inadequate operation of a machine or of one of its elements.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Hazard</td><td>Potential source of harm that, if not avoided, entails a risk to safety and health.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Protection</td><td>Defense against what may cause harm. It can be <strong>Active</strong> (operated by the operator) or <strong>Passive</strong> (acts without human command).</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Guard</td><td>Physical barrier, designed as a structural part of the machine, to provide protection.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Risk</td><td>Combination of the probability and the severity of an injury or damage in a hazardous situation.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Residual risk</td><td>Risk that remains after the protection and prevention measures have been adopted at the design stage.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Intended use</td><td>Use of the machine in accordance with the information provided in the instructions for use.</td></tr>
    <tr><td style="font-family:inherit;font-weight:700;color:#1a3a52;">Reasonably foreseeable misuse</td><td>Use not intended by the designer, resulting from easily foreseeable human behavior.</td></tr>
  </tbody>
</table>

---

## Mandatory Personal Protective Equipment (PPE)

When working close to the machine (assembly, maintenance, adjustment) the following PPE must be used:

<div class="isw-symbol-grid">
  <div class="isw-symbol-item">
    <img src="../../../../../_shared/media/images/obbligo_guanti.png" alt="Protective gloves">
    <div>
      <div class="isw-symbol-label">Protective gloves</div>
      <div class="isw-symbol-desc">Protective or insulating gloves must be worn to protect the hands.</div>
    </div>
  </div>
  <div class="isw-symbol-item">
    <img src="../../../../../_shared/media/images/obbligo_occhiali.png" alt="Safety glasses">
    <div>
      <div class="isw-symbol-label">Safety glasses</div>
      <div class="isw-symbol-desc">Protective glasses must be worn to safeguard the eyes.</div>
    </div>
  </div>
  <div class="isw-symbol-item">
    <img src="../../../../../_shared/media/images/obbligo_antiinf.png" alt="Safety shoes">
    <div>
      <div class="isw-symbol-label">Safety shoes</div>
      <div class="isw-symbol-desc">Safety shoes must be worn to protect the feet.</div>
    </div>
  </div>
  <div class="isw-symbol-item">
    <img src="../../../../../_shared/media/images/obbligo_rumore.png" alt="Hearing protection">
    <div>
      <div class="isw-symbol-label">Hearing protection</div>
      <div class="isw-symbol-desc">Earmuffs or earplugs must be worn to protect hearing.</div>
    </div>
  </div>
  <div class="isw-symbol-item">
    <img src="../../../../../_shared/media/images/obbligo_indumenti.png" alt="Protective clothing">
    <div>
      <div class="isw-symbol-label">Protective clothing</div>
      <div class="isw-symbol-desc">The specific protective work clothing must be worn.</div>
    </div>
  </div>
  <div class="isw-symbol-item">
    <img src="../../../../../_shared/media/images/obbligo_manuale.png" alt="Consult the manual">
    <div>
      <div class="isw-symbol-label">Consult the Manual</div>
      <div class="isw-symbol-desc">The instructions for use must be read and understood before any activity.</div>
    </div>
  </div>
  <div class="isw-symbol-item">
    <img src="../../../../../_shared/media/images/obbligo_casco.png" alt="Safety helmet">
    <div>
      <div class="isw-symbol-label">Safety helmet</div>
      <div class="isw-symbol-desc">A helmet must be worn to protect the head.</div>
    </div>
  </div>
</div>

```{warning}
**SAFETY CLOTHING**

Personnel clothing must comply with the essential requirements of **Regulation (EU) 2016/425** and with the laws in force in the country of installation. Failure to comply may compromise the safety of the operator and of exposed persons.
```

---

## Safety Area Mapping

<div class="isw-zones">
  <div class="isw-zone">
    <div class="isw-zone-label">Control zones</div>
    <div class="isw-zone-desc">Areas in which the operator controls the cyclic functions (in automatic or semi-automatic mode) by means of the dedicated panels.</div>
  </div>
  <div class="isw-zone">
    <div class="isw-zone-label">Maintenance / adjustment zones</div>
    <div class="isw-zone-desc">Accessible only to qualified mechanical and electrical maintenance technicians for setting operations. They remain off-limits during the standard production cycle.</div>
  </div>
  <div class="isw-zone">
    <div class="isw-zone-label">Danger zones</div>
    <div class="isw-zone-desc">Areas inside or around the machine with residual risks. <strong>Access is categorically forbidden to anyone when the machine is running.</strong></div>
  </div>
</div>

```{warning}
**ACCESS TO DANGER ZONES**

The risks in the machine zones are protected by physical guards (covers, doors) and interlocked electrical devices (sensors, microswitches).

When the system is active it is strictly forbidden to:
- climb over the guards;
- bypass the safety devices;
- intervene inside the protected areas.

Removing or circumventing the safety systems may cause serious injury to persons and damage to the machine.
```

---

## Warranty Conditions and Limits

The full clauses are set out in the sales contract, whose conditions always take priority over this manual.

<div class="isw-warranty-grid">
  <div class="isw-warranty-col valid">
    <div class="isw-warranty-col-header">✔ Conditions for validity</div>
    <ul>
      <li>Packaging opened with suitable means without damage to the systems.</li>
      <li>Installation and start-up carried out in the presence of authorized technicians.</li>
      <li>Use within the nominal limits declared in the contract.</li>
      <li>Maintenance at the scheduled times with <strong>original ARS S.r.l. spare parts</strong> entrusted to qualified personnel.</li>
    </ul>
  </div>
  <div class="isw-warranty-col invalid">
    <div class="isw-warranty-col-header">✘ Causes of immediate forfeiture</div>
    <ul>
      <li>Failure to comply with the safety rules or the instructions.</li>
      <li>Installation or use in unsuitable environments.</li>
      <li>Removal of or tampering with control and safety devices.</li>
      <li>Removal or alteration of the CE plate or of the pictograms.</li>
      <li>Unauthorized changes to the software (PLC, logic, passwords).</li>
      <li>Improper use or entrusting to unauthorized personnel.</li>
      <li>Mechanical/electrical/pneumatic modifications without the written authorization of the Manufacturer.</li>
      <li>Anomalies in the supply of power.</li>
      <li>Failure to implement the scheduled maintenance plan.</li>
      <li>Final disposal in violation of the environmental regulations in force.</li>
    </ul>
  </div>
</div>

---

## Safety

<div class="isw-safety-cards">

  <div class="isw-safety-card">
    <div class="isw-safety-card-title"><i class="ph ph-speaker-high"></i> Noise</div>
    <p>Measurements carried out in accordance with UNI EN 11200 and UNI EN ISO 3746. Noise exposure during operation is <strong>90 dB</strong>. The actual level on site may vary depending on the type of installation, the adjacent machines and the characteristics of the environment.</p>
  </div>

  <div class="isw-safety-card">
    <div class="isw-safety-card-title"><i class="ph ph-wave-sine"></i> Vibrations</div>
    <p>The vibrations produced by the machine under normal operating conditions are not hazardous to the health of the operators. Excessive vibration is a symptom of mechanical failure and must be reported and eliminated immediately.</p>
  </div>

  <div class="isw-safety-card">
    <div class="isw-safety-card-title"><i class="ph ph-broadcast"></i> Electromagnetic Compatibility</div>
    <p>The machine complies with the EMC Directive. Emission values fall within the regulatory limits thanks to the use of certified components, suitable connections and filters where necessary. Non-compliant maintenance work or incorrect replacement of components may compromise this compliance.</p>
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
**MANDATORY** — Personal protective equipment must be used while the machine is operating.
```

### Residual Risks

The machine has been designed to guarantee the essential safety requirements; however, residual risks remain in the following phases:
- transport and installation
- normal operation
- adjustment and setup
- maintenance and cleaning
- disassembly and dismantling

<div class="isw-risks">

  <div class="isw-risk">
    <div class="isw-risk-icons">
      <img src="../../../../../_shared/media/images/simbolo_avvertenza.png" alt="">
      <img src="../../../../../_shared/media/images/pericolo_movimento.png" alt="">
      <img src="../../../../../_shared/media/images/pericolo_spazi.png" alt="">
    </div>
    <div class="isw-risk-body">
      <div class="isw-risk-title">Hazards due to handling</div>
      <div class="isw-risk-desc">
        The operations of unloading, opening the packaging and handling the machine expose operators to the risk of <strong>suspended loads and crushing</strong>. They must be carried out exclusively by personnel specialized in operating lifting equipment and specifically trained.
        <br><br>The detailed procedures are described in the <em>"Transport and Installation"</em> chapter.
      </div>
    </div>
  </div>

  <div class="isw-risk">
    <div class="isw-risk-icons">
      <img src="../../../../../_shared/media/images/simbolo_avvertenza.png" alt="">
      <img src="../../../../../_shared/media/images/simbolo_elettrico.png" alt="">
    </div>
    <div class="isw-risk-body">
      <div class="isw-risk-title">Electrical hazard</div>
      <div class="isw-risk-desc">
        Access and maintenance operations expose to electrical risk. Work on live parts must be carried out exclusively by expert and qualified personnel. Safety measures:
        <ul>
          <li>Comply with the safety pictograms relating to electrical risk.</li>
          <li>Do not perform maintenance without first disconnecting the power supply.</li>
          <li>Consult the manuals of the commercial equipment for specific recommendations.</li>
          <li>Periodically inspect the equipotential protection circuit.</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="isw-risk">
    <div class="isw-risk-icons">
      <img src="../../../../../_shared/media/images/simbolo_avvertenza.png" alt="">
    </div>
    <div class="isw-risk-body">
      <div class="isw-risk-title">Hazard from dust and splinters</div>
      <div class="isw-risk-desc">
        At the end of the work cycle, residues of the fed parts or accumulations of dust may remain on the surface of the machine. Carefully clean the vibrating surface after each use (see chap. 7).
      </div>
    </div>
  </div>

</div>

```{attention}
Do not carry out maintenance and cleaning activities without first de-energizing all the energy sources present.
```

```{attention}
It is absolutely forbidden to remove the safety guards or open the fixed guards without first disconnecting the electrical and pneumatic power supply of the machine.
```

The user is required to:
- analyze the handling and installation risks within their own premises;
- raise awareness among and instruct the personnel assigned to the operations;
- apply visual safety signs in the working environment.

</div>