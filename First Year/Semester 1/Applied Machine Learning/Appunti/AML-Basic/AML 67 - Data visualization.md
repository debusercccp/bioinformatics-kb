---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 67
tags: [note, aml]
---

> [[AML 66 - Jupiter Notebooks & Google Colab + Pandas|← Jupiter Notebooks & Google Colab + Pandas]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 68 - Matplotlib - Customization & Advanced Features|Matplotlib - Customization & Advanced Features →]]

# Data visualization

Data visualization is the graphical display of data to uncover patterns and trends. Graphical display is useful to simplify complex datasets for quick understanding. In Machine Learning there are some benefits like explore feature distributions and relationships and also assess model performance and highlight easily anomalies. **Matplotlib**

Matplotlib is an external python library for data visualization. It allows to creates static, animated and interactive plots. It is fundamental for libraries like seaborn and pandas plotting.

Some advantages to use matplotlib are that:

- Highly customizable: control over every plot detail

- Works seamlessly with NumPy & Pandas

- Supports multiple backends (Jupyter, scripts, interactive) There are two ways to use it:

- **<u>Pyplot interface (plt)</u>** – quick, state-based, light syntax

- **<u>Object-Oriented API</u>** – More control, better for complex plots **Core Matplotlib components**

The core components of this library are:

![[AML-image419.jpg|343]]**Figure** – The entire **canvas** where plots are drawn

- (**plt.figure**() or **plt.subplots**() )

- overall plotting space (like a blank canvas)

**Axes** – Individual plotting areas

(**subplots**) inside a figure

- (**fig.add_subplot**() or **plt.subplots**() )

- **where data is actually plotted**

- a figure can have **multiple subplots**

**Axis (X/Y)** – The **horizontal and vertical scales** of a plot

**Artists** – All visual elements (lines, text, markers, etc.)

- **everything you see**

- lines, text, legends, markers, ticks, etc...

- Example: ax.plot (x, y, labe=‘line plot’)

In general:

- a **Figure** can contain multiple **Axes** (subplots)

- each **Axes** has its own **Axis (X/Y)**

- **Artists** define how data is visually represented

---
> [[AML 66 - Jupiter Notebooks & Google Colab + Pandas|← Jupiter Notebooks & Google Colab + Pandas]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 68 - Matplotlib - Customization & Advanced Features|Matplotlib - Customization & Advanced Features →]]
