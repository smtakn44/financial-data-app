import yfinance as yf
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Sayfa başlığını ayarlayın
st.title("Financial Data App ")

# Sidebar'ı oluşturun
st.sidebar.header("User Input")

# Şirket ve finansal enstrüman seçeneklerini belirtin
options = ["AAPL", "GOOGL", "MSFT", "NVDA", "TSLA", "AMZN", "FB", "NFLX", "GLD", "BTC-USD", "ETH-USD", "SI=F"]

# Kullanıcının enstrüman türünü seçmesini isteyin
selected_option = st.sidebar.multiselect("Select Financial Instrument(s):", options, default=["TSLA"])

# Tarih aralığını seçeneklerini belirtin
date_range_options = ["7d", "1m", "1y", "3y", "5y", "10y", "20y", "30y"]

# Kullanıcının tarih aralığını seçmesini isteyin
selected_date_range = st.sidebar.selectbox("Select Date Range:", date_range_options, index=2)

# Bugünün tarihini ayarlayın
today = datetime(2023, 9, 19)

# Kullanıcının özel tarih seçeneğini belirtin
if selected_date_range == "Custom":
    custom_start_date = st.sidebar.date_input("Start Date:", today - timedelta(days=365))
    custom_end_date = st.sidebar.date_input("End Date:", today)
else:
    # Seçilen tarih aralığına göre başlangıç ve bitiş tarihlerini hesaplayın
    if selected_date_range == "7d":
        start_date = today - timedelta(days=7)
    elif selected_date_range == "1m":
        start_date = today - timedelta(days=30)
    elif selected_date_range == "1y":
        start_date = today - timedelta(days=365)
    elif selected_date_range == "3y":
        start_date = today - timedelta(days=365 * 3)
    elif selected_date_range == "5y":
        start_date = today - timedelta(days=365 * 5)
    elif selected_date_range == "10y":
        start_date = today - timedelta(days=365 * 10)
    elif selected_date_range == "20y":
        start_date = today - timedelta(days=365 * 20)
    elif selected_date_range == "30y":
        start_date = today - timedelta(days=365 * 30)

    custom_start_date = start_date
    custom_end_date = today

if selected_option:
    data = pd.DataFrame()

    # Seçilen enstrümanlar için verileri alın
    for instrument in selected_option:
        if instrument in ["GLD", "BTC-USD", "ETH-USD", "SI=F"]:
            ticker_data = yf.download(instrument, start=custom_start_date, end=custom_end_date)
            data[instrument] = ticker_data['Close']
        else:
            ticker_data = yf.download(instrument, start=custom_start_date, end=custom_end_date)
            data[instrument] = ticker_data['Close']

    # Seçilen enstrümanların kapanış fiyatı grafiklerini gösterin
    st.write(
        """
        ## Closing Prices
        """
    )
    st.line_chart(data)
