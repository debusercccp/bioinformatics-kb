---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 46
tags: [note, aml]
---

> [[AML 45 - Autoencoders|← Autoencoders]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 47 - Memory Cells|Memory Cells →]]

# AE architectural choice

> Sometimes is needed, the one with increased number of layers. Ant the very end you need to think about choices, an overcomplete autoencoder doesn’t learn any meaningful representation of the data. If your contract the training data **perfectly** you haven’t learned nothing, **memorizing** **overfitting**, there is no reason to have something larger, you are wasting resources for your neural network. **Undercomplete AE**: code layer with lower dimensionality than the input data: it won’t be able to directly copy tis inputs to the outputs, will be forced to learn intelligent features.
>
> The key is hence to force the AE to learn useful features:

![[AML-image324.jpg|426]]

> **Denoising AEs**
>
> AE can learn useful features by adding **random noise** to the input and making it recover the original noise-free data. In this case, a straight copy input to output will not work, and the AE is forced to **identify the noise and subtract it**, thus exposing the underlying meaningful data. The thing to do is for the main action point is not to train with itself but the noisy sample with the labels that are the clean samples. In this way you can also try for **different** noise factor, that can be used for any possible image. **Expectedly** the output will be very clean, but there is not the same exact shape.

![[AML-image325.jpg|361]]

> Higher noisy factor will results in a not so well reconstructed image. But that would be expected.
>
> **Sparse AE**
>
> Basically, a way to avoid overfitting, regularising through a **sparsity constraint**. This simple trick forces the AE to represent each input using a combination of a smaller \# of nodes (not all of them), but still demands it to discover interesting structure in the data **AE use cases:**

- As compression method don’t perform better than its alternatives, their dataspecific makes them practical as general technique, the most common use cases:

- Data denoising, dimensionality reduction when you have high dimensional data. The idea is clever.

- Variational Autoencoders (VAE) are more modern and complete use case of AEs.

> You can of course **get more complicated architecture** using convolutional layers. If you are dealing with images, you might need an AE but the AE we have seen so far will not work well, it is necessary an autoencoder that **doesn’t have only multiple perception**, but you will need a convolutional layer. If the encoder is a regular CNN composed of convolutional layers and pooling layers, it typically reduces the spatial dimensionality of the inputs.
>
> This technique to put together convnet and autoencoders.

![[AML-image326.jpg|642]]

## RECURRENT NEURAL NETWORK (RNNs)

> **Recurrent Neural Networks** are a class of neural networks designed to handle **sequential data**. Unlike standard feedforward networks (which expect fixed-size input and no memory of past inputs), RNNs:

- Process **sequences of arbitrary length**

- Use their **internal memory** to store information about previous steps in the sequence

> They're ideal for tasks where **context and order matter**, such as:

- **Time series forecasting** (e.g., stock prices, weather)

- **Natural Language Processing** (e.g., machine translation, speech-to-text)

- **Autonomous driving** (e.g., predicting trajectories)

> RNN can work on **sequences of arbitrary lengths**. The major difference to expect is that all the network from NNP and autoencoders, **input are of a fixed sized**. This Is interesting, can be a time series or a sequences of any kind, like letters or words. RNN are extremely useful also for natural language processing (NLP) systems, such as automatic translation or speech to text.
>
> **Recurrent Neurons and layers**
>
> ![[AML-image327.jpg|280]]Up to now we have focused on **feedforward NNs**, where the activations flow only in one direction, from the input layer to the output layer. A RNN looks very much like a feedforward NN, expect it also has **connections pointing backward**. The simplest possible RNN is composed of one neuron receiving inputs, producing an output, and sending that output back to itself.
>
> At each time step t (also called a frame), this recurrent neuron receives:

- the inputs x(t)

- its own output from the previous time step, y(t–1)

> **X as a function of time**: it processes something, the outcome goes out but can came back to it. You can think of it at any time instant t and at the same time
>
> you have the y of the t-1 coming as input, and of course it goes back.

![[AML-image328.jpg|642]]

> The interesting thing is that you can represent the network like this: you can have like a **time** **axes**. You have something coming at the beginning. A single recurrent neuron on the left, the other one is a single neuron unrolled! It is not an architecture of four neurons.
>
> **Input** and **output** are just **scalar numbers**. You can create a layer of this neurons. Of course, the connections go back not to just one but consider the number of neurons unrolled through time.

![[AML-image329.jpg|642]]

> The layer in this case, at every time steps, gets as input some vectors: the **input vector** **Xt** at the **time t** and the output vector at the previous time frame: the layer, at each time step t, receives both the **input vector** (not scalar) x(t) and the **output vector** (not scalar) from the **previous time step** y(t–1). If you want to remember a sequence you need to pass it as an input. So, you need to remember like a letter before another. The logic Is complicated in terms of **notations**: you **need to deal with weights**.
>
> Every neuron in this case has **two sets of weights**: one set of weights for x as function of t(wx)and then another input that is the output of the previous time step, that are called the **Ws**. If you consider not only a single recurrent layer, but the weight vector can also be put to the weight matrix, Wx and Wy. Of course, if you need to write down how the W would be you must consider activation function of both.
>
> ![[AML-image330.jpg|457]]Output of a recurrent layer for a single instance
>
> Just as with feedforward neural networks, we can compute a recurrent layer’s output in one shot for a whole mini-batch by placing all the inputs at time step t in an input matrix X(t):
>
> ![[AML-image331.jpg|502]]Outputs of a layer of recurrent neurons for all instances in a mini batch.
>
> Y(t) is a function of all the inputs since time t = 0 (that is, X(0), X(1), ...X(t)).
>
> In this equation:

- **m**: is the number of instances in the mini batch

- **n neurons**: is the number of neurons

- **n inputs:** is the number of input features)

- **Y(t)** is a m×nneurons matrix containing the layer’s outputs at

- time step t for each instance in the mini-batch

- **X(t)** is an m×ninputs matrix containing the inputs for all

- instances

- **Wx** is an ninputs × nneurons matrix containing the connection weights for the inputs of the current time step

- **Wy** is an nneurons × nneurons matrix containing the connection weights for the outputs of the previous time step

- **b** is a vector of size nneurons containing each neuron’s bias term

- The weight matrices **Wx** and **Wy** are often concatenated vertically into a single weight matrix W of shape (ninputs+nneurons)×nneurons

- The notation **\[X(t) Y(t–1)\]** represents the horizontal

- concatenation of the matrices **X(t)** and **Y(t–1)**

> Is the same logic as before, but **we need to implement it in a more specific way**. The output of layer of recurrent neurons. Of course, the notation is a **bit heavier**. The interesting thing is that the Y as function of t is the function of the X at that time but also output of the previous time step.

---
> [[AML 45 - Autoencoders|← Autoencoders]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 47 - Memory Cells|Memory Cells →]]
