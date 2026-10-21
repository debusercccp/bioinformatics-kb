---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 25
tags: [note, aml]
---

> [[AML 24 - Error Metrics for Skewed Classes|← Error Metrics for Skewed Classes]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 26 - Machine Learning Development · Resampling|Machine Learning Development · Resampling →]]

# Data Preparation

#### • RESCALING

Rescaling data involves changing the scale of the features in your dataset without changing their distribution. It's commonly used when the features have different units or different ranges. The purpose of rescaling is to ensure that all features contribute equally to the analysis.

The most common rescaling technique is Min-Max scaling, where each feature is scaled to a specified range, typically between 0 and 1 or -1 and 1.

#### • STANDARDIZATION 

Standardizing data involves transforming the features so that they have a **mean of 0** and a s**tandard deviation of 1.** This process is also known as Z-score normalization. Standardization is useful when the features have different scales and distributions. By standardizing the data, you remove the mean and scale the variance to make the features comparable. It's important to note that standardization assumes that the data is normally distributed or approximately normally distributed.

#### • NORMALIZATION 

Normalizing data involves scaling individual samples to have unit norm, typically rescaling each observation to have a length of 1. This process is useful when the magnitude of the features is not important, but their direction matters. Normalization is often used in algorithms that compute distances or similarities between data points, such as K-Nearest Neighbors (KNN) or Support Vector Machines (SVM).

#### • BINARIZATION

Binarizing data involves **transforming numerical features** **into binary values based on a specified threshold.** Any value above the threshold is set to 1, and any value below or equal to the threshold is set to 0. Binarization is useful when you want to emphasize the presence or absence of a particular feature rather than its specific value.

It's commonly used in feature engineering or preprocessing steps before applying certain machine learning algorithms.

## 13.2 FEATURE SELECTION

Choosing a subset of the features in the dataset to use for the analysis can help in:

- Reducing overfitting

- Improving accuracy

- Reducing training time

There are several options to do so:

- **<u>Univariate feature selection</u>**

- **<u>Recursive feature elimination</u>**

- **<u>Features importance</u>**. After a model is trained, it’s possible to check the importance given to each feature.

- **<u>Principal component analysis</u>**

---
> [[AML 24 - Error Metrics for Skewed Classes|← Error Metrics for Skewed Classes]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 26 - Machine Learning Development · Resampling|Machine Learning Development · Resampling →]]
