# -*- coding: utf-8 -*-
"""
Created on Mon May 27 21:07:54 2024

@author: dinse
"""

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("set1.xlsx")
df.head()
df.columns
df[df["Sport"] == 5]



#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)  

def generate_unique_row():
    return np.random.permutation([1, 2, 3, 4, 5])

data = [generate_unique_row() for _ in range(150)]
columns = ['Academic Subject', 'Music', 'Sport', 'Art&Culture', 'Food&Cuisine']

df = pd.DataFrame(data, columns=columns)

df[df["Sport"] == 5].sum()

# Histogram sport
plt.hist(df['Sport'], bins=5, edgecolor='black',color="green")
plt.title('Sport')
plt.xlabel('Point')
plt.ylabel('Frequency')
plt.xticks(range(1, 6))  
plt.show()

df.to_excel('survey_data.xlsx', index=False)


plt.hist(df['Music'], bins=5, edgecolor='black',color="orange")
plt.title('Music')
plt.xlabel('Point')
plt.ylabel('Frequency')
plt.xticks(range(1, 6))  
plt.show()


plt.hist(df['Academic Subject'], bins=5, edgecolor='black')
plt.title('Academic')
plt.xlabel('Point')
plt.ylabel('Frequency')
plt.xticks(range(1, 6)) 
plt.show()


plt.hist(df['Art&Culture'], bins=5, edgecolor='black',color="purple")
plt.title('Art&Culture')
plt.xlabel('Point')
plt.ylabel('Frequency')
plt.xticks(range(1, 6)) 
plt.show()


plt.hist(df['Food&Cuisine'], bins=5, edgecolor='black',color="pink")
plt.title('Food&Cuisine')
plt.xlabel('Point')
plt.ylabel('Frequency')
plt.xticks(range(1, 6)) 
plt.show()


music_counts = df['Music'].value_counts().sort_index()


plt.figure(figsize=(8, 8))
plt.pie(
    music_counts, 
    labels=music_counts.index, 
    autopct='%1.1f%%', 
    startangle=140, 
    wedgeprops={'edgecolor': 'white', 'linewidth': 2}
)
plt.title('Music Pie Graph')
plt.axis('equal')  
plt.show()


academic_counts = df['Academic Subject'].value_counts().sort_index()

plt.figure(figsize=(8, 8))
plt.pie(
    academic_counts, 
    labels=academic_counts.index, 
    autopct='%1.1f%%', 
    startangle=140, 
    wedgeprops={'edgecolor': 'white', 'linewidth': 2}
)
plt.title('Academic Pie Graph')
plt.axis('equal')  
plt.show()


sport_counts = df['Sport'].value_counts().sort_index()

plt.figure(figsize=(8, 8))
plt.pie(
    sport_counts, 
    labels=sport_counts.index, 
    autopct='%1.1f%%', 
    startangle=140, 
    wedgeprops={'edgecolor': 'white', 'linewidth': 2}
)
plt.title('Sport Pie Graph')
plt.axis('equal')  
plt.show()


Art_Culture_counts = df['Art&Culture'].value_counts().sort_index()

plt.figure(figsize=(8, 8))
plt.pie(
    Art_Culture_counts, 
    labels=Art_Culture_counts.index, 
    autopct='%1.1f%%', 
    startangle=140, 
    wedgeprops={'edgecolor': 'white', 'linewidth': 2}
)
plt.title('Art&Culture Pie Graph')
plt.axis('equal') 
plt.show()


Food_Cuisine_counts = df['Food&Cuisine'].value_counts().sort_index()

plt.figure(figsize=(8, 8))
plt.pie(
    Food_Cuisine_counts, 
    labels=Food_Cuisine_counts.index, 
    autopct='%1.1f%%', 
    startangle=140, 
    wedgeprops={'edgecolor': 'white', 'linewidth': 2}
)
plt.title('Food&Cuisine Pie Graph')
plt.axis('equal')
plt.show()
df

columns = df.columns
for column in columns:
    counts = df[column].value_counts().sort_index()
    print(f'\n{column} sütunu için puan dağılımları:\n{counts}')
    
#%%

distributions = {
    "Pop&HipHop": [35, 30, 24, 31, 30],
    "Rock": [34, 26, 25, 31, 34],
    "Arabesque": [31, 30, 33, 28, 28],
    "Classical": [29, 25, 35, 37, 24],
    "Turkish Folkloric Music": [21, 33, 27, 37, 32],
    "Cinema": [35, 30, 24, 31, 30],
    "Theatre": [34, 26, 25, 31, 34],
    "Opera": [31, 30, 33, 28, 28],
    "Dancing": [29, 25, 35, 37, 24],
    "Drawing": [21, 33, 27, 37, 32],
    "Industrial Engineering Core Courses": [35, 30, 24, 31, 30],
    "Foreign Language (English)": [34, 26, 25, 31, 34],
    "Software (Python or Java Script)": [31, 30, 33, 28, 28],
    "Mathematics": [29, 25, 35, 37, 24],
    "Pure Sciences": [21, 33, 27, 37, 32],
    "Football": [35, 30, 24, 31, 30],
    "Fitness": [34, 26, 25, 31, 34],
    "Basketball": [31, 30, 33, 28, 28],
    "Swimming": [29, 25, 35, 37, 24],
    "Athleticism": [21, 33, 27, 37, 32],
    "Italian": [35, 30, 24, 31, 30],
    "Mexican": [34, 26, 25, 31, 34],
    "Fast Food": [31, 30, 33, 28, 28],
    "Chinese": [29, 25, 35, 37, 24],
    "Desserts": [21, 33, 27, 37, 32],
    "Academic Subject": [29, 30, 26, 32, 33],
    "Music": [31, 33, 35, 27, 24],
    "Sport": [21, 30, 40, 22, 37],
    "Art&Culture": [29, 31, 26, 35, 29],
    "Food&Cuisine": [40, 26, 23, 34, 27],
}


percent_distributions = {key: [value / 150 * 100 for value in values] for key, values in distributions.items()}
df.columns

for category, values in distributions.items():
    percentages = percent_distributions[category]
    print(f"\n{category} sütunu için puan dağılımları:")
    for i, value in enumerate(values, 1):
        print(f"{i}    {value}    {percentages[i-1]:.2f}%")
        
(df["Academic Subject"].mean()/15
 +df["Music"].mean()/15
 +df["Sport"].mean()/15
 +df["Art&Culture"].mean()/15
 +df["Food&Cuisine"].mean()/15)