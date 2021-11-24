# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 20:16:31 2021

@author: MorenoData
"""
#LIBRERIAS
import folium
import pandas as pd
import webbrowser
import geopandas as gpd ###Instalar Geopandas es un proceso a parte
webbrowser.open('https://www.python.org')

from folium.plugins import MarkerCluster #Para agrupar los puntos espaciales o Farmacias

#PUNTOS ESPACIALES
farmacias = pd.read_excel('C:/Users/MorenoData/Dropbox/BD-Proyectos/Python/FP.xlsx')

#DEPLOY MAP
mapa = folium.Map(location=[18.5109567,-69.8709901],
                  zoom_start=12)


#Capa de Farmacias

codigo = list (farmacias["CODIGO"])
latitud = list (farmacias["Latitud"])
longitud = list (farmacias["Longitud"])
fpp = list (farmacias["FARMACIAS DEL PUEBLO"])
color_e = list (farmacias["COLOR_EXTERNO"])
color_i = list (farmacias["COLOR_INTERNO"])
icons = list (farmacias["ICONO"])
prefx = list (farmacias["PREFIX"])

mc_fp = MarkerCluster ()

for cod,lat,lon,fp,c_e,c_i,ico,pref in zip(codigo,latitud,longitud,fpp,color_e,color_i,icons,prefx):
    mc_fp.add_child(folium.Marker(location=[lat,lon],
    popup="<b>Codigo: </b>"+str(cod)+ "<br> <b> Farmacia: <b> "+fp+"</br>", max_width=4000, min_width=4000,
    icon=folium.Icon(color=c_e,
    icon_color=c_i,
    icon=ico,
    prefix=pref)))
    

Capa_FP = folium.FeatureGroup(name='Farmacias')
mc_fp.add_to(Capa_FP)

mapa.add_child(Capa_FP)

#Cap-a Provincias------------------------------------------------------------------------------------
prov = gpd.read_file('C:/Users/MorenoData/Dropbox/BD-Proyectos/Python/PRO.geojson')
style = {'fillColor': '#DF0101', 'lineColor':'#00FFFFF'}
prov_layer=folium.GeoJson(
    prov,
    name='Provincias',
    style_function=lambda x: style,
    tooltip= folium.GeoJsonTooltip(
      fields=['PROV','TOPONIMIA'],
      aliases=['No.:','Nombre: '],
      localize=True  
    )).add_to(mapa)



#Capas del Mapa Base--------
folium.TileLayer('Stamen Terrain').add_to(mapa)
folium.TileLayer('Cartodb Positron').add_to(mapa)
folium.TileLayer('CartoDB dark_matter').add_to(mapa)
folium.TileLayer('stamentoner').add_to(mapa)

folium.LayerControl(position='topleft').add_to(mapa)




mapa.save('mimapa.html')
webbrowser.open('mimapa.html')


