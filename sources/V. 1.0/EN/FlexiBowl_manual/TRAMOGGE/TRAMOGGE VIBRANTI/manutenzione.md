# **Maintenance and Troubleshooting**

:::{warning}
Carry out maintenance operations when the machine is switched off.
:::

:::{warning}
Maintenance operations must be carried out by qualified and authorised personnel.
::: 

Maintenance of the machine includes the work (inspection, verification, checking, adjustment and replacement) that becomes necessary as a result of normal use.

**Guidelines for correct maintenance:**

<style>
  .isw-timeline-custom {
    display: flex !important;
    flex-direction: column !important;
    position: relative !important;
    padding-left: 45px !important;
    margin: 2.5rem 0 !important;
    list-style: none !important;
  }

  .isw-timeline-custom .isw-timeline-item-fixed {
    display: block !important;
    position: relative !important;
    padding-bottom: 2.5rem !important;
  }

  .isw-timeline-custom .isw-timeline-item-fixed:last-child {
    padding-bottom: 0 !important;
  }

  /* Forza la card con il tuo bordo azzurro e sfondo alternativo */
  .isw-timeline-custom .isw-card-fixed {
    display: block !important;
    padding: 1.4rem !important;
    border: 2px solid var(--c-accent, #2980b9) !important;
    border-radius: var(--radius, 10px) !important;
    background: var(--c-bg-alt, #f7fbfe) !important;
    box-shadow: var(--shadow-sm, 0 1px 4px rgba(41,128,185,.08)) !important;
  }

  /* Forza lo stile del titolo */
  .isw-timeline-custom .isw-card-fixed .isw-symbol-label {
    color: var(--c-accent, #2980b9) !important;
    font-size: 19px !important;
    font-weight: 700 !important;
    margin-bottom: 0.5rem !important;
    display: block !important;
    text-transform: none !important;
  }

  /* Linea verticale tratteggiata */
  .isw-timeline-custom .isw-timeline-item-fixed::before {
    content: '' !important;
    position: absolute !important;
    left: -24px !important;
    top: 25px !important;
    bottom: -15px !important;
    width: 2px !important;
    border-left: 2px dashed var(--c-accent, #2980b9) !important;
    z-index: 1 !important;
  }

  .isw-timeline-custom .isw-timeline-item-fixed:last-child::before {
    display: none !important;
  }

  /* Punta della freccia a V minimale */
  .isw-timeline-custom .isw-timeline-arrow-fixed {
    display: block !important;
    content: '' !important;
    position: absolute !important;
    left: -28px !important;
    bottom: 8px !important;
    width: 8px !important;
    height: 8px !important;
    border-right: 2px solid var(--c-accent, #2980b9) !important;
    border-bottom: 2px solid var(--c-accent, #2980b9) !important;
    transform: rotate(45deg) !important;
    z-index: 2 !important;
    background: var(--c-bg, #ffffff) !important;
  }
</style>

<div class="isw-timeline-custom">
  
  <div class="isw-timeline-item-fixed">
    <div class="isw-timeline-arrow-fixed"></div>
    <div class="isw-card-fixed">
      <span class="isw-symbol-label">Components</span>
      <div class="isw-symbol-desc">Use only original spare parts and tools suitable for the purpose and in good condition.</div>
    </div>
  </div>

  <div class="isw-timeline-item-fixed">
    <div class="isw-timeline-arrow-fixed"></div>
    <div class="isw-card-fixed">
      <span class="isw-symbol-label">Intervention frequencies</span>
      <div class="isw-symbol-desc">Observe the deadlines given in the manual for scheduled (preventive and periodic) maintenance. The time interval or the work cycles between one intervention and the next are to be understood as the maximum acceptable value and must not be exceeded.</div>
    </div>
  </div>

  <div class="isw-timeline-item-fixed">
    <div class="isw-timeline-arrow-fixed"></div>
    <div class="isw-card-fixed">
      <span class="isw-symbol-label">Preventive monitoring</span>
      <div class="isw-symbol-desc">Promptly investigate the cause of any anomalies such as excessive noise, overheating, fluid leaks, etc.</div>
    </div>
  </div>

  <div class="isw-timeline-item-fixed">
    <div class="isw-card-fixed">
      <span class="isw-symbol-label">Promptness</span>
      <div class="isw-symbol-desc">
        Immediately eliminating the causes of an anomaly or malfunction avoids further damage to the equipment and ensures the safety of the operators.
      </div>
    </div>
  </div>

</div>

The personnel in charge must be well trained and have a thorough knowledge of the accident-prevention rules. Unauthorised personnel must remain outside the work area during the operations.

Cleaning and adjustment activities are carried out solely and exclusively during maintenance, with the machine stopped, de-energised and with the electrical panel isolated.

:::{important}
In case of doubt, it is forbidden to operate. Consult the Manufacturer for the necessary clarifications.
:::

:::{attention}
Repair or maintenance work not covered by this manual may be carried out only with the prior authorisation of ARS S.r.l. No liability for damage to persons or property can be attributed to ARS S.r.l. for work other than that described or carried out in ways other than those indicated.
:::

### Operational classification of maintenance

| Maintenance type | Description |
| :--- | :--- |
| **Routine maintenance** | Preventive operations to ensure the proper operation of the machine over time (inspection, checking, adjustment, cleaning and lubrication). |
| **Extraordinary maintenance** | Corrective work as needed (overhaul, repair, restoration of nominal conditions or replacement of a faulty, defective or worn unit). |

---

## Safety Warnings 

:::{attention} 
Before starting any maintenance work on the machine, isolate and lock out all energy sources, and put the moving units that make it up into a safe locked condition. Place the sign “Machine under maintenance - do not switch on the power” at the main switch.
:::

:::{attention}
When the machine is under maintenance, to prevent it from being accidentally put into operation, place signs with the wording: “WARNING! Machine Under Maintenance”.
:::

<div class="isw-page">
  <div class="isw-timeline-container">
    <div class="isw-timeline-item">
      <div class="isw-timeline-arrow"></div>
      <div class="isw-timeline-card">
        <span class="isw-symbol-label">PPE</span>
        <div class="isw-symbol-desc">Maintenance personnel must wear all the personal protective equipment required (gloves, glasses, overalls) for the activity to be carried out.</div>
      </div>
    </div>
    <div class="isw-timeline-item">
      <div class="isw-timeline-arrow"></div>
      <div class="isw-timeline-card">
        <span class="isw-symbol-label">Signage</span>
        <div class="isw-symbol-desc">If the operation involves removing guards, cordon off the work area and signal the ban on access to unauthorised persons.</div>
      </div>
    </div>
    <div class="isw-timeline-item">
      <div class="isw-timeline-arrow"></div>
      <div class="isw-timeline-card">
        <span class="isw-symbol-label">Disconnection check</span>
        <div class="isw-symbol-desc">Before proceeding with any activity, verify that the energy sources (electric current, compressed air, hydraulic energy, etc.) are actually disconnected.</div>
      </div>
    </div>
    <div class="isw-timeline-item">
      <div class="isw-timeline-card">
        <span class="isw-symbol-label">Competence</span>
        <div class="isw-symbol-desc">Maintenance personnel must carry out only the operations within their own competence (Mechanical, Electrical, Fluidic) for which they are explicitly authorised, using instruments suitable for troubleshooting.</div>
      </div>
    </div>
  </div>
</div>

---

## Routine Maintenance 

Routine maintenance keeps the mechanical condition and cleanliness of the machine under control. The intervals indicated refer to normal operating conditions.

:::{important}
For routine maintenance of machines from external suppliers, refer to the attached sub-supplier manuals.
::: 

:::{important}
When tightening screws, always use LOCTITE 243 to ensure a perfect anti-vibration lock.
:::

### Checks and inspections

#### Routine maintenance table – Checks

| Operation | Daily | Weekly | Monthly | Six-monthly | Annual |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Check the condition of the tank before each start-up | ◈ | | | | |
| Check the state of wear of the relays | | | |  | ◈ |
| Check the fuses for correct operation | | | |  | ◈ |
| Check the state of wear of the leaf springs | | | | ◈ |  |
| Check the electromagnet for correct operation | | | | ◈ |  |
| Check the wear of the polyurethane coating *(where present)* | | | ◈ | |  |

#### Checking the safety devices

To check the integrity of the protection systems, carry out the following steps:

<div style="display: flex; flex-direction: column; gap: 12px; margin: 20px 0;">
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #34495e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">1</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Check that all the covers and casings of the machine are present and correctly secured.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #34495e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">2</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Check that the electrical power cable shows no damage, cuts or signs of surface wear.
    </div>
  </div>
</div>

#### Cleaning

:::{attention} 
Cleaning operations must be carried out only by qualified and authorised personnel.
:::

:::{attention} 
To clean the machine, do not use sponge fragments, damp and/or abrasive cloths, linting rags, petrol or flammable solvents as detergent.
:::

:::{attention} 
Do not use acids or aggressive chemical solvents to clean the base of the Bulk Feeder.
:::

:::{important}
Use mild, non-abrasive products, such as neutral degreasers or ordinary household soap. To remove fragments and dust, use a brush, taking care to wear protective glasses.
:::

#### Routine maintenance table – Cleaning

| Operation | Daily | Weekly | Monthly | Six-monthly | Annual |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Removal of process residues and waste from the tank surface | ◈ | | | | |
| Removal of grease and oil with neutral products or solvents | ◈ |  | | | |
| General cleaning of the machine | | ◈ |  | | |

#### General cleaning procedure

<div style="display: flex; flex-direction: column; gap: 12px; margin: 20px 0;">
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #7f8c8d; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">1</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Completely disconnect the electrical power supply from the machine.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #7f8c8d; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">2</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Manually remove any accumulated product residues.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #7f8c8d; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">3</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Remove localised dirt using non-flammable, non-toxic commercial solvents.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #7f8c8d; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">4</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      If necessary, use a vacuum cleaner to remove minute residues on the rotating surface.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #7f8c8d; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">5</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Once cleaning is finished, restore the machine connections.
    </div>
  </div>
</div>

:::{important}
General cleaning of the machine must be carried out whenever the type of component to be processed is changed, so as to eliminate contaminating residues from the previous processing.
:::

---

## Extraordinary Maintenance

:::{attention} 
Extraordinary maintenance and repair of the machine are reserved for qualified, trained and authorised technicians employed by the Manufacturer or by the authorised service centre.
:::

If exceptional events occur that require extraordinary work, the user's in-house maintenance personnel must:
1. Precisely check the state of the damaged or out-of-phase units.
2. Carry out only the operations described in this paragraph, if authorised.
3. If the operations are not covered in this manual, send the Manufacturer a detailed report of the facts, the result of the inspection and the observations noted.

:::{attention} 
The spare parts to be replaced must be ordered directly from ARS S.r.l. If original spare parts, or parts authorised in writing, are not used, the Manufacturer declines all liability for the operation of the machine and for the safety of the operators.
:::

:::{attention} 
Disconnect the electrical and pneumatic power supply before carrying out any extraordinary maintenance operation or before removing the protective covers.
:::

:::{important}
When tightening screws, always use LOCTITE 243 thread-locker to ensure mechanical hold.
:::

### Air gap adjustment

The air gap is the physical distance between the core and the counter-core; millimetre-precise adjustment is essential:
* **Air gap too narrow:** The surfaces of the core and counter-core come into mechanical contact during operation, causing "hammering".
* **Air gap too wide:** The electric current of the vibrator can rise to critical levels, causing the winding to burn out and damage to the internal components of the controller.

:::{attention}
Under no circumstances run the vibrator if either of the two conditions described above occurs.
:::

:::{important}
The air gap is properly calibrated at the factory; adjustments are necessary only in the event of improper handling or the application of overvoltages.
:::

| Operating data | Intervention specifications |
| :--- | :--- |
| **Operator qualification** | Mechanical maintenance technician |
| **Tools to be used** | Open-ended spanner |

#### Air gap adjustment procedure

![Air gap adjustment](../../../../../_shared/media/images/regolazione_traferro.png)

<div style="display: flex; flex-direction: column; gap: 12px; margin: 20px 0;">
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">1</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Loosen the locking lock nut <strong>(Nut 2)</strong>.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">2</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Screw in <strong>Screw 1</strong> clockwise until it reaches the end of its travel, i.e. up against the mechanical stop against the counter-core.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">3</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Unscrew <strong>Screw 1</strong> anticlockwise: refer to the table below to identify the correct value and turn the screw the number of turns and fractions needed to set the correct distance.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">4</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Tighten <strong>Nut 2</strong> fully to ensure the stability of adjustment screw 1.
    </div>
  </div>
</div>

:::{note} 
 Air gap adjustment is a precision operation that may require repeated checks to obtain the ideal setting.
:::
![Air gap adjustment](../../../../../_shared/media/images/disegno_tecnico.png)

#### Air gap technical reference table

| Model | Magnet size | Required air gap | Adjustment screw rotation |
| :---: | :---: | :---: | :---: |
| **1.5 l** | Ø21 | 1.5 mm | 360° (1 full turn) |
| **3 l** | Ø24 | 2 mm | 480° (1 turn + 1/3) |
| **5 l** | Ø28 | 3 mm | 720° (2 full turns) |
| **10 l** | Ø28 | 3 mm | 720° (2 full turns) |
| **20 l** | Ø28 | 3 mm | 720° (2 full turns) |
| **40 l** | 32x30 | 3 mm | 720° (2 full turns) |

### Replacing the leaf springs

| Operating data | Intervention specifications |
| :--- | :--- |
| **Operator qualification** | Mechanical maintenance technician |
| **Tools to be used** | Open-ended spanner |

Changing the sizing of the leaf spring pack (number and thickness of the leaves) serves to vary and adapt the useful capacity of the vibrator.

#### Leaf spring replacement procedure

<div style="display: flex; flex-direction: column; gap: 12px; margin: 20px 0;">
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">1</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Work on one leaf spring pack at a time, starting strictly with the one located on the rear side.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">2</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Note down or photograph the exact position and sequence order of each leaf spring, spacer and retaining clamp.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">3</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Remove the bolts anchoring it mechanically to the base and then the bolts fixing it to the bridge of the vibrating channel.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">4</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Replace worn or cracked elements with original spare parts.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">5</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Reassemble the leaf spring pack following exactly the reverse order of disassembly.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">6</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Tighten all the screws applying the tightening torque given in the following table.
    </div>
  </div>
</div>

#### Technical table of leaf springs and tightening torques

| Model | Leaf spring size | Leaf thickness | Tightening torque and thread |
| :---: | :---: | :---: | :--- |
| **1.5 l** | 40x48 mm | 1 - 1.5 - 2 mm | 7.5 N·m – M5 |
| **3 l** | 40x48 mm | 1 - 1.5 - 2 mm | 7.5 N·m – M5 |
| **5 l** | 70x82 mm | 1.5 - 2 mm | 30 N·m – M8 |
| **10 l** | 70x82 mm | 1.5 - 2 mm | 30 N·m – M8 |
| **20 l** | 70x82 mm | 1.5 - 2 mm | 30 N·m – M8 |
| **40 l** | 80x91 mm | 1.5 - 2 - 2.5 mm | 70 N·m – M10 |

### Replacing the tank

| Operating data | Intervention specifications |
| :--- | :--- |
| **Operator qualification** | Mechanical maintenance technician |
| **Tools to be used** | Open-ended spanner |

#### Tank removal and installation procedure

<div style="display: flex; flex-direction: column; gap: 12px; margin: 20px 0;">
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">1</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Support the tank firmly to prevent it from falling accidentally during removal.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">2</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Loosen the four set screws on the base plate of the tank.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">3</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Carefully lift the original tank and extract it from its seat.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">4</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Remove the gasket from the base plate.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">5</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Place the gasket on the new tank, checking that it is correctly seated.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">6</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Insert the new tank into its seat, checking that it is correctly engaged on the clamping pins and that the gasket is correctly positioned.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">7</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Tighten the four set screws on the base plate to secure the new tank.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">8</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Check that the new tank is correctly positioned and firmly secured.
    </div>
  </div>
</div>

![Tank removal and installation](../../../../../_shared/media/images/vasca.jpg)

:::{attention}
In the case of custom models, the components may differ, partially or totally, from those indicated. For such models, refer to the project technical file.
:::

---

## Troubleshooting

:::{attention}
During normal operation the vibrator must run quietly. If a dull noise caused by internal hammering occurs, switch the system off immediately.
:::

In the event of hammering, check and restore the optimal air gap: if the surfaces are too close they will hit each other mechanically; if too far apart, the abnormal rise in current will burn the stator windings.

| Observed symptom | Possible root cause | Corrective action required |
| :--- | :--- | :--- |
| **The vibrator runs too slowly** | The supply voltage is below the nominal threshold. | Increase the electrical voltage up to the correct rated value. |
| | The unit comes into contact with external rigid objects or adjacent structures. | Restore the physical clearances by isolating the vibrating unit (3-5 cm). |
| | The oscillation of the leaf spring packs is obstructed or braked by accumulations. | Disassemble, clean thoroughly and remove the residues from the leaf spring packs. |
| | The leaf springs show cracks, defects or structural yielding. | Replace the leaf spring set immediately. |
| | The vibrating channel is cracked or mechanically worn. | Replace the channel. |
| **The vibrator runs too fast** | The supply voltage exceeds the nominal limits *(primary cause of hammering)*. | Stabilise and reduce the supply voltage to the rated value. |
| **The unit makes noise (humming) but does not vibrate** | The electronic regulation board inside the box is faulty. | Replace the controller's electronic board. |
| **The unit does not activate and does not respond** | Total lack of electrical input power to the Controller. | Inspect the line and remove any electrical interruptions. |
| | The circuit breaker or the protection fuse has tripped/blown. | Replace the fuses or reset the breaker. |
| | The electronic board inside the control box is damaged. | Replace the electronic board. |
| | The internal winding of the vibrator is burnt out or discharges to earth. | Replace the electromagnet assembly. |
| | The winding has an internal short circuit. | Replace the winding. |
| | The winding of the regulating rheostat is open. | Replace the faulty component. |


