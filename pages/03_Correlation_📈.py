import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io
import numpy as np

st.set_page_config(
    page_title="Correlation",
    page_icon="📈",
)

@st.experimental_memo(show_spinner=False)
def read_df():
    data = pd.read_csv("./world-development-indicators/Indicators.csv")
    return pd.DataFrame(data)
df = read_df()

@st.experimental_singleton(show_spinner=False)
def unique_options():
    country_list = df["CountryName"].unique()
    indicator_list = df["IndicatorName"].unique()
    return country_list, indicator_list

country_list, indicator_list = unique_options()

st.markdown("# Correlation")
st.caption("Get correlation between two indicators for a country.")
st.sidebar.markdown("# Correlation Page 📈")
st.sidebar.caption("Get correlation between two indicators for a country.")


# country_select = st.selectbox("Indicator", options=indicator_list)
# country1, country2 = st.columns(2)
# with country1:
#   indicator1_select = st.selectbox(label = "Choose a indicator", options = indicator_list, key="indicator1")
# with country2:
#   indicator2_select = st.selectbox(label = "Choose a indicator", options = indicator_list, key="indicator2")


with st.sidebar:
    st.subheader("Configure the plot")
    country_select = st.selectbox(label = "Choose a continent", options = country_list)
    indicator1_select = st.selectbox(label = "Choose a indicator", options = indicator_list, key="indicator1")
    indicator2_select = st.selectbox(label = "Choose a indicator", options = indicator_list, key="indicator2")

country = df.CountryName.str.match(country_select)
indicator1 = df.IndicatorName.str.contains(indicator1_select, regex=False)
indicator2 = df.IndicatorName.str.contains(indicator2_select, regex=False)
df1 = df[(country) & (indicator1)]
df2 = df[(country) & (indicator2)]


X = df1["Value"]
Y = df2["Value"]


scatter, axis = plt.subplots()
axis.yaxis.grid(True)
axis.set_title(f"{indicator1_select} vs. \n{indicator2_select} for {country_select}", pad=30)
axis.set_xlabel(f"{indicator1_select}")
axis.set_ylabel(f"{indicator2_select}")

try:
    plt.scatter(X,Y)
    st.pyplot(scatter)

    correlation = np.corrcoef(X, Y)
    corrcoef = round(correlation[0][1], 3)
    
    st.markdown(f'The correlation between "{indicator1_select}" and "{indicator2_select}" is **{corrcoef}**.')
except ValueError:
    if len(df1.index) > len(df2.index):
        difference = len(df1.index) - len(df2.index)
        new_df1 = df1[:-int(difference)] 

        X = new_df1["Value"]
        plt.scatter(X, Y)

        st.pyplot(scatter)

        correlation = np.corrcoef(X, Y)
        corrcoef = round(correlation[0][1], 3)

        st.markdown(f'The correlation between "{indicator1_select}" and "{indicator2_select}" is **{corrcoef}**.')
    
    elif len(df1.index) < len(df2.index):
        difference = len(df2.index)- len(df1.index)
        new_df2 = df2[:-int(difference)]
        
        Y = new_df2["Value"]
        plt.scatter(X, Y)

        st.pyplot(scatter)

        correlation = np.corrcoef(X, Y)
        corrcoef = round(correlation[0][1], 3)

        st.markdown(f'The correlation between "{indicator1_select}" and "{indicator2_select}" is **{corrcoef}**.')



scatter_png = io.BytesIO()
scatter.savefig(scatter_png, format="png", bbox_inches='tight')
scatter_jpg = io.BytesIO()
scatter.savefig(scatter_jpg, format="jpg", bbox_inches='tight')
scatter_pdf = io.BytesIO()
scatter.savefig(scatter_pdf, format="pdf", bbox_inches='tight')



line_png_btn, line_jpg_btn, line_pdf_btn = st.columns(3)
with line_png_btn:
    st.download_button(
        label="Press to Download Graph as PNG",
        data=scatter_png,
        file_name=f"{country_select}-{indicator1_select}-{indicator2_select} Scatter Plot.png",
        mime="image/png"
    )
with line_jpg_btn:
    st.download_button(
        label="Press to Download Graph as JPG",
        data=scatter_jpg,
        file_name=f"{country_select}-{indicator1_select}-{indicator2_select} Scatter Plot.jpg",
        mime="image/jpg"
    )
with line_pdf_btn:
    st.download_button(
        label="Press to Download Graph as PDF",
        data=scatter_pdf,
        file_name=f"{country_select}-{indicator1_select}-{indicator2_select} Scatter Plot.pdf",
        mime="image/pdf"
    )