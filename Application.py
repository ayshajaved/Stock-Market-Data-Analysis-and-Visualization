import streamlit as st #streamlit for the frontend of the web application
import pandas as pd    #Pandas for the data analysis and using datetime

class Application:
    def __init__(self):
        st.title("Stock Market Data Analysis and Visualization")            #setting title on the web page
        st.text_input("Enter the Stock Ticker: ")                           #Input for the ticker eg(AAPL, MSFT, NVDA)
        st.date_input("Enter the Start Date: ",pd.to_datetime("01-01-2010"))#Input for the start date to analyze
        st.date_input("Enter the End Date: ",pd.to_datetime("01-01-2015"))  #Input for the start date to analyze
                