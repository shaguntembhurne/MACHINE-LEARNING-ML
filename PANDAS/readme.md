

# Pandas DataFrame Operations

This project demonstrates various data manipulation operations using the Pandas library in Python. It covers creating DataFrames, performing basic operations like accessing rows/columns, filtering data, handling missing values, and merging DataFrames. Additionally, it includes aggregating data and working with descriptive statistics.

## Features

- **Creating DataFrames**: Learn how to create DataFrames from dictionaries.
- **Accessing Rows and Columns**: Perform operations to access individual or multiple columns and specific rows.
- **Filtering Data**: Filter data based on conditions (e.g., Age > 25).
- **Handling Missing Data**: Drop or fill missing values (NaN).
- **Removing Duplicates**: Remove duplicate rows from the DataFrame.
- **Descriptive Statistics**: Calculate summary statistics like mean, sum, etc.
- **Merging DataFrames**: Merge two DataFrames on a common column.
- **Reading and Writing CSV Files**: Read data from CSV files and write data to CSV files.

## Requirements

- Python 3.x
- Pandas library

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/pandas-dataframe-operations.git
   ```

2. Install the required Python package (Pandas):
   ```bash
   pip install pandas
   ```

## Usage

1. Navigate to the project directory and run the script:
   ```bash
   python pandas_operations.py
   ```

2. The script will execute various Pandas operations and print the results in the terminal.

## Code Explanation

### 1. **Creating DataFrames**
   - `pd.DataFrame()` is used to create a DataFrame from a dictionary containing data (e.g., `Name`, `Age`, and `City`).

### 2. **Accessing Rows and Columns**
   - Single and multiple columns are accessed using column names (e.g., `df['Name']`).
   - Specific rows are accessed using `.iloc[]` to get data by position.

### 3. **Filtering Data**
   - Filter the DataFrame based on conditions (e.g., `df[df['Age'] > 25]`).

### 4. **Handling Missing Data**
   - Remove rows with missing values using `.dropna()`.
   - Fill missing values with default values using `.fillna()`.

### 5. **Removing Duplicates**
   - Remove duplicate rows using `.drop_duplicates()`.

### 6. **Descriptive Statistics**
   - `.describe()` provides a summary of statistics for numerical columns.
   - `.mean()` calculates the mean of a specified column.

### 7. **Merging DataFrames**
   - Merge two DataFrames on a common column using `pd.merge()`.

### 8. **Reading and Writing CSV Files**
   - `pd.read_csv()` is used to read data from a CSV file.
   - `.to_csv()` writes the DataFrame to a CSV file.

## Example Output

```bash
DataFrame:
       Name  Age           City
0     Alice   24       New York
1       Bob   27    Los Angeles
2   Charlie   22        Chicago
3     David   32        Houston

Single Column (Name):
 0      Alice
1        Bob
2    Charlie
3      David
Name: Name, dtype: object

Multiple Columns (Name, Age):
       Name  Age
0     Alice   24
1       Bob   27
2   Charlie   22
3     David   32

Specific Row [1, 2]: Los Angeles

Filtered Data (Age > 25):
     Name  Age         City
1     Bob   27  Los Angeles
3   David   32      Houston

Cleaned Data (Removed NaN values):
       Name  Age         City
0     Alice   24     New York
1       Bob   27  Los Angeles
2   Charlie   22      Chicago

Filled Missing Values (Age = 20):
       Name  Age           City
0     Alice   24       New York
1       Bob   27    Los Angeles
2   Charlie   20        Chicago
3     David   32        Houston

Data with Duplicates Removed:
       Name  Age           City
0     Alice   24       New York
1       Bob   27    Los Angeles
2   Charlie   22        Chicago
3     David   32        Houston

Descriptive Statistics:
              Age
count   4.000000
mean   26.250000
std     4.604642
min    22.000000
25%    23.000000
50%    25.500000
75%    29.500000
max    32.000000

Mean Age:
 26.25

Grouped by City (Mean Age):
City
Chicago         22.0
Houston         32.0
Los Angeles     27.0
New York        24.0
Name: Age, dtype: float64

Merged DataFrame (on 'Name'):
       Name  Age_x           City
0     Alice     24       New York
1       Bob     27    Los Angeles

DataFrame saved to 'output.csv'
```

