#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[22]:


pip install plotly seaborn


# In[2]:


# Load the dataset
df = pd.read_csv("sales_dataa.csv")


# In[3]:


# Convert 'Order Date' to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])


# In[4]:


# Extract Month for grouping
df['Month'] = df['Order Date'].dt.month_name()


# In[5]:


# Grouping sales by product
product_sales = df.groupby('Product')['Quantity Ordered'].sum()


# In[6]:


# Bar Chart - Total sales per product
product_sales.plot(kind='bar', title='Total Sales by Product', color='skyblue')
plt.xlabel('Product')
plt.ylabel('Quantity Sold')
plt.grid(True)
plt.show()


# In[7]:


# Line Chart - Monthly sales
monthly_sales = df.groupby('Month')['Quantity Ordered'].sum()
monthly_sales.plot(kind='line', marker='o', title='Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Quantity Sold')
plt.grid(True)
plt.show()


# In[8]:


# Pie Chart - Sales Distribution by Product
product_sales.plot(kind='pie', autopct='%1.1f%%', title='Sales Distribution by Product')
plt.ylabel('')
plt.show()


# In[9]:


# Scatter Plot - Quantity vs Price
plt.scatter(df['Quantity Ordered'], df['Price Each'], color='green')
plt.title('Quantity Ordered vs Price Each')
plt.xlabel('Quantity Ordered')
plt.ylabel('Price Each')
plt.grid(True)
plt.show()


# In[10]:


# Histogram - Quantity Distribution
df['Quantity Ordered'].plot(kind='hist', bins=20, title='Distribution of Order Quantities', color='orange')
plt.xlabel('Quantity Ordered')
plt.show()


# In[11]:


# Box Plot - Price Each distribution
df.boxplot(column='Price Each')
plt.title('Price Each Distribution')
plt.ylabel('Price Each')
plt.show()


# In[18]:


# Bubble Chart - Product vs Quantity (bubble size = Price Each)
plt.figure(figsize=(10,6))

# Group data to avoid too many overlapping points
bubble_data = df.groupby('Product')[['Quantity Ordered', 'Price Each']].mean().reset_index()

plt.scatter(
    bubble_data['Product'],
    bubble_data['Quantity Ordered'],
    s=bubble_data['Price Each'] * 10,  # bubble size
    alpha=0.6,
    color='purple'
)

plt.title('Bubble Chart: Avg Quantity vs Product (Bubble Size = Price)')
plt.xlabel('Product')
plt.ylabel('Average Quantity Ordered')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


# In[19]:


# Heatmap - Correlation between numeric columns
numeric_data = df[['Quantity Ordered', 'Price Each']].dropna()

plt.figure(figsize=(6,4))
sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm')
plt.title('Heatmap - Correlation')
plt.show()


# In[ ]:




