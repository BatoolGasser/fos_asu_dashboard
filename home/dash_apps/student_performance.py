# Libraries
import dash
from dash import dcc, html, Output, Input, State
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
from dash_extensions import Lottie
from ..views import get_student_data
from django.shortcuts import get_object_or_404

# Getting Data
from home.models import Student

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = DjangoDash('student_performance', external_stylesheets=[dbc.themes.SPACELAB, dbc.icons.FONT_AWESOME,
                                                           dbc.icons.BOOTSTRAP])


app.layout = html.Div([
            html.Div([
                html.H1('Square Root Slider Graph'),
                dbc.Card([
                    dbc.CardBody(id='student-warnings-data')  # Placeholder for data
                ]),
                dcc.Graph(id='slider-graph', animate=True, style={"backgroundColor": "#1a2d46", 'color': '#ffffff'}),
                dcc.Slider(
                    id='slider-updatemode',
                    marks={i: '{}'.format(i) for i in range(20)},
                    max=20,
                    value=2,
                    step=1,
                    updatemode='drag',
                ),

                dbc.Card([
                    dbc.CardHeader(
                        "Iam the rank"
                        # Lottie(options=dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice')),
                        #        width="37%", height="53%", url="https://assets1.lottiefiles.com/packages/lf20_cv6rdeii.json"),
                        # style={'background': 'white'}
                    ),
                    dbc.CardBody([
                        html.H6('Rank', style={'font-weight': '900', 'color': 'white', 'font-size': '19px',
                                               'margin-top': '5px'}),
                        html.H2("heheheh", style={'color': 'white'})
                    ], style={'textAlign': 'center', 'background': '#007bff'})
                ], style={"background-color": "black"}),

                dbc.Card([
                    dbc.CardHeader(
                        "Iam the rank"
                        # Lottie(options=dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice')),
                        #        width="37%", height="53%", url="https://assets1.lottiefiles.com/packages/lf20_cv6rdeii.json"),
                        # style={'background': 'white'}
                    ),
                    dbc.CardBody([
                        html.H6('Rank', style={'font-weight': '900', 'color': 'white', 'font-size': '19px',
                                               'margin-top': '5px'}),
                        html.H2("heheheh", style={'color': 'white'})
                    ], style={'textAlign': 'center', 'background': '#007bff'})
                ], style={"background-color": "black"}),
            ])
        ])


# @app.callback(
#     Output('slider-graph', 'figure'),
#     [Input('slider-updatemode', 'value')])
# def display_value(value):
#     x = []
#     for i in range(value):
#         x.append(i)
#
#     y = []
#     for i in range(value):
#         y.append(i * i)
#
#     graph = go.Scatter(
#         x=x,
#         y=y,
#         name='Manipulate Graph'
#     )
#     layout = go.Layout(
#         paper_bgcolor='#27293d',
#         plot_bgcolor='rgba(0,0,0,0)',
#         xaxis=dict(range=[min(x), max(x)]),
#         yaxis=dict(range=[min(y), max(y)]),
#         font=dict(color='white'),
#
#     )
#     return {'data': [graph], 'layout': layout}
