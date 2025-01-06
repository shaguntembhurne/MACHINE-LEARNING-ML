

# Titanic Survival Prediction

## Project Overview

This project involves using machine learning to predict whether a passenger on the Titanic survived based on various features such as age, sex, class, and other personal details. The dataset contains features like `PassengerId`, `Pclass`, `Sex`, `Age`, `SibSp`, `Parch`, `Fare`, `Embarked`, and the target variable `Survived` (indicating if the passenger survived).

The goal is to apply machine learning techniques to train a predictive model and make predictions on unseen data (the test set).

## Table of Contents

1. [Project Overview](#project-overview)
2. [Data](#data)
3. [Setup](#setup)
4. [Project Workflow](#project-workflow)
    - Data Loading
    - Preprocessing
    - Model Training
    - Predictions
5. [Code Structure](#code-structure)
6. [Requirements](#requirements)
7. [Future Improvements](#future-improvements)
8. [License](#license)

## Data

The Titanic dataset consists of two files:

1. **train.csv**: This file contains both features and the target variable `Survived`. It is used for training the model.
2. **test.csv**: This file contains the features only (without the `Survived` column). It is used to make predictions.

The following columns are present in the dataset:
- **PassengerId**: Unique ID for each passenger.
- **Pclass**: Passenger class (1st, 2nd, 3rd).
- **Name**: Name of the passenger.
- **Sex**: Gender of the passenger (male/female).
- **Age**: Age of the passenger.
- **SibSp**: Number of siblings or spouses aboard the Titanic.
- **Parch**: Number of parents or children aboard the Titanic.
- **Fare**: The fare paid by the passenger.
- **Embarked**: Port of embarkation (C = Cherbourg; Q = Queenstown; S = Southampton).
- **Survived**: Whether the passenger survived (1 = Yes, 0 = No).

## Setup

### 1. Clone the repository

To begin, clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/titanic-survival-prediction.git
cd titanic-survival-prediction
```

### 2. Install dependencies

Make sure you have Python 3.6 or higher installed, then create and activate a virtual environment. Install the required libraries by running:

```bash
pip install -r requirements.txt
```

`requirements.txt` should include the following dependencies:

```
pandas
numpy
scikit-learn
```

### 3. Place Data

Download the Titanic dataset from [Kaggle](https://www.kaggle.com/c/titanic/data) and place the `train.csv` and `test.csv` files in the `data/` directory.

## Project Workflow

### Data Loading

First, we load the dataset using pandas:

```python
import pandas as pd

# Load the Titanic dataset
train_data = pd.read_csv('data/train.csv')
test_data = pd.read_csv('data/test.csv')
```

The `train.csv` file will be used to train the model, and the `test.csv` will be used for prediction.

### Preprocessing

Before feeding the data into a machine learning model, we need to preprocess the data:

1. **Handle Missing Values**: Some columns like `Age` and `Embarked` may have missing values. We handle these by imputing the missing values (e.g., using the mean for `Age` and the most frequent value for `Embarked`).

2. **Feature Scaling**: Machine learning models perform better when numerical features are scaled. We apply `StandardScaler` to scale features like `Age`, `Fare`, and other numerical columns.

3. **Feature Encoding**: Categorical variables such as `Sex` and `Embarked` need to be encoded into numeric values using techniques such as `OneHotEncoder` or `LabelEncoder`.

4. **Feature Selection**: Drop irrelevant or unnecessary columns, such as `Name`, which are unlikely to help in predicting survival.

```python
# Handle missing values
train_data['Age'] = train_data['Age'].fillna(train_data['Age'].mean())
train_data['Embarked'] = train_data['Embarked'].fillna(train_data['Embarked'].mode()[0])

# Convert 'Sex' and 'Embarked' columns to numerical values
train_data['Sex'] = train_data['Sex'].map({'male': 0, 'female': 1})
train_data['Embarked'] = train_data['Embarked'].map({'C': 0, 'Q': 1, 'S': 2})

# Drop columns that are not needed
train_data = train_data.drop(['Name', 'Ticket', 'Cabin', 'PassengerId'], axis=1)
```

### Model Training

We use a machine learning model, such as **RandomForestClassifier**, to predict survival. The model is trained on the processed training data.

1. **Feature Selection**: The features used to train the model are `Pclass`, `Sex`, `Age`, `SibSp`, `Parch`, `Fare`, and `Embarked`.

2. **Model Fitting**: We fit the model on the training data.

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Separate features (X) and target variable (y)
X = train_data.drop('Survived', axis=1)
y = train_data['Survived']

# Split data into training and validation sets
X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_valid_scaled = scaler.transform(X_valid)

# Train RandomForest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Validate the model
print(f"Model accuracy: {model.score(X_valid_scaled, y_valid)}")
```

### Predictions

Once the model is trained, we use it to make predictions on the `test.csv` data. The predictions are saved to a CSV file (`test_predictions.csv`).

```python
# Process the test data in the same way as the training data
test_data['Sex'] = test_data['Sex'].map({'male': 0, 'female': 1})
test_data['Embarked'] = test_data['Embarked'].map({'C': 0, 'Q': 1, 'S': 2})
test_data = test_data.drop(['Name', 'Ticket', 'Cabin', 'PassengerId'], axis=1)

# Handle missing values
test_data['Age'] = test_data['Age'].fillna(test_data['Age'].mean())
test_data['Fare'] = test_data['Fare'].fillna(test_data['Fare'].mean())

# Scale features
X_test = scaler.transform(test_data)

# Make predictions
test_predictions = model.predict(X_test)

# Create a DataFrame with PassengerId and predictions
output_df = pd.DataFrame({'PassengerId': test_data['PassengerId'], 'Survived': test_predictions})

# Save predictions to CSV
output_df.to_csv('data/test_predictions.csv', index=False)
```

### Save and Share the Predictions

The predictions are saved in `test_predictions.csv` in the following format:

| PassengerId | Survived |
|-------------|----------|
| 892         | 0        |
| 893         | 1        |
| ...         | ...      |

You can submit this file to Kaggle or use it for further analysis.

## Code Structure

The code is structured as follows:

```
titanic-survival-prediction/
│
├── data/
│   ├── train.csv
│   ├── test.csv
│
├── src/
│   ├── data_preprocessing.py  # Code for data cleaning and preprocessing
│   ├── model_training.py      # Code for training the machine learning model
│   ├── predictions.py         # Code for making predictions on the test set
│
├── requirements.txt           # Python package dependencies
├── README.md                  # Project documentation
```

## Requirements

- Python 3.6 or higher
- pandas
- numpy
- scikit-learn

Install the required libraries using the following command:

```bash
pip install -r requirements.txt
```

## Future Improvements

1. **Hyperparameter Tuning**: Use techniques like GridSearchCV or RandomizedSearchCV to tune hyperparameters of the model for better performance.
2. **Model Evaluation**: Use additional evaluation metrics such as Precision, Recall, F1-Score, or ROC-AUC.
3. **Feature Engineering**: Explore new features such as `FamilySize` (combining `SibSp` and `Parch`) or `IsAlone` (whether the passenger is traveling alone).
4. **Ensemble Methods**: Combine predictions from multiple models (e.g., RandomForest, XGBoost, and Logistic Regression) to improve accuracy.

