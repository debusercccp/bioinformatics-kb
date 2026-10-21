---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 57
tags: [note, aml]
---

> [[AML 56 - Interpretability and Explainability in AI|← Interpretability and Explainability in AI]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 58 - Introduction to Natural Language Processing (NLP)|Introduction to Natural Language Processing (NLP) →]]

# Bonus Matherial

## Time Series exercises

> **Forecasting Time Series: Traditional vs Deep Learning Approaches: Why Time Series Forecasting Matters**
>
> Forecasting time series data — like stock prices, weather, energy demand, or sales — is a cornerstone of data-driven decision-making. Traditionally, this has been the domain of **statistical models**, but modern deep learning methods are now reshaping what's possible.

1.  **ARMA (AutoRegressive Moving Average)** At its core, ARMA models rely on two ideas:

    - **Autoregression (AR)**: Future values depend on past values.

    - **Moving Average (MA)**: Future values also depend on past forecast errors.

2.  **ARIMA: ARMA + Differencing**

> ARIMA improves upon ARMA by adding the **"Integrated" (I)** component, which involves differencing the data (e.g., subtracting a value from its previous value) to make it **stationary** — a key assumption for accurate modelling.

- Notation: **ARIMA(p, d, q)** o p: number of autoregressive terms o d: number of differences o q: number of moving average terms

> **pros of ARIMA**:

- Great for datasets with trends.

- Easy to interpret and relatively fast.

> **Cons**:

- Can’t directly model **seasonality** (like repeating annual/monthly patterns).

3.  **SARIMA: Seasonality to the Rescue**

> SARIMA extends ARIMA to explicitly model seasonal effects:

- Notation: **SARIMA (p, d, q)(P, D, Q, m)** o P, D, Q: same concepts, but for **seasonal** components

  - m: number of time steps in one seasonal period (e.g., 12 for monthly data with yearly seasonality) **Pros**:

- Handles both **trend and seasonality** well.

- Excellent performance on small/medium datasets.

> **Cons**:

- Needs **a lot of manual tuning** (7+ parameters!).

- Can be computationally expensive for exhaustive searches.

- Doesn’t scale as well on large or high-dimensional datasets.

> **Deep Neural Networks (DNNs) for Time Series**
>
> As datasets become **larger and more complex**, traditional statistical models hit a wall — and this is where **deep learning** comes in. **What DNNs offer**:

- They can learn **directly from raw data** without:

  - Scaling (normalization, standardization) o Making the data stationary (no differencing)

- They can model **non-linear**, complex relationships over time.

- Often **more robust** to noise or anomalies.

- **No need for feature engineering**: the network learns the important patterns automatically.

- Especially powerful when working with **Big Data**.

> **Example**:
>
> A simple feedforward DNN trained on raw historical values can outperform carefully-tuned ARIMA or SARIMA models on many univariate time series — even with trend and seasonality present. Note: We're saying **DNNs**, not specifically **RNNs** (Recurrent Neural Networks) — those will come up later and are specialized for sequential data.
>
> **Validation of time series: Walk-Forward Validation**
>
> **“Walk-forward” validation** is an approach to evaluate time series forecasting models on a test set

- the model makes a **forecast** for each observation, i.e. for each time step in the test set, one at a time.

- after each **forecast** is **made**, the true observation at that time step is added to the test dataset and made available to the model.

- In case of simple models, one can **refit** **them** with the observation prior to making the subsequent prediction.

- In case of **more complex models** - such as **NNs** - one cannot refit given the much greater computational cost. Nevertheless, the true observation for the time step can then be used as part of the input for making the prediction on the next time step.

> We live with the fact that NN models are **stochastic**

- given the **same** **model** **configuration** and the **same** **training** **dataset**, we will get a different internal set of weights every time the model is trained, so a different performance (according to its measure as from the metrics of my choice.)

> actually, it is a benefit:

- in theory, it is a sign that the model is allowed to be **adaptive** and hence can find high performing configurations towards solutions to complex problems.

- in practice, it is admittedly a problem when evaluating the performance of a set of developed models, and in choosing “my final model” to use in order to make predictions

> How do we address **model evaluation**? • we will **evaluate a model configuration multiple times via walk-forward validation and report the error as the average error across each evaluation.**
>
> From the multiple repeats, we will summarise the performance by using summary statistics (mean and std deviation) and/or plotting.

---
> [[AML 56 - Interpretability and Explainability in AI|← Interpretability and Explainability in AI]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 58 - Introduction to Natural Language Processing (NLP)|Introduction to Natural Language Processing (NLP) →]]
