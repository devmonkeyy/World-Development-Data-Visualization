import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io

st.set_page_config(
    page_title="Compare",
    page_icon="⚖️",
)

st.markdown("# Compare Page")
st.caption("Compare indicators between different countries.")
st.sidebar.markdown("# Compare Page ⚖️")
st.sidebar.caption("Compare indicators between different countries.")

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

# indicator = st.selectbox("Indicator", options=indicator_list)
# country1, country2 = st.columns(2)
# with country1:
#   one = st.selectbox("Country One", options=country_list)
# with country2:
#   two = st.selectbox("Country Two", options=country_list)

with st.sidebar:
    indicator = st.selectbox("Indicator", options=indicator_list)
    one = st.selectbox("Country One", options=country_list)
    two = st.selectbox("Country Two", options=country_list)

one_specification1 = df.CountryName.str.match(one)
one_specification2 = df.IndicatorName.str.contains(indicator, regex=False)
one_df = df[(one_specification1) & (one_specification2)]

two_specification1 = df.CountryName.str.match(two)
two_specification2 = df.IndicatorName.str.contains(indicator, regex=False)
two_df = df[(two_specification1) & (two_specification2)]

year1 = one_df["Year"].values
value1 = one_df["Value"].values

year2 = two_df["Year"].values
value2 = two_df["Value"].values


line, ax = plt.subplots()
ax.ticklabel_format(style="plain")
ax.plot(year1, value1, label=f"{one}")
ax.plot(year2, value2, label=f"{two}")
ax.set_title(f"Comparison of {indicator}\n Between {one} and {two}", pad=30)
ax.set_xlabel("Year")
ax.set_ylabel(indicator)
plt.legend(loc="upper left")
plt.axis([1959, 2011,0, None])

line_png = io.BytesIO()
line.savefig(line_png, format="png", bbox_inches='tight')
line_jpg = io.BytesIO()
line.savefig(line_jpg, format="jpg", bbox_inches='tight')
line_pdf = io.BytesIO()
line.savefig(line_pdf, format="pdf", bbox_inches='tight')


st.pyplot(line)

line_png_btn, line_jpg_btn, line_pdf_btn = st.columns(3)
with line_png_btn:
    st.download_button(
        label="Press to Download Graph as PNG",
        data=line_png,
        file_name=f"{one}-{two}-{indicator} Line Chart.png",
        mime="image/png"
    )
with line_jpg_btn:
    st.download_button(
        label="Press to Download Graph as JPG",
        data=line_jpg,
        file_name=f"{one}-{two}-{indicator} Line Chart.jpg",
        mime="image/jpg"
    )
with line_pdf_btn:
    st.download_button(
        label="Press to Download Graph as PDF",
        data=line_pdf,
        file_name=f"{one}-{two}-{indicator} Line Chart.pdf",
        mime="image/pdf"
    )