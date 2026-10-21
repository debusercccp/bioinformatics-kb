---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 50
tags: [note, aml]
---

> [[AML 49 - Not Saturating Activation Functions|← Not Saturating Activation Functions]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 51 - Alleviating the Short Memory Problem in RNNs|Alleviating the Short Memory Problem in RNNs →]]

# Handling Long Sequences: Part 2

> **Batch normalisation**
>
> BN is typically applied:

- **After the affine transformation**: z=Wx+bz = Wx + bz=Wx+b

- **Before** or **after** the **non-linear activation** (common before ReLU, sometimes after)

> it consists of adding an operation in the model just before or after the activation function of each hidden layer

- this operation simply **zero-centres** and **normalizes** each input, then it scales and shifts the result **using two new parameter vectors** per layer: one for scaling, the other for shifting ( in other words, this operation lets the model learn the optimal scale and mean of each of the layer’s inputs)

- In many cases, if you add a **BN** **layer** as the very first layer of your NN, you do not need to standardise your training set (e.g. using a StandardScaler in sklearn), as the BN layer will do it for you.

> In order to zero-centre and normalize the inputs, the BN algo needs to estimate each input’s mean and standard deviation: It does so by evaluating mean and standard deviation of each input over the current mini-batch (hence the name “Batch” Normalization).

![](media/media/image3020.jpg)

![[AML-image359.jpg|521]]

> To keep in mind

- N works best with **larger batch sizes** (e.g., ≥ 16)

- **During inference**, moving averages of μ\muμ and σ2\sigma^2σ2 from training are used

- **Not ideal for RNNs**: batch-wise computation can be problematic due to variable sequence lengths; use **LayerNorm** instead

- For **convolutional layers**, BN is typically applied across each **channel**, not per-pixel

> You may find that **training is rather slow**, because each epoch takes much more time **when you use Batch Normalisation**. This is usually counterbalanced by the fact that convergence is much faster with BN, so it will take fewer epochs to reach the same performance.

## ALLEVIATING THE UNSTABLE GRADIENT PROBLEM FOR RNNs

> Many of the tricks used in Deep NNs to alleviate the unstable gradients problem can also be used for RNNs:

- good parameter initialisation

- faster optimizers

- dropout

> However, others do not work:

- non-saturating activation functions (e.g. ReLU) may not help as much for RNNs. In fact, the latter may lead the RNN to be even more unstable during training

- Batch Normalization cannot be used as efficiently with RNNs as with deep FF NNs

> **ReLU**
>
> In **RNNs**, **the same weights** are reused at every time step. So, any **small change in the weights** affects **all future time steps**. If your activation function doesn't **saturate**, small changes **accumulate** rapidly → **outputs (and gradients) can explode**.

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p><strong>Property</strong></p>
</blockquote></th>
<th><strong>Problem</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote>
<p>Non-saturating (good for</p>
<p>DNNs)</p>
</blockquote></td>
<td>In RNNs, output keeps increasing across time steps — can explode</td>
</tr>
<tr>
<td><blockquote>
<p>No upper bound</p>
</blockquote></td>
<td>Doesn’t suppress large activations</td>
</tr>
<tr>
<td><blockquote>
<p>Zero gradient for negative inputs</p>
</blockquote></td>
<td>Leads to “dead neurons”</td>
</tr>
<tr>
<td><blockquote>
<p>Doesn’t naturally regulate output</p>
</blockquote></td>
<td>No mechanism to "cap" unstable growth</td>
</tr>
</tbody>
</table>

> **Use Saturating Activation Functions,** common alternatives:

- **tanh** (default in most RNNs)

- **sigmoid** (less common due to vanishing gradient at extremes)

<!-- -->

- These functions **compress outputs** into a bounded range:

  - tanh(x) ![[AML-image360.png]] \[-1, 1\] o Helps keep the outputs stable across time steps.

> **Use a Smaller Learning Rate**

- Reduces the size of weight updates.

- Slows down the risk of **compounding changes** over time steps.

> **Use Gradient Clipping**

- Cap gradients to avoid them exploding.

- Helps stabilize training in RNNs and LSTMs.

> **Use Better RNN Architectures:** Replace vanilla RNNs with:

- **LSTM** (Long Short-Term Memory) o **GRU** (Gated Recurrent Unit)

<!-- -->

- These cells **control memory flow** with gates and are designed to avoid exploding/vanishing gradients.

> **BN**
>
> You cannot use BN between time steps, only between recurrent layers.

- To be more precise, it is technically possible to **add a BN layer** to a **memory cell** so that will be applied at each time step (both on the inputs for that time step and the hidden state from the previous step).

- However, the same BN layer will **be used at each time step**, with the same parameters, regardless of the actual scale and offset of the inputs and hidden state.

- In practice, **this does not yield good results.**

> **Layer Normalisation**
>
> Instead of normalizing across the **batch dimension**, it normalizes across the **features** **dimension**. One advantage is that it can compute the required statistics on the fly, at each time step, independently for each instance.

- This also means that it behaves the same way during **training** and **testing** (as opposed to BN), and it does not need to use exponential moving averages to estimate the feature statistics across all instances in the training set. Like BN, Layer Normalization **learns a scale** and an offset parameter for each input.

---
> [[AML 49 - Not Saturating Activation Functions|← Not Saturating Activation Functions]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 51 - Alleviating the Short Memory Problem in RNNs|Alleviating the Short Memory Problem in RNNs →]]
