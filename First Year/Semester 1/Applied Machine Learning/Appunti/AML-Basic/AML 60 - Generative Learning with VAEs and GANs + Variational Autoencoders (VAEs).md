---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 60
tags: [note, aml]
---

> [[AML 59 - The Bag of Words Model|← The Bag of Words Model]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 61 - GANs – Generative Adversarial Networks|GANs – Generative Adversarial Networks →]]

# Generative Learning with VAEs and GANS

> When building machine learning models, you can take two main approaches: **discriminative** or **generative**.

- **Discriminative models** focus on *directly* learning the relationship between input data x and output labels y. That is, they learn how to *discriminate* between classes. These models estimate the **conditional probability** p(y \| x), which means they predict the label y given the input x. For example, if you feed in someone’s age, weight, and lifestyle, the model could predict whether they’re likely to develop diabetes.

> Discriminative models are great for classification and regression tasks. You’re not trying to understand how the input data is distributed — just how it relates to the labels.

- **Generative models**, on the other hand, try to learn **how the data is generated**. They model the **joint probability** p (x, y) — that is, the probability of seeing a particular input and its corresponding label together. Once trained, generative models can also estimate p (x \| y) — meaning, given a label, they can generate new inputs that fit that label. For instance, you could generate synthetic patient profiles that look like people with diabetes.

> Since they understand the underlying structure of the data, generative models can also be used to **detect outliers**, reconstruct missing data, or even **generate entirely new data samples**.
>
> **Autoencoders (AEs)**
>
> An **autoencoder** is a type of neural network designed to **reconstruct its own input**. It consists of two main parts:

- The **encoder**, which compresses the input into a lower-dimensional **latent representation** (often just called a “code”).

- The **decoder**, which takes that compressed representation and attempts to reconstruct the original input as closely as possible.

> Autoencoders are trained in an **unsupervised way** — they don’t need labeled data, since the goal is just to match the input to the output. They are commonly used for:

- **Dimensionality reduction** (like a neural version of PCA),

- **Denoising** corrupted inputs,

- **Anomaly detection** (reconstruction errors highlight anomalies), • And as **building blocks** in deeper neural networks.

## Variational Autoencoders (VAEs)

> **Generative** **autoencoders**
>
> While basic autoencoders aren't inherently generative (they're mainly focused on compression and reconstruction), **some advanced forms of autoencoders** can be used to **generate new data**. This leads us to one of the most important generative versions of an autoencoder: Variational Autoencoders (VAEs).
>
> **VAEs** are a special type of autoencoder introduced in 2014 that combine ideas from **probability and neural networks**. Here’s the key difference: instead of mapping an input to a single point in latent space, a VAE maps it to a **distribution** — usually a Gaussian (normal distribution). From that distribution, the model **samples** a point to use as the latent representation. Because of this, the output of a VAE is **probabilistic** — there’s randomness involved, even during inference — and this makes it a **true generative model**. Once trained, you can generate **entirely new data points** by sampling random vectors from the latent space and decoding them. For example, if your VAE was trained on images of faces, you can generate **new, realistic faces** that weren’t in the original dataset.
>
> To ensure that the latent space behaves nicely (i.e., smooth transitions, meaningful structure), VAEs include a second part in the training loss: the **KL divergence**. This regularizes the latent space so that it's close to a standard normal distribution. Without this, sampling from the latent space wouldn’t produce anything useful.

- They create a **structured, continuous latent space** where similar points correspond to similar outputs.

- You can **interpolate** between inputs — e.g., gradually morph one face into another.

- You can generate **completely new samples** that still look like real data.

- They’re **much easier to train** than earlier generative models like Restricted Boltzmann Machines.

- While GANs (Generative Adversarial Networks) might produce sharper outputs, VAEs are **more stable and principled**.

![[AML-image396.jpg|283]]

> Just like any regular autoencoder, a **VAE** has two main parts:

- An **encoder**, which transforms the input into a lower-dimensional “code” (or latent representation),

- A **decoder**, which tries to reconstruct the original input from this code.

> But here’s the **twist**:
>
> A **VAE does *not* encode each input into a fixed point in the latent space**. **Distributions Instead of Points**
>
> Instead of encoding the input into a single code vector, the **encoder learns to output two vectors**:

- A **mean vector** (μ), and

- A **standard deviation vector** (σ) — though in practice, it often outputs the **log of the variance** (log(σ²)) for numerical stability.

> These two vectors **define a multivariate Gaussian distribution** in the latent space. Then, for each input, the model **samples** a point from this Gaussian — and that **sampled point becomes the actual “code”** used by the decoder to reconstruct the input. So, every time you pass the same input through the VAE, it might generate a slightly different code (and thus slightly different reconstruction), depending on the random sample drawn.
>
> This randomness is **intentional**. It allows the model to learn a **smooth, continuous latent space** where similar inputs are encoded to **overlapping regions**. This has several benefits:

1.  **Generative power**: After training, you can sample any random point from a standard Gaussian and decode it — generating new, never-before-seen data.

2.  **Interpretable latent space**: Because the model is trained to push encodings to resemble a simple distribution (like a Gaussian), nearby points in the latent space produce similar outputs.

3.  **Continuity**: The latent space becomes continuous and compact, which is great for interpolating between inputs.

> The cost function of a VAE has two parts:

![[AML-image397.jpg|642]]

1.  **Reconstruction loss**

> This measures how well the output matches the input (just like in a standard AE). It ensures that the decoder learns to reconstruct inputs accurately.

2.  **KL Divergence loss**

> This is the "variational" part. It forces the learned latent distribution (from the encoder) to stay close to a **standard normal distribution**. This way, the latent space doesn't become wild or fragmented — it's shaped like a nice, continuous Gaussian cloud.
>
> So the total loss = reconstruction loss + KL divergence
>
> A common tweak to the VAE’s architecture is to make the encoder output γ=log(σ2) rather than σ. The latent loss can then be computed as shown above.
>
> Once training is done:

- You **don’t need an input anymore** to generate new data!

- Just **sample a point from a standard normal distribution** (e.g., a vector of random values from N(0, 1)),

- Feed it into the decoder,

- And you get a **new data point** that looks like it came from the original training set.

> That’s the **magic** of VAEs: they are autoencoders that **learn to generate**.

---
> [[AML 59 - The Bag of Words Model|← The Bag of Words Model]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 61 - GANs – Generative Adversarial Networks|GANs – Generative Adversarial Networks →]]
