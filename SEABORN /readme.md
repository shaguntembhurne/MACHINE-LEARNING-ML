

# Seaborn Data Visualization Example

This repository contains examples of various types of data visualizations using the `seaborn` library. The dataset used in this project includes **car crashes** data (`car_crashes`) and **tips** dataset (`tips`), which are available through Seaborn’s built-in dataset loader.

## Libraries Used
- **seaborn**: A Python data visualization library based on `matplotlib` that provides an interface for creating informative and attractive statistical graphics.
- **numpy**: Used for numerical operations.
- **matplotlib**: Used for creating static, animated, and interactive visualizations in Python.
- **pandas**: Data manipulation and analysis library.

## Setup Instructions

### Requirements

Ensure you have the following libraries installed:

```bash
pip install seaborn matplotlib numpy pandas
```

### Usage

You can run the notebook or script to view and analyze various visualizations.

```python
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Set up the environment
%matplotlib inline
%reload_ext autoreload
%autoreload
```

### Available Visualizations:

1. **Distribution Plot**: Visualizes the distribution of a numerical variable.
    ```python
    sns.displot(crash_df['no_previous'], kde=True, bins=25)
    ```

2. **Joint Plot**: Plots the relationship between two variables and their distributions.
    ```python
    sns.jointplot(x="alcohol", y="speeding", data=crash_df, kind="reg")
    ```

3. **KDE Plot**: Kernel Density Estimate plot that estimates the probability density function of a continuous variable.
    ```python
    sns.kdeplot(crash_df['alcohol'])
    ```

4. **Pair Plot**: Displays pairwise relationships between numerical variables.
    ```python
    sns.pairplot(crash_df)
    ```

5. **Categorical Plots**: Visualizations for categorical data, including bar plots, count plots, and box plots.
    ```python
    sns.barplot(x="sex", y='total_bill', data=tips_df, estimator=np.std)
    sns.countplot(x="sex", data=tips_df)
    sns.boxplot(x="day", y='total_bill', data=tips_df, hue="sex")
    ```

6. **Violin Plot**: A combination of box plot and KDE to show the distribution of the data.
    ```python
    sns.violinplot(x="day", y='total_bill', data=tips_df, hue="sex")
    ```

7. **Heatmap**: Visualizes data in a 2D matrix with color coding.
    ```python
    flights = sns.load_dataset('flights')
    flights = flights.pivot_table(index="month", columns="year", values="passengers")
    sns.heatmap(flights, cmap="Blues", linecolor="white", linewidths=1)
    ```

8. **FacetGrid**: Faceted grid-style plots for creating multiple subplots based on categorical variables.
    ```python
    g = sns.FacetGrid(crash_df, col="speeding", col_wrap=3, height=4)
    g.map(sns.histplot, "alcohol", kde=True)
    ```

### Custom Styling:

You can apply custom styles to improve the presentation of your plots:

```python
sns.set_style('darkgrid')
sns.set_context("paper")
```

### Example Plots:

- **Pair Plot with Hue**: Visualizing relationships with hue categories (e.g., `sex`):
  ```python
  sns.pairplot(tips_df, hue="sex", palette="Blues")
  ```

- **Strip Plot**: Display individual data points on a categorical axis:
  ```python
  sns.stripplot(x="day", y='total_bill', data=tips_df, dodge=True, hue="sex")
  ```

---

### Files Included

- **Visualization Notebooks**: Jupyter Notebooks or Python scripts to visualize the datasets.
- **Dataset**: The datasets are included via `seaborn.load_dataset()`.
