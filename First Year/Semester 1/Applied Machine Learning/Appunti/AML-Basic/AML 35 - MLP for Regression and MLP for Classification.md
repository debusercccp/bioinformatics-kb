---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 35
tags: [note, aml]
---

> [[AML 34 - Keras Interface for a Shallow NN|← Keras Interface for a Shallow NN]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 36 - Training An ANN|Training An ANN →]]

# MLP for Regression and MLP for Classification

> Good. So, what can you do with MLPs? And how you do it?

![[AML-image240.jpg|642]]

> Remember the classical architecture of a **Neural network**: input layer, hidden layer and output layer, that could be smaller or larger, depending on what you are working on. The structure for regression or classification is similar, we will change that for classification, the activation function would be put together by the **SoftMax** layer.
>
> What changes is mainly:

- Number of output neurons

- Activation function at the output

- Loss function

> **MLP for Regression**
>
> 1 vs many output neurons, depending on **univariate** vs **multivariate** regression.
>
> **Multivariate regression** means a greater number of neurons for the final layer, while for a **univariate regression** you will give you one output neuron.
>
> In general, no activation function for the output neurons, so free to output any range of values.

1.  if you want prediction to be **positive**, you can use the ReLU in the output layer, or (alternatively) a smooth variant of ReLU i.e. the soft plus (softplus(z) = log(1 + exp(z), i.e. close to 0 when z is negative, close to z when z is positive).

2.  if you want prediction to fall within a **given range of values**, use the logistic function or the hyperbolic tangent, and scale the labels to the appropriate range (0 to 1 for the logistic function, or –1 to 1 for the hyperbolic tangent).

> the loss function to use during training is typically the **MSE** (= (1/𝑛) ∗ 𝛴(𝑝𝑟𝑒𝑑𝑖𝑐𝑡𝑒𝑑 − 𝑡𝑟𝑢𝑒)^2**)**, but for example, for many outliers, you can use the 𝑀𝐴𝐸 = (= (1/𝑛) ∗ 𝛴\|𝑝𝑟𝑒𝑑𝑖𝑐𝑡𝑒𝑑 − 𝑡𝑟𝑢𝑒\|). Or you can use the Huber loss.
>
> **Huber loss**

![[AML-image241.jpg|406]]

> is a combination of both (quadratic when the error is smaller than a threshold δ - typically 1, but linear when the error is larger than δ. This makes it less sensitive to outliers than MSE, and it is often more precise and converges faster than MAE.
>
> Architecture for Regression MLP

![[AML-image242.jpg|597]]

> **Classification MLP**
>
> MLPs can be used for classification tasks: **oal**: Predict one **exclusive binary** label per instance. 1 vs many output neurons depending on single-label vs multi-label binary classification, all using the logistic activation function. It is necessary to dedicate one output neuron for each positive class: the output(s) will be a number between 0 and 1, which you can interpret as the **estimated probability P** of the positive class, with the estimated probability of the negative class being 1-P.

- **1 neuron**

- **Sigmoid** **activation**: gives a probability P(y=1![[AML-image243.png]]x)

- **Loss function: Binary Crossentropy** Classification tasks:

- **single-label** binary classification: e.g. spam/not-spam

- **multi-label** binary classification: e.g. spam/not-spam together with urgent/not-urgent (note that classes might be non-exclusive: in this case, probabilities will not add up to 1)

> 1 output neuron per class in case of multiclass classification, using the **SoftMax** activation function for the whole output layer:

- you need to have one output neuron per class, and you should use the **SoftMax** activation function to ensure that all the estimated probabilities are between 0 and 1 and that they add up to 1 (required if the classes are exclusive).

- e.g. classes 0 through 9 for **MNIST** classification: each instance can belong only to a single class, there are several, and they are exclusive.

![[AML-image244.jpg|471]]

---
> [[AML 34 - Keras Interface for a Shallow NN|← Keras Interface for a Shallow NN]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 36 - Training An ANN|Training An ANN →]]
