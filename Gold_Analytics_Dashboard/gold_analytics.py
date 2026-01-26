# -------------------------------------------------
# 1. Import required libraries
# -------------------------------------------------
import streamlit as st
import pandas as pd


# -------------------------------------------------
# 2. Page configuration
# -------------------------------------------------
st.set_page_config(
    page_title="Chennai Gold Price Dashboard",
    page_icon="🪙",
    layout="wide"
)


# -------------------------------------------------
# 3. App title and description
# -------------------------------------------------
st.title("🪙 Chennai 22K Gold Price Dashboard")
st.caption("Estimated monthly gold prices (₹ per gram)")


# -------------------------------------------------
# 4. Load and prepare data
# -------------------------------------------------
@st.cache_data
def load_data():
    # Read Excel file (pandas uses openpyxl internally)
    df = pd.read_excel(
        "Chennai_22K_Gold_Price_Mar2025_to_Mar2026.xlsx"
    )

    # Convert Month column (e.g., 'Mar 2025') to datetime
    df["Date"] = pd.to_datetime(df["Month"], format="%b %Y")

    # Extract Year and Month name for filtering
    df["Year"] = df["Date"].dt.year
    df["Month_Name"] = df["Date"].dt.strftime("%b")

    return df


df = load_data()


# -------------------------------------------------
# 5. Sidebar – Year + Month dropdown filter
# -------------------------------------------------
st.sidebar.header("📅 Filter by Year & Month")

# Available years and months
years = sorted(df["Year"].unique())
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Start period selection
start_year = st.sidebar.selectbox(
    "Start Year",
    years,
    index=0
)

start_month = st.sidebar.selectbox(
    "Start Month",
    months,
    index=months.index(df.iloc[0]["Month_Name"])
)

# End period selection
end_year = st.sidebar.selectbox(
    "End Year",
    years,
    index=len(years) - 1
)

end_month = st.sidebar.selectbox(
    "End Month",
    months,
    index=months.index(df.iloc[-1]["Month_Name"])
)


# -------------------------------------------------
# 6. Convert selected Year + Month to date range
# -------------------------------------------------
start_date = pd.to_datetime(f"{start_month} {start_year}")
end_date = pd.to_datetime(f"{end_month} {end_year}")


# -------------------------------------------------
# 7. Validate selection and filter data
# -------------------------------------------------
if start_date > end_date:
    st.warning("⚠️ Start period must be earlier than or equal to end period.")
    filtered_df = df.iloc[0:0]  # empty DataFrame
else:
    filtered_df = df[
        (df["Date"] >= start_date) &
        (df["Date"] <= end_date)
    ]


# -------------------------------------------------
# 8. Clean data for display
# -------------------------------------------------
display_df = filtered_df.drop(
    columns=["Date", "Year", "Month_Name"]
)


# -------------------------------------------------
# 9. Show selected period
# -------------------------------------------------
if not display_df.empty:
    st.markdown(
        f"**Showing data from _{display_df.iloc[0]['Month']}_ "
        f"to _{display_df.iloc[-1]['Month']}_**"
    )

st.divider()


# -------------------------------------------------
# 10. KPI metrics
# -------------------------------------------------
col1, col2, col3 = st.columns(3)

if not display_df.empty:
    col1.metric(
        "📉 Minimum Price",
        f"₹{display_df['Estimated 22K Gold Price (₹/gram)'].min():,.0f}"
    )

    col2.metric(
        "📊 Average Price",
        f"₹{display_df['Estimated 22K Gold Price (₹/gram)'].mean():,.0f}"
    )

    col3.metric(
        "📈 Maximum Price",
        f"₹{display_df['Estimated 22K Gold Price (₹/gram)'].max():,.0f}"
    )

st.divider()


# -------------------------------------------------
# 11. Data table
# -------------------------------------------------
st.subheader("📄 Monthly Gold Price Table")

st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True
)


# -------------------------------------------------
# 12. Line chart
# -------------------------------------------------
st.subheader("📈 Gold Price Trend")

if not display_df.empty:
    chart_df = display_df.set_index("Month")
    st.line_chart(chart_df)


# -------------------------------------------------
# 13. Download filtered data
# -------------------------------------------------
st.subheader("⬇️ Download Data")

st.download_button(
    label="Download CSV",
    data=display_df.to_csv(index=False),
    file_name="chennai_22k_gold_prices_filtered.csv",
    mime="text/csv"
)


# -------------------------------------------------
# 14. Footer
# -------------------------------------------------
st.caption(
    "📌 Prices are estimated monthly averages for analytical and educational use."
)
