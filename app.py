from dash import Dash, dash_table, dcc, html, Input, Output, callback
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.express as px
from datetime import datetime
import plotly.graph_objects as go
df_grp_dash=pd.read_csv('pie_states_dash.csv')
df_table = pd.read_csv('css_states_dash.csv')
df_states = pd.read_csv('css_states.csv')
df_time_lg = pd.read_csv('time.csv')

sram_df_grp_dash=pd.read_csv('sram_pie_states_dash.csv')
sram_df_table = pd.read_csv('sram_css_states_dash.csv')
sram_df_states = pd.read_csv('sram_css_states.csv')
sram_df_time_lg = pd.read_csv('sram_time.csv')

fcb_df_grp_dash=pd.read_csv('fcb_pie_states_dash.csv')
fcb_df_table = pd.read_csv('fcb_css_states_dash.csv')
fcb_df_states = pd.read_csv('fcb_css_states.csv')
fcb_df_time_lg = pd.read_csv('fcb_time.csv')



time_var= df_time_lg["Regression_Run_Time"]
print(time_var)

df_f = pd.read_csv('css_states.csv')
df_f = df_f[['IP', 'Test_Name', 'Status', 'Remarks']]

sram_df_f = pd.read_csv('sram_css_states.csv')
sram_df_f = sram_df_f[['Test_Name', 'Status', 'Remarks']]

fcb_df_f = pd.read_csv('fcb_css_states.csv')
fcb_df_f = fcb_df_f[['Test_Name', 'Status', 'Remarks']]

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
fig = px.pie(df_grp_dash, values='Numbers', names='Category',color = "Category",hole=.2,color_discrete_map={'Tests Passed':'#66CDAA',
                                 'Tests Under Development':'#00BFFF',                                                                           
                                 'Tests Failed':'#CD5C5C'})
fig.update_layout(title={'text': '<b>Pie Chart SoC</b>','y':1,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
font={'size': 15},
title_font_color='black',
legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="left",
    x=0.00,
))

fig_sram = px.pie(sram_df_grp_dash, values='Numbers', names='Category',color = "Category",hole=.2,color_discrete_map={'Tests Passed':'#66CDAA',
                                 'Tests Under Development':'#00BFFF',                                                                           
                                 'Tests Failed':'#CD5C5C'})
fig_sram.update_layout(title={'text': '<b>Pie Chart SRAM  (Unit Level)</b>','y':1,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
font={'size': 15},
title_font_color='black',
legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="left",
    x=0.00,
))

fig_fcb = px.pie(fcb_df_grp_dash, values='Numbers', names='Category',color = "Category",hole=.2,color_discrete_map={'Tests Passed':'#66CDAA',
                                 'Tests Under Development':'#00BFFF',                                                                           
                                 'Tests Failed':'#CD5C5C'})
fig_fcb.update_layout(title={'text': '<b>Pie Chart FCB  (Unit Level)</b>','y':1,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
font={'size': 15},
title_font_color='black',
legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="left",
    x=0.00,
))

arr =[158,158,158,158,158,158,250,250]
aarr= [21,35,39,56,65,96,139,165]
arr_f= [0,3,3,0,4,15,39,35]
arr_x=[1,2,3,4,5,6,7,8,9,10,11]
f1 = go.Figure(
    data = [
        go.Scatter(x=arr_x,y=arr, name="Tests Planned",line=dict(color="#00BFFF")),
        go.Scatter(x=arr_x,y=aarr, name="Tests Passed",line=dict(color="#66CDAA")),
        go.Scatter(x=arr_x,y=arr_f, name="Tests Failed",line=dict(color="#CD5C5C")),
    ],
    layout = {"xaxis": {"title": "Weeks"}, "yaxis": {"title": "No. of Tests"}, "title": "Weekly Statistics"}
)
f1.update_layout(title={'text': '<b>Weekly Statistics SoC</b>','y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
font={'size': 15},
title_font_color='black',
# legend=dict(
#     yanchor="top",
#     y=0.99,
#     xanchor="left",
#     x=0.00,
# ))
# width=1300,
# height=600
)
# f1.update_layout(width=int(width))

app.layout = html.Div(style = {
  'backgroundColor': '#FFFFFF',
  'fontSize' : '100'
}, children = [
    html.H1(
    children = 'RapidSilicon',
    style = {
      'textAlign': 'center',
      'color': 'Crimson',
      'fontWeight': 'bold',
      'font-size':'xx-large',
      'text-decoration-line': 'underline',
    }
    
  ),
    html.Div(children = 'Gemini SoC Tests Statistics', style = {
    'textAlign': 'center',
    # 'color': '#7FDBFF',
    'color': 'blue',
    'fontWeight': 'bold',
    'font-size':'x-large',
  }),

dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
#   html.Div(children = df_time_lg["Regression_Run_Time"], style = {
#     'textAlign': 'left',
#     'color': '#7FDBFF',
#     'fontWeight': 'bold'
#   }),
#  dcc.Graph(
#     id = 'gemini-graph-1',
#     figure = fig
#   ),
dbc.Container([
  html.Div(children = "Regression Date:   "+df_time_lg["Regression_Run_Time"], style = {
     'textAlign': 'left',
     'color': 'Black',
     'fontWeight': 'bold'
   }),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Graph(
    id = 'gemini-graph-1',
    figure = fig
  ),

html.Div(children = 'General Statistics', style = {
    'textAlign': 'center',
    # 'color': '#7FDBFF',
    'color': 'black',
    'fontWeight': 'bold',
    'font-size':'large',
  }),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
dash_table.DataTable(    style_data={
        'whiteSpace': 'normal',
        'height': 'auto',
        'textAlign': 'center',
        'lineHeight': '10px',
    },
    data=df_table.to_dict('records'), 
    columns=[{"name": i, "id": i} for i in df_table.columns],
        css=[{"selector": "input", "rule": "color:gray"}],
            # data=df.to_dict("records"),
            style_cell={"color": "gray"},
            # editable=True,
            style_data_conditional=[
                {"if": {"row_index": 0}, "backgroundColor": "#00BFFF"},
                {"if": {"row_index": 1}, "backgroundColor": "#66CDAA"},
                {"if": {"row_index": 2}, "backgroundColor": "#CD5C5C"},
                {
                    "if": {"state": "active"},
                    "backgroundColor": "inherit !important",
                    "border": "1px solid black",
                    # "color": "gray",
                },
                {
                    "if": {"state": "selected"},
                    "backgroundColor": "inherit !important",
                    # "border": "1px solid blue",
                },
        {
            'if': {
                'filter_query': '{Numbers} > 0',
                'row_index': 2,
            },
            'backgroundColor': '#CD5C5C',
            'color': 'black'
         },
            ],
        style_cell_conditional=[
        {'if': {'column_id': 'Category'},
         'width': '10%',
         'textAlign': 'center',
         'fontWeight': 'bold',
         'color': 'BLACK'},
        {'if': {'column_id': 'Numbers'},
         'width': '10%',
         'textAlign': 'center',
         'fontWeight': 'bold',
         'color': 'BLACK'},
    ]),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
# html.Div(children = 'Weekly Scatter Plot', style = {
#     'textAlign': 'left',
#     'color': 'black',
#     'fontWeight': 'bold'
#   }),
    dcc.Graph(
    id = 'gemini-graph-2',
    figure = f1
  ),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
html.Div(children = 'IP-wise Statistics', style = {
    'textAlign': 'center',
    # 'color': '#7FDBFF',
    'color': 'black',
    'fontWeight': 'bold',
    'font-size':'large',
  }),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
    # dcc.Markdown('# DataTable Tips and Tricks', style={'textAlign':'center'}),

    dbc.Label("Show number of rows:"),
     dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
    row_drop := dcc.Dropdown(value=10, clearable=False, style={'width':'35%'},
                             options=[10, 25, 50, 100]),
        dbc.Row([
        dbc.Col([
            IP_drop := dcc.Dropdown([x for x in sorted(df_f.IP.unique())])
        ], width=3),

    ], justify="between", className='mt-3 mb-4'),

    my_table := dash_table.DataTable(
        columns=[
            {'name': 'IP', 'id': 'IP', 'type': 'text'},
            {'name': 'Test_Name', 'id': 'Test_Name', 'type': 'text'},
            {'name': 'Status', 'id': 'Status', 'type': 'text'},
            {'name': 'Remarks', 'id': 'Remarks', 'type': 'text'}
        ],
        style_table={'overflowX': 'auto'},
        data=df_f.to_dict('records'),
        filter_action='native',
        page_size=10,
           style_data={
        'whiteSpace': 'normal',
        'height': 'auto',
        'textAlign': 'center',
        # 'lineHeight': '10px'
    },
            # editable=True,
            style_data_conditional=[
                {"if": {"row_index": "odd"}, "backgroundColor": "#66CDAA"},
                {"if": {"row_index": "even"}, "backgroundColor": "#66CDAA"},
                {
                    "if": {"state": "active"},
                    "backgroundColor": "inherit !important",
                    "border": "1px solid black",
                    # "color": "gray",
                },
                # {
                #     "if": {"state": "selected"},
                #     "backgroundColor": "black",
                #     # "border": "1px solid blue",
                # },
                   {"if": {"state": "selected"},
                         "backgroundColor": "inherit !important",
                          "border": "inherit !important",},
            {
            'if': {
                'filter_query': '{Status} contains "Failed"',
                'column_id': 'Status'
            },
            'backgroundColor': '#CD5C5C',
            'color': 'black'
         },
            {
            'if': {
                'filter_query': '{Status} contains "timeout"',
                'column_id': 'Status'
            },
            'backgroundColor': '#CD5C5C',
            'color': 'black'
         },

            ],
        style_cell_conditional=[
        {'if': {'column_id': 'IP'},
         'width': '10%',
         'textAlign': 'center',
            'color': 'BLACK',
            'fontWeight': 'bold'},
        {'if': {'column_id': 'Test_Name'},
         'width': '10%',
         'textAlign': 'center',
         'color': 'BLACK',
         'fontWeight': 'bold'},
                {'if': {'column_id': 'Status'},
         'width': '10%',
         'textAlign': 'center',
         'color': 'BLACK',
         'fontWeight': 'bold'},
                 {'if': {'column_id': 'Remarks'},
         'width': '50%',
         'textAlign': 'center',
         'color': 'BLACK',
         'fontWeight': 'bold'
         },
         
    ]),
html.Div(children = 'Combined Coverage Report:', style = {
    'textAlign': 'left',
    'color': 'BLACK',
    'fontWeight': 'bold'
  }),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),

 html.Div(
    
    children=[
        html.Iframe(
            src="assets/soc/dashboard.html",
            style={"height": "1067px", "width": "100%"},
        )
    ]
    
),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),

    html.Div(children = 'SRAM  (Unit Level) Tests Statistics', style = {
    'textAlign': 'center',
    # 'color': '#7FDBFF',
    'color': 'blue',
    'fontWeight': 'bold',
    'font-size':'x-large',
  }),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Graph(
    id = 'gemini-graph-sram',
    figure = fig_sram
  ),
html.Div(children = 'General Statistics SRAM  (Unit Level)', style = {
    'textAlign': 'center',
    # 'color': '#7FDBFF',
    'color': 'black',
    'fontWeight': 'bold',
    'font-size':'large',
  }),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
dash_table.DataTable(    style_data={
        'whiteSpace': 'normal',
        'height': 'auto',
        'textAlign': 'center',
        'lineHeight': '10px'
    },
    data=sram_df_table.to_dict('records'), 
    columns=[{"name": i, "id": i} for i in sram_df_table.columns],
        css=[{"selector": "input", "rule": "color:gray"}],
            # data=df.to_dict("records"),
            style_cell={"color": "gray"},
            # editable=True,
            style_data_conditional=[
                {"if": {"row_index": 0}, "backgroundColor": "#00BFFF"},
                {"if": {"row_index": 1}, "backgroundColor": "#66CDAA"},
                {"if": {"row_index": 2}, "backgroundColor": "#CD5C5C"},
                {
                    "if": {"state": "active"},
                    "backgroundColor": "inherit !important",
                    "border": "1px solid black",
                    # "color": "gray",
                },
                {
                    "if": {"state": "selected"},
                    "backgroundColor": "inherit !important",
                    # "border": "1px solid blue",
                },
        {
            'if': {
                'filter_query': '{Numbers} > 0',
                'row_index': 2,
            },
            'backgroundColor': '#CD5C5C',
            'color': 'black'
         },
            ],
        style_cell_conditional=[
        {'if': {'column_id': 'Category'},
         'width': '10%',
         'textAlign': 'center',
         'fontWeight': 'bold',
         'color': 'BLACK'},
        {'if': {'column_id': 'Numbers'},
         'width': '10%',
         'textAlign': 'center',
         'fontWeight': 'bold',
         'color': 'BLACK'},
    ]),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
html.Div(children = 'Test-wise Statistics', style = {
    'textAlign': 'center',
    # 'color': '#7FDBFF',
    'color': 'black',
    'fontWeight': 'bold',
    'font-size':'large',
  }),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
dbc.Label("Show number of rows for sram tests:"),
    sram_row_drop := dcc.Dropdown(value=10, clearable=False, style={'width':'35%'},
                             options=[10, 25, 50, 100]),
        dbc.Row([
        dbc.Col([
            sram_test_name_drop := dcc.Dropdown([x for x in sorted(sram_df_f.Test_Name.unique())])
        ], width=3),

    ], 
    justify="between", className='mt-3 mb-4'),

    my_table_sram := dash_table.DataTable(
        columns=[
            {'name': 'Test_Name', 'id': 'Test_Name', 'type': 'text'},
            {'name': 'Status', 'id': 'Status', 'type': 'text'},
            {'name': 'Remarks', 'id': 'Remarks', 'type': 'text'}
        ],
        style_table={'overflowX': 'auto'},
        data=sram_df_f.to_dict('records'),
        filter_action='native',
        page_size=10,
           style_data={
        'whiteSpace': 'normal',
        'height': 'auto',
        'textAlign': 'center',
        # 'lineHeight': '10px'
    },
            # editable=True,
            style_data_conditional=[
                {"if": {"row_index": "odd"}, "backgroundColor": "#66CDAA"},
                {"if": {"row_index": "even"}, "backgroundColor": "#66CDAA"},
                {
                    "if": {"state": "active"},
                    "backgroundColor": "inherit !important",
                    "border": "1px solid black",
                    # "color": "gray",
                },
                # {
                #     "if": {"state": "selected"},
                #     "backgroundColor": "black",
                #     # "border": "1px solid blue",
                # },
                   {"if": {"state": "selected"},
                         "backgroundColor": "inherit !important",
                          "border": "inherit !important",},
            {
            'if': {
                'filter_query': '{Status} contains "Failed"',
                'column_id': 'Status'
            },
            'backgroundColor': '#CD5C5C',
            'color': 'black'
         },
            {
            'if': {
                'filter_query': '{Status} contains "timeout"',
                'column_id': 'Status'
            },
            'backgroundColor': '#CD5C5C',
            'color': 'black'
         },
            ],
        style_cell_conditional=[
        {'if': {'column_id': 'Test_Name'},
         'width': '10%',
         'textAlign': 'center',
         'color': 'BLACK',
         'fontWeight': 'bold'},
                {'if': {'column_id': 'Status'},
         'width': '10%',
         'textAlign': 'center',
         'color': 'BLACK',
         'fontWeight': 'bold'},
                 {'if': {'column_id': 'Remarks'},
         'width': '50%',
         'textAlign': 'center',
         'color': 'BLACK',
         'fontWeight': 'bold'
         },
         
    ]),
html.Div(children = 'Coverage Report SRAM:', style = {
    'textAlign': 'left',
    'color': 'BLACK',
    'fontWeight': 'bold'
  }),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
html.Div(children = html.Iframe(
            src="assets/sram/dashboard.html",
            style={"height": "1067px", "width": "100%"},
        )
  ),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),

    html.Div(children = 'FCB  (Unit Level) Tests Statistics', style = {
    'textAlign': 'center',
    # 'color': '#7FDBFF',
    'color': 'blue',
    'fontWeight': 'bold',
    'font-size':'x-large',
  }),
dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Graph(
    id = 'gemini-graph-fcb',
    figure = fig_fcb
  ),
html.Div(children = 'General Statistics FCB  (Unit Level)', style = {
    'textAlign': 'center',
    # 'color': '#7FDBFF',
    'color': 'black',
    'fontWeight': 'bold',
    'font-size':'large',
  }),
dash_table.DataTable(    style_data={
        'whiteSpace': 'normal',
        'height': 'auto',
        'textAlign': 'center',
        'lineHeight': '10px'
    },
    data=fcb_df_table.to_dict('records'), 
    columns=[{"name": i, "id": i} for i in fcb_df_table.columns],
        css=[{"selector": "input", "rule": "color:gray"}],
            # data=df.to_dict("records"),
            style_cell={"color": "gray"},
            # editable=True,
            style_data_conditional=[
                {"if": {"row_index": 0}, "backgroundColor": "#00BFFF"},
                {"if": {"row_index": 1}, "backgroundColor": "#66CDAA"},
                {"if": {"row_index": 2}, "backgroundColor": "#CD5C5C"},
                {
                    "if": {"state": "active"},
                    "backgroundColor": "inherit !important",
                    "border": "1px solid black",
                    # "color": "gray",
                },
                {
                    "if": {"state": "selected"},
                    "backgroundColor": "inherit !important",
                    # "border": "1px solid blue",
                },
        {
            'if': {
                'filter_query': '{Numbers} > 0',
                'row_index': 2,
            },
            'backgroundColor': '#CD5C5C',
            'color': 'black'
         },
            ],
        style_cell_conditional=[
        {'if': {'column_id': 'Category'},
         'width': '10%',
         'textAlign': 'center',
         'fontWeight': 'bold',
         'color': 'BLACK'},
        {'if': {'column_id': 'Numbers'},
         'width': '10%',
         'textAlign': 'center',
         'fontWeight': 'bold',
         'color': 'BLACK'},
    ]),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
html.Div(children = 'Test-wise Statistics', style = {
    'textAlign': 'center',
    # 'color': '#7FDBFF',
    'color': 'black',
    'fontWeight': 'bold',
    'font-size':'large',
  }),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
dbc.Label("Show number of rows for fcb tests:"),
    fcb_row_drop := dcc.Dropdown(value=10, clearable=False, style={'width':'35%'},
                             options=[10, 25, 50, 100]),
        dbc.Row([
        dbc.Col([
            fcb_test_name_drop := dcc.Dropdown([x for x in sorted(fcb_df_f.Test_Name.unique())])
        ], width=3),

    ], 
    justify="between", className='mt-3 mb-4'),

    my_table_fcb := dash_table.DataTable(
        columns=[
            {'name': 'Test_Name', 'id': 'Test_Name', 'type': 'text'},
            {'name': 'Status', 'id': 'Status', 'type': 'text'},
            {'name': 'Remarks', 'id': 'Remarks', 'type': 'text'}
        ],
        style_table={'overflowX': 'auto'},
        data=fcb_df_f.to_dict('records'),
        filter_action='native',
        page_size=10,
           style_data={
        'whiteSpace': 'normal',
        'height': 'auto',
        'textAlign': 'center',
        # 'lineHeight': '10px'
    },
            # editable=True,
            style_data_conditional=[
                {"if": {"row_index": "odd"}, "backgroundColor": "#66CDAA"},
                {"if": {"row_index": "even"}, "backgroundColor": "#66CDAA"},
                {
                    "if": {"state": "active"},
                    "backgroundColor": "inherit !important",
                    "border": "1px solid black",
                    # "color": "gray",
                },
                # {
                #     "if": {"state": "selected"},
                #     "backgroundColor": "black",
                #     # "border": "1px solid blue",
                # },
                   {"if": {"state": "selected"},
                         "backgroundColor": "inherit !important",
                          "border": "inherit !important",},
            {
            'if': {
                'filter_query': '{Status} contains "Failed"',
                'column_id': 'Status'
            },
            'backgroundColor': '#CD5C5C',
            'color': 'black'
         },

            ],
        style_cell_conditional=[
        {'if': {'column_id': 'Test_Name'},
         'width': '10%',
         'textAlign': 'center',
         'color': 'BLACK',
         'fontWeight': 'bold'},
                {'if': {'column_id': 'Status'},
         'width': '10%',
         'textAlign': 'center',
         'color': 'BLACK',
         'fontWeight': 'bold'},
                 {'if': {'column_id': 'Remarks'},
         'width': '50%',
         'textAlign': 'center',
         'color': 'BLACK',
         'fontWeight': 'bold'
         },
         
    ]),
html.Div(children = 'Coverage Report FCB:', style = {
    'textAlign': 'left',
    'color': 'Black',
    'fontWeight': 'bold'
  }),
dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
 dcc.Markdown('''
    [](/)
'''),
html.Div(children = html.Iframe(
            src="assets/fcb/dashboard.html",
            style={"height": "1067px", "width": "100%"},
        )
  ),

])
])
@callback(
    Output(my_table, 'data'),
    Output(my_table, 'page_size'),
    Input(IP_drop, 'value'),
    Input(row_drop, 'value'),)
def update_dropdown_options(IP_v,row_v):
    dff = df_f.copy()
    if IP_v:
        dff = dff[dff.IP==IP_v]
    return dff.to_dict('records'), row_v
@callback(
    Output(my_table_sram, 'data'),
    Output(my_table_sram, 'page_size'),
    Input(sram_test_name_drop, 'value'),
    Input(sram_row_drop, 'value'),)
def update_dropdown_options_sram(tname_v,sram_row_v):
    dff_S = sram_df_f.copy()
    if tname_v:
        dff_S =dff_S[dff_S.Test_Name==tname_v]
    return dff_S.to_dict('records'),sram_row_v
@callback(
    Output(my_table_fcb, 'data'),
    Output(my_table_fcb, 'page_size'),
    Input(fcb_test_name_drop, 'value'),
    Input(fcb_row_drop, 'value'),)
def update_dropdown_options_sram(tname_v,fcb_row_v):
    dff_F = fcb_df_f.copy()
    if tname_v:
        dff_F =dff_F[dff_F.Test_Name==tname_v]
    return dff_F.to_dict('records'),fcb_row_v



if __name__ == '__main__':
    app.run_server(debug=False, port = 8080)
