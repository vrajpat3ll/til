# Feature Scaling Techniques

## Why?

- Speeds up convergence in gradient-based algorithms.
- Ensures that no single feature dominates the model due to its scale.
- Improves the performance of regularized models.
- Enhances numerical stability.
- Makes model coefficients more interpretable.

## Common techniques

### Min-Max normalisation

$$
X'\ =\ \frac{X\ -\ \min(X)}{\max(X)\ -\ \min(X)}
$$

- Values transform to range [0, 1]
- When to use:
  - the Data Distribution is _Unknown_
  - doesn't make any assumptions about the data distribution
  - suitable if data is `not Gaussian` (Normal) or has _`outliers`_
- Use when the Algorithms are _sensitive_ to scale of data
  - algos like KNN, SVM, K-Means, PCA, NNs

$$
X'\ =\ a\ +\ (b\ -\ a)\ \cdot\ \left(\frac{X\ -\ \min(X)}{\max(X)\ -\ \min(X)}\right)
$$

- Values transform to range [a, b]

- Advantages

  - `Simple Interpretation`: Transforms data to a uniform range.
  - `Retains Relationships`: Does not distort the shape or distribution of the data.
  - `Improved Convergence`: For gradient-based models like neural networks, scaled features help avoid exploding or vanishing gradients.

- Disadvantages
  - `Sensitive to Outliers`: Since min-max normalization uses the minimum and maximum values of a feature, it is sensitive to outliers. If outliers are present, consider robust scaling techniques (e.g., standardization or robust scaling).
  - `Feature Dependence`: If new data is added, the $\min(X)$ and $\max(X)$ might change, requiring re-scaling.

### Z-score Normalisation or Standardization

$$
X'\ =\ \frac{X\ -\ \mu}{\sigma}
$$

- Value centred around mean 0 with standard deviation of 1
- When to use:

  - Data follows Gaussian Distribution (algos like linear&logistic regression, LDA assume normal features)
  - Outlier Robustness is needed (less sensitive to outliers)
  - Algos sensitive to feature magnitude (PCA,SVM, KNN, GD-based models)\

- Advantages:

  - `Handles Data Centering and Scaling`: Centers data around zero and adjusts for varying feature magnitudes.
  - `Improved Performance for Distance-Based Models`: Works well for models that rely on distances or gradients.
  - `Less Sensitive to Outliers`: Compared to min-max normalization, z-score scaling is less affected by outliers.

- Disadvantages:
  - `Not Ideal for Non-Gaussian Data`: If the data does not follow a normal distribution, z-score scaling might not be as effective as other methods (e.g., robust scaling).
  - `Outliers Can Still Influence`: While more robust than min-max normalization, extreme outliers can still skew the mean and standard deviation.
  - `Dependent on Data`: Like min-max normalization, if new data is added, the mean and standard deviation might change, requiring re-scaling.
