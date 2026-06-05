import folium
import pandas as pd

# -----------------------------
# 1. wells data
# -----------------------------
data = {
    "wells" : ["well A","well B","well C"],
    "Latitude" : [30.5086, 30.7, 30.9],
   "Longitude" : [47.7804, 48.0, 47.6],
   "Production_BOPD" : [5000,7000,3000]
}
df = pd.DataFrame(data)


# -----------------------------
# 2.create map
# -----------------------------
map_oil = folium.Map(location=[30.6, 47.8],zoom_start=7)

# -----------------------------
# 3. add wells
# -----------------------------
for i in range(len(df)):
    if df['Production_BOPD'][i] > 6000:
        color = 'green'
    elif df['Production_BOPD'][i] > 4000:
        color = 'orange'
    else:
        color = 'red'

    # marker
    folium.Marker(
        location=[df['Latitude'][i],df['Longitude'][i]],
        popup=f"""
        <b> well: </b>{df['wells'][i]} <br>
        <b> production: </b> {df['Production_BOPD'][i]} BOPD
        """,
        tooltip=df['wells'][i],
        icon=folium.Icon(color=color)
    ).add_to(map_oil)

    #Drainage Radius
    folium.Circle(
        location=[df['Latitude'][i],df['Longitude'][i]],
        radius=1000,
        color=color,
        fill = True,
        fill_opacity=0.3
    ).add_to(map_oil)

    # pipeline
    pipeline_cord = df[['Latitude','Longitude']].values.tolist()
    folium.PolyLine(
        locations=pipeline_cord,
        color ="blue",
        weight = 0.3,
        tooltip="pipeline"
    ).add_to(map_oil)


# -----------------------------
# 6. layer map
# -----------------------------
folium.TileLayer(tiles='Stamen Terrain',
                 attr='Map tiles by Stamen Design, CC BY 3.0 — Map data © OpenStreetMap').add_to(map_oil)
#folium.TileLayer('CartoDB positron').add_to(map_oil)

# -----------------------------
# 7. control lyaer
# -----------------------------
folium.LayerControl().add_to(map_oil)

# -----------------------------
# 8. save map
# -----------------------------
map_oil.save("map_oil.html")
import pipreqs
