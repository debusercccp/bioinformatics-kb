---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 40
tags: [note, aml]
---

> [[AML 39 - Ensemble Learning + ENSEMBLE – Voting (hard voting – soft voting)|← Ensemble Learning + ENSEMBLE – Voting (hard voting – soft voting)]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 41 - ENSEMBLE – Stacking + Convolutional Neural Networks (CNN)|ENSEMBLE – Stacking + Convolutional Neural Networks (CNN) →]]

# Random Forests

> A Random Forest is an ensemble of DTs, generally trained via the **bagging** (sometimes **pasting**) method.

- in sklearn, does this mean to build a **BaggingClassifier** and pass it a **DecisionTreeClassifier**? Yes but.

- .. one can instead use the **RandomForestClassifier** class (similarly: **RandomForestRegressor**), which is more convenient and optimised for DTs Random Forest algo introduces extra randomness when growing trees:

- When splitting a node, a Random Forest **doesn’t look for the best feature** overall.

> Instead, it selects the best split from a **random subset of features**.

- This adds **more randomness**, resulting in:

- **Greater tree diversity**

- **Higher bias**, but

- **Lower variance**, which generally improves generalization.

> additional randomness → Extremely Randomised Trees ensembles. Another quality of Random Forests is that they make it easy to measure the relative importance of each feature.
>
> **Boosting**
>
> Boosting (originally called “**hypothesis boosting**”) refers to any ensemble method that can **combine several weak** **learners** into a strong learner, with the general idea to **train predictors sequentially**, each trying to correct its predecessor. The two most popular methods are **AdaBoost** (adaptive Boosting) and **Gradient** **Boosting**.
>
> **AdaBoost (Adaptive Boosting)**
>
> AdaBoost is a predictor that corrects/improves its predecessor by paying a bit more attention to the **training** **instances** that the predecessor underfitted. This results in new predictors focusing more and more on the hard cases.

- A **first base classifier** (such as a DT) is trained and used to make predictions on the training set. The **relative weight** of misclassified training instances is then **increased**. A second classifier is trained using the updated weights and again it **makes** **predictions** on the training set, then weights are updated.

- The ensemble progressively **focuses more on difficult cases**. Works well with **shallow trees**, reducing bias and variance over time.

> **Gradient Boosting**
>
> Gradient Boosting works by **sequentially** adding predictors to an ensemble, each one correcting its predecessor, but while **AdaBoost** tweaks the instance weights at every iteration, Gradient Boosting tries to fit the new predictor to the residual errors made by the previous predictor.
>
> Instead of updating instance weights, each new model is trained to **predict the residual errors** (i.e., what's left to correct) from the previous model.

![[AML-image265.jpg|642]]

> Now we have an ensemble containing 3 trees. It can make predictions on a new instance simply by adding up the predictions of all the trees. ![[AML-image266.jpg|642]]
>
> **Gradient Boosting tuning**
>
> Change the **learning_rate hyperparameter**: it scales the contribution of each tree. If you set it to a low value (such as 0.1 in this example), you will need more trees (*n_estimators*) in the ensemble to fit the training set, but the predictions will usually generalise better.

![[AML-image267.jpg|642]]

> **XGBoost (Extreme Gradient Boosting)**
>
> An optimized implementation of Gradient Boosting is available in the popular python library XGBoost, i.e. **Extreme Gradient Boosting**. XGBoost is one of the **fastest** **implementations** of gradient boosted trees. How does it work?
>
> It directly **attacks** one of their **major inefficiencies**. It considers the **potential loss** for all possible splits to create a new branch (especially useful in case of thousands of features, therefore thousands of possible splits), and tackles this inefficiency by looking at the **distribution** **of** **features** across all data points in a leaf and using this information to reduce the search space of possible feature splits. Yes, it uses a few regularisation tricks, but the achievable speed up is by far the **most useful aspect** of the XGBoost library: it allows many hyperparameter settings to be investigated quickly.
>
> ![[AML-image268.jpg|525]]

---
> [[AML 39 - Ensemble Learning + ENSEMBLE – Voting (hard voting – soft voting)|← Ensemble Learning + ENSEMBLE – Voting (hard voting – soft voting)]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 41 - ENSEMBLE – Stacking + Convolutional Neural Networks (CNN)|ENSEMBLE – Stacking + Convolutional Neural Networks (CNN) →]]
