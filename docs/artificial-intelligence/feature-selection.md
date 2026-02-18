# _Regularization_: A way to select features

We can add a penalty term to the loss/objective function to put a check on the weights' values.

| Type  | Penalty Term                                           |
| ----- | ------------------------------------------------------ |
| Lasso | L1 norm ($\lambda\cdot\sum_{i=1}^p \lvert w_i \rvert$) |
| Ridge | L2 norm ($\lambda\cdot\sum_{i=1}^pw_i^2$)              |

where $\lambda$ is a positive value. Deciding a good value for it is critical.

When $\lambda = 0$, penalty term does not have any effect on the loss.

If value is too large, al weights correspond to 0 (null model).

## Ridge Regression

- This penalty term can reduce the variance between the weights a lot.
- Should be applied after standardising the predictors.
- If number of features is large, subset selection requires large number of possbiile models. But here, we need to fit only model for a given $\lambda$, and computation turns out to be very simple.
- Weights tend towards 0 but never actually become 0.
- This leads to final model including all predictors, creating a challenge in model interpretation.

## Lasso Regression

- Weights can become 0 where importance is low.
- Produces more interpretabe modelss as they involve only a subset of predictors.
- As $\lambda \uparrow$, variance $\downarrow$ and bias $\uparrow$.

