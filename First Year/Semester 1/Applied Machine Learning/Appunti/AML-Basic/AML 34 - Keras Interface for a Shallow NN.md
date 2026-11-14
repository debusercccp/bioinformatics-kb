---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 34
tags: [note, aml]
---

> [[AML 33 - Decision Trees (DT)|← Decision Trees (DT)]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 35 - MLP for Regression and MLP for Classification|MLP for Regression and MLP for Classification →]]

# Keras Interface for a Shallow NN

> Among the possible **Keras** interfaces (e.g. Sequential, Functional) we focus on the
>
> **Sequential** interface at this stage. The Keras Sequential interface defines a neural network as a sequence of steps.
>
> Before one start learning the model, you specify an **optimizer**, the **loss** **function** to use, and the **metrics** that you want to log during training.

![](media/media/image223.jpeg)

> ![](media/media/image227.jpeg)

![](media/media/image231.jpeg)

> **Data preparation**

![[AML-image233.jpg|283]]

> To fit anything, i.e. before invoking any fit(), you need to prepare your data:
>
> **Fit()=**Similar to sklearn fit method, but in Keras it takes a bunch of other arguments, not only training and test sets.
>
> Training architecture is the important one, with the numbers of epochs.
>
> **Evaluate**

![[AML-image234.jpg|642]]

> **Loggers and callbacks**
>
> The fit() method returns a callback, that you can exploit. The history() methods returns a dictionary, that you can e.g. convert into a Pandas Dataframe and plot.

![[AML-image235.jpg|449]]

> Dictionary transformed into a data frame and then a plot.

![[AML-image236.jpg|484]]

> **10 epochs** do not show strong evidence of overfitting, that is clearer if epochs = 100.

![[AML-image237.jpg|559]]

> In deep learning projects, we often want the **power of Keras** for building neural networks *and* the **convenience of Scikit-learn** for model evaluation, hyperparameter tuning, and pipelines.
>
> To bridge the two frameworks, we use:

*KerasClassifier / KerasRegressor from tensorflow.keras.wrappers.scikit_learn*

> These wrappers allow a Keras model to behave like a **Scikit-learn estimator**, meaning you can:

- Use **GridSearchCV**, **cross_val_score**, and other sklearn tools

- Apply **hyperparameter tuning** easily

- Integrate your Keras model into a **scikit-learn pipeline**

![[AML-image238.jpg|642]]

> **Main Benefits:**

- **Standardised evaluation** using cross-validation

- **Hyperparameter optimization** (like finding best number of epochs, batch size, layers)

- **Integration** into broader ML workflows (e.g. pipelines, feature selection)

> Training deep models with GridSearchCV can be **very verbose** and **hard to read** due to multiple evaluations. You can easily convert results into a Pandas DataFrame for better analysis.
>
> This helps:

- Visually compare different configurations

- Spot trade-offs (e.g. accuracy vs training time)

- Identify the most stable/best-performing setup

![[AML-image239.jpg|487]]

> Training for 10 epochs, with an hidden layer size of 256, a very good training accuracy can be obtained (99.7%), with a 97.6% performance on the test set. With more fine tuning, one could perhaps increase the latter to ~98-99%.

---
> [[AML 33 - Decision Trees (DT)|← Decision Trees (DT)]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 35 - MLP for Regression and MLP for Classification|MLP for Regression and MLP for Classification →]]
