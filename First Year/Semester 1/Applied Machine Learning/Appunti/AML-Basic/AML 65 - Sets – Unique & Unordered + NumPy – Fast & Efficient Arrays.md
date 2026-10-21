---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 65
tags: [note, aml]
---

> [[AML 64 - Lists – Flexible & Intuitive + Dictionaries – Fast & Structured Data|← Lists – Flexible & Intuitive + Dictionaries – Fast & Structured Data]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 66 - Jupiter Notebooks & Google Colab + Pandas|Jupiter Notebooks & Google Colab + Pandas →]]

# Sets – Unique & Unordered

An unordered collection of unique elements, optimized for **fast membership checks** and **set operations.**

**Key Operations**

> **Add/remove elements** → add(), remove(), discard() **Operations of sets**:
>
> Union (A \| B) → combines elements from both sets
>
> Intersection (A & B) → keeps only common elements
>
> Difference (A - B) → removes elements in B from A

**Real-World Use Case**: Data Cleaning in ML

Removing duplicate values from a dataset before processing **Pros**

- **No duplicates → unique elements by design**

- **Fast membership checks**

- **Mutable → add/remove elements dynamically**

**Cons**

> ⅹ **Unordered** → no indexing or positional access ⅹ **No duplicate storage** → Data loss if duplicates matter ⅹ **Immutable** → only hashable types (no lists/dicts)

## NumPy – Fast & Efficient Arrays

A powerful numerical computing library that provides **fast, memory-efficient arrays** and **matrix operations**. **Key Operations**

> **Creating arrays** → np.array(\[1, 2, 3\])
>
> ![[AML-image410.jpg|297]]**Indexing & slicing** → Similar to lists but more powerful
>
> **Matrix computations** → np.dot(A, B), A @ B
>
> **Element-wise operations** → arr \* 2, arr + arr

**Real-World Use Case**: ML Data Processing

> Handling large-scale numerical data efficiently

**Pros**

- **Optimized (numerical) →** storage & operations

- **Faster than lists →** contiguous memory

- **Vectorized operations →** replace slow Python loops

- **Broad support →** pandas, scikit-learn, TF, torch

**Cons** ⅹ **Fixed-type elements →** all elements of same type ⅹ **Less flexible than lists →** all components of same size/length ⅹ **Steeper learning curve**

---
> [[AML 64 - Lists – Flexible & Intuitive + Dictionaries – Fast & Structured Data|← Lists – Flexible & Intuitive + Dictionaries – Fast & Structured Data]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 66 - Jupiter Notebooks & Google Colab + Pandas|Jupiter Notebooks & Google Colab + Pandas →]]
