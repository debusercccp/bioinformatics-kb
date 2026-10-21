---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 26
tags: [note, aml]
---

> [[AML 25 - Machine Learning Development · Data Preparation + Feature Selection|← Machine Learning Development · Data Preparation + Feature Selection]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 27 - Machine Learning Development · Performance Metrics|Machine Learning Development · Performance Metrics →]]

# Resampling

There are clever techniques from statistics called "**resampling**" methods: they allow to make accurate estimates for how well your algorithm performs.

A resampling method involves **<u>repeatedly drawing samples from a training data set</u> and <u>refitting a model to</u> <u>obtain additional information about that model,</u>** namely, how well the algorithm performs.

Note that no training data is lost: once the performance of our algorithm is evaluated, then the final algorithm can be re-trained on the entire training dataset and get ready for operational use. There are several ways to split the training set in this way:

- **<u>Split into train and test sets</u>**

Take two separate subsets of the data, one for training and one for testing. It is fast and ideal for large datasets but it may cause high variance.

- **<u>K-fold Cross-Validation</u>**

It works by **splitting the dataset into k-parts** (e.g. k=5 or k=10), each split of the data is called a ***fold***.

The algorithm is trained on k-1 folds (with 1 held back) and then tested on the held-back fold.

This is repeated k times so that *each* fold of the dataset is used as the held-back test set once.

The resulting k different performance scores can be summarized using a mean and a standard deviation, giving a more reliable estimate of the performance. iteration= k times and trainign= k-1 times for each iteration.

- **<u>Leave-One-Out Cross-Validation</u>**

It’s an extreme of K- fold CV in which the size of the folds is 1, so k is equal to the number of observations in the dataset. It’s slower and has higher variance than the K-fold CV.

- **<u>Repeated random test-train splits</u>**

A variation of the k-fold CV in which each split is done randomly (like test- train split). It has the speed of the test-train split and the low-variance of the K-fold CV, but introduces redundancy in the evaluation. Discussion at the lecture.

There are some tips to consider what resampling technique to use in different circumstances.

- Generally k-fold cross-validation is the gold standard for evaluating the performance of a ML algorithm on unseen data with k set to 3, 5, or 10 (typically 10).

- Using a train/test split is good for speed when using a slow algorithm and produces performance estimates with lower bias when using large datasets.

- Techniques like leave-one-out cross-validation and repeated random splits can be useful intermediates when trying to balance variance in the estimated performance, model training speed and dataset size.

The best possible advice is to experiment and find a technique for your problem that is fast and produces reasonable estimates of performance that you can use to make decisions. GOLDEN RULE: \*\*if in doubt, just use 10-fold cross-validation\*\*.

---
> [[AML 25 - Machine Learning Development · Data Preparation + Feature Selection|← Machine Learning Development · Data Preparation + Feature Selection]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 27 - Machine Learning Development · Performance Metrics|Machine Learning Development · Performance Metrics →]]
