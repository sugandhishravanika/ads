# -*- coding: utf-8 -*-
"""C.I.E=||

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15vRCYh2WaXiX4on-Jm4fpTZ9bhKevs7k
"""

import pandas as pd
data=pd.read_csv("/content/titanic (2).csv")
print(data)

data.describe()

import numpy as np
from scipy import stats
mean=np.mean(data['Age'])
median=np.median(data['Age'])
mode=stats.mode(data['Age'],keepdims=True).mode[0]
mean1=np.mean(data['Fare'])
median1=np.median(data['Fare'])
mode1=stats.mode(data['Fare'],keepdims=True).mode[0]
print("Central Tendence")
print("mean Age:",mean)
print("median Age:",median)
print("mode:",mode)
print("mean Fare:",mean1)
print("median Fare:",median1)
print("mode Fare:",mode1)

import pandas as pd
data['Survived']=data['Survived'].replace({1:'survived',0:'not survived'})
print(data['Survived'])

import numpy as np
import matplotlib.pyplot as plt
grouped_data=data.groupby(['Survived','Pclass'])['PassengerId'].count().unstack()
grouped_data.plot(kind='bar',)
plt.title('survied')
plt.xlabel('survived')
plt.ylabel('not survied')
plt.xticks(ticks=[0,1],labels=['survied','not survied'],rotation=0)
plt.show()

import pandas as pd
ur1 = '/content/titanic (2).csv'
titanic_data = pd.read_csv(ur1)
print(titanic_data)
null_values = titanic_data.isnull().sum()
titanic_filled_data = titanic_data.fillna(titanic_data.mean(numeric_only=True))

import pandas as pd
import numpy as np
data = pd.read_csv("/content/titanic (2).csv")

mean = np.mean(data['Age'])
std = np.std(data['Age'])
print('mean of the dataset is', mean)
print('std. deviation is', std)
threshold = 3
outlier = []

for i in data['Age']:
    z = (i-mean)/std
    if z > threshold:
        outlier.append(i)
print('outlier in dataset is', outlier)

import seaborn as sns
sns.boxplot(data['Age'])