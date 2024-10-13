import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Load the formatted sales data
file_path = 'data/formatted_sales_data.csv'
df = pd.read_csv(file_path)

# Convert 'date' column to datetime format for better sorting
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1(children="Soul Foods Sales Data Visualiser",
            style={'textAlign': 'center', 'color': '#007BFF'}),

    # Sub-header with instructions
    html.Div(children='''
        Compare Pink Morsel sales before and after the price increase on January 15, 2021.
    ''', style={'textAlign': 'center', 'fontSize': 20}),

    # Dropdown for selecting region
    html.Div([
        html.Label("Select Region:"),
        dcc.Dropdown(
            id='region-filter',
            options=[{'label': region, 'value': region} for region in df['region'].unique()],
            value='north',  # Default selected value
            clearable=False,
            style={'width': '50%'}
        )
    ], style={'margin': '20px auto', 'width': '50%'}),

    # Line chart for sales data
    dcc.Graph(
        id='sales-line-chart',
        style={'height': '600px'}
    )
])


# Define callback to update the chart based on selected region

@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_line_chart(selected_region):
    # Filter data by the selected region
    filtered_df = df[df['region'] == selected_region]

    # Debugging the date column
    print(filtered_df['date'].min(), filtered_df['date'].max())  # Print date range

    # Set the price increase date and another event date
    price_increase_date = pd.Timestamp('2021-01-15')
    marketing_event_date = pd.Timestamp('2020-07-01')

    # Get the date and value of the highest sales point
    highest_sales_date = filtered_df.loc[filtered_df['sales'].idxmax()]['date']
    highest_sales_value = filtered_df['sales'].max()

    # Plot the chart with filtered data
    fig = px.line(filtered_df, x='date', y='sales', title=f'Sales in {selected_region} Region')

    # Annotation 1: Price Increase
    fig.add_annotation(
        x=price_increase_date,
        y=highest_sales_value,  # Arrow points to the highest sales
        text="Price Increase",
        showarrow=True,
        arrowhead=2,  # Smaller arrowhead
        arrowsize=1.5,  # Reduced arrow size
        arrowwidth=1.5,
        arrowcolor='blue',
        ax=0,
        ay=-30,
        font=dict(size=12, color="white", family="Arial"),  # Smaller font
        bgcolor="red",
        bordercolor="black",
        borderwidth=1.5,  # Smaller border
        borderpad=2,
        opacity=0.8,
        xanchor='left',
        yanchor='top',
    )

    # Annotation 2: Highest Sales
    fig.add_annotation(
        x=highest_sales_date,
        y=highest_sales_value,  # Positioning at the highest sales value
        text="Highest Sales",
        showarrow=True,
        arrowhead=2,  # Smaller arrowhead
        arrowsize=1.5,
        arrowwidth=1.5,
        arrowcolor='green',
        ax=0,
        ay=-40,
        font=dict(size=12, color="black", family="Arial"),  # Smaller font
        bgcolor="yellow",
        bordercolor="black",
        borderwidth=1.5,  # Smaller border
        borderpad=2,
        opacity=0.8,
        xanchor='left',
        yanchor='top',
    )

    # Annotation 3: Marketing Event (Example)
    fig.add_annotation(
        x=marketing_event_date,
        y=filtered_df['sales'].min(),  # Arrow points to the lowest sales
        text="Marketing Event",
        showarrow=True,
        arrowhead=2,
        arrowsize=1.5,
        arrowwidth=1.5,
        arrowcolor='purple',
        ax=0,
        ay=-30,
        font=dict(size=12, color="white", family="Arial"),  # Smaller font
        bgcolor="purple",
        bordercolor="white",
        borderwidth=1.5,
        borderpad=2,
        opacity=0.8,
        xanchor='left',
        yanchor='top',
    )

    # Custom Legend Annotations (higher above the chart in the top-right)
    fig.add_annotation(
        xref="paper", yref="paper",  # Paper coordinates to position it outside
        x=0.95, y=1.25,  # Move legend higher above the chart
        text="Legend:",
        showarrow=False,
        font=dict(size=14, color="black", family="Arial"),
        xanchor="right", yanchor="bottom"
    )

    # Legend entry for Price Increase
    fig.add_annotation(
        xref="paper", yref="paper",
        x=0.95, y=1.20,
        text="• Price Increase (Red)",
        showarrow=False,
        font=dict(size=12, color="red"),
        xanchor="right"
    )

    # Legend entry for Highest Sales
    fig.add_annotation(
        xref="paper", yref="paper",
        x=0.95, y=1.15,
        text="• Highest Sales (Green)",
        showarrow=False,
        font=dict(size=12, color="green"),
        xanchor="right"
    )

    # Legend entry for Marketing Event
    fig.add_annotation(
        xref="paper", yref="paper",
        x=0.95, y=1.10,
        text="• Marketing Event (Purple)",
        showarrow=False,
        font=dict(size=12, color="purple"),
        xanchor="right"
    )

    # Customize layout: add axis labels and adjust margins
    fig.update_layout(
        xaxis_title='Date',
        yaxis_title='Total Sales',
        title_x=0.5,
        margin=dict(l=40, r=40, t=150, b=40),  # Increased top margin for the legend
        hovermode="x"
    )

    return fig


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
