# [MEC] **Maintenance and Troubleshooting**

:::{warning}
Carry out maintenance operations when the machine is switched off.
:::

:::{warning}
Maintenance operations must be carried out by qualified and authorized personnel.
::: 

Machine maintenance includes the interventions (inspection, verification, checking, adjustment and replacement) that become necessary as a result of normal use.

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

  /* Forces the card with your light-blue border and alternate background */
  .isw-timeline-custom .isw-card-fixed {
    display: block !important;
    padding: 1.4rem !important;
    border: 2px solid var(--c-accent, #2980b9) !important;
    border-radius: var(--radius, 10px) !important;
    background: var(--c-bg-alt, #f7fbfe) !important;
    box-shadow: var(--shadow-sm, 0 1px 4px rgba(41,128,185,.08)) !important;
  }

  /* Forces the title style */
  .isw-timeline-custom .isw-card-fixed .isw-symbol-label {
    color: var(--c-accent, #2980b9) !important;
    font-size: 19px !important;
    font-weight: 700 !important;
    margin-bottom: 0.5rem !important;
    display: block !important;
    text-transform: none !important;
  }

  /* Dashed vertical line */
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

  /* Minimal V-shaped arrow tip */
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
      <div class="isw-symbol-desc">Use only original spare parts and tools that are suitable for the purpose and in good condition.</div>
    </div>
  </div>

  <div class="isw-timeline-item-fixed">
    <div class="isw-timeline-arrow-fixed"></div>
    <div class="isw-card-fixed">
      <span class="isw-symbol-label">Intervention frequencies</span>
      <div class="isw-symbol-desc">Comply with the deadlines indicated in the manual for scheduled maintenance (preventive and periodic). The time interval or work cycles between one intervention and the next are to be understood as the maximum acceptable value and must not be exceeded.</div>
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
        Immediate removal of the causes of an anomaly or malfunction avoids further damage to the equipment and guarantees operator safety.
      </div>
    </div>
  </div>

</div>

The assigned personnel must be well trained and have a thorough knowledge of the accident-prevention regulations. Unauthorized personnel must stay outside the work area during the operations. 

Cleaning and adjustment activities are carried out only and exclusively during maintenance, with the machine stopped, de-energized and with the electrical panel disconnected.

:::{important}
If in doubt, do not operate. Contact the Manufacturer for the necessary clarifications.
:::

:::{attention}
Repair or maintenance work not contained in this manual may be carried out only with the prior authorization of ARS S.r.l.
No liability for damage to persons or property can be attributed to ARS S.r.l. for interventions other than those described or carried out in ways other than those indicated.
:::

### Operational classification of maintenance

| Maintenance type | Description |
| :--- | :--- |
| **Routine maintenance** | Preventive operations to ensure the proper operation of the machine over time (inspection, checking, adjustment, cleaning and lubrication). |
| **Extraordinary maintenance** | Corrective interventions as needed (overhaul, repair, restoration of nominal conditions or replacement of a faulty, defective or worn assembly). |

---

## Safety Warnings 

:::{attention} 
Before starting any maintenance work on the machine, disconnect and lock out all energy sources, and put the moving assemblies that make it up into a safe locked condition. Affix the sign “Machine under maintenance - do not switch on the power” at the main switch.
:::

:::{attention}
When the machine is under maintenance, to prevent it from being accidentally started, affix signs reading: “WARNING! Machine Under Maintenance”.
:::

<div class="isw-page">
  <div class="isw-timeline-container">
    <div class="isw-timeline-item">
      <div class="isw-timeline-arrow"></div>
      <div class="isw-timeline-card">
        <span class="isw-symbol-label">PPE</span>
        <div class="isw-symbol-desc">Maintenance technicians must wear all the personal protective equipment (gloves, glasses, overalls) required for the activity to be carried out.</div>
      </div>
    </div>
    <div class="isw-timeline-item">
      <div class="isw-timeline-arrow"></div>
      <div class="isw-timeline-card">
        <span class="isw-symbol-label">Signage</span>
        <div class="isw-symbol-desc">If the operation involves removing guards, cordon off the work area and signal the ban on access for unauthorized persons.</div>
      </div>
    </div>
    <div class="isw-timeline-item">
      <div class="isw-timeline-arrow"></div>
      <div class="isw-timeline-card">
        <span class="isw-symbol-label">Disconnection check</span>
        <div class="isw-symbol-desc">Before proceeding with any activity, verify the actual disconnection of the energy sources (electric current, compressed air, hydraulic energy, etc.).</div>
      </div>
    </div>
    <div class="isw-timeline-item">
      <div class="isw-timeline-card">
        <span class="isw-symbol-label">Competence</span>
        <div class="isw-symbol-desc">The maintenance technician must carry out only the operations within their own competence (Mechanical, Electrical, Fluidic) for which they are explicitly authorized, using instrumentation suitable for fault finding.</div>
      </div>
    </div>
  </div>
</div>

---

## Routine Maintenance 

Routine maintenance keeps the mechanical condition and the cleanliness of the machine under control. The intervals indicated refer to normal operating conditions. 

:::{important}
For the routine maintenance of machines coming from external suppliers, refer to the attached sub-supplier manuals.
::: 

:::{important}
When fastening screws, always use LOCTITE 243 to ensure a perfect anti-vibration tightening.
:::

### Checks and verifications

#### Routine maintenance table – Checks

| Operation | Daily | Weekly | Monthly | Six-monthly | Annual |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Check the condition of the bowl before each start-up | ◈ | | | | |
| Check the wear condition of the relays | | | |  | ◈ |
| Check the correct operation of the fuses | | | |  | ◈ |
| Check the wear condition of the leaf springs | | | | ◈ |  |
| Check the correct operation of the electromagnet | | | | ◈ |  |
| Check the wear of the polyurethane coating *(where present)* | | | ◈ | |  |

#### Safety device check

To check the integrity of the protection systems, carry out the following steps:

<div style="display: flex; flex-direction: column; gap: 12px; margin: 20px 0;">
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #34495e; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">1</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Check that all the covers and housings of the machine are present and correctly fastened.
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
Cleaning operations must be carried out only by qualified and authorized personnel.
:::

:::{attention} 
To clean the machine, do not use sponge fragments, damp and/or abrasive cloths, lint-shedding rags, petrol or flammable solvents as detergent.
:::

:::{attention} 
Do not use acids or aggressive chemical solvents to clean the base of the hopper.
:::

:::{important}
Use mild, non-abrasive products, such as neutral degreasers or ordinary household soap. To remove fragments and dust, use a brush, taking care to wear protective glasses.
:::

#### Routine maintenance table – Cleaning

| Operation | Daily | Weekly | Monthly | Six-monthly | Annual |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Removal of residues and process waste from the bowl surface | ◈ | | | | |
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
      Remove localized dirt using commercial solvents that are non-flammable and non-toxic.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #7f8c8d; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">4</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      If necessary, use a vacuum cleaner to remove small residues present on the rotating surface.
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
Extraordinary maintenance and repair of the machine are reserved for qualified, trained and authorized technicians employed by the Manufacturer or by the authorized service center.
:::

If exceptional events occur that require extraordinary interventions, the user's in-house maintenance technicians must:
1. Accurately verify the condition of the damaged or misaligned assemblies.
2. Carry out only the operations described in this paragraph, if authorized.
3. If the operations are not covered in this manual, send the Manufacturer a detailed report of the facts, the result of the inspection and the observations made.

:::{attention} 
Spare parts to be replaced must be ordered directly from ARS S.r.l. If original spare parts, or parts authorized in writing, are not used, the Manufacturer declines all liability for the operation of the machine and the safety of the operators.
:::

:::{attention} 
Disconnect the electrical and pneumatic power supply before carrying out any extraordinary maintenance operation or before removing the protective covers.
:::

:::{important}
When tightening screws, always use LOCTITE 243 threadlocker to ensure mechanical hold.
:::

### Air gap adjustment

The air gap is the physical distance between the core and the counter-core; a millimetric adjustment is essential:
* **Air gap too narrow:** The surfaces of the core and the counter-core come into mechanical contact during operation, causing "hammering".
* **Air gap too wide:** The electric current of the vibrator can rise to critical levels, causing the winding to burn out and damaging the internal components of the controller.

:::{attention}
Under no circumstances operate the vibrator if one of the two conditions described above occurs.
:::

:::{important}
The air gap is properly calibrated at the factory; adjustment work becomes necessary only in the event of improper handling or overvoltage.
:::

| Operating data | Intervention specifications |
| :--- | :--- |
| **Operator qualification** | Mechanical maintenance technician |
| **Tools to use** | Open-end wrench |

#### Air gap adjustment procedure

![Air gap adjustment](../../../../../_shared/media/images/regolazione_traferro.png)

<div style="display: flex; flex-direction: column; gap: 12px; margin: 20px 0;">
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">1</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Loosen the locking counter-nut <strong>(Nut 2)</strong>.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">2</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Tighten <strong>Screw 1</strong> clockwise until it reaches the end of its travel, i.e. against the mechanical stop on the counter-core.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">3</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Unscrew <strong>Screw 1</strong> counterclockwise: refer to the table below to identify the correct value and turn the screw by the number of turns and fractions required to set the correct distance.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">4</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Fully tighten <strong>Nut 2</strong> to ensure the stability of adjustment screw 1.
    </div>
  </div>
</div>

:::{note} 
 Air gap adjustment is a precision operation that may require repeated checks to obtain the ideal setting.
:::
![Air gap adjustment](../../../../../_shared/media/images/disegno_tecnico.png)

#### Air gap reference technical table

| Model | Magnet size | Required air gap | Adjustment screw rotation |
| :---: | :---: | :---: | :---: |
| **1.5 l** | Ø21 | 1.5 mm | 360° (1 full turn) |
| **3 l** | Ø24 | 2 mm | 480° (1 turn + 1/3) |
| **5 l** | Ø28 | 3 mm | 720° (2 full turns) |
| **10 l** | Ø28 | 3 mm | 720° (2 full turns) |
| **20 l** | Ø28 | 3 mm | 720° (2 full turns) |
| **40 l** | 32x30 | 3 mm | 720° (2 full turns) |

### Leaf spring replacement

| Operating data | Intervention specifications |
| :--- | :--- |
| **Operator qualification** | Mechanical maintenance technician |
| **Tools to use** | Open-end wrench |

Changing the sizing of the leaf spring pack (number and thickness of the leaves) serves to vary and adjust the useful capacity of the vibrator.

#### Leaf spring replacement procedure

<div style="display: flex; flex-direction: column; gap: 12px; margin: 20px 0;">
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">1</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Work on one leaf spring pack at a time, starting without fail with the one located on the rear side.
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
      Remove the mechanical anchoring bolts to the base and, subsequently, the fastening bolts to the bridge of the vibrating channel.
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

#### Leaf springs and tightening torques technical table

| Model | Leaf spring size | Leaf thickness | Tightening torque and thread |
| :---: | :---: | :---: | :--- |
| **1.5 l** | 40x48 mm | 1 - 1.5 - 2 mm | 7.5 N·m – M5 |
| **3 l** | 40x48 mm | 1 - 1.5 - 2 mm | 7.5 N·m – M5 |
| **5 l** | 70x82 mm | 1.5 - 2 mm | 30 N·m – M8 |
| **10 l** | 70x82 mm | 1.5 - 2 mm | 30 N·m – M8 |
| **20 l** | 70x82 mm | 1.5 - 2 mm | 30 N·m – M8 |
| **40 l** | 80x91 mm | 1.5 - 2 - 2.5 mm | 70 N·m – M10 |

### Bowl replacement

| Operating data | Intervention specifications |
| :--- | :--- |
| **Operator qualification** | Mechanical maintenance technician |
| **Tools to use** | Open-end wrench |

#### Bowl removal and installation procedure

<div style="display: flex; flex-direction: column; gap: 12px; margin: 20px 0;">
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">1</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Firmly support the bowl to prevent it from falling freely.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">2</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Completely unscrew all the fastening screws of the two side protective covers and remove them.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">3</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Loosen the lower retaining bolts of the bowl structure.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">4</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Carefully extract the original bowl from its seat.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">5</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Position the new replacement bowl, checking the alignment.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">6</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Firmly tighten the structural locking screws.
    </div>
  </div>
  <div style="display: flex; background-color: #f8f9fa; border-radius: 6px; border: 1px solid #e9ecef; overflow: hidden;">
    <div style="background-color: #2980b9; color: #ffffff; display: flex; align-items: center; justify-content: center; width: 45px; font-weight: bold; flex-shrink: 0;">7</div>
    <div style="padding: 12px 15px; color: #2c3e50; font-size: 0.95em;">
      Reassemble the two protective covers, taking care to refit last the one with bent flaps.
    </div>
  </div>
</div>

![Air gap adjustment](../../../../../_shared/media/images/vasca.jpg)

:::{attention}
In the case of custom models, the components may differ, partially or totally, from those indicated. For models of this kind, refer to the technical project file.
:::

---

## Troubleshooting

:::{attention}
During normal operation the vibrator must run quietly. If a dull noise caused by internal hammering occurs, switch off the system immediately.
:::

In the event of hammering, check and restore the optimal air gap: if the surfaces are too close they will impact mechanically; if too far apart, the abnormal rise in current will burn the stator windings.

| Symptom observed | Possible root cause | Corrective action required |
| :--- | :--- | :--- |
| **The vibrator runs too slowly** | The supply voltage is below the nominal threshold. | Increase the electrical voltage to the correct nameplate value. |
| | The unit comes into contact with external rigid objects or adjacent structures. | Restore the physical clearances by isolating the vibrating unit (3-5 cm). |
| | The oscillation of the leaf spring packs is obstructed or slowed by build-up. | Disassemble, clean thoroughly and remove the residues from the leaf spring packs. |
| | The leaf springs show cracks, defects or structural yielding. | Replace the leaf spring set immediately. |
| | The vibrating channel is cracked or mechanically worn. | Replace the channel. |
| **The vibrator runs too fast** | The supply voltage exceeds the nominal limits *(Primary cause of hammering)*. | Stabilize and reduce the supply voltage to the nameplate value. |
| **The unit makes noise (humming) but does not vibrate** | The electronic adjustment board inside the box is faulty. | Replace the electronic board of the controller. |
| **The unit does not activate and does not respond** | Total lack of electrical power at the Controller input. | Inspect the line and remove any electrical interruptions. |
| | The thermal-magnetic circuit breaker or protection fuse has tripped/blown. | Replace the fuses or reset the breaker. |
| | The electronic board inside the control box is damaged. | Replace the electronic board. |
| | The internal winding of the vibrator is burnt or short-circuits to ground. | Replace the electromagnet assembly. |
| | The winding has an internal short circuit. | Replace the winding. |
| | The winding of the adjustment rheostat is open. | Replace the faulty component. |


