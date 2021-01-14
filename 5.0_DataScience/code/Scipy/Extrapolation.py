import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.tools import FigureFactory as FF

#sudo pip3 install plotly
#pip3 install plotly --upgrade

#1D Extrapolation
points = np.array([(1, 1), (2, 4), (3, 1), (9, 3)])

x = points[:,0]
y = points[:,1]

z = np.polyfit(x, y, 3)
f = np.poly1d(z)

x_new = np.linspace(0, 10, 50)
y_new = f(x_new)

trace1 = go.Scatter(
    x=x,
    y=y,
    mode='markers',
    name='Data',
    marker=dict(
        size=12
    )
)

trace2 = go.Scatter(
    x=x_new,
    y=y_new,
    mode='lines',
    name='Fit'
)

annotation = go.Annotation(
    x=6,
    y=-4.5,
    text='$0.43X^3 - 0.56X^2 + 16.78X + 10.61$',
    showarrow=False
)

layout = go.Layout(
    title='Polynomial Fit in Python',
    annotations=[annotation]
)

data = [trace1, trace2]
fig = go.Figure(data=data, layout=layout)

py.iplot(fig, filename='interpolation-and-extrapolation')


