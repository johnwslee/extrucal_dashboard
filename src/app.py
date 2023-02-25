from dash import Dash, html, dcc, Input, Output
from extrucal.extrusion import throughput_cal, throughput_table, throughput_plot
from extrucal.cable_extrusion import cable_cal, cable_table, cable_plot
from extrucal.tube_extrusion import tube_cal, tube_table, tube_plot
from extrucal.rod_extrusion import rod_cal, rod_table, rod_plot
from extrucal.sheet_extrusion import sheet_cal, sheet_table, sheet_plot
import dash_bootstrap_components as dbc

# Setup app and layout/frontend
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = dbc.Container(
    [
        html.H1('Extrucal Dashboard', style={'textAlign': 'center'}),
        html.Br(),
        dcc.Tabs(
            [
                dcc.Tab(
                    label='Throughput Calculation',
                    children=[
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Screw Size [mm]'),
                                        dcc.Input(id='screw_size', type='number', value=200),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Melt Density of Material [kg/m^3]'),
                                        dcc.Input(id='melt_density', type='number', value=800),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Number of Screw Flight'),
                                        dcc.Input(id='n_flight', type='number', value=1),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Minimum Screw RPM'),
                                        dcc.Input(id='min_rpm', type='number', value=5),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Maximum Screw RPM'),
                                        dcc.Input(id='max_rpm', type='number', value=50),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Increment of Screw RPM'),
                                        dcc.Input(id='delta_rpm', type='number', value=5),
                                    ],
                                    md=4
                                ),
                                dbc.Col(
                                    [
                                        html.Br(),
                                        html.Br(),
                                        html.H3('Predicted Throughput [kg/hr]'),
                                        html.Iframe(
                                            id='throughput_plot',
                                            style={'border-width': '0', 'width': '100%', 'height': '85%'}
                                            ),
                                        html.H6('Note: Please put cursor onto the data point in the graph for the actual value'),
                                        html.Br(),
                                        html.Br(),
                                        html.H3('Throughput Table'),
                                        html.Iframe(
                                            id='throughput_table',
                                            style={'border-width': '0', 'width': '100%', 'height': '100%'}
                                            ),
                                    ],
                                    md=8
                                )
                            ]
                        )
                    ]
                ),
                dcc.Tab(
                    label='Calculation for Cable Extrusion',
                    children=[
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Insulation Outer Diameter [mm]'),
                                        dcc.Input(id='cable_outer_d', type='number', value=10),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Insulation Thickness [mm]'),
                                        dcc.Input(id='cable_thickness', type='number', value=2),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Solid Density of Material [kg/mm^3]'),
                                        dcc.Input(id='cable_s_density', type='number', value=920),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Melt/Solid Density Ratio'),
                                        dcc.Input(id='cable_density_ratio', type='number', value=0.85),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Minimum Line Speed [mpm]'),
                                        dcc.Input(id='cable_min_l_speed', type='number', value=1),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Maximum Line Speed [mpm]'),
                                        dcc.Input(id='cable_max_l_speed', type='number', value=10),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Increment of Line Speed [mpm]'),
                                        dcc.Input(id='cable_delta_l_speed', type='number', value=1),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Minimum Extruder Size [mm]'),
                                        dcc.Input(id='cable_min_size', type='number', value=40),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Maximum Extruder Size [mm]'),
                                        dcc.Input(id='cable_max_size', type='number', value=100),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Increment of Extruder Size [mm]'),
                                        dcc.Input(id='cable_delta_size', type='number', value=5),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Metering Depth to Extruder Size Ratio'),
                                        dcc.Input(id='cable_depth_percent', type='number', value=0.05),
                                    ],
                                    md=4
                                ),
                                dbc.Col(
                                    [
                                        html.Br(),
                                        html.Br(),
                                        html.H3('Screw RPM w.r.t. Extruder Size & Line Speed'),
                                        html.Iframe(
                                            id='cable_plot',
                                            style={'border-width': '0', 'width': '100%', 'height': '45%'}
                                            ),
                                        html.H6('Note: Please put cursor onto the data point in the graph for the actual value'),
                                        html.Br(),
                                        html.Br(),
                                        html.H3('Screw RPM Table'),
                                        html.Iframe(
                                            id='cable_table',
                                            style={'border-width': '0', 'width': '100%', 'height': '100%'}
                                            ),
                                    ],
                                    md=8
                                )
                            ]
                        )
                    ]
                ),
                dcc.Tab(
                    label='Calculation for Tube Extrusion',
                    children=[
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Tube Outer Diameter [mm]'),
                                        dcc.Input(id='tube_outer_d', type='number', value=10),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Tube Inner Diameter [mm]'),
                                        dcc.Input(id='tube_inner_d', type='number', value=8),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Solid Density of Material [kg/mm^3]'),
                                        dcc.Input(id='tube_s_density', type='number', value=920),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Melt/Solid Density Ratio'),
                                        dcc.Input(id='tube_density_ratio', type='number', value=0.85),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Minimum Line Speed [mpm]'),
                                        dcc.Input(id='tube_min_l_speed', type='number', value=1),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Maximum Line Speed [mpm]'),
                                        dcc.Input(id='tube_max_l_speed', type='number', value=10),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Increment of Line Speed [mpm]'),
                                        dcc.Input(id='tube_delta_l_speed', type='number', value=1),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Minimum Extruder Size [mm]'),
                                        dcc.Input(id='tube_min_size', type='number', value=40),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Maximum Extruder Size [mm]'),
                                        dcc.Input(id='tube_max_size', type='number', value=100),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Increment of Extruder Size [mm]'),
                                        dcc.Input(id='tube_delta_size', type='number', value=5),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Metering Depth to Extruder Size Ratio'),
                                        dcc.Input(id='tube_depth_percent', type='number', value=0.05),
                                    ],
                                    md=4
                                ),
                                dbc.Col(
                                    [
                                        html.Br(),
                                        html.Br(),
                                        html.H3('Screw RPM w.r.t. Extruder Size & Line Speed'),
                                        html.Iframe(
                                            id='tube_plot',
                                            style={'border-width': '0', 'width': '100%', 'height': '45%'}
                                            ),
                                        html.H6('Note: Please put cursor onto the data point in the graph for the actual value'),
                                        html.Br(),
                                        html.Br(),
                                        html.H3('Screw RPM Table'),
                                        html.Iframe(
                                            id='tube_table',
                                            style={'border-width': '0', 'width': '100%', 'height': '100%'}
                                            ),
                                    ],
                                    md=8
                                )
                            ]
                        )
                    ]
                ),
                dcc.Tab(
                    label='Calculation for Rod Extrusion',
                    children=[
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Rod Outer Diameter [mm]'),
                                        dcc.Input(id='rod_outer_d', type='number', value=2),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Number of Die Holes'),
                                        dcc.Input(id='rod_n_holes', type='number', value=10),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Solid Density of Material [kg/mm^3]'),
                                        dcc.Input(id='rod_s_density', type='number', value=920),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Melt/Solid Density Ratio'),
                                        dcc.Input(id='rod_density_ratio', type='number', value=0.85),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Minimum Line Speed [mpm]'),
                                        dcc.Input(id='rod_min_l_speed', type='number', value=1),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Maximum Line Speed [mpm]'),
                                        dcc.Input(id='rod_max_l_speed', type='number', value=10),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Increment of Line Speed [mpm]'),
                                        dcc.Input(id='rod_delta_l_speed', type='number', value=1),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Minimum Extruder Size [mm]'),
                                        dcc.Input(id='rod_min_size', type='number', value=40),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Maximum Extruder Size [mm]'),
                                        dcc.Input(id='rod_max_size', type='number', value=100),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Increment of Extruder Size [mm]'),
                                        dcc.Input(id='rod_delta_size', type='number', value=5),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Metering Depth to Extruder Size Ratio'),
                                        dcc.Input(id='rod_depth_percent', type='number', value=0.05),
                                    ],
                                    md=4
                                ),
                                dbc.Col(
                                    [
                                        html.Br(),
                                        html.Br(),
                                        html.H3('Screw RPM w.r.t. Extruder Size & Line Speed'),
                                        html.Iframe(
                                            id='rod_plot',
                                            style={'border-width': '0', 'width': '100%', 'height': '45%'}
                                            ),
                                        html.H6('Note: Please put cursor onto the data point in the graph for the actual value'),
                                        html.Br(),
                                        html.Br(),
                                        html.H3('Screw RPM Table'),
                                        html.Iframe(
                                            id='rod_table',
                                            style={'border-width': '0', 'width': '100%', 'height': '100%'}
                                            ),
                                    ],
                                    md=8
                                )
                            ]
                        )
                    ]
                ),
                dcc.Tab(
                    label='Calculation for Sheet Extrusion',
                    children=[
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Sheet Width [mm]'),
                                        dcc.Input(id='sheet_width', type='number', value=20),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Sheet Thickness [mm]'),
                                        dcc.Input(id='sheet_thickness', type='number', value=2),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Solid Density of Material [kg/mm^3]'),
                                        dcc.Input(id='sheet_s_density', type='number', value=920),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Melt/Solid Density Ratio'),
                                        dcc.Input(id='sheet_density_ratio', type='number', value=0.85),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Minimum Line Speed [mpm]'),
                                        dcc.Input(id='sheet_min_l_speed', type='number', value=1),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Maximum Line Speed [mpm]'),
                                        dcc.Input(id='sheet_max_l_speed', type='number', value=10),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Increment of Line Speed [mpm]'),
                                        dcc.Input(id='sheet_delta_l_speed', type='number', value=1),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Minimum Extruder Size [mm]'),
                                        dcc.Input(id='sheet_min_size', type='number', value=40),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Maximum Extruder Size [mm]'),
                                        dcc.Input(id='sheet_max_size', type='number', value=100),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Increment of Extruder Size [mm]'),
                                        dcc.Input(id='sheet_delta_size', type='number', value=5),
                                        html.Br(),
                                        html.Br(),
                                        html.H5('Metering Depth to Extruder Size Ratio'),
                                        dcc.Input(id='sheet_depth_percent', type='number', value=0.05),
                                    ],
                                    md=4
                                ),
                                dbc.Col(
                                    [
                                        html.Br(),
                                        html.Br(),
                                        html.H3('Screw RPM w.r.t. Extruder Size & Line Speed'),
                                        html.Iframe(
                                            id='sheet_plot',
                                            style={'border-width': '0', 'width': '100%', 'height': '45%'}
                                            ),
                                        html.H6('Note: Please put cursor onto the data point in the graph for the actual value'),
                                        html.Br(),
                                        html.Br(),
                                        html.H3('Screw RPM Table'),
                                        html.Iframe(
                                            id='sheet_table',
                                            style={'border-width': '0', 'width': '100%', 'height': '100%'}
                                            ),
                                    ],
                                    md=8
                                )
                            ]
                        )
                    ]
                )
            ]
        )
    ]
)

# Setup callbacks/backend for Throughput Plot
@app.callback(
    Output('throughput_plot', 'srcDoc'),
    Input('screw_size', 'value'),
    Input('melt_density', 'value'),
    Input('n_flight', 'value'),
    Input('min_rpm', 'value'),
    Input('max_rpm', 'value'),
    Input('delta_rpm', 'value'),
)
def show_throughput_plot(screw_size, melt_density, n_flight, min_rpm, max_rpm, delta_rpm):
    output = throughput_plot(screw_size, melt_density, n_flight=n_flight, min_rpm=min_rpm, max_rpm=max_rpm, delta_rpm=delta_rpm)
    return output.to_html()

# Setup callbacks/backend for Throughput Table
@app.callback(
    Output('throughput_table', 'srcDoc'),
    Input('screw_size', 'value'),
    Input('melt_density', 'value'),
    Input('n_flight', 'value'),
    Input('min_rpm', 'value'),
    Input('max_rpm', 'value'),
    Input('delta_rpm', 'value'),
)
def show_throughput_table(screw_size, melt_density, n_flight, min_rpm, max_rpm, delta_rpm):
    output = throughput_table(screw_size, melt_density, n_flight=n_flight, min_rpm=min_rpm, max_rpm=max_rpm, delta_rpm=delta_rpm)
    return output.to_html()

# Setup callbacks/backend for Cable Plot
@app.callback(
    Output('cable_plot', 'srcDoc'),
    Input('cable_outer_d', 'value'),
    Input('cable_thickness', 'value'),
    Input('cable_s_density', 'value'),
    Input('cable_density_ratio', 'value'),
    Input('cable_min_l_speed', 'value'),
    Input('cable_max_l_speed', 'value'),
    Input('cable_delta_l_speed', 'value'),
    Input('cable_min_size', 'value'),
    Input('cable_max_size', 'value'),
    Input('cable_delta_size', 'value'),
    Input('cable_depth_percent', 'value'),
)
def show_cable_plot(
    outer_d, thickness, s_density, density_ratio, min_l_speed, max_l_speed, delta_l_speed, 
    min_size, max_size, delta_size, depth_percent
    ):
    output = cable_plot(
        outer_d=outer_d, thickness=thickness, s_density=s_density, density_ratio=density_ratio, 
        min_l_speed=min_l_speed, max_l_speed=max_l_speed, delta_l_speed=delta_l_speed, min_size=min_size,
        max_size=max_size, delta_size=delta_size, depth_percent=depth_percent
        )
    return output.to_html()

# Setup callbacks/backend for Cable Table
@app.callback(
    Output('cable_table', 'srcDoc'),
    Input('cable_outer_d', 'value'),
    Input('cable_thickness', 'value'),
    Input('cable_s_density', 'value'),
    Input('cable_density_ratio', 'value'),
    Input('cable_min_l_speed', 'value'),
    Input('cable_max_l_speed', 'value'),
    Input('cable_delta_l_speed', 'value'),
    Input('cable_min_size', 'value'),
    Input('cable_max_size', 'value'),
    Input('cable_delta_size', 'value'),
    Input('cable_depth_percent', 'value'),
)
def show_cable_table(
    outer_d, thickness, s_density, density_ratio, min_l_speed, max_l_speed, delta_l_speed, 
    min_size, max_size, delta_size, depth_percent
    ):
    output = cable_table(
        outer_d=outer_d, thickness=thickness, s_density=s_density, density_ratio=density_ratio, 
        min_l_speed=min_l_speed, max_l_speed=max_l_speed, delta_l_speed=delta_l_speed, min_size=min_size,
        max_size=max_size, delta_size=delta_size, depth_percent=depth_percent
        )
    return output.to_html()

# Setup callbacks/backend for Tube Plot
@app.callback(
    Output('tube_plot', 'srcDoc'),
    Input('tube_outer_d', 'value'),
    Input('tube_inner_d', 'value'),
    Input('tube_s_density', 'value'),
    Input('tube_density_ratio', 'value'),
    Input('tube_min_l_speed', 'value'),
    Input('tube_max_l_speed', 'value'),
    Input('tube_delta_l_speed', 'value'),
    Input('tube_min_size', 'value'),
    Input('tube_max_size', 'value'),
    Input('tube_delta_size', 'value'),
    Input('tube_depth_percent', 'value'),
)
def show_tube_plot(
    outer_d, inner_d, s_density, density_ratio, min_l_speed, max_l_speed, delta_l_speed, 
    min_size, max_size, delta_size, depth_percent
    ):
    output = tube_plot(
        outer_d=outer_d, inner_d=inner_d, s_density=s_density, density_ratio=density_ratio, 
        min_l_speed=min_l_speed, max_l_speed=max_l_speed, delta_l_speed=delta_l_speed, min_size=min_size,
        max_size=max_size, delta_size=delta_size, depth_percent=depth_percent
        )
    return output.to_html()

# Setup callbacks/backend for Tube Table
@app.callback(
    Output('tube_table', 'srcDoc'),
    Input('tube_outer_d', 'value'),
    Input('tube_inner_d', 'value'),
    Input('tube_s_density', 'value'),
    Input('tube_density_ratio', 'value'),
    Input('tube_min_l_speed', 'value'),
    Input('tube_max_l_speed', 'value'),
    Input('tube_delta_l_speed', 'value'),
    Input('tube_min_size', 'value'),
    Input('tube_max_size', 'value'),
    Input('tube_delta_size', 'value'),
    Input('tube_depth_percent', 'value'),
)
def show_tube_table(
    outer_d, inner_d, s_density, density_ratio, min_l_speed, max_l_speed, delta_l_speed, 
    min_size, max_size, delta_size, depth_percent
    ):
    output = tube_table(
        outer_d=outer_d, inner_d=inner_d, s_density=s_density, density_ratio=density_ratio, 
        min_l_speed=min_l_speed, max_l_speed=max_l_speed, delta_l_speed=delta_l_speed, min_size=min_size,
        max_size=max_size, delta_size=delta_size, depth_percent=depth_percent
        )
    return output.to_html()

# Setup callbacks/backend for Rod Plot
@app.callback(
    Output('rod_plot', 'srcDoc'),
    Input('rod_outer_d', 'value'),
    Input('rod_s_density', 'value'),
    Input('rod_n_holes', 'value'),
    Input('rod_density_ratio', 'value'),
    Input('rod_min_l_speed', 'value'),
    Input('rod_max_l_speed', 'value'),
    Input('rod_delta_l_speed', 'value'),
    Input('rod_min_size', 'value'),
    Input('rod_max_size', 'value'),
    Input('rod_delta_size', 'value'),
    Input('rod_depth_percent', 'value'),
)
def show_rod_plot(
    outer_d, s_density, n_holes, density_ratio, min_l_speed, max_l_speed, delta_l_speed, 
    min_size, max_size, delta_size, depth_percent
    ):
    output = rod_plot(
        outer_d=outer_d, s_density=s_density, n_holes=n_holes, density_ratio=density_ratio, 
        min_l_speed=min_l_speed, max_l_speed=max_l_speed, delta_l_speed=delta_l_speed, min_size=min_size,
        max_size=max_size, delta_size=delta_size, depth_percent=depth_percent
        )
    return output.to_html()

# Setup callbacks/backend for Rod Table
@app.callback(
    Output('rod_table', 'srcDoc'),
    Input('rod_outer_d', 'value'),
    Input('rod_s_density', 'value'),
    Input('rod_n_holes', 'value'),
    Input('rod_density_ratio', 'value'),
    Input('rod_min_l_speed', 'value'),
    Input('rod_max_l_speed', 'value'),
    Input('rod_delta_l_speed', 'value'),
    Input('rod_min_size', 'value'),
    Input('rod_max_size', 'value'),
    Input('rod_delta_size', 'value'),
    Input('rod_depth_percent', 'value'),
)
def show_rod_table(
    outer_d, s_density, n_holes, density_ratio, min_l_speed, max_l_speed, delta_l_speed, 
    min_size, max_size, delta_size, depth_percent
    ):
    output = rod_table(
        outer_d=outer_d, s_density=s_density, n_holes=n_holes, density_ratio=density_ratio, 
        min_l_speed=min_l_speed, max_l_speed=max_l_speed, delta_l_speed=delta_l_speed, min_size=min_size,
        max_size=max_size, delta_size=delta_size, depth_percent=depth_percent
        )
    return output.to_html()

# Setup callbacks/backend for Sheet Plot
@app.callback(
    Output('sheet_plot', 'srcDoc'),
    Input('sheet_width', 'value'),
    Input('sheet_thickness', 'value'),
    Input('sheet_s_density', 'value'),
    Input('sheet_density_ratio', 'value'),
    Input('sheet_min_l_speed', 'value'),
    Input('sheet_max_l_speed', 'value'),
    Input('sheet_delta_l_speed', 'value'),
    Input('sheet_min_size', 'value'),
    Input('sheet_max_size', 'value'),
    Input('sheet_delta_size', 'value'),
    Input('sheet_depth_percent', 'value'),
)
def show_sheet_plot(
    width, thickness, s_density, density_ratio, min_l_speed, max_l_speed, delta_l_speed, 
    min_size, max_size, delta_size, depth_percent
    ):
    output = sheet_plot(
        width=width, thickness=thickness, s_density=s_density, density_ratio=density_ratio, 
        min_l_speed=min_l_speed, max_l_speed=max_l_speed, delta_l_speed=delta_l_speed, min_size=min_size,
        max_size=max_size, delta_size=delta_size, depth_percent=depth_percent
        )
    return output.to_html()

# Setup callbacks/backend for Sheet Table
@app.callback(
    Output('sheet_table', 'srcDoc'),
    Input('sheet_width', 'value'),
    Input('sheet_thickness', 'value'),
    Input('sheet_s_density', 'value'),
    Input('sheet_density_ratio', 'value'),
    Input('sheet_min_l_speed', 'value'),
    Input('sheet_max_l_speed', 'value'),
    Input('sheet_delta_l_speed', 'value'),
    Input('sheet_min_size', 'value'),
    Input('sheet_max_size', 'value'),
    Input('sheet_delta_size', 'value'),
    Input('sheet_depth_percent', 'value'),
)
def show_sheet_table(
    width, thickness, s_density, density_ratio, min_l_speed, max_l_speed, delta_l_speed, 
    min_size, max_size, delta_size, depth_percent
    ):
    output = sheet_table(
        width=width, thickness=thickness, s_density=s_density, density_ratio=density_ratio, 
        min_l_speed=min_l_speed, max_l_speed=max_l_speed, delta_l_speed=delta_l_speed, min_size=min_size,
        max_size=max_size, delta_size=delta_size, depth_percent=depth_percent
        )
    return output.to_html()

if __name__ == '__main__':
    app.run_server(debug=True)