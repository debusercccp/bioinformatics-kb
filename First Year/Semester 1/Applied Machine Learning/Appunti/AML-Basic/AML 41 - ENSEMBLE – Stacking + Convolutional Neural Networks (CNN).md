---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 41
tags: [note, aml]
---

> [[AML 40 - Random Forests|← Random Forests]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 42 - Support Vector Machines (SVM)|Support Vector Machines (SVM) →]]

# ENSEMBLE: Stacking

> Stacking is another Ensemble method that aggregate predictions form predictors in the ensemble **not using trivial functions** (such as hard voting) but by training a model to perform such aggregation. The additional intelligence lies in a **final** **predictor** (blender, or metalearner) whose task is to take intermediate predictions as inputs and to make the final prediction.
>
> ![[AML-image269.jpg|320]]
>
> The training set is **splitted into subsets**: the first one is used to **train** the **first layer**, the second one is used to create the training set used to **train** the **second layer** ( using predictions made by the predictors of the first layer), the third one is used to create the training set to train the **third layer** (using predictions made by the predictors of the second layer).

![[AML-image270.jpg|642]]

## CONVOLUTIONAL NEURAL NETWORKS (CNN)

> The **most popular Deep Learning architecture,** started with AlexNet in 2012 and grew since then. Its area of application is computer vision, as it is excellent in any 2D/3D image-related tasks, and successfully applied also to recommender systems, NLP and more.
>
> Advantages of a CNNs

- **superhuman accuracy**: beating humans in most image classification tasks.

- it performs **automatic feature extractions**, i.e. detects the important features without any human supervision (feed it with pics of cats and dogs and it will learn distinctive features for each class by itself).

- it is **computationally efficient**: It uses convolution and pooling operations and performs parameter sharing. This enables CNN models to run on any device, making them universally attractive.

> We will discuss some of the best CNN architectures, as well as some visual tasks, e.g.:

- **object detection** (classifying multiple objects in an image and placing bounding boxes around them)

- **semantic segmentation** (classifying each pixel according to the class of the object it belongs to)

> **Receptive fields and hierarchy of neurons : the Architecture of the Visual Cortex most relevant observations**:

- “**neurons in general get active on small visual areas**”: many neurons in the visual cortex have a small local “receptive field”, i.e. they react only to **visual** **stimuli** located in a limited region of the visual field. The receptive fields of different neurons may overlap, of course, and altogether they tile the whole visual field.

- **“neurons get active on patterns”:** some neurons react only to images of **horizontal** **lines**, while others react only to lines with **different** **orientations** (two neurons may have the same receptive field - previous bullet - but react to different line orientations).

- “**some neurons work on larger visual areas**”: they have larger receptive fields, and they react to more complex patterns that are combinations of the lower-level patterns.

> These observations led a classification of **higher-level** and **lower-level neurons**, and to the idea that higher-level ones are based on the outputs of neighbouring lower- level ones (see Figure). This powerful architecture is able to detect all sorts of complex patterns in any area of the visual field.
>
> Summary:
>
> most biological neurons in the visual cortex respond to specific visual patterns in small regions of the human visual field (“**receptive fields**”)

- as the visual signal makes its way through consecutive brain modules, neurons respond to more complex patterns in larger receptive fields.

![[AML-image271.jpg|642]]

> These studies of the visual cortex inspired the **neocognitron**, introduced in 1980 \[RefFukushima\], which gradually evolved into what we now call a **convolutional neural networ**k. Were later introduced two new building blocks: **convolutional layers** and **pooling layers**.
>
> N.B. : since for larger imagers a huge number of parameters is required, a deep neural network with fully connected layers wouldn’t be enough. **MNIST** has 28x28 images. A 100×100 image has 10,000 pixels, so with aNN with 1,000 neurons in the first layer and beyond, one easily get to millions of connections, and that’s just the first layer.
>
> **Convolution**
>
> This architecture allows the network to concentrate on **small low-level features** in the first hidden layer, then assemble them into **larger** higher-level features in the next hidden layer, and so on. A convolution is a mathematical operation on 2 functions f and g that produces a third function that expresses how the **shape** of one is modified by the other.

- **Function f**: the *input signal* — e.g., an image, audio, or a time series

- **Function g**: the *filter* or *kernel* — a small matrix used to detect specific features

![[AML-image272.jpg|642]]

- The filter g is **reversed** and **shifted**, then **multiplied pointwise** with f and **integrated** (summed) over.

- In deep learning, we deal with **discrete** and **finite** signals, so integrals become sums.

> In practice, signals like images or audio are **finite** and **discrete**, so the sums are over finite ranges.
>
> ![[AML-image273.jpg|642]] basically the integral of their product after one is reversed and shifted.
>
> Functions are not considered over all **R**, but we take f as one signal (data) of finite length (like a 1D array whose elements are only in part not equals to zero) and another function g as a filter (or kernel).

- signal → an image (simple or a 3D MRI image), a sound wave, a time series, • filter → a discrete Laplacian

> ![](media/media/image232.jpg)

- The **convolution operation** is applied

> between the input and the filter(s) • Output is a **feature map** that
>
> highlights where the filter found a pattern • Often followed by:

1.  **Activation functions** (e.g., ReLU)

2.  **Pooling layers** (downsample)

3.  **More convolutions** to build complex features

> **Convolution 2D**

![[AML-image276.jpg|510]]

> The **convolution** **operation** is performed **sliding** the filter over the input, and at every location, an element-wise matrix **multiplication** is **performed**. The results are summed and the feature map is filled.

![[AML-image277.jpg|491]]

> Real image convolutions are performed in 3D as a single image is represented as a 3D matrix with dimensions of height, width and depth.

![[AML-image278.jpg|642]]

> Apply more filters (say, 10 in total). You get **10 32x32x1 feature maps**. Stacking them along the depth dimension give us the **final output** of the convolution layer: a volume of size 32x32x10, shown as the large blue box on the right. Note that the convolution operation for each filter is performed independently and the resulting feature maps are disjoint.
>
> The actual values in the final feature maps (one per filter) are **not actually the sums** of the products, but the output of the activation function applied to them.
>
> Convolutional layers process input data using **filters** (also called kernels) that scan over the input. Two critical hyperparameters that affect **how** the scanning happens are:
>
> **Stride**
>
> The stride **specifies how much we move** the convolution filter at each step, Default is 1. Bigger strides yields less overlap between the receptive fields and makes the resulting feature map smaller. A **stride of 1** keeps more detail and creates a larger output. A **stride \> 1** is like zooming out: you skip some positions and get a **compressed** representation.
>
> **Padding**
>
> If you constrain the convolution filter to be contained in the input, feature maps are **smaller** than the **input**, This is often not desirable in CNNs as it yields smaller feature maps shrinking at each layer. The filter cannot be applied to the border pixels without going out of bounds.

- **Padding = "fence"** around your data so the filter can fully scan edges.

- Avoids **progressive shrinking** of feature maps across layers.

> **Borders of the convolution**:

- **Full**: outcome is the full convolution.

- **Same**: pad with the numbers on the edge. Outcome is the central part of the convolution, of the same size as the original input.

- **Valid**: no padding. Outcome restricted to only those parts of the convolution that are computed w/o the zero-padded edges.

![[AML-image279.jpg|588]]

> **Pooling layers**
>
> After one or more convolution operations we apply **pooling** to **reduce** **the** **dimensionality**,
>
> The goal is to **reduce the number of parameters**, as it shortens the training time and fights overfitting. This is done by adding a **pooling layer**.

![[AML-image280.jpg|642]]

> Deep Learning is all about “**clever compression**”, i.e. find low dimensional representations of the input that **disentangle** the **distinguishing** **variation** **factors** in your data). Pooling layer down samples each feature map independently, reducing the height and width, keeping the depth intact.
>
> **Padding Vs Pooling**
>
> ![](media/media/image283.jpeg)
>
> For a **typical CNN architecture**:

- convolution is done with 3x3 windows, stride 1 and with padding

- pooling is performed with 2x2 windows, stride 2 and no padding

> **Hyperparameters of CNNs**

- **Filter size**: not so many options. Typically, 3x3 filters, but 5x5 or 7x7 are also often used (depending on the application). All filters are **3D** (we often omit thinking of depth, as it is not changing through layers) An apparently useless 1x1 filter might be used.

- **Filter count**: quite some variability. Any power of 2 between 25 and 210. More filters give a more powerful model, but more params expose to risks of overfitting. Best practices indicate to start with small \# filters in the initial layers and progressively increase as we go deeper into the NN.

- **Stride**: default is 1.

- **Padding**: yes, usually it is used.

> After convolution + pooling layers, in a CNN architecture we add a couple of fully connected (FC) layers. Layers need to be **properly connected**, though:
>
> Conv/Pooling layers are **3D volumes**. but a FC layer expects to get a 1D vector of numbers, So, the output of the final pooling layer need to be flattened in **1D** and then sent as input to the final FC layers.
>
> Basic CNN architecture

![[AML-image283.jpg|642]]

> Feature extraction via **Conv layers**: it is not easy to automatic detect meaningful features in an image given only image+label. Conv layers can learn such complex features by building on top of each other.
>
> Early layers learn to detect **simple patterns** like:

- **Edges**

- **Corners**

- **Lines**

> Middle layers start detecting:

- **Simple shapes**

- **Combinations** of edges (e.g. circles, rectangles) Deeper layers identify:

- More abstract or **high-level patterns**

- **Object parts** (like a cat’s tail or a dog’s nose)

> **first layers detect edges**; the next layers combine them to detect shapes; to following layers merge this information to infer perhaps a **specific object** (e.g. a cat’s tail). Note that a CNN **does not know what a tail is** - but, by seeing many of these objects in images, it learns to detect it as a feature once it sees one.
>
> As such, Cons layers are the **horsepower** of a **CNN**. Most of the work is done here! Then, next is:
>
> **Classification via FC layers**: act as a classifier on top of such features, i.e. learn how to use the features produced by Conv layers to correctly classify the images. Once features have been extracted by the convolutional layers, the fully connected layers take over to **make a final decision**.

- **The FC layers** act as a classifier.

- They receive the **high-level features** (e.g., "has whiskers", "round ears") and learn how to combine them to make a correct prediction (e.g., "cat").

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><blockquote>
<p><strong>HANDS -ON : DROP-OUT</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<blockquote>
<p>Dropout is a regularization technique used during training of neural networks to prevent overfitting — when a model performs very well on training data but poorly on unseen data. At each training step, randomly “drop” (i.e., deactivate) a proportion p of the neurons in the network. That means:</p>
</blockquote>
<ul>
<li><p>With probability p, a neuron (along with its incoming and outgoing connections) is disabled just for that iteration.</p></li>
<li><p>On the next iteration, a new random set of neurons will be dropped.</p></li>
<li><p>This happens only during training, never at test time.</p></li>
</ul>
<blockquote>
<p>The dropout rate is the hyperparameter p — commonly set to 0.5, meaning 50% of neurons are randomly dropped during each training pass. Disabling neurons on purpose may seem counterintuitive, but it actually improves performance. It:</p>
</blockquote>
<ul>
<li><p>Prevents the network from becoming overly reliant on specific neurons.</p></li>
<li><p>Forces the network to distribute learning across many neurons, promoting redundancy and robustness.</p></li>
<li><p>Acts like training many different subnetworks and averaging their outputs (an implicit ensemble effect).</p></li>
</ul>
<blockquote>
<p>Imagine a team where only a few key members do all the work. If they’re absent, the team collapses. Dropout is like randomly removing team members during practice so that everyone learns to contribute.</p>
</blockquote>
<table>
<colgroup>
<col style="width: 42%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p>During Training</p>
</blockquote></th>
<th>During Testing</th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote>
<p>Neurons are randomly dropped with prob. p</p>
</blockquote></td>
<td>No dropout applied</td>
</tr>
<tr>
<td><blockquote>
<p>Weights are scaled appropriately at each step</p>
</blockquote></td>
<td>We use all neurons but scale outputs to match expected activations</td>
</tr>
</tbody>
</table>
<p>Where Is Dropout Applied?</p>
<ul>
<li><p>Input layer (sometimes)</p></li>
<li><p>Hidden layers (most common)</p></li>
<li><p>Output layer — dropout is not applied here</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><blockquote>
<p><strong>HANDS -ON : DATA AUGMENTATION IN DEEP LEARNING</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<ul>
<li><p>Overfitting happens when a model performs well on training data but fails to generalize to new, unseen data. One core reason is too little training data.</p></li>
<li><p>In theory, with infinite diverse training data, a model wouldn't overfit. But in practice, it's hard and expensive to collect more real data.</p></li>
</ul>
<p>Data augmentation is a strategy to artificially increase the size and diversity of your training dataset — using your existing data.You create realistic variations of your training data through transformations that don’t change the class label. The idea: a slightly rotated image of a cat is still a cat. These new samples are meant to help the model learn robustness to natural variations.</p>
<table style="width:85%;">
<colgroup>
<col style="width: 35%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr>
<th>Transformation</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td>Rotation</td>
<td>Tolerate rotated subjects</td>
</tr>
<tr>
<td>Translation (shifting)</td>
<td>Learn invariance to object position</td>
</tr>
<tr>
<td>Scaling/resizing</td>
<td>Handle objects of various sizes</td>
</tr>
<tr>
<td>Flipping (e.g. horizontal)</td>
<td>Especially effective in symmetrical images</td>
</tr>
<tr>
<td>Contrast/brightness changes</td>
<td>Deal with different lighting conditions</td>
</tr>
<tr>
<td>Zoom, cropping</td>
<td>Focus on part of the object</td>
</tr>
</tbody>
</table>
<ul>
<li><p>Forces the model to <strong>focus on essential features</strong>, not memorized positions.</p></li>
<li><p>Promotes <strong>invariance</strong> to variations commonly seen in real-world data.</p></li>
<li><p>Acts as a <strong>regularization technique</strong>, reducing overfitting.</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

---
> [[AML 40 - Random Forests|← Random Forests]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 42 - Support Vector Machines (SVM)|Support Vector Machines (SVM) →]]
