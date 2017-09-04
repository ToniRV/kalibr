WS="/home/tonirv/ws_zurich_eye/src"
CHAIN="calib_image"
BAG="calib_image_imu_quad"
CAM_NAME="DAVIS-84010032"
kalibr_calibrate_imu_camera --target $WS/rpg_calib/scripts/kalibr_targets/apriltag_75_15.yaml --bag $BAG'.bag' --cam camchain-$CHAIN.yaml --imu $WS/rpg_calib/zurich_eye/imu_davis_mpu6150.yaml $WS/rpg_calib/zurich_eye/imu_px4.yaml --imu-models calibrated calibrated --time-calibration --timeoffset-padding 0.1

# Copy to rpg-calib
cp imu-$BAG.yaml $WS/rpg_calib/zurich_eye/quads/kenny_$CAM_NAME.yaml
