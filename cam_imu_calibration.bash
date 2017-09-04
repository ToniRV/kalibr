# Cam-IMU
WS="/home/tonirv/ws_zurich_eye/src"
CHAIN="calib_image"
BAG="calib_image_imu"
TARGET="checkerboard.yaml"
#TARGET="apriltag_75_15.yaml"
kalibr_calibrate_imu_camera --target $WS/rpg_calib/scripts/kalibr_targets/$TARGET --bag $BAG.bag --cam camchain-$CHAIN.yaml --imu $WS/rpg_calib/zurich_eye/imu_davis_mpu6150.yaml --time-calibration
