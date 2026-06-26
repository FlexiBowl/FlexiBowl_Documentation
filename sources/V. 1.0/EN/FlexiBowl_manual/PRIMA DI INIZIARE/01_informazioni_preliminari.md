(info)=
# **Preliminary Information**

This section contains legal information and important warnings regarding the use of the FlexiBowl® and this documentation. Please read carefully before proceeding with the installation and use of the system.

---

## Target audience

```{note}
**Who this manual is intended for**

This documentation is addressed to qualified technicians with expertise in:
- Robotic system integration
- Industrial vision system configuration
- Installation and maintenance of electromechanical equipment

The reader is assumed to possess the basic technical knowledge required to understand the information provided. Information that can be easily inferred from technical drawings or diagrams may not be further detailed.
```

---

## Important warnings

### **Read before use**
```{warning}

Before using the FlexiBowl®, it is mandatory to:
- Read this manual in its entirety to ensure correct use of the system
- Follow the operating instructions and recommendations
- Adequately train all personnel responsible for operating the system
- Consult the instruction manuals of all connected hardware components (FlexiVision One, Hopper, VisionController, Camera, Robot, etc.)

Failure to comply with these instructions may cause malfunctions, equipment damage or hazardous situations.
```
### **Operating context and liability limitations**

The FlexiBowl® is a flexible feeding system with a rotating vibrating disc for the random positioning and orientation of components for robotic picking.

```{warning}
During operation, the operator must:
- Take into account the physical footprint of the system
- Monitor the movements of the robot and feeder
- Anticipate and manage unexpected operating situations
- Comply with safety regulations applicable to robots and industrial machinery
```
```{warning}
**ARS S.r.l. accepts no liability for damage to persons or property arising from the movement of machines and systems connected to the FlexiVision One software.**

Integration of the system into the working environment and risk assessment are the responsibility of the system integrator and the end user.
```

(operatori)=
## Operators

In order to clearly establish the competencies and qualifications required for personnel assigned to the various tasks (commissioning, cleaning, routine maintenance), refer to the following table:

:::{list-table}
:header-rows: 1
:widths: 30 70

* - Qualification
  - Definition

* - **System Integrator**
  - Personnel responsible for layout design, component sizing and verification of technical requirements for the installation of the FlexiBowl®.

* - **Installation Technician**
  - Personnel responsible for mechanical assembly, electrical and pneumatic connections, and network configuration.

* - **Operator**
  - User personnel trained and authorised to operate and run the machine for the productive activities for which it was built and supplied. Must be able to perform all operations necessary for the proper functioning of the machine and for the safety of themselves and any co-workers. Must have proven experience in the correct use of such types of machinery and be trained, informed and instructed accordingly. In case of doubt, must report any anomaly to their supervisor.

    **Note:** Not authorised to carry out any maintenance activities.
    
* - **Mechanical Maintenance Technician**
  - Qualified technician capable of:

    * carrying out preventive/corrective maintenance on all mechanical parts of the machine subject to maintenance or repair;
    * accessing all parts of the machine for visual inspection, condition assessment of equipment, adjustments and calibration;
    * working on mechanical components for adjustments, maintenance and repairs;
    * reading pneumatic and hydraulic diagrams, technical drawings and spare parts lists.

    In extraordinary cases, is authorised to operate the machine with reduced safety guards. Where necessary, may instruct the operator on the correct use of the machine for productive purposes.

    **Note:** Not authorised to work on live electrical systems (where present).

* - **Electrical Maintenance Technician**
  - Qualified technician capable of:
    * carrying out preventive/corrective maintenance on all mechanical parts of the machine subject to maintenance or repair;
    * accessing all parts of the machine for visual inspection, condition assessment of equipment, adjustments and calibration;
    * operating the machine as an operator;
    * working on electrical systems for maintenance, repair and replacement of worn parts;
    * reading electrical diagrams and verifying the correct functional cycle.
  Where necessary, may instruct the operator on the correct use of the machine for productive purposes. May work in the presence of live voltage inside electrical panels, junction boxes, control equipment etc. only if classified as a qualified electrical person (PEI). (Refer to standard **EN50110-1**). Does not perform software programming of systems such as: PLC (logic or safety), and may not modify system passwords.

* - **Expert Software Technician**
  - Qualified technician capable of:
    * carrying out preventive/corrective activities on all software parts of the machine;
    * accessing all parts of the machine for visual inspection, condition assessment of equipment, adjustments and calibration.
  Qualified manufacturer's technician with proven experience and training in systems based on: PLC/PC drives, etc. (knowledge of programming, machine functions, etc.) for complex operations such as:
    * modification of machine data; 
    * creation of work programs; 
    * adjustment of drive parameters, etc., with knowledge of the production, technological and construction cycle of the supplied machine. 
  May work inside electrical panels, junction boxes, control equipment etc. in the presence of live voltage only if classified as a qualified electrical person (PEI) (Refer to standard **EN50110-1**). Competencies are of an electronic and/or software nature.

* - **Manufacturer's Technician**
  - Technician qualified by the Manufacturer and/or their distributor for complex operations, with knowledge of the machine's production and construction cycle. This person intervenes in accordance with the user's requests. Competencies are of a mechanical nature.

* - **Trained Person**
  - Encompasses all qualifications listed in this table: a person who has been informed, instructed and trained on the job and on the potential hazards arising from improper use. Also aware of the importance of safety devices, accident prevention regulations and safe working conditions.

:::

---

## Documentation notes

### **Version and updates**

```{note}

- **Reference language**: the Italian version of this document is the official one and prevails in the event of discrepancies with other translations
- **Updates**: the information contained herein is subject to change without notice due to product improvements
- **Units of measurement**: unless otherwise stated, all dimensions are expressed in millimetres (mm)
- **Document version**: always ensure you have the most recent version by consulting [www.flexibowl.it](https://www.flexibowl.it)
```
### **How to make the most of this manual**

```{tip}

For the best experience:
- Use the side navigation menu to quickly move between sections
- Consult the initial index to immediately identify the section of interest
- Pay particular attention to warning, note and tip banners
- Follow procedures in the order indicated, especially during initial installation
- Keep this manual in digital format to facilitate quick keyword searches
```

---


## Reproduction rights and legal notices

```{important}
**Copyright © ARS S.r.l. - All rights reserved**

No part of this publication may be reproduced, distributed, translated or transmitted by any means (electronic, mechanical, photocopy, recording or any other storage system) for purposes other than personal use, without prior written authorisation from ARS S.r.l.

ARS S.r.l. accepts no liability for consequences arising from incorrect operations performed by the user or from improper use of the product.

**Registered trademarks**: FlexiBowl® is a registered trademark of ARS S.r.l. All other trademarks, trade names and logos mentioned in this document belong to their respective owners and are used solely for identification purposes.
```
---


