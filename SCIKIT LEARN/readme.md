# K-Nearest Neighbors Regression for California Housing

This project demonstrates the use of **K-Nearest Neighbors (KNN)** regression to predict the housing prices in California using the **California Housing dataset**. It covers basic data processing, model training, and evaluation using `KNeighborsRegressor`, `GridSearchCV`, and `Pipeline`. The goal is to show how KNN regression works, tune hyperparameters using GridSearchCV, and visualize the results.

## Features

- **Basic Model**: KNN regression to predict housing prices.
- **Pipeline with Scaling**: Using `StandardScaler` to scale features.
- **Grid Search for Hyperparameter Tuning**: Finding the best `n_neighbors` for the KNN model.
- **Visualization**: Scatter plot comparing actual vs predicted values.

## Prerequisites

To run this project, you need to have the following libraries installed:

- **scikit-learn**
- **pandas**
- **matplotlib**

You can install these dependencies using pip:

```bash
pip install scikit-learn pandas matplotlib
```

## Code Walkthrough

### 1. **Loading the Dataset**

We start by fetching the California Housing dataset using `fetch_california_housing()` from `sklearn.datasets`.

```python
X, y = fetch_california_housing(return_X_y=True)
```

### 2. **Training the Basic Model**

We fit a **KNeighborsRegressor** to the dataset and make predictions.

```python
mod = KNeighborsRegressor().fit(X, y)
pred = mod.predict(X)
```

A scatter plot is used to compare the predicted vs actual housing prices.

```python
plt.scatter(pred, y)
plt.show()
```

### 3. **Using a Pipeline with Scaling**

To improve model performance, we use a pipeline that includes **StandardScaler** for feature scaling followed by KNN regression.

```python
pipe = Pipeline([
    ("scale", StandardScaler()),
    ("model", KNeighborsRegressor())
])
pipe.fit(X, y)
pred = pipe.predict(X)
```

A scatter plot is generated for the predictions.

```python
plt.scatter(pred, y)
plt.show()
```

### 4. **Hyperparameter Tuning with Grid Search**

We tune the **`n_neighbors`** parameter using **GridSearchCV**. The model is trained with different values of `n_neighbors` to find the optimal value.

```python
mod = GridSearchCV(estimator=pipe,
                   param_grid={"model__n_neighbors": [1, 2, 3, 4, 5, 7, 8, 9, 10]},
                   cv=3)
mod.fit(X, y)
```

### 5. **Visualizing Actual vs Predicted Values**

A scatter plot is generated to compare actual vs predicted values, with a line representing perfect predictions.

```python
plt.scatter(y, pred, alpha=0.7, edgecolors='k', label="Predicted vs Actual")
plt.plot([y.min(), y.max()], [y.min(), y.max()], color='red', linestyle='--', label="Perfect Prediction Line")
plt.title("Actual vs Predicted Values")
plt.xlabel("Actual Values (y)")
plt.ylabel("Predicted Values")
plt.legend()
plt.show()
```

### 6. **Viewing Predictions**

After the GridSearchCV model is fitted, we view the first few predicted values alongside actual values.

```python
predictions_df = pd.DataFrame({"Actual": y, "Predicted": pred})
print(predictions_df.head(10))
```

## Example Output

The output of the model includes:

1. **Predicted vs Actual Scatter Plot**: A scatter plot showing the correlation between predicted and actual housing prices.
2. **Hyperparameter Tuning Results**: The best `n_neighbors` value found using GridSearchCV.
3. **Predictions**: The first 10 predicted housing prices alongside the actual values.

## Conclusion

This project demonstrates the use of **K-Nearest Neighbors regression** for predicting housing prices using the **California Housing dataset**. It also showcases how to use **Pipeline** for feature scaling, and how to fine-tune the model with **GridSearchCV**.
