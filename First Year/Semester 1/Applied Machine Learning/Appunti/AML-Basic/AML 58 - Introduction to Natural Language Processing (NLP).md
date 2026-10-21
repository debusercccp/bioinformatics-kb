---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 58
tags: [note, aml]
---

> [[AML 57 - Bonus Matherial + Time Series exercises|← Bonus Matherial + Time Series exercises]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 59 - The Bag of Words Model|The Bag of Words Model →]]

# Introduction to Natural Language Processing (NLP)

> **Text preprocessing pipeline**
>
> Raw text is messy — it contains punctuation, case inconsistencies, whitespace issues, and more. Machine learning models **cannot work directly with unprocessed text**. So, we need to:

- Convert text into **tokens** (usually words)

- Remove unwanted elements (punctuation, symbols, etc.)

- Optionally normalize or format the text in ways that suit our task

> **Load the Text**

If the text is small: *with open('your_file.txt', 'r') as f raw_text = f.read()* If the file is large:

- Use memory mapping or chunked reading (mmap, NLTK, or gensim help with this). **2. Split Text into Words (Tokenization) Basic Whitespace Tokenization:**

*tokens = raw_text.split()*

- Fast and simple

- **Keeps punctuation** attached (e.g., "thought." remains) **Regex-Based Tokenization:**

> ![[AML-image393.jpg|595]]
>
> Removes most punctuation

- Splits armour-like into \["armour", "like"\]

- Contractions like what’s become \["what", "s"\] — not ideal in all cases **Remove Punctuation After Split:**

> If you’re okay losing punctuation entirely:

![[AML-image394.jpg|622]]

> **3. Normalize Case**
>
> Convert all text to lowercase to reduce vocabulary size:

*t* ![[AML-image395.jpg|550]]

**Tradeoff**: Lose distinction between Apple the company and apple the fruit. **Using Libraries (Recommended): NLTK for Robust Preprocessing** *import nltk from nltk.tokenize import word_tokenize, sent_tokenize nltk.download('punkt') \# Only needed once* **Tokenize Words:**

*tokens = word_tokenize(raw_text)*

- Handles punctuation and contractions more gracefully

- "what's" → \['what', "'s"\]

- Quotes and symbols are kept as tokens **Tokenize Sentences:**

*sentences = sent_tokenize(raw_text)*

- Useful for models like Word2Vec or sentence embedding models

> **Stemming of words**
>
> In NLP, the process of “**stemming**” refers to the reduction of each word to its root/base • e.g.
>
> fishing, fished, fisher, ..all reduce to the stem fish.

- if your task it **text prediction**, *do NOT* implement stemming!

- if your task is **text classification**, instead, *do* implement it!

> There is a nice suite of **stemming** algorithms to choose from in NLTK, if reducing words to their root is something you need for your project
>
> Once you've **tokenized** your text, the next step is to **numerically encode** it for machine learning. This process is called **vectorization**, and it typically maps words or documents to a **vector space model**.
>
> **1. Bag of Words (BoW)**
>
> **Concept**: Ignores **word order** and **context**, focuses on **word occurrence** only, each document becomes a **sparse vector** of word counts.
>
> **2.TF-IDF (Term Frequency–Inverse Document Frequency) Concept**: Improves BoW by **scaling down common words** (like “the”, “is”, “and”)**.** Highlights **informative** words that are:
>
> Frequent in the current document (TF)**,** Rare in the corpus overall (IDF).
>
> **Pros**: Captures more relevant features, Often improves accuracy in ML models
>
> **Cons**: Still ignores word order, requires storing the vocabulary (can be large)
>
> **3.Hashing Vectorizer Concept**: Avoids building a vocabulary**,** Uses **hashing** to map words to vector indices**.** Vector size is fixed in advance
>
> **Pros**: Very memory-efficient, Useful for large-scale or streaming data, No need to fit() — it's stateless
>
> **Cons**: **No inverse mapping**: can’t recover original words. **Hash collisions**: different words may map to same index To summarize:

- BoW and TF-IDF are **classic, reliable techniques**, still very useful in many contexts

- For **deep learning**, you’ll want to move to **embeddings** (e.g. Word2Vec, GloVe, BERT), but these vectorizers are perfect for many ML pipelines

- Vectorization is a **feature engineering step** — experiment with what gives the best performance

> **Keras**
>
> When working with **text data**, one of the first challenges is converting **human-readable words** into something **machine learning models** can understand — numbers. Keras provides several tools to help you transform raw text into numerical representations, making it easier to train neural networks.
>
> To begin with, if you just want to split a sentence into individual words while cleaning it up a bit, Keras has a convenient function called ***text_to_word_sequence().*** This function takes care of a few common tasks for you: it converts all text to lowercase, removes punctuation, and splits the sentence into a list of words using spaces.
>
> For example, a sentence like
>
> “Keras is Awesome!” would be turned into \['keras', 'is', 'awesome'\].
>
> This is useful when you just want to break down the text simply, without worrying about building vocabularies or encoding.
>
> If you want to go a step further and assign numbers to each word, Keras offers the ***one_hot()*** function. Despite its name, this function doesn’t perform traditional one-hot encoding. Instead, it uses a hashing trick to map each word to an integer within a fixed-size range.
>
> So, for instance, if you say your vocabulary size is 100, each word will be assigned a number from 1 to 100 based on its hash. This method is fast and doesn’t require building or storing a full dictionary of words, but the downside is that different words might get mapped to the same number (called collisions), and you can’t convert the numbers back into words.
>
> For more control over this hashing-based encoding, there’s also the ***hashing_trick()*** function. This does the same thing as one_hot(), but lets you choose how the words are hashed, such as using the default Python hash() function or a more consistent one like md5.
>
> However, if you're working on a serious project, or if you need to reuse the same vocabulary across different datasets like training and testing sets, Keras offers a much more powerful tool: **the Tokenizer class**.
>
> This class is designed to help you build a consistent and reusable vocabulary across your whole dataset. You create a Tokenizer, fit it on your text data, and it learns which words exist, how often they occur, and in which documents they appear. After fitting, it gives you access to several useful pieces of information, such as a dictionary mapping words to their assigned numbers (***word_index***) and how many times each word appeared (***word_counts).***
>
> Once the Tokenizer is trained, you can use it to convert text into sequences of numbers using the ***texts_to_sequences()*** method. This is especially useful when you're preparing text for models that work with word embeddings, like LSTMs or CNNs. Each sentence is turned into a list of integers, one for each word.
>
> Additionally, if your model expects input in the form of a fixed-size vector (such as in logistic regression or a **fully-connected neural network**), you can use the **texts_to_matrix()** method. This will convert each document into a vector using one of several encoding schemes, like binary presence/absence of words, raw word counts, term frequencies, or even TF-IDF scores. This is a simple way to get a numeric representation of your text that can be used directly in dense neural networks.
>
> In summary, Keras provides a clean and flexible way to preprocess text, starting from simple tokenization and cleaning with text_to_word_sequence, moving through hashing-based quick encodings with one_hot() and hashing_trick(), and offering robust and scalable tokenization and vectorization with the Tokenizer class. For serious NLP tasks, the Tokenizer is the preferred approach, as it gives you full control over how your text is processed and encoded.

---
> [[AML 57 - Bonus Matherial + Time Series exercises|← Bonus Matherial + Time Series exercises]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 59 - The Bag of Words Model|The Bag of Words Model →]]
