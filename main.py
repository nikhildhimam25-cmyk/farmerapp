import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit.components.v1 as components

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(page_title="MP Crops Dashboard", page_icon="🌾", layout="wide")

# -------------------------------------------------
# SIDEBAR MENU
# -------------------------------------------------
with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",
        options=["Home", "Charts", "About"],
        icons=["house", "bar-chart", "info-circle"],
        default_index=0
    )

# -------------------------------------------------
# HOME PAGE (main.py)
# -------------------------------------------------
def home_page():
    st.title("MADHYA PRADESH 2026 CROPS ARRIVAL 🌾")

    video_url = "https://www.pexels.com/download/video/2530656/"
    components.html(
        f"""
        <video autoplay muted loop playsinline width="100%">
            <source src="{video_url}" type="video/webm">
        </video>
        """,
        height=400,
    )

    st.subheader("𝗖𝗥𝗢𝗣𝗦")
    st.write(
        "Crop prices play an important role in the lives of farmers and consumers. "
        "They depend on weather, water availability, seed costs, fertilizers, and market demand."
    )

    st.write("### 𝗛𝗢𝗪 𝗙𝗔𝗥𝗠𝗘𝗥𝗦 𝗛𝗘𝗟𝗣 𝗦𝗢𝗖𝗜𝗘𝗧𝗬")
    c1, c2 = st.columns(2)
    with c1:
        st.image("img5.jpg")
    with c2:
        st.image("img8.jpg")

    st.write(
        "Farmers are fundamental to the survival of society by ensuring food security "
        "and strengthening the rural economy."
    )

    st.write("### 𝗜𝗡𝗙𝗟𝗔𝗧𝗜𝗢𝗡 𝗢𝗡 𝗖𝗥𝗢𝗣𝗦")
    c3, c4 = st.columns(2)
    with c3:
        st.image("img7.jpg")
    with c4:
        st.image("imgd3.jpg")

    st.write(
        "Inflation increases the cost of seeds, fertilizers, fuel, and equipment, "
        "which ultimately raises food prices."
    )

    st.subheader("TO UNDERSTAND PRICE & ARRIVAL DATA → GO TO CHARTS 📊")

# -------------------------------------------------
# CHARTS PAGE (1Charts.py)
# -------------------------------------------------
def charts_page():
    st.title("📊 MADHYA PRADESH 2026 CROPS ARRIVAL PRICES")

    df = pd.read_csv("Marketwise_Price_Arrival_05-01-2026_02-00-10_PM.csv")

    df.rename(columns={
        "Unnamed: 0": "Commodity Group",
        "Unnamed: 1": "Commodity",
        "Unnamed: 2": "MSP (Rs./Quintal) 2026-27",
        "Unnamed: 3": "Price on 03 Jan, 2026",
        "Marketwise Price & Arrival Report (03-01-2026)": "Price on 02 Jan, 2026",
        "Unnamed: 5": "Price on 01 Jan, 2026",
        "Unnamed: 6": "Arrival on 03 Jan, 2026",
        "Unnamed: 7": "Arrival on 02 Jan, 2026",
        "Unnamed: 8": "Arrival on 01 Jan, 2026"
    }, inplace=True)

    df.drop([0, 1], inplace=True)

    with st.sidebar:
        commodity = st.selectbox(
            "Select Commodity Group",
            df["Commodity Group"].unique()
        )

    df_sel = df[df["Commodity Group"] == commodity]

    st.plotly_chart(
        px.pie(df_sel, values="Price on 01 Jan, 2026", names="Commodity",
               title="Prices on 1st Jan 2026"),
        use_container_width=True
    )

    st.plotly_chart(
        px.pie(df_sel, values="Price on 02 Jan, 2026", names="Commodity",
               title="Prices on 2nd Jan 2026"),
        use_container_width=True
    )

    st.plotly_chart(
        px.pie(df_sel, values="Price on 03 Jan, 2026", names="Commodity",
               title="Prices on 3rd Jan 2026"),
        use_container_width=True
    )

    st.plotly_chart(
        px.scatter(
            df,
            x="Commodity Group",
            y="MSP (Rs./Quintal) 2026-27",
            color="Commodity",
            title="MSP Forecast 2026–27"
        ),
        use_container_width=True
    )

# -------------------------------------------------
# ABOUT PAGE (2about.py)
# -------------------------------------------------
def about_page():
    st.title("🧾 ORIGINAL DATASET – ALL INDIA CROPS")
    st.link_button("CLICK HERE", "https://agmarknet.gov.in/home")

    video_url = "https://www.shutterstock.com/shutterstock/videos/3833711813/preview/stock-footage-aerial-view-of-beautiful-landscape-with-a-crop-sprayer-applying-pesticide-in-a-wheat-field-at.webm"
    components.html(
        f"""
        <video autoplay muted loop playsinline width="100%">
            <source src="{video_url}" type="video/webm">
        </video>
        """,
        height=500,
    )

    st.subheader("📩 Inquiry Form")

    with st.form("inquiry_form", clear_on_submit=True):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        subject = st.selectbox("Subject", ["General Inquiry", "Support", "Feedback", "Other"])
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Submit")

    if submitted:
        if name and email and message:
            st.success("✅ Inquiry submitted successfully!")
        else:
            st.error("❌ Please fill all required fields.")

# -------------------------------------------------
# ROUTING
# -------------------------------------------------
if selected == "Home":
    home_page()
elif selected == "Charts":
    charts_page()
elif selected == "About":
    about_page()
