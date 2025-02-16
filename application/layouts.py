
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Common style dictionaries
dropdown_style = {
    'width': '100%',
    'padding': '6px',
    'fontSize': '12px'  # Smaller font size for a more compact design
}

input_style = {
    'width': '100%',
    'padding': '6px',  # Reduced padding for a more compact design
    'fontSize': '12px',  # Smaller font size for a more compact design
    'marginBottom': '6px'  # Reduced margin for compactness
}

button_style = {
    'width': '40%',  # Adjusted width for better centering
    'padding': '10px',
    'fontSize': '14px',
    'backgroundColor': '#007BFF',
    'color': 'white',
    'border': 'none',
    'borderRadius': '5px',
    'cursor': 'pointer',
    'margin': 'auto'  # Center the button within its container
}

# Define the layout with pre-filled sample data
layout = html.Div([
    html.Div([ 
        # Container for NCT ID input and Autofill button
        html.Div([ 
            dcc.Input(
                id='nct_id',
                type='text',
                placeholder="Enter NCT ID",
                value="",  # Pre-fill with sample data
                style={'width': '50%', 'fontSize': '14px', 'display': 'inline-block'}
            ),
            html.Button(
                'Autofill', 
                id='autofill-button', 
                style={
                    'width': '20%',  # Smaller width for the button
                    'padding': '6px',
                    'fontSize': '12px',
                    'backgroundColor': 'blue',  # Green color for the button
                    'color': 'white',
                    'border': 'none',
                    'borderRadius': '5px',
                    'cursor': 'pointer',
                    'marginLeft': '10px',  # Add some space between the input and button
                    'display': 'inline-block'
                }
            )
        ], style={'textAlign': 'center', 'margin': '10px 0'}),  # Center the container
    ]),

    # Add "OR" text and horizontal line
    html.Div([
        html.Div("OR", style={'textAlign': 'center', 'fontSize': '14px', 'margin': '10px 0'}),
        html.Hr(style={'width': '50%', 'margin': 'auto', 'border': '1px solid #ccc'})
    ]),

    # 2x2 Grid Layout for Categories
    html.Div([ 
        html.Div([ 
            # First Box: Medical Features
            html.Div([ 
                html.H4("Medical Features", style={'fontSize': '12px', 'marginBottom': '8px'}),
                html.Div([ 
                    dcc.Input(id='study_design', type='text', placeholder="Study Design", value="", style=input_style),
                    dcc.Input(id='study_title', type='text', placeholder="Study Title", value="", style=input_style),
                    dcc.Input(id='primary_outcome_measures', type='text', placeholder="Primary Outcome Measures", value="", style=input_style),
                    dcc.Input(id='secondary_outcome_measures', type='text', placeholder="Secondary Outcome Measures", value="", style=input_style)
                ], style={'display': 'grid', 'gridTemplateColumns': 'repeat(2, 1fr)', 'gap': '6px', 'marginBottom': '6px'})
            ], style={'border': '1px solid #ccc', 'padding': '8px', 'margin': '8px', 'flex': 1, 'maxWidth': '40%'}), 

            # Second Box: Categorical Columns
            html.Div([ 
                html.H4("Categorical Columns", style={'fontSize': '12px', 'marginBottom': '8px'}),
                html.Div([ 
                    dcc.Input(id='sponsor', type='text', placeholder="Sponsor", value="", style=input_style),
                    dcc.Input(id='conditions', type='text', placeholder="Conditions", value="", style=input_style),
                    dcc.Input(id='brief_summary', type='text', placeholder="Brief Summary", value="", style=input_style),
                    dcc.Input(id='collaborators', type='text', placeholder="Collaborators", value="", style=input_style),
                    dcc.Dropdown(id='sex', options=[{'label': 'Male', 'value': 'male'}, {'label': 'Female', 'value': 'female'}, {'label': 'All', 'value': 'all'}], value='', placeholder="Select Sex", style=dropdown_style),
                    dcc.Dropdown(id='age', options=[{'label': 'Adult', 'value': 'adult'}, {'label': 'Older Adult', 'value': 'older_adult'}, {'label': 'Child', 'value': 'child'}], value='', placeholder="Select Age Group", style=dropdown_style),
                    dcc.Dropdown(id='phases', options=[{'label': 'Phase 1', 'value': 'phase1'}, {'label': 'Phase 2', 'value': 'phase2'}, {'label': 'Phase 3', 'value': 'phase3'}, {'label': 'Phase 4', 'value': 'phase4'}], value='', placeholder="Select Phase", style=dropdown_style),
                    dcc.Dropdown(id='funder_type', options=[{'label': 'Other', 'value': 'other'}, {'label': 'Industry', 'value': 'industry'}, {'label': 'Other Government', 'value': 'other_gov'}, {'label': 'Federal', 'value': 'federal'}], value='', placeholder="Select Funder Type", style=dropdown_style)
                ], style={'display': 'grid', 'gridTemplateColumns': 'repeat(2, 1fr)', 'gap': '6px', 'marginBottom': '6px'})
            ], style={'border': '1px solid #ccc', 'padding': '8px', 'margin': '8px', 'flex': 1, 'maxWidth': '40%'}), 
        ], style={'display': 'flex', 'flexWrap': 'wrap', 'gap': '8px', 'marginTop': '6px', 'justifyContent': 'center'}), 

        # Numeric columns
        html.Div([ 
            html.Div([ 
                html.H4("Numeric Columns", style={'fontSize': '12px', 'marginBottom': '8px'}),
                html.Div([ 
                    dcc.Input(id='enrollment', type='text', placeholder="Enrollment", value="", style=input_style),
                ], style={'display': 'grid', 'gridTemplateColumns': 'repeat(2, 1fr)', 'gap': '6px', 'marginBottom': '6px'})
            ], style={'border': '1px solid #ccc', 'padding': '8px', 'margin': '8px', 'flex': 1, 'maxWidth': '40%'}),

            html.Div([ 
                html.H4("TF-IDF Vector", style={'fontSize': '12px', 'marginBottom': '8px'}),
                html.Div([ 
                    dcc.Input(id='city', type='text', placeholder="City", value="", style=input_style),
                    dcc.Input(id='sponsor_tf', type='text', placeholder="Sponsor", value="", style=input_style)
                ], style={'display': 'grid', 'gridTemplateColumns': 'repeat(2, 1fr)', 'gap': '6px', 'marginBottom': '6px'})
            ], style={'border': '1px solid #ccc', 'padding': '8px', 'margin': '8px', 'flex': 1, 'maxWidth': '40%'}), 
        ], style={'display': 'flex', 'flexWrap': 'wrap', 'gap': '8px', 'marginTop': '6px', 'justifyContent': 'center'}), 
    ], style={'width': '100%', 'margin': 'auto'}),  

    # Centered Predict Button and Output
    html.Div([ 
        html.Button('Predict', id='predict-button', style=button_style)
    ], style={'display': 'flex', 'justifyContent': 'center', 'margin': '10px 0'}),

    html.Div([ 
        html.Div(id='result-output', style={'fontSize': '14px', 'padding': '10px', 'textAlign': 'center'}),
        html.Div(id='error-message', style={'color': 'red', 'fontSize': '14px', 'padding': '10px', 'textAlign': 'center'})
    ], style={'textAlign': 'center', 'marginTop': '20px'})
])
#     html.Div(
#     id='result-output',
#     style={
#         'fontSize': '14px',
#         'padding': '10px',
#         'textAlign': 'left',
#         'border': '1px solid #ccc',  # Add a border around the output
#         'borderRadius': '5px',  # Rounded corners
#         'backgroundColor': '#f9f9f9',  # Light background color
#         'marginTop': '10px',
#         'width': '80%',  # Adjust width as needed
#         'margin': 'auto'  # Center the output container
#     }
# )
