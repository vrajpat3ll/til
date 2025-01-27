# Data Pre-Processing

- Identification of Dependent and Independent features
- Nominal features
- Missing values features
- [Feature scaling](./feature-scaling.md)

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

<ol>
    <li>
        Drop rows or columns that contain missing values
    </li>
    <li>
        Replace by mean of the entire feature
    </li>
    <li>
        Replace by mean of consecutive values
    </li>
</ol>


<h5 style="text-align: right;">
    <em>last updated on 27th January, 2025</em>
<h6>
