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

# Define the layout of the app with CSS styling
app.layout = html.Div(style={
    'backgroundColor': '#f4faff',
    'fontFamily': 'Arial, sans-serif',
    'padding': '20px'
}, children=[

    # Header
    html.H1(children="Soul Foods Sales Data Visualiser",
            style={
                'textAlign': 'center',
                'color': '#007BFF',
                'fontSize': '38px',
                'fontWeight': 'bold',
                'marginBottom': '30px'}),

    # Sub-header
    html.Div(children='''Compare Pink Morsel sales before and after the price increase on January 15, 2021.''',
             style={
                 'textAlign': 'center',
                 'fontSize': '20px',
                 'color': '#555',
                 'marginBottom': '20px'}),

    # Radio buttons for selecting region with horizontal layout and no empty space
    html.Div([
        html.Label("Select Region:", style={'fontSize': '18px', 'color': '#333'}),
        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
                {'label': 'All', 'value': 'all'}
            ],
            value='all',
            style={
                'display': 'flex',
                'justifyContent': 'space-between',  # Tighten spacing between items
                'padding': '5px',
                'backgroundColor': '#e0f4fc',
                'border': '1px solid #007BFF',
                'borderRadius': '10px',
                'boxShadow': '2px 2px 10px rgba(0, 0, 0, 0.1)',
                'fontSize': '16px',
                'color': '#00796B'
            }
        )
    ], style={'margin': '20px auto', 'width': '40%', 'textAlign': 'center', 'padding': '5px', 'borderRadius': '15px',
              'backgroundColor': '#eef9ff'}),

    # Line chart for sales data with enhanced styling and legend
    dcc.Graph(
        id='sales-line-chart',
        style={
            'height': '600px',
            'border': '2px solid #007BFF',
            'padding': '10px',
            'borderRadius': '15px',
            'backgroundColor': '#ffffff',
            'boxShadow': '2px 2px 10px rgba(0, 0, 0, 0.1)'
        }
    )
])


# Define callback to update the chart based on selected region
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_line_chart(selected_region):
    # Filter data by the selected region, or show all regions if 'all' is selected
    if selected_region == 'all':
        filtered_df = df.groupby('date').sum().reset_index()  # Aggregate the data when showing all
        fig = px.line(filtered_df, x='date', y='sales', title=f'Sales in All Regions')  # Single line for all regions
    else:
        filtered_df = df[df['region'] == selected_region]
        # Use specific color for each region
        region_color_map = {
            'north': 'blue',
            'east': 'orange',
            'south': 'green',
            'west': 'red'
        }
        fig = px.line(filtered_df, x='date', y='sales', title=f'Sales in {selected_region.title()} Region')
        fig.update_traces(line_color=region_color_map[selected_region])  # Set specific color

    # Set the price increase date and marketing event date
    price_increase_date = pd.Timestamp('2021-01-15')
    marketing_event_date = pd.Timestamp('2020-07-01')

    # Get the highest sales date and value
    highest_sales_date = filtered_df.loc[filtered_df['sales'].idxmax()]['date']
    highest_sales_value = filtered_df['sales'].max()

    # Annotation for Price Increase
    fig.add_annotation(
        x=price_increase_date,
        y=highest_sales_value,
        text="Price Increase",
        showarrow=True,
        arrowhead=2,
        arrowsize=1.5,
        arrowwidth=1.5,
        arrowcolor='blue',
        ax=0,
        ay=-30,
        font=dict(size=12, color="white"),
        bgcolor="red",
        bordercolor="black",
        borderwidth=1.5,
        borderpad=2,
        opacity=0.8,
        xanchor='left',
        yanchor='top',
    )

    # Annotation for Highest Sales
    fig.add_annotation(
        x=highest_sales_date,
        y=highest_sales_value,
        text="Highest Sales",
        showarrow=True,
        arrowhead=2,
        arrowsize=1.5,
        arrowwidth=1.5,
        arrowcolor='green',
        ax=0,
        ay=-40,
        font=dict(size=12, color="black"),
        bgcolor="yellow",
        bordercolor="black",
        borderwidth=1.5,
        borderpad=2,
        opacity=0.8,
        xanchor='left',
        yanchor='top',
    )

    # Update layout with axis labels, legend, and overall styling
    fig.update_layout(
        yaxis_title='Sales',
        xaxis_title='Date',
        plot_bgcolor='#f9f9f9',
        paper_bgcolor='#f4faff',
        font=dict(family="Arial, sans-serif", size=14),
        legend_title="Region",
        legend=dict(orientation="h", yanchor="bottom", y=1, xanchor="center", x=0.5, title_text="Regions",
                    bordercolor="Black", borderwidth=1)
    )

    return fig


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
