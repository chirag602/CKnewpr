import pandas as pd

file_path = ()

df = pd.read_excel(r"C:\Users\DELL\PycharmProjects\streamlitpro\african_crises.xlsx")

print(df.head())

import streamlit as st
import plotly.express as px

# Sample economic data for African countries
def get_sample_data():
    data = {
        'Country': ['Nigeria', 'South Africa', 'Kenya', 'Egypt', 'Ghana'],
        'GDP (Billion USD)': [432, 388, 95, 404, 77],
        'Inflation (%)': [15.6, 5.4, 7.2, 6.8, 10.3],
        'Trade Balance (Billion USD)': [-20, 5, -8, 10, -3],
    }
    return pd.DataFrame(data)

df = get_sample_data()

# Streamlit App Layout
st.set_page_config(page_title="African Economy Dashboard", layout="wide")
st.title("🌍 African Economy Dashboard")
st.sidebar.header("🔍 Filter Options")

# Country selection
selected_countries = st.sidebar.multiselect("Select Countries", df['Country'].unique(), default=df['Country'].unique())
filtered_df = df[df['Country'].isin(selected_countries)]

# GDP Visualization
st.subheader("📊 GDP Comparison")
fig_gdp = px.bar(filtered_df, x='Country', y='GDP (Billion USD)', color='Country', title='GDP by Country')
st.plotly_chart(fig_gdp, use_container_width=True)

# Inflation Visualization
st.subheader("📈 Inflation Rates")
fig_inflation = px.line(filtered_df, x='Country', y='Inflation (%)', markers=True, title='Inflation Rate by Country')
st.plotly_chart(fig_inflation, use_container_width=True)

# Trade Balance Visualization
st.subheader("📉 Trade Balance")
fig_trade = px.bar(filtered_df, x='Country', y='Trade Balance (Billion USD)', color='Country', title='Trade Balance by Country')
st.plotly_chart(fig_trade, use_container_width=True)

# Insights Section
st.write("## Key Insights")
st.write("- **Nigeria** has the highest GDP but faces a significant trade deficit.")
st.write("- **South Africa** shows a positive trade balance.")
st.write("- Inflation rates vary significantly across the countries.")

st.sidebar.write("📧 For more information, contact: info@africaeconomy.com")



