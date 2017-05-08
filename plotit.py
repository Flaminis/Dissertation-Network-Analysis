import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as ff
from operator import itemgetter

def distplot(distdata,name='Basic Distplot'):
    group_labels = ['distplot']
    colors = ['rgb(0, 200, 200)']
    fig = ff.create_distplot([distdata], group_labels,bin_size=[.4],colors=colors)
    py.plot(fig, filename=name)
def barplot(baradata,name='Dot-Plot'):
    ddlen = len(baradata)
    botline = range(0,ddlen)
    trace = go.Bar(
        x = botline,
        y = baradata,
        name = 'markers'
    )
    trace1 = go.Scatter(
        x = botline,
        y = baradata,
        mode = 'lines+markers',
        name = 'lines+markers'
    )
    data = [trace,trace1]
    py.plot(data, filename=name)
def barplotduo(baradata,name='Dot-Plot'):
    
    ddlen = len(baradata)
    botline = range(0,ddlen)
    trace = go.Bar(
        x = botline,
        y = map(itemgetter(0),baradata),
        text = map(itemgetter(1),baradata),
        name = 'markers'
    )
    trace1 = go.Scatter(
        x = botline,
        y = map(itemgetter(0),baradata),
        mode = 'lines+markers',
        name = 'lines+markers'
    )
    data = [trace,trace1]
    py.plot(data, filename=name)
