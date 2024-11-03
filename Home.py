from PIL import Image 
import streamlit as st
import json # pip install requests

import requests 
import streamlit as st
from streamlit_lottie import st_lottie 
# ---  phase3  --- (animation)
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

 
#st.set_page_config(page_title="website local", page_icon=":tada", layout="wide")
st.set_page_config(
    page_title="Discover Sirmaur",
    page_icon="🏔️",
    layout="wide"
)

st.title("Welcome to Sirmaur!")
st.subheader("So come and seek the magic, in the valleys and the peaks")

lottie_animation_1 = "https://lottie.host/1dfcda62-bd2e-4202-bbf4-53f1b37ff6fc/snl3ttvPO2.json"
lottie_anime_json = load_lottie_url(lottie_animation_1)

st_lottie(lottie_anime_json, key = "hello")
     

# ------  hader section ---
with st.container():
     
     st.title("Introduction:")
     st.write("Nestled in the serene hills of Himachal Pradesh, Sirmaur is a hidden gem that offers breathtaking landscapes, rich cultural heritage, and a plethora of outdoor adventures. Known for its lush greenery and tranquil atmosphere, Sirmaur is the perfect destination for nature lovers and adventure seekers alike.")


# ---- second fase ----(right and left sides)
with st.container():
     st.write("---")
     st.header("Explore Sirmaur")
     left_column, right_column = st.columns(2)
     with left_column:
          st.write("##")
          st.header("Discover the Beauty")
          st.write(
            """
           From the majestic Renuka Lake to the historical Kotla Fort, Sirmaur boasts a variety of attractions that showcase the region's natural beauty and historical significance. Whether you’re wandering through charming villages or trekking in the picturesque mountains, every moment spent here is a memory in the making.
            """
          )
          st.write("[learn more >](https://www.youtube.com/watch?v=008VzrP7yCk)")

     with right_column:
          st.write("##")
          st.header("Local Cuisine")
          st.write(
            """Indulge your taste buds in the authentic flavors of Himachali cuisine. Don't miss trying local delicacies like Siddu, Chana Madra, and the famous Renukaji Fish,Pahari Dham: A traditional meal that includes rice, lentils, and various local vegetables, often cooked during festivals and special occasions.


            
            """
          )
          st.write("[learn more >](https://www.youtube.com/watch?v=Z1jN9aqK1Y8)")
st.write("---")
st.header("Cultural sites")
#image assets


st.write("####")

img_sirmaur1 = Image.open("images/sirmaur1.png")
#inset image   
with st.container():
     image_column, text_column = st.columns((1,2))
     with image_column: 
          #image will be put here
          st.image(img_sirmaur1) 
     with text_column:
          #insert text details
          st.subheader("Churdhar peak")
          st.write(" Churdhar Peak is not just a trek but an immersive experience that combines adventure with spirituality. Whether you’re seeking solitude in nature or a challenge on the trails.")
          st.write("Trekking Route: The trek is about 22 kilometers (round trip) and takes approximately 6-7 hours to reach the summit. The trail is well-marked, winding through lush forests of pine and oak, and features various scenic viewpoints.")

# --
img_sirmaur2 = Image.open("images/sirmaur2.png")
#inset image   
with st.container():
     image_column, text_column = st.columns((1,2))
     with image_column: 
          #image will be put here
          st.image(img_sirmaur2) 
     with text_column:
          #insert text details
          st.subheader("Renuka Lake")
          st.write(" Renuka Lake is the largest lake in Himachal Pradesh and a stunning natural attraction nestled in the Sirmour District. Spanning approximately 2.5 kilometers in length.")
          st.write("Shape: The lake is uniquely shaped like a sleeping woman, which adds to its charm and local folklore.")
          st.write("Location: Renuka Lake is located about 42 kilometers from Nahan, the district headquarters, and is easily accessible by road")
# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/codingisfun.preritthakur2800@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

# use local CSS
def local_css(file_name): 
     with open(file_name) as f:
          st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")  

# Primary accent for interactive elements
primaryColor = '#7792E3'

# Background color for the main content area
backgroundColor = '#273346'

# Background color for sidebar and most interactive widgets
secondaryBackgroundColor = '#B9F1C0'

# Color used for almost all text
textColor = '#FFFFFF'

# Font family for all text in the app, except code blocks
# Accepted values (serif | sans serif | monospace) 
# Default: "sans serif"
font = "sans serif"







