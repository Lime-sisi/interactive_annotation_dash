from dash import Dash, html, dcc, Input, Output
import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px
import plotly.colors as pc
import pandas as pd
import numpy as np

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000,3650), 
                   np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), 
                   np.random.normal(48000,70000,3650)], 
                  index=[1992,1993,1994,1995])


# calculate mean and standard error for error bars
df_std_error = df.sem(axis=1)
df_means = df.mean(axis=1)
z_score = 1.96
margin_error = z_score * df_std_error

# The strftime to parse time
x_coordinate = pd.to_datetime(df.index,format='%Y').strftime('%Y')

# create customized colorscale
reds = pc.sequential.Reds
blues = pc.sequential.Blues
reds_interp = pc.sample_colorscale(reds, [i/4 for i in range(5)])
blues_interp = pc.sample_colorscale(blues, [i/5 for i in range(6)])
ccmap=[]
ccmap = blues_interp[::-1] + reds_interp
customized_cscale = [[v,c] for v,c in zip(np.linspace(0,1,11),ccmap)]


#construct duplicated color list for fake trace's colorscale
all_colors = [c for c in ccmap for i in range(2)]

# construct duplicated numeric list for fake trace's colorscale
matching_numeric_arr = np.linspace(0,1,12)
duplicated_numeric_arr = [num for num in matching_numeric_arr for _ in range(2)]
paper_cscale = [[v,c] for c, v in zip(all_colors,duplicated_numeric_arr[1:])]


# helper function to get color index for each bar
def color_idx(pos_in_between):
    if pos_in_between < 0:
        idx = 10
    elif pos_in_between > 1:
        idx = 0
    else:
        # 0-8 --> 1-9 ---> 9-1  
        idx = 10-(int(pos_in_between * 9) + 1) 
    return idx    # plain list for color index now

def fill_color_bar(user_choose_y):
    bar_colors= []
    for i in range(4):
        re = (user_choose_y - (df_means.iloc[i] - margin_error.iloc[i]))/(2*margin_error.iloc[i])
        bar_colors.append(customized_cscale[color_idx(re)][1])

    return bar_colors



# slider length matches y_axis length 
min=0
max=51595.8

app = Dash(__name__)

ticks = np.linspace(0,1,12,dtype=np.float64)

app.layout = html.Div([
   
    html.Div([
        dcc.Graph(id='dynamic_graph'),
        dcc.Markdown(
        """
        Note:  
        -- Use the knob on the vertical slider to move the dashed line up and down and observe color changes.  
        -- In probabilistic tasks, constant value comparison indicates if a value is likely to be higher than another.
        """,
        id='note-text'
        ),
        
        html.Div(
                dcc.Slider(
                id='y-slider',
                min=min,
                max=max,
                step=100,
                value=40400,
                vertical=True,
                verticalHeight=442,
                marks={v: '' for v in np.linspace(min, max, 9)}
                ),
                id = 'slider-container'
            ),
        ],
        id='graph-container'
    )       
])
    

@app.callback(
    Output('dynamic_graph', 'figure'),
    Input('y-slider', 'value')
)

def update_plot(value):
    fig = go.Figure()
    custom_y_range = np.linspace(0,51595.8,9)
    
    y_err = go.bar.ErrorY(array = margin_error,color ='lightgrey',width=8.4)
    
    trace_dict = go.Bar(x = x_coordinate.to_list(),
                        y = df_means.to_list(), 
                        marker = dict(
                                    color = fill_color_bar(value)
                        ),
                        hovertemplate = "year: %{x}<br>mean: %{y}<extra></extra>",
                        error_y = y_err,
                        showlegend=False)

    colorbar_fake_trace = go.Scatter(x=[None], y=[None],
                        showlegend=False,mode = 'markers',
                                marker = dict(
                                        colorscale = paper_cscale,
                                        cmin=0,
                                        cmax=1,
                                        colorbar=dict(
                                            tickfont=dict(size=10),
                                            thickness=15,
                                            orientation='h',
                                            x=0.65,
                                            y=-0.05,
                                            xanchor="center",
                                            yanchor="top",
                                            len=0.7,
                                            tickformat=".2f",
                                            tickvals=ticks,
                                            ticktext=[f"{t:.2f}" for t in ticks],
                                            ticks="outside",
                                            ticklen=2
                                        )
                                    ),
                           )

    fig.add_trace(trace_dict)
    fig.add_trace(colorbar_fake_trace)
    
    fig.add_hline(y=value, line_width=0.8, line_dash="dash", line_color="grey",
                     )
  
    fig.add_annotation(
        text=f"{value}",
        x= -1.1, 
        y= value , 
        borderpad = 5,
        height = 10,
        hovertext = "y-axis value of interest",
        bgcolor = "black",
        xshift = 0,
        opacity = 0.31,
        align = "right",
        font = dict(
            color="beige",
            family="verdana, sans-serif",
            size = 12
        ),
        arrowcolor="grey",
        ax=-45,
        ay=0     
    )

    fig.update_xaxes(
            tickmode="array",  # Set tick mode to "array" to use custom tickvals and ticktext
            automargin=True,
            tickvals=np.arange(0,4,1),  # Numeric values, not datetime, for ticks so that y axis can move
            ticktext= x_coordinate.to_list(),
            showline=True,
            linecolor = 'black',
            range=[-1.25, 3 + .65]
        )
    
    
    fig.update_yaxes(
        tickmode="array",  
        tickvals= custom_y_range,  # Custom tick values
        tickformat=".1f",
        ticks="outside",  # Ticks positioned outside the axis line
        automargin=True,
        showline=True,
        linecolor = 'black',
        position = 0.12
    )

    
    
    fig.update_layout(
        autosize=False,
        bargap=0,
        width=690,
        height=630,
        plot_bgcolor = "white",
        title = {
            'text': "Interactive annotation<br>simulation",
            'x': 0.56,
            'y': 0.95,
            'xanchor': "center",
            'font': {'size': 25, 'color': 'black', 'family': 'Arial'}
        }
    )
    
    return fig

if __name__ == "__main__":  
    app.run(debug=True)

