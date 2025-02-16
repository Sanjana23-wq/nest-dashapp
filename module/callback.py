from dash import Input, Output, State
import pandas as pd
import dash_html_components as html

def register_callbacks(app):
    # Load the dummy CSV file
    df = pd.read_csv('dummy_data.csv')
    print("CSV Loaded Successfully:")
    print(df)  # Debugging

    @app.callback(
        [Output('study_title', 'value'),
         Output('study_design', 'value'),
         Output('primary_outcome_measures', 'value'),
         Output('secondary_outcome_measures', 'value'),
         Output('sponsor', 'value'),
         Output('conditions', 'value'),
         Output('brief_summary', 'value'),
         Output('collaborators', 'value'),
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
                    row['study_title'], row['study_design'], row['primary_outcome_measures'],
                    row['secondary_outcome_measures'], row['sponsor'], row['conditions'],
                    row['brief_summary'], row['collaborators'], row['sex'], row['age'],
                    row['phases'], row['funder_type'], row['enrollment'],
                    row['city'], row['sponsor_tf'], ""
                )
            else:
                print("nct_id not found in CSV")  # Debugging
                # If nct_id does not exist, return empty values and show an error message
                return [""] * 15 + ["Error: NCT ID does not exist."]
        # If the button is not clicked, return empty values
        return [""] * 16

    @app.callback(
        Output('result-output', 'children'),
        [Input('predict-button', 'n_clicks')],
        [State('study_title', 'value'),
         State('study_design', 'value'),
         State('primary_outcome_measures', 'value'),
         State('secondary_outcome_measures', 'value'),
         State('sponsor', 'value'),
         State('conditions', 'value'),
         State('brief_summary', 'value'),
         State('collaborators', 'value'),
         State('sex', 'value'),
         State('age', 'value'),
         State('phases', 'value'),
         State('funder_type', 'value'),
         State('enrollment', 'value'),
         State('city', 'value'),
         State('sponsor_tf', 'value')]
    )


    def display_autofilled_data(n_clicks, study_title, study_design, primary_outcome_measures, secondary_outcome_measures,
                                sponsor, conditions, brief_summary, collaborators, sex, age, phases, funder_type,
                                enrollment, city, sponsor_tf):
        if n_clicks:
            # Return each field in a separate Div, effectively stacking them vertically
            return html.Div([
                html.Div(f"Study Title: {study_title}"),
                html.Div(f"Study Design: {study_design}"),
                html.Div(f"Primary Outcome Measures: {primary_outcome_measures}"),
                html.Div(f"Secondary Outcome Measures: {secondary_outcome_measures}"),
                html.Div(f"Sponsor: {sponsor}"),
                html.Div(f"Conditions: {conditions}"),
                html.Div(f"Brief Summary: {brief_summary}"),
                html.Div(f"Collaborators: {collaborators}"),
                html.Div(f"Sex: {sex}"),
                html.Div(f"Age: {age}"),
                html.Div(f"Phases: {phases}"),
                html.Div(f"Funder Type: {funder_type}"),
                html.Div(f"Enrollment: {enrollment}"),
                html.Div(f"City: {city}"),
                html.Div(f"Sponsor TF: {sponsor_tf}")
            ])
        return ""
