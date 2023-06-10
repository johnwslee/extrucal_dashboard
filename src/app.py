import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, dash_table, dcc, html
from pretty_html_table import build_table

from extrucal.cable_extrusion import cable_cal, cable_plot, cable_table
from extrucal.extrusion import throughput_cal, throughput_plot, throughput_table
from extrucal.rod_extrusion import rod_cal, rod_plot, rod_table
from extrucal.sheet_extrusion import sheet_cal, sheet_plot, sheet_table
from extrucal.tube_extrusion import tube_cal, tube_plot, tube_table

# Styles

h1_style = {
    "background": "white",
    "text-transform": "uppercase",
    "textAlign": "center",
    "color": "black",
    "border": "black",
    "font-size": "50px",
    "font-weight": 600,
    "align-items": "center",
    "justify-content": "center",
    "border-radius": "4px",
    "padding": "6px",
}

h3_style = {
    "background": "white",
    "text-transform": "uppercase",
    # 'textAlign': 'center',
    "color": "#484848",
    "border": "black",
    "font-size": "30px",
    "font-weight": 600,
    # 'align-items': 'center',
    # 'justify-content': 'center',
    # 'border-radius': '4px',
    # 'padding':'6px'
}

h5_style = {
    # 'background': 'white',
    "color": "grey",
    "border": "black",
    "font-weight": 600,
}

tab_style = {
    "background": "#D3D3D3",
    "text-transform": "uppercase",
    "color": "white",
    "border": "white",
    "font-size": "18px",
    "font-weight": 600,
    "align-items": "center",
    "justify-content": "center",
    "border-radius": "4px",
    "padding": "6px",
}

tab_selected_style = {
    "background": "#484848",
    "text-transform": "uppercase",
    "color": "white",
    "font-size": "18px",
    "font-weight": 600,
    "align-items": "center",
    "justify-content": "center",
    "border-radius": "4px",
    "padding": "6px",
}

left_column_style = {"width": "30%", "background-color": "#F0F0F0"}

# Setup app and layout/frontend
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = dbc.Container(
    [
        html.H1("Extrucal Dashboard", style=h1_style),
        html.Br(),
        dcc.Tabs(
            [
                dcc.Tab(
                    label="Throughput Calculation",
                    style=tab_style,
                    selected_style=tab_selected_style,
                    children=[
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Br(),
                                        html.H5("Screw Size [mm]", style=h5_style),
                                        dcc.Input(
                                            id="screw_size",
                                            type="number",
                                            value=200,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5(
                                            "Melt Density of Material [kg/m^3]",
                                            style=h5_style,
                                        ),
                                        dcc.Input(
                                            id="melt_density",
                                            type="number",
                                            value=800,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5(
                                            "Number of Screw Flight", style=h5_style
                                        ),
                                        dcc.Input(
                                            id="n_flight",
                                            type="number",
                                            value=1,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5("Minimum Screw RPM", style=h5_style),
                                        dcc.Input(
                                            id="min_rpm",
                                            type="number",
                                            value=5,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5("Maximum Screw RPM", style=h5_style),
                                        dcc.Input(
                                            id="max_rpm",
                                            type="number",
                                            value=50,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5(
                                            "Increment of Screw RPM", style=h5_style
                                        ),
                                        dcc.Input(
                                            id="delta_rpm",
                                            type="number",
                                            value=5,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                    ],
                                    style=left_column_style,
                                    md=4,
                                ),
                                dbc.Col(
                                    [
                                        html.Br(),
                                        html.H3("Predicted Throughput", style=h3_style),
                                        html.Iframe(
                                            id="throughput_plot",
                                            style={
                                                "border-width": "0",
                                                "width": "100%",
                                                "height": "76%",
                                            },
                                        ),
                                        html.H6(
                                            "Note: Please put cursor onto the data point in the graph for the actual value"
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H3("Throughput Table", style=h3_style),
                                        html.Iframe(
                                            id="throughput_table",
                                            style={
                                                "border-width": "0",
                                                "width": "100%",
                                                "height": "100%",
                                            },
                                        ),
                                    ],
                                    md=8,
                                ),
                            ]
                        )
                    ],
                ),
                dcc.Tab(
                    label="Cable Extrusion",
                    style=tab_style,
                    selected_style=tab_selected_style,
                    children=[
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Br(),
                                        html.H5(
                                            "Insulation Outer Diameter [mm]",
                                            style=h5_style,
                                        ),
                                        dcc.Input(
                                            id="cable_outer_d",
                                            type="number",
                                            value=10,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5(
                                            "Insulation Thickness [mm]", style=h5_style
                                        ),
                                        dcc.Input(
                                            id="cable_thickness",
                                            type="number",
                                            value=2,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5(
                                            "Solid Density of Material [kg/m^3]",
                                            style=h5_style,
                                        ),
                                        dcc.Input(
                                            id="cable_s_density",
                                            type="number",
                                            value=920,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5(
                                            "Melt/Solid Density Ratio", style=h5_style
                                        ),
                                        dcc.Input(
                                            id="cable_density_ratio",
                                            type="number",
                                            value=0.85,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5(
                                            "Minimum Line Speed [mpm]", style=h5_style
                                        ),
                                        dcc.Input(
                                            id="cable_min_l_speed",
                                            type="number",
                                            value=1,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5(
                                            "Maximum Line Speed [mpm]", style=h5_style
                                        ),
                                        dcc.Input(
                                            id="cable_max_l_speed",
                                            type="number",
                                            value=10,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5(
                                            "Increment of Line Speed [mpm]",
                                            style=h5_style,
                                        ),
                                        dcc.Input(
                                            id="cable_delta_l_speed",
                                            type="number",
                                            value=1,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5(
                                            "Minimum Extruder Size [mm]", style=h5_style
                                        ),
                                        dcc.Input(
                                            id="cable_min_size",
                                            type="number",
                                            value=40,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5(
                                            "Maximum Extruder Size [mm]", style=h5_style
                                        ),
                                        dcc.Input(
                                            id="cable_max_size",
                                            type="number",
                                            value=100,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5(
                                            "Increment of Extruder Size [mm]",
                                            style=h5_style,
                                        ),
                                        dcc.Input(
                                            id="cable_delta_size",
                                            type="number",
                                            value=5,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5(
                                            "Metering Depth to Extruder Size Ratio",
                                            style=h5_style,
                                        ),
                                        dcc.Input(
                                            id="cable_depth_percent",
                                            type="number",
                                            value=0.05,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                    ],
                                    md=4,
                                    style=left_column_style,
                                ),
                                dbc.Col(
                                    [
                                        html.Br(),
                                        html.H3("Required Screw RPM", style=h3_style),
                                        html.Iframe(
                                            id="cable_plot",
                                            style={
                                                "border-width": "0",
                                                "width": "100%",
                                                "height": "45%",
                                            },
                                        ),
                                        html.H6(
                                            "Note: Please put cursor onto the data point in the graph for the actual value"
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H3("Screw RPM Table", style=h3_style),
                                        html.Iframe(
                                            id="cable_table",
                                            style={
                                                "border-width": "0",
                                                "width": "100%",
                                                "height": "100%",
                                            },
                                        ),
                                    ],
                                    md=8,
                                ),
                            ]
                        )
                    ],
                ),
                dcc.Tab(
                    label="Tube Extrusion",
                    style=tab_style,
                    selected_style=tab_selected_style,
                    children=[
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Br(),
                                        html.H5(
                                            "Tube Outer Diameter [mm]", style=h5_style
                                        ),
                                        dcc.Input(
                                            id="tube_outer_d",
                                            type="number",
                                            value=10,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5(
                                            "Tube Inner Diameter [mm]", style=h5_style
                                        ),
                                        dcc.Input(
                                            id="tube_inner_d",
                                            type="number",
                                            value=8,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5(
                                            "Solid Density of Material [kg/m^3]",
                                            style=h5_style,
                                        ),
                                        dcc.Input(
                                            id="tube_s_density",
                                            type="number",
                                            value=920,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5(
                                            "Melt/Solid Density Ratio", style=h5_style
                                        ),
                                        dcc.Input(
                                            id="tube_density_ratio",
                                            type="number",
                                            value=0.85,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5(
                                            "Minimum Line Speed [mpm]", style=h5_style
                                        ),
                                        dcc.Input(
                                            id="tube_min_l_speed",
                                            type="number",
                                            value=1,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5(
                                            "Maximum Line Speed [mpm]", style=h5_style
                                        ),
                                        dcc.Input(
                                            id="tube_max_l_speed",
                                            type="number",
                                            value=10,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5(
                                            "Increment of Line Speed [mpm]",
                                            style=h5_style,
                                        ),
                                        dcc.Input(
                                            id="tube_delta_l_speed",
                                            type="number",
                                            value=1,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5(
                                            "Minimum Extruder Size [mm]", style=h5_style
                                        ),
                                        dcc.Input(
                                            id="tube_min_size",
                                            type="number",
                                            value=40,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5(
                                            "Maximum Extruder Size [mm]", style=h5_style
                                        ),
                                        dcc.Input(
                                            id="tube_max_size",
                                            type="number",
                                            value=100,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5(
                                            "Increment of Extruder Size [mm]",
                                            style=h5_style,
                                        ),
                                        dcc.Input(
                                            id="tube_delta_size",
                                            type="number",
                                            value=5,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5(
                                            "Metering Depth to Extruder Size Ratio",
                                            style=h5_style,
                                        ),
                                        dcc.Input(
                                            id="tube_depth_percent",
                                            type="number",
                                            value=0.05,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                    ],
                                    md=4,
                                    style=left_column_style,
                                ),
                                dbc.Col(
                                    [
                                        html.Br(),
                                        html.H3("Required Screw RPM", style=h3_style),
                                        html.Iframe(
                                            id="tube_plot",
                                            style={
                                                "border-width": "0",
                                                "width": "100%",
                                                "height": "45%",
                                            },
                                        ),
                                        html.H6(
                                            "Note: Please put cursor onto the data point in the graph for the actual value"
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H3("Screw RPM Table", style=h3_style),
                                        html.Iframe(
                                            id="tube_table",
                                            style={
                                                "border-width": "0",
                                                "width": "100%",
                                                "height": "100%",
                                            },
                                        ),
                                    ],
                                    md=8,
                                ),
                            ]
                        )
                    ],
                ),
                dcc.Tab(
                    label="Rod Extrusion",
                    style=tab_style,
                    selected_style=tab_selected_style,
                    children=[
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Br(),
                                        html.H5(
                                            "Rod Outer Diameter [mm]", style=h5_style
                                        ),
                                        dcc.Input(
                                            id="rod_outer_d",
                                            type="number",
                                            value=2,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5("Number of Die Holes", style=h5_style),
                                        dcc.Input(
                                            id="rod_n_holes",
                                            type="number",
                                            value=10,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5(
                                            "Solid Density of Material [kg/m^3]",
                                            style=h5_style,
                                        ),
                                        dcc.Input(
                                            id="rod_s_density",
                                            type="number",
                                            value=920,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5(
                                            "Melt/Solid Density Ratio", style=h5_style
                                        ),
                                        dcc.Input(
                                            id="rod_density_ratio",
                                            type="number",
                                            value=0.85,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5(
                                            "Minimum Line Speed [mpm]", style=h5_style
                                        ),
                                        dcc.Input(
                                            id="rod_min_l_speed",
                                            type="number",
                                            value=1,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5(
                                            "Maximum Line Speed [mpm]", style=h5_style
                                        ),
                                        dcc.Input(
                                            id="rod_max_l_speed",
                                            type="number",
                                            value=10,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5(
                                            "Increment of Line Speed [mpm]",
                                            style=h5_style,
                                        ),
                                        dcc.Input(
                                            id="rod_delta_l_speed",
                                            type="number",
                                            value=1,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5(
                                            "Minimum Extruder Size [mm]", style=h5_style
                                        ),
                                        dcc.Input(
                                            id="rod_min_size",
                                            type="number",
                                            value=40,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5(
                                            "Maximum Extruder Size [mm]", style=h5_style
                                        ),
                                        dcc.Input(
                                            id="rod_max_size",
                                            type="number",
                                            value=100,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5(
                                            "Increment of Extruder Size [mm]",
                                            style=h5_style,
                                        ),
                                        dcc.Input(
                                            id="rod_delta_size",
                                            type="number",
                                            value=5,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5(
                                            "Metering Depth to Extruder Size Ratio",
                                            style=h5_style,
                                        ),
                                        dcc.Input(
                                            id="rod_depth_percent",
                                            type="number",
                                            value=0.05,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                    ],
                                    md=4,
                                    style=left_column_style,
                                ),
                                dbc.Col(
                                    [
                                        html.Br(),
                                        html.H3("Required Screw RPM", style=h3_style),
                                        html.Iframe(
                                            id="rod_plot",
                                            style={
                                                "border-width": "0",
                                                "width": "100%",
                                                "height": "45%",
                                            },
                                        ),
                                        html.H6(
                                            "Note: Please put cursor onto the data point in the graph for the actual value"
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H3("Screw RPM Table", style=h3_style),
                                        html.Iframe(
                                            id="rod_table",
                                            style={
                                                "border-width": "0",
                                                "width": "100%",
                                                "height": "100%",
                                            },
                                        ),
                                    ],
                                    md=8,
                                ),
                            ]
                        )
                    ],
                ),
                dcc.Tab(
                    label="Sheet Extrusion",
                    style=tab_style,
                    selected_style=tab_selected_style,
                    children=[
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Br(),
                                        html.H5("Sheet Width [mm]", style=h5_style),
                                        dcc.Input(
                                            id="sheet_width",
                                            type="number",
                                            value=20,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5("Sheet Thickness [mm]", style=h5_style),
                                        dcc.Input(
                                            id="sheet_thickness",
                                            type="number",
                                            value=2,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5(
                                            "Solid Density of Material [kg/m^3]",
                                            style=h5_style,
                                        ),
                                        dcc.Input(
                                            id="sheet_s_density",
                                            type="number",
                                            value=920,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5(
                                            "Melt/Solid Density Ratio", style=h5_style
                                        ),
                                        dcc.Input(
                                            id="sheet_density_ratio",
                                            type="number",
                                            value=0.85,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5(
                                            "Minimum Line Speed [mpm]", style=h5_style
                                        ),
                                        dcc.Input(
                                            id="sheet_min_l_speed",
                                            type="number",
                                            value=1,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5(
                                            "Maximum Line Speed [mpm]", style=h5_style
                                        ),
                                        dcc.Input(
                                            id="sheet_max_l_speed",
                                            type="number",
                                            value=10,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5(
                                            "Increment of Line Speed [mpm]",
                                            style=h5_style,
                                        ),
                                        dcc.Input(
                                            id="sheet_delta_l_speed",
                                            type="number",
                                            value=1,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5(
                                            "Minimum Extruder Size [mm]", style=h5_style
                                        ),
                                        dcc.Input(
                                            id="sheet_min_size",
                                            type="number",
                                            value=40,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5(
                                            "Maximum Extruder Size [mm]", style=h5_style
                                        ),
                                        dcc.Input(
                                            id="sheet_max_size",
                                            type="number",
                                            value=100,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5(
                                            "Increment of Extruder Size [mm]",
                                            style=h5_style,
                                        ),
                                        dcc.Input(
                                            id="sheet_delta_size",
                                            type="number",
                                            value=5,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H5(
                                            "Metering Depth to Extruder Size Ratio",
                                            style=h5_style,
                                        ),
                                        dcc.Input(
                                            id="sheet_depth_percent",
                                            type="number",
                                            value=0.05,
                                            debounce=True,
                                        ),
                                        html.Br(),
                                        html.Br(),
                                    ],
                                    md=4,
                                    style=left_column_style,
                                ),
                                dbc.Col(
                                    [
                                        html.Br(),
                                        html.H3("Required Screw RPM", style=h3_style),
                                        html.Iframe(
                                            id="sheet_plot",
                                            style={
                                                "border-width": "0",
                                                "width": "100%",
                                                "height": "45%",
                                            },
                                        ),
                                        html.H6(
                                            "Note: Please put cursor onto the data point in the graph for the actual value"
                                        ),
                                        html.Br(),
                                        html.Br(),
                                        html.H3("Screw RPM Table", style=h3_style),
                                        html.Iframe(
                                            id="sheet_table",
                                            style={
                                                "border-width": "0",
                                                "width": "100%",
                                                "height": "100%",
                                            },
                                        ),
                                    ],
                                    md=8,
                                ),
                            ]
                        )
                    ],
                ),
            ]
        ),
    ]
)


# Setup callbacks/backend for Throughput Plot
@app.callback(
    Output("throughput_plot", "srcDoc"),
    Input("screw_size", "value"),
    Input("melt_density", "value"),
    Input("n_flight", "value"),
    Input("min_rpm", "value"),
    Input("max_rpm", "value"),
    Input("delta_rpm", "value"),
)
def show_throughput_plot(
    screw_size, melt_density, n_flight, min_rpm, max_rpm, delta_rpm
):
    output = throughput_plot(
        screw_size,
        melt_density,
        n_flight=n_flight,
        min_rpm=min_rpm,
        max_rpm=max_rpm,
        delta_rpm=delta_rpm,
    )
    return output.to_html()


# Setup callbacks/backend for Throughput Table
@app.callback(
    Output("throughput_table", "srcDoc"),
    Input("screw_size", "value"),
    Input("melt_density", "value"),
    Input("n_flight", "value"),
    Input("min_rpm", "value"),
    Input("max_rpm", "value"),
    Input("delta_rpm", "value"),
)
def show_throughput_table(
    screw_size, melt_density, n_flight, min_rpm, max_rpm, delta_rpm
):
    output = throughput_table(
        screw_size,
        melt_density,
        n_flight=n_flight,
        min_rpm=min_rpm,
        max_rpm=max_rpm,
        delta_rpm=delta_rpm,
    )
    return build_table(
        output,
        "grey_light",
        font_size="16px",
        index=True,
        text_align="center",
        padding="5px",
    )


# Setup callbacks/backend for Cable Plot
@app.callback(
    Output("cable_plot", "srcDoc"),
    Input("cable_outer_d", "value"),
    Input("cable_thickness", "value"),
    Input("cable_s_density", "value"),
    Input("cable_density_ratio", "value"),
    Input("cable_min_l_speed", "value"),
    Input("cable_max_l_speed", "value"),
    Input("cable_delta_l_speed", "value"),
    Input("cable_min_size", "value"),
    Input("cable_max_size", "value"),
    Input("cable_delta_size", "value"),
    Input("cable_depth_percent", "value"),
)
def show_cable_plot(
    outer_d,
    thickness,
    s_density,
    density_ratio,
    min_l_speed,
    max_l_speed,
    delta_l_speed,
    min_size,
    max_size,
    delta_size,
    depth_percent,
):
    output = cable_plot(
        outer_d=outer_d,
        thickness=thickness,
        s_density=s_density,
        density_ratio=density_ratio,
        min_l_speed=min_l_speed,
        max_l_speed=max_l_speed,
        delta_l_speed=delta_l_speed,
        min_size=min_size,
        max_size=max_size,
        delta_size=delta_size,
        depth_percent=depth_percent,
    )
    return output.to_html()


# Setup callbacks/backend for Cable Table
@app.callback(
    Output("cable_table", "srcDoc"),
    Input("cable_outer_d", "value"),
    Input("cable_thickness", "value"),
    Input("cable_s_density", "value"),
    Input("cable_density_ratio", "value"),
    Input("cable_min_l_speed", "value"),
    Input("cable_max_l_speed", "value"),
    Input("cable_delta_l_speed", "value"),
    Input("cable_min_size", "value"),
    Input("cable_max_size", "value"),
    Input("cable_delta_size", "value"),
    Input("cable_depth_percent", "value"),
)
def show_cable_table(
    outer_d,
    thickness,
    s_density,
    density_ratio,
    min_l_speed,
    max_l_speed,
    delta_l_speed,
    min_size,
    max_size,
    delta_size,
    depth_percent,
):
    output = cable_table(
        outer_d=outer_d,
        thickness=thickness,
        s_density=s_density,
        density_ratio=density_ratio,
        min_l_speed=min_l_speed,
        max_l_speed=max_l_speed,
        delta_l_speed=delta_l_speed,
        min_size=min_size,
        max_size=max_size,
        delta_size=delta_size,
        depth_percent=depth_percent,
    )
    return build_table(
        output,
        "grey_light",
        font_size="16px",
        index=True,
        text_align="center",
        padding="5px",
    )


# Setup callbacks/backend for Tube Plot
@app.callback(
    Output("tube_plot", "srcDoc"),
    Input("tube_outer_d", "value"),
    Input("tube_inner_d", "value"),
    Input("tube_s_density", "value"),
    Input("tube_density_ratio", "value"),
    Input("tube_min_l_speed", "value"),
    Input("tube_max_l_speed", "value"),
    Input("tube_delta_l_speed", "value"),
    Input("tube_min_size", "value"),
    Input("tube_max_size", "value"),
    Input("tube_delta_size", "value"),
    Input("tube_depth_percent", "value"),
)
def show_tube_plot(
    outer_d,
    inner_d,
    s_density,
    density_ratio,
    min_l_speed,
    max_l_speed,
    delta_l_speed,
    min_size,
    max_size,
    delta_size,
    depth_percent,
):
    output = tube_plot(
        outer_d=outer_d,
        inner_d=inner_d,
        s_density=s_density,
        density_ratio=density_ratio,
        min_l_speed=min_l_speed,
        max_l_speed=max_l_speed,
        delta_l_speed=delta_l_speed,
        min_size=min_size,
        max_size=max_size,
        delta_size=delta_size,
        depth_percent=depth_percent,
    )
    return output.to_html()


# Setup callbacks/backend for Tube Table
@app.callback(
    Output("tube_table", "srcDoc"),
    Input("tube_outer_d", "value"),
    Input("tube_inner_d", "value"),
    Input("tube_s_density", "value"),
    Input("tube_density_ratio", "value"),
    Input("tube_min_l_speed", "value"),
    Input("tube_max_l_speed", "value"),
    Input("tube_delta_l_speed", "value"),
    Input("tube_min_size", "value"),
    Input("tube_max_size", "value"),
    Input("tube_delta_size", "value"),
    Input("tube_depth_percent", "value"),
)
def show_tube_table(
    outer_d,
    inner_d,
    s_density,
    density_ratio,
    min_l_speed,
    max_l_speed,
    delta_l_speed,
    min_size,
    max_size,
    delta_size,
    depth_percent,
):
    output = tube_table(
        outer_d=outer_d,
        inner_d=inner_d,
        s_density=s_density,
        density_ratio=density_ratio,
        min_l_speed=min_l_speed,
        max_l_speed=max_l_speed,
        delta_l_speed=delta_l_speed,
        min_size=min_size,
        max_size=max_size,
        delta_size=delta_size,
        depth_percent=depth_percent,
    )
    return build_table(
        output,
        "grey_light",
        font_size="16px",
        index=True,
        text_align="center",
        padding="5px",
    )


# Setup callbacks/backend for Rod Plot
@app.callback(
    Output("rod_plot", "srcDoc"),
    Input("rod_outer_d", "value"),
    Input("rod_s_density", "value"),
    Input("rod_n_holes", "value"),
    Input("rod_density_ratio", "value"),
    Input("rod_min_l_speed", "value"),
    Input("rod_max_l_speed", "value"),
    Input("rod_delta_l_speed", "value"),
    Input("rod_min_size", "value"),
    Input("rod_max_size", "value"),
    Input("rod_delta_size", "value"),
    Input("rod_depth_percent", "value"),
)
def show_rod_plot(
    outer_d,
    s_density,
    n_holes,
    density_ratio,
    min_l_speed,
    max_l_speed,
    delta_l_speed,
    min_size,
    max_size,
    delta_size,
    depth_percent,
):
    output = rod_plot(
        outer_d=outer_d,
        s_density=s_density,
        n_holes=n_holes,
        density_ratio=density_ratio,
        min_l_speed=min_l_speed,
        max_l_speed=max_l_speed,
        delta_l_speed=delta_l_speed,
        min_size=min_size,
        max_size=max_size,
        delta_size=delta_size,
        depth_percent=depth_percent,
    )
    return output.to_html()


# Setup callbacks/backend for Rod Table
@app.callback(
    Output("rod_table", "srcDoc"),
    Input("rod_outer_d", "value"),
    Input("rod_s_density", "value"),
    Input("rod_n_holes", "value"),
    Input("rod_density_ratio", "value"),
    Input("rod_min_l_speed", "value"),
    Input("rod_max_l_speed", "value"),
    Input("rod_delta_l_speed", "value"),
    Input("rod_min_size", "value"),
    Input("rod_max_size", "value"),
    Input("rod_delta_size", "value"),
    Input("rod_depth_percent", "value"),
)
def show_rod_table(
    outer_d,
    s_density,
    n_holes,
    density_ratio,
    min_l_speed,
    max_l_speed,
    delta_l_speed,
    min_size,
    max_size,
    delta_size,
    depth_percent,
):
    output = rod_table(
        outer_d=outer_d,
        s_density=s_density,
        n_holes=n_holes,
        density_ratio=density_ratio,
        min_l_speed=min_l_speed,
        max_l_speed=max_l_speed,
        delta_l_speed=delta_l_speed,
        min_size=min_size,
        max_size=max_size,
        delta_size=delta_size,
        depth_percent=depth_percent,
    )
    return build_table(
        output,
        "grey_light",
        font_size="16px",
        index=True,
        text_align="center",
        padding="5px",
    )


# Setup callbacks/backend for Sheet Plot
@app.callback(
    Output("sheet_plot", "srcDoc"),
    Input("sheet_width", "value"),
    Input("sheet_thickness", "value"),
    Input("sheet_s_density", "value"),
    Input("sheet_density_ratio", "value"),
    Input("sheet_min_l_speed", "value"),
    Input("sheet_max_l_speed", "value"),
    Input("sheet_delta_l_speed", "value"),
    Input("sheet_min_size", "value"),
    Input("sheet_max_size", "value"),
    Input("sheet_delta_size", "value"),
    Input("sheet_depth_percent", "value"),
)
def show_sheet_plot(
    width,
    thickness,
    s_density,
    density_ratio,
    min_l_speed,
    max_l_speed,
    delta_l_speed,
    min_size,
    max_size,
    delta_size,
    depth_percent,
):
    output = sheet_plot(
        width=width,
        thickness=thickness,
        s_density=s_density,
        density_ratio=density_ratio,
        min_l_speed=min_l_speed,
        max_l_speed=max_l_speed,
        delta_l_speed=delta_l_speed,
        min_size=min_size,
        max_size=max_size,
        delta_size=delta_size,
        depth_percent=depth_percent,
    )
    return output.to_html()


# Setup callbacks/backend for Sheet Table
@app.callback(
    Output("sheet_table", "srcDoc"),
    Input("sheet_width", "value"),
    Input("sheet_thickness", "value"),
    Input("sheet_s_density", "value"),
    Input("sheet_density_ratio", "value"),
    Input("sheet_min_l_speed", "value"),
    Input("sheet_max_l_speed", "value"),
    Input("sheet_delta_l_speed", "value"),
    Input("sheet_min_size", "value"),
    Input("sheet_max_size", "value"),
    Input("sheet_delta_size", "value"),
    Input("sheet_depth_percent", "value"),
)
def show_sheet_table(
    width,
    thickness,
    s_density,
    density_ratio,
    min_l_speed,
    max_l_speed,
    delta_l_speed,
    min_size,
    max_size,
    delta_size,
    depth_percent,
):
    output = sheet_table(
        width=width,
        thickness=thickness,
        s_density=s_density,
        density_ratio=density_ratio,
        min_l_speed=min_l_speed,
        max_l_speed=max_l_speed,
        delta_l_speed=delta_l_speed,
        min_size=min_size,
        max_size=max_size,
        delta_size=delta_size,
        depth_percent=depth_percent,
    )
    return build_table(
        output,
        "grey_light",
        font_size="16px",
        index=True,
        text_align="center",
        padding="5px",
    )


if __name__ == "__main__":
    app.run_server(debug=True)