import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from sqlalchemy import create_engine

# 1️⃣ Postgres Database connection
DB_USER = "iot_user"
DB_PASS = "your_password_here"
DB_HOST = "dpg-d6n8b9tactks738h6t3g-a.render.com"
DB_PORT = "5432"
DB_NAME = "iot_data_9s26"

engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# 2️⃣ Load sensor data from database
query = "SELECT * FROM sensor_data;"  # latitude/longitude columns 
df = pd.read_sql(query, engine)

# 3️⃣ Yangon filter (latitude/longitude)
yangon_df = df[
    (df['lat'] >= 16.75) & (df['lat'] <= 16.95) &
    (df['lon'] >= 96.10) & (df['lon'] <= 96.25)
]

# 4️⃣ Map setup
yangon_location = [16.8409, 96.1735]
m = folium.Map(location=yangon_location, zoom_start=12)

# 5️⃣ Add markers
for index, row in yangon_df.iterrows():
    folium.Marker(
        location=[row['lat'], row['lon']],
        popup=f"{row['name']}: {row['value']}",
        icon=folium.Icon(color="blue")
    ).add_to(m)

# 6️⃣ Display on Streamlit
st.title("Yangon IoT Sensor Map")
st_folium(m, width=700, height=500)
