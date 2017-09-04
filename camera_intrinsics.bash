WS="/home/tonirv/ws_zurich_eye/src"
BAG="calib_image"
TARGET="checkerboard.yaml"
#TARGET="apriltag_75_15.yaml"
kalibr_calibrate_cameras --target $WS/rpg_calib/scripts/kalibr_targets/$TARGET --bag $BAG.bag --models pinhole-equi --topics /dvs/image_raw --show-extraction
