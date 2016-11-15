import plotly 
plotly.tools.set_credentials_file(username='deepikasr', api_key='htiu1pfeoz')


import plotly.plotly as py
import plotly.graph_objs as go

file_type = ['raster_images','developer_files','page_layout_files','data_files','game_files','database_files','executable_files','encode_files','web_files','ebook_files','3d_image_files','compressed_files','system_files','spreadsheet_files','setting_file','misc_files'
]
wireless = [7165,35531,0,0,470,0,139337,179,42178,0,0,0,0,312,2567,0]
vlsi = [1575,26540,369,2697,1350,3558,160,0,0,0,0,4653,0,0,0,0]
imaging = [140,13504,0,0,0,0,39,158,1896,27,22,78,78,0,0,]
micro = [0,31676,55,55,0,0,28565,0,5352,0,0,0,0,0,0,1580]

trace0 = go.Scatter(
    x=wireless,
    y=file_type,
    mode='markers',
    name='wieless',
    marker=dict(
        color='rgba(156, 165, 196, 0.95)',
        line=dict(
            color='rgba(156, 165, 200, 1.0)',
            width=1,
        ),
        symbol='circle',
        size=16,
    )
)
trace1 = go.Scatter(
    x=vlsi,
    y=file_type,
    mode='markers',
    name='VLSI',
    marker=dict(
        color='rgba(156, 165, 196, 0.95)',
        line=dict(
            color='rgba(156, 165, 196, 1.0)',
            width=1,
        ),
        symbol='circle',
        size=16,
    )
)

trace2 = go.Scatter(
    x=imaging,
    y=file_type,
    mode='markers',
    name='imaging',
    marker=dict(
        color='rgba(204, 204, 204, 0.95)',
        line=dict(
            color='rgba(217, 217, 217, 1.0)',
            width=1,
        ),
        symbol='circle',
        size=16,
    )
)
trace3 = go.Scatter(
    x=micro,
    y=file_type,
    mode='markers',
    name='micro',
    marker=dict(
        color='rgba(156, 165, 196, 0.95)',
        line=dict(
            color='rgba(156, 165, 196, 1.0)',
            width=1,
        ),
        symbol='circle',
        size=16,
    )
)

data = [trace0, trace1,trace2,trace3]
layout = go.Layout(
    title="different categories of files",
    xaxis=dict(
        showgrid=False,
        showline=True,
        linecolor='rgb(102, 102, 102)',
        titlefont=dict(
            color='rgb(204, 204, 204)'
        ),
        tickfont=dict(
            color='rgb(102, 102, 102)',
        ),
        autotick=False,
        dtick=10000,
        ticks='outside',
        tickcolor='rgb(102, 102, 102)',
    ),
    margin=dict(
        l=140,
        r=40,
        b=50,
        t=80
    ),
    legend=dict(
        font=dict(
            size=10,
        ),
        yanchor='middle',
        xanchor='right',
    ),
    width=800,
    height=600,
    paper_bgcolor='rgb(254, 247, 234)',
    plot_bgcolor='rgb(254, 247, 234)',
    hovermode='closest',
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='lowest-oecd-votes-cast')