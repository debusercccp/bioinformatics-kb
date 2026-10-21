---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 68
tags: [note, aml]
---

> [[AML 67 - Data visualization|← Data visualization]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]]

# Matplotlib - Customization & Advanced Features

**Styling & Customization**

- **Change colors**, line styles, markers, ... *color=‘red’, linestyle=‘--’*

- **Adjust figure size** & resolution *figsize=(8,6), dpi=100*

- **Use gridlines, legends, and annotations** *plt.grid(True), ax.legend()*

**Themes & Styles**

- **Use predefined styles** *plt.style.use(‘ggplot’)*

> *plt.style.available*

- **Customize font and background colors** *ax.set_facecolor()*

**Advanced Layouts & Subplots**

- **Multiple plots in one figure** *plt.subplots(ntows, ncols)*

- **Adjust spacing** *fig.tight_layout()*

- **Share axes across subplots** *sharex=True, sharey=True*

**Interactive & Live Updating Plots**

- **Interactive visualizations** *plt.ion* for Jupyter Notebooks

- **Can animate plots** *from matplotlib.animation import*

> *FuncAnimation*

| **Lecture 4- Data Management**      |
|-------------------------------------|
| **Exploratory Data Analysis (EDA)** |

Exploratory Data Analysis (EDA) is a crucial step in the data analysis process that involves examining datasets to summarize their main characteristics, often using visual methods.

It helps in:

- understanding the data, o what is the information our data carry? o what characteristics will be useful for their analysis?

> o what are the limitations?

- uncovering patterns,

- check data consistency,

- spotting anomalies,

- and testing hypotheses.

The major steps in a comprehensive EDA include:

- **Understand the Dataset**: Examine the dataset's structure, content, and context. Identify data types, review variable definitions, and assess data quality. This provides a clear understanding of the information contained in the dataset and its potential value for analysis.

- **Data Cleaning**: Identify and handle missing or inconsistent data. This may involve imputing missing values, correcting errors, or removing irrelevant data to ensure the dataset is accurate and reliable.

- **Descriptive Statistics**: Generate summary statistics such as mean, median, standard deviation, and range for numerical variables. For categorical variables, calculate frequencies and mode. This step provides insights into the central tendency and dispersion of the data.

- **Data Visualization**: Create visual representations like histograms, box plots, scatter plots, and bar charts to identify patterns, trends, and potential outliers. Visualization aids in understanding relationships between variables and detecting anomalies.

- **Identify Outliers and Anomalies**: Detect data points that deviate significantly from the rest of the dataset. Investigate these anomalies to determine if they result from data entry errors, measurement errors, or genuine variability.

- **Assess Relationships Between Variables**: Analyze correlations and interactions between variables using correlation matrices or pair plots. This helps in understanding dependencies and potential predictors for modeling.

- **Dimensionality Reduction**: If dealing with high-dimensional data, apply techniques like Principal Component Analysis (PCA) to reduce the number of variables while retaining most of the information. This simplifies analysis and visualization.

- **Formulate Hypotheses**: Based on the insights gained, develop hypotheses about the data. These hypotheses can guide further analysis and inform decision-making processes.

- **Document Findings**: Summarize the insights, patterns, and anomalies discovered during EDA. Proper documentation ensures that the findings can be referenced in future analyses and supports transparency.

First step is to just inspect what is the content of our data.

To do this it can be useful to adjust numbers formatting and get high-level info about our features.

**UNIVARIATE DISTRIBUTION**

Once we have a general understanding of our data content, the next step is to inspect the distributions of features.

An important step in the initial stage is to check if there are **missing values**.

**Note:** sometimes this is not enough, and spotting missings is more tricky.

For example, some data have missing values encoded as *weird* values. This means they use values that are out of scale with respect to normal feature values, e.g.:

- Area: -1

- Growth Rate: 9999 Remember to always:

- check data documentation

- carefully inspect data

- ...if you are sharing data: please provide comprehensive documentation to maximise re-use!

Another aspect you may want to check are **unique values**. This is helpful to check data consistency and uncover unexpected patterns.

For example:

- feature with only 1 unique value: all entries are equal, so we cannot discriminate based on that feature

**DATA VISUALIZATION**

Can we explore the distributions more easily?

Looking at tables gives you a precise idea of the scale of features, their values, ... ...but sometimes it is not that easy to digest. In those cases, we can leverage data visualization techniques to gain more readable insights.

In one picture we can spot several data characteristics and compare all features at once. For example, most variables have a left-skewed distribution with the core shifted towards low values and longer right tails.

Growth Rate is instead more symmetric and centered around 1.

![[AML-image420.jpg|642]]

In general, data exploration is not a linear process! We typically jump back and forth from univariate to bivariate analysis depending on questions that arise along the way.

An example where we could be interested in the joint distribution of two features is if we want to inspect the population not in general, but by Continent.

**CORRELATIONS**

Now we explore a bit the relationships among pairs of features. Possible questions we may be interested in:

- What are the most correlated features?

- Is this expected?

- What do you expect for correlation between population and area?

**Note:** you can explore different kinds of correlation measures by changing the argument method in .corr():

- kendall : Kendall Tau correlation coefficient

- spearman : Spearman rank correlation

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p>Spearman’s ρ (<strong>rho</strong>) è un <strong>indice di correlazione non parametrico</strong> che misura quanto due variabili sono <strong>ordinatamente correlate</strong>. Invece di misurare <strong>quanto due variabili sono correlate in modo lineare</strong> (come fa la correlazione di Pearson), <strong>Spearman misura se due variabili crescono o decrescono insieme in maniera ordinata</strong>, anche se la relazione non è perfettamente lineare. <img src="_attachments/AML-image217.png" width="300"></p>
<p><strong>Pearson’s correlation (r)</strong> misura <strong>solo relazioni lineari</strong> tra due variabili.</p>
<ul>
<li><p>Se una variabile cresce e l’altra cresce in modo proporzionale → <strong>correlazione alta</strong>.</p></li>
<li><p>Se una variabile cresce e l’altra decresce in modo proporzionale → <strong>correlazione negativa alta</strong>.</p></li>
</ul>
<p><strong>Spearman’s correlation (ρ)</strong> misura <strong>qualsiasi relazione monotona</strong> tra due variabili, anche se non è lineare.</p>
<ul>
<li><p>Se una variabile cresce e l’altra cresce (anche in modo non proporzionale) → <strong>correlazione positiva</strong>.</p></li>
<li><p>Se una variabile cresce e l’altra decresce (anche in modo non proporzionale) → <strong>correlazione negativa</strong>.</p></li>
</ul>
<p><strong>Come funziona Spearman’s ρ?</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

1.  **Converti i dati in ranghi** (cioè ordinali: primo, secondo, terzo, ecc.)

2.  **Calcola la correlazione di Pearson** sui ranghi invece che sui valori originali.

> **Esempio pratico:**
>
> Immaginiamo di avere due studenti e i loro voti in Matematica e Storia.

**Studente Voto Matematica Voto Storia Rank Matematica Rank Storia**

<table style="width:80%;">
<colgroup>
<col style="width: 0%" />
<col style="width: 10%" />
<col style="width: 3%" />
<col style="width: 19%" />
<col style="width: 3%" />
<col style="width: 12%" />
<col style="width: 3%" />
<col style="width: 20%" />
<col style="width: 3%" />
</colgroup>
<thead>
<tr>
<th>A</th>
<th></th>
<th>90</th>
<th></th>
<th>85</th>
<th></th>
<th>1º</th>
<th></th>
<th>1º</th>
</tr>
</thead>
<tbody>
<tr>
<td>B</td>
<td></td>
<td>80</td>
<td></td>
<td>75</td>
<td></td>
<td>2º</td>
<td></td>
<td>2º</td>
</tr>
<tr>
<td>C</td>
<td></td>
<td>70</td>
<td></td>
<td>65</td>
<td></td>
<td>3º</td>
<td></td>
<td>3º</td>
</tr>
<tr>
<td colspan="9"><p>I ranghi sono identici → <strong>ρ = 1</strong> (correlazione perfetta).</p>
<p>Se i ranghi fossero perfettamente inversi, <strong>ρ = -1</strong> (correlazione inversa perfetta). Se non c’è nessun ordine coerente, <strong>ρ ≈ 0</strong> (nessuna correlazione).</p></td>
</tr>
<tr>
<td colspan="9"><p>Kendall’s <strong>τ (tau)</strong> è un coefficiente di <strong>correlazione non parametrico</strong> che misura <strong>quanto due variabili sono ordinate allo stesso modo</strong>.</p>
<p><strong>In parole semplici:</strong> confronta le <strong>coppie di dati</strong> e vede <strong>quante mantengono lo stesso ordine</strong> e <strong>quante lo invertono</strong>. Dopodichè applica una formula per valutare il valore di tau</p></td>
</tr>
</tbody>
</table>

> che se è negativo e circa 1 descrive una correlazione negativa, altrimenti positiva o se è circa 0 una correlazione inesistente.

![[AML-image421.jpg|642]]

**OUTLIERS**

A very important (crucial) aspect to inspect is the presence of outliers, i.e. values that are very far from the central part of the distribution of a feature.

How to define what an outlier is, is not so easy. Sometimes *weird/extreme* values are just part of the distribution. Other times, they may be the result of some typing errors in data collection, unspecified missing values encoding, ...

**DATA PREPARATION**

Let's explore how to prepare your data in Python in such a way to best expose the structure of the problem to the ML algorithms, and we will do it by using ***scikit-learn***. Focus will be on:

1.  Rescaling the data

2.  Standardizing the data

3.  Normalizing the data

4.  Binarizing the data

**SCIKIT-LEARN**

The *scikit-learn* library provides two standard idioms for transforming data. Each is useful in different circumstances.

- Fit and Multiple Transform

- Combined Fit-And-Transform

After importing the datas, procedure continues with:

1.  Rescale data: You can rescale your data using scikit-learn using the MinMaxScaler class

2.  You can standardize data using scikit-learn with the StandardScaler: The values for each attribute now have a mean value of 0 and a standard deviation of 1.

3.  Normalize data: You can normalize data in Python with scikit-learn using the Normalizer class

4.  You can normalize data in Python with scikit-learn using the Binarizer class So, you can prepare your data for ML in Python using **scikit-learn, with 4 recipes.**

**DATA CLEANING**

Data cleaning is one of the most important steps in a data analysis workflow.

Sometimes this is the most important part! [<u>Surveys</u>](https://www.google.com/url?q=https%3A%2F%2Fwww.pragmaticinstitute.com%2Fresources%2Farticles%2Fdata%2Fovercoming-the-80-20-rule-in-data-science%2F) reveal that ML practitioners spend on average about 80% of their time on finding, cleaning, and organizing the data!!

Common steps include:

- **ensuring data are correctly imported**

- **check format consistency**

- **checking missing values** o discard missing values o impute missing values

- **check for outliers and decide how to treat them**

**<u>MACHINE LEARNING EXAM BASIC</u>**

1)  **In a ML project, which of the following is a wrong way to handle missing/corrupted data in an input dataset?**

> Scegli un'alternativa:

1.  Ignore missing/corrupted values if they affect less than 25% of the total dataset

2.  Replace missing/corrupted values with mean/median/mode

3.  Drop rows or columns that contain missing/corrupted entries

4.  Assign a unique category to missing/corrupted values

<!-- -->

2)  **When would you reduce dimensions in your data?**

> Scegli un'alternativa:

1.  When you have a limited set of features with very diverse characteristics

2.  When you have a large set of features with similar characteristics

3.  When you work with data-intensive science

4.  When you work with Big Data

<!-- -->

3)  **Which of the following is false about cross validation?**

> Scegli un'alternativa:

1.  It can help in hyper-parameter tuning

2.  It can be used in classification or regression ML project

3.  It can help to reduce overfitting

4.  It can help in reducing computation time

<!-- -->

4)  **What is Scikit-learn?**

> Scegli un'alternativa:

1.  An open-source ML library that supports supervised and unsupervised learning

2.  A Google ML library that supports all existing types of machine learning

3.  A Google ML library that supports supervised and unsupervised learning

4.  An open-source ML library that supports all existing types of machine learning

<!-- -->

5)  **Which class of ML algorithms is generically adequate to find patterns in data when the data is not labeled?**

> Scegli un'alternativa:

1.  Reinforcement learning

2.  Unsupervised learning

3.  Deep learning

4.  Supervised learning

<!-- -->

6)  **Which of the following are good test dataset characteristics, e.g. for a classification case?**

> Scegli un'alternativa:

1.  Large enough to yield meaningful results, and containing examples only from some classes

2.  Always larger that the training dataset, and containing examples only from some classes

3.  Large enough to yield meaningful results, and representative of the total dataset

4.  Always larger than the training dataset, and representative of the total dataset

<!-- -->

7)  **Which among these is true about Jupyter?**

> Scegli un'alternativa:

1.  Jupyter requires network to be be used

2.  Jupyter allows to create and share code, plots, documents

3.  Jupyter targets the compilation of large portion of ML code

4.  Jupyter allows to write ML-related code in Python and C++ only

<!-- -->

8)  **Which class of ML algorithms is generically adequate to make classification predictions in case you have input data examples and truth information for each?**

> Scegli un'alternativa:

1.  Supervised learning

2.  Deep learning

3.  Unsupervised learning

4.  Reinforcement learning

<!-- -->

9)  **What does a classification model ultimately do?**

> Scegli un'alternativa:

1.  Clusters responses in groups based on similarity, to find patterns

2.  Assigns data to one out of few predefined categories

3.  Produces predictions whose performance can be measured by e.g. MSE or MAE

4.  Predicts real number responses such as changes in temperature, date, or time

<!-- -->

10) **In ML, which evaluation metric is typically used for classification problems to measure the ratio of correctly predicted positive observations to the total predicted positives?**

> Scegli un'alternativa:

1.  Precision

2.  Accuracy

3.  F1 score

4.  Recall

<!-- -->

11) **Which one is a general-enough definition of ML?**

> Scegli un'alternativa:

1.  A field of study that exploits software and data to perform classification tasks

2.  A field of study that uses labels to train models so that they can perform predictions

3.  A field of study that enables computers to learn patterns from data

4.  A field of study that is based on neural networks to make predictions

<!-- -->

12) **What can happen if you select a too large value for the regularization parameter (lambda)?**

> Scegli un'alternativa:

1.  It will become ineffective to fight overfitting

2.  It may cause overfitting

3.  It may cause underfitting

4.  The training may become very quick but displaying an erratic behaviour

<!-- -->

13) **Which one of the following is a good example of a regression problem in ML, in the case of managing a blog online?**

> Scegli un'alternativa:

1.  Predict if a given reader will connect to the blog page everyday

2.  Predict the number of readers in a given time slot of the day

3.  Predict if users want more blog posts per week

4.  Predict if the number of readers will be higher or lower next month

<!-- -->

14) **Which of the following is true about Numpy?**

> Scegli un'alternativa:

1.  It is a third-party Python package that offers a variety of ML algorithms

2.  It is part of the Python core language, devoted to ML

3.  It is a third-party Python package that supports multi-dimensional array objects

4.  It is part of the Python core language, devoted to GPU-based training of ML models

<!-- -->

15) **If you need to make plots in your ML project in Python, which of the following is true?**

> Scegli un'alternativa:

1.  Not so many packages are available, the only choise would be Matplotlib

2.  Many python packages are available, an example is Matplotlib

3.  I could choose between NumPy and Matplotlib

4.  Many python packages are available, Seaborn is graphically the most basic one

<!-- -->

16) **A Google Colab runtime is?**

> Scegli un'alternativa:

1.  A physical environment available to any user via Jupyter, requiring only the network

2.  A virtual environment available to any user on Google Colab, with no time/usage restrictions

3.  A physical environment available to any user Jupyter, not requiring the network

4.  A virtual environment available to any user on Google Colab, with time/usage restrictions

<!-- -->

17) **Which method is used to transform categorical variables into numerical representations that can be used as input for ML algorithms?**

> Scegli un'alternativa:

1.  Standardization

2.  Min-Max Scaling

3.  One-Hot Encoding

4.  Normalization

<!-- -->

18) **Standardization transforms the data such that its distribution will have:**

> Scegli un'alternativa:

1.  Mean 1, standard deviation 1

2.  Mean 0, standard deviation 1

3.  Mean 0, standard deviation 0

4.  Mean 1, standard deviation 0

<!-- -->

19) **Which one of the following is a good example of a classification problem in ML, in the case of weather forecast:**

> Scegli un'alternativa:

1.  Tomorrow’s weather forecast, in terms of ‘probability of rain’

2.  Tomorrow’s weather forecast, in terms of ‘maximum humidity level’

3.  Tomorrow’s weather forecast, in terms of ‘the temperature at 15:00’

4.  Tomorrow’s weather forecast, in terms of ‘it will rain or not’

<!-- -->

20) **Which of the following does not fall under Feature Engineering?**

> Scegli un'alternativa:

1.  Feature Scaling (e.g Standardization and Normalization)

2.  Binning of continuous variables

3.  Feature Encoding (e.g One Hot Encoding)

4.  Removal of examples in the dataset due to missing/corrupted entries

<!-- -->

21) **Which of the following techniques does not help in reducing overfitting?**

> Scegli un'alternativa:

1.  Cross validation techniques

2.  GPU-enabled training techniques

3.  Dimensionality reduction techniques

4.  Regularization techniques

<!-- -->

22) **Which one of the following is a good example of a regression problem in ML, in the case of an e-commerce web site?**

> Scegli un'alternativa:

1.  Predict the number of users placing at least one order online in the next week

2.  Predict if a given item will go out of stock in the next week

3.  Predict if the number of user complaints will decrease or not within a month

4.  Predict if the income next week will be higher or lower than last week

<!-- -->

23) **If you need to perform descriptive statistics and make plots in your ML project in Python, which modules could you use?**

> Scegli un'alternativa:

1.  Matplotlib, or Seaborn, or similar

2.  Pandas, or NumPy, or similar

3.  Matplotlib is the only available option

4.  Pandas is the only available option

<!-- -->

24) **What is overfitting?**

> Scegli un'alternativa:

1.  When a predictive model is accurate but takes long time to run

2.  When you apply a powerful DL algorithm to a simple ML problem

3.  When the model learns specifics of training data but it’s unable to generalize

4.  When you perform hyperparameter tuning and performance degrades

---
> [[AML 67 - Data visualization|← Data visualization]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]]
