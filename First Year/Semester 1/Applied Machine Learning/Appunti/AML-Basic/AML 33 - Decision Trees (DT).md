---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 33
tags: [note, aml]
---

> [[AML 32 - Non-linear Classification|← Non-linear Classification]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 34 - Keras Interface for a Shallow NN|Keras Interface for a Shallow NN →]]

# Decision Trees (DT)

> **Decision Trees (DTs)** are highly versatile machine learning algorithms capable of handling a wide range of tasks:

- They can perform **both classification and regression**, including **multi-output tasks**

- They are powerful enough to fit **complex, non-linear datasets**

- DTs are also the fundamental building blocks of **Random Forests**, one of the most powerful ensemble learning methods used today Why use decision trees?

- **Minimal data preparation required**: no need for feature scaling or normalization

- Naturally handle both **numerical** and **categorical features**

- Easy to set up and fast to train

- Work well even with **imbalanced datasets** or **non-linear relationships**

> A DT can estimate the probability that an example (or instance) belongs to a particular class k:

- first, it traverses the Tree to find the leaf node for this instance

- second, it returns the ratio of training instances of class k in this node

> Decision Trees learn patterns by **splitting** the dataset into branches based on the feature values. Each split is a **threshold** (e.g., “is petal length ≤ 2.5?”). At each node:

- If the condition is **true**, the instance follows the **left** branch

- If **false**, it follows the **right** branch

> This continues recursively until a **leaf node** is reached.

![[AML-image209.jpg|639]]

> **Example: Iris Dataset**
>
> This classic dataset contains features like:

- Sepal length and width

- Petal length and width

- Three flower classes (Setosa, Versicolor, Virginica)

> A Decision Tree can automatically learn rules that separate Setosa (which is linearly separable) from the other classes based on, for example, petal length.
>
> Once trained, a Decision Tree can estimate the **probability** that an instance belongs to a class k:

1.  Traverse the tree to reach the corresponding **leaf node**

2.  Compute the **ratio** of training samples of class kkk in that node

> ![[AML-image210.jpg|301]]In scikit-learn, this is done via the predict_proba() method, which returns an array of probabilities for each class.
>
> This script tells you the probability that will be split out will be in a python array with the probabilities.

![[AML-image211.jpg|559]]

> This is how the points look like; I’ve drawn identifying the region having point given kind of flower. Setosa in very far away from the others.
>
> How is your intuition of the characteristics of this algo?
>
> Decision Trees are intuitive, and decisions are easy to interpret: one of the most appreciated features of Decision Trees is their **transparency**:

- They are considered **"white-box" models**

- You can easily **reconstruct the path** from root to leaf that led to any prediction

- The rules used for classification are **explicit** and **human-readable**

- This makes it possible to apply the same logic “manually” if needed, even outside of an ML context **In contrast:**

- **Random Forests** and **Neural Networks** may provide **higher predictive performance**

- However, they are typically seen as **"black-box" models** o You can trace calculations, but not always understand **why** a prediction was made

> o Interpretation is possible, but not as intuitive **Why Decision Trees Are Appealing**

- Intuitive to understand and visualize

- Transparent: you can see **exactly what decisions were made**

- Powerful enough to model **complex patterns**

- Require **little to no preprocessing**

- Serve as a **foundation** for more advanced ensemble methods like **Random Forests** and **Gradient Boosted Trees**

> **CART: classification and regression Tree**
>
> Sklearn uses the CART algo to train DTs. Short for *Classification And Regression Tree*. This is a powerful yet intuitive method for both classification and regression tasks.

- it produces only **binary trees** (non-leaf nodes always have **2 children**, i.e. questions only have yes/no answers)

- Other algos (such as ID3) can produce DTs with nodes that have \>2 children At each step, CART:

> Evaluates all possible splits using a single feature k and a threshold tk. Chooses the pair (k,tk)that produces the **purest** subsets (i.e., subsets with the most homogeneous labels) and recursively splits the resulting subsets using the same logic.
>
> ❖ The cost function that the CART algo
>
> ![[AML-image212.jpg|483]]
>
> tries to minimize for classification is:

- it splits the 2 sub-sets in 2 again using the same logic, and so on, recursively, until indicated by the max_depth hyperparameter (or if it cannot find a split that will reduce impurity). Some algorithms don’t split in two but even more.

> Hyperparameters will tell you how deep you want to go or decide when you want to stop with a specific tree.
>
> The algorithm stops when one of the following occurs:

- The **max depth** is reached

- Further splits do not improve purity

- Other stopping criteria are met (e.g., min_samples_split, min_samples_leaf, etc.) he CART algorithm uses **cost functions** to decide the best split.

- For **classification**, it minimizes **Gini impurity** (default in sklearn) or **entropy**

- For **regression**, it minimizes the **Mean Squared Error (MSE)**

> Suppose you have a regression tree trained on 200 data points. A new input x1=0.6x_1 = 0.6x1 =0.6 is evaluated by traversing the tree. It ends up in a leaf node where: 110 training samples are grouped, the predicted value is the **average target value** of these 110 points (e.g., 0.111),

![[AML-image213.jpg|504]]

> The MSE in that leaf is 0.015.
>
> Red is our outcome; we are trying regression for decision tree. Larger depth make you become more and more precise but be careful overfitting!
>
> **Deeper trees** can model the data more precisely—but also risk **overfitting**: regularization is essential to control the depth and complexity of the tree. Examples of important hyperparameters:

- *max_depth*: limits the depth of the tree

- *min_samples_split*: minimum number of samples required to split an internal node

- *min_samples_leaf:* minimum number of samples required in a leaf node

- *min_weight_fraction_leaf*: fraction of total samples required in a leaf

- *max_leaf_nodes*: limits the number of terminal nodes (leaves)

> **CART for classification/ regression:**
>
> The CART algo for regression (classification) tries to split the training set in a way that minimises impurity (MSE), it produces only binary trees (non-leaf nodes always have 2 children, i.e. questions only have yes/no answers).

- The cost function that the CART algo tries to **minimise** for classification was:

> ![[AML-image214.jpg|510]] then, it splits the **2 sub-sets** in 2 again using the same logic, and so on, **recursively**, until indicated by the max_depth hyperparameter (or if it cannot find a split that will reduce impurity).
>
> **DTS prone to overfitting**
>
> Just like for classification tasks - DTs are prone to overfitting also when dealing with **regression** **tasks**. Using the default hyper-parameters, i.e. without any regularization, you get the predictions of type \[A\]. Just setting min_samples_leaf=10 in sklearn results in a much more reasonable model as in \[B\] below.

![[AML-image215.jpg|642]]

> Prediction with overfitting: applying depths limits you would like to have your hands on another hyperparameter. When you get to the limit you need STOP, otherwise you will get overfitting.

![[AML-image216.jpg|642]]

> E.g. *DecisionTreeClassifier(max_leaf_node=N)* specifies N leaves at maximum, so - unless the tree builder has some other reasons to stop - it will **hit** **the** **max**. Suppose I run it with N=10, it might happen that some (e.g. 4) of the N leaves would have a very small amount of samples (e.g. ≲3) compared to the others 6 leaves (e.g. ≳50), this being a possible sign of over-fitting. One could “**prune**” the tree a-posteriori (after training). Or another viable option is to specify either *min_samples_leaf* (or *min_samples_split*) to better guide the training: it will likely get rid of the problematic leaves. e.g. set the value 0.03 if you want at least 3% of examples.
>
> ![](media/media/image219.png) CART is **sensitive to variations in the training data:**
>
> Even with the same data, results can vary due to the **stochastic** nature of the algorithm, this makes individual decision trees unstable.
>
> Additionally, remember that since the training algo used by sklearn is stochastic, one may get different models even on the same training data. Remember: sensitive to variation in data.
>
> To mitigate the instability of single decision trees:

- **Random Forests** train **many decision trees** on different subsets of the data and average their predictions

- This leads to:

> o More **robust** and **accurate** predictions o **Reduced overfitting** o Better generalization

---
> [[AML 32 - Non-linear Classification|← Non-linear Classification]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 34 - Keras Interface for a Shallow NN|Keras Interface for a Shallow NN →]]
