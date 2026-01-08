import streamlit as st 
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px 
import base64
import seaborn as sns
import matplotlib.pyplot as plt
st.set_page_config(page_icon="🧾",page_title="ABOUT")
st.title("ORIGNAL DATASET OF ALL INDIA CROPS")
st.link_button(label="CLICK HERE",url="https://agmarknet.gov.in/home")
# st.video("https://www.shutterstock.com/shutterstock/videos/3833711813/preview/stock-footage-aerial-view-of-beautiful-landscape-with-a-crop-sprayer-applying-pesticide-in-a-wheat-field-at.webm",autoplay=True)

import streamlit.components.v1 as components

video_url = "https://www.shutterstock.com/shutterstock/videos/3833711813/preview/stock-footage-aerial-view-of-beautiful-landscape-with-a-crop-sprayer-applying-pesticide-in-a-wheat-field-at.webm"

components.html(
    f"""
    <video autoplay muted loop playsinline width="100%">
        <source src="{video_url}" type="video/webm">
        Your browser does not support the video tag.
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
        
        # Optional: display submitted data
        st.write("### Submitted Details")
        st.write("**Name:**", name)
        st.write("**Email:**", email)
        st.write("**Subject:**", subject)
        st.write("**Message:**", message)
    else:
        st.error("❌ Please fill in all required fields.")