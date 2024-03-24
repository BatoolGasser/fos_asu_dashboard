# Libraries
import dash
from dash import dcc, html, Output, Input, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
from dash_extensions import Lottie
from ..views import get_student_data
from django.shortcuts import get_object_or_404

# Getting Data
from home.models import Student

app = DjangoDash('student_register', external_stylesheets=[dbc.themes.SPACELAB, dbc.icons.FONT_AWESOME,
                                                           dbc.icons.BOOTSTRAP])

app.layout = html.Div([
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                    "For More Information through Registration Process",
                ], style={'color': '#007bff', 'font-weight': '600', 'font-size': '18px', "background": "none"}),
                dbc.CardBody([
                    html.Div(children=[
                        html.Div(id='graphs-section', children=[
                            dcc.Graph(id='Graph1_Track',
                                      style={'width': '691px', 'height': '370px'})])
                    ])
                ], style={'padding': '0px'}),
                dbc.CardFooter([
                    html.Label("Conclusion",
                               style={'color': '#007bff', 'font-weight': '600', 'font-size': '18px'}),
                    html.Div(children=[],
                             id="conclusion1_track",
                             style={
                                 "white-space": "pre-wrap",
                                 "width": "668pxx",  # set to the desired width
                                 "height": "100px",  # set to the desired height
                                 "overflow-y": "auto",
                                 # add this property to enable vertical scrolling when the content exceeds the height
                                 "scrollbar-color": "gray #f0f0f0",
                                 # set the color of the scrollbar track and thumb
                                 "scrollbar-width": "thin",  # set the width of the scrollbar track and thumb
                             })
                ], style={"background": "none"})
            ]),
        ]),
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    html.Div(children=[
                        html.I(className="fa-solid fa-book", style={'color': '#007bff'}),
                        html.Label("Course", style={'padding': '5px', 'font-weight': '600'})
                    ], className="d-inline"),

                    dcc.Dropdown(
                        id='filter1-dpdn_track',
                        options=["COMP 104", "COMP 106", "STAT 202"],
                        value="COMP 104"
                    ),
                ], style={'height': '100%'}),
                dbc.Col([
                    html.Div(children=[
                        html.I(className="fa-solid fa-user-group", style={'color': '#007bff'}),
                        html.Label("Doctor", style={'padding': '5px', 'font-weight': '600'})
                    ], className="d-inline"),

                    dcc.Dropdown(
                        id='filter2-dpdn_track',
                        options=["Mohamed Fakhry", "Ahmed Mohamed"],
                        value="Mohamed Fakhry",
                        style={'width': '230px'}
                    ),
                ])
            ], style={'flex-wrap': 'nowrap', }),
            dbc.Row([
                html.Div(
                    children=[
                        html.I(className="bi bi-mortarboard-fill", style={'color': '#007bff'}),
                        html.Label("GPA Range", style={'padding': '5px', 'font-weight': '600'}),
                    ], className="d-inline"),

                dcc.RangeSlider(
                    id='gpa-range-slider-track',
                    min=0, max=4, step=0.01,
                    marks={0: '0', 1: '1', 2: '2', 3: '3', 4: '4'},
                    value=[0, 4]
                ),
                html.Div(id='slider-output-container'),

            ]),
            dbc.Row([
                html.Div(
                    children=[
                        html.I(className="bi bi-calendar4-range", style={'color': '#007bff'}),
                        html.Label("Year Range", style={'padding': '5px', 'font-weight': '600'}),
                    ]
                ),

                dcc.RangeSlider(
                    id='year-range-slider-track',
                    min=2017, max=2022, step=1,
                    marks={2017: '2017', 2018: '2018', 2019: '2019', 2020: '2020', 2021: '2021', 2022: '2022'},
                    value=[2017, 2022]
                ),
            ]),
            dbc.Row([
                html.Div(children=[
                    html.Div(id='add-course', children=[
                        dbc.Button("Filter By Completed Course", outline=True, color="primary",
                                   className="me-1",
                                   id="add-btn", n_clicks=0,
                                   style={'margin-top': '10px',
                                          }),

                    ], style={'margin-top': '17px'}),
                    dbc.Button('Clear', outline=True, color="primary", className="me-1",
                               id='clear-btn', n_clicks=0,
                               style={
                                   'margin-bottom': '10px',
                                   'margin-top': '-57px',
                                   'margin-left': '253px',
                                   'width': '100px',
                               }),
                    html.Div(id="dropdown-container-output-div"),
                    html.Div(id='container', children=[]),
                ])
            ])
        ])
    ], style={'border': '2px solid #ededed', 'box-shadow': '4px 5px 21px -7px rgb(31 84 173)',
              'margin-bottom': '20px'}),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                    "Student Who Register in Courses in Same Semester"
                ], style={'color': '#007bff', 'font-weight': '600', 'font-size': '18px', "background": "none"}),
                dbc.CardBody([
                    html.Div(children=[
                        html.Div(id='graphs-section', children=[
                            dcc.Graph(id='Graph2_Track',
                                      # figure=fig2,
                                      style={'width': '691px', 'height': '370px'})])
                    ])
                ], style={'padding': '0px'}),
                # dbc.CardFooter([
                #     html.Label("Conclusion",
                #                style={'color': '#007bff', 'font-weight': '600', 'font-size': '18px'}),
                # ], style={"background": "none"})
            ], style={
                "border-top": "0px",
                "border-radius": "0px",
                "border-left": "0px",
                "border-right": "0px"
            })
        ], style={'height': '100%'}),

        dbc.Col([
            dbc.Row([
                dbc.Col([
                    html.Div(children=[
                        html.I(className="fa-solid fa-book", style={'color': '#007bff'}),
                        html.Label("Course", style={'padding': '5px', 'font-weight': '600'})
                    ], className="d-inline"),

                    dcc.Dropdown(
                        id='filter1-dpdn2_track',
                        options=["COMP202", "COMP 104", "STAT 202"],
                        multi=True
                    ),
                ], style={'height': '100%'}),
            ], style={'flex-wrap': 'nowrap', }),

            dbc.Row([
                dbc.Button("Update", outline=True, color="primary", className="me-1", id="update-btn",
                           style={'width': '208px', 'margin-left': '11px', 'margin-top': '15px',
                                  'margin-bottom': '13px'})
            ]),
            dbc.Row([
                html.Div(
                    children=[
                        html.I(className="bi bi-mortarboard-fill", style={'color': '#007bff'}),
                        html.Label("GPA Range", style={'padding': '5px', 'font-weight': '600'}),
                    ], className="d-inline"),

                dcc.RangeSlider(
                    id='gpa-range-slider2-track',
                    min=0, max=4, step=0.01,
                    marks={0: '0', 1: '1', 2: '2', 3: '3', 4: '4'},
                    value=[0, 4]
                ),
                html.Div(id='slider-output-container2'),
            ]),

            dbc.Row([
                html.Div(
                    children=[
                        html.I(className="bi bi-calendar4-range", style={'color': '#007bff'}),
                        html.Label("Year Range", style={'padding': '5px', 'font-weight': '600'}),
                    ]
                ),

                dcc.RangeSlider(
                    id='year-range-slider2-track',
                    min=2017, max=2022, step=1,
                    marks={2017: '2017', 2018: '2018', 2019: '2019', 2020: '2020', 2021: '2021', 2022: '2022'},
                    value=[2017, 2022]
                ),
            ])
        ])
    ])
], style={'border': '2px solid #ededed', 'box-shadow': 'rgb(31 84 173) -5px -3px 13px -7px', 'margin-top': '80px'})


# ########### CALLBACK : GPA Range Slider Content ####################
@app.callback(
    Output('slider-output-container', 'children'),
    Input('gpa-range-slider-track', 'value'))
def update_output(value):
    return 'You have selected "{}"'.format(value)


############# CALLBACK : Filter By Courses ################
@app.callback(
    Output(component_id='container', component_property='children'),
    [Input(component_id='add-btn', component_property='n_clicks'),
     Input(component_id='clear-btn', component_property='n_clicks')],
    [State(component_id='container', component_property='children')]
)
def add_course_to_container(n_clicks, clear_clicks, container):
    ctx = dash.callback_context
    if not ctx.triggered:
        raise PreventUpdate
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if button_id == 'add-btn':
            if n_clicks is None or n_clicks == 0:
                raise PreventUpdate
            else:
                return container + new_courses_container(n_clicks) + grades_checklists(n_clicks)
        elif button_id == 'clear-btn':
            return []
        else:
            raise PreventUpdate


def new_courses_container(n_clicks):
    if n_clicks is None or n_clicks == 0:
        raise PreventUpdate
    else:
        my_dpdn = dcc.Dropdown(
            id={"type": "Courses-filter-dropdown", "index": n_clicks},
            options=["COMP 303", "COMP 202", "STAT 303", "STAT 405"],
            value="COMP 303",
            style={'width': '150px',
                   'display': 'inline-block'
                   })
        return [my_dpdn]


def grades_checklists(n_clicks):
    if n_clicks is None or n_clicks == 0:
        raise PreventUpdate
    else:
        my_checklist = dcc.Checklist(
            id={"type": "Grades-filter-checklist", "index": n_clicks},
            options=[
                {'label': 'A', 'value': 'A'},
                {'label': 'A-', 'value': 'A-'},
                {'label': 'B+', 'value': 'B+'},
                {'label': 'B', 'value': 'B'},
                {'label': 'C+', 'value': 'C+'},
                {'label': 'C', 'value': 'C'},
                {'label': 'D', 'value': 'D'},
                {'label': 'F', 'value': 'F'}],
            value=['A', 'B', 'C'],
            style={
                'vertical-align': 'super',
                'padding-left': '4px',
                'display': 'inline-flex'
            }
        )
        return [my_checklist]


def clear_button():
    my_button = html.Button('Clear', id='clear-btn', style={'margin-left': '10px'})
    return my_button


# ########### CALLBACK : GPA Range Slider Content 2 ####################
@app.callback(
    Output('slider-output-container2', 'children'),
    Input('gpa-range-slider2-track', 'value'))
def update_output(value):
    return 'You have selected "{}"'.format(value)
