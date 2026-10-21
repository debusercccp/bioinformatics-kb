---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 39
tags: [note, aml]
---

> [[AML 38 - Gradient Based Optimization|← Gradient Based Optimization]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 40 - Random Forests|Random Forests →]]

# Ensemble Learning

> Combining the predictions of multiple models leads to better performance than relying on a single model. This is inspired by the “**wisdom of the crowd**” principle — aggregating opinions from multiple experts usually yields more reliable decisions.
>
> This idea in ML gives this tactic:

- **run** a **group** of predictors (such as classifiers or regressors)

- **aggregate** their **predictions**

> A group of predictors is called an “**ensemble**” → these techniques are referred to as
>
> “**Ensemble** **Learning**” (Ensemble algos/methods). The most popular ensemble methods are:

- voting

- bagging (Bootstrap Aggregation)

- boosting

- stacking

## ENSEMBLE: Voting (hard voting – soft voting)

> I trained various classifiers. Each one achieving its **own** (goodish) **accuracy**.
>
> ![[AML-image262.jpg|313]]An even better classifier can be built by **aggregating** the **predictions** from each classifier and then predict, per each instance, the class that gets the most votes out of the ensemble of classifiers.
>
> These diverse predictions can say something about that. The **majority of votes wins**, but in this case, you just count the votes. Putting one classifier together with the other, the
>
> classifier has a stronger power. This idea of **hard voting** might work but might be perhaps fragile.
>
> A voting classifier often achieves higher accuracy than the best classifier in the ensemble.
>
> • even if each classifier is a **weak learner** (i.e. only slightly better than random guessing), the ensemble of classifiers can still be a **strong learner** (i.e. achieving high accuracy), provided

1)  there are **a sufficient number of weak learners** and

2)  they are **sufficiently diverse**.

> This is thanked to the **law or large numbers**. You can use also but classifier, that are right 51% of the times. The ensemble of that classifier can be a stronger learner than the original one. There must be a high number obviously, and they should be diverse! They should be independent one from the other.
>
> Suppose I build an ensemble containing 10^3 classifiers that are relatively poor, i.e. individually correct only 51% of the time (barely better than random guessing). If I predict the majority voted class, I can hope for something up to 75% accuracy. However, this is true if all classifiers are perfectly independent, make **uncorrelated errors**, etc (impossible, they are trained on the same data.). Best is to put together **diverse classifiers** trained using very **different algos**, i.e. higher chances they will make very different types of errors, thus improving the ensemble’s accuracy.
>
> **Soft Voting classifiers**
>
> If (and only if) all classifiers you select for your ensemble can **estimate class probabilities** (i.e. in sklearn they have a predict_proba() method), then you can avoid a hard voting, and instead use **sklearn** to predict the class with the highest-class probability, averaged over all the individual classifiers.
>
> **Bagging**
>
> Instead of using different training algos to get different predictors in the ensemble, just use the same training algo for every predictor, but train them on different random subsets of the training set. They are trained by a different subset of data. You can allow some **overlap** or allow **different** **subsets**.
>
> For each predictor:

- Randomly draw samples **with replacement** from the training set (bootstrap sampling).

- Train the model on this subset.

> Random sampling performed **w** **replacement** (use instances more than once) → Bagging (Bootstrap AGGregation → “bootstrap=True” in the sklearn implementation).
>
> Aggregation of predictions from all predictors is typically the **most frequent** (hard voting) for classification, or the average for regression. they can be **trained in parallel** (multiple CPUs or different servers, even), one of the reasons why they are popular: they scale up well.

![[AML-image263.jpg|558]]

> With bagging, for any given predictor, some instances may be **sampled several times**, while others may not be sampled at all. only ![[AML-image264.png|10]]63% of the m training instances are sampled on average for each predictor. On m training instances, bagging (i.e. w/ replacement) gives a chance for an instance of not being selected in any of draws as (1-1/n)n, which for large n yields 1/e ≈ 0.37. These remaining 37% are called “**out-of-bag**” (oob) training. As a predictor never sees the **oob** instances during training, it can be **evaluated** on **these** **instances**, without the need for a separate validation set. by adding **oob_score**=**True** in my
>
> BaggingClassifier in sklearn, I can perform an oob evaluation of the ensemble’s accuracy on that test set (averages out the oob evaluations of each predictor).

---
> [[AML 38 - Gradient Based Optimization|← Gradient Based Optimization]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 40 - Random Forests|Random Forests →]]
