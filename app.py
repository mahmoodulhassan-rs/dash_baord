import pandas as pd
import dash
import dash_table
import os
from dash.dependencies import Input, Output
from dash import dcc
from dash import html
df = pd.DataFrame()
# print(df)
df_grp_dash=pd.DataFrame()



df_grp_dash=pd.DataFrame(df,columns=["Category","Numbers"])

df_grp_dash.loc["1","Category"]="Tests Passed"
df_grp_dash.loc["2","Category"]="Tests Failed"

df_grp_dash.loc["1","Numbers"]= "24"
df_grp_dash.loc["2","Numbers"]= "3"
assets_path = os.getcwd() +'/src/new_assets'
# print("assets path",assets_path)
app = dash.Dash(__name__)
# path= location

server = app.server
app.title = "Gemini Dashboard"




df_table = pd.read_csv('css_states_dash.csv')
df_states = pd.read_csv('css_states.csv')
fig = px.pie(df_grp_dash,"Category","Numbers", color = "Numbers")
fig.update_layout(legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="left",
    x=0.01,
))
arr =[24,10,15]
aarr= [20,3,15]
arr_x=[1,2,3,4,5,6,7]
f1 = go.Figure(
    data = [
        go.Scatter(x=arr_x,y=arr, name="Tests Planned"),
        go.Scatter(x=arr_x,y=aarr, name="Tests Passed"),
    ],
    layout = {"xaxis": {"title": "Weeks"}, "yaxis": {"title": "Numbers(Tets Passed, Tests Failed, Tests Planned)"}, "title": "Weekly Statistics"}
)

app.layout = html.Div(style = {
  'backgroundColor': '#111111'
}, children = [
    html.H1(
    children = 'RapidSilicon',
    style = {
      'textAlign': 'center',
      'color': 'Crimson'
    }
  ),
    html.Div(children = 'Gemini Tests Statistics', style = {
    'textAlign': 'center',
    'color': '#7FDBFF',
    'fontWeight': 'bold'
  }),

    dcc.Graph(
    id = 'gemini-graph-1',
    figure = fig
  ),
  dash_table.DataTable(    style_data={
        'whiteSpace': 'normal',
        'height': 'auto',
        'textAlign': 'center',
        'lineHeight': '10px'
    },
    data=df_table.to_dict('records'), 
    columns=[{"name": i, "id": i} for i in df_table.columns],
        css=[{"selector": "input", "rule": "color:gray"}],
            # data=df.to_dict("records"),
            style_cell={"color": "gray"},
            # editable=True,
            style_data_conditional=[
                {"if": {"row_index": "odd"}, "backgroundColor": "green"},
                {"if": {"row_index": "even"}, "backgroundColor": "green"},
                {
                    "if": {"state": "active"},
                    "backgroundColor": "",
                    "border": "1px solid red",
                    # "color": "gray",
                },
                {
                    "if": {"state": "selected"},
                    "backgroundColor": "black",
                    # "border": "1px solid blue",
                },
        {
            'if': {
                'filter_query': '{Numbers} > 0',
                'column_id': 'Numbers'
            },
            'backgroundColor': 'red',
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

    dcc.Graph(
    id = 'gemini-graph-2',
    figure = f1
  ),
  dash_table.DataTable(    style_data={
        'whiteSpace': 'normal',
        'height': 'auto',
        'textAlign': 'center',
        'lineHeight': '10px'
    },
    data=df_states.to_dict('records'), 
    columns=[{"name": i, "id": i} for i in df_states.columns],
    export_format="csv",
         css=[{"selector": "input", "rule": "color:green"}],
            # data=df.to_dict("records"),
            style_cell={"color": "green"},
            # editable=True,
            style_data_conditional=[
                {"if": {"row_index": "odd"}, "backgroundColor": "green"},
                {"if": {"row_index": "even"}, "backgroundColor": "green"},
                {
                    "if": {"state": "active"},
                    "backgroundColor": "",
                    "border": "1px solid red",
                    # "color": "gray",
                },
                {
                    "if": {"state": "selected"},
                    "backgroundColor": "black",
                    # "border": "1px solid blue",
                },

            {
            'if': {
                'filter_query': '{Status} contains "Failed"',
                'column_id': 'Status'
            },
            'backgroundColor': 'red',
            'color': 'black'
         },

            ],
        style_cell_conditional=[
        {'if': {'column_id': 'IP'},
         'width': '10%',
         'textAlign': 'center',
            'color': 'BLACK',
            'fontWeight': 'bold'},
        {'if': {'column_id': 'Test Name'},
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
         'width': '10%',
         'textAlign': 'center',
         'color': 'BLACK',
         'fontWeight': 'bold'},
         
    ]),

    html.Div(
    children=[
        html.Iframe(
            src="assets/dashboard.html",
            style={"height": "1067px", "width": "100%"},
        )
    ]
),

# fig.write_html("path"),

# dashboard.save_html("dashboard.html")
])
# print ("**********************,",path)
if __name__ == '__main__':

  app.run_server(debug=False, port = 8080)
