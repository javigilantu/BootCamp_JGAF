import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode()
import seaborn as sns
import matplotlib as plt 
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="my_application")
import folium
from folium.plugins import MarkerCluster
import pandas as pd 
import numpy as np

def swarmplot(y , x, data, color):
    g = sns.swarmplot(y = y,
              x = x,
              data = data,
              color = color)
    # remove the top and right line in graph
    sns.despine()
    return g.figure.set_size_inches(14,10)


def figure(x , y, title):
    fig = go.Figure(data=[go.Scatter(
    x=x, y=y,
    mode='markers')])
    fig.update_layout(title=title)
    return fig.show()

def cordinates_ISO3(data):
    def geolocate(Name):
        try:
            # Geolocate the center of the country
            loc = geolocator.geocode(Name)
            # And return latitude and longitude
            return (loc.latitude, loc.longitude)
        except:
            # Return missing value
            return np.nan

    location = data.apply(geolocate)
    location= pd.DataFrame(location)
    location = location.Name.apply(lambda x : list(x))
    location_= pd.DataFrame(location)
    df2 = pd.DataFrame(location_)
    df2[['lat', 'long']]= pd.DataFrame(location_.Name.tolist(), index= df2.index)
    return df2