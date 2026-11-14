---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 19
tags: [note, aml]
---

> [[AML 18 - Model Diagnostics|← Model Diagnostics]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 20 - Model Diagnostics · Model Selections & Tvt Sets|Model Diagnostics · Model Selections & Tvt Sets →]]

# Training/testing Procedure

After formulating a hypothesis and training our learning algorithm to minimize the training error, it's essential to evaluate the effectiveness of the hypothesis thoroughly. **Achieving a low training error may not necessarily indicate a successful model,** as it could be due to overfitting to the training data.

To assess whether our model can generalize well beyond the training data and make accurate predictions on new data, we need to conduct proper evaluation steps.

One crucial step is to partition the dataset into a **TRAINING SET** and a **TEST SET*.***

The majority of the data, around **70%**, is used for **training**, while the remaining portion is reserved for testing.

![[AML-image104.jpg|329]]It's vital to avoid any peeking at the test data during model development to ensure an unbiased evaluation. Therefore, all **examples** should be **<u>shuffled</u>** and **<u>divided</u> <u>randomly into training and test sets.</u>**

Let *m* represent the **index for the training set**, while the remaining examples are allocated to the test set. This random partitioning ensures that both sets hold the same statistical significance, enabling the model to be constructed using the training data without any prior knowledge of the test set.

The training/test procedure involves 2 key steps:

1.  **<u>Learning parameters from the training dataset</u>**

Initially, we utilize the training dataset, typically constituting 70% of the total data, to learn the parameters *θ* of our model. The primary objective during this phase is to **minimize the training error** *J*(*θ*) or *J*<sub>train</sub>(*θ*).

2.  **<u>Computing the test set error</u>**

Once the parameters are learned and the training error is minimized, we **proceed to assess the performance of our model using the test set.** This step is crucial as it evaluates how well the model would generalize to unseen data, representing the remaining 30% of the dataset.

By training on 70% of the data and evaluating on the remaining 30%, we gain insights into the model's ability to predict outcomes on new, unseen data.

The **<u>test set error</u> (***J***<sub>test</sub>) provides** a **<u>measure</u> of the <u>model's predictive accuracy on this unseen portion of</u> <u>the dataset</u>.**

It's important to highlight that the test error *J*<sub>test</sub> may differ from the training error *J*<sub>train</sub>, as it reflects the model's performance on previously unseen data.

By comparing these two error metrics, we can assess the model's generalization capability and understand how effectively it performs in real-world scenarios beyond the training data.

![[AML-image105.jpg|697]]

## 11.3 0/1 MISCLASSIFICATION ERROR

While the traditional definition of test set error *J*<sub>test</sub> provides valuable insights into the model's performance, there's an alternative metric known as the 0/1 misclassification error that offers a more intuitive interpretation.

The **0/1 misclassification error <u>simplifies</u>** the **<u>evaluation</u>** process by **<u>categorizing predictions</u> as either correct (0) or incorrect (1)**.

Essentially, for **each example in the test set**, if the model predicts the outcome:

- **Correctly —\> error = 0**

- **Wrongly —\> error = 1**

This metric offers a straightforward measure of how well the model is performing, as **it directly quantifies the proportion of misclassified examples**.

By **averaging these 0/1 errors across the entire test set**, we obtain a **single value** that r**epresents the model's <u>overall misclassification rate</u>.**

To calculate the misclassification error, we first train the model on the training set to learn its parameters. Then, we apply the trained model to the test set and evaluate its predictions.

The resulting misclassification error provides a clear indication of the model's accuracy in classifying unseen data.

![[AML-image106.jpg|391]]

> ![[AML-image107.jpg|448]]

---
> [[AML 18 - Model Diagnostics|← Model Diagnostics]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 20 - Model Diagnostics · Model Selections & Tvt Sets|Model Diagnostics · Model Selections & Tvt Sets →]]
