import math
import pandas as pd
import numpy as np
import flask
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px
from dash.dependencies import Input, Output, State
from homeNavbar import Navbar
import sys


nav = Navbar()


output_piegraph = html.Div(className = "output_piegraph",id = 'output_piegraph',
                children = [],
                )
output_bargraph = html.Div(className = "output_bargraph",id = 'output_bargraph',
                children = [],
                )
output_linegraph = html.Div(className = "output_linegraph",id = 'output_linegraph',
                children = [],
                )

header = html.H1(
    'Select the FEATURE of Campaign to see Insights!!!!'
)

def Campaign_Visualizor(feature_dropdown):
    layout = html.Div([
        nav,
        header,
        feature_dropdown,
        output_piegraph,
        output_bargraph,
        output_linegraph
    ])
    return layout

       
def visualize_bargraph(feature):
    if feature is not None:
        marketingData_grouped = fetchFeaturesAPI(feature)
        marketingData = marketingData_grouped.to_frame()
        fig = go.Figure(data=[
        go.Bar(name='CONFIRMED',x= marketingData.index,y=marketingData[feature]),
        ])
        fig.update_layout(barmode='stack')
        fig.layout.plot_bgcolor = "#1A1C23";
        fig.layout.paper_bgcolor = "#1A1C23";
        fig.layout.autosize= True;
        fig.update_layout(
        title=feature+ " for Ad Campaign",
        xaxis_title="Ad Campaign",
        yaxis_title="Audience " +feature,
        font=dict(
            color="#DCF7F7"
        )
        )
        fig2 = dcc.Graph(
            figure=fig
        )
        return fig2

def visualize_linegraph(feature):
    if feature is not None:
        marketingData_grouped = fetchFeaturesAPI(feature)
        marketingData = marketingData_grouped.to_frame()
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=marketingData.index,
            y=marketingData[feature],
            
            line_color='#0557EB',
            name='Confirmed',
        ))
        

        fig.update_traces(mode='lines')
        fig.layout.plot_bgcolor = "#1A1C23";
        fig.layout.paper_bgcolor = "#1A1C23";
        fig.layout.autosize= True;
        fig.update_layout(
        xaxis_title="AD CAMPAIGN",
        yaxis_title="Audience " +feature,
        font=dict(
            color="#DCF7F7"
        )
        )
        fig2 = dcc.Graph(
            figure=fig
        )
        
        return fig2
    
def visualize_piegraph(feature):
    if feature is not None:
        marketingData_grouped = fetchFeaturesAPI(feature)
        print (feature)
        marketingData = marketingData_grouped.to_frame()
        print (marketingData)
        data = [
        {
            'values': marketingData[feature],
            'type': 'pie',
            'labels': marketingData.index
        },
        ]
        fig = dcc.Graph(
            id='graph',
            figure={
                'data': data,
                'layout': {
                "paper_bgcolor": "#1A1C23",
                "plot_bgcolor": "#1A1C23",
                "autosize": True,
                 "title": feature+ " for Ad Campaign",
            "font":dict(
                color="#DCF7F7"
            )
                }
            }
        )
        return fig


def fetchFeaturesAPI(feature):
    marketingData = pd.read_excel("marketingTeamData.xlsx")
    marketingData_grouped =  marketingData.groupby(['Campaign ID'])[feature].sum()
    return marketingData_grouped;



def featurerender():
    dis = ['Reach','Impressions','Frequency','Clicks','Unique Clicks','Unique Link Clicks (ULC)','Click-Through Rate (CTR)','Unique Click-Through Rate (Unique CTR)',
           'Amount Spent in INR','Cost Per Click (CPC)','Cost per Result (CPR)']
    options = [{'label':x, 'value': x} for x in dis]
    feature_dropdown = html.Div(dcc.Dropdown(
        id = 'feature_dropdown',
        options = options,
        placeholder="Select FEATURE"
    ))
    return feature_dropdown
    





    
