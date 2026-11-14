---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 48
tags: [note, aml]
---

> [[AML 47 - Memory Cells|← Memory Cells]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 49 - Not Saturating Activation Functions|Not Saturating Activation Functions →]]

# Handling Long Sequences: Part 1

> **Why Simple RNNs Struggle with Long Sequences Strengths of Simple RNNs**

- Handle sequences and time series well **if sequences are short**

- Can learn dependencies over recent time steps (like 5–10 steps)

- Lightweight and fast to train compared to advanced architectures

> **Weaknesses on Long Sequences:** when used on long sequences (e.g., long text, long time series), **two classes of problems** arise:

1.  **Problems Shared with Deep Neural Networks:** simple RNNs, when unrolled over many time steps, behave like **very deep neural networks**. This means: **Vanishing/Exploding Gradients**

    - Gradients **shrink** → early layers (early time steps) receive almost no signal to update

    - Or gradients **blow up** → cause **unstable training**, often leading to NaNs **Slow and Difficult Training**

    - Many parameters → longer time to converge

    - Gradients might take longer to stabilize **Overfitting Risk**

    - Deep models = many parameters

    - Need **lots of data** to avoid memorization

    - Noise or insufficient data → model memorizes instead of learning patterns

2.  **Problems Specific to RNNs on Long Sequences: Memory Loss Over Time** • Basic RNNs **forget earlier inputs** as the sequence gets longer

    - This is due to the **recursive update of the hidden state**:

> ![[AML-image340.jpg|379]]

- Over many steps, h(t-1) becomes **less influenced by earlier x values**

- Network **fails to capture long-term dependencies**

> **RNN as a Shallow Memory**
>
> Think of a simple RNN like a person trying to remember a list by repeating it over and over, but **only the last few items stick**. Without a stronger memory mechanism, everything from the start fades.
>
> **Vanishing/Exploding gradients BP recap:**

- the BP algo works by going **from the output layer** to the **input layer,** and it **propagates** the error gradient along the way.

- Once the BP also has computed the gradient of the cost function regarding **each** **parameter** in the network, it uses these gradients to update each parameter with a GD step **The problem:**

- Unfortunately, gradients often get **smaller** and **smaller** as the algorithm progresses down to the lower layers

- As a result, the GD update leaves the lower layer connection weights virtually unchanged. Therefore, training never converges to a good solution, which is why we call this the **vanishing gradients** problem.

- In some cases, the opposite can happen: the gradients can grow bigger and bigger until layers get insanely **large weight updates** and the algorithm diverges. This is the **exploding gradients** problem (this surfaces e.g. in RNNs).

> **DNN suffer from unstable gradients: Solutions**
>
> So, how to **alleviate** the unstable gradients problem, and allow a proper flow of gradients? We need the variance of the outputs of each layer to be equal to the variance of its inputs, as well as we need the gradients to have equal variance before and after flowing through a layer in the reverse direction.
>
> Imagine a chain of **microphone amplifiers**:

- If each one is **too quiet**, the final signal is inaudible (vanishing gradients)

- If each one is **too loud**, the signal distorts (exploding gradients)

- **Goal**: Keep signal strength constant across all layers

> In deep learning terms: we want the **output variance** and **gradient variance** of each layer to match the input's, to maintain stable learning. For stable forward and backward propagation:

- **Variance of activations** after each layer ≈ variance of inputs

- **Variance of gradients** across layers remains stable

> This is **not possible** unless the number of inputs = number of outputs per layer (i.e., fanin = fanout)
>
> **Weight Initialization Strategies: Xavier Initialization (Glorot Initialization)**

- Works well with **sigmoid** and **tanh** activations

- **Assumes input and output variances** should be equal

![](media/media/image343.jpeg)

> **LeCun Initialization**

- Proposed by **Yann LeCun (1990s)**, best for **SELU** and **sigmoid.**

- Uses only the **fanin**.

- If fanin = fanout, it's **equivalent to Xavier.** **He Initialization (He et al., 2015)**

- Best for **ReLU** and its variants (Leaky ReLU, ELU)

- Assumes ReLU kills half of activations → needs more variance This initialization trick was a **turning point** in deep learning:

- Enabled successful training of **very deep networks**

- Improved **convergence speed**

- Reduced dependence on hand-tuned learning rates

---
> [[AML 47 - Memory Cells|← Memory Cells]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 49 - Not Saturating Activation Functions|Not Saturating Activation Functions →]]
