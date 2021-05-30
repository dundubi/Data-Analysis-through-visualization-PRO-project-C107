import pandas as pd
import plotly.graph_objects as go

readData = pd.read_csv("data1.csv")
z = readData.groupby("level")["attempt"].mean()
print(z)

fig = go.Figure(go.Scatter(z , x = ['TRL_xsl', 'TRL_abc', 'TRL_xyz', 'TRL_zet'], y = ['Level 1', 'Level 2', 'Level 3', 'Level 4'],orientation = 'h', color = 'attempt'))
fig.show()