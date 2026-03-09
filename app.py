import streamlit as st
import folium
from streamlit_folium import st_folium

st.title("Yangon Sensor Map")

# Yangon center
center = [16.8409, 96.1735]

# Create map
m = folium.Map(location=center, zoom_start=13)

# Example sensors
folium.Marker(
    [16.8409, 96.1735],
    popup="Sensor Node 1",
    icon=folium.Icon(color="red")
).add_to(m)

folium.Marker(
    [16.8500, 96.1800],
    popup="Sensor Node 2",
    icon=folium.Icon(color="blue")
).add_to(m)

# Show map
st_folium(m, width=700, height=500)
