import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Sample sensor data
df = pd.DataFrame({
    'name': ['Sensor 1', 'Sensor 2'],
    'lat': [16.8471, 16.7904],
    'lon': [96.1735, 96.1715]
})

# Yangon map
m = folium.Map(location=[16.8409, 96.1735], zoom_start=12)

for i, row in df.iterrows():
    folium.Marker(
        location=[row['lat'], row['lon']],
        popup=row['name']
    ).add_to(m)

st_folium(m, width=700, height=500)
