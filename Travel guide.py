import streamlit as st
import streamlit as st
from PIL import Image

st.set_page_config(
     layout = "wide"
)
st.title("The Road to Sirmour ")

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

lottie_animation_1 = "https://lottie.host/721de97c-ef96-4b0c-831a-c8770f92ec6c/o1a810aLo6.json"
lottie_anime_json = load_lottie_url(lottie_animation_1)



st_lottie(lottie_anime_json, key = "hello")

st.header("Travel Guide")
st.write("Sirmour, with its scenic beauty and rich culture, is accessible by various modes of transport. Here’s how you can plan your journey to this enchanting Himalayan district.")
st.header("Getting to Sirmour")
st.subheader("By Air")

img_sirmaur8 = Image.open("images/sirmaur8.png")
#inset image   
with st.container():
     image_column, text_column = st.columns((1,2))
     with image_column: 
          #image willasa be put here
          st.image(img_sirmaur8)
     with  text_column:
          st.write("- The nearest airport to Sirmour is Chandigarh Airport (IXC), located about 90 kilometers from Nahan, Sirmour’s district headquarters.");
          st.write("- From Chandigarh, visitors can hire a taxi or take a bus to reach Sirmour. ")
          st.write("""
                  -  Alternative Option: For those closer to Uttarakhand, Dehradun’s Jolly Grant Airport (DED) is around 80 kilometers from Paonta Sahib, another prominent town in Sirmour. The drive from Dehradun to Paonta Sahib is scenic,
                     following the Yamuna River and winding through the Shivalik hills.
                   
                   """)
          
st.subheader("By train ")
st.write("While Sirmour doesn’t have its own railway station, several nearby railheads offer convenient access.")

img_sirmaur9 = Image.open("images/sirmaur9.png")
#inset image   
with st.container():
     image_column, text_column = st.columns((1,2))
     with image_column: 
          #image willasa be put here
          st.image(img_sirmaur9)
     with  text_column:
          st.write("- Ambala Cantt Junction (UMB): About 85 kilometers from Nahan, this is the nearest major railhead with good connectivity to cities like Delhi, Chandigarh, and Amritsar.");
          st.write("- Yamunanagar-Jagadhri Railway Station: Located around 60 kilometers from Paonta Sahib, this station also offers access to those arriving from northern cities ")
          st.write("""
                  - Dehradun Railway Station: Situated approximately 65 kilometers from Paonta Sahib, Dehradun is well-connected with major Indian cities.
                   
                   """)
          st.write("From these stations, regular bus services and taxis are available for the onward journey to Sirmour.") 
          

st.subheader("By Road ")
st.write("Sirmour is well-connected to neighboring states and cities, with smooth and scenic routes making road travel popular.")

img_sirmaur10 = Image.open("images/sirmaur10.png")
#inset image   
with st.container():
     image_column, text_column = st.columns((1,2))
     with image_column: 
          #image willasa be put here
          st.image(img_sirmaur10)
     with  text_column:
          st.write("- From Chandigarh (Approx. 2.5 hours): Take the Chandigarh-Nahan road (National Highway 7) for a straightforward route to Nahan.");
          st.write("- From Dehradun (Approx. 2 hours): Follow the Dehradun-Paonta Sahib Road via NH 72. This route is particularly scenic and follows the Yamuna River for much of the way.")
          st.write("""
                  - From Delhi (Approx. 5 hours): Delhi is around 270 kilometers from Sirmour. Take NH 44 towards Ambala, then NH 7 to Nahan.
                   
                   """)
          st.write("Regular bus services are available from Delhi, Chandigarh, and Dehradun, with options ranging from state-run buses to private Volvo services.") 
          
st.write("---")

st.header("Local Travel in Sirmour")
st.write("Once in Sirmour, you can explore local attractions by renting a car or opting for taxis available in Nahan and Paonta Sahib. Local buses also connect some major sites, but for remote areas and high-altitude spots like Churdhar, it’s recommended to hire a local taxi or join a guided tour for a comfortable experience.")
st.subheader("Tips for Traveling to Sirmour")
st.write("""
     - Best Time to Visit: October to April is ideal for comfortable temperatures, but each season brings its unique charm.
     - Permits: While no special permits are required for Indian nationals, foreigners may need to register at certain checkpoints if venturing near border areas.
     - Weather Prep: Given Sirmour’s location in the lower Himalayas, the climate can vary. Pack warm clothes if visiting in winter, and light layers in summer.   
         """)
st.write("With its accessibility and natural beauty, getting to Sirmour is as enjoyable as exploring its wonders. Plan your journey to discover the charm of this Himalayan paradise.")