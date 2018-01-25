# Unscented Kalman Filter Project Starter Code
Self-Driving Car Engineer Nanodegree Program

In this project utilize an Unscented Kalman Filter to estimate the state of a moving object of interest with noisy lidar and radar measurements. Passing the project requires obtaining RMSE values that are lower that the tolerance outlined in the project rubric. 

This project involves the Term 2 Simulator which can be downloaded [here](https://github.com/udacity/self-driving-car-sim/releases)

This repository includes two files that can be used to set up and intall [uWebSocketIO](https://github.com/uWebSockets/uWebSockets) for either Linux or Mac systems. For windows you can use either Docker, VMware, or even [Windows 10 Bash on Ubuntu](https://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/) to install uWebSocketIO. Please see [this concept in the classroom](https://classroom.udacity.com/nanodegrees/nd013/parts/40f38239-66b6-46ec-ae68-03afd8a601c8/modules/0949fca6-b379-42af-a919-ee50aa304e6a/lessons/f758c44c-5e40-4e01-93b5-1a82aa4e044f/concepts/16cf4a78-4fc7-49e1-8621-3450ca938b77) for the required version and installation scripts.

Once the install for uWebSocketIO is complete, the main program can be built and ran by doing the following from the project top directory.

1. mkdir build
2. cd build
3. cmake ..
4. make
5. ./UnscentedKF

The following image of Position Estimation wrt to ground truth and sensor measurements

![Position Estimation](visualizations_graph/UKF_Position_Estimation.png)

The following image of Px Estimation wrt to ground truth and sensor measurements

![Px Estimation](visualizations_graph/UKF_Px.png)

The following image of Velocity Estimation wrt to ground truth velocity

![Velocity Estimation](visualizations_graph/UKF_V.png)

The following image of Yaw Estimation wrt to ground truth yaw

![Yaw Estimation](visualizations_graph/UKF_Yaw.png)

The following image of Yaw Rate Estimation wrt to ground truth yaw rate

![Yaw Rate Estimation](visualizations_graph/UKF_Yaw_Rate.png)

The following image of All State Estimation wrt to ground truth

![All State Estimation](visualizations_graph/UKF_All_Combined.png)

The following image of NIS for radar

![NIS Radar](visualizations_graph/UKF_NIS_Radar.png)

The following image of NIS for laser

![NIS Laser](visualizations_graph/UKF_NIS_Laser.png)


