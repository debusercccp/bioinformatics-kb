---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 2
tags: [note, aml]
---

> [[AML 01 - Definition of Machine Learning|← Definition of Machine Learning]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 03 - Univariate Model Regression|Univariate Model Regression →]]

# Types of Machine Learning

According to traditional classification, the 3 most populated classes of learning algorithms are:

- ***Supervised*** learning: **teach the machine how to** do something —\> the learning happens with you r supervision, you assist the learning process as a human

- ***Unsupervised*** learning: l**et the machine learn by itself** what to do —\> there are algorithms that extract info from data without you saying information of the data

- ***Reinforcement*** learning: make the machine **learn by feedback** —\> you learn by giving the machine some feedback after execution, you give a penalty or a reward.

## 2.1 SUPERVISED ML

Example: we want to predict housing prices in an area, it’s a good example of a ML project that starts from a need. You have your house to sell, you have area data, you have a clear goal.

- A learning algorithm could fit a straight line to the data and give you a predicted sell value (The larger the size of houses, the higher their price will be. This relationship can be represented by a straightforward line, making it easy to predict.)

- A better learning algorithm could find better ways: a second-order polynomial fit to this same data?

Both are “***supervised***” learning algorithms: we gave the algorithms a dataset (e.g. location, size, .. and prices) in which the "right answers" (prices) were included.

This is a “***<u>regression</u>***” problem example: we are trying to **<u>predict a continuous value output</u>** (a price).

The line serves as an approximation because it represents a simplified model of the relationship between house characteristics and price. However, it may not capture all the nuances of the houses' features.

Both scenarios can be considered supervised learning because they **involve using a dataset of known house characteristics and prices to train the machine learning model**.

With this trained model, it becomes possible to predict the price of a new house based on its characteristics, even though it wasn't explicitly mentioned before.

### *Example* *1: houses* 

In this scenario, we're dealing with supervised machine learning regression tasks where we have a dataset of houses represented as red crosses on a plot:

- X-axis represents the size of houses in square meters

- Y-axis represents the price of the houses in 1000 euros

We're considering two hypotheses for modeling the relationship between house size and price:

- a linear model (depicted in pink)

- polynomial model (depicted in blue)

Both models aim to predict the price of a house given its size.

When we encounter a new house with a size of 125 square meters, each model will provide a different prediction for the price. This variation in predictions arises from the different assumptions and complexities of each model.

Ultimately, these examples illustrate the essence of supervised machine learning regression, where the models learn from labeled training data to make predictions (in this case, predicting house prices) based on input features (in this case, house size).

The output of these regression models is a numerical value representing the predicted price of the house.

> ![[AML-image3.jpg|335]]

### *Example 2: tumor* 

Consider a dataset containing information about tumors, where the only available characteristic is the size. This is not a regression problem, since we're not seeking a numerical prediction.

Instead, the objective is to classify tumors as either malignant or benign. This represents a ***binary classification problem*** (0 or 1, benign or malignant) within the realm of supervised learning. Each patient's data in the dataset is labeled, facilitating the distinction between malignant and benign tumors.

The goal is to try to predict if a given breast cancer is malignant or benign: given an additional new patient with a tumor of a given size, can ML use the available data to estimate what is the probability that this tumor is malignant versus benign?

This scenario remains under supervised learning because we have labeled data: for instance, "Patient 1" is labeled as "malignant" and "Patient 2" as "benign."

Our objective here is binary classification, meaning we aim to categorize tumors as either malignant or benign. Comparing this to the house example, where we only have the size on one axis, here we are dealing with tumor data and considering the likelihood of malignancy as tumor size increases.

We observe that larger tumors tend to be associated with a higher probability of malignancy.

In our plot, we notice that the f<u>requency of red crosses (representing malignant tumors) is higher as tumor</u> <u>size increases</u>. However, <u>there isn't a specific size threshold that definitively separates benign from malignant</u> <u>tumors.</u>

![](media/media/image32.jpg)

If we now **include additional characteristics** such as the age of the patients along with tumor size, the data distribution may become more complex. In a two-dimensional plot, it might not be feasible to separate the two groups (malignant and benign tumors) with a simple straight line.

Instead, the **division between the two groups might require a curved boundary or surface**.

When we have more characteristics (**features)** available, we can **represent** them as **additional dimensions in our dataset**. As the dimensionality of the dataset increases, the potential complexity of the boundary or surface that separates the two groups also increases.

This means that in higher-dimensional space, we may be able to find a more intricate shape or boundary that effectively separates the different classes of data points.

Machine learning algorithms can **utilize all available data parameters (features) to make prediction**s. As we include more diverse and informative features (such as tumor thickness, cell size uniformity, cell shape uniformity, etc.), the algorithm can learn to leverage these features to make more accurate predictions about tumor malignancy.

In essence, by expanding the dataset to include a larger, more diverse set of characteristics, machine learning algorithms can better discern patterns and relationships within the data, leading to more accurate predictions. This is advantageous because with a well-trained model, we can predict the diagnosis of new patients based solely on their available characteristics.

*Take-away message*

In **supervised ML**, we have a dataset, plus some idea that there must be a relationship between the input(s) and the output. And we already know what our correct output should be.

Supervised ML problems can be categorized into “**regression**" (**how many**) and “**classification**" (**whether**) problems.

- In a ***regression*** problem, we are trying to predict results within a **continuous output** —\> trying to map input variables to some continuous function

- In a ***classification*** problem, we are instead trying to predict results among a **discrete output** set

—\>trying to map input variables to some discrete categories

CYU

You are running a company and you want to develop learning algos to address these 2 problems.

1.  you have a large inventory of items to sell. You want to predict how many of a type you will sell in the next 6 months.

2.  you have plenty of users/customers. You want software to examine each individual customer's accounts on your commerce web site, to decide whether or not the account has been hacked. Should they be treated as classification or regression problems?

- treat both as classification

- treat 1 as classification, treat 2 as regression

- treat 1 as regression, treat 2 as classification

- treat both as regression

Problem 1 —\> thousands of integers and need to predict a number

Problem 2 —\> 0 (non hacked) or 1 (hacked)

## 2.2 UNSUPERVISED ML

In unsupervised machine learning, the algorithm works without labeled data: it is tasked with f**inding patterns in the data without being told what they are**. For example, a clustering algorithm might group data points into clusters without knowing what each cluster represents.

An unsupervised ML algorithm may **discern that the data naturally segregates into distinct groups or clusters**. Such algorithms are often referred to as "**c*lustering algorithms***”.

For instance, consider the aggregation of news articles into cohesive story categories online, as seen in platforms like Google News. These categories are generated automatically by clustering algorithms, which identify common themes or topics within the articles and group them accordingly, even in the absence of explicit labels or instructions.

We are not given any label here, by construction (“**unlabelled data**”).

We know nothing about these people ( age, gender, ethnic group, pre-existing conditions).

We can think of running a clustering algorithm and -based on this data- to group individuals into different categories.

*(NOTE: a-priori a data scientist does not know what each category might mean)*

![[AML-image6.jpg|358]]This algorithm doesn't understand anything about animals; it only knows the features of the data. It groups data points without overlapping, which can include very similar (like dogs and cats) or very different (like snakes) items. Clustering is like sorting items into containers without knowing what's inside each container.

For example, in an image of a cat, labeling it as a cat requires human input. If you have billions of images that might or might not contain a cat, who decides if it's a cat? Usually, underpaid humans are tasked with labeling these images. The same concept applies to CAPTCHA tasks where humans label things to train algorithms.

**We can run algos to use this data (that we are given) to group people (that we know nothing about) into groups (that were not a-priori defined by us).**

Everything is decided by just data and algos. This is **unsupervised ML**, some examples:

- **Organize large computer clusters:** trying to figure out which machines tend to “work together”: if set-up takes this into account, the data centre works more efficiently.

- **Social network clustering:** Given knowledge about which friends you message the most, or given your \<pick-your-social\> connections, try to automatically identify which are cohesive groups of people who know each other (or may want to connect).

- **Market segmentation:** Analyse huge DBs of customers’ info and try to automatically group customers into different market segments, to target advertisement, offers, etc.

- **Physics/Astronomy data analysis**: Clustering algos might give insight into possible logical grouping of previously disconnected data.

**Unsupervised learning can be applied not only to clustering.**

The cocktail party problem falls under the broad category of signal processing challenges. In this problem, multiple sound sources are recorded simultaneously, creating a chaotic mixture of signals.

The goal here is to extract meaningful structure from this cacophony without prior knowledge or labels. This task exemplifies unsupervised learning but not clustering specifically.

It’s indeed an unsupervised (non-clustering) learning problem where the goal is to find structure in a chaotic environment.

**<u>Summary</u>**

**Unsupervised ML** allows to approach problems with little or no idea about what results should look like. We *derive structure from data*, we do not necessarily know the effect of the variables, there is no feedback based on the prediction results.

We can derive this structure by *clustering* algos (i.e. grouping the data based on relationships among its variables) or *non-clustering* algos (i.e. find structure in chaotic environment).

---
> [[AML 01 - Definition of Machine Learning|← Definition of Machine Learning]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 03 - Univariate Model Regression|Univariate Model Regression →]]
