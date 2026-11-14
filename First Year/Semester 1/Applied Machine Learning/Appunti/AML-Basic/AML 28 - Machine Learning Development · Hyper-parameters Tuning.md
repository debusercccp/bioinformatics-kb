---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 28
tags: [note, aml]
---

> [[AML 27 - Machine Learning Development · Performance Metrics|← Machine Learning Development · Performance Metrics]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 29 - Neural Networks|Neural Networks →]]

# Hyper-parameters Tuning

***Algorithm tuning*** is a final step in applied ML development, before finalizing a model. It is sometimes called ***hyperparameter optimization*** and it can be treated as a search problem for the best combination of hyperparameters:

- **<u>Grid search</u>**

Grid search is a structured technique aimed at optimizing the performance of machine learning models by **exhaustively exploring a defined grid of hyperparameters** and their potential values. Essentially, it involves **systematically traversing through various combinations of these hyperparameters**, **evaluating the resultant models** using techniques like cross-validation, and recording the performance metrics. Ultimately, the **combination of hyperparameters that produces the most favorable outcome is identified as the optimal configuration for the model**.

While grid search provides a thorough exploration of the hyperparameter space, it can be **computationally** **demanding**, particularly when dealing with a plethora of hyperparameters or a broad range of values.

- **<u>Random search</u>**

Random search operates by **randomly selecting hyperparameter values from a predefined distribution.** Unlike grid search, which exhaustively evaluates every combination of hyperparameters, random search **explores a broader range of values by randomly sampling them for a set number of iterations.**

Random search is particularly **useful when the search space is large** **and** it's **not clear which hyperparameters are the most important**. It also allows for parallelization since each iteration is independent of the others.

For instance, let's say we're tuning a model and want to find an appropriate value for a parameter like alpha, which falls within the \[0,1\] interval. Instead of exhaustively testing every possible value, we can use random search to sample values from this range. Since we're not constrained by time limitations and don't necessarily need the most optimal value, this approach suits our needs.

By employing random search, we can construct and evaluate models for each combination of randomly selected parameters. This process enables us to explore a diverse set of hyperparameter configurations without being restricted to a predefined grid. Additionally, random search allows for parallelization, meaning we can evaluate multiple parameter combinations simultaneously, further improving efficiency.

Overall, random search offers a flexible and efficient approach to hyperparameter tuning, particularly in scenarios where exhaustive search methods like grid search may be impractical or too resource-intensive.

> **APPLIED MACHINE**
>
> **LEARNING -ADVANCE**

**NEURAL NETWORKS 3**

**LOGICAL COMPUTATION WITH NEURONS 4**

**HANDS ON EXPLORATION: UNDERSTANDING NEURAL NETWORKS USING TENSORFLOW PLAYGROUND 8**

**NNS-REPRESENTATION 10**

**NON-LINEAR CLASSIFICATION 19**

**MNIST 26**

**DECISION TREES (DT) 27**

**KERAS INTERFACE FOR A SHALLOW NN 34**

**MLP FOR REGRESSION AND MLP FOR CLASSIFICATION 40**

**TRAINING AN ANN 43**

**NNs’ BUILDING BLOCKS 48**

GRADIENT BASED OPTIMIZATION **52**

**ENSEMBLE LEARNING 56**

ENSEMBLE: Voting (hard voting – soft voting) 56

RANDOM FORESTS 59

ENSEMBLE: Stacking 62

**CONVOLUTIONAL NEURAL NETWORKS (CNN) 64**

HANDS -ON : DROP-OUT 72

HANDS -ON : DATA AUGMENTATION IN DEEP LEARNING 73

**SUPPORT VECTOR MACHINES (SVM) 74**

**DIMENSIONALITY REDUCTION 80**

DIMENSIONALITY REDUCTION ALGORITHMS: PCA 82

DIMENSIONALITY REDUCTION ALGORITHMS: LLE 84

**VISUALISING FEATURE MAPS, FILTERS AND CLASS OUTPUTS 86**

**AUTOENCODERS 90**

AE architectural choice 94

**RECURRENT NEURAL NETWORK (RNNs) 96**

MEMORY CELLS 99

**HANDLING LONG SEQUENCES: PART 1 102**

NOT SATURATING ACTIVATION FUNCTIONS 104

**HANDLING LONG SEQUENCES: PART 2 109**

ALLEVIATING THE UNSTABLE GRADIENT PROBLEM FOR RNNs 111

ALLEVIATING THE SHORT MEMORY PROBLEM IN RNNs 113

Using 1D convolutional layers to process sequences 116

**DEEP DIVE: OBJECT RECONGITION AND COUNTING 119**

**DEEP DIVE: SEMANTIC SEGMENTATION 121**

**DEEP DIVE: MLops 126**

**INTERPRETABILITY AND EXPLAINABILITY IN AI 131**

Time Series exercises 138

**BONUS MATHERIAL 138**

Introduction to Natural Language Processing (NLP) 141

THE BAG OF WORDS MODEL 145

Generative Learning with VAEs and GANS 148

Generative autoencoders 149

Variational Autoencoders (VAEs) 149

GANS: Generative Adversarial Networks 151

---
> [[AML 27 - Machine Learning Development · Performance Metrics|← Machine Learning Development · Performance Metrics]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 29 - Neural Networks|Neural Networks →]]
