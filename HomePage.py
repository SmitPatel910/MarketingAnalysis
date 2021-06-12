import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import pandas as pd
import dash_html_components as html
from homeNavbar import Navbar
import plotly.graph_objs as go


#Initialize Header and Footer
nav = Navbar()

#Initialize Dash app
app = dash.Dash(__name__, external_stylesheets = [dbc.themes.UNITED])
app.config.suppress_callback_exceptions = True

output_statebargraph = html.Div(className = "output_bargraph",id = 'output_statebargraph',
                children = [],
                )

output_statelinegraph = html.Div(className = "output_linegraph",id = 'output_statelinegraph',
                children = [],
                )

output_statepieconfirmedgraph = html.Div(className = "output_statepieconfirmedgraph",id = 'output_statepieconfirmedgraph',
                children = [],
                )

output_statepierecoveredgraph = html.Div(className = "output_statepierecoveredgraph",id = 'output_statepierecoveredgraph',
                children = [],
                )

output_statepiedeathgraph = html.Div(className = "output_statepiedeceasedgraph",id = 'output_statepiedeceasedgraph',
                children = [],
                )

output_statepieactivegraph = html.Div(className = "output_statepieactivegraph",id = 'output_statepieactivegraph',
                children = [],
                )

#Set main Content
body = dbc.Container(
    [
       dbc.Row(
           [
               dbc.Col(
                  [
                     html.H1("Superhero U"),
                     html.H3(
                         """\
Driven towards instilling a sense of innovation and inventiveness among our youth, Superhero U was an endeavor to empower imaginative and fervent young minds to make the best possible use of their skills and creativity.Influenced by the UN's mission “to promote prosperity while protecting the planet”, Superhero U was a competitive event that was targeted towards providing an encouraging and equal educational opportunity to the budding stars"""
                           ),
                           html.A(html.Button('VISUALIZOR',className='Visualizor'),
    href='/visualize',target='_blank')
                                              
                   ],
                  md=5,
               ),
              dbc.Col(
                 [
                     html.H2("Track and Visualize different Ad Campaign on basis of Audience Interaction"),
                     html.Img(
                            className="logo1", src=app.get_asset_url("globalInsight3.png")
                        )

                        ]
                     ),
                ]
            )
       ],
className="mt-4",
)




#define MainFunction to call
def Homepage():
    layout = html.Div([
    nav,
    body
    ])
    return layout




    
