---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 12
tags: [note, aml]
---

> [[AML 11 - Logistic Regression|← Logistic Regression]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 13 - Logistic Regression · Cost Function|Logistic Regression · Cost Function →]]

# Decision Boundary

In logistic regression, our objective shifts from predicting numerical values to making classifications. Instead of estimating a continuous output, we're now interested in predicting discrete classes.

The ***decision boundary*** is a critical concept in logistic regression that **<u>defines the separation between</u> <u>different classes in the feature space</u>**. In many real-world scenarios, especially in higher-dimensional spaces, there exists a boundary that divides the instances into different regions.

If an instance lies on one side of this boundary, it's assigned to one class, and if it lies on the other side, it's assigned to a different class. The decision boundary essentially delineates where one class ends and another begins. There are 2 types:

- Linear decision boundary

- Non-linear decision boundary

LINEAR DECISION BOUNDARY

Imagine you have a 2D space where each axis represents a different feature. In this space, you've plotted

- blue circles to represent negative examples

- red crosses for positive examples

Visually, you can see that these two classes can be separated by a line. When we mention "putting a line between the 2 groups of data", it means drawing a line (the decision boundary) that effectively separates the instances belonging to class 0 from those belonging to class 1 in our dataset. This process is essentially what logistic regression aims to achieve: creating a model that accurately distinguishes between different classes based on the input features.

![[AML-image71.jpg|697]]

1.  **Hypothesis Formation**

In logistic regression, the hypothesis represents our model's prediction of the probability that a given input example belongs to a particular class.

**To establish a classification boundary**, we **first construct a <u>hypothesis that incorporates all the features</u> <u>available in our dataset.</u>**

In this example we have a dataset with two features, so the hypothesis would involve multiplying each feature by its corresponding theta parameter. For instance, if we have features x1 and x2, our initial hypothesis might look something like this: *h*(*x*) = *θ*<sub>0</sub> + *θ*<sub>1</sub>*x*<sub>1</sub> + *θ*<sub>2</sub>*x*<sub>2</sub>

Here *θ*0,*θ*1, and *θ*2 are the parameters (also called coefficients) that we need to learn from the training data.

However, since this is a classification task, not regression, we apply a sigmoid function to the linear hypothesis to obtain our classification hypothesis.

2.  **Parameter Vector Example**

Suppose that after training our logistic regression model, we obtain a parameter vector that defines our hypothesis. This vector might look like −3 ⋅ *θ*<sub>0</sub> + 1 ⋅ *θ*<sub>1</sub> + 1 ⋅ *θ*<sub>2</sub> where θ₀, θ₁, and θ₂ are the learned parameters.

If −3 + *x*<sub>1</sub> + *x*<sub>2</sub>:

• ≥ 0 —\> we classify the input example into one class (e.g., positive examples) • \< 0 —\> we classify it into the other class (e.g., negative examples) This process effectively partitions the feature space into distinct regions.

One side of the partition corresponds to one class, while the other side corresponds to the other class. In essence, the parameter vector determines the orientation and position of the decision boundary that separates the different classes in the feature space.

**3**. **Decision** **Boundary**

The line that separates these regions is called the decision boundary and in this example it's represented by the equation −3 + *x*<sub>1</sub> + *x*<sub>2</sub> = 0

The decision boundary separates the regions where we predict y = 1 from those where we predict y = 0 in the feature space. In a 2D space, the decision boundary is often visualized as a line, while with more features, it becomes a higher-dimensional surface, dividing the space into distinct regions.

The decision boundary is a property of the hypothesis and the parameter values, not the training data itself. The **decision boundary's characteristics**, such as its shape and position, are not determined by individual data points in the training set. Instead, they are a **consequence of how the hypothesis function and parameter values interact with the input features.**

During the training process, the algorithm adjusts the parameters *θ* to optimize the fit between the model's predictions and the actual outcomes in the training data.

As a result, the learned parameter values define the decision boundary in the feature space.

This boundary serves as the threshold that separates regions where the model predicts different classes.

It's important to note that even though the decision boundary is influenced by the training data indirectly through the parameter learning process, it remains consistent in its type (e.g., a line) as long as the underlying hypothesis function remains unchanged. This consistency ensures that the model's classification behavior is stable and reliable across different datasets, promoting its generalization to new, unseen data.

Recap

- Training set influence: The training set is instrumental in determining the parameters *θ* through the training process. These parameters are adjusted to best fit the data. However, it's crucial to understand that while the data influences the parameter values, it's ultimately our decision to define the decision boundary, whether it's linear or otherwise.

- Hypothesis and decision boundary: Once we've derived the parameters *θ* for our hypothesis, it's the hypothesis itself that dictates the nature of the decision boundary. The decision boundary is a direct consequence of the hypothesis function and its associated parameters.

- Independence from training data remarkably: we don't need to visualize the training set explicitly to ascertain the decision boundary. Instead, we can analyze our hypothesis to understand its implications for the decision boundary. This means that the decision boundary, as defined by the hypothesis, applies not only to the training data but also to other datasets.

In essence, the relationship between the hypothesis, parameters, and decision boundary highlights the internal logic and consistency of logistic regression. This understanding allows us to generalize the model's classification behavior beyond the training data, ensuring its applicability to new datasets.

> ![[AML-image72.jpg|565]]

#### NON LINEAR DECISION BOUNDARY

![[AML-image73.jpg|183]]In scenarios where a linear decision boundary is insufficient to separate the data effectively, we turn to non linear decision boundaries. One approach is to leverage polynomial regression techniques within logistic regression to create more complex decision boundaries.

Consider a two-dimensional feature space with features *x*1and *x*2, where the data distribution doesn't neatly align with a linear boundary. Attempting to separate the data with a linear boundary would likely lead to poor classification results.

To address this limitation, we **extend our hypothesis to include polynomial**

**terms** of the original features. For instance, we can introduce new features *x*3 = *x*1<sup>2</sup> and *x*4 = *x*2<sup>2</sup> effectively capturing quadratic relationships between the features. Our hypothesis now includes terms such as *x*1<sup>2</sup> and *x*2<sup>2</sup> alongside the original features. Suppose, after training, our parameter vector yields values such as:

- *θ*<sub>0</sub> = − 1

- *x*<sub>1</sub> = 0

- *x*<sub>2</sub> = 0

- *x*<sub>1</sub><sup>2</sup> = 1

- *x*<sub>2</sub><sup>2</sup> = 1

This implies that our decision boundary equation would be:

−1 + *x*<sub>1</sub><sup>2</sup> + *x*<sub>2</sub><sup>2</sup> ≥ 0 to predict class 1

−1 + *x*<sub>1</sub><sup>2</sup> + *x*<sub>2</sub><sup>2</sup> \< 0 to predict class 0

> ![[AML-image74.jpg|493]]

Graphically, this decision boundary forms a **circular boundary** in the feature space rather than a straight line. Despite its nonlinear nature, this circular boundary effectively separates the classes, as evidenced by the green line in the illustration.

In summary, by introducing polynomial terms into our logistic regression hypothesis, we can create nonlinear decision boundaries that better capture the complexities of the underlying data distribution, thus improving classification performance.

In both scenarios presented, the data points are visualized within a two-dimensional feature space, where the decision boundary, depicted as the green line and green circle, serves to separate the red and blue data points. On the right side, we have the corresponding hypotheses or decision boundaries represented algebraically.

Interestingly, the decision boundaries, whether linear or nonlinear, are primarily determined by the hypotheses rather than the specific data points. Essentially, the data points inform the parameter values of the hypothesis, influencing the precise location and orientation of the decision boundary. However, the nature of the hypothesis itself dictates the form of the decision boundary.

Therefore, we can consider these hypotheses independently of the data points, focusing instead on how they define the decision boundary. The choice of algorithm and the complexity of the hypothesis significantly impact our ability to construct a decision boundary that effectively separates the data points based on their classes. As we increase the complexity of our approach during training, we gain more flexibility in designing decision boundaries that align better with the underlying data distribution.

> ![[AML-image75.jpg|439]]

![[AML-image76.jpg|446]]

## Collegamenti
- [[MBD 05 - Module 1 – Vectors and Hyperplanes · Hyperplanes and linear classification]] — iperpiani e decision boundary lineare

---
> [[AML 11 - Logistic Regression|← Logistic Regression]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 13 - Logistic Regression · Cost Function|Logistic Regression · Cost Function →]]
