import pandas as pd

# Data for creating DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

# Creating a DataFrame
df = pd.DataFrame(data)
print("DataFrame:\n", df)

# Accessing the rows and columns
# Single column
print("\nSingle Column (Name):\n", df['Name'])

# Multiple columns
print("\nMultiple Columns (Name, Age):\n", df[['Name', 'Age']])

# Specific row (row 1, column 2)
print("\nSpecific Row [1, 2]:", df.iloc[1, 2])

# Filtered data (Age > 25)
filtered_data = df[df['Age'] > 25]
print("\nFiltered Data (Age > 25):\n", filtered_data)

# Data with NaN values
data_with_nan = {
    'Name': ['Alice', 'Bob', 'Charlie', None],
    'Age': [24, 27, None, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

# Creating a DataFrame with NaN values
dafa = pd.DataFrame(data_with_nan)

# Clean data by removing rows with NaN values
cleaned_df = dafa.dropna()
print("\nCleaned Data (Removed NaN values):\n", cleaned_df)

# Fill missing values with a default value (Age = 20)
filled_data = dafa.fillna({"Age": 20})
print("\nFilled Missing Values (Age = 20):\n", filled_data)

# Drop duplicate rows
drop_duplicate = dafa.drop_duplicates()
print("\nData with Duplicates Removed:\n", drop_duplicate)

# Descriptive statistics
print("\nDescriptive Statistics:\n", df.describe())
print("\nMean Age:\n", df['Age'].mean())

# Group data by 'City' and calculate the mean Age
grouped = df.groupby('City')['Age'].mean()
print("\nGrouped by City (Mean Age):\n", grouped)

# Merging DataFrames
df1 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22]
})

df2 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'David'],
    'City': ['New York', 'Los Angeles', 'Chicago']
})

# Merging df1 and df2 on 'Name' column
merged_df = pd.merge(df1, df2, on="Name")
print("\nMerged DataFrame (on 'Name'):\n", merged_df)

# To read and write data from CSV files
# Reading a CSV file
# df_from_csv = pd.read_csv('file.csv')

# Writing DataFrame to a CSV file
df.to_csv('output.csv', index=False)
print("\nDataFrame saved to 'output.csv'")
