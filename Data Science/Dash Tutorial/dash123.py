import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

fig = px.scatter(df, x="gdp per capita", y="life expectancy",
                 size="population", color="continent", hover_name="country",
                 log_x=True, size_max=30)

app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig
    )
])

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
# df = pd.DataFrame({
#     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#     "Amount": [4, 1, 2, 2, 4, 5],
#     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# })

# fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# app.layout = html.Div(children=[
#     html.H1(children='Hello Dash'),

#     html.Div(children='''
#         Dash: A web application framework for Python.
#     '''),

#     dcc.Graph(
#         id='example-graph',
#         figure=fig
#     )
# ])

if __name__ == '__main__':
    app.run_server(debug=True)