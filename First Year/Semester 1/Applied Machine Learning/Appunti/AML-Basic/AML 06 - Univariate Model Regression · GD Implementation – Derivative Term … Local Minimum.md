---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 6
tags: [note, aml]
---

> [[AML 05 - Univariate Model Regression · Gradient Descent Algorithm|← Univariate Model Regression · Gradient Descent Algorithm]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 07 - Univariate Model Regression · Applying GD to Linear Regression + Batch Gradient Descent (bgd)|Univariate Model Regression · Applying GD to Linear Regression + Batch Gradient Descent (bgd) →]]

# GD Implementation: Derivative Term

When we compute the **derivative**, we're essentially finding the **<u>slope of a curve</u>**. In gradient descent, this derivative term guides how we adjust our parameters:

- If the **derivative** shows a **positive slope**, the **update** to our parameters will be **<u>negative</u>**.

This happens because when we multiply the derivative term by the negative learning rate α, we get a negative value. So our parameters θ decrease, moving our model towards the left in parameter space, closer to the minimum of the cost function.

- If the **derivative** shows a **negative slope**, the **update** to our parameters will be **<u>positive</u>**.

This occurs because when we multiply the derivative term by the negative learning rate α, we get a positive value. So, our parameters θ increase, moving our model towards the right in parameter space, aiming to approach the minimum of the cost function.

![[AML-image27.jpg|342]]Regardless of our starting point in parameter space, gradient descent ensures our movement towards the cost function's minimum. The derivative term, multiplied by the negative learning rate α, determines the direction and magnitude of our parameter updates.

As we approach the minimum, the magnitude of the derivative decreases, leading to a gradual slowdown in parameter updates. This iterative process continues until the derivative becomes negligible (multiplied by - α), indicating our proximity to the cost function's minimum.

## 3.5 GD IMPLEMENTATION: LEARNING RATE

The learning rate can vary in magnitude:

- If too small = each iteration will result in minimal adjustments to the parameters. While this cautious approach may seem prudent, it can **significantly increase computational requirements**, necessitating a **large number of iterations** to converge to the minimum. This slow convergence can be computationally expensive and time-consuming.

- If too large, the parameter **updates** may be substantial, potentially **overshooting the minimum of the cost function**. In this scenario, the **algorithm may fail to converge or even diverg**e, leading to inaccurate results.

Finding the appropriate balance for the learning rate is crucial. It's often a matter of trial and error, as tuning alpha involves experimenting with different values to achieve optimal performance.

The **goal** is to **select** a **learning rate** that **minimizes the cost function efficiently, <u>requiring the fewest</u> <u>computational resources possible.</u>**

This optimization aims to strike a balance between convergence speed and computational efficiency, ultimately minimizing the cost associated with computational resources.

> ![[AML-image28.jpg|272]]

## 3.6 LOCAL MINIMUM

In the context of minimizing the cost function in machine learning, the primary goal is to find parameter values that result in the lowest possible cost, as this typically indicates a better fit of the model to the data. This **minimum point** represents an optimal solution for the model, as it reflects the **best compromise between capturing patterns in the data and avoiding overfitting.**

However, it's important to recognize that the cost function landscape can be complex, with multiple peaks and valleys. The global minimum, which is the absolute lowest point of the cost function, represents the best possible solution across all possible parameter values. Achieving this global minimum would indicate that the model is perfectly fit to the data and would perform optimally in all scenarios.

While reaching the global minimum sounds ideal, it's not always feasible or necessary in practice.

In many cases, the cost function landscape may have numerous local minima—points where the cost is lower than in the immediate surrounding area but not necessarily the lowest possible cost across all parameter values. These local minima can trap optimization algorithms like gradient descent, leading them to converge to suboptimal solutions.

Therefore, overly fixating on reaching the global minimum may not serve the broader goals of machine learning. Instead, the focus should be on finding a solution that strikes a balance between minimizing the cost function and achieving good generalization performance. This means obtaining a model that performs well not only on the training data but also on unseen data, demonstrating the ability to generalize patterns effectively.

Machine learning is not solely about minimizing the cost function; it's also about generalization.

Gradient descent, while effective, may converge to a local minimum rather than the global minimum. However, this is not necessarily a drawback.

**If the local minimum obtained** by gradient descent **yields satisfactory results** **that are relatively minimized and generalize well to unseen data, it can still be considered a successful outcome.**

In essence, while the focus is on minimizing the cost function, it's essential to keep in mind that machine learning is ultimately about achieving effective generalization, not just optimization. Therefore, reaching a local minimum that provides a good trade-off between minimization and generalization is often considered a desirable outcome in machine learning tasks.

> ![[AML-image29.jpg|550]]

The convergence of gradient descent (GD) with a fixed learning rate is contingent on various factors, including the choice of learning rate, the nature of the cost function, and the initial conditions of the optimization problem.

In principle, gradient descent can converge with a fixed learning rate if the learning rate is appropriately chosen and remains within a suitable range throughout the optimization process. However, finding the optimal fixed learning rate can be challenging and often requires empirical testing.

While it's true that in some cases, the derivatives naturally decrease as the optimization process approaches the minimum, relying solely on this phenomenon may not guarantee convergence. Additionally, the rate at which the derivatives decrease can vary depending on the characteristics of the cost function and the specific optimization problem.

The concept of changing the learning rate over time, known as learning rate scheduling or adaptive learning rates, offers a more flexible approach to optimization. By adjusting the learning rate dynamically based on the progress of the optimization process, adaptive learning rates can help overcome challenges associated with fixed learning rates, such as oscillations, slow convergence, or overshooting the minimum.

In summary, while gradient descent can theoretically converge with a fixed learning rate, the effectiveness of convergence depends on various factors. Experimentation with different learning rates, along with considering adaptive learning rate techniques, can help improve convergence and optimize the performance of the optimization algorithm.

![[AML-image30.jpg|697]]

**Summary**

Once we have made our hypothesis via the function h, we need to estimate the θs parameters.

For this task we introduced GD.

We graph the cost function J as a function of the θs estimates

Note we are not graphing x and y themselves, but the θ parameter range of our h function and the cost J resulting from selecting a particular set of parameters.

E.g. 2 parameters: we put θ0 on the x axis and θ1 on the y axis, with the cost function J on the vertical z axis. The points on our J graph will be the result of the cost function using our hypothesis h with those specific θ parameters.

GD gives you a protocol to follow:

- Take the derivative of the cost function

> The slope of the tangent is the derivative at that point, it gives us a direction to move towards on the next step

- Does it converge? Yes. Regardless of the slope's sign for the derivative, it eventually converges to the parameters’ minimum values

> The direction in which the step is taken is determined by the partial derivative of J; when the slope is negative, the value of a parameter increases and when it is positive, the value decreases

- At each iteration j, one should simultaneously update the parameters θj.

> Careful! Updating a specific parameter prior to calculating another one on the same iteration would yield to a wrong implementation of GD!

We make steps down the cost function in the direction with the steepest descent

The size of each step is determined by the parameter α, which is called the learning rate

We should adjust our parameter α to ensure that the GD algo converges in a reasonable time.

- a smaller/larger α would result in a smaller/larger step, respectively

- failure to converge or too much time to obtain the minimum value imply that our step size is wrong

We will know that we have succeeded when our cost function J is at the very bottom of the pits in the graph, i.e. when its value is the minimum.

How does GD converge with a fixed step size α? The derivative approaches 0 as we approach the bottom of our convex function. At the minimum, the derivative will always be 0 and thus no parameters update are done NOTE: depending on where one starts on the graph, one could end up at different points. This is a propriety of GD.

## Collegamenti
- [[MBD 14 - Module 5 – Multivariable Calculus and Optimisation]] — estremi, Hessiana, condizioni di ottimo

---
> [[AML 05 - Univariate Model Regression · Gradient Descent Algorithm|← Univariate Model Regression · Gradient Descent Algorithm]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 07 - Univariate Model Regression · Applying GD to Linear Regression + Batch Gradient Descent (bgd)|Univariate Model Regression · Applying GD to Linear Regression + Batch Gradient Descent (bgd) →]]
