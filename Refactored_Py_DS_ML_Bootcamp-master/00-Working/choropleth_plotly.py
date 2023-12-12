import chart_studio.plotly as py
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import numpy as np

from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

# When casting data with a dict, the keys are used as the column names and converted to strings
# The values are used as the data in the columns are aligned by the keys
data = dict(
    type="choropleth",  # type of map, choropleth is a map that uses colors to represent values
    locations=["AZ", "CA", "NY"],  # location of the data, in this case, states
    locationmode="USA-states",  # location mode, in this case, USA states. Can also be country names
    colorscale="Portland",  # color scale, can be any color scale
    text=[
        "text1",
        "text2",
        "text3",
    ],  # text that will be displayed when hovering over the data (aligned with locations)
    z=[
        1.0,
        2.0,
        3.0,
    ],  # data that will be represented by the color scale, aligned with locations
    colorbar={"title": "Colorbar Title Goes Here"},  # color bar title
)
print(data)

# layout/scope of the map, dictates what map the data will be plotted on
layout = dict(geo={"scope": "usa"})

# create the map
# assign the data and layout to a figure object. pass data as a list []
choromap = go.Figure(data=[data], layout=layout)  # .show()
choromap.show()

# real data
df = pd.read_csv(
    "D:\\Projects\Refactored_Py_DS_ML_Bootcamp-master\\09-Geographical-Plotting\\2011_US_AGRI_Exports"
)
# data for df
data2 = dict(
    type="choropleth",
    colorscale="ylorbr",
    locations=df["code"],
    locationmode="USA-states",
    z=df["total exports"],
    text=df["text"],
    colorbar={"title": "Millions USD"},
    marker=dict(line=dict(color="rgb(255,255,255)", width=2)),
)

layour2 = dict(
    title="2011 US Agriculture Exports by State",
    geo=dict(scope="usa", showlakes=True, lakecolor="rgb(85,173,240)"),
)

choromap2 = go.Figure(data=[data2], layout=layour2)
choromap2.show()

df2 = pd.read_csv(
    "D:\\Projects\Refactored_Py_DS_ML_Bootcamp-master\\09-Geographical-Plotting\\2014_World_GDP"
)

data3 = dict(
    type="choropleth",
    locations=df2["CODE"],
    z=df2["GDP (BILLIONS)"],
    text=df2["COUNTRY"],
    colorbar={"title": "GDP Billions US"},
)

layout3 = dict(
    title="2014 Global GDP", geo=dict(showframe=False, projection={"type": "mercator"})
)

choromap3 = go.Figure(data=[data3], layout=layout3)
choromap3.show()
