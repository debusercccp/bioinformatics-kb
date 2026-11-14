---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 36
tags: [note, aml]
---

> [[AML 35 - MLP for Regression and MLP for Classification|← MLP for Regression and MLP for Classification]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 37 - NNs’ Building Blocks|NNs’ Building Blocks →]]

# Training An ANN

> How do you compute the weights. I.e. how do you train ANN?
>
> **NNs** are an old class of algorithms that have been originally inspired by one goal: build a machine that can **mimic the brain**. It is necessary to get a sense of how this basic logic drove their conceptual development, though, what we can expect them to ultimately do.

- **Forward pass**: Make a prediction

- **Loss**: Measure how wrong the prediction was

- **Backward pass (Backpropagation)**: Figure out how to adjust weights to make predictions better

- **Gradient Descent**: Actually, apply those adjustments

- Repeat this loop over and over (epochs)

> Think about the senses. The brain can learn to process images (=see), process acoustic waves (= hear), process other signals (e.g. sense of touch). Quite complex! and different tasks!
>
> **One single learning algorithm**
>
> The “one single learning algorithm” hypothesis is currently just a hypothesis. But it is not with 0 evidence.

![[AML-image245.jpg|608]]

> So, if the same piece of physical brain tissue may be able to process sight or sound or touch, then maybe there is just one learning algorithm behind, that can process any of them. So - **if the former is true** - in trying to emulate the brain, instead of implementing a thousand different algorithms, maybe what we need is to figure out some approximation of whatever the brain's one-and-only-one **learning algorithm** is and implement it. This might be our best shot at making real progress towards the AI dream of building someday truly intelligent machines.
>
> Training a neural network is just optimizing a loss function.

- **Loss function:** Measures how far off the predictions are

> → e.g., MSE for regression, cross-entropy for classification

- **Objective:** Minimize the loss using **Gradient Descent**

- **Challenge:** Millions of parameters (weights & biases) — need a fast way to compute gradients

- **Solution: Backpropagation**

> **Backward Propagation**
>
> For many years, researchers struggled to find a way to train **MLPs**. 1986,
>
> Rumelhart/Hinton/Williams introduced the backpropagation (BP) training algorithm \[RefRumelhartHintonWilliams\] - still used today.

- it is simply **GD** using an efficient technique for computing the gradients automatically.

- call “**BP**” because it does two propagations through the **network** (one forward, one backward), and can compute the gradient (\*) of the network’s error with every single model parameter. It can find out how each connection weight and each bias term should be tweaked to reduce the network error.

> Automatically computing gradients is called **automatic differentiation** (**autodiff**). Various techniques exist; BP uses reverse-mode autodiff. It is fast and precise and is well suited when the function to differentiate has **many variables** (e.g. connection weights) and few outputs (e.g. one loss).

- once it has these gradients, it just performs a regular GD step

- the whole process is iteratively repeated - in epochs - until the network converges

> Gradient Descent (GD)
>
> A method for finding the **minimum of a function** by following the **negative gradient**.
>
> 𝜕𝐿𝑜𝑠𝑠
>
> 𝑤: = 𝑤 − 𝜂 ⋅
>
> 𝜕𝑤
>
> where η is the **learning rate**

- **Mini-batch GD**: break data into batches for faster, more stable training

- Often used together with **optimizers** like Adam, RMSprop, etc

> **Activation Functions Matter**
>
> They introduce non-linearity, so the network can learn complex mappings.

- Must be differentiable to work with backprop

- Should avoid flat regions, or gradients vanish

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 44%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Name</strong></th>
<th style="text-align: center;"><strong>Formula</strong></th>
<th><strong>Used In</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Sigmoid</td>
<td style="text-align: center;"><blockquote>
<p>1</p>
<p>𝜎(𝑧) = <sub>−𝑧</sub> 1 + 𝑒</p>
</blockquote></td>
<td>Output layer (binary classification)</td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Tanh</p>
</blockquote></td>
<td style="text-align: center;"><blockquote>
<p>𝑒𝑧 − 𝑒−𝑧</p>
</blockquote>
<p>𝑡𝑎𝑛ℎ(𝑧) = <sub>𝑧</sub> + 𝑒−<sub>𝑧</sub></p>
<blockquote>
<p>𝑒</p>
</blockquote></td>
<td>Hidden layers (less common now)</td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>ReLU</p>
</blockquote></td>
<td style="text-align: center;">max(0,z)</td>
<td>Most hidden layers (default)</td>
</tr>
<tr>
<td style="text-align: center;"><blockquote>
<p>Leaky ReLU</p>
</blockquote></td>
<td style="text-align: center;">max(0.01z, z)</td>
<td>Avoid dying neurons</td>
</tr>
<tr>
<td style="text-align: center;">Softmax</td>
<td style="text-align: center;">Converts logits into a probability distribution</td>
<td>Multiclass classification output</td>
</tr>
</tbody>
</table>

> **how do GD and BP work together**
>
> **GD**: the big hill represents the error or loss function of a problem. The goal is to find the lowest point on the hill (which corresponds to the minimum error). GD is like the hiker following a path towards the lowest point on the hill, by **taking** **small** **steps** in the direction of the steepest slope, and hence he gets down-hill.; eventually the goal would be to reach the **bottom of the hill** (which represents the minimum error). One path, executed just once, might work but might not be the optimal, though.
>
> **BP**: (in **a NN only**) it is a way for the N to figure out which direction the hiker had better go, ultimately (the NN needs to know how each weight and bias in the NN contributes to the error). It's like a trail of breadcrumbs left by the hiker on its way, **moved and “tuned”** again in the reverse direction now, going back up-hill. The hiker starts at the bottom of the hill and leaves breadcrumbs along the way as it climbs up (they represent the gradients, which tell the NN how much each weight and bias needs to change to decrease the error). By following the adjusted breadcrumbs, at the next GD step, the hiker can follow a better path ( the NN can adjust its weights and biases using GD to eventually reach the minimum error in next rounds.
>
> For each training instance, the algo first makes a **prediction**, measures the **error** and **preserve** **info** on all steps (BP in NN, here), then goes through each layer in reverse to measure the error contribution from each connection (backwards/reverse pass, BP), and finally slightly tweaks the connection weights to reduce the error (forward pass, GD). Retain information that tell you how to do the steps with a chain rule of derivatives, remeasuring and gring at every epoch of the training.

![](media/media/image248.jpeg)

> **BP and activation functions** the BP authors made a key change to the MLP architecture: they replaced the step function with the **logistic function**. BP uses GD which can thus make a progress at every step.
>
> Back propagation used **gradient descent**, logistic is ok because you don’t have any flat segments. No activation function should be linear. The first function with the step function they decided to move to the sigmoid: very good idea.

![[AML-image250.jpg|622]]

> I**nitialisation**
>
> It is important to **initialise** all the hidden layers’ connection weights randomly, or else training will fail. e.g. if all weights and biases stay **initialised** to **0**, then all neurons in each layer will be identical, thus **BP** will affect them in the same way, and they will remain identical → no actual training. You need to initialise, so you break the symmetry, and allow BP to train a diverse team of neurons. Symmetry must be break and let **BP** do it. If you are training different team of neurons, will be able to say some values are high, low witch ones must be high and which ones must be low.

---
> [[AML 35 - MLP for Regression and MLP for Classification|← MLP for Regression and MLP for Classification]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 37 - NNs’ Building Blocks|NNs’ Building Blocks →]]
