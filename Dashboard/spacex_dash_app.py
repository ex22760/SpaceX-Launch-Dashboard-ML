# Import required libraries
import pandas as pd
import dash
from dash import html, dcc  # Updated import style
from dash.dependencies import Input, Output
import plotly.express as px

# Read the spacex launch data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")

# Get the max and min payload for Task 3, converted to integers
max_payload = int(spacex_df['Payload Mass (kg)'].max())
min_payload = int(spacex_df['Payload Mass (kg)'].min())

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    
    # TASK 1: Add a dropdown list to enable Launch Site selection
    dcc.Dropdown(
        id='site-dropdown',  # Unique identifier for the dropdown
        options=[
            {'label': 'All Sites', 'value': 'ALL'},  # Option for all sites
            {'label': 'CCAFS LC-40', 'value': 'CCAFS SLC-40'},
            {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
            {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
            {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'}
        ],  # Options containing labels and values
        value='ALL',  # Default value is 'ALL' (to show data for all sites by default)
        placeholder="Select a Launch Site here",  # Placeholder text to guide the user
        searchable=True,  # Allows the user to search for launch sites
        style={'width': '50%', 'padding': '3px', 'font-size': '20px', 'margin': 'auto'}  # Styling of the dropdown
    ),
    
    html.Br(),
    
    # TASK 2: Add a pie chart to show the total successful launches count for all sites
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),
    
    html.P("Payload range (Kg):"),
    
    # TASK 3: Add a slider to select payload range
    dcc.RangeSlider(
        id='payload-slider',
        min=min_payload,
        max=max_payload,
        step=100,
        marks={i: str(i) for i in range(min_payload, max_payload + 1, 500)},  # Display steps of 500 on the slider
        value=[min_payload, max_payload],  # Initial range of payload
    ),
    
    html.Br(),
    
    # TASK 4: Add a scatter chart to show the correlation between payload and launch success
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(
    Output('success-pie-chart', 'figure'),
    [Input('site-dropdown', 'value')]
)
def update_pie_chart(selected_site):
    if selected_site == 'ALL':
        # All sites (display success counts per launch site)
        site_data = spacex_df.groupby(['Launch Site', 'class']).size().reset_index(name='count')
        fig = px.pie(site_data, values='count', names='Launch Site', title='Total Success Launches by Site')
    else:
        # Specific site
        site_data = spacex_df[spacex_df['Launch Site'] == selected_site].groupby('class').size().reset_index(name='count')
        fig = px.pie(site_data, values='count', names='class', title=f'Launch Success ({selected_site})')
    return fig

# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(
    Output('success-payload-scatter-chart', 'figure'),
    [Input('site-dropdown', 'value'),
     Input('payload-slider', 'value')]
)
def update_scatter_chart(selected_site, payload_range):
    # Filter by selected site
    if selected_site == 'ALL':
        filtered_df = spacex_df[(spacex_df['Payload Mass (kg)'] >= payload_range[0]) & 
                                (spacex_df['Payload Mass (kg)'] <= payload_range[1])]
    else:
        filtered_df = spacex_df[(spacex_df['Launch Site'] == selected_site) & 
                                (spacex_df['Payload Mass (kg)'] >= payload_range[0]) & 
                                (spacex_df['Payload Mass (kg)'] <= payload_range[1])]
    
    # Plot scatter plot with color representing the 'Booster Version Category'
    fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class', 
                     color='Booster Version Category', title='Success vs Payload Mass')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server()
