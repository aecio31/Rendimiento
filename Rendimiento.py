#!/usr/bin/env python
# coding: utf-8

# In[11]:


import yfinance as yf
from scipy.integrate import quad

# Función para calcular el rendimiento R(T, dt) con datos reales
def calculate_return(ticket_data, delta_t):
    returns = np.log(ticket_data['Close'].pct_change() + 1)
    return np.sum(returns) * delta_t

# Función para calcular el producto punto del rendimiento con datos reales
def calculate_dot_product(T, ticket_data):
    delta_t = T / len(ticket_data)
    
    # Función de rendimiento R(T, dt)
    def performance(t):
        index = int(t / T * len(ticket_data))
        return calculate_return(ticket_data[:index+1], delta_t)
    
    # Calcular la integral numérica
    dot_product, _ = quad(performance, 0, T)
    
    return dot_product / T

# Descargar datos históricos de Tesla desde Yahoo Finance
ticker_symbol = 'TSLA'
start_date = '2023-10-12'
end_date = '2023-10-24'  # Una semana antes

ticket_data = yf.download(ticker_symbol, start=start_date, end=end_date)

# Parámetros de la simulación
T = 1.0  # Tiempo total

# Calcular el producto punto del rendimiento con datos reales
result = calculate_dot_product(T, ticket_data)

print(f"Producto punto del rendimiento: {result}")


# In[3]:


import yfinance as yf


# In[4]:


from scipy.integrate import quad


# In[5]:


import numpy as np


# In[21]:


# Función para calcular el rendimiento R(T, dt) con datos reales
def calculate_return(ticket_data, delta_t):
    returns = np.log(ticket_data['Close'].pct_change() + 1)
    return np.sum(returns) * delta_t

# Función para calcular el producto punto del rendimiento con datos reales
def calculate_dot_product(T, ticket_data):
    delta_t = T / len(ticket_data)
    
    # Función de rendimiento R(T, dt)
    def performance(t):
        index = int(t / T * len(ticket_data))
        return calculate_return(ticket_data[:index+1], delta_t)
    
    # Calcular la integral numérica
    dot_product, _ = quad(performance, 0, T)
    
    return dot_product / T

# Descargar datos históricos de Tesla desde Yahoo Finance
ticker_symbol = 'TSLA'
start_date = '2023-10-9'
end_date = '2023-10-24'  # Una semana antes

ticket_data = yf.download(ticker_symbol, start=start_date, end=end_date)

# Parámetros de la simulación
T =10 # Tiempo total

# Calcular el producto punto del rendimiento con datos reales
result = calculate_dot_product(T, ticket_data)

print(f"Producto punto del rendimiento: {result}")


# In[ ]:




