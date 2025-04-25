# 🌦️ Weather Data Analysis with Pandas

This project is a data analysis script written in Python using the **pandas** library.

It performs a series of **data exploration** and **filtering operations** on a weather dataset.

---

## 📊 Dataset

The dataset used is from **Kaggle**, saved as a file named `Weather Data.csv`.  
It contains hourly weather observations including temperature, humidity, visibility, wind speed, and more.

---

## 🔍 What This Script Does

- Displays basic dataset info (shape, columns, dtypes, unique values, nulls)
- Finds:
  - All unique weather types
  - Instances of specific weather conditions (like "Clear", "Snow", etc.)
  - When wind speed = 4 km/h
  - When wind speed > 24 km/h & visibility = 25
- Calculates:
  - Mean visibility
  - Std dev of pressure
  - Variance of humidity
- Filters based on conditions:
  - Weather is "Clear"
  - Visibility > 40
  - Weather is "Fog" and more

---

## 📁 Project Structure

weather-data-analysis/
├── Weather Data.csv
└── weather-data-analysis-project.py

---

## 🛠 Tools Used

- Python
- pandas
- IDE: Spyder 




