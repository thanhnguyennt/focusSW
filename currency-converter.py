import streamlit as st
import requests

st.title("Currency Converter")
st.sidebar.header("Settings")


APP_ID = '0cd3669d811c4b59b8a0723717063186'  #from Open Exchange Rates

# API URL for latest exchange rates
base_url = 'https://open.er-api.com/v6/latest'


def convert_currency(amount, from_currency, to_currency):
    params = {'app_id': APP_ID, 'base': from_currency}
    response = requests.get(base_url, params=params)
    data = response.json()
    exchange_rate = data['rates'][to_currency]
    converted_amount = amount * exchange_rate
    return converted_amount


amount = st.sidebar.number_input("Enter amount to convert", min_value=0.01, step=0.01)
from_currency = st.sidebar.selectbox("From Currency", ["USD", "EUR", "GBP", "JPY", "CAD", "AUD", "CHF", "CNY", "SEK", "NZD", "KRW", "VND"])  
to_currency = st.sidebar.selectbox("To Currency", ["USD", "EUR", "GBP", "JPY", "CAD", "AUD", "CHF", "CNY", "SEK", "NZD", "KRW", "VND"])  


if st.sidebar.button("Convert"):
    result = convert_currency(amount, from_currency, to_currency)
    st.write(f"{amount} {from_currency} = {result:.2f} {to_currency}")
