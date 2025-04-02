import streamlit as st
import Funciones as MCF
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt #Visualizacion de datos
import yfinance as yf #Api de Yahoo Finanzas
from scipy.stats import kurtosis, skew, shapiro ,norm,t #Funciones estadísticas
from datetime import date

ticker = "NVDA"
st.title(f'Análisis del activo {ticker} desde 2010')

st.header('Visualización de datos')


with st.spinner('Descargando data...'):
    df_precios = MCF.obtener_datos(ticker)
    df_rendimientos = MCF.calcular_rendimientos_Log(df_precios)

#Datos inciso b)

st.subheader(f"Gráfico de precio: {ticker}")

fig,ax = plt.subplots(figsize = (10,5))
ax.plot(df_precios.index,df_precios)
ax.axhline(y = 0,linestyle = '-',alpha = 0.7)
ax.set_xlabel("Fecha")
ax.set_ylabel("Precio Diario")
st.pyplot(fig)

st.subheader("Medidas de los rendimientos logarítmicos diarios")

promedio_rendi_diario = df_rendimientos.mean()
kurtosis = kurtosis(df_rendimientos)
skew = skew(df_rendimientos)
col1,col2,col3 = st.columns(3)

col1.metric("Rendimiento Medio Diario", f"{promedio_rendi_diario:.4%}")
col2.metric("Kurtosis",f"{kurtosis:.4}")
col3.metric("Sesgo",f"{skew:.3}")


st.subheader(f'Gráfico de Rendimientos : {ticker}')

fig,ax = plt.subplots(figsize = (10,5))
ax.plot(df_rendimientos.index,df_rendimientos)
ax.axhline(y = 0,linestyle = '-',alpha = 0.7)
ax.set_xlabel("Fecha")
ax.set_ylabel("Rendimiento Diario")
st.pyplot(fig)

 # Histograma 
st.subheader(f'Histograma de Rendimientos : {ticker}')
fig,ax = plt.subplots(figsize =(10,5))
ax.hist(df_rendimientos,bins=50,alpha=0.5,color = 'green')
ax.set_title('Histograma')
ax.set_xlabel('Rendimiento Diario')
ax.set_ylabel('Frecuencia')
st.pyplot(fig)

#VaR y ES inciso c)

