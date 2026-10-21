---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 16
tags: [note, aml]
---

> [[AML 15 - Multiclass Classification|← Multiclass Classification]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 17 - Regularisation|Regularisation →]]

# Alternatives to GD

We explored Gradient Descent (GD) as a method for minimizing the cost function *J*(*θ*) in logistic regression. However, there are alternative optimization concepts and algorithms that are more optimized than the basic GD approach.

These alternative methods offer the potential to accelerate logistic regression, potentially outpacing the speed achieved with GD. Moreover, they may enhance the scalability of the algorithm, particularly when dealing with vast datasets and machine learning problems featuring numerous features.

*These optimization algorithms offer different approaches to achieving the same goal of minimizing the cost function J*(*θ*) *and computing its derivatives. While they provide more sophisticated options, each comes with its own set of advantages and drawbacks. Although delving into these algorithms may require extensive study, particularly in advanced numerical computing courses, this course will not delve into their intricacies. Many experts have successfully utilized these algorithms for years before fully comprehending their inner workings, emphasizing that one can effectively apply them to various learning problems without a deep understanding of their complexities.*

**CONJUGATE GRADIENT**

Conjugate Gradient is an iterative algorithm based on search directions that minimizes the cost function without the need for a learning rate hyperparameter.

Gradient Descent works by iteratively moving in the direction of the negative gradient of the cost function, which helps to find the minimum point of the function. Essentially, it follows the slope of the function downhill until it reaches the minimum.

Conjugate Gradient uses a different approach to determine the direction of each step: the search directions are specified in a way that they are orthogonal to each other, which is a key difference compared to GD.

**BFGS**

The BFGS algorithm, which stands for Broyden–Fletcher–Goldfarb–Shanno, is a method used for solving optimization problems, particularly in scenarios where traditional Newton-Raphson methods are not feasible. Newton-Raphson methods typically require the calculation of the Jacobian or Hessian matrices at each iteration. However, in many cases, these matrices may either be unavailable or too complex to compute efficiently.

In such situations, the BFGS algorithm provides an effective alternative. It is an iterative optimization technique that does not rely on explicit computation of the Jacobian or Hessian matrices. Instead, it updates an approximation of the inverse Hessian matrix as it iterates towards the optimal solution. This makes it suitable for a wide range of non-linear optimization problems where traditional methods may not be practical.

#### L-BFGS 

The L-BFGS algorithm, where "L" stands for "limited-memory," is a variant of the BFGS (Broyden–Fletcher– Goldfarb–Shanno) algorithm.

In traditional BFGS, the algorithm maintains an approximation of the inverse Hessian matrix, which can become computationally expensive when dealing with problems that involve a large number of variables. LBFGS addresses this issue by using limited memory, meaning it stores only a few vectors from previous iterations instead of the full Hessian matrix.

This limited-memory approach significantly reduces the memory requirements of the algorithm, making it particularly well-suited for optimization problems with a large number of variables, typically in the thousands or more. Despite its reduced memory usage, L-BFGS remains highly efficient and effective in finding optimal solutions for a wide range of optimization problems.

## 9.1 GD VERSUS NOT-GD

The **non-gradient descent** algorithms offer several **<u>advantages</u>** over GD:

- **Automatic learning rate selection** = These algorithms typically eliminate the need for manually selecting a learning rate *α*. Instead, they employ a line search algorithm that dynamically adjusts and selects the learning rate for each iteration, optimizing performance.

- **Faster convergence**: Implementation choices and optimization strategies often lead to faster convergence compared to GD, making them more efficient for large-scale problems.

- **Automatic optimization**: The line search algorithm intelligently explores various learning rates, enhancing optimization performance without manual intervention.

However, they also come with certain **<u>disadvantages</u>**:

- **Complexity:** Non-GD algorithms such as conjugate gradient, L-BFGS, and BFGS are considerably more complex than GD. Implementing these algorithms requires expertise in numerical computing, and manual implementation is not recommended.

- **Debugging challenges**: The sophisticated nature of these algorithms can make debugging more challenging, particularly when using optimization libraries. Debugging becomes more complex due to the opaque nature of these algorithms.

- **Dependency on optimization libraries:** While software libraries exist for implementing these algorithms, not all languages or libraries may support every algorithm. Additionally, the quality of the algorithm implementation in the chosen library is crucial for optimal performance.

In summary, while non-GD algorithms offer advantages in terms of automatic learning rate selection and faster convergence, they also introduce complexity and debugging challenges. Using optimization libraries can streamline implementation but requires careful consideration of language and library choices.

To utilize these algorithms effectively, it is advisable to leverage existing software libraries rather than attempting to implement them from scratch. Similar to how one wouldn't write their own code for basic mathematical operations like computing square roots or matrix inversions, relying on established libraries for non-gradient descent algorithms is recommended. However, there are some considerations:

- **Availability in different tools =** Not all algorithms may be available in every programming language or tool. Therefore, it's essential to explore multiple libraries to find one that offers the desired algorithm implementations.

- **Quality of algorithm implementation =** The effectiveness of the algorithms can vary based on the quality of their implementation in the library of choice. It's crucial to ensure that the selected library provides wellimplemented and efficient versions of the algorithms.

When selecting a library:

- Experiment with different libraries: If your ML application is developed in a specific programming language, consider trying out various libraries to identify the one that offers the best implementations of the algorithms you require.

- Stay updated: Newer versions of libraries may introduce improvements or additional features. Stay informed about updates and assess whether newer versions offer enhancements that align with your needs.

In summary, the choice of tools significantly influences applied ML practices. While gradient descent and its variations suffice for many ML applications in the Python ecosystem, exploring and utilizing different libraries can provide access to advanced optimization algorithms when necessary.

---
> [[AML 15 - Multiclass Classification|← Multiclass Classification]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 17 - Regularisation|Regularisation →]]
