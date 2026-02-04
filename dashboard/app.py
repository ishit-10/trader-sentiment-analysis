import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Trader Sentiment Dashboard",
    layout="wide",
)

# Load Data
@st.cache_data
def load_data():
    trades = pd.read_csv("../data/historical_data.csv")
    sentiment = pd.read_csv("../data/fear_greed_index.csv")

    # Parse timestamps
    trades["Timestamp IST"] = pd.to_datetime(trades["Timestamp IST"], errors="coerce")
    trades["date"] = pd.to_datetime(trades["Timestamp IST"].dt.date)

    sentiment["date"] = pd.to_datetime(sentiment["date"], errors="coerce")

    merged = trades.merge(sentiment, on="date", how="left")

    merged["win"] = (merged["Closed PnL"] > 0).astype(int)
    merged["Exposure"] = merged["Start Position"] * merged["Execution Price"]

    return merged

merged = load_data()

# Sidebar
st.sidebar.title("Filters")

sentiment_filter = st.sidebar.multiselect(
    "Sentiment",
    merged["classification"].dropna().unique(),
    default=list(merged["classification"].dropna().unique())
)

account_filter = st.sidebar.selectbox(
    "Account",
    ["All"] + list(merged["Account"].unique())
)

# Apply filters
filtered = merged[merged["classification"].isin(sentiment_filter)]
if account_filter != "All":
    filtered = filtered[filtered["Account"] == account_filter]

# Header
st.title("📊 Trader Sentiment Analysis Dashboard")

st.markdown("A one-screen overview of trading behavior across sentiment regimes.")

# KPIs
c1, c2, c3, c4 = st.columns(4)

c1.metric("Trades", f"{len(filtered):,}")
c2.metric("Win Rate", f"{filtered['win'].mean()*100:.1f}%")
c3.metric("Avg PnL", f"{filtered['Closed PnL'].mean():.2f}")
c4.metric("Avg Exposure", f"{filtered['Exposure'].mean():,.2f}")

# PnL & Exposure
col1, col2 = st.columns(2)

with col1:
    st.subheader("PnL by Sentiment")
    fig, ax = plt.subplots(figsize=(5,3))
    sns.boxplot(data=filtered, x="classification", y="Closed PnL", ax=ax)
    plt.xticks(rotation=45, fontsize=8)
    st.pyplot(fig)

with col2:
    st.subheader("Exposure (Leverage Proxy)")
    fig, ax = plt.subplots(figsize=(5,3))
    sns.boxplot(data=filtered, x="classification", y="Exposure", ax=ax)
    plt.xticks(rotation=45, fontsize=8)
    st.pyplot(fig)

# Long/Short & Frequency
col3, col4 = st.columns(2)

with col3:
    st.subheader("Long/Short Ratio")
    side_counts = filtered.groupby(["classification", "Side"]).size().unstack(fill_value=0)
    fig, ax = plt.subplots(figsize=(5,3))
    side_counts.plot(kind="bar", stacked=True, ax=ax)
    plt.xticks(rotation=45, fontsize=8)
    st.pyplot(fig)

with col4:
    st.subheader("Trade Frequency Over Time")
    freq = filtered.groupby(["date", "classification"]).size().reset_index(name="count")
    fig, ax = plt.subplots(figsize=(5,3))
    sns.lineplot(data=freq, x="date", y="count", hue="classification", marker="o", ax=ax)
    plt.xticks(rotation=45, fontsize=8)
    st.pyplot(fig)

# Data Preview
st.subheader("Data Preview (Top 20)")
st.dataframe(filtered.head(20), height=200)
