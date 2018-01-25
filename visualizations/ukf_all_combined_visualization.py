import plotly.plotly as py
from plotly.graph_objs import *
import pandas as pd
import math
import plotly 

plotly.tools.set_credentials_file(username='username', api_key='api_key')


my_cols=['p1est','p2est','vest','yawest','yawrateest','p1meas','p2meas','p1','p2','v','yaw', 'yawrate','v1_gt','v2_gt', 'NIS_laser', 'NIS_radar']
with open('obj_pose-laser-radar-ukf-output.txt') as f:
    table_ekf_output = pd.read_table(f, sep='\t', header=None, names=my_cols, lineterminator='\n')

t = list(range(0,len(table_ekf_output)))

trace1 = Scatter(
    x=t,
    y=table_ekf_output['p1'],
    xaxis='x2',
    yaxis='y2',
    name = 'p1',
    #mode = 'markers'
)

trace2= Scatter(
    x=t,
    y=table_ekf_output['p1est'],
    xaxis='x2',
    yaxis='y2',
    name = 'p1est',
    #mode = 'markers'
)

trace3 = Scatter(
    x=t,
    y=table_ekf_output['p1meas'],
    xaxis='x2',
    yaxis='y2',
    name = 'p1meas',
    #mode = 'markers'
)

trace4= Scatter(
    x=t,
    y=table_ekf_output['p2'],
    xaxis='x2',
    yaxis='y2',
    name = 'p2',
    #mode = 'markers'
)

trace5 = Scatter(
    x=t,
    y=table_ekf_output['p2est'],
    xaxis='x2',
    yaxis='y2',
    name = 'p2est',
    #mode = 'markers'
)

trace6= Scatter(
    x=t,
    y=table_ekf_output['p2meas'],
    xaxis='x2',
    yaxis='y2',
    name = 'p2meas',
    #mode = 'markers'
)

trace7 = Scatter(
    x=t,
    y=table_ekf_output['v'],
    xaxis='x2',
    yaxis='y2',
    name = 'v',
    #mode = 'markers'
)

trace8 = Scatter(
    x=t,
    y=table_ekf_output['vest'],
    xaxis='x2',
    yaxis='y2',
    name = 'vest',
    #mode = 'markers'
)

trace9= Scatter(
    x=t,
    y=table_ekf_output['yaw'],
    xaxis='x2',
    yaxis='y2',
    name = 'yaw',
    #mode = 'markers'
)

trace10 = Scatter(
    x=t,
    y=table_ekf_output['yawest'],
    xaxis='x2',
    yaxis='y2',
    name = 'yawest',
    #mode = 'markers'
)

trace11= Scatter(
    x=t,
    y=table_ekf_output['yawrate'],
    xaxis='x2',
    yaxis='y2',
    name = 'yawrate',
    #mode = 'markers'
)

trace12= Scatter(
    x=t,
    y=table_ekf_output['yawrateest'],
    xaxis='x2',
    yaxis='y2',
    name = 'yawrateest',
    #mode = 'markers'
)

data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9, trace10, trace11, trace12]

layout = Layout(
    xaxis2=dict(
   
        anchor='x2',
        title='t'
    ),
    yaxis2=dict(
    
        anchor='y2',
        #title='py'
    )
)

fig = Figure(data=data, layout=layout)
py.iplot(fig, filename= 'UKF All Combined')

