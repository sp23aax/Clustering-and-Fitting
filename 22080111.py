# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 10:41:07 2024

@author: Saikiran
"""
#Importing required librarries
import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have a DataFrame with relevant data
data = {
    'Country': ['USA', 'China', 'India'],
    'GDP_per_Capita': [60000, 10000, 2000],
    'CO2_per_Capita': [15, 8, 2],
    'CO2_per_GDP': [0.3, 0.8, 0.5],
    'Energy_Sector': [70, 20, 10],
    'Transportation_Sector': [20, 30, 40],
    'Industrial_Sector': [10, 50, 50]
}

df = pd.DataFrame(data)

# Print the DataFrame
print("Original DataFrame:")
print(df)

# Plotting GDP per Capita
plt.figure(figsize=(10, 6))
plt.bar(df['Country'], df['GDP_per_Capita'], color=['blue', 'orange', 'green'])
plt.title('GDP per Capita')
plt.xlabel('Country')
plt.ylabel('GDP per Capita (USD)')
plt.show()

# Plotting CO2 per Capita
plt.figure(figsize=(10, 6))
plt.bar(df['Country'], df['CO2_per_Capita'], color=['blue', 'orange', 'green'])
plt.title('CO2 per Capita')
plt.xlabel('Country')
plt.ylabel('CO2 per Capita (tons)')
plt.show()

# Plotting CO2 per GDP
plt.figure(figsize=(10, 6))
plt.bar(df['Country'], df['CO2_per_GDP'], color=['blue', 'orange', 'green'])
plt.title('CO2 per GDP')
plt.xlabel('Country')
plt.ylabel('CO2 per $ of GDP')
plt.show()

# Plotting Fraction of Sectors
plt.figure(figsize=(10, 6))
plt.bar(df['Country'], df['Energy_Sector'], label='Energy', color='blue')
plt.bar(df['Country'], df['Transportation_Sector'], label='Transportation', color='orange', bottom=df['Energy_Sector'])
plt.bar(df['Country'], df['Industrial_Sector'], label='Industrial', color='green', bottom=df['Energy_Sector'] + df['Transportation_Sector'])
plt.title('Fraction of Sectors Contributing to CO2 Emissions')
plt.xlabel('Country')
plt.ylabel('Percentage of Total Emissions')
plt.legend()
plt.show()