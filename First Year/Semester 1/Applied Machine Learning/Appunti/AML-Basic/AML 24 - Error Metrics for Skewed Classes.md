---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 24
tags: [note, aml]
---

> [[AML 23 - Model Diagnostics · Learning Curves|← Model Diagnostics · Learning Curves]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 25 - Machine Learning Development · Data Preparation + Feature Selection|Machine Learning Development · Data Preparation + Feature Selection →]]

# Error Metrics for Skewed Classes

When working with skewed classes, accuracy alone is not an adequate metric for evaluating classifier performance. Instead, we rely on more informative measures:

- **PRECISION** = proportion of **<u>correctly predicted positive</u>** cases **<u>among all cases predicted as positive</u>**

- **RECALL** = proportion of **<u>correctly predicted positive</u>** cases **<u>among all actual positive cases.</u>**

***Skewed classes*** refer to a situation where there is a **significant imbalance in the distribution of classes within a dataset**. Specifically, one class (the minority class) is heavily outnumbered by another class (the majority class). In this case the algorithms may have difficulty accurately predicting the minority class due to its limited representation in the data.

Example: Let's consider a cancer classification problem where we aim to determine whether patients have cancer based on certain features. This is a binary classification task, where patients are categorized as either having cancer (1) or not (0). We can employ a simple logistic regression model as our hypothesis to predict these labels. Now, suppose when we evaluate our model on a test set, we observe a 1% error rate.

This implies that in 99% of cases, our model correctly predicts whether a patient's diagnosis is malignant or benign.

In the context of classification problems, **NON-LEARNING ALGORITHMS** offer a **straightforward approach** to **assign <u>labels</u>** or categories **<u>based on predefined criteria</u>**, **<u>rather than learning from data.</u>**

For instance, in cancer classification, a non-learning algorithm might determine labels using fixed rules established by medical experts instead of data-driven patterns.

Non-learning algorithms are suitable for well-understood problems where decision-making criteria are explicitly defined. However, they **lack the adaptability and flexibility** of machine learning algorithms, which limits their performance in dynamic or complex environments.

![[AML-image130.jpg|420]]In scenarios where there's a significant class imbalance, meaning that one class is heavily outnumbered by the other, such as when only 0.5% of cases are positive for cancer and the remaining 99.5% are negative, we refer to this as having skewed classes. In such cases, non-learning algorithms, which are simple and don't involve learning from data, might perform better than learning algorithms.

For example, in the context of cancer classification, if we have a vast majority of patients who do not have cancer, a **non-learning algorithm might simply predict that all patients do not have cancer** (**assigning y = 0 to all patients**). Surprisingly, this approach might yield lower error rates than using a learning algorithm that tries to learn patterns from the data.

In scenarios like cancer classification, where obtaining balanced data is impractical, dealing with skewed classes becomes inevitable. **Many datasets** used in **scientific research exhibit this imbalance,** requiring us to address the challenges associated with skewed classes.

## 12.1 CONFUSION MATRIX

![[AML-image131.png|219]]A confusion matrix is a fundamental tool in binary classification, providing a structured representation of model performance. It consists of rows and columns, where:

- **Columns** represent the **actual values** (positives and negatives)

- **Rows** represent the **predicted values** (1 and 0)

**1. TRUE POSITIVE (TP)**

- Instances where the **actual class is positive** (1) and the **model correctly predicts** them as **positive** (1).

- *Example*: In medical diagnosis, a true positive would be when a patient actually has a disease (positive class) and the model correctly identifies them as having the disease.

**2. TRUE NEGATIVE (TN)**

- Instances where the **actual class is negative** (0) and **the model correctly predicts** them as **negative** (0).

- *Example*: In medical diagnosis, a true negative would occur when a patient does not have the disease (negative class) and the model correctly identifies them as not having the disease.

**3. FALSE POSITIVE (FP)**

- Instances where the **actual class is negative** (0) but the **model incorrectly predicts** them as **positive** (1).

- *Example*: In medical diagnosis, a false positive would be when a patient does not have the disease (negative class) but the model incorrectly diagnoses them as having the disease.

**4. FALSE NEGATIVE (FN)**

- Instances where the **actual class is positive** (1) but the **model incorrectly predicts** them as **negative** (0).

- *Example*: In medical diagnosis, a false negative would occur when a patient actually has the disease (positive class) but the model fails to detect it and predicts them as not having the disease.

**<u>Consequence variation</u>**

The **impact of false positives** (FP) **and false negatives** (FN) **can differ** based on the specific application or scenario.

- False Positives (FP) = in medical diagnosis or security screenings, false positives can result in unnecessary actions or anxiety. If a medical test incorrectly indicates that a person has a disease when they actually don't, it might lead to unnecessary follow-up tests, treatments, and unnecessary stress for the individual.

- False Negatives (FN) = they can have more severe consequences, particularly in critical contexts like medical diagnosis. A false negative occurs when the model fails to detect a condition or problem that actually exists. For example, if a medical test fails to detect a disease that a patient truly has, it could lead to a lack of treatment, allowing the disease to progress undetected and potentially causing harm to the patient.

**<u>Positional Dependence</u>**

The arrangement of elements in the confusion matrix is solely determined by the predicted and actual values of the classification, while the classification of positive and negative outcomes depends solely on the predictions made by the model, regardless whether they are true or false

- True Positives (TP) and True Negatives (TN) = instances where the model correctly predicts the class (positive or negative) based on the actual values.

- False Positives (FP) and False Negatives (FN) = These occur when the model incorrectly predicts the class (positive or negative) based on the actual values.

## 12.2 PRECISION

Precision measures the **<u>accuracy of the positive predictions</u>** made by the classifier.

It answers the question: *"Out of all the samples predicted to be positive, how many actually have the condition?"*

Precision is calculated as the number of true positives divided by the total number of predicted positives (true positives + false positives):

$$
\text{Precision} = \frac{\text{True~Positives}}{\text{True~Positives} + \text{False~Positives}}
$$

Precision focuses on **minimizing false positives**, **ensuring** that **when** the **classifier predicts a positive outcome, it is highly likely to be correct.**

A **<u>high precision</u>** score indicates that the classifier **<u>has a low rate of falsely predicting positive samples</u>**, making it reliable when it labels a sample as positive.

Intuitively = Precision is the ability of the classifier **<u>not to label as positive a sample that is negative</u>**.

## 12.3 RECALL

Recall, also known as ***sensitivity*** or *true positive rate*, measures the **ability of the classifier to identify all positive instances.**

It answers the question: *"Out of all the samples that actually have the condition, how many did the classifier correctly predict?”*

Recall is calculated as the number of true positives divided by the total number of actual positives (true positives + false negatives):

#### 
$$
\text{Recall}\mathbf{=}\frac{\text{True~Positives}}{\text{True~Positives}\mathbf{+}\text{False~Negatives}}
$$

Recall focuses on **minimizing false negatives**, **ensuring** that the **classifier captures as many positive instances as possible**, even if it means occasionally misclassifying some negative instances as positive.

A **<u>high recall</u>** score indicates that the classifier is **<u>effective at identifying positive samples</u>**, reducing the likelihood of missing true positive instances.

Intuitively = Recall is the ability of the classifier to **<u>find all the positive samples.</u>**

> ![[AML-image132.jpg|462]]

In precision and recall calculations, we typically **set the condition of interest**, which is often the **rarer class**, as the positive class, represented by **y = 1.**

For instance, when dealing with rare conditions like cancer, where we're interested in detecting the presence of cancerous cases, we assign y = 1 to represent the positive class.

This means that the positive class, in this case, is the presence of cancer, which is the condition we're particularly concerned about identifying accurately.

If we assume that everyone is healthy (meaning there are no cases of the rare condition, like cancer), then there are no true positives (TP), false positives (FP), or false negatives (FN). Therefore, both precision and recall would be 0.

When we talk about a non-learning algorithm, it doesn't consider any data or patterns but simply assigns everyone as healthy. So, in this case, the results would indeed be all zeros: TP = 0, FP = 0, FN = 0, precision = 0, and recall = 0.

Your algorithm has a performance on the test set given by this matrix. Precision = 0.8

Recall = 0.5

![[AML-image133.jpg|424]]![[AML-image134.jpg|164]]

![[AML-image135.jpg|697]]

#### TRADE OFF PRECISION VS RECALL 

We discussed precision and recall as vital evaluation metrics for classification problems, particularly those with imbalanced classes. In many scenarios, we aim to strike a balance between precision and recall. The objective is to configure the system to reliably predict instances where y = 1.

For example, let's consider a decision threshold of 0.5. In this scenario, if the model predicts a cancer probability exceeding 0.5, it will classify the patient as positive for cancer. Otherwise, it will classify them as negative. **Adjusting this threshold allows us to control the model's sensitivity in identifying positive cases**, thereby influencing the balance between precision and recall.

![[AML-image136.jpg|329]]In essence, we want the system to be highly confident when predicting the positive class.

We aim for a high level of certainty in our predictions, ensuring that when the model identifies something as positive, it's indeed true. To achieve this, we often set a threshold, such as 0.7, to determine when to classify an instance as positive.

By setting a **higher threshold 0.7**, for classifying instances as positive, we prioritize precision over recall. This means that **when the model predicts a positive case**, **it's more likely to be correct** (higher precision), **but it may miss some actual positive cases** (lower recall). In other words, the model becomes more selective in labeling instances as positive, leading to fewer false positives but potentially more false negatives.

##### Example 1 

We have 10 patients represented by crosses, using a threshold of 0.5 we classify them into two classes: positive (cancer) and negative (no cancer) and we mark patients classified as positive with a blue circle. Precision measures the accuracy of positive predictions. In our case, we selected 6 patients as positive (blue circles), but only 3 of them actually have cancer (true positives).

Recall measures the ability of the model to identify all positive instances. Out of all patients who have cancer (represented by crosses), the model identified 3 of them correctly as positive (TP). However, 1 patient who actually has cancer was classified as negative (FN)

- ![[AML-image137.jpg|394]]Precision of 0.5 means that out of all patients classified as positive by the model, only 50% of them actually have cancer.

- Recall of 0.75 means that the model identified 75% of all patients who have cancer correctly.

##### Example 2 

![[AML-image138.jpg|332]]When we increase the decision threshold to 0.7, the model becomes more selective in classifying patients as positive for cancer. This adjustment results in 2 true positives (TP), 0 false positives (FP), 2 false negatives (FN), and 6 true negatives (TN). With these values, we calculate the precision and recall metrics.

- Precision = 1, as all of the patients classified as positive by the model actually have cancer, resulting in a precision score of 100%

- Recall = 0.5, indicating that the model identified only 50% of all cancer patients, showing a decrease in recall compared to the previous threshold of 0.5

The choice of decision threshold depends on the specific needs of the problem and the relative implications of false positives and false negatives:

- **Raising the decision threshold** —\> model more selective and leads to **higher precision/lower recall**

- **Lowering the decision threshold** -\> model less selective and leads to **higher recall/lower precision**

In the first case, where we used a threshold of 0.5, the model was less selective and identified a higher proportion of patients as positive for cancer. This scenario might be suitable for selecting patients who need further examination or diagnostic testing to confirm whether they have cancer. The higher recall value indicates that the model is effective at capturing a significant portion of all cancer cases, ensuring that fewer cases are missed.

![[AML-image139.jpg|183]]In the second case, where we increased the threshold to 0.7, the model became more selective and classified fewer patients as positive for cancer. This scenario might be appropriate for recommending surgery or invasive procedures, where it is crucial to be highly confident that the patient indeed has cancer before proceeding with treatment. The higher precision value ensures that a larger proportion of patients classified as positive by the model actually have cancer, reducing the likelihood of unnecessary procedures on patients who do not have the condition.

##### Example 3 

![[AML-image140.jpg|348]]Suppose we set the threshold at 0.9. We predict only if we are 90% certain it is cancer. In this case, we want to identify and be really sure.

With such a threshold, the model becomes very selective and conservative in its predictions. It will classify fewer patients as positive for cancer, but those predictions are expected to be highly accurate. This approach is suitable for scenarios where the consequences of a false positive diagnosis are severe, such as recommending invasive procedures or initiating aggressive treatments like chemotherapy.

##### Example 4 

![[AML-image141.jpg|348]]Setting the threshold at 0.3 means we're being less strict about identifying cancer. The model will say more people have cancer, even if it's not certain. This might catch more cases of cancer, which is good, but it might also say someone has cancer when they don't, which is not so good.

This approach could be useful for spotting possible cases that need further checking. But it might also mean more people have to undergo tests or treatments they don't really need. So, deciding on a threshold like 0.3 involves thinking about how many real cases we want to catch versus how many false alarms we're willing to accept.

Choosing the right threshold for classification can significantly impact the performance of a model. Whether we set it above or below 0.5 depends on the specific needs of the problem we're solving.

> ![[AML-image142.jpg|588]]

## 12.2 F1 SCORE

**How do we decide on the best threshold** and how do we compare models that have different precision and recall values?

Computing the **average of precision and recall** may not provide an accurate representation of a model's performance. This approach t**reats both metrics equally,** assuming that precision and recall are equally important, which may not always be the case. For example, in scenarios where false positives have severe consequences, precision becomes more critical than recall. Similarly, in situations where missing positive instances is unacceptable, recall takes precedence over precision.

In scenarios where false positives or false negatives have severe consequences, precision or recall becomes more critical than the other. Averaging these metrics does not consider this imbalance in importance.

$$
\text{Average} = \frac{\text{Precision} + \text{Recall}}{2}
$$

A common approach to evaluating classification models is to calculate a score that combines precision and recall into a single value, known as the **F1 score**. Unlike simply averaging precision and recall, the F1 score provides a balanced measure of a model's performance by taking the harmonic mean of precision and recall. The **harmonic mean** gives **<u>more weight to lower values</u>**, which means that if either precision or recall is low, the F1 score will reflect that.

This makes the F1 score a better choice for evaluating models, especially in **situations where precision and recall have different implications** or when there is an **imbalance between false positives and false negatives**. It aims for a balance between precision and recall, seeking to maximize both without sacrificing one for the other. When comparing different models or choosing a threshold, the F1 score provides a comprehensive and reliable measure of performance. **It ranges from 0 to 1:**

- **1** indicates **perfect precision and recall**

- **0** indicates **poor performance**

> 
> ``` math
> F_{1} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}
> ```

We started by questioning whether accuracy alone is sufficient as the sole evaluation metric for classification tasks. While accuracy is a common metric, it can be misleading, especially when dealing with imbalanced datasets.

To address the limitations of accuracy, we introduced precision and recall as alternative metrics.

Precision measures the proportion of true positive predictions among all positive predictions, while recall measures the proportion of true positive predictions among all actual positives. We discussed the trade-off between precision and recall: increasing one often leads to a decrease in the other.

Recognizing the need for a unified metric that balances precision and recall, we introduced the F1-score. The F1-score is the harmonic mean of precision and recall, providing a single value that considers both metrics. It is particularly useful when there is an uneven class distribution or when false positives and false negatives have different consequences.

> ![[AML-image143.jpg|593]]

## 12.3 ROC AND AUC

A **Receiver Operating Characteristic (ROC)** is a **graphical representation** of the **performance** of a **classification model across all possible classification thresholds**.

The curve plots the **<u>True Positive Rate (TPR)</u>** **against** the **<u>False Positive Rate (FPR)</u>** **for different threshold values.**

**TRUE POSITIVE RATE (TPR) -** also known as sensitivity or recall, measures the **<u>proportion of actual positive</u>** samples that are **<u>correctly identified as positive</u>** by the model.

It is calculated as the ratio of true positives to the sum of true positives and false negatives.

**FALSE POSITIVE RATE (FPR)** measures the **<u>proportion of actual negative</u>** samples that are **<u>incorrectly</u> <u>classified as positive</u>** by the model. It is calculated as the ratio of false positives to the sum of false positives and true negatives.

> ![[AML-image144.png|329]]

A ROC curve illustrates the relationship between True Positive Rate (TPR) and False Positive Rate (FPR) across various classification thresholds.

- Each point on the ROC curve corresponds to a specific threshold, representing the trade-off between correctly identifying true positives and incorrectly classifying negatives as positives.

- Lowering the classification threshold increases both True Positives and False Positives, influencing the TPR and FPR accordingly.

![[AML-image145.jpg|216]]Ideally, a **perfect classifier would have an ROC curve that passes through the top-left corner of the plot, where TPR is 1 and FPR is 0**. This scenario signifies high sensitivity and a low false positive rate across all thresholds. Conversely, a random classifier's ROC curve would closely align with the diagonal line (45-degree line), indicating no discrimination ability. Thus, the closer the ROC curve is to the top-left corner, the better the model's performance.

![[AML-image146.png|167]]To construct an ROC curve, we typically evaluate a model with different classification thresholds. However, evaluating a model multiple times with varying thresholds can be inefficient. Thankfully, there's an efficient, sortingbased algorithm known as AUC (Area Under the Curve) that provides this information for us. AUC quantifies the overall performance of a classification model by measuring the area under the ROC curve, with higher values indicating better discrimination ability.

AUC is a commonly used metric derived from the ROC curve.

It quantifies the overall performance of a classification model by measuring the entire two-dimensional area underneath the entire ROC curve from

(0,0) to (1,1). AUC ranges in value from 0 to 1:

- a model whose predictions are **100% correct** has **AUC = 1.0**

- a model whose predictions are **100% wrong** has **AUC = 0.0**

- a model whose predictions are **50% correct and 50% wrong** (random guessing) has **AUC = 0.5**

**AUC** can be **interpreted** as as the ***probability that the model ranks a randomly selected positive example “higher” than a randomly selected negative example***. Consider a scenario where examples are arranged in ascending order of logistic regression predictions from left to right.

AUC represents the likelihood that a randomly chosen positive (green) example is positioned to the right of a randomly chosen negative (red) example within this ranking.

> ![[AML-image147.jpg|528]]
>
> AUC (Area Under the Curve) is often favored in classification model evaluation due to several key reasons.

- **AUC is *classification-threshold-invariant* =** meaning it **assesses the quality** of a model's **predictions** **irrespective of the chosen classification threshold.**

> This property is particularly advantageous as it provides a comprehensive evaluation of the model's performance across a range of thresholds, offering insights into its general discriminatory ability.

- **AUC is *scale-invariant* =** focusing on the ranking of predictions rather than their absolute values.

> This characteristic is beneficial as it measures how well the model's predictions are ranked relative to each other, disregarding specific prediction magnitudes.
>
> Consequently, AUC offers a robust evaluation metric that remains unaffected by variations in prediction scales, enhancing its applicability across different datasets and models.

Despite these advantages, AUC also has **<u>limitations</u>** that may restrict its utility in certain scenarios:

- **When the cost of false negatives significantly differs from that of false positives**, optimizing for AUC might not be suitable. For instance, in email spam detection, minimizing false positives is often prioritized, even if it leads to an increase in false negatives.

AUC, however, does not directly address this optimization need, limiting its effectiveness in specific contexts where such trade-offs are critical for decision-making.

- While scale invariance is generally desirable, there are instances where well-calibrated probability outputs **are essential**. In situations where the **calibration of predicted probabilities is crucial for decision-making or risk assessment**, AUC may not provide sufficient information.

Consequently, while AUC remains a popular metric for classification evaluation due to its classificationthreshold-invariant and scale-invariant properties, its application should be evaluated in conjunction with the specific requirements and nuances of the classification task to ensure meaningful insights are derived.

*"Well-calibrated probability outputs" refer to the accuracy of the probabilities assigned by a classification model. In some cases, it's not just enough for a model to predict whether an instance belongs to a certain class, but also for the predicted probabilities to be meaningful and reliable.*

*For example, in applications like medical diagnosis or financial risk assessment, not only do we want the model to predict whether a patient has a certain disease or whether a transaction is fraudulent, but we also want the predicted probabilities to reflect the actual likelihood of these events. In other words, if a model predicts that a patient has a 70% chance of having a disease, ideally, that probability should accurately reflect the patient's actual likelihood of having the disease.*

---
> [[AML 23 - Model Diagnostics · Learning Curves|← Model Diagnostics · Learning Curves]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 25 - Machine Learning Development · Data Preparation + Feature Selection|Machine Learning Development · Data Preparation + Feature Selection →]]
