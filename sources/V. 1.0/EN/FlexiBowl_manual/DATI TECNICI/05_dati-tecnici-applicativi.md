# **Application Technical Data**

## Characteristics of the components permitted on the FlexiBowl®

:::{raw} html
   <style>
     .ars-components td, .ars-components th { text-align: center; vertical-align: middle; }
     .ars-components td:first-child, .ars-components th:first-child { text-align: left; }
   </style>
:::

:::{list-table}
:class: ars-components
:header-rows: 1
:align: center
:widths: 40 25 25 25 25 25 25

* - Component specifications
  - FlexiBowl® 200
  - FlexiBowl® 350
  - FlexiBowl® 500
  - FlexiBowl® 650
  - FlexiBowl® 800
  - FlexiBowl® 1200

* - Maximum size of a single component
  - 20 mm
  - 50 mm
  - 100 mm
  - 150 mm
  - 250 mm
  - 400 mm

* - Maximum height of a single component¹
  - 10 mm
  - 20 mm
  - 40 mm
  - 45 mm
  - 60 mm
  - 70 mm

* - Maximum weight of a single component
  - 20 g
  - 40 g
  - 100 g
  - 170 g
  - 250 g
  - 300 g

* - Maximum load capacity on surface
  - N.A.
  - N.A.
  - 7 kg
  - 7 kg
  - 7 kg
  - 7 kg

* - Maximum load capacity on rigid disc
  - 1 kg
  - 3 kg
  - 7 kg
  - N.A.
  - N.A.
  - N.A.

:::

1) The maximum component height is the one that leaves the necessary space between the component and the top surface of the flip screen to allow it to be flipped

:::{note}
The maximum component size value is derived from internal tests and is to be considered purely indicative, as other factors may influence it (hopper dimensions, the robot tool used for *picking*, etc.); for more precise indications, do not hesitate to [contact our team](https://www.arsautomation.com/contact) or request a [*free test*](https://www.flexibowl.it/free-test).
:::

:::{note}
The maximum component height is calculated taking into account the space needed to flip it using the flip, and is to be considered purely indicative, since the possibility of flipping also depends on the ratio between its dimensions. For a more precise assessment of the FlexiBowl® size best suited to the part to be handled, or of the component's compatibility with the desired FlexiBowl®, you can [contact our team](https://www.arsautomation.com/contact) or request a [*free test*](https://www.flexibowl.it/free-test).
:::

## How to assess the flippability of the component

To understand whether a part loaded in the hopper can be effectively separated and flipped by the flip, three main factors must be evaluated: geometry, mass limits and material.

### Slenderness index

With the part placed in its most stable configuration, the following dimensions are measured:

- Maximum height ***H***: Vertical distance from the supporting surface to the highest point of the part.

- Minimum width at the base ***$B_{\min}$***: The narrowest side of the bounding rectangle of the supporting base.

The index ***$I_s$*** is calculated as follows:

$$
I_s = \frac{H}{B_{\min}}
$$

This value tells us how easy it is to flip the part:

:::{list-table}
:widths: 33 33 33
:header-rows: 1
* - Slenderness index $I_s$
  - Part stability
  - Suitability for flipping
* - $I_s < 1.0$ (wide and low)
  - **Extremely Stable.** It tends to jump vertically without rotating or falls back onto the same base.
  - **Difficult to flip.** Requires the maximum flip energy.
* - $1.0 < I_s < 2.0$
  - **Moderate Stability.** The dynamic behavior depends on the symmetry of the part.
  - **Critical Zone.** Requires a practical validation test on the machine.
* - $I_s > 2.0$ (slender and tall)
  - **Highly Unstable.** The high center of gravity makes it extremely sensitive to impact.
  - **Excellent.** It flips very easily with standard energy settings.
:::

Based on the value of the slenderness index, a **base pressure** value is chosen for the flip:

:::{raw} html

<style>
     table.ars-table {
       border-collapse: collapse;
       width: 100%;
       font-family: inherit;
       border: 1px solid #cccccc;
     }
     table.ars-table thead tr {
       background-color: #f5f5f5;
       border-bottom: 2px solid #3366CC;
     }
     table.ars-table thead th {
       font-weight: bold;
       padding: 12px 16px;
       text-align: center;
       border-right: 1px solid #cccccc;
     }
     table.ars-table thead th:first-child {
       text-align: left;
     }
     table.ars-table thead th:last-child {
       border-right: none;
     }
     table.ars-table tbody tr:nth-child(odd)  { background-color: #f5f5f5; }
     table.ars-table tbody tr:nth-child(even) { background-color: #ffffff; }
     table.ars-table tbody tr:hover           { background-color: #ddeeff; }
     table.ars-table td {
       padding: 10px 16px;
       text-align: center;
       border-right: 1px solid #cccccc;
     }
     table.ars-table td:first-child {
       text-align: left;
     }
     table.ars-table td:last-child {
       border-right: none;
     }
/* Main table structure */
[data-theme="dark"] table.ars-table {
  border-collapse: collapse;
  border-spacing: 0;
  
  /* Removes the outer vertical borders (left and right) */
  border-left: none;
  border-right: none;
  
  /* Keeps only the thin outer horizontal borders (top and bottom) */
  border-top: 1px solid #383f4f;
  border-bottom: 1px solid #383f4f;
}

/* Handling of the inner cell borders (th and td) */
[data-theme="dark"] table.ars-table th,
[data-theme="dark"] table.ars-table td {
  padding: 10px 12px;
  
  /* Same bottom horizontal line for all rows */
  border-bottom: 1px solid #383f4f;
  
  /* Inner vertical line (on the right of each cell) */
  border-right: 1px solid #383f4f;
  
  /* Resets the other sides to avoid conflicts */
  border-left: none;
  border-top: none;
}

/* Removes the last vertical line on the right so as not to create the outer right border */
[data-theme="dark"] table.ars-table th:last-child,
[data-theme="dark"] table.ars-table td:last-child {
  border-right: none;
}

/* Removes the last horizontal line so as not to double it with the table bottom */
[data-theme="dark"] table.ars-table tbody tr:last-child td {
  border-bottom: none;
}

/* ══════════ MATCHING COLORS SECTION ══════════ */

/* Header background */
[data-theme="dark"] table.ars-table thead tr {
  background-color: #29313d;
}

[data-theme="dark"] table.ars-table thead th {
  color: #e0e0e0;
  font-weight: 600;
}

/* Zebra striping identical to the first table */
[data-theme="dark"] table.ars-table tbody tr:nth-child(odd) {
  background-color: #222832; /* Dark row */
}

[data-theme="dark"] table.ars-table tbody tr:nth-child(even) {
  background-color: #29313d; /* Light row */
}

/* Hover effect on mouse-over */
[data-theme="dark"] table.ars-table tbody tr:hover {
  background-color: #282d3a;
}
   </style>
<table class="ars-table">
  <thead>
    <tr>
      <th style="padding:10px 14px; text-align:left;">FlexiBowl® Size</th>
      <th style="padding:10px 14px; text-align:left;">Component Geometry</th>
      <th style="padding:10px 14px; text-align:left;">Base Pressure</th>
      <th style="padding:10px 14px; text-align:left;">Operating Notes and Behavior</th>
    </tr>
  </thead>
  <tbody>
    <!-- Sizes 200 / 350 -->
    <tr>
      <td rowspan="2" style="padding:10px 14px; font-weight:bold; vertical-align:middle;">200-350</td>
      <td style="padding:10px 14px;">I<sub>s</sub> &lt; 1.0 (Flat/Wide)</td>
      <td style="padding:10px 14px;">2.5 bar</td>
      <td style="padding:10px 14px;">Overlapping risk. Increase the number of strokes if the parts overlap.</td>
    </tr>
    <tr>
      <td style="padding:10px 14px;">I<sub>s</sub> &ge; 1.0 (Slender/Tall)</td>
      <td style="padding:10px 14px;">2.0 bar</td>
      <td style="padding:10px 14px;">Excellent flippability. Pay attention to parts that are too light.</td>
    </tr>
    <!-- Sizes 500 / 650 -->
    <tr>
      <td rowspan="2" style="padding:10px 14px; font-weight:bold; vertical-align:middle;">500-650</td>
      <td style="padding:10px 14px;">I<sub>s</sub> &lt; 1.0 (Flat/Wide)</td>
      <td style="padding:10px 14px;">3.2 bar</td>
      <td style="padding:10px 14px;">Requires more energy to overcome geometric stability.</td>
    </tr>
    <tr>
      <td style="padding:10px 14px;">I<sub>s</sub> &ge; 1.0 (Slender/Tall)</td>
      <td style="padding:10px 14px;">2.8 bar</td>
      <td style="padding:10px 14px;">Balanced standard configuration.</td>
    </tr>
    <!-- Sizes 800 / 1200 -->
    <tr>
      <td rowspan="2" style="padding:10px 14px; font-weight:bold; vertical-align:middle;">800-1200</td>
      <td style="padding:10px 14px;">I<sub>s</sub> &lt; 1.0 (Flat/Wide)</td>
      <td style="padding:10px 14px;">4.0 bar</td>
      <td style="padding:10px 14px;">Necessary to separate flat, heavy geometries.</td>
    </tr>
    <tr>
      <td style="padding:10px 14px;">I<sub>s</sub> &ge; 1.0 (Slender/Tall)</td>
      <td style="padding:10px 14px;">3.5 bar</td>
      <td style="padding:10px 14px;">Optimal starting point for bulky components.</td>
    </tr>
  </tbody>
</table>

:::

### Material correction factor ($K_m$)

The stiffness of the component directly affects the efficiency of the flip pulse transmission. Materials with elastic or damping behavior absorb part of the kinetic energy during impact, requiring compensation of the line pressure.

- **Rigid materials** ($K_m$ = 1.0):

  *Materials:* steel, aluminum, brass, sheet metal, POM, PA (rigid Nylon), ABS, glass, bakelite.

  *Notes:* Perfectly elastic impact. All of the energy is transferred to the part, which snaps instantly. No correction to the base pressure is required.

- **Semi-rigid materials** ($K_m$ = 1.2):

  *Materials:* polyethylene (PE), polypropylene (PP), unfilled Nylon, dense cardboard, layered composite materials.
  
  *Notes:* Presence of structural micro-damping. Increase the base pressure by 20% to ensure the same jump height as the rigid part.

- **Non-rigid materials** ($K_m$ = 1.0):

  *Materials:* natural rubber, nitrile rubber (NBR), silicone, polyurethane, soft TPU.
  
  *Notes:* Strongly inelastic impact. The component deforms momentarily under the pulse. Requires a 50% increase in the base pressure (up to the maximum line limit of 6.0 bar if necessary).

### Weight correction factor ($K_w$)

The mass of the component determines its inertia at take-off. Very light components require reduced pressures to avoid chaotic trajectories or spilling off the plate, while heavy components need a greater energy push to lift the center of gravity.

:::{raw} html
<style>
  table.ars-table {
    border-collapse: collapse;
    width: 100%;
    font-family: inherit;
    border: 1px solid #cccccc;
  }
  table.ars-table thead tr {
    background-color: #f5f5f5;
    border-bottom: 2px solid #3366CC;
  }
  table.ars-table thead th {
    font-weight: bold;
    padding: 12px 16px;
    text-align: center;
    border-right: 1px solid #cccccc;
  }
  table.ars-table thead th:first-child { text-align: left; }
  table.ars-table thead th:last-child  { border-right: none; }
  table.ars-table tbody tr:nth-child(odd)  { background-color: #f5f5f5; }
  table.ars-table tbody tr:nth-child(even) { background-color: #ffffff; }
  table.ars-table tbody tr:hover           { background-color: #ddeeff; }
  table.ars-table td {
    padding: 10px 16px;
    text-align: center;
    border-right: 1px solid #cccccc;
  }
  table.ars-table td:first-child { text-align: left; }
  table.ars-table td:last-child  { border-right: none; }

/* Main table structure */
[data-theme="dark"] table.ars-table {
  border-collapse: collapse;
  border-spacing: 0;
  
  /* Removes the outer vertical borders (left and right) */
  border-left: none;
  border-right: none;
  
  /* Keeps only the thin outer horizontal borders (top and bottom) */
  border-top: 1px solid #383f4f;
  border-bottom: 1px solid #383f4f;
}

/* Handling of the inner cell borders (th and td) */
[data-theme="dark"] table.ars-table th,
[data-theme="dark"] table.ars-table td {
  padding: 10px 12px;
  
  /* Same bottom horizontal line for all rows */
  border-bottom: 1px solid #383f4f;
  
  /* Inner vertical line (on the right of each cell) */
  border-right: 1px solid #383f4f;
  
  /* Resets the other sides to avoid conflicts */
  border-left: none;
  border-top: none;
}

/* Removes the last vertical line on the right so as not to create the outer right border */
[data-theme="dark"] table.ars-table th:last-child,
[data-theme="dark"] table.ars-table td:last-child {
  border-right: none;
}

/* Removes the last horizontal line so as not to double it with the table bottom */
[data-theme="dark"] table.ars-table tbody tr:last-child td {
  border-bottom: none;
}

/* ══════════ MATCHING COLORS SECTION ══════════ */

/* Header background */
[data-theme="dark"] table.ars-table thead tr {
  background-color: #29313d;
}

[data-theme="dark"] table.ars-table thead th {
  color: #e0e0e0;
  font-weight: 600;
}

/* Zebra striping identical to the first table */
[data-theme="dark"] table.ars-table tbody tr:nth-child(odd) {
  background-color: #222832; /* Dark row */
}

[data-theme="dark"] table.ars-table tbody tr:nth-child(even) {
  background-color: #29313d; /* Light row */
}

/* Hover effect on mouse-over */
[data-theme="dark"] table.ars-table tbody tr:hover {
  background-color: #282d3a;
}
</style>

<table class="ars-table">
  <thead>
    <tr>
      <th>Category</th>
      <th>Mass (FlexiBowl® 200/350/500)</th>
      <th>Mass (FlexiBowl® 650/800/1200)</th>
      <th>K<sub>w</sub></th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Light Components</strong></td>
      <td>&lt; 10 g</td>
      <td>&lt; 30 g</td>
      <td>0.8</td>
      <td>Low inertia. Reduces the base pressure by 20% to ensure a controlled, damped jump, avoiding uncontrolled bouncing.</td>
    </tr>
    <tr>
      <td><strong>Standard Components</strong></td>
      <td>10 &divide; 100 g</td>
      <td>30 &divide; 250 g</td>
      <td>1.0</td>
      <td>Optimal working window of the machine. No correction required.</td>
    </tr>
    <tr>
      <td><strong>Heavy Components</strong></td>
      <td>&gt; 100 g</td>
      <td>&gt; 250 g</td>
      <td>1.3</td>      
      <td>High inertia. Increases the base pressure by 30% to overcome gravity and allow the mass to be flipped.</td>
    </tr>
  </tbody>
</table>
:::

### Calculating the flip pressure

The pressure to be set for the flip is obtained by applying the formula:

$$
P_{flip} = P_{base} × K_m × K_w
$$

:::{attention}
If the calculation returns a value above 6.0 bar, set the regulator to the limit value of 6.0 bar (maximum operating pressure of the flip cylinder) and increase the Flip Count parameter if the part does not flip consistently. For a more precise and detailed assessment of the flip parameters, do not hesitate to [contact our team](https://www.arsautomation.com/contact) or request a [*free test*](https://www.flexibowl.it/free-test).
:::