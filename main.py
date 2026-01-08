import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import base64
import streamlit.components.v1 as components

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(page_title="MP Crops Dashboard", page_icon="🌾", layout="wide")

# --------------------------------------------------
# SIDEBAR NAVIGATION
# --------------------------------------------------
with st.sidebar:
    selected = option_menu(
        ["Home", "Charts", "About"],
        icons=["house", "bar-chart", "info-circle"],
        default_index=0
    )

# ==================================================
# HOME PAGE  (main.py – FULL CONTENT)
# ==================================================
if selected == "Home":
    st.title('MADYA PRADESH 2026 CROPS ARRIVAL')

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
        "They depend on factors such as weather conditions, availability of water, "
        "cost of seeds and fertilizers, and market demand. When production is high, "
        "prices usually fall, while low production can lead to higher prices. "
        "Fair and stable crop prices help farmers earn a good income and ensure that "
        "food remains affordable for everyone."
    )

    st.write("𝗛𝗢𝗪 𝗙𝗔𝗥𝗠𝗘𝗥𝗦 𝗛𝗘𝗟𝗣 𝗦𝗢𝗖𝗜𝗘𝗧𝗬")
    im1, im2 = st.columns(2)
    with im1:
        st.image("img5.jpg")
    with im2:
        st.image("img8.jpg")

    st.write(
        "Farmers are fundamental to the survival and progress of society. "
        "Through their constant labor, they provide the food that sustains populations "
        "and supports economic stability. Their contribution extends beyond agriculture, "
        "strengthening communities and ensuring food security for present and future generations."
    )

    st.write("𝗜𝗡𝗙𝗟𝗔𝗧𝗜𝗢𝗡 𝗢𝗡 𝗖𝗥𝗢𝗣𝗦")
    im4, im3 = st.columns(2)
    with im3:
        st.image("img7.jpg")
    with im4:
        st.image("imgd3.jpg")

    st.write(
        "Inflation has a significant impact on crops by increasing the cost of seeds, "
        "fertilizers, fuel, and farm equipment. As production expenses rise, farmers are "
        "forced to sell their crops at higher prices to avoid losses. This leads to increased "
        "food prices in markets, affecting consumers and reducing affordability. Inflation "
        "also makes it difficult for farmers to invest in better technology, which can limit "
        "productivity and long-term agricultural growth."
    )

    st.write("𝗖𝗥𝗢𝗣𝗦 𝗚𝗥𝗢𝗪𝗡 𝗜𝗡 𝗠𝗔𝗗𝗛𝗬𝗔 𝗣𝗥𝗔𝗗𝗘𝗦𝗛")
    t1, t2 = st.columns(2)
    with t1:
        st.write("𝗖𝗮𝘁𝗲𝗴𝗼𝗿𝘆")
        st.write("Cereals ")
        st.write("Pulses")
        st.write(" Oilseeds")
        st.write("Fibre Crops")
        st.write("vegetables")
    with t2:
        st.write("𝗖𝗥𝗢𝗣𝗦")
        st.write("Wheat, Rice, Maize, Sorghum (Jowar), Barley")
        st.write("Potato, Tomato, Onion, Brinjal, Cabbage")
        st.write("Chickpea (Gram), Lentil (Masoor), Pigeon Pea (Arhar/Tur), Moong")
        st.write("Soybean, Groundnut, Mustard, Sunflower")
        st.write("Cotton, Jute")

    st.write("𝗥𝗘𝗟𝗔𝗧𝗜𝗢𝗡 𝗕𝗘𝗧𝗪𝗘𝗘𝗡 𝗙𝗔𝗥𝗠𝗘𝗥𝗦 𝗔𝗡𝗗 𝗖𝗥𝗢𝗣𝗦")
    col2, col3 = st.columns(2)
    with col2:
        st.write(
            "Understanding the relationship between farmers and crops is essential because "
            "it forms the foundation of sustainable agriculture..."
        )
    with col3:
        st.image("download.jpg")

    st.write("𝗜𝗠𝗣𝗢𝗥𝗧𝗔𝗡𝗖𝗘 𝗢𝗙 𝗠𝗔𝗗𝗬𝗔 𝗣𝗥𝗔𝗗𝗘𝗦𝗛 𝗙𝗔𝗥𝗠𝗘𝗥𝗦")
    col1, col2 = st.columns(2)
    with col1:
        video_url = "https://www.pexels.com/download/video/32508413/"
        components.html(
            f"""
            <video autoplay muted loop playsinline width="100%">
                <source src="{video_url}" type="video/webm">
            </video>
            """,
            height=400,
        )
    with col2:
        st.write(
            "𝗙𝗔𝗥𝗠𝗘𝗥𝗦 of Madhya Pradesh play a very important role in Indian farming..."
        )

    st.subheader("TO UNDERSTAND HOW NEW YEAR BEGINS WITH PRODUCTION AND COST OF CROPS CLICK ON CHARTS")

# ==================================================
# CHARTS PAGE  (1Charts.py – FULL CONTENT)
# ==================================================
elif selected == "Charts":
    st.title('MADYA PRADESH 2026 CROPS ARRIVAL PRICES')

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
    st.dataframe(df)

    var = df["Commodity Group"].value_counts().index
    select = st.selectbox("Select Commodity", var)

    df_sel = df[df["Commodity Group"] == select]

    st.plotly_chart(px.pie(df_sel, values="Price on 01 Jan, 2026", names="Commodity",
                           title="𝗣𝗿𝗶𝗰𝗲𝘀 𝗼𝗻 𝗡𝗲𝘄 𝗬𝗲𝗮𝗿"))
    st.plotly_chart(px.pie(df_sel, values="Price on 02 Jan, 2026", names="Commodity",
                           title="𝗣𝗿𝗶𝗰𝗲𝘀 𝗼𝗻 2𝗻𝗱 𝗝𝗮𝗻𝘂𝗮𝗿𝘆"))
    st.plotly_chart(px.pie(df_sel, values="Price on 03 Jan, 2026", names="Commodity",
                           title="𝗣𝗿𝗶𝗰𝗲𝘀 𝗼𝗻 3𝗿𝗱 𝗝𝗮𝗻𝘂𝗮𝗿𝘆"))

    st.plotly_chart(px.scatter(
        df, x="Commodity Group", y="MSP (Rs./Quintal) 2026-27",
        color="Commodity",
        title="𝗠𝗦𝗣 𝗢𝗙 𝗗𝗜𝗙𝗙𝗘𝗥𝗘𝗡𝗧 𝗖𝗢𝗠𝗠𝗢𝗗𝗜𝗧𝗜𝗘𝗦"
    ))

    st.plotly_chart(px.bar_polar(
        df, r="Arrival on 01 Jan, 2026",
        theta="Commodity Group",
        color="Commodity Group",
        title="𝗤𝗨𝗔𝗡𝗧𝗜𝗧𝗬 𝗔𝗥𝗥𝗜𝗩𝗘𝗗 𝗢𝗡 𝗡𝗘𝗪 𝗬𝗘𝗔𝗥"
    ))

    st.plotly_chart(px.scatter(
        df, x="Commodity", y="Arrival on 01 Jan, 2026",
        color="Commodity",
        title="𝗣𝗘𝗥 𝗜𝗧𝗘𝗠 𝗤𝗨𝗔𝗡𝗧𝗜𝗧𝗬"
    ))

    st.plotly_chart(px.scatter_3d(
        df,
        x="Arrival on 03 Jan, 2026",
        y="Arrival on 02 Jan, 2026",
        z="Arrival on 01 Jan, 2026",
        color="Commodity",
        title="𝗗𝗜𝗙𝗙𝗘𝗥𝗘𝗡𝗖𝗘 𝗢𝗙 𝗤𝗨𝗔𝗡𝗧𝗜𝗧𝗬"
    ))

# ==================================================
# ABOUT PAGE  (2about.py – FULL CONTENT)
# ==================================================
elif selected == "About":
    st.title("ORIGNAL DATASET OF ALL INDIA CROPS")
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

    st.title("📩 Inquiry Form")
    st.write("Please fill out the form below and submit your inquiry.")

    with st.form("inquiry_form", clear_on_submit=True):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        subject = st.selectbox(
            "Subject",
            ["General Inquiry", "Support", "Feedback", "Other"]
        )
        message = st.text_area("Your Message")

        submitted = st.form_submit_button("Submit Inquiry")

    if submitted:
        if name and email and message:
            st.success("✅ Your inquiry has been submitted successfully!")
            st.write("### Submitted Details")
            st.write("**Name:**", name)
            st.write("**Email:**", email)
            st.write("**Subject:**", subject)
            st.write("**Message:**", message)
        else:
            st.error("❌ Please fill in all required fields.")
