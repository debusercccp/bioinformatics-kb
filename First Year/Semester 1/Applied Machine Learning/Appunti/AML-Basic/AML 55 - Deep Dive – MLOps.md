---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 55
tags: [note, aml]
---

> [[AML 54 - Deep Dive – Semantic Segmentation|← Deep Dive – Semantic Segmentation]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 56 - Interpretability and Explainability in AI|Interpretability and Explainability in AI →]]

# DEEP DIVE: MLops

> **ML Models in Production: Challenges and Best Practices**
>
> Deploying machine learning models into production is a critical step in turning prototypes into real-world applications. However, many ML projects fail before reaching this stage. Why? Because transitioning from research to production introduces a new set of challenges, often related to engineering, reproducibility, scalability, and maintenance. To address this, the emerging field of **MLOps** (Machine Learning Operations) combines machine learning with software engineering practices to ensure that models are robust, reproducible, and maintainable over time.
>
> **The ML Project Pipeline**

![[AML-image383.jpg|269]]

> Machine learning projects follow a structured pipeline that typically includes:

3.  **Data processing** – This involves collecting, cleaning, transforming, and validating data. It also includes exploring the dataset (EDA: Exploratory Data Analysis) to understand potential issues like imbalance or noise.

4.  **Model development** – During this stage, models are trained, evaluated, and iteratively

> improved based on insights from data and performance metrics.
>
> The goal throughout this process is to build models that are not only accurate but also **portable, reproducible**, and capable of operating reliably in production environments.
>
> **MLOps: Managing the Full Lifecycle**
>
> MLOps introduces tools and practices to manage the complete lifecycle of ML models, from development to deployment and monitoring. It supports:

- Reproducible experiments

- Scalable training and inference

- Version control for data, code, and models

- Continuous monitoring and retraining

> While there are many powerful tools available (e.g., MLflow, Kubeflow, DVC), it can be overwhelming to choose and integrate them. A good practice is to start with a manageable stack and expand only when necessary.
>
> **The Importance of Data-Centric AI**

![[AML-image384.jpg|492]]

> A key shift in recent years has been the move from a **model-centric** to a **data-centric** approach. Instead of endlessly refining model architecture, more emphasis is now placed on improving the **quality, balance, and consistency of the data**.
>
> Data issues like imbalance or rare events can significantly skew model performance. For example, in a binary classification task with 3,130 healthy samples and only 112 failure cases, a model that always predicts "healthy" would still be 97% accurate. However, this would be useless in practice. Metrics such as **precision, recall, and F1-score** are much more informative in such scenarios.
>
> To address imbalance, one can:

- Apply upsampling or downsampling strategies.

- Use data augmentation techniques.

- Gather more data for underrepresented classes.

> **Evaluation and Loss Functions**
>
> Performance should be measured using **task-specific metrics**. For imbalanced classification, precision, recall, and F1-score per class are more appropriate than accuracy. Additionally:

- **Macro vs. Micro averaging** offer different insights: macro treats each class equally, while micro considers class frequency.

- **PR-AUC (Precision-Recall Area Under Curve)** is usually more informative than ROCAUC in the presence of imbalance.

> Several **loss functions** are used to guide training:

- **Binary Cross Entropy (BCE)**: standard for binary classification, but less effective with imbalance.

- **Weighted BCE**: assigns more weight to underrepresented classes.

- **Focal Loss**: emphasizes difficult examples and reduces the impact of easy ones.

- **Dice Loss**: common in segmentation, measures similarity between predicted and actual regions.

- **Label Smoothing**: helps reduce overconfident predictions and improves generalization.

> **Experiment Tracking and Model Versioning**
>
> Tracking your experiments is essential. Initially, you may use notebooks, spreadsheets, or even pen and paper, but as complexity grows, frameworks like MLflow or Weights & Biases offer powerful tools for logging:

- Model metrics

- Parameters and hyperparameters

- Dataset versions

- Code versions

> This enables reproducibility and better decision-making during model selection. Additionally, **model versioning** ensures that every deployed model can be traced back to its training data, code, and configuration. A common strategy for versioning uses **semantic versioning** (major.minor.patch, e.g., v2.1.3), and a Git-like workflow for experimentation and release tagging.
>
> A **model registry** acts as a centralized location for storing and managing models, along with their metadata and artifacts. It also controls model lifecycle stages such as:

- **Staging**

- **Production**

- **Archived**

> **Data and Concept Drift**
>
> Once a model is in production, its performance may degrade over time due to **drift**, i.e., changes in data patterns:

- **Data drift** (covariate shift): Input data distribution changes, while the target relationship stays the same.

- **Concept drift**: The relationship between input and target (P(Y\|X)) changes.

- **Label drift**: Distribution of labels changes over time.

> Drift can be detected through:

- Statistical tests (e.g., Kolmogorov-Smirnov, chi-square)

- Distribution metrics (e.g., Jensen-Shannon divergence)

- Monitoring business metrics or model outputs

- Dedicated drift-detection models Common mitigation strategies include:

- Automated retraining pipelines

- Online learning (continuous updates)

- Ensembles of models trained at different times

> **Infrastructure & Containerization**
>
> Robust infrastructure is key for scaling ML in production. **Containerization** (e.g., with Docker) ensures that environments are consistent across development, testing, and deployment.
>
> Benefits of containerization include:

- Isolation of dependencies

- Portability across systems

- Scalability with orchestration tools like Kubernetes

- Easy deployment on cloud platforms (AWS SageMaker, GCP Vertex AI, Azure ML)

> Architectural patterns like **microservices** allow models to be served independently. **Eventdriven** systems can trigger retraining when new data arrives. **Serverless** solutions let you pay per inference and scale automatically.
>
> **Deployment Strategies**
>
> Several deployment strategies are available depending on your risk tolerance and rollout needs:

- **Blue-green deployment**: Switch between two environments (current and new) with instant rollback capability.

- **Canary deployment**: Gradually expose the new model to a small subset of traffic.

- **Shadow deployment**: The new model runs in parallel to the old one, but its outputs are not used.

- **A/B testing**: Run two versions of a model in production to compare performance statistically.

> Other deployment considerations include:

- **Latency**: Real-time systems may need sub-second responses.

- **Throughput**: The number of requests the system can handle concurrently.

- **Resource use**: Ensure the model fits memory and compute constraints.

> **Security, Ethics, and Monitoring**
>
> ML models must operate not only efficiently, but also **responsibly**:

- Ensure **compliance** with data protection regulations (e.g., GDPR, HIPAA).

- Minimize **bias** to ensure fair treatment across demographics.

- Protect against **adversarial attacks**.

- Provide **explainable outputs** when required by regulators or business stakeholders.

> **Monitoring** is critical in production. You should continuously track:

- Model performance over time

- Data quality and consistency

- System infrastructure metrics (e.g., latency, CPU/GPU usage)

- Business KPIs linked to model outputs

> Set up **alerts** to detect anomalies or drops in performance, using either thresholds or MLbased anomaly detection.
>
> **Conclusion**
>
> Although MLOps might seem overwhelming at first, it pays off in the long run. It enables teams to move from proof-of-concept notebooks to reliable, scalable, and maintainable production systems.
>
> There’s no one-size-fits-all tool. Start with a manageable framework, become proficient, and evolve your stack as needed.
>
> **Key Takeaway**
>
> Transitioning from prototype to production is not just about building the best model—it's about ensuring **reproducibility**, **monitoring**, and **alignment with business goals**. Always use the **right metrics** for your application, and keep monitoring, improving, and learning.

---
> [[AML 54 - Deep Dive – Semantic Segmentation|← Deep Dive – Semantic Segmentation]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 56 - Interpretability and Explainability in AI|Interpretability and Explainability in AI →]]
