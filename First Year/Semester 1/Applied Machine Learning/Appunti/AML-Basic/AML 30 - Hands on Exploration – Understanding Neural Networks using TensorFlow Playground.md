---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 30
tags: [note, aml]
---

> [[AML 29 - Neural Networks|← Neural Networks]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 31 - NNs-representation|NNs-representation →]]

# Hands on Exploration: Understanding Neural Networks using TensorFlow Playground

> **TensorFlow Playground** is a visual, interactive tool developed by the Google TensorFlow team to help users **build intuition** about neural networks — without writing code.
>
> It allows you to:

- Experiment with binary classification tasks

- Modify the **architecture** (layers, neurons)

- Tune **hyperparameters** (learning rate, activation functions, etc.)

- Observe how different configurations influence learning and model behavior

1.  **Effect of Dataset and Data Randomness**

    - What to expect**:** By selecting different datasets (e.g., circular, spiral, clustered) and regenerating them multiple times, you can observe how randomness affects the model's ability to learn.

> → Some patterns are inherently more **complex** to learn, requiring deeper networks or non-linear activations.

2.  **Changing the Training/Test Data Ratio**

    - What to expect**:** Adjusting the training/test ratio affects generalization.

> → If too little test data is used, **overfitting** may go unnoticed.
>
> → If too little training data is used, **underfitting** becomes likely, and learning fails to generalize.

3.  **Learning Patterns Across Layers**

    - What to expect after training a default NN:

      - **First hidden layer** neurons learn **simple geometric patterns**. o **Second hidden layer** neurons learn to **combine** these into more **complex patterns**.

> → In general, **deeper architectures** can model more complex functions.

4.  **Effect of Activation Functions**

    - What to expect: Replacing the tanh activation with ReLU often leads to **faster convergence**.

> → However, since ReLU is piecewise linear, the decision boundaries it produces tend to be **linear**, limiting expressiveness in some problems.

5.  **Risk of Local Minima in Small Networks**

    - What to expect: Reducing the architecture to **one hidden layer with 3 neurons** increases the risk of **getting stuck in local minima**.

> → Training results may vary widely across runs, and solutions may be suboptimal or inconsistent.

6.  **Underfitting with Insufficient Capacity**

    - What to expect: Further reducing to **just 2 neurons** in the hidden layer typically leads to **consistent underfitting**.

> → The model lacks the capacity (too few parameters) to capture the data distribution, even across multiple runs.

7.  **Robust Performance with Larger Networks**

    - What to expect: Increasing the number of neurons (e.g., to **8**) often leads to:

      - **Faster training** o **Stable convergence** o **Lower chance of poor local minima**

> → Large neural networks rarely get stuck in bad local minima, and even when they do, the local optima are often close in performance to the global optimum.

8.  **Trade-off: Network Size vs. Task Complexity**

    - What to expect: For complex patterns, increasing the number of neurons/layers improves learning.

> → But there is a point of **diminishing returns**: more complexity is not always better — the key is to find the **optimal model size** for your specific task.

9.  **Vanishing Gradients in Deep Networks**

    - What to expect: In a deep architecture (e.g., **4 hidden layers with 8 neurons each**) trained on complex datasets like the **spiral**, you may observe:

      - Training becomes **slower** o The network may get **stuck on flat plateaus** o Neurons in **higher layers** (right side) tend to evolve faster than those in **lower layers** (left side)

> → This is known as the **vanishing gradients problem**, where early layers receive **very small updates** and learn slowly.
>
> **Mitigation techniques:**

- Better weight initialization o Optimizers like **Adam** or **AdaGrad** o **Batch Normalization** **Summary of Observations:**

<!-- -->

- **Small networks** often underfit and may get stuck in poor solutions.

- **Large networks** are more robust and consistently find better optima.

- **Depth** allows modeling more complex relationships but introduces challenges like vanishing gradients.

- **Activation functions** affect both convergence speed and expressiveness.

- There is always a **trade-off** between model complexity, training time, and generalization.

---
> [[AML 29 - Neural Networks|← Neural Networks]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 31 - NNs-representation|NNs-representation →]]
