---
course: "[[Applied Machine Learning]]"
module: "[[Applied Machine Learning (AML-Basic)]]"
source: "MCB/AML/MLFULL.docx"
order: 1
tags: [note, aml]
---

> [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 02 - Types of Machine Learning|Types of Machine Learning →]]

# Definition of Machine Learning

There are **3 main definitions of Machine Learning:**

“The capacity of a computer to learn from experience, i.e. to modify its processing on the basis of newly acquired information”

– The Oxford dictionary of statistics terms (today)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p>“ML is the field of study that gives computers the ability to learn without being explicitly programmed”</p>
<p>– Arthur Samuel (1959), author of the Samuel Checkers-playing Program (and some TeX..)</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

“A machine is said to learn from **<u>experience E</u>** with respect to some **<u>class of tasks T</u>** and **<u>performance measure P</u>** if its performance at tasks in T, as measured by P, improves with experience E.” – Tom Mitchell (1997), \[MIT1\]

Even among ML practitioners there isn't a unique, universally accepted best way to define what ML is in words.

But the ML community agrees on what ML is. Back on Mitchell’s one, which is remarkably interesting, and thinking on a checkers/chess playing example:

- **T** = the task of playing checkers

- **E** = the experience of playing many games of checkers (against itself)

- **P** = the probability that the program will win the next game (against somebody else)

Read it again now, in this example:

“A machine is said to learn from **(E) playing many games** with respect to **(T) the task of** playing that game and the (P) probability to win if the ability to play, measured by the number of wins, improves as more and more games are played”

Applying Mitchell definition to another example.

Your e-mail system is monitoring which emails you do (or do not) flag as spam. Based on the collected info, it learns over time how to flag (and filter out) spam e-mails for you. What is the task T, E, P in this example, among the following?

- classifying emails as spam or not spam —\> T

- watching you label emails as spam or not spam —\> E

- the \# or fraction of emails correctly classifieds spam/not spam —\> P

- none of the above - this is not a ML problem

## 1.1 MACHINE LEARNING VS AI

Another bigger definitions is this one that inherits a bit of theorizer definitions;

“A **sub-domain of AI** that provides software systems the ability to **automatically learn** and **improve** **from experience without being explicitly programmed.** It relies on an underlying hypothesis about a model one creates, and tries to improve such model by fitting more and more data into the model over time.”

– one possible elaboration of definitions from various ML practitioners

Prior to the 1980s, artificial intelligence (AI) existed, albeit not with the emphasis on machines capable of learning autonomously. However, from the 1980s onward, machine learning (ML) began to emerge as a prominent approach within AI, although AI could still be implemented without ML.

![[AML-image1.jpg|408]]By the **2010s**, deep learning (**DL**) **gained prominence as a subset of ML**. However, the advent of DL did not render traditional AI obsolete; rather, it provided a powerful new tool within the broader AI framework.

It's important to note that while these advancements may seem revolutionary, the fundamental concepts of AI and machine learning have roots dating back to the 1950s. These disciplines are intricately nested within each other, with each building upon and refining the principles established over decades of research and development.

Learning algorithms are *everywhere:*

- **spam** mail filters

- **web search engines** (ranking possible because of a learning algo)

- **clickstream data** collection and consumers’ profiling via ML

- **self-customizing programs** (Amazon, Spotify, etc), ML-based recommendation systems, as there is no way to write different programs for million of users

- **pattern recognition**. Handwriting recognition. Natural language processing (NLP). Computer vision.

- It may apply to **Science** (e.g. medical diagnosis applications, computational biology, gene/DNA sequencing, ..), as well as **Industry** (many segments of engineering, predictive maintenance. All fields of research/industry pertaining to finding patterns (at large) and using these to produce predictions is largely influenced by techniques from applied ML.

We tend to talk about AI because it raises the dichotomy with the human intelligence, that is try to do with machines what humans do. Will AI replace human intelligence?

**No**. At least, not in a foreseeable future. Admittedly AI experts think the best approach to implement the ML definition of learning is to try to mimic how the human brain learns, but that’s a different point.

- *Example*: where is intelligence (HI) located, at the best of today’s knowledge?

- *Example*: a baby learning car shapes over time, is this “intelligence”?

Before continuing, we had better reshape our terminology to assess the proper content of the course when we talk about “AI”

“AIˮ terminology perhaps misleading in most practical discussions. Most of AI research today is actually not trying to recreate intelligence in any shape or form, at all.

The objective is **collecting data around how humans make decisions**, **<u>to perform the same tasks at a scale</u> <u>(LARGE) and latency (SMALL) that are not humanly possible.</u>**

![[AML-image2.jpg|697]]

Example: facial recognition.

The best of us can link thousands of faces to names, without cheating. Machines can do this for hundreds of millions of faces, and in less time. Are such machines smarter than us in a general sense? Not even close! But for that specific domain, once trained with large amounts of data, they perform that task at a speed and scale that is beyond what any human may ever hope for.

—\> This is the “artificial intelligenceˮ we are talking about.

So, all started from AI decades ago when the original idea was to build intelligent machines by programming them, but programming for a task work for *some* tasks - not for *all* tasks…

- we can program a machine to solve math, or find the shortest path from A to B

- we cannot program a machine to read-and-tag a spam email or to see-and-tag a photo - unless we accept to continuously retune the algorithm, personalize it, etc

…so, it soon became clear that the only way to perform such tasks is to enable a machine to learn how to perform specific tasks by itself.

We actually want to develop a system so that the machine is able to learn how to perform tasks by itself. We want something that complements the human mind, not replace it.

**Integration of intelligences**

Areas that may benefit from this “***automation of task execution and decision making***” are areas where such advancement would eventually **help humans**.

In this scope, it is beneficial to use machines instead of humans in tasks that either humans do not want to do or cannot do as well:

- *Example*: AI-based systems able to retain high-performances also in high- stress conditions or environmental dangers unbearable by humans

The keyword might be **integration —\>** AI “**together with**” HI, and not “instead of”.

- *Example*: recent progresses in ML-based radiology, yielding unprecedented results, as well as surprisingly interesting ethical implications in not using AI.

## 1.2 ACCELERATION TOWARDS LARGER ADOPTION OF ML

If all this was already available decades ago, why the rise of AI we see today has not happened earlier like in the 70s or 80s? Something happened only in the second decades of this century.

Recently, there has been a resurgence and rapid advancement in machine learning and deep learning, driven by several key factors:

1.  **<u>The raise of Big Data</u>**

Big data serves as the crucial fuel for driving advancements in these fields. Just like how a car engine requires fuel to run efficiently, without quality data, the potential of powerful processing units like GPUs remains untapped. High-quality data leads to meaningful insights, whereas poor-quality data yields inferior results.

2.  **<u>Technological Progress</u>**

Technological advancements, particularly in **graphics processing units** (GPUs), have played a **significant role** in **accelerating the development of machine learning** and deep learning algorithms.

In the realms of machine learning and deep learning, computational tasks predominantly entail a **multitude of elementary operations** rather than intricate computations. The development of the processing units needed for these tasks originated from the gaming industry's desire for better graphics. This technological evolution emerged during a period when such advanced computational capabilities were not readily accessible. Consequently, these specialized chips found utility beyond gaming, serving as instrumental components in teaching computers to glean insights from data.

3.  **<u>Democratization of Computing Resources through Cloud Technology</u>**

Historically, accessing substantial computing resources required establishing and maintaining dedicated computer centers, which was complex and costly. However, the advent of cloud computing has democratized access to massive computing power. Through cloud-based services, individuals and organizations can **rent server resources** **from providers** like Google or Amazon, paying only for what they use.

While this **democratization** **makes** it **possible** for more people to **access computing resources**, it remains relatively expensive and is not feasible for everyone.

Today, it is a fact that ML/DL are among the core transformative technologies at the basis of most world-wide activities aiming at extracting actionable insight from (big) data.

These technologies have the potential to bring about significant and far-reaching changes similar to the profound impact that the internet had when it first emerged With an abundance of data at our disposal and sophisticated analytical tools at hand, we are empowered to derive valuable information and insights applicable across diverse fields. It's imperative to explore and discuss various methodologies for extracting actionable insights from big data to fully leverage the capabilities of ML and DL.

---
> [[Applied Machine Learning (AML-Basic)|↑ AML-Basic]] · [[AML 02 - Types of Machine Learning|Types of Machine Learning →]]
