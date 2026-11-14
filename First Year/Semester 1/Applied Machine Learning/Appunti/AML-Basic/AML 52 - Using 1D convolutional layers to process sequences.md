---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 52
tags: [note, aml]
---

> [[AML 51 - Alleviating the Short Memory Problem in RNNs|← Alleviating the Short Memory Problem in RNNs]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 53 - Deep Dive – Object Recongition and Counting|Deep Dive – Object Recongition and Counting →]]

# Using 1D convolutional layers to process sequences

> **A 1D convolution layer** slides kernels (also called filters) over the time dimension of the sequence. Each kernel detects **local sequential patterns** (like a word pattern in a sentence or a motif in a DNA sequence). The output is a set of **feature maps,** each corresponding to one kernel. For example, 10 filters = 10 feature maps = a 10-dimensional sequence.
>
> You can **combine** Conv1D layers and RNNs for the best of both worlds:

- Conv1D layers **detect short-term features** and **compress the sequence** (temporal down sampling).

- RNNs (like GRU or LSTM) then **focus on long-term dependencies** in the compressed version.

- This procedure reduces the **length** of the sequence → RNN sees fewer steps → less memory + faster and allows the model to **focus on relevant features** rather than raw input.

> You can also replace RNNs entirely with stacked Conv1D layers
>
> ![[AML-image370.jpg|529]]
>
> Multiple convolutional layers can detect **increasingly long patterns:**

- **1st layer:** local patterns o **2nd layer:** patterns of patterns o **etc.**

> Convolutions are:

- Faster (parallelizable)

- More stable during training (no recurrence)

- Often as accurate (especially on tasks like audio processing, text classification)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr>
<th><blockquote>
<p><strong>Approach</strong></p>
</blockquote></th>
<th><strong>Use When</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote>
<p><strong>Conv1D + RNN</strong></p>
</blockquote></td>
<td>You want to speed up training and handle both short and long-term patterns</td>
</tr>
<tr>
<td><blockquote>
<p><strong>Conv1D only</strong></p>
</blockquote></td>
<td>You want fast, scalable sequence modeling (e.g. text classification, audio)</td>
</tr>
<tr>
<td><blockquote>
<p><strong>RNN only</strong></p>
</blockquote></td>
<td>You expect long-term dependencies and variable-length inputs are common</td>
</tr>
<tr>
<td><blockquote>
<p><strong>Transformers</strong></p>
</blockquote></td>
<td>You want the best of both worlds at scale (but expensive!)</td>
</tr>
</tbody>
</table>

> **Wavenet**
>
> In a 2016 paper by Aaron van den Oord and other DeepMind researchers, the authors introduced an architecture called **WaveNet.**
>
> They stacked 1D Conv layers, doubling the “dilation rate” at every layer (that’s how spread apart each neuron’s inputs are):

- the lowest layer gets a glimpse of just 2 time steps at a time.

- while the next one sees 4 time steps (its receptive field is 4 time steps long).

- .. the next one sees 8-time steps, and so on.

> In this way, the lower layers will learn short-term patterns, while the higher layers will learn long-term patterns. Thanks to the doubling dilation rate, **Wavenet can process extremely large sequences very efficiently.**

![[AML-image371.jpg|413]]

> That was the idea. In the paper, this is what the authors did:

- they stacked 10 Conv layers with dilation rates of 1, 2, 4, 8, …, 256, 512…

- then they stacked another group of 10 identical layers (also with dilation rates 1, 2, 4, 8, …, 256, 512).

- then again, another identical group of 10 layers.

> **Justification**: a single stack of 10 Conv layers with these dilation rates will act like a superefficient Conv layer with a kernel of size 1,024 (except way faster, more powerful, and using significantly fewer parameters), so they kept it and stacked 3 such blocks.
>
> In the WaveNet paper, the authors achieved state-of-the-art performance on various audio tasks (hence the name of the architecture), including text-to-speech tasks, producing incredibly realistic voices across several languages.

---
> [[AML 51 - Alleviating the Short Memory Problem in RNNs|← Alleviating the Short Memory Problem in RNNs]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 53 - Deep Dive – Object Recongition and Counting|Deep Dive – Object Recongition and Counting →]]
