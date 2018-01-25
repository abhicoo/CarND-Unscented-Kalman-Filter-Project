import plotly.plotly as py
from plotly.graph_objs import *
import pandas as pd
import math
import plotly 

plotly.tools.set_credentials_file(username='username', api_key='api_key')


my_cols=['p1est','p2est','vest','yawest','yawrateest','p1meas','p2meas','p1','p2','v','yaw', 'yawrate','v1_gt','v2_gt', 'NIS_laser', 'NIS_radar']
with open('obj_pose-laser-radar-ukf-output.txt') as f:
    table_ekf_output = pd.read_table(f, sep='\t', header=None, names=my_cols, lineterminator='\n')

table_ekf_output[0:5]

#Ground Truth
trace1 = Scatter(
    x=table_ekf_output['p1'],
    y=table_ekf_output['p2'],
    xaxis='x2',
    yaxis='y2',
    name = 'ground truth position',
    mode = 'markers'      
)


#estimations
trace2 = Scatter(
    x=table_ekf_output['p1est'],
    y=table_ekf_output['p2est'],
    xaxis='x2',
    yaxis='y2',
    name='UKF position estimation',
    mode = 'markers'       
)

#Measurements
trace3 = Scatter(
    x=table_ekf_output['p1meas'],
    y=table_ekf_output['p2meas'],
    xaxis='x2',
    yaxis='y2',
    name = 'position measurements',
    #mode = 'markers'
)


data = [trace1, trace2, trace3]

layout = Layout(
    xaxis2=dict(
   
        anchor='x2',
        title='px in m'
    ),
    yaxis2=dict(
    
        anchor='y2',
        title='py in m'
    )
)

fig = Figure(data=data, layout=layout)
py.iplot(fig, filename= 'UKF Position Estimation')