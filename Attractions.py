import streamlit as st
from PIL import Image 

st.set_page_config(
layout="wide"
)
st.title("Attractions of Sirmour")
st.write("Sirmour District’s cultural sites reflect its rich history and diverse traditions. From ancient temples to historical forts, these landmarks offer a deep insight into the region's heritage and are essential for anyone looking to explore the cultural tapestry of Sirmour.")
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
          st.write("---")

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
st.header("Cultural Sites")
img_sirmaur4 = Image.open("images/sirmaur4.png")
#inset image   
with st.container():
     image_column, text_column = st.columns((1,2))
     with image_column: 
          #image will be put here
          st.image(img_sirmaur4) 
     with text_column:
          #insert text details
          st.subheader("Nahan Fort")
          st.write("Location: Nahan")
          st.write(" Description: A historic fort overlooking the town, built in the 18th century by Raja Karam Prakash.")
          st.write("Significance: Provides panoramic views of the surrounding landscape and is a symbol of Nahan's rich heritage.")

img_sirmaur5 = Image.open("images/sirmaur5.png")
#inset image   
with st.container():
     image_column, text_column = st.columns((1,2))
     with image_column: 
          #image will be put here
          st.image(img_sirmaur5) 
     with text_column:
          #insert text details
          st.subheader("Paonta Sahib Gurudwara")
          st.write("Location:Paonta ")
          st.write("This revered site is closely associated with Guru Gobind Singh Ji, the tenth Sikh Guru, who visited here in the early 1700s")
          st.write("Significance: Serves as a place of worship and community gathering for the local Sikh population.")

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
          st.write("---")


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