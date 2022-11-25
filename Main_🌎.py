import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Main",
    page_icon="🌎",
)

@st.cache(show_spinner=False)
def read_df():
    data = pd.read_csv("./world-development-indicators/Indicators.csv")
    return pd.DataFrame(data)
df = read_df()

st.markdown("# World Development Data Visualizer")
st.markdown("###### Generate cool graphs that visualize development indicators for countries or regions!")
st.markdown("Socials: [Github](github.com/devmonkeyy) [Discord](https://discord.gg/Av3tAFfkEq) [Reddit](https://www.reddit.com/user/devmonkeyy)")
st.caption("Dataset from [link](https://www.kaggle.com/datasets/kaggle/world-development-indicators/versions/2?resource=download)")
st.sidebar.markdown("# Main page 🎈")


st.subheader("Graphing")
st.caption("Generate bar, line, and correlation graphs for given country and indicator(s).")
bar, png = st.columns(2)
with bar:
    st.image("./images/bar_plot.png")
with png:
    st.image("./images/line_plot.png")

st.subheader("Compare")
st.caption("Compare indicators between different countries")
st.image("./images/compare.png")

st.subheader("Correlation")
st.caption("Get correlation between two indicators for a country.")
st.image("./images/correlation.png")


st.subheader("Data")
st.caption("Download date for choosen continent and indicator, and explore datasets.")
st.image("./images/data.png")