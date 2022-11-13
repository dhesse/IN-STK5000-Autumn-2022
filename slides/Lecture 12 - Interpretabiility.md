# Lecture 12

## Interpretability and Explainability

---


%%%

## Interpretability

* High model transparency 
* Understand exactly **why** and **how** the model is generating
predictions
* Need to observe the **inner mechanics** of the AI/ML method
* Interpreting the model’s **weights and features** to determine the
  given output.

%%%

## Explainability

* Take an ML model and explain the **behavior in human terms**
* With **complex models** one cannot fully understand how and why the
 inner mechanics impact the prediction
* Use model agnostic methods (for example, partial dependence plots,
  SHapley Additive exPlanations (SHAP))

---

# Why is interpretability and explainability important? 

* Trust from business
* Avoiding errors
* Fairness
* Compliance
* ...

---

# Interpretability

* Usually stems from simple models
  * Linear models (log. regression, linear regression)
  * Trees
  * (KNN)
* The more complex a model the harder it is to understand inner
  workings
* Challenging examples: Boosted models, random forests, NN

---

## Partial dependence

* Shows marginal effect of one or two features on predicted outcome
* Shows if dependence is linear, monotonic, or more complex
* Can help model trouble-shooting
* Formally defined as
$$\hat f_S(x_S) = \operatorname{E}_{X_C}\left[\hat f(x_s, X_C)\right]$$
* Can be estimated from data (Monte Carlo)

---

# Shapley Values (SHAP)

* Formal definition

$$\phi_j(v) = \sum_{S\subset \{1,\ldots,p\}\setminus\{j\}}
\frac{|S|!(p - |S|  - 1)!}{p!}\left\{v(S\cup \{j\}) - v(S)\right\}$$

* Computationally expensive to compute
* Efficient methods exists
  * Some exact for specific model classes
  * Some approximate
* Only explanation method with solid theory
