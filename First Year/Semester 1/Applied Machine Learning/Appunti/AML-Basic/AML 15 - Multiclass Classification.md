---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 15
tags: [note, aml]
---

> [[AML 14 - Simplified Cost Function and Gradient Descent + GD Linear Regression vs GD Logistic Regression|← Simplified Cost Function and Gradient Descent + GD Linear Regression vs GD Logistic Regression]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 16 - Alternatives to GD|Alternatives to GD →]]

# Multiclass Classification

A multi-class classification problem is a type of machine learning problem where the task is to classify instances into one of three or more classes or categories. In other words, instead of simply distinguishing between two classes (binary classification), the model must differentiate between multiple classes.

Examples:

- email foldering/tagging (home, work, family, hobby)

- medical diagnosis (not ill, cold, flu, pneumonia)

- weather (sunny, rainy, snowy, windy)

## 8.1 ONE VS ALL

The one-vs-all classification approach is a strategy used to extend binary classification algorithms to handle multi-class classification problems.

1.  **Problem Decomposition**

Given a multi-class classification problem with k classes, decompose it into k separate binary classification sub-problems, each one focuses on distinguishing between one class and all the other classes combined.

2.  **Binary Classification**

For each binary sub-problem, construct a "fake" training set where instances belonging to the target class are labeled as positive (1), and instances belonging to all other classes are labeled as negative (0).

3.  **Model Training**

Train a standard binary classifier (logistic regression) for each binary sub-problem. For example:

- For the first sub-problem, train a classifier to distinguish between class 1 and the rest (not class 1).

- For the second sub-problem, train another classifier to distinguish between class 2 and the rest (not class 2).

- Repeat this process for each class in the dataset.

**4. Decision Making**

When making predictions for a new instance, apply each of the k classifiers to obtain probability scores. The class with the highest probability score is then predicted as the final class for the instance.

The one-vs-all method for multi-class classification problems involves the following steps:

- For each class in the multi-class problem, train a logistic regression classifier *h*(*x*) to predict the probability that *y* = 1 ( the probability of belonging to that class).

- To make a prediction for a new instance *x*, apply each of the trained classifiers to obtain probability scores.

- Select the class that maximizes the probability score ( the class with the highest predicted probability) as the final predicted class for the instance.

![[AML-image87.jpg|339]]By training separate logistic classifiers for each class and selecting the class with the highest probability score during prediction, the one-vs-all method enables the logistic regression classifier to effectively handle multi-class classification problems.

---
> [[AML 14 - Simplified Cost Function and Gradient Descent + GD Linear Regression vs GD Logistic Regression|← Simplified Cost Function and Gradient Descent + GD Linear Regression vs GD Logistic Regression]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 16 - Alternatives to GD|Alternatives to GD →]]
