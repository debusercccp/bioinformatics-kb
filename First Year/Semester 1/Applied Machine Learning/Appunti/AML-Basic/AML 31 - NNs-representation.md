---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 31
tags: [note, aml]
---

> [[AML 30 - Hands on Exploration – Understanding Neural Networks using TensorFlow Playground|← Hands on Exploration – Understanding Neural Networks using TensorFlow Playground]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 32 - Non-linear Classification|Non-linear Classification →]]

# NNs-representation

> Understanding some standard **terminology** and **notations** is essential when dealing with artificial neural networks (ANNs), especially as they scale in complexity.
>
> **Bias Unit**

- A **bias neuron** (or **bias unit**) is a special input node x0 that is **always equal to 1**.

- It is added to every layer except the output layer.

- Its role is similar to the intercept term in linear models — it allows the activation function to be shifted left or right, **increasing model flexibility**.

- Bias values have their own associated weights

> **Activation Function (Non-Linearity)**
>
> Instead of calling it "non-linearity", we refer to it as the **activation function**. Each **neuron applies an activation function** to its input — typically:

- **Sigmoid** (or logistic): σ(𝑧) = <sup>1</sup><sub>−𝑧</sub> σ(z)

1+𝑒

- Other common functions include ReLU, tanh, and softmax (depending on task).

> The activation function allows the network to **learn non-linear patterns**. The **step function** used in early models is now replaced by smoother alternatives like **sigmoid** or **ReLU**, which are differentiable and trainable using gradient descent.
>
> **Weights and Parameters**
>
> The parameters of the network (traditionally θ\thetaθ) are now called **weights** and denoted by www. Each **connection** between two neurons has an associated **weight**, which is learned during training. These weights **modulate the signal strength** from one neuron to the next.
>
> **A Single Artificial Neuron (Logistic Unit)**
>
> The **basic computational unit** is a logistic neuron:
>
> ![](media/media/image160.jpeg)It takes **real-valued inputs** (plus bias), computes a **weighted sum**, and applies a **sigmoid activation**.
>
> Formula:
>
> ``` math
> h(x) = \sigma\left( w^{T}x \right) = \frac{1}{1 + e^{- w^{T}x}}
> ```
>
> Here:

- 𝑥 is the **input vector** (including bias: 𝑥 0= 1)

- 𝑤 is the **vector of weights**

- ℎ(𝑥) is the **output** of the neuron

> ![[AML-image162.jpg|549]]
>
> **From One Neuron to Multi-layer Networks Network Structure:**
>
> **Layer 1**: Input layer (not a computational layer)

- **Layer 2**: First hidden layer (contains real computation)

- **Layer 3**: Output layer

> Each hidden or output layer consists of:

- **Neurons** (also called **units**), denoted as 𝑎<sub>𝑗</sub><sup>(𝑙)</sup>

- A **bias neuron** ( ex. 𝑎<sub>0</sub><sup>2</sup>in the hidden layer)

> **Forward Propagation: Matrix View**

![[AML-image163.jpg|490]]

> The **core computation** from one layer to the next is a **matrix operation**:

- Each transition from layer j to layer j+1 is defined by a **weight matrix** 𝛩(𝑗)

- 𝛩(𝑗) maps the activations from layer j (including bias) to layer j+1 **Dimensions** If:

> Layer j has sj units (not counting bias)
>
> ![[AML-image164.jpg|565]]

- Layer j+1 has sj+1 units has dimensions 𝑠<sub>(𝑗+1)</sub> × (𝑠<sub>𝑗</sub> + 1) **Computation for each layer:**

> 𝑧![[AML-image165.png|129]]𝑒𝑛 𝑎(𝑗+1) = 𝑔(𝑧(𝑗+1))
>
> Where:

- 𝑧 is the **pre-activation** (weighted input)

- 𝑎 is the **activation** (after applying 𝑔)

- 𝑔 is typically the **sigmoid** or **ReLU** **Example** If you have:

- 3 input features + bias → input layer has 4 neurons (1 bias + 3 features)

- Hidden layer with 3 neurons + bias → 4 neurons in layer 2

> 1 output neuron in the output layer
>
> ![[AML-image166.jpg|423]]
>
> Then:

- Θ(1) is 3×4 (maps 4 inputs → 3 hidden units)

- Θ(2) is 1×4 (maps 4

> hidden activations → 1 output)
>
> The **power** of a neural network does **not lie in the input or output layers**, but in the **hidden layers**, where abstract patterns are extracted and transformed. The more hidden layers (depth), the more complex the function the network can model — but this also introduces **computational cost** and **training challenges**. We have previously given a **mathematical definition** of how to compute the output (or **hypothesis**) of a neural network (NN). Now we focus on:

- How to **compute this efficiently** using a **vectorized implementation**

- Building **intuition** about why NNs can learn **complex, non-linear hypotheses**

![[AML-image167.jpg|476]]

> To compute the output of a neural network efficiently, we **vectorize the operations**. Rather than looping over each neuron and each connection, we work with **matrices and vectors**:

- Each **layer**'s computation is represented as a **matrix multiplication** followed by an **activation function**

![](media/media/image170.jpeg)

> Input= X activation of layer. This process — computing activations layer by layer using matrix operations — is called **forward propagation**. If you're using the sigmoid activation function, each layer is essentially performing **logistic regression**, but on **features learned by the previous layer** rather than on raw input.
>
> ![](media/media/image1550.jpg)
>
> At each step:

- You're **not just predicting the final output**

- Each layer is learning its **own intermediate representation** of the data (a kind of "feature engineering")

> .

![](media/media/image177.jpeg)

> We are not starting from Xs but from as in this case.
>
> ![](media/media/image183.jpeg)
>
> Think of a neural network as a **machine learning system that builds its own features**:

- Each hidden layer is not directly concerned with the final task (e.g., cat vs. dog classification)

- Instead, each layer **extracts useful patterns** from the previous one

- The network **digests the input step by step**, gradually transforming raw data (like pixel values) into **higher-level abstractions** (like shapes, textures, or object parts)

> This layered approach allows neural networks to learn **complex non-linear hypotheses** — much more powerful than a single logistic regression model could ever achieve.
>
> Takeaway message:

- A **neural network** can be viewed as **stacked logistic regression models**, where each layer operates on the **output of the previous one**, not on the original input.

- **Forward propagation** lets you compute the output efficiently, using vectorized operations.

- Each layer **learns meaningful features** to pass forward, enabling the whole network to represent **highly complex, non-linear decision boundaries**.

> Let me know if you'd like this turned into a **slide**, **diagram**, or **formula sheet** to study or teach more effectively.

![](media/media/image188.jpeg)

---
> [[AML 30 - Hands on Exploration – Understanding Neural Networks using TensorFlow Playground|← Hands on Exploration – Understanding Neural Networks using TensorFlow Playground]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 32 - Non-linear Classification|Non-linear Classification →]]
