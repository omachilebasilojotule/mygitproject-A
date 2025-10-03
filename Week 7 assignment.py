
#iris_analysis.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

#Load Iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target
df['species'] = df['species'].map({i: name for i, name in enumerate(iris.target_names)})

#Display first 5 rows
print("Head of the dataset:")
print(df.head())

#Data types and missing values
print("\nData Info:")
print(df.info())

#Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

#Basic statistics
print("\nStatistical Summary:")
print(df.describe())

#Group by species and get mean of each feature
print("\nMean values per species:")
print(df.groupby('species').mean())

#Findings
print("\nObservation:")
print("Different species have distinguishable petal sizes. 'Setosa' species shows smallest petal dimensions.")

#Visualizations
sns.set(style='whitegrid')

plt.plot(df.index, df['petal length (cm)'], label='Petal Length')
plt.title('Petal Length over Index')
plt.xlabel('Index')
plt.ylabel('Length (cm)')
plt.legend()
plt.tight_layout()
plt.show()

# Bar chart: Avg petal length per species
df.groupby('species')['petal length (cm)'].mean().plot(kind='bar', title='Avg Petal Length per Species')
plt.ylabel('Petal Length (cm)')
plt.tight_layout()
plt.show()

#Histogram: Sepal length distribution
df['sepal length (cm)'].plot(kind='hist', bins=15, title='Sepal Length Distribution')
plt.xlabel('Sepal Length (cm)')
plt.tight_layout()
plt.show()

#Scatter plot: Sepal vs Petal length
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df)
plt.title('Sepal Length vs Petal Length')
plt.tight_layout()
plt.show()