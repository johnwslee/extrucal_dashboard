from dash import Dash, html

app = Dash()
app.layout = html.Div('I am alive!!')
app.run_server()