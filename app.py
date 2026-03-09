import streamlit as st
import folium
from streamlit_folium import st_folium

st.title("Yangon IoT Sensor Map")

# Yangon location example
lat = 16.8661
lon = 96.1951

m = folium.Map(location=[lat, lon], zoom_start=12)

folium.Marker(
    [lat, lon],
    popup="Sensor Location"
).add_to(m)

st_folium(m, width=700, height=500)
