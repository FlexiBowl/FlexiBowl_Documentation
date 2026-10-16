# [SOF] **Mix Mode**

## Operation in MIX Mode

**MIX Mode** allows parts of different types to be fed simultaneously on the same FlexiBowl® surface.    

This mode is particularly suitable for **sorting** applications in which several references are required on the same work surface without having to multiply the robotic stations.

```{figure}  ../../../../_shared/media/images/flexibowl_standard_cycle.jpg
:align: center
:width: 50%
:alt: *Operating cycle in Mix Mode: Detect → Pick-Drop → Move-Flip*
```

```{image}  ../../../../_shared/media/videos/MIX_MODE.gif
:align: center
:width: 100%
:alt: *Operating cycle in Mix Mode: Detect → Pick-Drop → Move-Flip*
```
---

## Main features

| Feature | Description |
|---|---|
| **Application** | Ideal for sorting applications with several types of parts |
| **Flexibility** | Feeding of mixed parts on the same surface |

---

## Operating cycle

The MIX Mode cycle is simplified compared to the standard mode, with only three stages
that repeat in sequence:

```{list-table}
:header-rows: 1
:widths: 20 80

* - Phase
  - Description
* - **Detect**
  - The camera acquires the image of the common surface, identifying the position and orientation of all the parts present, regardless of their type.
* - **Move-Flip**
  - The FlexiBowl® rotates and the parts that are not correctly oriented are flipped or repositioned.
* - **Pick-Drop**
  - The robot picks the correct part based on the sorting logic and places it in the destination position.
```


---

## Operating notes

:::{tip}
MIX Mode does not require additional hardware compared to a standard configuration.  
 It is sufficient to configure the vision software to recognize several references and to set the sorting logic in the robot program.
:::

:::{note}
For the optimal placement of the FlexiBowl® and of the robot, refer to the {ref}`Layout Best Practice <layoutbp>` chapter.
:::
