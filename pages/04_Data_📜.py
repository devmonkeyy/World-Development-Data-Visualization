import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Data",
    page_icon="📜",
)

st.markdown("# Data Page")
st.caption("Download date for choosen continent and indicator, and explore datasets.")
st.sidebar.markdown("# Data Page 📜")
st.sidebar.caption("Download date for choosen continent and indicator, and explore datasets.")

@st.experimental_memo(show_spinner=False)
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')

@st.experimental_memo(show_spinner=False)
def read_df():
    data = pd.read_csv("./world-development-indicators/Indicators.csv")
    return pd.DataFrame(data)
df = read_df()

@st.experimental_memo(show_spinner=False)
def unique_options():
    country_list = df["CountryName"].unique()
    indicator_list = df["IndicatorName"].unique()
    return country_list, indicator_list

country_list, indicator_list = unique_options()



with st.sidebar:
    st.subheader("Configure the plot")
    country = st.selectbox(label = "Choose a continent", options = country_list)
    indicator = st.selectbox(label = "Choose a indicator", options = indicator_list)
specification1 = df.CountryName.str.match(country)
specification2 = df.IndicatorName.str.contains(indicator, regex=False)
final_df = df[(specification1) & (specification2)]
csv = convert_df(final_df)

st.dataframe(final_df)
st.download_button(
    label="Press to Download CSV",
    data=csv,
    file_name=f"{country}'s-{indicator}.csv",
    mime="text/csv"
)