---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 38
tags: [note, aml]
---

> [[AML 37 - NNs’ Building Blocks|← NNs’ Building Blocks]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 39 - Ensemble Learning + ENSEMBLE – Voting (hard voting – soft voting)|Ensemble Learning + ENSEMBLE – Voting (hard voting – soft voting) →]]

# Gradient Based Optimization

> In every neural network (NN), each layer has ***W* (weights)** and ***b* (biases)** that are trainable parameters of that layer, and they are attributes of the layer (namely, the kernel and bias attributes). They contain the information learned by the NN from **exposure** to **training** **data**.
>
> They are tensors. What’s in them?

- initially, they are filled with **small random values** (random initialization).

- Are adjusted during training to minimize the model’s **loss**

- Contain the knowledge the NN has **learned** from the data The training happens in **loops**, let’s zoom into one loop.

1.  Draw a batch of training samples: input ***x*** and corresponding targets ***y***

2.  Run the **NN**, i.e. run a forward pass on ***x*** to obtain predictions ***y_pred***

3.  Compute the loss of the **NN** on this **batch** (i.e. a measure of the mismatch between **y_pred** and **y**)

> 3\. Update all weights of the network in a way that slightly reduces the loss on this batch
>
> Repeat this loop over many **epochs** (passes over the full dataset).
>
> When you eventually end up with a NN that has a very low loss on its training data, and you call it done, you judge that the NN has “learned” to map its inputs to correct targets.

![[AML-image256.jpg|477]]

> I can **naively** think of freezing all weights in the **NN**, except the one scalar coefficient being considered → then, try different values for that coefficient.
>
> • e.g. assume that the initial value (of one single coefficient) is 0.3. I do a first forward pass on a batch of data → loss of the NN on that batch is 0.9. If I change the coefficient to 0.35 (0.25) and rerun the forward pass, the loss increases (decreases) to 1.0 (0.8) → you update it e.g. by 0.05 to contribute to minimising the loss. And you need to repeat this for all coefficients in the NN. This approach is terribly inefficient → 2 (expensive) forward passes needed per each coefficient (and they are many).
>
> A much better approach is to take advantage of the fact that all **ops** used in the NN are **differentiable**, hence compute the gradient of the loss regarding the NN’s coefficients → you can then move the coefficients in the opposite direction from the gradient, thus decreasing the loss
>
> ![[AML-image257.jpg|287]]The strategy is simple:

- we modify the parameters little by little based on the **current loss value** on a random batch of data.

- as we are dealing with a differentiable function, we can compute its gradient.

- the gradient gives us an **efficien**t way to **implement** the difficult step 4 as per our training loop → we just need to update the weights in the opposite direction from the gradient, and the loss will be a little less every time.

> ![[AML-image258.jpg|642]]
>
> **Optimizers: improving SGD**
>
> Multiple variants of SGD exists, and they are known as **optimisers** or **optimisation methods**. e.g. SGD with momentum, as well as Adagrad, RMSProp, and others.

- they differ by taking into account **previous weight updates** when the concept of **momentum** (derived from physics) .

- it addresses two **SGD issues:** convergence speed and local minima.

![[AML-image259.jpg|661]]

> In the training loop discussed so far, we can casually think of a “**NN function**” that is **differentiable** → we can compute its **derivatives**. In practice, a NN function consists of **many tensor operations** chained together, each of which has a simple, known derivative.

- e.g. **f(w1, w2, w3) = a(w1, b(w2, c(w3)))** is a NN function f composed by 3 tensor ops a, b and c acting on weight tensors **w1, w2 and w2.**

- to derive f above, I would apply the chain rule **(f(g(x)) = f'(g(x)) \* g’(x) ).**

> Applying the chain rule to the computation of the gradient values of a NN gives rise to an algo called **backpropagation** (or reverse mode differentiation).

- it starts with the **final loss value** and works **backward** from the top layers to the bottom layers, applying the chain rule to compute the contribution that each parameter had in the loss value.

> **Backpropagation: Efficient Gradient Computation**
>
> Backpropagation (or reverse-mode automatic differentiation) lets us compute all the required gradients efficiently, by applying the chain rule through the network:
>
> ![[AML-image260.jpg|427]]Each layer computes:

- The gradient of its output w.r.t. its input

- Passes it backward (hence the name “backpropagation”)

> This lets us **update all parameters at once** with only **one forward pass + one backward pass**.

![[AML-image261.jpg|642]]

---
> [[AML 37 - NNs’ Building Blocks|← NNs’ Building Blocks]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 39 - Ensemble Learning + ENSEMBLE – Voting (hard voting – soft voting)|Ensemble Learning + ENSEMBLE – Voting (hard voting – soft voting) →]]
