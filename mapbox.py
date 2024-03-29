#%%

import plotly.offline as pyo
import plotly.graph_objs as go

#%%

color2 = ['red']*13
color2[0] = 'blue'
color2[-1] = 'green'

#%%

# obs: criar uma conta e testar o próprio token
mapbox_access_token = 'pk.eyJ1IjoibWFyaW8tdWZmIiwiYSI6ImNqdWl3ZmFqNjA1MGY0M280OTdka3RsNGEifQ.hvLN_LDGfu5F_XAkhz0tZg'

data = [
    go.Scattermapbox(
        lat=['38.91427','38.91538','38.91458',
             '38.92239','38.93222','38.90842',
             '38.91931','38.93260','38.91368',
             '38.88516','38.921894','38.93206',
             '38.91275'],
        lon=['-77.02827','-77.02013','-77.03155',
             '-77.04227','-77.02854','-77.02419',
             '-77.02518','-77.03304','-77.04509',
             '-76.99656','-77.042438','-77.02821',
             '-77.01239'],
        mode='markers',
        marker= go.scattermapbox.Marker(
            size=9,
            color=color2
        ),
        text=["The coffee bar","Bistro Bohem","Black Cat",
             "Snap","Columbia Heights Coffee","Azi's Cafe",
             "Blind Dog Cafe","Le Caprice","Filter",
             "Peregrine","Tryst","The Coupe",
             "Big Bear Cafe"],
    )
]

layout = go.Layout(
    autosize=True,
    hovermode='closest',
    mapbox=go.layout.Mapbox(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=go.layout.mapbox.Center(
            lat=38.92,
            lon=-77.07
        ),
        pitch=0,
        zoom=10,
        style="satellite-streets"
    ),
)

fig = go.Figure(data=data, layout=layout)
pyo.iplot(fig, filename='Multiple Mapbox')

#%%
