import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Page Configuration
st.set_page_config(
    page_title="Carbon Dashboard",
    page_icon="📊",
    layout="wide" # Wide layout works better for charts
)

# 2. Sidebar - Setup/Inputs
with st.sidebar:
    st.title("Settings")
    data_points = st.slider("Number of data points", 5, 50, 10)
    st.divider()
    st.info("Adjust the slider to see how the charts react to new data volumes.")

# 3. Main Header
st.title("🌱 Personal Carbon Analytics")
name = st.text_input("Enter your name:", placeholder="e.g. Alex")

if name:
    st.write(f"### Welcome back, **{name}**! Here is your trend analysis.")

# 4. Data Logic
# Using the random data provided
df = pd.DataFrame(
    np.random.randn(data_points, 2), 
    columns=['Emissions Index A', 'Emissions Index B']
)

# 5. Dashboard Layout
# Using columns for high-level metrics
m1, m2, m3 = st.columns(3)
m1.metric("Current Level", f"{df.iloc[-1, 0]:.2f}", "+1.2%")
m2.metric("Target Goal", "0.50", "-0.1%")
m3.metric("Efficiency", "88%", "5%")

st.divider()

# 6. Chart Section using Tabs
tab1, tab2, tab3 = st.tabs(["📈 Trend Line", "📊 Comparison Bar", "📄 Raw Data"])

with tab1:
    st.subheader("Emission Trends Over Time")
    st.line_chart(df, use_container_width=True)

with tab2:
    st.subheader("Category Comparison")
    st.bar_chart(df, use_container_width=True)

with tab3:
    st.subheader("Detailed Logs")
    st.dataframe(df, use_container_width=True)

# 7. Footer
st.caption("Data generated randomly for visualization purposes.")
st.sidebar.title("Navigator")
st.image("https://th.bing.com/th/id/OIP.uZsIyLwP36HVMylgx5CzGgHaEK?w=309&h=180&c=7&r=0&o=7&cb=defcache2&dpr=1.5&pid=1.7&rm=3&defcache=1")
st.video("https://www.youtube.com/watch?v=34Pl2DTuwoQ&list=RD34Pl2DTuwoQ&start_radio=1")

upload = st.file_uploader("Upload your carbon data (CSV)", type=["csv"])

if upload:
    user_df = pd.read_csv(upload)
    st.write("### Your Uploaded Data")
    st.dataframe(user_df, use_container_width=True)

#Text and markdown formatting
st.header("About This Dashboard")
st.subheader("Purpose")

st.markdown("**Bold**,*italic*,'`code`' [link](https://www.example.com)")
st.code("for i in range(5): print(i)", language="python")

st.text_input("What's your favorite aspect of carbon analytics?", placeholder="Type here...")
st.text_area("Describe your carbon footprint in a few sentences.")
st.number_input("On a scale of 1-10, how concerned are you about carbon emissions?", min_value=1, max_value=10, value=5)
st.slider("Select your carbon reduction goal (%)", 0, 100, 20)
st.selectbox("Choose your preferred visualization type", ["Line Chart", "Bar Chart", "Data Table"])
st.multiselect("Select the metrics you want to track", ["Emissions Index A", "Emissions Index B"])
st.radio("Choose your dashboard theme", ["Light", "Dark", "Auto"])
st.checkbox("Enable notifications for carbon updates")
 
fig,ax = plt.subplots()
ax.plot([1,2,3,4], [10,20,25,30])
st.pyplot(fig)