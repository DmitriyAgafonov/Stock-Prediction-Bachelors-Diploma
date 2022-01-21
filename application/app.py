import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np

import plotly.graph_objs as go
import plotly.express as px

import warnings
warnings.filterwarnings('ignore')

# -------------------------------------------------------

BS = dbc.themes.CYBORG

app = dash.Dash(__name__, external_stylesheets=[BS])


# ------------import and set dataframes-------------------


last_train_val = float(0.6671207107686448)
first_timestamp = '2018-01-01'
second_timestamp = '2019-09-01'
# outfile = r'C:\Users\adima\Desktop\thesis\data_overview\data\train_val_test.npz'
#
# npzfile = np.load(outfile)
# print(npzfile.files)
#
# X_train = npzfile['X_train']
# y_train = npzfile['y_train']
# X_val = npzfile['X_val']
# y_val = npzfile['y_val']
# X_test = npzfile['X_test']
# y_test = npzfile['y_test']

ti_df = pd.read_csv(r'C:\Users\adima\Desktop\thesis\data_overview\data\pre_ready_data\tech_info.csv', index_col='Date')
ti_df = ti_df[ti_df.index<=second_timestamp]


ind_list = ['GS', 'MA7', 'MA21',
       'EMA', 'PCh_up', 'PCh_dn','20STD', 'upper_band',
       'lower_band', 'LeadingSpanA', 'LeadingSpanB', 'BaseLine',
       'ConversionLine', 'MassIndex', 'Stoch', 'StochSignal', 'rsi', 'EMA12',
       'EMA26', 'MACD','ROC7', 'momentum', 'VWAP', 'MFI']

pred_df = pd.read_csv(r'C:\Users\adima\Desktop\thesis\project\data\predictions_final.csv', index_col='Date')
stat_train = pd.read_csv(r'C:\Users\adima\Desktop\thesis\project\data\stationaty_train.csv', index_col='Date')
df = pd.read_csv(r'C:\Users\adima\Desktop\thesis\data_overview\data\ready_data.csv', index_col = 'Date')

gs_train_stat = stat_train[['GS']]
gs_real = df[['GS']]

# print(pred_df)
# print(gs_train_stat)
# print(gs_real)



# -------------------------------------------------------

def plt3():
    trace0 = go.Scatter(
        x=gs_real.index, y=gs_real['GS'], name= 'Real', marker ={'color': 'white'} ##1f77b4
            )

    trace1 = go.Scatter(
            x=pred_df.index, y= pred_df['Predicted_inverse'], name='Predicted', marker ={'color': '#FF1493'} #ff7f0e
        )

    # trace2 = go.Scatter(
    #         x=df2_test_.index, y=df2_test_['BEER_PROD'], name= 'Beer test part', marker ={'color': 'white'}
    #     )



    data= [trace0, trace1]
        # data =[]
    layout = go.Layout(
            title="Stock prediction Graph from "+second_timestamp,
            height=800,
        )

    fig = go.Figure(data=data, layout=layout)



    fig.add_shape(type="line",
                  # xref="x",
                  # yref="paper",
                  x0=pred_df.index[0],
                  y0=-15,
                  x1=pred_df.index[0],
                  y1=360,
                  line=dict(color="red", width=1, ),
                  # fillcolor=fillcolor,
                  # layer=layer
                  )

    fig.update_xaxes(rangeslider_visible=True)

    fig.update_layout(
            xaxis_title="Time",
            yaxis_title="Value",
            template='plotly_dark'
    )
    return fig






# -------------------------------------------------------


app.layout = html.Div([

    html.H1("Stock Price Prediction", style={'margin': '1% 0 1% 7.5%'}),
    html.Hr(style={'background-color': 'grey', 'size': '1px', 'width': '85%'}),

        html.H5("Techncal Indicatiors untill "+second_timestamp, style={'margin': '1.5% 0 1% 8.4%'}),

            dbc.Row([
                dbc.Col(dbc.Label('Choose tech indicator'),
                        width={'size': 3, 'offset': 2})

                # dbc.Col(dbc.Label('Smooth type'),
                #         width={'size': 3, 'offset': 2}),
            ]),

            dbc.Row([
                dbc.Col(

                    dcc.Dropdown(id='feature_drop1',
                                 options=[
                                     {'label': i, 'value': i} for i in ind_list
                                 ],
                                 value=['GS'],
                                 style = {"background-color": "#1A1A1A", 'margin': '0 0 5% 0', 'color': 'black'},
                                 multi=True

                                 ),
                    width={'size': 3, 'offset': 2}
                )

            ]),




        dbc.Row([

            dbc.Col(dcc.Graph(id='graph1'),
                # width=10, lg={'size': 10, 'offset': 1}
                width={'size': 10, 'offset': 1}
                    )

        ]),

    dbc.Row([

        dbc.Col(dbc.Table.from_dataframe(ti_df[['Open', 'High', 'Low', 'GS', 'Adj Close', 'Volume']].head(5), striped=True, bordered=True, hover=True),
                width={'size': 10, 'offset': 1}
                # width=10, lg={'size': 10, 'offset': 1}
                )

    ]),

    html.Hr(style={'background-color': 'grey', 'size': '1px', 'width': '83%'}),
    html.H5("Goldman Sachs Stock Prediction", style={'margin': '1.5% 0 1% 8.4%'}),

    dbc.Row([

            dbc.Col(dcc.Graph(id='graph3', figure=plt3()),
                # width=10, lg={'size': 10, 'offset': 1}
                width={'size': 10, 'offset': 1}
                    )

        ])
])


@app.callback(
    Output('graph1', 'figure'),
    [Input('feature_drop1', 'value')])
def plt1(feature_drop1):
    #cols = feature_drop1

    data = []

    for i in feature_drop1:
        data.append(go.Scatter(
            x=ti_df.index, y=ti_df[i], name=i
        ))

    layout = go.Layout(
        title="Goldman Sachs Group",
        height=670,
    )

    fig = go.Figure(data=data, layout=layout)

    fig.update_xaxes(rangeslider_visible=True)

    fig.update_layout(
        xaxis_title="Time",
        yaxis_title="Deviation",
        template='plotly_dark')


    return fig


if __name__ == '__main__':
    app.run_server(debug=True)