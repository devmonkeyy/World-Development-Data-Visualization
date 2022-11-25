import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io

st.set_page_config(
    page_title="Graphing",
    page_icon="📊",
)

st.markdown("# Graphing")
st.sidebar.markdown("# Graphing Page 📊")
st.sidebar.caption("Generate bar, line, and correlation graphs for given country and indicator(s).")

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
    st.subheader("Configure the plot")
    country = st.selectbox(label = "Choose a continent", options = country_list)
    indicator = st.selectbox(label = "Choose a indicator", options = indicator_list)
specification1 = df.CountryName.str.match(country)
specification2 = df.IndicatorName.str.contains(indicator, regex=False)
final_df = df[(specification1) & (specification2)]

# Bar Plot
year = final_df["Year"].values
value = final_df["Value"].values
bar, ax = plt.subplots()
ax.ticklabel_format(style="plain")
ax.bar(year, value)
ax.set_title(f"{country}'s {indicator}\n Statistics from 1960 to 2015", pad=20)
ax.set_xlabel("Year")
ax.set_ylabel(indicator)

bar_png = io.BytesIO()
bar.savefig(bar_png, format="png", bbox_inches='tight')
bar_jpg = io.BytesIO()
bar.savefig(bar_jpg, format="jpg", bbox_inches='tight')
bar_pdf = io.BytesIO()
bar.savefig(bar_pdf, format="pdf", bbox_inches='tight')


st.subheader(f"Bar Plot of {indicator} for {country}.")
st.pyplot(bar)

bar_png_btn, bar_jpg_btn, bar_pdf_btn = st.columns(3)
with bar_png_btn:
    st.download_button(
        label="Press to Download Graph as PNG",
        data=bar_png,
        file_name=f"{country}-{indicator} Bar Chart.png",
        mime="image/png",
        key="bar_png"
    )
with bar_jpg_btn:
    st.download_button(
        label="Press to Download Graph as JPG",
        data=bar_jpg,
        file_name=f"{country}-{indicator} Bar Chart.jpg",
        mime="image/jpg",
        key="bar_jpg"
    )
with bar_pdf_btn:
    st.download_button(
        label="Press to Download Graph as PDF",
        data=bar_pdf,
        file_name=f"{country}-{indicator} Bar Chart.pdf",
        mime="image/pdf",
        key="bar_pdf"
    )
st.text("")
st.text("")

# Line plot
line, ax = plt.subplots()
ax.ticklabel_format(style="plain")
ax.plot(year, value)
ax.set_title(f"{country}'s {indicator}\n Statistics from 1960 to 2015", pad=20)
ax.set_xlabel("Year")
ax.set_ylabel(indicator)
plt.axis([1959, 2011,0, None])

line_png = io.BytesIO()
line.savefig(line_png, format="png", bbox_inches='tight')
line_jpg = io.BytesIO()
line.savefig(line_jpg, format="jpg", bbox_inches='tight')
line_pdf = io.BytesIO()
line.savefig(line_pdf, format="pdf", bbox_inches='tight')

st.subheader(f"Line Plot of {indicator} for {country}")
st.pyplot(line)

line_png_btn, line_jpg_btn, line_pdf_btn = st.columns(3)
with line_png_btn:
    st.download_button(
        label="Press to Download Graph as PNG",
        data=line_png,
        file_name=f"{country}-{indicator} Line Chart.png",
        mime="image/png"
    )
with line_jpg_btn:
    st.download_button(
        label="Press to Download Graph as JPG",
        data=line_jpg,
        file_name=f"{country}-{indicator} Line Chart.jpg",
        mime="image/jpg"
    )
with line_pdf_btn:
    st.download_button(
        label="Press to Download Graph as PDF",
        data=line_pdf,
        file_name=f"{country}-{indicator} Line Chart.pdf",
        mime="image/pdf"
    )