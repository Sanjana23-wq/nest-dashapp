from dash import Input, Output, State
import pandas as pd
import plotly.express as px
from dash import ctx,dcc,html
from dash.exceptions import PreventUpdate
import sys

from data_access.data_management import get_preds_explaination
from analysis.lime import get_lime_figure

if sys.platform=='linux':
    DATA_PATH='/home/research/Documents/NEST/nest-dashapp/Datasets/combined_data_test_show.csv'
else:
    DATA_PATH='E:\Dashappnest\Datasets\combined_data_test_show.csv'

df = pd.read_csv(DATA_PATH)
def register_callbacks(app):
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
         Output('sex', 'value'),
         Output('age', 'value'),
         Output('phases', 'value'),
         Output('funder_type', 'value'),
         Output('enrollment', 'value'),
         Output('city', 'value'),
         Output('sponsor_tf', 'value'),
         Output('error-message', 'children'),
         Output('graph-container','style',allow_duplicate=True),
         Output('pred-message','children',allow_duplicate=True)],
        [Input('autofill-button', 'n_clicks')],
        [State('nct_id', 'value')]
    )
    def autofill_fields(n_clicks, nct_id):
        print(f"Autofill button clicked: {n_clicks}")  # Debugging
        print(f"nct_id entered: {nct_id}")  # Debugging
        style={
            'width': '50%',  # Set width to 50% for the graph container
            'display': 'none',  # Initially hidden
            'padding': '20px',  # Add padding for better readability
            'borderRadius': '10px',  # Optional: Add rounded corners
            'backgroundColor': '#f9f9f9',
        }

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
                row=row.replace(float('nan'),'')
                # Return the values for all fields
                return (
                    row['study_title'], row['study_design'], row['conditions'],row['interventions'],
                    row['primary_outcome_measures'], row['secondary_outcome_measures'], row['study_results'], 
                    row['country'],row['brief_summary'], row['sex'], row['age'],
                    row['phases'], row['funder_type'], row['enrollment'],
                    row['city'], row['sponsor'], "",style,None
                )
            else:
                print("nct_id not found in CSV")  # Debugging
                # If nct_id does not exist, return empty values and show an error message
                return [""] * 16 + ["Error: NCT ID does not exist.",style,None]
        # If the button is not clicked, return empty values
        return [""] * 17+[style,None]
    
    @app.callback(
            [Output('graph-container','children'),
             Output('graph-container','style'),
             Output('pred-message','children')],
            [Input('predict-button', 'n_clicks')],
            [State('nct_id', 'value')]
    )
    def update_graphs(n_clicks, nct_id):
        global df

        if not ctx.triggered:
            raise PreventUpdate

            # Initialize an empty figure (valid structure)
        style={
            'width': '50%',  # Set width to 50% for the graph container
            'display': 'none',  # Initially hidden
            'padding': '20px',  # Add padding for better readability
            'borderRadius': '10px',  # Optional: Add rounded corners
            'backgroundColor': '#f9f9f9',
        }

        button_id=ctx.triggered[0]['prop_id'].split('.')[0]

        if nct_id not in df.nct_id.values:
            return None, style
        if button_id == 'predict-button':
            
            lime_values,pred=get_preds_explaination(nct_id)
            print('lime_values',lime_values)
            features=[]
            weights=[]
            for tup in lime_values:
                vals=tup[0].split(" > ")
                if len(vals)==1:
                    vals=vals[0]
                    vals=vals.split(" <")
                for v in vals:
                    v=v.strip()
                    if v[0].isalpha():
                        features.append(v)
                        break
            
                weights.append(tup[1])
            print('features= ',features)
            fig=get_lime_figure(features,weights)
            graph= dcc.Graph(id='graph-1')
            graph.figure=fig
            style['display']='flex'
            pred_message=f"Predicted Time taken for enrollement: {pred:.2f} Months"
            children=[graph]
        return children,style,pred_message
    

    