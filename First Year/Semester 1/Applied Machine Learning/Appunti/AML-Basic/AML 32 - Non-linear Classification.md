---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 32
tags: [note, aml]
---

> [[AML 31 - NNs-representation|← NNs-representation]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 33 - Decision Trees (DT)|Decision Trees (DT) →]]

# Non-linear Classification

> How a NN can compute a complex non-linear function of the input? We are analysing a simple **feedforward neural network (NN)** where the output hypothesis h is computed using a **sigmoid activation function** over a linear combination of inputs and weights

![](media/media/image192.jpeg)

> can build a **truth table** with different input combinations and compute the sigmoid to approximate logical gates like AND, OR, NOT.

![[AML-image194.jpg|593]]

- XOR: exclusive one

- XNOR: represent simplified case.

> **AND Gate**
>
> Suppose you take a network to demonstrate set of weights that can describe logical and. let’s consider a simple NN with:

- ![[AML-image195.jpg|462]]Two inputs: X1,X2.

- One bias input: X0

> =1

- One output neuron using sigmoid activation

> You can find a set of weights θ such that the sigmoid output is close to:

- **1** when both X1=1 and X2=1

- **0** in all other cases

> This replicates the behaviour of the logical **AND:** Try this with specific weights (e.g., θ=\[−30,20,20\]) and verify that the output behaves like an AND gate.
>
> ![[AML-image196.jpg|281]]
>
> ![[AML-image197.jpg|274]]
>
> **Sigmoid:** something of the very left, the g value would be very close to zero, following how the sigmoid goes. I do the computation for all cases, getting: a column with something positive only when positive x1 and x2 are positive. Other ways is zero. This is an implementation that the logical function of our artificial neural network can be approximately nicely to any and entity. I can use one network with single layer that does it. My problem: not having the AND.
>
> **OR Gate**
>
> Similarly, you can implement an **OR gate**:

- Output should be **1** when **at least one** of x1x_1x1 or x2x_2x2 is 1

- Only return **0** when both are 0

> This can also be achieved with a **single-layer sigmoid neuron**, using a different set of weights.

![[AML-image198.jpg|412]]

> We get one in all cases apart when both are zero, so at least one is needed. NOT Gate (Negation) he **NOT** gate can be implemented with a single input (plus bias):

- If x=0x = 0x=0, output close to **1**

- If x=1x = 1x=1, output close to **0**

> Again, by selecting the appropriate weights (e.g., θ=\[10,−20\]) this behaviour can be modelled with a **single sigmoid unit**. However, note that the **architecture** for negation is different — it’s a one-input neuron rather than two.

![[AML-image199.jpg|567]]

> We should try the negation, with only one input: you have one architecture and the bias neuron. Found a set of weights, I got a sigmoid that gives me one for zero input and zero if input is one. That is ok compatible with approximation. The architecture is different form negation. Let’s put all together
>
> XNOR
>
> ![[AML-image200.jpg|445]]
>
> **XNOR implementation**
>
> ![[AML-image201.jpg|406]]Now consider a more complex logic operation: **XNOR** (exclusive NOR), which is true when inputs are the same (00 or 11), and false otherwise.
>
> This operation **cannot be implemented with a single-layer NN**. Why?
>
> Because:

- The XNOR function is **not linearly separable**

- A single-layer perceptron can only implement **linear decision boundaries** To implement **XNOR**, we build a **multi-layer neural network**:

> **First hidden layer:**

- Neuron 1 implements **AND**: detects when X1=1 = X2=2

- Neuron 2 implements **NOT AND** of -X1, -X2 **Second layer:**

- A neuron combines the outputs of the previous two neurons using an **OR** operation

> ![](media/media/image204.jpeg)

![[AML-image206.jpg|495]]

> **Key Takeaways**

- Logical operations like **AND**, **OR**, and **NOT** can be approximated using a **single-layer neural network** with sigmoid units.

- More complex functions like **XNOR** require **multiple layers** — single-layer NNs are limited to **linearly separable functions**.

- This motivates the use of **multi-layer perceptrons (MLPs)** in deep learning for **nonlinear classification tasks**.

![](media/media/image208.jpeg)

---
> [[AML 31 - NNs-representation|← NNs-representation]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 33 - Decision Trees (DT)|Decision Trees (DT) →]]
