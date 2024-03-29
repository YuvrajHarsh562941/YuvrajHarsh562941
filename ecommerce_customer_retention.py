# -*- coding: utf-8 -*-
"""Ecommerce Customer Retention.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/189vGqhjHTdYHaaRt3FkJL5NKFZIO8Rxj
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

!pip install openpyxl

df=pd.read_excel('/content/E-commerce.xlsx')
df.head(10)

pd.set_option("display.max_columns",None)
pd.set_option("display.max_rows", None)

from string import digits

#Removing tab spaces
df.columns = df.columns.str.replace('\t','')

#Removing digits
remove_digits = str.maketrans('', '', digits)
df.columns = df.columns.str.translate(remove_digits)

#Removing leading and trailling spaces
df.columns = df.columns.str.strip()

df.head()

df.shape

df.dtypes

df.isnull().sum().any()

df.nunique()

personal_info=['Gender of respondent','How old are you?','Which city do you shop online from?',
               'What is the Pin Code of where you shop online from?','Since How Long You are Shopping Online ?',
                   'How many times you have made an online purchase in the past  year?']

for i in personal_info:
    if i!='What is the Pin Code of where you shop online from?':
        plt.figure(figsize=(6,5))
        df[i].value_counts().plot.pie(autopct='%1.1f%%')
        centre=plt.Circle((0,0),0.7,fc='white')
        fig=plt.gcf()
        fig.gca().add_artist(centre)
        plt.xlabel(i)
        plt.ylabel('')
        plt.figure()

#Analysis on Various Factors

"""Intention Of Repeat Purchase

"""

#Resolving ambiguity of column
#Changing 42 times and above to 41 times and above
df['How many times you have made an online purchase in the past  year?'].replace('42 times and above','41 times and above',
                                                                                inplace=True)

plt.figure(figsize=(12,5))
sns.lineplot(df['How many times you have made an online purchase in the past  year?'])

dict={'31-40 times':35,'41 times and above':45,'Less than 10 times':5,'11-20 times':15,'21-30 times':25}
df['Average times made an online purchase']=df['How many times you have made an online purchase in the past  year?'].replace(dict)

plt.figure(figsize=(10,5))
sns.violinplot(
               df['Average times made an online purchase'])
plt.xticks(rotation=45)







performance=['Easy to use website or application',
       'Visual appealing web-page layout', 'Wild variety of product on offer',
       'Complete, relevant description information of products',
       'Fast loading website speed of website and application',
       'Reliability of the website or application',
       'Quickness to complete purchase',
       'Availability of several payment options', 'Speedy order delivery',
       'Privacy of customers’ information',
       'Security of customer financial information',
       'Perceived Trustworthiness',
       'Presence of online assistance through multi-channel']

for i in performance:
        plt.figure(figsize=(8,6))
        df[i].value_counts().plot.pie(autopct='%1.1f%%')
        centre=plt.Circle((0,0),0.7,fc='white')
        fig=plt.gcf()
        fig.gca().add_artist(centre)
        plt.xlabel(i)
        plt.ylabel('')
        plt.figure()

plt.figure(figsize=(5,4))
sns.stripplot(
              df['From the following, tick any (or all) of the online retailers you have shopped from;'])

plt.figure(figsize=(5,4))
sns.stripplot(df['Why did you abandon the “Bag”, “Shopping Cart”?'])