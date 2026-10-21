---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 47
tags: [note, aml]
---

> [[AML 46 - AE architectural choice + Recurrent Neural Network (RNNs)|← AE architectural choice + Recurrent Neural Network (RNNs)]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 48 - Handling Long Sequences – Part 1|Handling Long Sequences – Part 1 →]]

# Memory Cells

> In an RNN, the output at each time step is **fed back into the network** as input for the next step. This recurrence allows the network to **retain information from previous steps —** a concept we refer to as **memory.** In this sense, a single recurrent neuron or a layer of recurrent neurons, acts as a very basic memory cell, capable of learning only short patterns.
>
> A **recurrent layer or neuron** is often called a **memory cell**, because it: • Maintains a **state** across time (h(t))

• Updates its state using:

> ![[AML-image332.jpg|274]]o Current input **x(t)** o Previous state **h(t−1)**
>
> Short = about 10 steps long, depending on the task.
>
> **Formalising Memory in RNNs**

- ![[AML-image333.jpg|418]]h(t) = hidden state at

> time t

- x(t) = input at time t

- y(t) = output at time t

> ![[AML-image334.jpg|362]]The RNN computes:
>
> A cell’s state at time step t denoted h(t) is a function of some inputs at that time step, and its state at the previous time step.
>
> **Input and Output Sequences**
>
> ![[AML-image335.jpg|268]]**Seq-2-seq**
>
> **RNN** can **simultaneously** *take a sequence of inputs and produce a sequence of outputs* **(“sequence-tosequence” network**).
>
> **Seq-2-Vec**
>
> ![[AML-image336.jpg|205]]Used when you want to extract a **single value** from a sequence.

5.  **g., sentiment analysis:**

> **\[This","movie","was","great"\]→\[Positive\]**
>
> The last hidden state is often used as a fixed-size representation of the entire sequence.
>
> **Vec-2-seq**
>
> ![[AML-image337.jpg|193]]Conversely, you could feed the network the same input vector over and over again at each time step and let it output a sequence **(“vector-to-sequence” network).**
>
> E.g. the input could be an image (or the output of a CNN), and the output could be a caption for that image
>
> **Encoder-Decoder Architecture**
>
> This is an improvement over basic Seq2Seq.

- ![[AML-image338.jpg|315]]**Encoder** reads the input sequence → compresses it into a context vector (a single vector c)

- **Decoder** uses this vector to generate a completely new sequence

> “Je suis heureux"→"I am happy"
>
> Why better than basic Seq2Seq?

- It **separates the understanding phase (encoder)** from the **generation phase (decoder)**

- It's more flexible and more performant on **longer sequences**

> **How do you train a RNN**
>
> ![[AML-image339.jpg|273]]Standard backpropagation doesn’t work directly due to the time-unfolded structure of RNNs. **Backpropagation Through Time (BPTT)**

1.  **Unroll the RNN over time steps**

2.  Perform **forward pass** through this unrolled structure

3.  Compute the loss **over all time steps**

4.  Backpropagate the gradients through each time step (like a very deep network) The **BPTT steps**:

    - Just like in regular BP, there is a first forward pass through the unrolled network (dashed “⇢” arrows).

    - Then the output sequence is evaluated using a cost function **C(Y(0), Y(1), …Y(T))** (where **T** is the max time step). Note that this cost function may ignore some outputs (e.g. in a sequence-to-vector RNN, all outputs are ignored, except for the very last one).

    - The gradients of that C are then propagated backward through the unrolled network

> (solid “⟶” arrows)

- Finally, the model parameters are updated using the gradients computed during BPTT.

---
> [[AML 46 - AE architectural choice + Recurrent Neural Network (RNNs)|← AE architectural choice + Recurrent Neural Network (RNNs)]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 48 - Handling Long Sequences – Part 1|Handling Long Sequences – Part 1 →]]
