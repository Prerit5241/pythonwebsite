import streamlit as st
from PIL import Image 


##st.header("media gallery")

st.set_page_config(
layout="wide"
)
st.title("Media Gallery")
st.write("""The official Sirmaur district website, hosted by the Himachal Pradesh government,
          includes a gallery that highlights notable locations and attractions within the district.
          The "Media Gallery" section showcases images of key tourist spots like Renuka Lake, an oval lake known for its serene boating activities; 
         Paonta Sahib, a significant religious site for Sikhs with its scenic Gurudwara; the mountainous Haripur Dhar fort; the Jaitak Fort with its historical significance related to battles against the British; and the Churdhar Summit,
          ideal for trekkers and religious pilgrims due to its Shiva temple.""")
st.subheader("Highlights")
st.write("""
       - Renuka Lake: An oval-shaped lake with boating activities and surrounded by a sanctuary.
        - The Renuka Ji Fair, with vibrant cultural activities
       
      - Paonta Sahib: A revered Sikh site with a historic Gurudwara,
          offering views of the Yamuna River and Dun Valley  
      
      - Churdhar Summit: A popular trekking and pilgrimage destination with a Shiva temple,
           accessible by hiking through small glaciers  
         
      - Jaitak Fort: A historical fort associated with the Gurkha-British battles,
           located on a high ridge with panoramic views
         
      - Haripur Dhar Fort: Built to guard Sirmaur’s borders,
         it is now used by the Forest Department
         
      - Rajgarh: Known as the "Peach Valley," this agricultural area is famous for its orchards and scenic beauty
         
      - Sarahan: Known for its lush valley and historical temples, ideal for religious tourism.
         """)
st.header("Natural Attractions")
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
img_sirmaur3 = Image.open("images/sirmaur3.png")
#inset image   
with st.container():
     image_column, text_column = st.columns((1,2))
     with image_column: 
          #image will be put here
          st.image(img_sirmaur3) 
     with text_column:
          #insert text details
          st.subheader("Churdhar peak")
          st.write(" Churdhar Peak is not just a trek but an immersive experience that combines adventure with spirituality. Whether you’re seeking solitude in nature or a challenge on the trails.")
          st.write("Trekking Route: The trek is about 22 kilometers (round trip) and takes approximately 6-7 hours to reach the summit. The trail is well-marked, winding through lush forests of pine and oak, and features various scenic viewpoints.")

st.write("---")


st.header("Traking sites")
st.write("Sirmour District is a treasure trove for adventure seekers, offering a mix of activities that cater to all levels of thrill-seekers. Whether you're trekking to high peaks, paragliding over valleys, or simply enjoying the beauty of nature, Sirmour promises an unforgettable experience.")

img_sirmaur6 = Image.open("images/sirmaur6.png")
#inset image   
with st.container():
     image_column, text_column = st.columns((1,2))
     with image_column: 
          #image will be put here
          st.image(img_sirmaur6) 
     with text_column:
          #insert text details
          st.subheader("Churdhar Trek")
          st.write("Location:churdhar ")
          st.write(" A popular trekking route that leads to Churdhar Peak, offering breathtaking views and diverse flora and fauna.")
          st.write("Starting Point: The trek to Churdhar Peak typically begins from the village of Dhandrori, which is accessible by road from major towns in Sirmour.")


img_sirmaur7 = Image.open("images/sirmaur7.png")
#inset image   
with st.container():
     image_column, text_column = st.columns((1,2))
     with image_column: 
          #image will be put here
          st.image(img_sirmaur7) 
     with text_column:
          #insert text details
          st.subheader("Renuka Lake Trek")
          st.write("Location:Renuka")
          st.write(" Scenic trails around the lake provide opportunities for shorter hikes and nature walks.")
          st.write("There are several trekking trails around the lake that lead to scenic viewpoints, offering stunning panoramas of the region.")

st.write("---")