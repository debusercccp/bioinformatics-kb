---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 8
tags: [note, aml]
---

> [[AML 07 - Univariate Model Regression · Applying GD to Linear Regression + Batch Gradient Descent (bgd)|← Univariate Model Regression · Applying GD to Linear Regression + Batch Gradient Descent (bgd)]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 09 - Polynomial Regression|Polynomial Regression →]]

# Multivariate Model Regression

Multivariate linear regression extends the concept of univariate linear regression by incorporating multiple features (variables) to predict an outcome. This approach allows for a more comprehensive analysis, considering the potential influence of multiple factors on the target variable.

When transitioning from univariate to multivariate regression, the fundamental difference lies in the inclusion of multiple features.

While univariate regression focuses on predicting outcomes based on a single feature, multivariate regression considers the interplay between multiple features in predicting the target variable.

In multivariate regression, the features can vary in complexity and type. They can include numerical values, categorical variables, squares of existing features, or transformations of the original data.

This flexibility allows for a more nuanced understanding of the relationships between features and the target variable.

> ![[AML-image38.jpg|541]]

**NOTATION AND TERMINOLOGY:**

In multivariate linear regression, we deal multiple features represented by *xij*, where:

- *i* represents the example number (ranges from 1 to the number of examples m)

- *j* represents the feature index and (ranges from 1 to the number of features n)

- *x<sup>i</sup>* denotes the input feature vector of the training example i, containing all the features for that example.

- *x<sub>j</sub>*<sup>(*i*)</sup> represents the value of the j-th feature in the i-th training example.

> ![[AML-image39.jpg|444]]

## 4.1 HYPOTHESIS

![[AML-image40.png|311]]In multivariate linear regression, the hypothesis function expands to include more parameters specifically *n* + 1 terms to account for each feature and the intercept term. Despite this expansion, the hypothesis remains linear in all dimensions, representing a linear combination of features with their respective parameters. The initial presence of the *θ*0**, representing the intercept term, can sometimes be inconvenient.**

To address this, we introduce the ***“zero feature”***.

This entails augmenting our feature set with an additional column consisting solely of 1s, denoted as *<sup>x</sup>*<sub>0</sub><sup>(*i*)</sup>.

This column vector remains constant across all examples and serves to ensure that each feature *x* is consistently multiplied by its corresponding parameter *θ*.

![[AML-image41.jpg|388]]Once we incorporate the zero feature, we achieve consistency in the dimensions of our column vector X (the feature vector) and parameter vectors. This alignment facilitates the process of vectorization across our hypothesis function for individual training examples.

Vectorization involves representing our **hypothesis function** as the **product of a parameter vector and a feature vector**, allowing for more efficient computation and handling of multiple features.

We transition to a vectorized form to represent parameters and features compactly.

- The <u>f**eature vector** *x*</u> contains all feature values for a given example, organized as a column vector.

- The parameters vector *θ* is linearly transposed to become a row vector.

By vectorizing parameters and features, we can perform operations efficiently and compactly, facilitating computations in multivariate regression.

![[AML-image42.jpg|288]]The use of vectors allows for a concise and efficient representation of the hypothesis function and parameter updates. The compactness of vectorized notation simplifies calculations and enhances clarity in expressing multivariate linear regression algorithms.

When extending to multivariate regression, the hypothesis function follows the same principle of vectorization. It is represented as the product of the transpose of the parameter vector *θ* and the feature vector *x*, resulting in a scalar value. However, in multivariate regression, the feature vector *x* now consists of multiple features, and the parameter vector *θ* includes terms for each feature and the intercept term.

Despite these additions, the vectorization process remains unchanged, providing a compact and efficient representation of the hypothesis function.

## 4.2 GRADIENT DESCENT ALGORITHM

The Gradient Descent algorithm for multivariate regression involves iterating to update parameters based on the partial derivatives of the cost function. This process accounts for all features and results in optimized parameter values for the regression model.

In multivariate regression, the hypothesis function is represented as the product of a parameter vector and a feature vector. This results in a scalar value, signifying the predicted output. The parameters now include n+1 terms to account for each feature and the intercept term.

The cost function J is defined as the average of the squared differences between the predicted values (hypothesis) and the true values for each example. Unlike univariate regression, J **now depends on all the features.** Although the notation for *h*(*θ*) remains similar, it now represents the product of vectorized hypotheses.

![](media/media/image366.png)

In the Gradient Descent algorithm for multivariate regression, iterations are performed to update the parameters *θ*. Each iteration involves updating all parameters, indexed from 0 to n, as J depends on all the features. The parameter update is determined by subtracting the product of the learning rate *α* and the partial derivative of the cost function with respect to the corresponding parameter.

When computing the partial derivative of J, the expression varies based on the number of features n.

- For *n* = 1 (univariate regression), the derivative is calculated separately for each parameter ( *θ*0 and *θ*1).

- For *n* \> 1 (multivariate regression), a generic form is employed to encompass all

> This formulation incorporates the features accordingly, with *x*0 = 1 or the intercept term.
>
> ![[AML-image45.png|373]]

**4.3 FEATURE SCALING & MEAN NORMALIZATION**

FEATURE SCALING

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><p>Feature scaling is a crucial step in data pre-processing for machine learning algorithms, particularly Gradient Descent (GD), to ensure optimal performance. It involves <strong>standardizing the scale of different features within a dataset,</strong> ensuring that they all fall within a similar range of values.</p>
<p>This standardization is essential, as features with disparate scales can introduce bias into the learning process and adversely affect the convergence speed of GD.</p>
<p><img src="_attachments/AML-image46.jpg" width="300">Consider a scenario where GD is navigating through a cost function with a skewed, elliptical shape. Depending on the initial starting point and the varying scales of features, GD may take significantly longer to converge to the minimum. This disparity in convergence time arises due to features taking on different ranges of values.</p>
<p>To mitigate this issue and ensure consistent convergence rates, it is imperative to scale all features to a similar range.</p>
<p>By adopting feature scaling, we enhance the robustness and effectiveness of GD in optimizing model parameters, ultimately leading to improved model performance and faster convergence times. This preprocessing step underscores the importance of presenting data in a well-prepared format to maximize the learning potential of machine learning algorithms.</p>
<p>In previous example, we ended up with both features between 0 and 1, however more generally, in feature scaling, we often want to get every feature into “approximately” a [-1,+1] range.</p>
<p>(Remember: your feature x0 is always equal to 1, so that's already in that range)</p>
<ul>
<li><p>features in [0,3] or [-3,+3] or [-2,0.5]? maybe not. You are still close enough and no scaling is probably needed</p></li>
<li><p>features in [-100,+100]? yes. You might benefit from rescaling</p></li>
<li><p>features in [-0.0001,+0.0001]? yes. This is within [-1,1] but their relative difference might still be large, so you may benefit from rescaling.</p></li>
</ul>
<p>It is not the absolute value that matters, but more the proximity to a [-1,+1] range and - most important - the similarity of possible ranges of values across different features This ensures that no single feature dominates the learning process due to differences in scale. By having similar ranges across features, each feature can contribute more equally to the model's predictions, leading to more balanced and effective learning. Essentially, it highlights the need for feature scaling to maintain consistency and fairness in the contribution of each feature to the overall model performance. <em>x</em>scaled = <em>x</em>(−<em>x</em>)min− min(<em>x</em>)(<em>x</em>) × 2 − 1 max</p>
<p>Where:</p>
<ul>
<li><p><em>x</em> = original feature value</p></li>
<li><p>min(<em>x</em>) = the minimum value of the feature.</p></li>
</ul>
<p>-max(<em>x</em>) = the maximum value of the feature.</p>
<ul>
<li><p><em>x</em><sub>scaled</sub> = denotes the scaled feature values in the range [-1, +1].</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

MEAN NORMALIZATION

![](media/media/image48.jpeg)

![](media/media/image368.png)

## 4.4 LEARNING RATE

![[AML-image51.png|310]]The learning rate α is a crucial hyper-parameter in the iterative process of Gradient Descent (GD) which determines the size of the steps taken towards the minimum of the cost function J(θ).

The update rule for GD involves simultaneously updating all parameters θ from θ0 to θn using the formula specified. When implementing GD in code, choosing an appropriate learning rate is essential for ensuring the algorithm converges effectively.

![[AML-image52.png|337]]Observing the behavior of the cost function J(θ) over iterations is a common method to verify the correctness of GD. **Plotting J(θ) against the number of iterations** offers valuable insights into the algorithm's progress. Ideally, J(θ) should exhibit a decreasing trend as GD iterates, indicating movement towards the optimal solution. Convergence behavior may vary across applications, and the stabilization time can differ significantly. The rate at which J(θ) decreases after each iteration depends on the learning rate α. In

scenarios like linear regression, a small α ensures consistent reduction in J(θ) with each iteration, as mathematically proven under specific assumptions about the cost function J.

While visualizing J(θ) against iterations provides a helpful overview of GD's performance, implementing automatic convergence tests is also feasible. These tests determine if GD has sufficiently converged, typically by setting a threshold for J(θ) decrease. However, selecting an appropriate threshold can be challenging and may not always yield reliable results. Therefore, manual inspection of J(θ) plots remains a valuable practice for nuanced convergence assessment.

This **automatic test typically involves setting a threshold value**, such as **10**<sup>-**3**</sup>, and **declaring c<u>onvergence if</u> <u>the cost function J(θ) decreases by less than this threshold in a single iteration.</u>**

While this approach offers automation, selecting an appropriate threshold can be challenging. Consequently, relying solely on automatic convergence tests may not always be reliable.

In practice, **manually inspecting the plot of J(θ) versus the number of iterations may be more effective**: while automatic convergence tests offer convenience, they may benefit from human oversight to ensure accurate convergence detection.

Moreover, considering automatic stopping criteria prompts the question: why not stop automatically when there is no change in the slope? While this method seems intuitive, aggressive descent with a high learning rate α can lead to oscillations. Starting with a slow learning rate and gradually increasing it is often more effective. Incrementing the learning rate slightly if progress seems too slow is a practical strategy.

The decision to automatically stop training if parameters are not updated requires careful consideration.

Although it may seem logical, training may continue due to plateaus in the cost function surface.

Thus, starting slowly and incrementing the learning rate gradually is advisable.

**Experimenting with factors of 10, ranging from 10<sup>-n</sup> to 1, can help identify an optimal learning rate.** Additionally, choosing an appropriate learning rate α is crucial for GD convergence. If J(θ) fails to decrease on every iteration, α may be too large, leading to non-convergence. Conversely, setting α too small can result in slow convergence. Therefore, experimenting with factors of 10 or 3 can aid in finding the optimal learning rate.

## Collegamenti
- [[MBD 06 - Module 2 – Matrices and Linear Systems · Definitions and special types + Operations – how they are performed]] — notazione matriciale delle feature
- [[MBD 09 - Module 2 – Matrices and Linear Systems · Linear systems Ax=b]] — minimi quadrati

---
> [[AML 07 - Univariate Model Regression · Applying GD to Linear Regression + Batch Gradient Descent (bgd)|← Univariate Model Regression · Applying GD to Linear Regression + Batch Gradient Descent (bgd)]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 09 - Polynomial Regression|Polynomial Regression →]]
