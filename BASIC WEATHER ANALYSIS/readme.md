
# Weather Data Analysis

This project demonstrates basic weather data analysis using Python libraries such as **Pandas**, **NumPy**, and **Matplotlib**. The data consists of randomly generated temperature and humidity values over a span of 10 days. The project includes data visualization using line and bar charts to analyze temperature trends and humidity patterns.

## Features
- **Temperature Trend**: A line plot showing temperature changes over the days.
- **Humidity Analysis**: A bar chart visualizing humidity levels on each date.
- **Basic Data Analysis**: Calculation of mean temperature and mean humidity.

## Prerequisites
To run this project, you will need to have the following libraries installed:

- **NumPy**
- **Matplotlib**
- **Pandas**

You can install these dependencies using pip if you don't already have them:

```bash
pip install numpy matplotlib pandas
```

## Code Walkthrough

### 1. **Creating Dummy Weather Data**

We create a dictionary with date, temperature, and humidity data. The `date` is generated using `pandas.date_range()`, and random temperature and humidity values are generated using `numpy.random.randint()`.

```python
data = {
    "date": pd.date_range(start="2024-11-01", periods=10),
    "Temperature (C)": np.random.randint(15, 30, 10),
    "Humidity (%)": np.random.randint(30, 90, 10)
}
```

### 2. **DataFrame Creation**

We then convert this dictionary into a `pandas.DataFrame` for easy manipulation and analysis.

```python
df = pd.DataFrame(data)
```

### 3. **Mean Calculation**

We calculate the mean values for temperature and humidity using `numpy.mean()`.

```python
mean_temp = np.mean(df["Temperature (C)"])
mean_humidity = np.mean(df["Humidity (%)"])
```

### 4. **Data Visualization**

#### **Temperature Trend Line Plot**

We plot the temperature trend using a line plot with `matplotlib.pyplot.plot()`.

```python
plt.plot(df['date'], df["Temperature (C)"], label="Temperature trend", color="red", marker="o")
```

#### **Humidity Analysis Bar Chart**

We plot the humidity data using a bar chart with `matplotlib.pyplot.bar()`.

```python
plt.bar(df['date'], df['Humidity (%)'])
```

### 5. **Displaying the Plots**

We use `plt.show()` to display both plots.

## Output

- **Temperature Trend Line Plot**: Shows the changes in temperature across 10 days.
- **Humidity Bar Chart**: Displays humidity levels for each corresponding date.

## Example Output

### Temperature Trend:
A line plot with dates on the x-axis and temperature in Celsius on the y-axis, showing temperature variations over the given period.

### Humidity Analysis:
A bar chart with dates on the x-axis and humidity percentage on the y-axis, representing daily humidity levels.

## Conclusion

This project showcases basic data handling, analysis, and visualization using **Pandas**, **NumPy**, and **Matplotlib**. It is an example of how to process and present weather data for better understanding and decision-making.
