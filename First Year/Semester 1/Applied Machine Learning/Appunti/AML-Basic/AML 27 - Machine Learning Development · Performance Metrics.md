---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 27
tags: [note, aml]
---

> [[AML 26 - Machine Learning Development · Resampling|← Machine Learning Development · Resampling]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 28 - Machine Learning Development · Hyper-parameters Tuning|Machine Learning Development · Hyper-parameters Tuning →]]

# Performance Metrics

The choice of metrics influences how the performance of ML algorithms is measured and compared, how the importance of different characteristics is weighted in the results and your ultimate choice of which algorithm to choose.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><p>CLASSIFICATION METRICS</p>
<p>Classification problems are perhaps the most common type of ML problem and as such many metrics can be used to evaluate predictions for these problems.</p>
<ul>
<li><p><strong><u>Accuracy</u></strong></p></li>
</ul>
<p>It is the ratio of correct predictions over all predictions made (i.e. percentage of test data correctly classified). It’s suitable only when the classes are balanced and the prediction errors are equally important.</p>
<p>Note that accuracy doesn’t tell anything about how confident the model was on a correct or wrong prediction.</p>
<ul>
<li><p><strong><u>Logarithmic Loss (logloss)</u></strong></p></li>
</ul>
<p>It evaluates the model’s confidence in a prediction as a scalar probability. A smaller logloss is better, with 0 representing a perfect logloss. Logloss is a measure of uncertainty, for this reason, it’s also called entropy.</p>
<ul>
<li><p><strong><u>Area Under Curve (AUC)</u></strong></p></li>
</ul>
<p>It’s a performance metric for binary classification problems that represents a model’s ability to discriminate between positive and negative classes. An area of 1.0 represents a model that made all predictions perfectly. An area of 0.5 represents a model that is as good as random.</p>
<ul>
<li><p><strong><u>Confusion matrix</u></strong></p></li>
</ul>
<p>It’s a more informative presentation of the accuracy of a model with two or more classes.</p>
<p>Note that this metric cannot be used as a score, it’s just a summary of the evaluation process.</p></th>
</tr>
</thead>
<tbody>
<tr>
<td><blockquote>
<p>REGRESSION METRICS</p>
</blockquote>
<ul>
<li><p><strong><u>Mean Absolute Error (MAE)</u></strong></p></li>
</ul>
<p>The MAE is the average of the absolute differences between predictions and actual values.</p>
<p>It gives an idea of the magnitude of the error, but not of its direction (e.g. over- or under-predicting).</p>
<ul>
<li><p><strong><u>Mean Square Error (MSE)</u></strong></p></li>
</ul>
<p>The MSE is similar to the MAE in that it provides an idea of the magnitude of the error.</p>
<p>The Root Mean Squared Error (or RMSE) is its square root, it can be useful for description and presentation.</p>
<ul>
<li><p><strong><u>R</u>2</strong></p></li>
</ul>
<p>R-squared <strong>indicates</strong> the <strong>goodness of fit of a set of predictions to the actual values</strong>.</p>
<p>In statistical literature, this measure is called the coefficient of determination.</p>
<p>This is a value between 0 and 1 for no-fit and perfect fit respectively.</p></td>
</tr>
</tbody>
</table>

**ACCURACY VS LOGLOSS**

***Accuracy*** is a fundamental metric used to evaluate classification models. It measures the percentage of correctly classified instances in the test dataset. For example, in a binary classification scenario distinguishing between cat and non-cat images, if 95 out of 100 samples are correctly classified, the accuracy is calculated as 95%.

However, while accuracy offers a straightforward measure of classification correctness, it may not provide a comprehensive understanding of model performance on its own. To gain deeper insights into model behavior, it's essential to complement accuracy with other evaluation techniques. One such technique is utilizing a confusion matrix, which delineates true positives, true negatives, false positives, and false negatives. By examining these components, we can obtain a more nuanced assessment of classification errors and model performance.

***Logloss***, or logarithmic loss, is a metric that evaluates the predictive performance of classification models by considering the probabilities assigned to different classes. Unlike accuracy, which focuses solely on correct classification, logloss assesses the confidence and balance of predictions across different classes.

To illustrate, imagine a binary classification task of identifying cat images. The model predicts the probability of each image being a cat, ranging from 0 to 1. Logloss calculates how closely these predicted probabilities align with the actual outcomes. In simpler terms, logloss tells us whether the model's level of certainty matches reality. It's like asking: "***When the model says it's 60% sure an image is a cat, is it actually a cat 60% of the time?***"

Furthermore, logloss becomes especially valuable in complex scenarios like multiclass classification, where there are more than two classes. In such cases, it helps ensure that the model's predictions are balanced across all classes. This is crucial because models often show biases towards larger classes, which can skew evaluations if solely relying on traditional accuracy metrics.

While accuracy provides a basic measure of correctness, logloss offers a deeper understanding of model behavior by considering prediction probabilities. Both metrics play vital roles in evaluating classification models effectively. Moreover, in scenarios with class imbalances, it's essential to consider metrics like the F1 score, which balance precision and recall, to ensure a comprehensive assessment of model performance. By understanding and utilizing both accuracy and logloss alongside complementary evaluation techniques, we can gain valuable insights into the strengths and weaknesses of classification models, enabling more informed decision-making in various applications.

The log loss **penalizes more heavily incorrect predictions made with high confidence**.

In other words, if the model is very confident in an incorrect prediction, the log loss will be larger.

This makes it a useful metric for evaluating models that produce probability estimates, as it encourages the model to be confident in its predictions only when justified.

In general, a lower log loss value indicates better calibration of the model's predicted probabilities, and therefore higher accuracy of its predictions.

**<u>Example</u>**

In a scenario where we want to classify images from a balanced dataset as either containing cats or dogs, we can compare two classifiers to illustrate the differences between accuracy and logloss.

**Classifier 1**

- Correctly identifies the category in 80 out of 100 cases • Exhibits varying levels of confidence:

- 100% certainty in correct predictions, but only 80% of the time.

- Confidence drops significantly in incorrect predictions, sometimes as low as 51%.

**Classifier 2**

- Achieves accuracy in 95 out of 100 cases, indicating higher accuracy compared to Classifier 1.

- Always seems sure of its predictions:

- confidently predicts an image to be a cat, even when it actually contains a dog

At first glance, it's evident that Classifier 2 has a higher accuracy rate, making it seem like the superior model.

However, **accuracy alone may not provide a complete picture of a classifier's performance.**

This distinction in confidence levels between the two classifiers is crucial in understanding their performance beyond accuracy. Classifier 1 may have a lower accuracy rate, but its confidence levels in correct predictions are more consistent compared to Classifier 2, which exhibits overconfidence in its incorrect predictions.

This **difference in confidence levels** directly **affects the logloss**, which **looks at how sure a classifier is about its predictions**. While accuracy gives a simple measure of how often a classifier is right, it might not show all the details, especially about how confident the classifier is. Logloss gives us a better understanding by looking at these details, making it a more complete way to assess a classifier's performance.

**Logloss is like a measure of confidence** or certainty within the model.

When the **model assigns <u>strong probabilities to its prediction</u>**s, the **<u>logloss</u>** tends to be <u>low</u>, approaching zero. You can think of logloss as a way to measure uncertainty: a **<u>lower logloss</u>** indicates that the model is **<u>more</u> <u>confident about its predictions.</u>**

Uncertainty can be thought of as a measure of how unpredictable something is, therefore logloss may be called entropy.

So, when a model has low uncertainty or entropy, it means it's more certain and less messy in its predictions. Similarly, a low logloss indicates that the model is confident and less messy in its predictions.

While accuracy focuses on counting correct predictions, logloss delves deeper into the quality of these predictions. **Logloss prefers models that can confidently differentiate between different categories** or classes. Essentially, if a model is proficient at distinguishing between various categories, it tends to have a lower logloss.

#### CONFUSION MATRIX ~~A~~ND SKLEARN

If the question is “***can I use confusion matrix as a scoring metric in a CV-based approach, using sklearn***?", the answer basically is **NO**.

When we discuss using the confusion matrix as a scoring metric in a cross-validation (CV) approach with \`sklearn\`, it's essential to grasp the distinction between:

- Cross-validation as a method for model selection = it helps us determine the best model among various candidates by repeatedly splitting the dataset into training and testing sets and evaluating each model's performance.

- The specific function \`cross_val_score\` provided by the \`sklearn\` library = it focuses on returning scores, typically floating-point numbers, that represent the performance of each model.

Scores generated by \`cross_val_score\` are crucial for comparing different models. For example, if we have two models, method A and method B, we can compare their respective scores to determine which one performs better. These scores provide a quantitative measure of how well each model predicts outcomes.

Contrastingly, a confusion matrix offers a more detailed insight into a model's performance during evaluation. It provides information about true positives, true negatives, false positives, and false negatives.

Each element in the confusion matrix represents the count of instances where the predicted label matches the true label or where it differs. While confusion matrices are valuable for understanding the nuances of a model's classification performance, they are not suitable as scoring metrics like the scores returned by \`cross_val_score\`.

In the context of cross-validation, each evaluation run may produce its confusion matrix, reflecting the performance of the model on a specific fold or split of the data.

However, it's important to note that generating a confusion matrix for each evaluation run requires additional code, as it's not directly provided by the \`sklearn\` library's \`cross_val_score\` function.

---
> [[AML 26 - Machine Learning Development · Resampling|← Machine Learning Development · Resampling]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 28 - Machine Learning Development · Hyper-parameters Tuning|Machine Learning Development · Hyper-parameters Tuning →]]
