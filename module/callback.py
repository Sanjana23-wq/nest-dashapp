from dash import Input, Output, State
import pandas as pd
import dash_html_components as html
import plotly.express as px
from dash import ctx
from dash.exceptions import PreventUpdate

from data_access.data_management import get_lime

df = pd.read_csv('E:\Dashappnest\Datasets\combined_data_test_show.csv')
def register_callbacks(app):
    # Load the dummy CSV file
    global df
    print("CSV Loaded Successfully:")
    print(df)  # Debugging

    @app.callback(
            
        [Output('study_title', 'value'),
         Output('study_design', 'value'),
         Output('Conditions', 'value'),
         Output('interventions', 'value'),
         Output('primary_outcome_measures', 'value'),
         Output('secondary_outcome_measures', 'value'),
         
         Output('study_result', 'value'),
         Output('country', 'value'),
         Output('brief_summary', 'value'),
        #  Output('collaborators', 'value'),
         Output('sex', 'value'),
         Output('age', 'value'),
         Output('phases', 'value'),
         Output('funder_type', 'value'),
         Output('enrollment', 'value'),
         Output('city', 'value'),
         Output('sponsor_tf', 'value'),
         Output('error-message', 'children')],
        [Input('autofill-button', 'n_clicks')],
        [State('nct_id', 'value')]
    )
    def autofill_fields(n_clicks, nct_id):
        print(f"Autofill button clicked: {n_clicks}")  # Debugging
        print(f"nct_id entered: {nct_id}")  # Debugging

        if n_clicks:
            # Strip any extra spaces and convert to uppercase for matching
            nct_id = nct_id.strip().upper() if nct_id else ""
            print(f"Processed nct_id: {nct_id}")  # Debugging

            # Check if the nct_id exists in the CSV
            if nct_id in df['nct_id'].values:
                print("nct_id found in CSV")  # Debugging
                # Get the row corresponding to the nct_id
                row = df[df['nct_id'] == nct_id].iloc[0]
                print("Row data:")  # Debugging
                print(row)  # Debugging
                # Return the values for all fields
                return (
                    row['study_title'], row['study_design'], row['primary_outcome_measures'], row['conditions'],
                    row['secondary_outcome_measures'], row['study_results'], row['interventions'],
                    row['brief_summary'], row['sex'], row['age'], row['country'],
                    row['phases'], row['funder_type'], row['enrollment'],
                    row['city'], row['sponsor'], ""
                )
            else:
                print("nct_id not found in CSV")  # Debugging
                # If nct_id does not exist, return empty values and show an error message
                return [""] * 16 + ["Error: NCT ID does not exist."]
        # If the button is not clicked, return empty values
        return [""] * 17
    
    @app.callback(
            [Output('graph-1','figure'),
             Output('graph-container','style')],
            [Input('predict-button', 'n_clicks')],
            [State('nct_id', 'value')]
    )
    def update_graphs(n_clicks, nct_id):
        global df

        if not ctx.triggered:
            raise PreventUpdate
        data = {
            'Category': ['A', 'B', 'C', 'D'],
            'Value': [10, 15, 7, 20]
        }

            # Initialize an empty figure (valid structure)
        style={
            'width': '50%',  # Set width to 50% for the graph container
            'display': 'none',  # Initially hidden
            'padding': '20px',  # Add padding for better readability
            'borderRadius': '10px',  # Optional: Add rounded corners
            'backgroundColor': '#f9f9f9',
            'display': None,
        }

        fig = px.bar(data, x='Category', y='Value', title="Feature Weights for LIME Explanation",orientation='h')
        button_id=ctx.triggered[0]['prop_id'].split('.')[0]

        if nct_id not in df.nct_id.values:
            return None, style
        if button_id == 'predict-button':
            
            # Example graphs (replace with your actual graph logic)
            lime_values=get_lime(nct_id)
            style['display']='block'
            print('lime_values',lime_values)
        return fig,style