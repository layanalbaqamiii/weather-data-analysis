#Import required libraries
import pandas as pd

#Load the weather dataset
data = pd.read_csv("C:/Users/Lenovo/Desktop/project/python-weather-data-analysis-project/Weather Data.csv")

#Display the first few rows of the dataset
print("\nFirst 5 Rows of the Dataset:")
print(data.head())

#Show the shape of the dataset (rows, columns)
print("\nDataset Shape (Rows, Columns):")
print(data.shape)

#Show the index range of the dataset
print("\nDataset Index:")
print(data.index)

#Show the column names
print("\nColumn Names:")
print(data.columns)

#Display the data types of each column
print("\nData Types of Columns:")
print(data.dtypes)

#Unique weather conditions in the data
print("\nUnique Weather Conditions:")
print(data['Weather'].unique())

#Number of unique values in each column
print("\nNumber of Unique Values per Column:")
print(data.nunique())

#Count of non-null values in each column
print("\nCount of Non-Null Entries per Column:")
print(data.count())

#Frequency of each weather condition
print("\nFrequency of Each Weather Type:")
print(data['Weather'].value_counts())

#General information about the dataset
print("\nDataset Info:")
print(data.info())

#All unique wind speed values
print("\nUnique Wind Speed Values:")
print(data['Wind Speed_km/h'].unique())

#Number of times weather was exactly "Clear"
print("\nRecords Where Weather is Exactly 'Clear':")
print(data[data['Weather'] == 'Clear'])

#Number of times wind speed was exactly 4 km/h
print("\nRecords with Wind Speed Exactly 4 km/h:")
print(data[data['Wind Speed_km/h'] == 4])

#Checking for missing values
print("\nMissing Values in Dataset:")
print(data.isnull().sum())

#Checking for non-missing values
print("\nNon-Missing Values per Column:")
print(data.notnull().sum())

#Renaming 'Weather' column to 'Weather Condition'
data.rename(columns={'Weather': 'Weather Condition'}, inplace=True)
print("\nRenamed 'Weather' to 'Weather Condition':")
print(data.columns)

#Average visibility
print("\nAverage Visibility (km):")
print(data['Visibility_km'].mean())

# 📈 Standard deviation of pressure
print("\n🔹 Standard Deviation of Pressure (kPa):")
print(data['Press_kPa'].std())

#Variance of relative humidity
print("\nVariance of Relative Humidity (%):")
print(data['Rel Hum_%'].var())

#All records where snow is mentioned in weather condition
print("\nAll Records With 'Snow' in Weather Condition:")
print(data[data['Weather Condition'].str.contains('Snow')])

#Records with wind speed > 24 km/h and visibility = 25 km
print("\nRecords Where Wind Speed > 24 km/h AND Visibility = 25 km:")
print(data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)])

#Mean value of each column per weather condition
print("\nMean of Each Column by Weather Condition:")
print(data.groupby('Weather Condition').mean(numeric_only=True))

#Minimum values per weather condition
print("\nMinimum Values by Weather Condition:")
print(data.groupby('Weather Condition').min())

#Maximum values per weather condition
print("\nMaximum Values by Weather Condition:")
print(data.groupby('Weather Condition').max())

#Show all records where weather is 'Fog'
print("\nAll Records Where Weather is 'Fog':")
print(data[data['Weather Condition'] == 'Fog'])

#Records where weather is 'Clear' or visibility > 40
print("\nRecords Where Weather is 'Clear' OR Visibility > 40:")
print(data[(data['Weather Condition'] == 'Clear') | (data['Visibility_km'] > 40)])

#Complex condition with AND/OR logic
print("\nRecords Where (Weather is 'Clear' AND Humidity > 50%) OR Visibility > 40:")
print(data[(data['Weather Condition'] == 'Clear') & (data['Rel Hum_%'] > 50) | (data['Visibility_km'] > 40)])
