---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 18
tags: [note, aml]
---

> [[AML 17 - Regularisation|← Regularisation]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 19 - Model Diagnostics · Trainingtesting Procedure + 01 Misclassification Error|Model Diagnostics · Trainingtesting Procedure + 01 Misclassification Error →]]

# Model Diagnostics

**Machine learning diagnostics** provide insights into the algorithm's strengths and weaknesses, guiding the selection of promising improvement strategies. While implementing and interpreting diagnostics may require time and effort, it's a worthwhile investment in optimizing the algorithm's performance.

Additionally, some machine learning problems may lend themselves more favorably to diagnostic analysis

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Than others.</th>
<th style="text-align: center;"></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="2" style="text-align: center;"><strong>11.1 EVALUATE A LEARNING MODEL</strong></td>
</tr>
</tbody>
</table>

Understanding a machine learning algorithm is just the beginning, when it comes to real-world datasets there are no guaranteed formulas or step-by-step instructions for success.

Each problem presents its own unique challenges, making the application of machine learning both demanding and unpredictable. Efforts to tackle these challenges can be painstaking and time-intensive, and there's often no clear roadmap to guide the process.

Any ML practitioner (less or more expert) need to be able to realize quickly in which direction next efforts had better be invested. What follows aims at giving a number of practical suggestions, advice, guidelines on how to improve in that. A key question is:

*“In developing a ML system and/or trying to improve the performances of a developed one, how do I decide what are the best next steps?”*

There are not specific things that always have to be done, there’s a lot of variability.

You <u>cannot try all the possible things</u>, but you need to <u>find a solution to discard things to try.</u>

Back to the example of housing prices, you have implemented and regularized linear regression, minimized the cost function J, tuned a bit your hyper-parameters. But if you test your hypothesis on new set of houses, suppose you find that this is making huge errors in the prediction of the housing prices.

What should you then try in order to improve the learning algo?

So, everything at the beginning has been trained with our dataset, but somebody gives us additional data. We have a model with previous data, can we predict the price with the new data? What can we do if this doesn’t work. To **enhance** the **performance** of a learning algorithm, several strategies can be considered:

- **<u>Increase training examples</u>**: **Obtaining more training dat**a may improve the model's predictive ability, especially if the current dataset is insufficient. However, acquiring additional data can be costly and timeconsuming, and there's no guarantee of success.

> It's essential to assess the likelihood of improvement before investing resources in collecting more data.

- **<u>Reduce Feature Set</u>**: If overfitting is suspected, reducing the number of features can help prevent the model from fitting noise in the data. Careful **selection of a smaller subset of features** can be a pragmatic approach to address overfitting.

- <u>**Explore Different Features**:</u> Sometimes, the existing features may not provide sufficient information for accurate predictions. Gathering additional or **alternative features** could **enhance** the model's **performance** by capturing more relevant information from the data.

**Implementing changes in these directions often entails <u>significant effort</u>**, particularly when obtaining more data or refining feature sets. Therefore, it's crucial to evaluate the potential benefits before embarking on extensive projects. Alternatively, one can consider **<u>adjusting the complexity of the hypothesis</u>**, such as:

- **<u>Adding Polynomial Features</u>**

- **<u>Tuning Regularization Parameter (λ)</u>**

---
> [[AML 17 - Regularisation|← Regularisation]] · [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 19 - Model Diagnostics · Trainingtesting Procedure + 01 Misclassification Error|Model Diagnostics · Trainingtesting Procedure + 01 Misclassification Error →]]
