# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 15:42:47 2023

@author: rizal
"""

import pandas as pd

# file_name = pd.read_csv('file.csv') <---- format of read_csv

data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv',sep=';')

data.info()

#working with calculation
#defining variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberofItemsPurchased = 6

#Math Operations 
ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem
ProfitPerTransaction = NumberofItemsPurchased * ProfitPerItem
SellingPricePerTransaction = NumberofItemsPurchased * SellingPricePerItem

# CostPerTransaction Column Calculation
#CostPerTransaction = CostPerItem * NumberofItemsPurchased
# variable = dataframe['column_name']

CostPerItem = data['CostPerItem']
NumberofItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem*NumberofItemsPurchased


#Adding a new columnn to a dataframe
data['CostPerTransaction'] = CostPerTransaction

#Sales per Transaction
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']
data['Profit'] = data['SalesPerTransaction'] - data['CostPerTransaction']
data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction']) /data['CostPerTransaction']

#Rounding Markin

roundmarkup = round(data['Markup'],2)
data['Markup'] = round(data['Markup'],2)

#combining data fields
my_name = 'Dee'+'Naidoo'



my_date = 'day'+'-'+'Month'+'-'+'Year'
my_data = data['Day']+'-'

#checking columns data type
print(data['Day'].dtype)

#phyton columns type

day = data['Day'].astype(str)
year = data['Year'].astype(str)
print(day.dtype)
my_date = day+'-'+data['Month']+'-'+year
data['date'] = my_date

#using iloc to view specifics column

data.iloc[0:3]
data.head(5)
#new_var = column.str.split('sep' , expand = True)

split_col = data['ClientKeywords'].str.split(',' , expand=True)

#creating new columns for the split columns in Client Keywords
data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContract']= split_col[2]

#using the replace function
data['ClientAge'] = data['ClientAge'].str.replace('[','')
data['LengthofContract'] = data['LengthofContract'].str.replace(']','')

#using the lower function to change item to lowercase
data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files
#bringing in a new dataset

seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

#merging files: merge_df = pd.merge(df_old, df_new, on = 'key')

data = pd.merge(data,seasons, on = 'Month')

#dropping columns

#df = df.drop('columnname' , axis =1)

data = data.drop('ClientKeywords', axis = 1)
data = data.drop('Day', axis = 1)
data = data.drop(['Year','Month'], axis =1)

#Export into CSV

data.to_csv('ValueInc_Cleaned.csv', index = False)














