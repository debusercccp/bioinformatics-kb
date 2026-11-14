---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 56
tags: [note, aml]
---

> [[AML 55 - Deep Dive – MLOps|← Deep Dive – MLOps]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 57 - Bonus Matherial + Time Series exercises|Bonus Matherial + Time Series exercises →]]

# Interpretability and Explainability in AI

> **Linear Models**
>
> Linear models, such as linear regression, are inherently interpretable. Their structure is straightforward: each feature has a coefficient, and predictions are made through a simple equation like **y = β₀ + β₁x₁ + β₂x₂ + ... + β**ₙ**x**ₙ.
>
> This makes it easy to trace how each input affects the output. A positive coefficient increases the predicted value, while a negative one decreases it. The relationship between features and the prediction is direct and transparent.
>
> **Tree-Based Models**
>
> Tree-based models use a flowchart-like structure to make decisions. Each internal node represents a condition (e.g., “Age \> 30?”), and the data follows a path based on these if-else rules. While single decision trees remain fairly interpretable, as we move toward **Random Forests** and **Gradient Boosting Machines (GBMs)**, interpretability starts to decrease. This is due to the use of many trees, often hundreds or thousands, working together. The overall structure becomes too complex for humans to follow easily, even though each individual tree is transparent.
>
> **Neural Networks**
>
> Artificial Neural Networks (ANNs), especially deep learning models, are often referred to as **black boxes**. From simple feedforward networks to more advanced architectures like CNNs, RNNs, and Transformers, these models are highly capable but difficult to interpret. Their predictions are based on learned weights and complex feature interactions across multiple layers. As performance improves, the ability to understand the model’s inner workings by design diminishes.
>
> **The Interpretability Spectrum**

![[AML-image385.jpg|642]]

> We can place machine learning models along a spectrum based on how transparent their internal workings are:

- **White Box Models** are fully interpretable. Examples include linear or logistic regression, decision trees, and rule-based systems. Their behavior can be easily understood by inspecting their structure.

- **Gray Box Models** offer partial interpretability. Models like Random Forests, Gradient Boosting, and SVMs with non-linear kernels can be interpreted with the help of external tools or explanations, but not directly.

- **Black Box Models** are the least interpretable. Deep neural networks, including CNNs, RNNs, LSTMs, and Transformers, often require post-hoc techniques to explain why they make certain predictions.

> **The Machine Learning Dilemma**
>
> This leads to a well-known trade-off in ML:

- **Simple models** are easy to interpret but may underperform on complex tasks.

- **Complex models** tend to achieve higher accuracy, but their decision-making process is much harder to understand.

> **The Growing Need for Transparency**
>
> This dilemma has gained real-world significance due to increasing legal and ethical pressures.
>
> Under the **General Data Protection Regulation (GDPR)**, individuals have the **right to an explanation** when subject to automated decisions. The **EU AI Act (2024)** further reinforces this by requiring different levels of transparency based on the risk associated with the AI system.
>
> **Example: COMPAS Case Study**
>
> The COMPAS system, used in the U.S. for criminal risk assessments, assigned higher risk scores to people of color. Because it was a black-box model with no built-in transparency, it required an external audit to reveal its biases. This highlighted the importance of **fairness, accountability**, and **trust** in AI systems.
>
> **Interpretability vs Explainability**
>
> These two concepts are related but not the same:

- **Interpretability** refers to the extent to which a model can be understood just by looking at it. It's an **intrinsic** property. For example, in linear regression or decision trees, you can follow the logic step-by-step.

- **Explainability**, on the other hand, refers to **external techniques** applied after a model is built. These techniques help make sense of complex models. Examples include SHAP values, LIME, and feature importance plots. Here, the goal is not to understand the model’s internal mechanics, but to explain **why it made a specific prediction**.

![[AML-image386.jpg|642]]

> **Explainable AI (XAI)**
>
> ![[AML-image387.jpg|357]]XAI is a research field focused on making machine learning systems more transparent and accountable.
>
> Its core objective is to make the model’s decisions understandable to humans. Explanations can take various forms:

- Attributing a percentage of the decision to specific input features (e.g., "Debt-to-income ratio contributed 60%").

- Pointing to similar examples the model has seen before.

- Providing counterfactuals ("If income were €10,000 higher, the loan would be approved").

> **Levels of Explanation**

- **Global**: Understand how the model behaves overall.

- **Group**: Investigate how it treats a subgroup (e.g., 30–40-year-olds with average income).

- **Local**: Focus on a single prediction.

![[AML-image388.jpg|565]]

> **Challenges in XAI**

1.  **What makes a "good" explanation?** Different users (data scientists, regulators, customers) require different kinds of explanations.

2.  **Trust and correctness**: It's not enough for explanations to look convincing — they must accurately reflect the model’s logic.

3.  **Combining techniques**: Blending methods must clarify, not confuse.

4.  **Tool usability**: End-users need intuitive tools to explore and understand model decisions.

5.  **Efficiency**: Explanations should be fast to compute.

6.  **Robustness**: We need frameworks to test how reliable explanation techniques are.

7.  **Built-in explainability**: The long-term goal is to design AI that is transparent by default.

> **Responsible AI**
>
> Explainability is part of the broader concept of **Responsible AI**, which emphasizes the ethical and secure use of AI. Its core pillars include:

- **Fairness**: Avoiding discrimination.

- **Transparency**: Explaining decisions.

- **Accountability**: Holding developers and users responsible.

- **Privacy and Security**: Safeguarding personal data.

> Laws like GDPR, the Data Protection Act, and the EU AI Act reflect these values.
>
> **Explainable AI for Tabular Data**
>
> Tabular data (organized into rows and columns) is common in business, finance, and healthcare. Each row is an observation, and each column is a feature.

![[AML-image389.jpg|642]]

> **Before Modeling: Exploratory Data Analysis (EDA)**
>
> EDA helps identify patterns, detect anomalies, and choose the right model. It includes descriptive statistics, checking for missing or duplicate values, and studying correlations.
>
> **During Modeling: Use Interpretable Algorithms**
>
> Linear models and decision trees are examples where predictions can be explained directly from model structure — no extra tools needed.
>
> Example:
>
> **Price = €50,000 + €10,000 × Number of Rooms – €5,000 × Distance to City Center** This tells you how each feature affects the outcome, both in direction and magnitude.
>
> **After Modeling: Post-Hoc Techniques**
>
> Once complex models are used, we rely on tools to explain them:

- **Feature Importance** assigns scores to features based on how much they influence predictions.

- In trees, importance comes from how much a feature reduces uncertainty at each split.

- In ensembles, multiple metrics are used (split frequency, impurity reduction, etc.).

> **SHAP (SHapley Additive exPlanations)**
>
> SHAP is based on **game theory** and offers a mathematically fair way to assign credit to features for their contribution to a prediction. Its logic is similar to splitting a restaurant bill based on each person's order. For ML models, it means evaluating how much a feature changes the prediction, averaged across all possible combinations of inputs.
>
> **Example:** Predicting house price based on "Rooms", "Location", and "Age" involves looking at every possible order these features could be added. SHAP calculates how much each one contributes, regardless of order.

![[AML-image390.jpg|642]]

> **Challenges**
>
> SHAP is precise but computationally expensive. For large feature sets, exact calculation is impractical. Optimized versions like **TreeExplainer**, **DeepExplainer**, and **KernelExplainer** reduce runtime by approximating values.
>
> **LIME (Local Interpretable Model-agnostic Explanations)**
>
> LIME works by approximating the complex model **locally** using a simpler, interpretable model (like a linear regression), focusing only on one prediction at a time.

![[AML-image391.jpg|642]]

> **Example**
>
> Say the model predicts a 72% loan approval probability for a 35-year-old earning €45,000.
>
> LIME generates slight variations of this input and observes how the prediction changes. A simple model is fit to these points, helping explain which features mattered most — perhaps showing that credit score had the biggest impact.
>
> LIME is fast and useful for local explanations, but it lacks the theoretical guarantees of SHAP.
>
> **SHAP vs LIME: Key Differences**

- **Scope**: SHAP can explain both globally and locally; LIME is local only.

- **Theory**: SHAP is grounded in game theory and guarantees fairness; LIME uses sampling and linear fitting.

- **Speed**: LIME is generally faster; SHAP can be slower unless optimized.

- **Interpretability**: LIME always gives a linear explanation; SHAP can capture non-linear effects too.

![[AML-image392.jpg|642]]

---
> [[AML 55 - Deep Dive – MLOps|← Deep Dive – MLOps]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 57 - Bonus Matherial + Time Series exercises|Bonus Matherial + Time Series exercises →]]
