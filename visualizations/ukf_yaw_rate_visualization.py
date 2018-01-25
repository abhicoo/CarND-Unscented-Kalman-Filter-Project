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

trace7 = Scatter(
    x=t,
    y=table_ekf_output['yawrate'],
    xaxis='x2',
    yaxis='y2',
    name = 'ground truth yaw rate ',
    #mode = 'markers'
)

trace8 = Scatter(
    x=t,
    y=table_ekf_output['yawrateest'],
    xaxis='x2',
    yaxis='y2',
    name = 'estimated yaw rate',
    #mode = 'markers'
)



data = [trace7, trace8]

layout = Layout(
    xaxis2=dict(
   
        anchor='x2',
        title='t'
    ),
    yaxis2=dict(
    
        anchor='y2',
        title='rad/s'
    )
)

fig = Figure(data=data, layout=layout)
py.iplot(fig, filename= 'UKF Yaw Rate')