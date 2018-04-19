#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import plotly.offline as offline
import plotly.graph_objs as go
offline.init_notebook_mode()

if __name__ == "__main__":
    model1_precision = [0.1, 0.2]
    model1_recall = [0.7, 0.8]
    model2_precision = [0.1, 0.3]
    model2_recall = [0.5, 0.6]

    trace0 = go.Scatter(
        x = np.array(model1_recall),
        y = np.array(model1_precision),
        name = "model1",
        mode = "markers",
        marker = dict(size=10, color="rgb(255, 0, 255)"))

    trace1 = go.Scatter(
        x = np.array(model2_recall),
        y = np.array(model2_precision),
        name = "model2",
        mode = "markers",
        marker = dict(size=10, color="rgb(255, 165, 0)"))

    layout = go.Layout(
        title='preicision recall trade off curve',
        xaxis=dict(title='recall', range=[0, 1]),
        yaxis=dict(title='precision', range=[0, 1]),
        showlegend=True)

    data = [trace0, trace1]
    fig = dict(data=data, layout=layout)

    offline.iplot(fig, filename="tradeoff_curve", image="png")