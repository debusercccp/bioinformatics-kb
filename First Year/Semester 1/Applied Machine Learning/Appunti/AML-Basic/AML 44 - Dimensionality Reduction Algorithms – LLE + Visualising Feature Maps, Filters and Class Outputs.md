---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 44
tags: [note, aml]
---

> [[AML 43 - Dimensionality Reduction + Dimensionality Reduction Algorithms – PCA|← Dimensionality Reduction + Dimensionality Reduction Algorithms – PCA]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 45 - Autoencoders|Autoencoders →]]

# Dimensionality Reduction Algorithms: LLE

> **LLE: Locally linear embedding** a Manifold Learning technique, it does not rely on projections like the previous (PCA) algos. LLE works by first **measuring how each training instance** linearly relates to its closest neighbours and then looking for a low-dimensional representation of the training set where these local relationships are best preserved.

- **Pros**: particularly good at unrolling twisted manifolds, especially when not too much noise

- **Cons**: (at least in sklearn) computationally scales as m2, i.e. poorly to very large datasets

> ![](media/media/image2630.jpg)

## VISUALISING FEATURE MAPS, FILTERS AND CLASS OUTPUTS

> ![[AML-image314.jpg|387]]VGG is a classical CNN from 2014. VGG has 16 layers.
>
> **VGG architecture**
>
> **input:** An image (typically 224x224 RGB).
>
> Layers**:**

- 13 Convolutional layers

- 5 Max-Pooling layers

- 3 Fully Connected (Dense) layers

> **Output:** SoftMax layer for classification
>
> Each **Conv layer output** is a **3D volume**:

- **Height × Width** → spatial dimension of the feature map

- **Depth (Channels)** → each filter’s output (i.e., feature map) These depth channels are also called **intermediate activations**.

> Let’s see inside the network. Let’s start visualising the feature map. Remember the output of a conv layer is a 3D volume and every **feature map** is the outcome of a specific filter. **Visualizing Feature Maps**

- Each filter produces one **feature map**

- By visualizing them, we see **what pattern a filter reacts to**

- **BlockX_ConvY** notation is used to refer to layers

> Any deep depth channel you have is a feature map connected to set of feature exposed specifically to this depth channels are also called **intermediate activation**, that is what are you learning set of features after set of features, single one are 2D things only, planes inside that volume.
>
> We want to visualize exactly those. So we take input image, pass it through the CNN and try to see the intermediate activation. We will check different feature map in that volume, checking how the original input is transformed.

![[AML-image315.jpg|476]]

> We can check some block and convolutional layer, **BlockX-convY** gives us the block number and conv layer number. The more the number block is high the more you ultimate convolutional layer in that specific block. Regions activate in the intermediate activation are those where the **filter is detecting some pattern**: highlighted area are the one reacted positively to the filter used. It looks like the filter is trying to **encode** **something** to be visually recognise as eye and nose.
>
> I can check more feature map. So I can number these thing and select them more. The first thing is to check some convolution per block. As we discussed last time is evident that on average what is noticeable is the overall vision of thigs. You can be focusing in different details. You still see a cat in the first images, but the more you go on the less of a cat you can recognize.
>
> ![[AML-image316.jpg|411]]

- Feature maps from first layer (block1_conv1), lower-level, retain most of the info in the original image. In CNN architectures, first layers usually act as **edge/shape** detectors

- Start to go deep, and feature maps will look more like an **abstract** **representation** of the original (see block3_conv1)

- Go even deeper, and higher-level feature maps will encode **high level concepts** like “cat nose” or “dog tail”. They indeed contain less information about the image and more about the class of the image.

- Overall, feature maps become **sparser** as we go further, meaning the filters detect less features (every image contains shapes/edges → many features; then, complex stuff like “dog tail”, not in every image → fewer features).

> **Visualizing filters**
>
> Filters are the main structure used in the Conv operation. The filter is the main structure used in the conv operation. Visualising **CNN filters is not reasonable**, the idea is to visualize the pattern each filter maximally respond to, where each filter is activated the most.

- **Filters** are not directly interpretable like images

- But we can generate images that activate a filter the most

> **(**also known as ***feature visualization*)**
>
> There are tricks nowadays to do it. An artificial way not to show the filter but **images activating specific filters.** So enhanced images where the filter is very active. We take the last layer of every convolutional block. You can see images that **maximise specific filters**. From the very beginning we will look for pattern pretty easy. Images at the end layers are very specific. I’m looking form patter way more complicated than a horizontal line.
>
> So, some pictures activate the layer and thus are corrected. colour here don’t make particular sense here: at the very beginning might be **looking** **for** **colours**.
>
> If in every position of the picture there is a bird, the function will be activate: **translational invariance** of a CNN. So, for feature maps: lower-layers encode/detect simple structures and as we go further the layer build on top of each other and learn to encode more complex patterns.
>
> ![[AML-image317.jpg|325]]**Visualising class outputs**
>
> What comes out from **multi-class classification**. We want to visualize the very final **SoftMax layer** in output. You can choose a category of object and you ask the CNN to generate an image to represent **maximally** **that** **image**. The method to do this is a trick, is a similar method to the one used to visualize the filter, from blank, you generate the image to maximise probability
>
> to be generated in a certain category. The results show how the CNN sees the elements of a specific category.

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p><strong>Concept</strong></p>
</blockquote></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote>
<p><strong>Feature Maps</strong></p>
</blockquote></td>
<td>3D outputs of conv layers showing activations from filters</td>
</tr>
<tr>
<td><blockquote>
<p><strong>Intermediate Activations</strong></p>
</blockquote></td>
<td>Deep layer outputs, showing learned features</td>
</tr>
<tr>
<td><blockquote>
<p><strong>Filter Visualization</strong></p>
</blockquote></td>
<td>Shows what patterns each filter is detecting</td>
</tr>
<tr>
<td><blockquote>
<p><strong>Class Visualization</strong></p>
</blockquote></td>
<td>Generates images to visualize what a class "looks like" to the model</td>
</tr>
<tr>
<td><blockquote>
<p><strong>Translational Invariance</strong></p>
</blockquote></td>
<td>CNNs detect features regardless of where they appear in the image</td>
</tr>
</tbody>
</table>

---
> [[AML 43 - Dimensionality Reduction + Dimensionality Reduction Algorithms – PCA|← Dimensionality Reduction + Dimensionality Reduction Algorithms – PCA]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 45 - Autoencoders|Autoencoders →]]
