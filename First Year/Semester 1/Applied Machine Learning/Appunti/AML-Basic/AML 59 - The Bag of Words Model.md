---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 59
tags: [note, aml]
---

> [[AML 58 - Introduction to Natural Language Processing (NLP)|← Introduction to Natural Language Processing (NLP)]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 60 - Generative Learning with VAEs and GANs + Variational Autoencoders (VAEs)|Generative Learning with VAEs and GANs + Variational Autoencoders (VAEs) →]]

# The Bag of Words Model

> **The Bag-of-Words model**
>
> It is a way of representing text data when modelling text with ML algos.

- simple to understand and implement

- great success in problems such as **language modeling** and **document classification**

> BoW model for feature extraction in NLP

- what it is, why it is needed to represent text

- how to develop a BoW model for a collection of docs

- how to use different techniques to prepare a vocabulary and score words Text is messy → modelling text is VERY hard. If you want to to use ML:

- **you cannot work directly with raw text**: you need (vectors of) **numbers**.

- ML algos prefer well defined fixed-length inputs and outputs.

> Plenty of work is needed to build meaningful vectors from textual data, i.e. vectors that reflect various linguistic properties of the original text:

- this is **feature extraction** (or feature encoding) for NLP Need for methods that perform feature extraction with text data

- most popular: the so-called **Bag of Words model of text**

> The **Bag of Words (BoW)** model is one of the simplest and most effective ways to **convert text into numbers** so that machine learning algorithms can understand and use it. It **does not consider grammar, word order, or meaning**, but instead focuses only on **how often each word appears** in a document. Think of it like a **word frequency histogram**: each document is turned into a vector, and each element in that vector tells us how many times a certain word appears.
>
> **How Does BoW Work:** To build a BoW representation, we follow these steps:

1.  **Create a vocabulary**: a list of all the unique words (tokens) that appear in the entire dataset (corpus).

2.  **Map each word to an index** in a fixed-length vector.

3.  **Transform each document into a vector**, where:

    - Each position corresponds to a word from the vocabulary

    - The value can be:

    - **0 or 1** (presence/absence)

    - **A count** of how many times the word appears

    - **Relative frequency**

> **A Simple Example**
>
> Let’s say you have two documents:

- Doc 1: "The building blocks of **music** are notes and players"

- Doc 2: "The building blocks of **soccer** are fans and players"

> Both documents share many words but clearly **talk about different topics**. BoW doesn't capture that — it only sees that they share words like "the", "building", "blocks", "players".
>
> **Limitation**: BoW is **blind to meaning** — it only cares about **word frequency**, not **context**.
>
> **Pros of BoW**

- **Easy to implement**

- **Flexible**: you can use binary presence, counts, or frequencies

- A **great starting point** for many text classification tasks **Weaknesses of BoW**

- **Ignores word order** — so it loses context

- **Can result in huge vectors**, especially with large vocabularies

- **Sparse representations**: most values in the vector are zero

- **Cannot detect synonyms** or semantic similarities **How to Improve It?**

> Before building the vocabulary, we can clean and normalize the text:

- Convert everything to **lowercase**

- Remove **punctuation**

- Remove **stop words** (e.g. “the”, “and”, “of”)

- Apply **stemming or lemmatization** (e.g. “playing” → “play”)

> **Using N-grams to Add Context:** A basic BoW uses **single words (unigrams)**, but you can capture more context by using **n-grams**, which are sequences of n words:

- **Unigram**: "play"

- **Bigram**: "play music"

- **Trigram**: "play music together"

> This helps BoW models understand simple phrases or fixed expressions that have special meaning.
>
> **Scoring Words: Different Modes**
>
> Once you build the vocabulary, you need to decide **how to represent each word** in the vector. Options include:

- **Binary**: 1 if word is present, 0 otherwise

- **Count**: number of times the word appears in the document

- **Frequency**: relative to total words in the doc

- **TF-IDF** (Term Frequency - Inverse Document Frequency):

> o Highlights **important, rare words** in each document o **TF** measures how often a word appears in a doc o **IDF** measures how rare that word is across all docs o Common words get **downweighted**, rare words get **boosted**
>
> **The Sparsity Problem**
>
> In large corpora, the vocabulary can get huge → which means very **long vectors**. But each document contains only a few of those words → so most of the vector will be filled with **zeros**. This is called a **sparse representation**, and it:

- Requires **more memory**

- Slows down training

- Makes learning harder for many models

> **Solution: Hashing (Hash Trick)**
>
> Instead of keeping a large vocabulary, you can **use a hash function** to map each word to a fixed-size index in a vector.

- No need to store the actual vocabulary

- Words are converted to integer positions

- You can still use counts or binary values at those positions

> Be careful: different words **might get mapped to the same position** (collisions), especially if your hash space is too small.
>
> **Final Thoughts**
>
> BoW is a **simple and powerful tool** for text representation, especially when you're just getting started. It’s flexible, works well for many basic tasks, and is easy to combine with machine learning models.
>
> However, **it discards context**, and **vectors become sparse and large**, so for more advanced applications or deeper understanding, you may want to explore:

- **TF-IDF**

- **Word embeddings** (Word2Vec, GloVe)

- **Deep learning models** like LSTM, BERT, etc.

> Still, **Bag of Words is a great starting point** in NLP — and many systems are built on top of it.

---
> [[AML 58 - Introduction to Natural Language Processing (NLP)|← Introduction to Natural Language Processing (NLP)]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 60 - Generative Learning with VAEs and GANs + Variational Autoencoders (VAEs)|Generative Learning with VAEs and GANs + Variational Autoencoders (VAEs) →]]
