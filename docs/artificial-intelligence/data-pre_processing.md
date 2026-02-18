# Data Pre-Processing

- Identification of Dependent and Independent features
- Nominal features
- Missing values features
- [Feature scaling](./feature-scaling-techniques.md)

## Identification of Dependent and Independent features

> Understand the problem at hand.

---

## Nominal features

- Features that do not have any inherent numerical value or ordinal relationship.
- Find out the number of possible values a few basic features take and make a note of it.
- Encode them with [0, 1, 2, ...] or something similar.

---

## Missing values features

We can do either of the three given methods to get rid of missing values:

1. Drop rows or columns that contain missing values
1. Replace by mean of the entire feature
1. Replace by mean of consecutive values
