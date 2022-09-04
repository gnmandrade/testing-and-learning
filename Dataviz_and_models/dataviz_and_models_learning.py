#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Numpy and Pandas
import numpy as np
import pandas as pd

# To get stocks data
import yfinance as yf

# For ploting
import matplotlib.pyplot as plt

# Statistical functions
from scipy import stats


# In[9]:


# Create standard random number generator
rng = np.random.default_rng()


# In[2]:


# Sample data
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]


# In[4]:


# Plot the sample data
plt.scatter(x,y)
plt.show()


# In[8]:


# Compute linear regression
slope, intercept, r, p, std_err = stats.linregress(x,y)

# Print the parameters
print(slope)
print(intercept)
print(r)
print(p)
print(std_err)


# In[6]:


# Get the model predictions
# Define function to apply the model
def lin_predictor_func(x):
    return slope * x + intercept

# Apply function to x data
y_predicted = list(map(lin_predictor_func,x))


# In[10]:


# Plot the data and the predictive trend line
plt.scatter(x,y)
plt.plot(x,y_predicted)
plt.show()


# In[17]:


# Generate random data
data_length = 100
x_test = rng.random(data_length)
y_test = 1.6*x_test + rng.random(data_length)


# In[19]:


plt.scatter(x_test,y_test)
plt.show()


# In[22]:


result = stats.linregress(x_test,y_test)
print(result.slope)
print(result.intercept)
print(result.stderr)


# In[29]:


def linear_function(x):
    return result.slope * x + result.intercept


# In[30]:


y_pred = list(map(linear_function,x_test))


# In[35]:


plt.plot(x_test,y_test,'o',label = 'Original Data')
plt.plot(x_test,y_pred,'r',label = 'Linear Regression')
plt.legend()
plt.show()

