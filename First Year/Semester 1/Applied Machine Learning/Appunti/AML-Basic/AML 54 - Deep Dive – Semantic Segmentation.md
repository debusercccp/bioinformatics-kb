---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 54
tags: [note, aml]
---

> [[AML 53 - Deep Dive – Object Recongition and Counting|← Deep Dive – Object Recongition and Counting]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 55 - Deep Dive – MLOps|Deep Dive – MLOps →]]

# Deep Dive: Semantic Segmentation

> **Image Segmentation for Cell Detection**
>
> **Image segmentation** is a technique used to identify and classify regions of interest within an image. It works by assigning a specific category or class to each individual pixel. There are **two main types of segmentation**:

- **Semantic segmentation**: All pixels belonging to the same class (e.g., “cell”) share the same label, regardless of which object they belong to.

- **Instance segmentation**: Each instance of an object receives a unique label, even if multiple instances belong to the same class.

> In the context of **cell counting**, the goal is to distinguish **cells from the background**, framing it as a **binary classification** task:

- **Class 0**: Background

- **Class 1**: Cell

> The model typically outputs a **probability heatmap** for class 1 (cell), showing the likelihood that each pixel belongs to a cell.
>
> **U-Net Architecture**
>
> Originally introduced by **Ronneberger et al. (2015)** for **semantic segmentation** in biomedical images, **U-Net** has become a foundational architecture in medical image analysis.
>
> It consists of two main parts:

- ![[AML-image372.jpg|349]]A **contracting path** (encoder) for **downsampling** and extracting features. • An **expanding path** (decoder) for **upsampling** and reconstructing spatial resolution.

> **Basic U-Net block**
>
> ![[AML-image373.jpg|327]]Two 3×3 convolutional layers (without padding), each followed by an activation function.
>
> A 2×2 max-pooling layer for downsampling.
>
> **Key properties:** Each downsampling step **doubles the number of feature maps** and **halves the spatial dimensions**.
>
> **Contracting Path (Encoder)**

- ![[AML-image374.jpg|357]]Composed of **four U-Net blocks** followed by a **bottleneck** layer.

- With each block:

> o The spatial resolution is halved. o The number of feature maps is doubled.

- The bottleneck ends with **1024 feature maps** at **1/16th** the original input size.

- The encoder captures high-level patterns and semantics in the input image.

> **Expanding Path (Decoder)**
>
> ![[AML-image375.jpg|355]]Consists of **four upsampling blocks**:

- Uses **up-convolutions** instead of max-pooling. o Integrates **long-range skip connections** from the encoder. o Each block contains two convolutional layers.

<!-- -->

- Each step:

  - **Doubles** the spatial resolution.

  - **Halves** the number of feature maps. • The final **segmentation map** matches the input size (except for slight differences due to lack of padding).

- This path is responsible for **precise object localization**.

> **ResUNet**
>
> ![[AML-image376.jpg|226]]**ResUNet**, introduced by **Zhang et al. (2018)**, builds on the original U-Net by incorporating **residual units**, inspired by ResNet.
>
> **Benefits:**

- Helps mitigate the **vanishing gradient problem**, making training easier.

- Requires **fewer parameters**, improving efficiency.

> ![[AML-image377.jpg|262]]**Residual Unit Components**:

- Modified U-Net block with:

<!-- -->

- **Batch normalization**. o Activation **before** convolution.

- A shortcut or **identity path**, which bypasses the main convolutional stream.

<!-- -->

- Output = input + conv(input)

> **cell ResUNet (c-ResUNet)**
>
> ![[AML-image378.jpg|295]]**Morelli et al. (2021)** proposed **c-ResUNet**, a version of ResUNet **specifically designed for fluorescence microscopy** and tested for cell counting tasks.
>
> **Key Modifications:**

- **1×1 convolution** at the input to learn a custom color space.

- Uses **ELU** activation instead of ReLU. • Residual connections also include **convolutions** in the identity path.

- Adds a **bottleneck residual block** with **5×5 filters** (instead of 3×3) for a **larger receptive field**.

> **Loss Functions**
>
> Loss functions guide the model during training by quantifying the error between predictions and ground truth. The **choice of loss function** is critical:

- It affects **which types of errors are prioritized**.

- Influences **training dynamics and convergence speed**.

- Should align with the task, data distribution, and analysis objectives. **1. Binary Cross-Entropy (BCE)**

![[AML-image379.jpg|523]]

> Measures the difference between predicted and actual probabilities.

- Commonly used in **binary classification** and can be adapted for segmentation.

- **Not ideal** for **imbalanced classes**, as it treats all pixels equally.

> **2. Weighted Binary Cross-Entropy (WBCE)**

![[AML-image380.jpg|616]]

> • Assigns **different weights** to each class to **compensate for imbalance**, giving more importance to the minority class (e.g., cells).

3.  **Focal Loss**

    - A variant of BCE that **down-weights “easy” examples** and focuses more on **difficult or rare samples**.

    - Particularly effective in handling class imbalance.

![[AML-image381.jpg|459]]

4.  **Dice Loss**

    - Based on the **Dice coefficient**, a measure of overlap between predicted and ground truth regions.

    - Especially well-suited for **segmentation tasks**, where spatial accuracy matters.

![[AML-image382.jpg|642]]

---
> [[AML 53 - Deep Dive – Object Recongition and Counting|← Deep Dive – Object Recongition and Counting]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 55 - Deep Dive – MLOps|Deep Dive – MLOps →]]
