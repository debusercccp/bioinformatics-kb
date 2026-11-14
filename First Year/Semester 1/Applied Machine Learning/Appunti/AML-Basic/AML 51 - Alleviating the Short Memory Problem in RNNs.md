---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 51
tags: [note, aml]
---

> [[AML 50 - Handling Long Sequences – Part 2 + Alleviating the Unstable Gradient Problem for RNNs|← Handling Long Sequences – Part 2 + Alleviating the Unstable Gradient Problem for RNNs]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 52 - Using 1D convolutional layers to process sequences|Using 1D convolutional layers to process sequences →]]

# ALLEVIATING THE SHORT MEMORY PROBLEM IN RNNs

> Due to the transformations that the data goes through when traversing an RNN, some information is **lost** at each time step. After a while, the RNN’s state contains virtually no trace of the very first inputs.

- e.g. Dory in “Finding nemo”: trying to translate a long sentence. By the time she’s finished reading it, she has no clue how it started!

> To tackle this problem, **various types of cells with long-term memory** have been introduced. They have proven so successful that in many cases the basic cells are not used so much anymore. Let’s first (and briefly!) look at the most popular of these long-term memory cells: the **LSTM** cell.
>
> **Long Short-Term Memory (LSTM)**

![](media/media/image363.jpeg)

> The network can learn **what to store in the long-term state**, what to **throw away**, and what to read from it. As the long-term state c(t–1) traverses the network from left to right, you can see that:

- it first goes through a ***forget gate***, dropping some memories

> •then it adds some new memories via the addition operation (which adds the memories that were selected by an ***input gate***)

- at the end, the result c(t) is sent straight out, without any further transformation In a nutshell, at each time step, some memories are dropped and some memories are added. Moreover, after the addition operation, the long-term state is copied and passed through the *tanh* function, and then the result is filtered by the ***output gate***. This produces the short-term state h(t) (which is equal to the cell’s output for this time step y(t)).

> **FC layers in LSTM**
>
> The current input vector x(t) and the previous short-term state h(t–1) are fed to **4 different FC layers**.
>
> ![[AML-image365.jpg|338]]
>
> The **main layer** is the one that outputs g(t).
>
> It has the usual role of **analyzing** the **current** **inputs** x(t) and the **previous** (short-term) state h(t–1).

- In a basic cell, there is nothing else than this **layer**, and its output would go straight out to y(t) and h(t).

- In contrast, in an **LSTM** cell this layer’s output does not go straight out, but instead its most important parts are stored in the long-term state (and the rest is dropped).

> The three other layers are **gate controllers:**
>
> ![[AML-image366.jpg|285]]Since they use the logistic activation function, their outputs range from **0 to 1**. Their outputs are fed to element-wise multiplication operations, so if they output 0s, they close the gate, and if they output 1s, they open it.
>
> Specifically:

- The ***forget gate*** (controlled by *f(t)* ) controls which parts of the long-term state should be erased

- The ***input gate*** (controlled by *i(t)* ) controls which parts of g(t) should be added to the long-term state

- The ***output gate*** (controlled by *o(t)* ) controls which parts of the long-term state should be read and output at this time step, both to h(t) and y(t). **LSTM computations**

![[AML-image367.jpg|616]]

> **Peephole connections**
>
> In a regular LSTM cell, the gate controllers can look only at the input **x(t)** and the previous short-term state **h(t–1). It can be given a bit more context by letting them peek at the longterm state as well** A variant of a LSTM emerged, with extra connections called **peephole connections**:

- the previous long-term state **c(t–1)** is added as an input to the controllers of the forget gate and the input gate, and the current long-term state **c(t)** is added as input to the controller of the output gate.

- This often improves performance, but not always, and there is no clear pattern on which tasks are better off with or without them: you will have to try it on your task and see if it helps.

> GRU cell
>
> The **Gated Recurrent Unit** (**GRU**) cell was proposed in 2014. The GRU cell is a simplified version of the LSTM cell. These are the main simplifications:

- ![[AML-image368.jpg|278]]Both state vectors are **merged** into a single vector **h(t)**

- A single gate controller **z(t)** controls both the **forget** **gate** and the **input** **gate** ❖ if the gate controller outputs a 1, the forget gate is open (= 1), the input gate is closed (1 – 1 = 0)

  - if it outputs a 0, the opposite happens

  - in other words, whenever a memory

> must be **stored**, the location where it will be stored is erased first

- There is no output gate; the **full** **state** **vector** is output at every time step. However, there is a new gate controller **r(t)** that controls which part of the previous state will be shown to the main layer (**g(t)**) It seems to perform just as well

![[AML-image369.jpg|382]]

---
> [[AML 50 - Handling Long Sequences – Part 2 + Alleviating the Unstable Gradient Problem for RNNs|← Handling Long Sequences – Part 2 + Alleviating the Unstable Gradient Problem for RNNs]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 52 - Using 1D convolutional layers to process sequences|Using 1D convolutional layers to process sequences →]]
