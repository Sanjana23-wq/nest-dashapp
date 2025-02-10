import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Common style dictionary
dropdown_style = {
    'width': '100%',
    'padding': '10px'
}

button_style = {
    'width': '50%',
    'margin': 'auto',
    'display': 'block',
    'padding': '10px',
    'fontSize': '16px',
    'backgroundColor': '#007BFF',
    'color': 'white',
    'border': 'none',
    'borderRadius': '5px',
    'cursor': 'pointer'
}

layout = html.Div([
    # Centered NCT ID Dropdown
    html.Div([
        dcc.Dropdown(
            id='nct_id',
            options=[{'label': 'NCT ID', 'value': 'nct_id'}],
            placeholder="Select NCT ID",
            style={'width': '50%', 'margin': 'auto'}
        )
    ], style={'textAlign': 'center', 'margin': '20px'}),

    # Grid Layout for Other Dropdowns and Input Fields
    html.Div([

        # First Row
        html.Div([
            dcc.Dropdown(
                id='study_design',
                options=[{'label': 'Study Design', 'value': 'study_design'}],
                placeholder="Study Design",
                style=dropdown_style
            ),
            dcc.Dropdown(
                id='study_title',
                options=[{'label': 'Study Title', 'value': 'study_title'}],
                placeholder="Study Title",
                style=dropdown_style
            ),
            dcc.Dropdown(
                id='primary_outcome_enrollment',
                options=[{'label': 'Primary Outcome Enrollment', 'value': 'primary_outcome_enrollment'}],
                placeholder="Primary Outcome Enrollment",
                style=dropdown_style
            ),
            dcc.Dropdown(
                id='secondary_outcome_enrollment',
                options=[{'label': 'Secondary Outcome Enrollment', 'value': 'secondary_outcome_enrollment'}],
                placeholder="Secondary Outcome Enrollment",
                style=dropdown_style
            )
        ], style={'display': 'grid', 'gridTemplateColumns': 'repeat(4, 1fr)', 'gap': '20px', 'marginBottom': '30px'}),

        # Second Row
        html.Div([
            dcc.Dropdown(
                id='sponsor',
                options=[{'label': 'Sponsor', 'value': 'sponsor'}],
                placeholder="Sponsor",
                style=dropdown_style
            ),
            dcc.Dropdown(
                id='conditions',
                options=[{'label': 'Conditions', 'value': 'conditions'}],
                placeholder="Conditions",
                style=dropdown_style
            ),
            dcc.Dropdown(
                id='interventions',
                options=[{'label': 'Interventions', 'value': 'interventions'}],
                placeholder="Interventions",
                style=dropdown_style
            ),
            dcc.Dropdown(
                id='sex',
                options=[ 
                    {'label': 'ALL', 'value': 'ALL'},
                    {'label': 'MALE', 'value': 'MALE'},
                    {'label': 'FEMALE', 'value': 'FEMALE'}
                ],
                placeholder="Sex",
                style=dropdown_style
            )
        ], style={'display': 'grid', 'gridTemplateColumns': 'repeat(4, 1fr)', 'gap': '20px', 'marginBottom': '30px'}),

        # Third Row
        html.Div([
            dcc.Dropdown(
                id='age',
                options=[
                    {'label': 'ADULT', 'value': 'ADULT'},
                    {'label': 'CHILD', 'value': 'CHILD'},
                    {'label': 'OLDER_ADULT', 'value': 'OLDER_ADULT'}
                ],
                placeholder="Age",
                style=dropdown_style
            ),
            dcc.Dropdown(
                id='study_title_intervention',
                options=[{'label': 'Study Title (Intervention)', 'value': 'study_title_intervention'}],
                placeholder="Study Title (Intervention)",
                style=dropdown_style
            ),
            dcc.Dropdown(
                id='brief_summary',
                options=[{'label': 'Brief Summary', 'value': 'brief_summary'}],
                placeholder="Brief Summary",
                style=dropdown_style
            ),
            dcc.Dropdown(
                id='enrollment',
                options=[{'label': 'Enrollment', 'value': 'enrollment'}],
                placeholder="Enrollment",
                style=dropdown_style
            )
        ], style={'display': 'grid', 'gridTemplateColumns': 'repeat(4, 1fr)', 'gap': '20px', 'marginBottom': '30px'}),

        # Fourth Row
        html.Div([
            dcc.Dropdown(
                id='zip',
                options=[{'label': 'ZIP Code', 'value': 'zip'}],
                placeholder="ZIP Code",
                style=dropdown_style
            ),
            dcc.Dropdown(
                id='time_taken_for_enrollment',
                options=[{'label': 'Time Taken for Enrollment', 'value': 'time_taken_for_enrollment'}],
                placeholder="Time Taken for Enrollment",
                style=dropdown_style
            ),
            dcc.Dropdown(
                id='funder_type',
                options=[{'label': 'Funder Type', 'value': 'funder_type'}],
                placeholder="Funder Type",
                style=dropdown_style
            ),
            dcc.Dropdown(
                id='phases',
                options=[
                    {'label': 'Phase 1', 'value': 'phase1'},
                    {'label': 'Phase 2', 'value': 'phase2'},
                    {'label': 'Phase 3', 'value': 'phase3'},
                    {'label': 'Phase 4', 'value': 'phase4'}
                ],
                placeholder="Phases",
                style=dropdown_style
            )
        ], style={'display': 'grid', 'gridTemplateColumns': 'repeat(4, 1fr)', 'gap': '20px', 'marginBottom': '30px'})
    ], style={'width': '80%', 'margin': 'auto'}),

    # Centered Predict Button (Not a Dropdown)
    html.Div([
        html.Button(
            'Predict',
            id='predict-button',
            style=button_style
        )
    ], style={'textAlign': 'center', 'margin': '20px'})
])
