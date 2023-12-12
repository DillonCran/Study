import pandas as pd
import numpy as np
import plotly

# %matplotlib inline
import cufflinks as cf
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

print(__version__)  # requires version >= 1.9.0


cf.go_offline()  # access to plotly offline mode

# data
df = pd.DataFrame(np.random.randn(100, 4), columns="A B C D".split())
print(df.head())
df2 = pd.DataFrame({"category": ["a", "b", "c"], "values": [32, 43, 50]})
print(df2.head())


df.iplot(kind="scatter", x="A", y="B", mode="markers", size=10)

# This is how to get plotly working outside of jupyter notebook
import plotly.express as px

fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])
fig.write_html("first_figure.html", auto_open=True)
