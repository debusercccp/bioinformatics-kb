---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 49
tags: [note, aml]
---

> [[AML 48 - Handling Long Sequences – Part 1|← Handling Long Sequences – Part 1]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 50 - Handling Long Sequences – Part 2 + Alleviating the Unstable Gradient Problem for RNNs|Handling Long Sequences – Part 2 + Alleviating the Unstable Gradient Problem for RNNs →]]

# Not Saturating Activation Functions

> Even with proper weight initialization (e.g., Xavier or He), if the **activation function** is a poor match for the architecture or data:

- You still face **vanishing gradients** (e.g., with sigmoid)

- Or neurons that **die permanently** (e.g., with ReLU) ReLu: rectified Linear Unit

- ![[AML-image345.jpg|196]]Fast to compute

- Doesn't saturate for large positive inputs

- Helps reduce vanishing gradient problems (especially in deep nets)

- Encourages sparsity (many activations are 0)

> A neuron **dies** if it always receives **negative input**, and thus **always outputs 0**, because:

- Gradient of ReLU for x\<0 is **0**

- Once output is 0, gradient descent **can't update** the weights anymore

• This often happens when:

- You use a **large learning rate** o Poor weight initialization

- Bad data distribution (e.g., inputs not centered)

> It's common to find **30–50% of neurons dead** in badly tuned deep ReLU networks. Rarely a neuron can "revive" **if it's not in the first hidden layer**. If the layers **below** change enough during training (due to GD), the dead neuron's input may become positive again but often: once dead, they **stay dead.**
>
> **ReLU Variants: Leaky ReLU**

![](media/media/image348.jpeg)

- **Allows a small gradient** even when x\<0, avoiding dying neurons

- Easy drop-in replacement for **ReLU**

- Needs tuning of α

> The hyperparameter α defines how much the function “leaks”
>
> ![[AML-image350.jpg|307]]

- it is the slope of the function for z \< 0 and is typically set to 0.01 This small slope ensures that leaky ReLUs never die

- well, they can go into a long coma, but they have a chance to eventually wake up

> Few conclusions:

- the leaky variants always outperformed the strict ReLU activation function

- setting e.g. α = 0.2 (huge leak) seemed to result in better performance than α =

> 0.01 (small leak)

- **randomized leaky ReLU** (**RReLU**), where α is picked randomly in a given range during training and is fixed to an average value during testing, performed fairly well in comparison, and seemed to act as a regularizer (i.e. reducing the risk of overfitting the training set).

- **parametric leaky ReLU** (**PReLU**), where α is authorized to be learned during training (instead of being a hyperparameter, it becomes a parameter that can be modified by BP like any other parameter), strongly outperform ReLU on large image datasets (but on smaller datasets, it runs the risk of overfitting the training set)

> **ELU (Exponential linear unit)**

![](media/media/image353.jpeg)

- it takes on **negative** **values** when z \< 0

1.  ❖ this allows the unit to have an **average** **output** closer to **0** and helps alleviate the vanishing gradients problem.

2.  ❖ the **hyperparameter α** defines the value that the ELU function **approaches** when z is a **large negative number.** It is usually set to 1, but you can tweak it like any other hyperparameter.

- it has a **nonzero gradient for z \< 0**, which avoids the dead neurons problem

- if **α is equal to 1**, then the function is smooth everywhere, including around z = 0, which helps speed up GD, since it does not bounce as much left and right of z = 0

> Main drawback of the ELU activation function: exponential, so it is slower to compute wrt ReLU and variants (but its faster convergence rate during training compensates for that slow computation). Still at test time an ELU network will be slower than a ReLU network.
>
> **SELU (scaled ELU)**

![[AML-image355.jpg|385]]

> if you build a NN composed exclusively of a **stack of dense layers,** and if all hidden layer’s use **SELUs**, then the network will **self-normalize**: the output of each layer will tend to preserve **mean 0** and **standard deviation 1** during training, which solves the vanishing/exploding gradients problem.
>
> Few conditions for self-normalization to happen exist, though:

- The input features must be standardized (mean 0 and standard deviation 1)

- Every hidden layer’s weights must be initialized with LeCun normal initialization

- The network’s architecture must be sequential. Unfortunately, if you try to use SELU in nonsequential architectures, such as RNN or networks with skip connections, self-normalization will not be guaranteed, so SELU will not necessarily outperform other activation functions.

> The approach only **guarantees self-normalization if all layers are dense**, but some researchers have noted that the SELU activation function can improve performance in CNN as well (see later).

- As a result, SELU often significantly outperforms other activation functions for such NNs (especially DNNs).

![[AML-image356.jpg|642]]

---
> [[AML 48 - Handling Long Sequences – Part 1|← Handling Long Sequences – Part 1]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 50 - Handling Long Sequences – Part 2 + Alleviating the Unstable Gradient Problem for RNNs|Handling Long Sequences – Part 2 + Alleviating the Unstable Gradient Problem for RNNs →]]
