import streamlit as st
import requests
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image

image = Image.open('Image/logo.png')
st.image(image, width=390)

st.title("Currency Converter")
st.sidebar.header("Settings")

APP_ID = '0cd3669d811c4b59b8a0723717063186'  #from Open Exchange Rates
base_url = 'https://open.er-api.com/v6/latest'

def convert_currency(amount, from_currency, to_currency):
    params = {'app_id': APP_ID, 'base': from_currency}
    response = requests.get(base_url, params=params)
    data = response.json()
    exchange_rate = data['rates'][to_currency]
    converted_amount = amount * exchange_rate
    return converted_amount, data['rates']

amount = st.sidebar.number_input("Enter amount to convert", min_value=0.01, step=0.01)
from_currency = st.sidebar.selectbox("From Currency", ["USD", "EUR", "GBP", "JPY", "CAD", "AUD", "CHF", "CNY", "SEK", "NZD", "KRW", "VND"])  
to_currency = st.sidebar.selectbox("To Currency", ["USD", "EUR", "GBP", "JPY", "CAD", "AUD", "CHF", "CNY", "SEK", "NZD", "KRW", "VND"])  

if st.sidebar.button("Convert"):
    result, rates = convert_currency(amount, from_currency, to_currency)
    st.write(f"{amount} {from_currency} = {result:.2f} {to_currency}")

    # Create a DataFrame for selected currencies' exchange rates
    df = pd.DataFrame(rates.items(), columns=['Currency', 'Rate'])
    df = df[(df['Currency'] == from_currency) | (df['Currency'] == to_currency)]
 

    # Plot exchange rates 
    fig, ax = plt.subplots()
    df.plot(kind='bar', x='Currency', y='Rate', ax=ax, color=['blue', 'green'])
    plt.title(f'Exchange Rates: {from_currency} to {to_currency}')
    plt.xlabel('Currency')
    plt.ylabel('Exchange Rate')
    st.pyplot(fig)
