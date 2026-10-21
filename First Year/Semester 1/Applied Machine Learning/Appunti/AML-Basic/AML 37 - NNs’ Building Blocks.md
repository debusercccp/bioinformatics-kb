---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 37
tags: [note, aml]
---

> [[AML 36 - Training An ANN|← Training An ANN]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 38 - Gradient Based Optimization|Gradient Based Optimization →]]

# NNs’ BUILDING BLOCKS

> **Data tensor**
>
> Let’s make data tensors more concrete, with some examples of what you may encounter in real life (or: “you might need to force your dataset into”).
>
> The data you’ll manipulate will almost always fall into one of the following categories:

- **Vector data**: 2D tensors of shape (samples, features)

- **Timeseries data** (or “sequence data”): 3D tensors of shape (samples, timesteps, features)

- **Images**: 4D tensors of shape (samples, height, width, channels) or (samples, channels, height, width)

- **Videos**: 5D tensors of shape (samples, frames, height, width, channels) or (samples, frames, channels, height, width)

> **Vector data: two dimensional tensors**

- every single data point can be encoded as a vector→ a batch of data will be encoded as a **2D vector data tensor** (i.e. an array of vectors) additional dimension are given by the two number given to the vector.

- the first axis is the **samples axes**, and the second axis is the **features axes**. This at mist of handwritten digit, were you have samples and features (populated by n of arrays as the sample).

> **examples**

1.  **A** **dataset of people,** where we consider e.g. each person’s age, ZIP code, and income.

> Each person can be characterised as a **vector** of **3** **values** (3 attributes), and thus an entire dataset of 100k people can be stored in a **2D tensor of shape** (100’000, 3).

2.  **A dataset of text documents**, where we represent each document by the counts of how many times each word appears in it (out of a dictionary of e.g. 20k common words).

> Each document can be encoded as a vector of 20k values (one count per word in the dictionary), and thus an entire dataset of 500 documents can be stored in a **tensor** of shape (500, 20’000).
>
> **Time series**
>
> Whenever time matters in your data (or the notion of **sequence** **order**), it makes sense to store it → a 3D time-series (or sequence) data tensor with an explicit time axis.

- ![[AML-image251.jpg|385]]every sample can be encoded as a **sequence of vectors** (i.e. a 2D tensor).

- a batch of data will be encoded as a 3D tensor which has thus **an explicit time axis.**

- the time axis is always the **second**

> **axis** (axis of index 1), by convention.
>
> A dataset of tweets. We encode each tweet as a sequence of 280 characters out of an alphabet of 128 unique characters. each character can be “**one-hot-encoded**” as a binary vector of size 128 (an all-0s vector except for a 1 entry at the index corresponding to the character) → each tweet can be encoded as a 2D tensor of shape (280, 128), and a dataset of 1M tweets can be stored in a tensor of shape (1000000, 280, 128)
>
> **Image data**
>
> Images typically have 3 dimensions: height, width, and color depth. This is for each sample, so **→ 4D image** data tensors.
>
> Grayscale images (e.g. MNIST) have only a single-color channel and could thus be stored in 3D tensors, by convention image tensors are always 4D, with a one-dimensional color channel for grayscale images.
>
> → a batch of 128 grayscale images of size 256×256 could thus be stored in a tensor of shape (128, 1, 256, 256), while a batch of 128 color images could be stored in a tensor of shape (128, 3, 256, 256).
>
> There are 2 conventions for their shapes:

- **the channels-last convention** (e.g. used by TensorFlow). it places the color-depth axis at the end: (samples, height, width, color_depth)

- **the channels-first convention** (e.g. used by Theano). it places the colour depth axis right after the batch axis: (samples, color_depth, height, width).

- And the Keras framework? Needless to say, it provides support for both formats.

> **Video data**
>
> A video can be interpreted as a sequence of frames, each frame being a colour image → a vector of 4D image data tensors → 5D video data tensors

![[AML-image252.jpg|468]]

> **Tensor Operations**
>
> Any computer program does what it does, if reduced to its core actions, via a combination of a relatively small set of binary operations on binary inputs. For example, take bits and perform combinations of ANDs, Ors, NORs. Every operation in a neural network is a **tensor operation** (like dot product, addition, activation). These operations have a **geometric interpretation**:

- **Tensors** are multi-dimensional arrays, representing data.

- Each layer **transforms input geometry** into a new form that is easier to separate, cluster, or interpret.

- **Affine transformations**, **rotations**, and **scalings** are all tensor operations.

> Much along the same lines, all “transformations” that a deep NN can learn can be reduced to a handful of **tensor operations** applied **to tensors of numerical** **data**.
>
> ![[AML-image253.jpg|631]]
>
> Dense layers on top of each other. Take one:

- this layer can be interpreted as a **function**: it takes as “**input**” a tensor and returns as “**output**” a new representation of the input tensor.

> The function specifically does a dot product, an addition and then applies a function **relu**(x) (which is basically max(x,0)).

![[AML-image254.jpg|395]]

> The **relu** operation and the addition are ***element-wise*** operations

- operations applied independently to each entry in the tensors being considered

- highly adequate to massively parallel implementations (i.e. *vectorized* implementations)

> **From a geometric interpretation of tensor operations**
>
> We are considering a **combination** of **tensor** **operation**, in a very **high dimensional complex space**, that is a long series of operation. Output inside data, visually we can thigh this as a process that is trying to find from the **input** the **output** that is a bit clear. Steb by step going from a paper bowl, then many operations to try to unnoble it ad extract many paper layers, applying them **one** **after** **the** **others**, sequentially going from one to the others. If I change the operations, I can go to the right and wrong direction.
>
> The tensors’ content can be interpreted as **point coordinates in some geometric space** → tensor operations have a geometric interpretation

- e.g. a vector A\[1,2\] can be interpreted as the coordinate of a point in a 2**D space**, and one can even draw a vector as if it was a position vector of a physical point w.r.t the origin of a coordinate system.

- if you take another vector and make the sum, analytically or visually, you get the **coordinate of a third point** in the same geometrical space This is general - elementary geometric operations such as affine transformations, rotations, scaling, ... can be expressed as **tensor operations.**

- e.g. a rotation of a 2D vector by an angle θ can be achieved via a dot product with a 2×2 rotation matrix R=\[u,v\], where u and v are vector of the plane, namely u=\[cos(θ), sin(θ)\] and v=\[-sin(θ), cos(θ)\]

![[AML-image255.jpg|532]]

> Think of a neural network as a process that:

- Starts with **raw, tangled data** (like a crumpled paper ball**),**

- Then applies **layer after layer** of transformations**,**

- Gradually **unfolding and flattening** it into a representation that is easier to interpret or classify.

> **How Do Neural Networks Learn?**

- Each **dense layer** applies a geometric transformation.

- The model learns by **backpropagation** + **gradient descent**.

- **Activation functions** ensure non-linear learning.

- Every transformation can be seen as a **tensor operation** with geometric meaning.

- Training is iterative: forward → loss → backward → update → repeat

•

---
> [[AML 36 - Training An ANN|← Training An ANN]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 38 - Gradient Based Optimization|Gradient Based Optimization →]]
