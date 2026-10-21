---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 4
tags: [note, aml]
---

> [[AML 03 - Univariate Model Regression|← Univariate Model Regression]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 05 - Univariate Model Regression · Gradient Descent Algorithm|Univariate Model Regression · Gradient Descent Algorithm →]]

# Minimization and Cost Function

To choose the parameters θ0 and θ1, our goal is to ensure that our predicted values, represented by h(x), closely match the actual values, denoted as y, in our training data.

This process allows us to effectively fit the best possible straight line to our dataset.

![[AML-image10.png|145]]![[AML-image11.jpg|378]]

We aim to minimize the difference between our predicted values and the actual values.

So, we're essentially solving a **<u>minimization problem</u>.**

**We aim to minimize the difference between our predicted values, h(x), and the actual values, y, for each example in our training set**. This involves adjusting the parameters θ0 and θ1 to reduce the gap between h(x) and y for each example in our training set.

| $\min_{\theta_{0},\theta_{1}}{J\left( \theta_{0},\theta_{1} \right)} = \min_{\theta_{0},\theta_{1}}\frac{1}{2m}\sum_{i = 1}^{m}\left( h_{\theta}\left( x^{(i)} \right) - y^{(i)} \right)^{2}$ |
|----|

- Squared differences = we measure the squared differences between h(x) and y for each example. This allows us to capture both the magnitude and direction of the differences, without concern for whether they're positive or negative.

- Average squared differences = we calculate the average of these squared differences across all examples in our training set. This gives us a measure of how well our model fits the data overall.

By **iteratively adjusting θ0 and θ1 to minimize the average squared differences,** we gradually improve the accuracy of our model in capturing the underlying relationship between the input and output variables.

The <u>**COST FUNCTION** *J*(*θ*0,*θ*1)</u> serves **as a** **measure** **of how well our hypothesis function** **hθ(x) fits the training data**. In the context of univariate linear regression, the cost function **<u>quantifies the difference</u> <u>between the predicted values h(x) and the actual values y for each example in our dataset.</u>**

The goal of the cost function is to capture the discrepancy between our predicted outcomes and the true outcomes, allowing us to assess the overall performance of our model.

By **<u>minimizing the cost function</u>** over the parameters θ0 and θ1, **<u>we effectively optimize our model to find</u> <u>the best-fitting straight line that describes the relationship between the input variable (x) and the output</u> <u>variable (y).</u>**

![[AML-image12.jpg|365]]In simpler terms, the cost function tells us how far off our predictions are from the actual values, and our objective is to minimize this difference to ensure that our model accurately captures the underlying patterns in the data.

- H is a function of x (given the θs) —\> The hypothesis function h(x) is determined by the parameters θ0 and θ1. It takes input values of x and produces predicted output values.

- J is a function of θs —\> The cost function J(θ0, θ1) measures the error between the predicted values h(x) and the actual values y for all examples in the training dataset.

- θs in the x-y “space”: When we visualize the parameters θ0 and θ1 in the x-y space, they represent different lines. They are the parameters of the function h. Each set of θs defines a unique straight line in the x-y plane, and each line represents a different hypothesis or model fit to the training data. Every couple of θs gives a different line.

- θs in the J “space”: In contrast, when we view the parameters θ0 and θ1 in the space of the cost function J, each couple of θs corresponds to a single point. This point represents the overall cost or error associated with that particular set of parameters.

- Minimization in the J Space: Our objective is to minimize the cost function J(θ0, θ1) by adjusting the parameters θ0 and θ1. We search for the set of θs that results in the lowest possible value of J, indicating the best fit of the hypothesis to the training data.

In summary, while each set of θs defines a line in the x-y space, it corresponds to a single point in the J space. By finding the set of θs that minimizes J, we determine the optimal parameters for our model, resulting in the best possible fit to the training dataset.

![[AML-image13.jpg|530]]

We take the squares of the errors because the squared error cost function is a practical and effective choice for most regression problems. While there are alternative cost functions that can yield satisfactory results, the square cost function is widely adopted and commonly used in regression tasks due to its simplicity, mathematical properties, and effectiveness in capturing the discrepancies between predicted and actual values in regression problems.

- Sensitivity to deviations: Squaring the errors emphasizes larger deviations between predicted and actual values. This can be beneficial for identifying and correcting significant discrepancies in the model's predictions.

- Mathematical properties: The squared error cost function is differentiable, which facilitates the use of optimization algorithms such as gradient descent for minimizing the cost. This makes it computationally efficient to optimize the model parameters.

- Statistical justification: Under certain assumptions, such as normally distributed errors with constant variance, minimizing the squared error corresponds to maximizing the likelihood of the observed data. This statistical justification lends further support to the use of the squared error cost function.

**<u>Simplified version</u>**

In the simplified version where the line passes through the origin and θ0 becomes equal to 0, our hypothesis <sub>simplifies to:</sub> *h*(*x*) = *θ*1\**x*

Here, θ1 is the parameter we want to minimize over, as it determines the slope of the line. We assume we have m = 3 examples in the training set.

To visualize how the cost function J varies with respect to θ1, we first compute the squared error for each example and then take the average over all examples.

The cost function J(θ1) can be expressed as the following and substituting the simplified hypothesis $h_{\theta}(x) = \theta_{1}x$, we get:

$$
\begin{array}{r}
 \\
J\left( \theta_{1} \right) = \frac{1}{2m}\sum_{i = 1}^{m}\left( h_{\theta}\left( x^{(i)} \right) - y^{(i)} \right)^{2} = \frac{1}{2m}\sum_{i = 1}^{m}\left( \theta_{1}x^{(i)} - y^{(i)} \right)^{2}
\end{array}
$$

Since we have m = 3 examples, we can compute J(θ1) for different values of θ1 and observe how it changes. We can plot J(θ1) against θ1 to visualize its shape and identify the minimum value of J, which corresponds to the optimal value of θ1 that minimizes the cost function.

This gives us insight into how well our model fits the training data and helps us fine-tune our parameter θ1 for better performance.

![](media/media/image131.jpg)

These examples provide insight into how different choices of the parameter θ1 impact the hypothesis and the resulting cost function in linear regression.

<u>Example: θ1 = 1</u>

This represents an ideal scenario where the hypothesis perfectly aligns with the data.

![[AML-image16.jpg|322]]The line defined by the hypothesis passes through the data points, resulting in a cost function value of 0. This indicates that the model perfectly predicts the observed data.

- Hypothesis: h(x) = x

- The hypothesis perfectly fits the data, resulting in a cost function J(1) = 0.

- Corresponding point in J space: (1, 0)

<u>Example: θ1 = 0.5</u>

![[AML-image17.jpg|301]]Here, the hypothesis underestimates the position of the points compared to the actual values. While the model is not as accurate as in the first example, it still provides a reasonable fit to the data.

However, the non-zero cost function value suggests that there are errors in the predictions, albeit not as severe as in other cases.

- Hypothesis: h(x) = 0.5 \* x

- The hypothesis underestimates the position of the points compared to the actual values, resulting in a non-zero cost function J(0.5).

- Corresponding point in J space: Higher than 0, indicating some error.

<u>Example: θ1 = 0</u>

This scenario demonstrates a significant underestimation of the data. The hypothesis predicts all values to be

![[AML-image18.jpg|312]]0, leading to a poor fit to the data. The high cost function value indicates a substantial discrepancy between the predicted and actual values, highlighting the inadequacy of the model.

- Hypothesis: h(x) = 0

- The hypothesis predicts all values to be 0, resulting in a significant underestimation of the actual values.

- Cost function J(0) likely indicates a high cost due to the substantial discrepancy between the predicted and actual values.

- Corresponding point in J space: Represents a high cost, highlighting the poor fit to the data.

**Evolution of the cost function in relation to the parameter θ1 in linear regression.**

As θ1 varies, the cost function forms a bowel-shaped curve. This shape is ideal because it indicates that there is **only one minimum point**, and this minimum is unique and reachable.

Specifically, when θ1 equals 1, the curve reaches its minimum, suggesting that this parameter value produces the best fit for the data.

In real-world scenarios, **linear regression involves optimizing both θ0 and θ1 simultaneously.**

This introduces an additional dimension, requiring a 3D space to represent the cost function.

Previously, with only one parameter θ1, the cost function was represented as a 2D surface.

With both θ0 and θ1, each point in the cost function's space corresponds to a line in the hypothesis space (X-Y space).

![[AML-image19.jpg|342]]This is because the combination of θ0 and θ1 defines the equation of the line. The objective is to find the combination of θ0 and θ1 that minimizes the cost function, leading to the best-fit line for the data. The contour plot represents the cost function J in the parameter space defined by θ0 (x-axis) and θ1 (yaxis). The contours on the plot indicate regions of equal cost (J), forming oval shapes.

In the first example, we assume that smaller houses are priced higher than larger houses, which contradicts common sense. When examining the contour plot of the cost function J, where oval shapes represent regions of equal cost, we observe that the hypothesis line associated with certain θ0 and θ1 values does not fit the data well. This suggests that the parameters are not optimized effectively, resulting in a poor fit of the hypothesis line to the data and a relatively high cost function J.

![[AML-image20.jpg|402]]

In the second example, all houses are priced the same regardless of their size. However, we notice a trend towards convergence to a central point on the contour plot. This implies that, on average, larger houses tend to command higher prices. As we move closer to the center of the plot, indicating larger house sizes, the prices increase accordingly.

![[AML-image21.jpg|427]]

In the third example, big houses cost more than small houses. In this case, the contour plot would likely show an upward trend, indicating that as house size increases, so does the price. This aligns with common intuition and reflects a more accurate fit of the hypothesis line to the data, resulting in a lower cost function J.

![[AML-image22.jpeg|366]]

---
> [[AML 03 - Univariate Model Regression|← Univariate Model Regression]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 05 - Univariate Model Regression · Gradient Descent Algorithm|Univariate Model Regression · Gradient Descent Algorithm →]]
