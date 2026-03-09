import streamlit as st
import folium
from streamlit.components.v1 import html

st.title("Yangon IoT Sensor Map (Test)")

# Yangon center
center = [16.8409, 96.1735]

# Create map
m = folium.Map(location=center, zoom_start=13)

# Sensor nodes
folium.Marker([16.8409, 96.1735], popup="Sensor Node 1").add_to(m)
folium.Marker([16.8500, 96.1800], popup="Sensor Node 2").add_to(m)

# Convert map to HTML and show in Streamlit
map_html = m._repr_html_()
html(map_html, height=500)
