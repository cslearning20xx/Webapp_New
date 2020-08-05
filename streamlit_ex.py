# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 19:28:50 2020

@author: 91998
"""



import yfinance as yf
import streamlit as st
import pandas as pd

st.write( """ 
         
         # Simple stock Price App
         
         """)

st.sidebar.title("Choose stock")
tickersymbol =st.sidebar.selectbox( "Select stock", ['AAPL', 'GOOGL'])
#tickersymbol = 'GOOGL'

tickerData = yf.Ticker(tickersymbol)

tickerDf = tickerData.history( period = '1d', start = '2010-5-31', end = '2020-5-31')

st.line_chart(tickerDf.Close)                              
st.line_chart(tickerDf.Volume)                              
