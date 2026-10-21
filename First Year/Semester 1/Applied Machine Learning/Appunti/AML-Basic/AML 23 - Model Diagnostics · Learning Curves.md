---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 23
tags: [note, aml]
---

> [[AML 22 - Model Diagnostics · Regularisation Bias and Variance|← Model Diagnostics · Regularisation Bias and Variance]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 24 - Error Metrics for Skewed Classes|Error Metrics for Skewed Classes →]]

# Learning Curves

Whether we seek to verify the correctness of our algorithm or enhance its performance, learning curves offer valuable insights. It is a **tool** often used to **diagnose** if a learning **algorithm** may be **suffering** from a **bias problem or a variance problem,** or a little bit of both.

![[AML-image123.jpg|348]]We begin by **analyzing** the **training error**, followed by the validation error, plotting both as a function of the training set size *m*. Initially, with only 6 examples in the dataset, we plot them one by one. Starting with a quadratic hypothesis, we observe that the training error remains low when the dataset size is small, often reaching zero without regularization. As we **add more examples** to the dataset, such as the 4<sup>th</sup> example, we notice a notable **increase in the training error.** This increase indicates the growing challenge for the quadratic hypothesis to effectively fit the expanding dataset, particularly evident when working with few data points.

This trend indicates that the algorithm is struggling

to fit the data adequately as the dataset size *m* increase, therefore **the more datapoints we add, the training error will increase.**

![[AML-image124.jpg|326]]Now, shifting our focus to the **validation set**, it aims to assess our model's ability to generalize beyond the training data. Initially, when dealing with a limited number of examples, the validation error tends to be high. However, **as we augment the dataset with more examples, the validation error typically improves.**

This pattern illustrates a fundamental behavior: as we accumulate more data, o**ur capacity to generalize enhances, as we gain deeper insights from the broader dataset.** Consequently, the validation error curve initiates from elevated error levels and progressively descends as more data is incorporated.

> ![[AML-image125.jpg|435]]

Let's examine the learning curves in the context of high bias and high variance issues.

#### HIGH BIAS (UNDERFITTING) 

At the outset, when dealing with a **limited number of examples**, the **model** may **seem** **adequate** as it fits the available data relatively well. However, as we continue to **add more data points**, the model's performance doesn't substantially improve beyond a certain point. **It reaches a plateau where additional data doesn't lead to significant alignment enhancements**.

Essentially, **the model remains <u>simplistic</u>** and cannot capture the underlying complexity of the data. In this situation, simply **<u>increasing the volume of data without modifying the hypothesis won't address the issue</u>**. Instead, we need to introduce more complexity into the hypothesis to better align with the underlying patterns in the data.

![[AML-image126.jpg|697]]

#### HIGH VARIANCE (OVERFITTING) 

Conversely, in the case of high variance, the model's hypothesis becomes overly intricate compared to the available data, resulting in overfitting. For instance, employing an excessively high-degree polynomial (e.g., degree 100) leads the model to excessively adapt to the training data, even capturing noise and insignificant details. Initially, with a small number of data points, the error is notably low as the model adeptly fits these few points. However, as more data is introduced, the error gradually increases because the model struggles to generalize beyond the training data.

Despite the inclusion of more data, **the training error remains relatively low as the model continues to fit the existing data well, albeit excessively**. Consequently, the **disparity between the training error and the validation error (Jtrain - Jcv) widens**, indicating the model's strong ability to adapt to the training data but poor generalization capability.

Increasing the number of examples can mitigate high variance by providing the model with a more diverse dataset to discern patterns and relationships effectively. Unlike high bias scenarios, where additional examples don't significantly impact error rates, in high variance situations, **<u>more examples can enhance</u> <u>generalization</u>**, **reducing the disparity** between training and validation errors and bolstering the model's predictive accuracy on new data.

![[AML-image127.jpg|697]]

It's important to note that the learning curves we've discussed so far present a clean and idealized representation of the relationship between error and various factors like model complexity or dataset size. However, in real-world scenarios, learning curves are often much noisier and messier due to several factors such as noise in the data, variability in model performance, and other unforeseen complexities.

Despite these caveats, plotting learning curves remains a valuable tool in assessing whether a learning algorithm is encountering issues related to bias or variance. While the curves may not always exhibit smooth or predictable behavior, analyzing their trends can still provide valuable insights into the performance of the algorithm and guide adjustments or improvements to enhance its effectiveness

![[AML-image128.jpg|697]]

![[AML-image129.jpg|697]]

We've delved into the evaluation of learning algorithms, explored model selection techniques, and extensively covered the concepts of bias and variance. But how does this knowledge guide us in improving the performance of a learning algorithm?

Debugging a Learning Algorithm:

Imagine you've implemented regularized linear regression to forecast housing prices. However, when you apply your model to a new dataset of houses, you discover significant errors in its predictions. What steps should you take next? Here are the strategies we discussed:

- **Getting more training example** (Recommended for checking high variance problems)

- Good to **fix high variance** problem (if cross-validation error significantly exceeds training error)

- Ineffective for high bias: don't waste time collecting more examples in this case

- **Try smaller sets of features**

- Good to **fix high variance** problems

- Ineffective for high bias: don’t waste time in carefully selecting features

- **Try getting additional features**

- Good to **fix** **high bias** problems

- Especially beneficial when the hypothesis (h) is too simple; adding features helps h fit the training set better.

- **Try adding polynomial features**

- Good to **fix** **high bias** problems

- Adding polynomial features increases the model's complexity, aiding in better fitting the data.

- **Try increasing lambda**

- Good to **fix high variance** problem —\> increasing lambda helps mitigate overfitting issues.

- **Try decreasing lambda**

- Good to **fix high bias** problems —\> decreasing lambda allows the model to capture more complexity, addressing underfitting.

---
> [[AML 22 - Model Diagnostics · Regularisation Bias and Variance|← Model Diagnostics · Regularisation Bias and Variance]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 24 - Error Metrics for Skewed Classes|Error Metrics for Skewed Classes →]]
