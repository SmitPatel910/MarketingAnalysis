import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED])

def Navbar():
     navbar = dbc.NavbarSimple(
          className = "navbar",
           children=[
               dbc.Row(
                [
                    dbc.Col(html.Img(className="globallogo", src=app.get_asset_url("glabalshala.png"), height="30px")),
                
                ],
                align="center"
                
               )
              
                  ],
          brand="GlobalShala Marketing",
          brand_href="/home",
          sticky="top",
          color="#292B33",
          dark=True,
          expand='xl',
          id="navbar"
        )
     
     return navbar
 
