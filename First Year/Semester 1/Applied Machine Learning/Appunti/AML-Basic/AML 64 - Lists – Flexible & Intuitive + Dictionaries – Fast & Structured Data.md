---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 64
tags: [note, aml]
---

> [[AML 63 - Python basics – functions … Python Data Structures – Built-in Options|← Python basics – functions … Python Data Structures – Built-in Options]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 65 - Sets – Unique & Unordered + NumPy – Fast & Efficient Arrays|Sets – Unique & Unordered + NumPy – Fast & Efficient Arrays →]]

# Lists – Flexible & Intuitive

A dynamic, ordered collection that can store elements of **different types** and **sizes**.

**Key Operations**

> **Indexing & Slicing** → my_list\[0\], my_list\[1:3\]
>
> ![[AML-image408.jpg|281]]**Adding Elements** → append(), extend(), insert()
>
> **Removing Elements** → remove(), pop()

**List comprehension** → compact and faster than loops

**Real-World Use Case**: ML Data Preprocessing

Lists can be useful to storing & manipulating raw dataset rows before conversion to NumPy/Pandas **Pros**

- **Ordered → keeps insertion order**

- **Flexible → accepts different types & lengths**

- **Mutable → can modify contents in place**

- **Easy to use → simple syntax & intuitive**

**Cons** ⅹ **Slow for large data → costly iteration & edits** ⅹ **No built-in math operations → requires loops** ⅹ **Memory overhead → Stores references, not raw data**

## Dictionaries – Fast & Structured Data

A collection of key-value pairs optimized for **fast lookups** and **structured storage**.

**Key Operations**

> **Access values** → my_dict\["key"\], or my_dict.get(“key”, None)
>
> **Add/update** → my_dict\["new_key"\] = value
>
> **Remove** → del my_dict\["key"\], .pop("key")
>
> **Check existence** → "key" in my_dict
>
> **Dict comprehension** for one-liner definitions

![[AML-image409.jpg|317]]**Real-World Use Case**: ML Model Parameters

Removing duplicate values from a dataset before processing **Pros**

- **Fast lookups →** direct access via keys

- **Structured data →** key-value pairs

- **Flexible values →** any data type (lists, dicts, etc.)

- **Mutable →** modify, add, or remove key-value pairs

**Cons** ⅹ **Unordered (pre-3.7) →** order of keys was unpredictable ⅹ **More memory overhead →** keys & values separately ⅹ **Key constraints →** unique & immutable keys (str, num, tuples)

---
> [[AML 63 - Python basics – functions … Python Data Structures – Built-in Options|← Python basics – functions … Python Data Structures – Built-in Options]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 65 - Sets – Unique & Unordered + NumPy – Fast & Efficient Arrays|Sets – Unique & Unordered + NumPy – Fast & Efficient Arrays →]]
