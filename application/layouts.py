import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import sys

if sys.platform=='linux':
    IMAGE_PATH='/home/research/Documents/NEST/nest-dashapp/assets/novartis background image.jpg'
else:
    IMAGE_PATH="E:\Dashappnest\assets\novartis background image.jpg"
# Common style dictionaries
dropdown_style = {
    'width': '100%',
    'padding': '6px',
    'fontSize': '12px',  # Smaller font size for a more compact design
    'marginBottom': '10px',  # Add space below each dropdown
    'color': 'blue'  # Blue text for dropdowns
}

input_style = {
    'width': '100%',
    'padding': '6px',  # Reduced padding for a more compact design
    'fontSize': '12px',  # Smaller font size for a more compact design
    'marginBottom': '10px',  # Add space below each input field
    'color': 'black'  # Black text for input fields
}

pred_style = {
    'width': '99%',
    'padding': '5px',  # Reduced padding for a more compact design
    'fontSize': '26px',  # Smaller font size for a more compact design
    'marginBottom': '9px',  # Add space below each input field
    'color': 'blue'  
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
    # Header Section with Title
    html.Div([
        html.H1("EnrollPredict AI", style={'color': 'blue', 'textAlign': 'center', 'marginBottom': '20px'}),
        html.Img(
            src='https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Novartis-Logo.svg/2560px-Novartis-Logo.svg.png',  # Adjust path based on your setup
            style={
                'position': 'absolute',
                'top': '10px',
                'left': '0px',
                'height': '50px'
            }
        )
    ], style={'position': 'relative'}),
    

    html.Div(id='main-container', children=[
        # Left Side: Input Fields
        html.Div(id='input-container', children=[
            html.Div([ 
                # Container for NCT ID input and Autofill button
                html.Div([ 
                    dcc.Input(
                        id='nct_id',
                        type='text',
                        placeholder="Enter NCT ID",
                        value="",  # Pre-fill with sample data
                        style={
                            'width': '50%', 
                            'fontSize': '14px', 
                            'display': 'inline-block', 
                            'marginBottom': '10px',
                            'color': 'blue',  # Blue text
                            'border': '2px solid yellow'  # Yellow outline
                        }
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
                            'display': 'inline-block',
                            'marginBottom': '10px'  # Add space below the button
                        }
                    )
                ], style={'textAlign': 'center', 'margin': '10px 0'}),  # Center the container
            ]),

            # Add "OR" text and horizontal line
            html.Div([
                #html.Div("OR", style={'textAlign': 'center', 'fontSize': '14px', 'margin': '10px 0'}),
                html.Hr(style={'width': '50%', 'margin': 'auto', 'border': '2px solid #ccc'})
            ]),

            # 2x2 Grid Layout for Categories
            html.Div([ 
                html.Div([ 
                    # First Box: Medical Features
                    html.Div([ 
                        html.H4("Medical Features", style={'fontSize': '12px', 'marginBottom': '8px', 'color': 'red'}),
                        html.Div([ 
                            dcc.Input(id='study_design', type='text', placeholder="Study Design", value="", style=input_style),
                            dcc.Input(id='study_title', type='text', placeholder="Study Title", value="", style=input_style),
                            dcc.Input(id='Conditions', type='text', placeholder="Conditions", value="", style=input_style),
                            dcc.Input(id='brief_summary', type='text', placeholder="brief_summary", value="", style=input_style),
                            dcc.Input(id='interventions', type='text', placeholder="interventions", value="", style=input_style),
                            dcc.Input(id='primary_outcome_measures', type='text', placeholder="Primary Outcome Measures", value="", style=input_style),
                            dcc.Input(id='secondary_outcome_measures', type='text', placeholder="Secondary Outcome Measures", value="", style=input_style)
                        ], style={'display': 'grid', 'gridTemplateColumns': 'repeat(2, 1fr)', 'gap': '10px', 'marginBottom': '10px'})  # Add gap between grid items
                    ], style={'border': '2px solid yellow', 'padding': '8px', 'margin': '8px', 'flex': 1, 'maxWidth': '40%'}),  # Yellow border

                    # Second Box: Categorical Columns
                    html.Div([ 
                        html.H4("Categorical Features", style={'fontSize': '12px', 'marginBottom': '8px', 'color': 'red'}),
                        html.Div([ 
                            dcc.Input(id='study_result', type='text', placeholder="study_result", value="", style=input_style),
                            dcc.Input(id='country', type='text', placeholder="Conditions", value="", style=input_style),
                            # dcc.Input(id='brief_summary', type='text', placeholder="Brief Summary", value="", style=input_style),
                            # dcc.Input(id='collaborators', type='text', placeholder="Collaborators", value="", style=input_style),
                            dcc.Input(id='sex', type='text', placeholder="Sex", value="", style=input_style),
                            dcc.Input(id='age', type='text', placeholder="Age", value="", style=input_style),
                            dcc.Input(id='phases', type='text', placeholder="Phases", value="", style=input_style),
                            dcc.Input(id='funder_type', type='text', placeholder="Funder type", value="", style=input_style),
                        ], style={'display': 'grid', 'gridTemplateColumns': 'repeat(2, 1fr)', 'gap': '10px', 'marginBottom': '10px'})  # Add gap between grid items
                    ], style={'border': '2px solid yellow', 'padding': '8px', 'margin': '8px', 'flex': 1, 'maxWidth': '40%'}),  # Yellow border
                ], style={'display': 'flex', 'flexWrap': 'wrap', 'gap': '10px', 'marginTop': '10px', 'justifyContent': 'center'}), 

                # Numeric columns
                html.Div([ 
                    html.Div([ 
                        html.H4("Numerical Features", style={'fontSize': '12px', 'marginBottom': '8px', 'color': 'red'}),
                        html.Div([ 
                            dcc.Input(id='enrollment', type='text', placeholder="Enrollment", value="", style=input_style),
                        ], style={'display': 'grid', 'gridTemplateColumns': 'repeat(2, 1fr)', 'gap': '10px', 'marginBottom': '10px',})  # Add gap between grid items
                    ], style={'border': '1px solid #ccc', 'padding': '8px', 'margin': '8px', 'flex': 1, 'maxWidth': '40%','border': '2px solid yellow'}),

                    html.Div([ 
                        html.H4("TF-IDF Features", style={'fontSize': '12px', 'marginBottom': '8px', 'color': 'red'}),
                        html.Div([ 
                            dcc.Input(id='city', type='text', placeholder="City", value="", style=input_style),
                            dcc.Input(id='sponsor_tf', type='text', placeholder="Sponsor", value="", style=input_style)
                        ], style={'display': 'grid', 'gridTemplateColumns': 'repeat(2, 1fr)', 'gap': '10px', 'marginBottom': '10px'})  # Add gap between grid items
                    ], style={'border': '2px solid yellow', 'padding': '8px', 'margin': '8px', 'flex': 1, 'maxWidth': '40%'}),  # Yellow border
                ], style={'display': 'flex', 'flexWrap': 'wrap', 'gap': '10px', 'marginTop': '10px', 'justifyContent': 'center'}), 
            ], style={'width': '100%', 'margin': 'auto'}),  

            # Centered Predict Button and Output
            html.Div([ 
                html.Button('Predict', id='predict-button', style=button_style),
                html.Label(id='pred-message',children=None, style=pred_style)
            ], style={'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center', 'gap': '10px', 'margin': '10px 0'}),

            html.Div([ 
                html.Div(id='result-output', style={'fontSize': '14px', 'padding': '10px', 'textAlign': 'center'}),
                html.Div(id='error-message', style={'color': 'red', 'fontSize': '14px', 'padding': '10px', 'textAlign': 'center'})
            ], style={'textAlign': 'center', 'marginTop': '20px'})
        ], style={
            'backgroundImage': f'url({IMAGE_PATH})',  # Replace with your image URL
            'backgroundSize': 'cover',
            'backgroundPosition': 'center',
            'backgroundRepeat': 'no-repeat',
            'padding': '20px',  # Add padding for better readability
            'borderRadius': '10px',  # Optional: Add rounded corners
            'color': 'white'  # Optional: Change text color for better contrast
        }),

        # Right Side: Graphs (initially hidden)
        html.Div(id='graph-container', children=[
        ], style={
            'width': '50%',  # Set width to 50% for the graph container
            'padding': '20px',  # Add padding for better readability
            'borderRadius': '10px',  # Optional: Add rounded corners
            'backgroundColor': '#f9f9f9',
            'display': 'none',
            'flexDirection':'column',
            'alignItems':'center'
        }),
        ], style={'display': 'flex', 'flexDirection': 'row'})
])

