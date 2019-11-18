# CMake generated Testfile for 
# Source directory: /home/sou/catkin_ws/src/create_autonomy/ca_driver
# Build directory: /home/sou/catkin_ws/build_isolated/ca_driver
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_ca_driver_roslint_package "/home/sou/catkin_ws/build_isolated/ca_driver/catkin_generated/env_cached.sh" "/usr/bin/python" "/opt/ros/kinetic/share/catkin/cmake/test/run_tests.py" "/home/sou/catkin_ws/build_isolated/ca_driver/test_results/ca_driver/roslint-ca_driver.xml" "--working-dir" "/home/sou/catkin_ws/build_isolated/ca_driver" "--return-code" "/opt/ros/kinetic/share/roslint/cmake/../../../lib/roslint/test_wrapper /home/sou/catkin_ws/build_isolated/ca_driver/test_results/ca_driver/roslint-ca_driver.xml make roslint_ca_driver")
subdirs(gtest)
