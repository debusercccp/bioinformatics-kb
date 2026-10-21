---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 3
tags: [note, aml]
---

> [[AML 02 - Types of Machine Learning|← Types of Machine Learning]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 04 - Univariate Model Regression · Minimization and Cost Function|Univariate Model Regression · Minimization and Cost Function →]]

# Univariate Model Regression

It is **supervised learning** because we're given the "right answer" for each example (house details, and price it was sold at).

It is ***regression*** because we are **predicting a real-valued output**, namely the price

You can easily draw a reasonable line, no? (fit a line is not a term of AML)

![](media/media/image610.jpg)

In machine learning, we start with a simple idea: a straight line. This is like drawing the most basic curve on a graph. If that's not enough to explain the data, we make it a bit more complicated.

**As we aim to capture more complexity, we progressively complicate the model representation.** When it comes to supervised learning, particularly regression tasks where the goal is to predict a continuous output, **we typically start with the most basic representation**.

It's not always perfect, but it's the simplest way to start understanding how things are related.

We can summarize the plot of the housing dataset into a table with two columns: one for the input variable (x) and another for the output variable (y), where y represents the label or target variable.

This table essentially represents the training set, which is the data used to train your machine learning model. Each row in this table corresponds to a single example or sample from the dataset, so the number of rows in this table equals the number of examples or samples in your training dataset.

- m = number of training **examples** in the training set

- x = input variables or **features** (features are essentially the attributes or qualities that we find interesting and want to use in our machine learning models. So, when we talk about an attribute being utilized in machine learning, we promote it to the status of a “feature")

- y = output variable or **target**

- (x, y) = a single training example (a row in the table above)

- (x<sup>(i)</sup>, y<sup>(i)</sup>) =the i<sup>th</sup> training example (the i<sup>th</sup> row)

> ![[AML-image9.jpg|278]]

**3.1 HYPOTHESIS**

How do I represent this hypothesis h?

$$
h_{\theta}(x) = \theta_{0} + \theta_{1}
$$

**θ** are called “***parametersˮ*** of the model so, we are making the hypothesis that **y is a linear function of x.** This ML model is called **<u>univariate linear regression</u>**.

> ***Univariate linear regression*** is a type of machine learning model used to **predict a continuous output variable (y) based on a single input variable (x)**, **assuming that the relationship between the variables can be described by a straight line.**

- **Univariate**: the model is based on only one variable. We are predicting outcomes (prices) as function os just one input variable “x”.

- **Linear Regression**: This refers to the method used to model the relationship between the input variable (x) and the output variable (y). In linear regression, we assume that the relationship between x and y can be represented by a straight line. The goal is to find the best-fitting line that describes the relationship between the variables.

- **Hypothesis**: In univariate linear regression, our hypothesis is that the relationship between x and y can be expressed by the <u>equation of a straight line</u>**: y = mx + b.** Here, 'm' represents the slope of the line, and 'b' represents the y-intercept.

- **Predictions**: The purpose of univariate linear regression is to make predictions of the output variable (y) based on the input variable (x). Given new values of x, the model calculates the corresponding predicted values of y along the line defined by the equation y = mx + b.

In univariate linear regression, the hypothesis hθ(x) is a function used to predict the output variable (y) based on the input variable (x).

- *h*0(*x*) = This is the **predicted value** of the output variable (y) for a given input value (x) using our hypothesis function hθ(x).

- *θ*0 and *θ*1 = These are the parameters of our hypothesis function.

- *θ*0 is the y-intercept of the line (where the line crosses the y-axis),

- *θ*1 is the slope of the line (the rate at which y changes with respect to x).

- *x* = This represents the input variable or feature. In univariate linear regression, we have only one input variable, so x is a single value.

- *θ*0 + *θ*1*x* = This is the equation of a straight line, where *θ*0 is the y-intercept and *θ*1*x* represents the change in y for a unit change in x (the slope of the line).

So, when we use the hypothesis *h*0(*x*) = *θ*0 + *θ*1*x* in univariate linear regression, we're essentially saying that we can predict the value of y for a given input value of x by multiplying the input value by the slope *θ*1 and adding the y-intercept *θ*0.

## Collegamenti
- [[MBD 19 - Module 7 – Correlation and Regression]] — regressione lineare, lato matematico
- [[MBD 04 - Module 1 – Vectors and Hyperplanes · Norm, distance, inner product – what is actually different]] — norma e distanza

---
> [[AML 02 - Types of Machine Learning|← Types of Machine Learning]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 04 - Univariate Model Regression · Minimization and Cost Function|Univariate Model Regression · Minimization and Cost Function →]]
