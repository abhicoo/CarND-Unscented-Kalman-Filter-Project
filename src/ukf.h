#ifndef UKF_H
#define UKF_H

#include "measurement_package.h"
#include "Eigen/Dense"
#include <vector>
#include <string>
#include <fstream>

using Eigen::MatrixXd;
using Eigen::VectorXd;

class UKF {
public:

  ///* initially set to false, set to true in first call of ProcessMeasurement
  bool is_initialized_;

  ///* if this is false, laser measurements will be ignored (except for init)
  bool use_laser_;

  ///* if this is false, radar measurements will be ignored (except for init)
  bool use_radar_;

  ///* state vector: [pos1 pos2 vel_abs yaw_angle yaw_rate] in SI units and rad
  VectorXd x_;

  ///* state covariance matrix
  MatrixXd P_;

  ///* predicted sigma points matrix
  MatrixXd Xsig_pred_;

  ///* prediction noise matrix
  MatrixXd Q_;

  ///* time when the state is true, in us
  long long time_us_;

  ///* Process noise standard deviation longitudinal acceleration in m/s^2
  double std_a_;

  ///* Process noise standard deviation yaw acceleration in rad/s^2
  double std_yawdd_;

  ///* Laser measurement noise standard deviation position1 in m
  double std_laspx_;

  ///* Laser measurement noise standard deviation position2 in m
  double std_laspy_;

  ///* Radar measurement noise standard deviation radius in m
  double std_radr_;

  ///* Radar measurement noise standard deviation angle in rad
  double std_radphi_;

  ///* Radar measurement noise standard deviation radius change in m/s
  double std_radrd_ ;

  ///* Weights of sigma points
  VectorXd weights_;

  ///* State dimension
  int n_x_;

  ///* Augmented state dimension
  int n_aug_;

  ///* Sigma point spreading parameter
  double lambda_;

  ///* File to write data for visulization
  std::ofstream out_file_;

  /**
   * Constructor
   */
  UKF();

  /**
   * Destructor
   */
  virtual ~UKF();

  /**
   * ProcessMeasurement
   * @param meas_package The latest measurement data of either radar or laser
   */
  void ProcessMeasurement(MeasurementPackage meas_package, VectorXd all_gt_values);

  /**
   * Prediction Predicts sigma points, the state, and the state covariance
   * matrix
   * @param delta_t Time between k and k+1 in s
   */
  void Prediction(double delta_t);

  /**
   * Updates the state and the state covariance matrix using a laser measurement
   * @param meas_package The measurement at k+1
   */
  void UpdateLidar(MeasurementPackage meas_package, VectorXd all_gt_values);

  /**
   * Updates the state and the state covariance matrix using a radar measurement
   * @param meas_package The measurement at k+1
   */
  void UpdateRadar(MeasurementPackage meas_package, VectorXd all_gt_values);

  /**
    * Generates the augmented sigma points
    * @param Xsig_out matrix to store the augmented sigma points
    */
  void AugmentedSigmaPoints(MatrixXd* Xsig_out);

  /**
    * Generates the predicted sigma points
    * @param X_sig_aug matrix that stores the augmented sigma points
    * @delta_t time elasped
    * @param Xsig_out matrix to store the predicted sigma points
    */
  void SigmaPointPrediction(MatrixXd Xsig_aug, double delta_t, MatrixXd* Xsig_out);

  /**
    * Generates the mean predicted state and process covariance matrix
    * @param x_out vector to store the mean state
    * @param P_out matrix to store the mean process covariance matrix
    */
  void PredictMeanAndCovariance(VectorXd* x_out, MatrixXd* P_out);

  /**
    * Generates the mean predicted measurement and measurement covariance matrix for radar
    * @param z_out vector to store the mean measurement
    * @param S_out matrix to store the mean measurement covariance matrix
    */
  void PredictRadarMeasurement(MatrixXd* Zsig_out, VectorXd* z_out, MatrixXd* S_out);

  /**
    * Generates the mean predicted measurement and measurement covariance matrix for lidar
    * @param z_out vector to store the mean measurement
    * @param S_out matrix to store the mean measurement covariance matrix
    */
  void PredictLidarMeasurement(MatrixXd* Zsig_out, VectorXd* z_out, MatrixXd* S_out);

  /**
    * Generates the radar cross correlation matrix
    * @param Zsig matix that contains values of sigma points in measurement space
    * @param z_pred vector that contains value of state in measurement space
    * @param T_out matrix to store the cross correlation matrix
    */
  void RadarCrossCorrelationMatrix(MatrixXd Zsig, VectorXd z_pred, MatrixXd* T_out);

  /**
    * Generates the lidar cross correlation matrix
    * @param Zsig matix that contains values of sigma points in measurement space
    * @param z_pred vector that contains value of state in measurement space
    * @param T_out matrix to store the cross correlation matrix
    */
  void LidarCrossCorrelationMatrix(MatrixXd Zsig, VectorXd z_pred, MatrixXd* T_out);

};

#endif /* UKF_H */
