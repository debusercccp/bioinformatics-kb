---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 66
tags: [note, aml]
---

> [[AML 65 - Sets – Unique & Unordered + NumPy – Fast & Efficient Arrays|← Sets – Unique & Unordered + NumPy – Fast & Efficient Arrays]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 67 - Data visualization|Data visualization →]]

# Jupiter Notebooks & Google Colab

Jupyter Notebook is an interactive **web based environment** that allows you to **create and share documents** in **live code**, equations, visualizations and narratives text.

Jupyter contains code and markdown cells.

Code cells supports over 40 languages (python, R, C++, Julia..)

Markdown cells are useful to write texts with rich formatting and supports HTML.

Jupyter is ideal for quick prototyping and sharing ideas but in particular it is **useful for data analysis and interactive visualization.**

A similar resource to Jupiter is **Google Colab**. This is a **free cloud-based Jupyter notebook** produced by google, without setup required because **you can access easily through browser**. It allows also **free access to GPUs and TPUs**, and allows **easy collaboration to share and collab in real time.**

## Pandas

Pandas is a powerful open source library for **data analysis & manipulation.** It is useful for data wrangling (confronto di dati), cleaning, transforming and aggregating in Machine Learning pipelines.

**Two types of Data Structures**

In pandas we have two types of Data Structures:

- ![[AML-image411.jpg|296]]**Series**: 1 dimension labelled array. **<u>Series can store numbers, strings and</u> <u>other data types</u>**. It is **<u>often used for</u> <u>time series, single-column data or</u> <u>intermediate calculations</u>.** Series are **<u>faster than lists and dicts</u>** for numerical operations.

- **Dataframe**: 2 dimensions labelled structure ideal for tabular data (rows and

> columns)

**Pandas vs Numpy**

We have some differences between **Pandas** and **Numpy**, but also similarities:

Similarities:

- built on efficient, **high-performance C code**

- **vectorized operations for speed (significa che sia Pandas che NumPy eseguono operazioni su interi array o serie di dati senza usare loop espliciti in Python)** Differences:

- **NumPy**: **numerical** computations with **homogeneous**, **n-dimensional arrays**

- **Pandas**:

- labeled data (structured arrays)

- richer functionality for handling data (cleaning, indexing, merging, ...) • **supports heterogeneous data**

**Creating & importing data**

In Pandas you can import or create data. You can import from various sources like CSV, Excel, JSON, SQL. In this way you can handle missing values, specific column types and indexing on load.

Here some import commands:

- pd.read_csv("data.csv") → easy, fast and flexible

- pd.read_excel("data.xlsx", sheet_name="Sheet1")

- pd.read_json("data.json"), pd.read_sql(query, conn)

But you can also create dataframes from python structures, numpy arrays and customize index and columns.

![[AML-image412.jpg|282]]

**Data Selection & Index**

In pandas you can select files. You can do it with two main methods:

.loc\[\] → label-based selection (row/col names)

.iloc\[\] → position-based selection (row/col order)

![](media/media/image3520.jpg)

**Data Cleaning & Preparation**

Cleaning data is important. That’s because real world data are messy: we can have missing **values**, **wrong types** and **duplicates** that could lead error to analysis results. Pandas makes cleaning easy, fast and efficient.

![[AML-image416.jpg|450]]

**Aggregation & Summary**

The aggregation during analysis is important because in this way we can summarize & extract insights from large datasets. It is a common procedure in ML feature engineering.

![[AML-image417.jpg|442]]

**Merging & Joining Dataframes**

In this way we can combine datasets from different sources and it is essential for working with relational data (for example user data + transaction history).

![[AML-image418.jpg|442]]

**Lecture 3 – Matplotlib**

---
> [[AML 65 - Sets – Unique & Unordered + NumPy – Fast & Efficient Arrays|← Sets – Unique & Unordered + NumPy – Fast & Efficient Arrays]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 67 - Data visualization|Data visualization →]]
