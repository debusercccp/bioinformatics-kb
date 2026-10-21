---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 29
tags: [note, aml]
---

> [[AML 28 - Machine Learning Development · Hyper-parameters Tuning|← Machine Learning Development · Hyper-parameters Tuning]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 30 - Hands on Exploration – Understanding Neural Networks using TensorFlow Playground|Hands on Exploration – Understanding Neural Networks using TensorFlow Playground →]]

# Neural Networks

> The architecture of **biological neural networks (BNNs)** is still an active area of research. However, some regions of the brain have been mapped, and we know that:

- Neurons are relatively simple processing units.

- They are connected in large networks, often organized into **sequential layers**.

> **Artificial Neural Networks (ANNs)** are **inspired simulations** of biological ones. While there is **no one-to-one mapping** between artificial and biological neurons, the analogy remains a useful conceptual model.
>
> In the brain:

- The **cell body (soma)** is the computational centre.

- **Dendrites** are input channels.

- The **axon** is the output channel.

> We can model this biologically inspired structure as a **computational unit** that:

- Receives inputs

- Applies a computation (e.g., a **sigmoid function**)

- Sends the output to other units (nodes) **Why Neural Networks as ML Algorithms?**

> Neural Networks are powerful tools to **capture complex, non-linear relationships** among input features — more effectively than, for example, high-degree polynomials.
>
> **Key advantages:**

- **Non-linearity modelling**

- **Flexibility**

- **Scalability**

> NNs are well-suited for large-scale, high-complexity ML tasks such as:

- **Image classification** at massive scale (e.g., Google Images)

- **Speech recognition** (e.g., Siri, Alexa)

- **Recommendation systems** for hundreds of millions of users (e.g., YouTube)

- **Superhuman performance** in specific tasks (e.g., radiology, board games like Go via DeepMind’s AlphaZero)

> Important: NNs are highly effective for **well-defined, specific tasks**, not general-purpose reasoning.
>
> **Brief History of Neural Networks**

- **1943** – First artificial neuron model by **McCulloch and Pitts**

- **1960s** – Early success, then decline: **first AI winter**

- **1980s** – Revival of interest: new architectures, better training techniques

- **1990s** – Rise of alternative ML techniques (e.g., **SVMs**) with stronger theoretical backing → **second AI winter**

- **2000s–2010s** – Emergence of a new **AI spring** **Enablers of the modern AI era:**

- Availability of **Big Data**

- **Advances in hardware** (GPUs, TPUs)

- **Cloud computing**: democratized access to large-scale computation

- Improved **training algorithms** and optimization methods

> Today, **Machine Learning and Deep Learning** are **foundational technologies** driving global innovation and insight extraction from big data.

**LOGICAL COMPUTATION WITH NEURONS**

> The **McCulloch-Pitts neuron model**, later called an **artificial neuron**, is a simplified representation of a biological neuron. **Key Features:**

- Takes **1 or more binary inputs** (on/off values)

- Produces a **binary output** (also on/off)

- The output is **activated** only if the number of active inputs exceeds a certain **threshold** (e.g., ≥ 2 inputs)

> Despite its simplicity, this model showed that **networks of such neurons** can compute any basic **logical function** (AND, OR, NOT, etc.).

![[AML-image148.jpg|589]]

> **Threshold Logic Unit (TLU) / Linear Threshold Unit (LTU)**
>
> ![[AML-image149.jpg|317]]The **TLU (or LTU)** is an enhanced version of the McCulloch-Pitts model, introducing **numerical inputs and weighted connections**.

- Inputs and outputs are **real numbers**, not just binary

- Each input is associated with a **weight**

- The unit computes a **weighted sum** of the inputs

- Applies a **step function** (activation threshold)

- Produces a **binary output**

> A **single TLU** can act as a **linear binary classifier**, similar to Logistic Regression or Linear SVM**.**
>
> **The Perceptron**
>
> The **Perceptron** is an architecture composed of a **single layer of TLUs**, where:

- ![[AML-image150.jpg|382]]Each TLU is **fully connected** to all input features

- A special **bias input** is added (typically x0=1x_0 = 1x0=1) via a **bias neuron** that always outputs 1

> F**ully Connected (Dense) Layer:**
>
> When every neuron in one layer is connected to **all neurons in the previous layer**, it's called a **fully connected** or **dense** layer.

![](media/media/image153.jpeg)

- It allows the model to **shift the activation function** left or right.

- This is crucial for **learning flexibility** and **model expressiveness**.

- It increases the model's ability to **fit** a wide range of functions.

> A single-layer Perceptron:

- Can classify inputs into **multiple binary classes simultaneously**

- Serves as a **linear multi-class classifier**

> **Training a Perceptron**
>
> The **Perceptron training algorithm**, introduced by **Frank Rosenblatt**, is largely inspired by **Hebb’s rule**:

*"When a biological neuron consistently activates another, the connection between them is strengthened."*

> **Training Process:**
>
> ![[AML-image155.jpg|360]]The Perceptron processes **one training instance at a time**.

- For each input:

  1.  It makes a prediction.

  2.  If the prediction is **wrong**, it adjusts the **weights**.

> Specifically, it **reinforces** the weights of input features that should have contributed to the **correct output**. This
>
> is like **rewarding** the inputs that would’ve helped the model be correct.

![[AML-image156.jpg|642]]

> The main limitations are the fact that Each output neuron has a linear decision boundary.
>
> And as a result, Perceptrons cannot learn non-linear patterns (e.g., XOR problem).
>
> **Multi-Layer Perceptrons (MLP)**
>
> To address the linearity issue of simple Perceptrons, we **stack multiple layers** of neurons: This creates a **Multi-Layer Perceptron (MLP)** — a more powerful **artificial neural network (ANN)** architecture.
>
> ![[AML-image157.jpg|520]]
>
> **MLPs:**

- One or more **hidden layers** between input and output

- Use of **non-linear activation functions** (e.g., ReLU, tanh, sigmoid)

- Can model **non-linear relationships** and **complex functions**

> MLPs are the **foundation of deep learning** — they allow neural networks to:

- Learn hierarchical representations

- Solve tasks where single-layer networks fail

---
> [[AML 28 - Machine Learning Development · Hyper-parameters Tuning|← Machine Learning Development · Hyper-parameters Tuning]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 30 - Hands on Exploration – Understanding Neural Networks using TensorFlow Playground|Hands on Exploration – Understanding Neural Networks using TensorFlow Playground →]]
