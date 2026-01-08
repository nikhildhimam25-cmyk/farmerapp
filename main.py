import streamlit as st 
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px 
import base64 
import seaborn as sns
import matplotlib.pyplot as plt 


st.set_page_config(page_title="HOME",page_icon="🌾")
st.title('MADYA PRADESH 2026 CROPS ARRIVAL')
import streamlit.components.v1 as components

video_url = "https://www.pexels.com/download/video/2530656/"

components.html(
    f"""
    <video autoplay muted loop playsinline width="100%">
        <source src="{video_url}" type="video/webm">
        Your browser does not support the video tag.
    </video>
    """,
    height=400,
)
st.subheader("𝗖𝗥𝗢𝗣𝗦")
st.write("Crop prices play an important role in the lives of farmers and consumers. They depend on factors such as weather conditions, availability of water, cost of seeds and fertilizers, and market demand. When production is high, prices usually fall, while low production can lead to higher prices. Fair and stable crop prices help farmers earn a good income and ensure that food remains affordable for everyone.")
st.write("𝗛𝗢𝗪 𝗙𝗔𝗥𝗠𝗘𝗥𝗦 𝗛𝗘𝗟𝗣 𝗦𝗢𝗖𝗜𝗘𝗧𝗬")
im1,im2=st.columns(2)
with im1:
 st.image("img5.jpg") 
with im2:
 st.image("img8.jpg") 
st.write("Farmers are fundamental to the survival and progress of society. Through their constant labor, they provide the food that sustains populations and supports economic stability. Their contribution extends beyond agriculture, strengthening communities and ensuring food security for present and future generations.")
st.write("𝗜𝗡𝗙𝗟𝗔𝗧𝗜𝗢𝗡 𝗢𝗡 𝗖𝗥𝗢𝗣𝗦")
im4,im3=st.columns(2)
with im3:
 st.image("img7.jpg") 
with im4:
 st.image("imgd3.jpg") 
st.write(" Inflation has a significant impact on crops by increasing the cost of seeds, fertilizers, fuel, and farm equipment. As production expenses rise, farmers are forced to sell their crops at higher prices to avoid losses. This leads to increased food prices in markets, affecting consumers and reducing affordability. Inflation also makes it difficult for farmers to invest in better technology, which can limit productivity and long-term agricultural growth")
st.write("𝗖𝗥𝗢𝗣𝗦 𝗚𝗥𝗢𝗪𝗡 𝗜𝗡 𝗠𝗔𝗗𝗛𝗬𝗔 𝗣𝗥𝗔𝗗𝗘𝗦𝗛")
t1,t2=st.columns(2)
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
col2,col3=st.columns(2)
with col2:
  st.write("Understanding the relationship between farmers and crops is essential because it forms the foundation of sustainable agriculture. Farmers’ decisions—such as what to plant, when to irrigate, and how to protect crops from pests—directly impact crop yield, quality, and environmental health. Likewise, knowledge of crop needs helps farmers optimize resources, reduce losses, and ensure food security. Studying this relationship enables better farming practices, supports rural livelihoods, and promotes a balance between productivity and ecological sustainability.")
  with col3:
      st.image("download.jpg")
st.write(" 𝗜𝗠𝗣𝗢𝗥𝗧𝗔𝗡𝗖𝗘 𝗢𝗙 𝗠𝗔𝗗𝗬𝗔 𝗣𝗥𝗔𝗗𝗘𝗦𝗛 𝗙𝗔𝗥𝗠𝗘𝗥𝗦 𝗜𝗡 𝗜𝗡𝗗𝗜𝗔 𝗔𝗚𝗥𝗜𝗖𝗨𝗟𝗧𝗨𝗥𝗘")
col1,col2=st.columns(2)
with col1:
  video_url = "https://www.pexels.com/download/video/32508413/"

  components.html(
    f"""
    <video autoplay muted loop playsinline width="100%">
        <source src="{video_url}" type="video/webm">
        Your browser does not support the video tag.
    </video>
    """,
    height=400,
)
with col2:
 st.write("𝗙𝗔𝗥𝗠𝗘𝗥𝗦 of Madhya Pradesh play a very important role in Indian farming and agricultural development. The state is one of the largest producers of wheat, soybean, pulses, oilseeds, and gram, making a major contribution to India’s food security. Madhya Pradesh is often called the heart of India, and its farmers support agriculture across the nation by supplying food grains and raw materials for industries. With fertile soil, favorable climate, and the growing use of modern farming methods, 𝗙𝗔𝗥𝗠𝗘𝗥𝗦 of Madhya Pradesh help strengthen the rural economy, create employment, and ensure stable food availability for millions of people in India.")
st.subheader("TO UNDERSTAND HOW NEW YEAR BEGINS WITH PRODUCTION AND COST OF CROPS CLICK ON CHARTS")
# with open('download.jfif','rb') as f:
#     file=f.read()
# img =  base64.b64encode(file).decode()

# css=f"""
#     <style>
#     [data-testid="stAppViewContainer"]{{
#         background-image:url('data:image/png;base64,{img}');
#         background-size:cover
#     }}
#     </style>"""
# st.markdown(css, unsafe_allow_html=True)