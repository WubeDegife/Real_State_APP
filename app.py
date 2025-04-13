import streamlit as st
import pandas as pd
import plotly.express as px

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("Sacramentorealestatetransactions.csv")
    df['sale_date'] = pd.to_datetime(df['sale_date'])
    df['price_per_sqft'] = df['price'] / df['sq__ft'].replace(0, pd.NA)
    return df.dropna(subset=['price_per_sqft'])

df = load_data()

# Sidebar Filters
st.sidebar.header("Filter Listings")
cities = df['city'].unique()
selected_cities = st.sidebar.multiselect("Select City", cities, default=cities[:5])
price_range = st.sidebar.slider("Price Range", int(df['price'].min()), int(df['price'].max()), (100000, 500000))
sqft_min, sqft_max = st.sidebar.slider("Square Footage", 0, int(df['sq__ft'].max()), (0, 3000))

# Apply filters
filtered_df = df[
    (df['city'].isin(selected_cities)) &
    (df['price'] >= price_range[0]) & (df['price'] <= price_range[1]) &
    (df['sq__ft'] >= sqft_min) & (df['sq__ft'] <= sqft_max)
]

# Tabs
tab1, tab2, tab3 = st.tabs(["🏠 Listings", "📈 Visualizations", "📥 Export"])

with tab1:
    st.subheader("Filtered Real Estate Listings")
    st.write(f"{len(filtered_df)} properties found")
    st.dataframe(filtered_df[['street', 'city', 'zip', 'price', 'sq__ft', 'beds', 'baths', 'type', 'price_per_sqft']])

with tab2:
    st.subheader("Price Distribution")
    fig1 = px.histogram(filtered_df, x='price', nbins=50, title="Price Distribution")
    st.plotly_chart(fig1)

    st.subheader("Average Price per City")
    avg_price_city = filtered_df.groupby('city')['price'].mean().reset_index()
    fig2 = px.bar(avg_price_city, x='city', y='price', title="Average Price per City")
    st.plotly_chart(fig2)

    st.subheader("Price per Sqft over Time")
    fig3 = px.scatter(filtered_df, x='sale_date', y='price_per_sqft', color='city', title="Price/Sqft Over Time")
    st.plotly_chart(fig3)

with tab3:
    st.subheader("Download Filtered Data")
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button("Download CSV", csv, "filtered_real_estate.csv", "text/csv")

