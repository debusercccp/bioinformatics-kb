---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 45
tags: [note, aml]
---

> [[AML 44 - Dimensionality Reduction Algorithms – LLE + Visualising Feature Maps, Filters and Class Outputs|← Dimensionality Reduction Algorithms – LLE + Visualising Feature Maps, Filters and Class Outputs]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 46 - AE architectural choice + Recurrent Neural Network (RNNs)|AE architectural choice + Recurrent Neural Network (RNNs) →]]

# Autoencoders

> Autoencoders are a type of neural network used to **learn efficient representations**, typical for the purposes of **dimensionality reduction**, **denoising** or **anomaly detection**. It can be described as a feed-forward NN with the output that is the same as the input. Abstract reasoning is needed. NN architecture needs to **find patterns**. For the machine a shorter sequence would be easier to remember, but the idea is that with a pattern even a longer sequence would become easier to remember. Patterns help in general.
>
> **Intuition of autoencoders**
>
> Autoencoders are a sort of architecture, and containing an autoencoder during training pushes it to discover and exploit patterns in the state.
>
> **The AE**: compresses the input into a **lower dimensional representation**, called **latent-space representation** or **code**, that can be thought of a compact summary a compression of the input. Then reconstruct the output from such representation. You are encoding because you are taking the input and compressing it into a code, and then you encode it back into the beginning.
>
> An AE consists of three components: **encoder**, **code**, **decoder**.

![[AML-image318.jpg|642]]

> The encoder and decoder do not talk to each other, the encoder compresses the input and reproduces the code, the decoder uses the code and reconstructs the input, yielding the output. To build an AE we need an **encoding method**, a decoding method, a loss function to compare the output with the target.
>
> AE is not gzip, so it is not only a dimensionality reduction algorithm we have specific peculiar properties. Ato think of it as a compression we must consider:

- **data-specific**: w.r.t. standard data compression algorithms, AEs learn features specific for the given training data, so they are only able to meaningfully compress data like what they have been trained on. of course, the zipping procedure or compression procedures is a compression that learns. It’s like a degraded representation of the input. So, we don’t get exactly the first thing.

- **lossy**: the AE’s output will be a close but somehow degraded representation of the input

- **{un-,self-}supervised**: we can throw data to an AE and train it w/o any prior action. No need for labels → un-supervised, but imprecise: self-supervised, because they generate their own labels from the training dataset

![[AML-image319.jpg|328]]

> **Input and output are in blue**. Both encoder and decoders are **FC** and **FF ANN**.
>
> Code is a single layer of an ANN with the dimensionality of our choice. The important thing is that the dimensionality of input and output is the same. This is a requirement, what is not a requirement is that the encoding and decoding architecture are **symmetric**, so this is a choice. This symmetry is not so peculiar, is not a necessity, you can have more layers. The code itself has a dimensionality you decide.
>
> **AE hyperparameters:**
>
> Pretty easy in terms of managing hyperparameters.

![[AML-image320.jpg|496]]

> For a **sandwich-like structure**, the typical thing is that since you have a smaller thing inside, you usually decrease for each subsequent layer of encoder and increase for the decoder. Once you have coded the stuff with something like this you have a normal neural network, using backpropagation and **Gradient Descent**.
>
> **AE implementation on MNIST**
>
> A four form mnist can run it through a network that cans squeeze into something with lower dimensionality and reconstruct it to the input.

![[AML-image321.jpg|642]]

> **Creating autoencoder:** taking input and output, with binary cross entropy and an optimizer and that’s it. The differences we have seen so far with keras are: For of all syntax is not the same we saw normally. This is not a sequentially interface.
>
> **Remember Functional Vs Sequential API**
>
> The **Sequential API** is the simplest way to build a model in Keras. You just stack layers one after another — each layer has exactly **one input tensor** and **one output tensor.**
>
> **When to use it?**

- When your model has **a single input and output**

- When the model is **a linear stack of layers**

> The **Functional API** is more flexible. You define layers as functions applied to tensors — so you can build models that are **non-linear**, **multi-input**, **multi-output**, **shared layers**, etc.
>
> **When to use it?**

- When you need **multiple inputs/outputs**

- When building **non-sequential architectures** (like ResNets, Siamese networks)

- When you need **shared layers** or **skip connections**

> For Autoencoders: This is not a sequential API in Keras but a **Functional API**, this I just a way to create thing as we saw before. If you don’t need it **sequential API** is the easiest but sometimes need another one. Functional API how you to deal with modes with nonlinear topology, models with shared layers, models with multiple inputs or outputs. How do you do it in sequential API?
>
> You specify the input this is sort of design as a **DAG** (**Direct Acyclic Graph**) that describes a sequence of layer as a graph of layers.

![[AML-image322.jpg|642]]

> **Functional API is non sequential**; you can use different input. Might be more verbose, but it is more flexible. For complex model, you don’t use it.
>
> Every time you have a layer, these layers are callable at the very end of the first layer.
>
> Model fil: there are no labels, this is self-supervised. The target of the autoencoders would be the same of the inputs.

![[AML-image323.jpg|642]]

> You can see the output here. At most we have 209968 parameters. This is drawn horizontally usually. You can do the summary not vertically but horizontally. There are ways to make your autoencoders deeper, to get a higher quality for your code.

## Collegamenti
- [[MBD 20 - Module 8 – Principal Component Analysis]] — PCA come riduzione lineare di dimensionalità

---
> [[AML 44 - Dimensionality Reduction Algorithms – LLE + Visualising Feature Maps, Filters and Class Outputs|← Dimensionality Reduction Algorithms – LLE + Visualising Feature Maps, Filters and Class Outputs]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 46 - AE architectural choice + Recurrent Neural Network (RNNs)|AE architectural choice + Recurrent Neural Network (RNNs) →]]
