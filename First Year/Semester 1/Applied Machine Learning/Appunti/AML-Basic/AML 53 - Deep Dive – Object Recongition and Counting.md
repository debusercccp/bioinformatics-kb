---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 53
tags: [note, aml]
---

> [[AML 52 - Using 1D convolutional layers to process sequences|← Using 1D convolutional layers to process sequences]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 54 - Deep Dive – Semantic Segmentation|Deep Dive – Semantic Segmentation →]]

# Deep Dive: Object Recongition and Counting

> **Problem: Object Counting**
>
> Object counting in images is a common task in many real-world applications, including crowd surveillance, smart agriculture (Agriculture 4.0), and life sciences such as biology and medicine. Performing this task manually is extremely time-consuming, labor-intensive, and prone to fatigue-related errors. The main goal is to automate this process to make it faster, reduce human involvement, and eliminate fatigue-related mistakes. Ideally, automated models should also produce **interpretable results**, meaning they can justify their outputs in a way that is understandable to human users.
>
> **Object Localization and Counting Approaches**
>
> A key step in object counting is localizing the objects in the image. This can be done using:

- **Density maps**

- **Point-based annotations**

- **Bounding boxes**

- **Pixel-wise segmentation**

> Object counting is particularly interesting because it can be approached in several fundamentally different ways, each with its own trade-offs:

1.  **Counting-by-Regression**

> This approach maps the entire input image directly to a single output count, without explicitly recognizing or localizing the individual objects.
>
> It is a simple method but lacks interpretability, as it provides no information about where the objects are. Moreover, it requires large amounts of annotated data to train effectively.

2.  **Counting-by-Detection**

> Here, the goal is to **localize** objects using bounding boxes. The count is obtained by simply counting the number of detected objects.
>
> This method is more interpretable than regression because it visually shows what is being counted. However, it becomes challenging in crowded scenes and requires more complex annotations, which are time-consuming to produce.

3.  **Counting-by-Segmentation**

> This strategy involves learning the exact contours of objects by predicting them at the **pixel level**. The count is then derived by identifying connected regions in the segmented output. This approach is highly interpretable and gives the most precise object definition. However, it is computationally more demanding and requires extremely detailed, pixel-level annotations, which are expensive and time-consuming to obtain. **Fluorescence Microscopy and Cell Counting**

- **Fluorescence** is the emission of light by a substance that has absorbed energy, often in the form of radiation. After absorbing energy, molecules enter an unstable state and release energy to return to equilibrium, emitting light in the process. Substances capable of this are called **fluorophores**. Each fluorophore emits light at a specific wavelength, which can be predicted based on its properties (known as the *Stokes shift*).

- **Fluorescence microscopy** is an imaging technique that leverages this phenomenon to visualize specific biological compounds. A sample is illuminated with a controlled light source of a known wavelength, and a microscope with filters captures the emitted fluorescence, allowing for selective visualization of the target structures. This technique is widely used, especially in life science research.

> **Use Case: Cell Counting in Hitrec et al., 2019**
>
> This study investigated biological mechanisms underlying torpor (a state of metabolic suppression), with potential applications in **intensive surgery** and **space travel**.
>
> Researchers used the **Cholera Toxin B-subunit (CTb)** as a fluorophore, which emits light in the yellow spectrum. CTb is a marker for **cytoplasmic structures** in neurons, specifically those linked to the **Raphe Pallidus** brain region.
>
> One major challenge in this context is the high **heterogeneity** of labeled cells in terms of **shape**, **size**, and **color**, making it difficult to clearly define what counts as a “cell.”
>
> This introduces subjectivity and inconsistency in manual counting, as different observers may count differently — and even the same observer may count inconsistently over time (known as the **operator effect**).
>
> These inconsistencies severely limit the ability to compare results across different experiments.
>
> **Challenges of Manual Annotation**
>
> Supervised learning models require **labeled data** to learn the relationship between input images and the desired outputs. In the context of cell counting, this means experts must manually annotate the exact location and shape of each cell — often at the pixel level.
>
> While some software tools help by allowing the user to draw outlines that are automatically filled in, the process remains extremely labor-intensive and slow.
>
> A semi-automatic annotation approach is sometimes used: an initial draft is created by thresholding pixel values, and then expert researchers refine it manually.
>
> In the referenced study, **31 images were manually segmented**, underscoring the high annotation burden even for a small dataset.

---
> [[AML 52 - Using 1D convolutional layers to process sequences|← Using 1D convolutional layers to process sequences]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 54 - Deep Dive – Semantic Segmentation|Deep Dive – Semantic Segmentation →]]
