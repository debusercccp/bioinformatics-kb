---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 10
tags: [note, aml]
---

> [[AML 09 - Polynomial Regression|← Polynomial Regression]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 11 - Logistic Regression|Logistic Regression →]]

# Classification

***Classification*** is a fundamental task in machine learning where the goal is to **<u>categorize or label data into</u> <u>different classes </u>**or categories based on their features. It falls under the broader umbrella of **supervised learning**, where the algorithm learns from labeled training data.

While logistic regression contains the term "regression," it is actually a classification algorithm, not a regression algorithm like linear regression.

In logistic regression, the algorithm generates hypotheses to estimate the probability of an input belonging to a certain class.

While logistic regression is conceptually similar to linear regression, it is specifically designed for classification problems where the **variable we aim to predict** typically represents a **binary outcome**, denoted as y, which can take on two values: **0 or 1**.

These values correspond to two distinct classes: a ***positive class*** and a ***negative class.***

- **Binary Classification**: In binary classification, we have two classes: positive (1) and negative (0). However, it's important to note that the assignment of these labels is somewhat arbitrary. While conventionally, 1 may represent the positive class and 0 the negative class, this assignment can vary depending on the context of the problem. For instance, in some cases, 0 might represent the positive class and 1 the negative class.

- **Multiclass Classification**: In contrast to binary classification, multiclass classification involves predicting outcomes across more than two classes. Here, the class labels extend beyond just 0 and 1, encompassing a broader range of values.

## 6.1 APPLYING LINEAR REGRESSION TO A CLASSIFICATION PROBLEM

When faced with a classification problem, it might seem natural to consider using linear regression at first glance. However, applying linear regression to classification problems is not typically effective or appropriate. Consider a scenario where we want to predict whether a tumor is malignant (positive class, 1) or benign (negative class, 0) based on its size, intuitively one might think that larger tumors are more likely to be malignant than benign.

If we plot tumor size against malignancy status and attempt to fit a straight line using linear regression, we would encounter several issues. In the case of a person with an exceptionally large tumor size, when fitting a linear regression line to the data, th**is outlier point significantly influences the slope and position of the line.** As a result, the line may be skewed towards this outlier, impacting the classification boundary and potentially leading to misclassification.

![[AML-image64.jpg|700]]

- **Assumption of Continuous Output**

Linear regression assumes a continuous output range, which does not align with the discrete nature of classification problems. In classification tasks, the target variable typically represents discrete class labels (e.g., positive or negative), making linear regression ill-suited for this purpose.

- **Ambiguity in Prediction**

When attempting to use linear regression for classification, one must establish a threshold value to separate the predicted outcomes into distinct classes. For example, in a binary classification problem, a common approach is to classify data points with predicted values above the threshold as belonging to one class (e.g., positive or 1) and those below the threshold as belonging to another class (e.g., negative or 0).

However, determining an appropriate threshold value can be challenging, especially in cases where the output values are distributed continuously across the range. This ambiguity in prediction arises because linear regression does not explicitly define the decision boundaries between classes.

Consequently, data points falling near the threshold may be classified differently depending on the chosen threshold, leading to uncertainty in predictions for these middle-range values.Linear regression lacks a clear mechanism for class prediction in the middle range of output values.

- **Sensitivity to Outliers**

Linear regression is highly sensitive to outliers, which are data points that deviate significantly from the majority of the data. Outliers can exert a disproportionate influence on the fitted regression line, causing it to deviate from the true relationship between the variables. In classification tasks, outliers may lead to misclassification and inaccuracies in the model's predictions.

> ![[AML-image65.jpg|521]]

---
> [[AML 09 - Polynomial Regression|← Polynomial Regression]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 11 - Logistic Regression|Logistic Regression →]]
