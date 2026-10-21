---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 11
tags: [note, aml]
---

> [[AML 10 - Classification|← Classification]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 12 - Logistic Regression · Decision Boundary|Logistic Regression · Decision Boundary →]]

# Logistic Regression

Logistic regression is a classification algorithm that we apply to settings where the label y has discrete values, when it is either 0 or 1.

In logistic regression, we aim to create a **hypothesis function** that **outputs** **values between 0 and 1,** representing the ∫.

A threshold is then applied to these probabilities to make a binary classification decision: values below the threshold are classified as one class (usually 0), while values above the threshold are classified as the other class (usually 1).

While logistic regression is often used for binary classification problems, it can also be extended to handle multi-class classification tasks. The core idea remains the same: **<u>predicting the probability</u>** **<u>of each class</u>** and assigning the input to the class with the highest probability.

For example, in a weather forecasting scenario, logistic regression could predict the probability of rain (regression task) and then classify the decision to bring an umbrella based on a threshold probability

(classification task).

Initially, y**ou use regression to predict the probability of raining,** that is estimate the likelihood of rain based on various factors (temperature, humidity, wind speed, etc). The output of this model is a continuous value representing the probability of rain, which technically aligns with the concept of regression.

Once you have the probability estimate from your regression model, you convert this into a binary classification task. This is where the threshold of 0.8 comes into play. If the predicted probability of rain is greater than 0.8, you classify the instance as "rainy" (1); otherwise, you classify it as "not rainy" (0). This step involves converting the regression output into a classification decision.

## 7.1 HYPOTHESIS

The hypothesis plays a pivotal role in any machine learning algorithm as it defines the mapping between input features and output predictions. In logistic regression, understanding the hypothesis is crucial for determining the model parameters.

In logistic regression, **initially, the hypothesis resembles that of linear regression, expressed as** *θ*<sup>⊤</sup> ⋅ *x*, where θ is the parameter vector and x is the feature vector. This means that the prediction in logistic regression starts with a linear combination of the input features, similar to linear regression.

*h<sub>θ</sub>*(*x*) = *θ*<sub>0</sub>*x*<sub>0</sub> + *θ*<sub>1</sub>*x*<sub>1</sub> + … + *θ<sub>n</sub>x<sub>n </sub>*= *θ<sup>T</sup> x*

However, unlike linear regression, where the output is a continuous value, **logistic regression requires the output to be bounded between 0 and 1** to represent probabilities. Therefore, a **<u>transformation is needed</u>** to ensure that the predictions remain within this range.

The chosen function *g* is the **sigmoid function** that **maps** **any real number z to the range \[0, 1\].**

$$
g(z) = \frac{1}{1 + e^{- z}}
$$

> ![[AML-image66.jpg|500]]

- Starting Point: The curve starts at 0 when z tends towards negative infinity.

- Midpoint: At z = 0, the value of the sigmoid function is 0.5, which represents the midpoint of the curve.

- Rising Trend: As z increases from negative infinity towards 0, the sigmoid function rises from 0 towards 0.5.

- Approaching 1: As z tends towards positive infinity, the sigmoid function approaches 1, indicating a high probability or certainty.

When **we apply the sigmoid function to the <u>hypothesis of linear regression</u>**, **we transform it into the <u>argument of the sigmoid</u>,** resulting in *g*(*θ<sup>T </sup>*⋅ *x*).

This transformation marks the essence of logistic regression.

Interpreting the new hypothesis*g*(*θ<sup>T </sup>*⋅ *x*) is crucial, especially in classification tasks.

For instance, in a binary classification scenario where the output is either 0 or 1, the output of *g*(*θ<sup>T </sup>*⋅ *x*) can be interpreted as the predicted probability that the given input belongs to the positive class.

#### *Example* 

Imagine our hypothesis in logistic regression as estimating the probability that a new input example x belongs to the positive class y=1. In practical terms, consider a patient undergoing an examination, where the features x represent various medical indicators.

If our hypothesis h outputs 0.7, it suggests a 70% likelihood that the patient has malignant cancer (corresponding to y = 1). Here, x serves as a basic feature vector encapsulating relevant patient data.

![[AML-image67.jpg|348]]

Formally, we interpret our **<u>hypothesis as the probability of an input belonging to the positive class</u>**, given its features x and parameterized by *θ*. Essentially, our hypothesis embodies the likelihood that y=1 given the specific input features x, with the parameter vector *θ* influencing this estimation.

Now, let's delve into understanding the parameter *θ*.

![[AML-image68.jpg|287]]In this scenario, we're dealing with a binary condition, meaning that the sum of conditional probabilities to have 0 and to have 1 must be 1. Thus, the probability to belong to the other class is 1 - the previous probability.

At this juncture, we're not only shaping the way we think but also influencing the way we interpret our data. Therefore, h represents the probability of belonging to either the positive or negative class. When we apply the sigmoid function to our original hypothesis g, denoted as *g*(*h*), the output predicts:

- *y* = 1 if the value of *h<sub>θ</sub>*(*x*) ≥ 0.5 —\> if the probability estimated by the hypothesis is more than 50%, we classify the outcome as positive (y = 1).

- *y* = 0 if the value of *h<sub>θ</sub>*(*x*) ≤ 0.5 —\> —\> if the probability estimated by the hypothesis is less than 50%, we classify the outcome as negative (y = 0).

The **sigmoid** function essentially acts as a **thresholding mechanism to make binary predictions** based on the output of the hypothesis.

Think of *z* which represents the input to the sigmoid function. It can be on either side of the graph, depending on whether the hypothesis leans towards positive or negative outcomes.

However, when we apply *g*(*z*), our new hypothesis, it follows the green line of the sigmoid curve.

By setting the threshold at 0.5, any values above it tend to predict *y* = 1 while those below it predict 0. This distinction helps us categorize outcomes more effectively. In essence, while the original hypothesis h may vary, the transformed hypothesis *g*(*h*)ensures a clearer delineation between the two classes.

> ![](media/media/image62.jpg)

## Collegamenti
- [[MBD 05 - Module 1 – Vectors and Hyperplanes · Hyperplanes and linear classification]] — iperpiani come classificatori lineari

---
> [[AML 10 - Classification|← Classification]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 12 - Logistic Regression · Decision Boundary|Logistic Regression · Decision Boundary →]]
