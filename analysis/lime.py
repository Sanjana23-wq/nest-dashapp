import plotly.express as px
import pandas as pd

def get_lime_figure(features,weights):
    # Create DataFrame
    df = pd.DataFrame({
        'Features': features,
        'Weights': weights
    })

    # Create the bar chart
    fig = px.bar(
        df,
        x='Weights',
        y='Features',
        orientation='h',
        text=[f"{w:.6f}" for w in weights],
        color_discrete_sequence=['skyblue']
    )

    # Update layout
    fig.update_layout(
        title='Feature Importance Using LIME',
        xaxis_title='Weight',
        yaxis_title='Features',
        xaxis=dict(
            gridwidth=1,
            gridcolor='rgba(0,0,0,0.1)',
            showgrid=True,
        ),
        height=400,
        margin=dict(l=10, r=10, t=40, b=10)
    )

    # Update text position
    fig.update_traces(textposition='auto')
    return fig

if __name__=='__main__':
    pass