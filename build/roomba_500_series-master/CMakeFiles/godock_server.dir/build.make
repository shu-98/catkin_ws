# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/sou/catkin_ws/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/sou/catkin_ws/build

# Include any dependencies generated for this target.
include roomba_500_series-master/CMakeFiles/godock_server.dir/depend.make

# Include the progress variables for this target.
include roomba_500_series-master/CMakeFiles/godock_server.dir/progress.make

# Include the compile flags for this target's objects.
include roomba_500_series-master/CMakeFiles/godock_server.dir/flags.make

roomba_500_series-master/CMakeFiles/godock_server.dir/src/godock_server.o: roomba_500_series-master/CMakeFiles/godock_server.dir/flags.make
roomba_500_series-master/CMakeFiles/godock_server.dir/src/godock_server.o: /home/sou/catkin_ws/src/roomba_500_series-master/src/godock_server.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/sou/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object roomba_500_series-master/CMakeFiles/godock_server.dir/src/godock_server.o"
	cd /home/sou/catkin_ws/build/roomba_500_series-master && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/godock_server.dir/src/godock_server.o -c /home/sou/catkin_ws/src/roomba_500_series-master/src/godock_server.cpp

roomba_500_series-master/CMakeFiles/godock_server.dir/src/godock_server.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/godock_server.dir/src/godock_server.i"
	cd /home/sou/catkin_ws/build/roomba_500_series-master && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/sou/catkin_ws/src/roomba_500_series-master/src/godock_server.cpp > CMakeFiles/godock_server.dir/src/godock_server.i

roomba_500_series-master/CMakeFiles/godock_server.dir/src/godock_server.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/godock_server.dir/src/godock_server.s"
	cd /home/sou/catkin_ws/build/roomba_500_series-master && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/sou/catkin_ws/src/roomba_500_series-master/src/godock_server.cpp -o CMakeFiles/godock_server.dir/src/godock_server.s

roomba_500_series-master/CMakeFiles/godock_server.dir/src/godock_server.o.requires:

.PHONY : roomba_500_series-master/CMakeFiles/godock_server.dir/src/godock_server.o.requires

roomba_500_series-master/CMakeFiles/godock_server.dir/src/godock_server.o.provides: roomba_500_series-master/CMakeFiles/godock_server.dir/src/godock_server.o.requires
	$(MAKE) -f roomba_500_series-master/CMakeFiles/godock_server.dir/build.make roomba_500_series-master/CMakeFiles/godock_server.dir/src/godock_server.o.provides.build
.PHONY : roomba_500_series-master/CMakeFiles/godock_server.dir/src/godock_server.o.provides

roomba_500_series-master/CMakeFiles/godock_server.dir/src/godock_server.o.provides.build: roomba_500_series-master/CMakeFiles/godock_server.dir/src/godock_server.o


roomba_500_series-master/CMakeFiles/godock_server.dir/src/GoDock/GoDock.o: roomba_500_series-master/CMakeFiles/godock_server.dir/flags.make
roomba_500_series-master/CMakeFiles/godock_server.dir/src/GoDock/GoDock.o: /home/sou/catkin_ws/src/roomba_500_series-master/src/GoDock/GoDock.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/sou/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object roomba_500_series-master/CMakeFiles/godock_server.dir/src/GoDock/GoDock.o"
	cd /home/sou/catkin_ws/build/roomba_500_series-master && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/godock_server.dir/src/GoDock/GoDock.o -c /home/sou/catkin_ws/src/roomba_500_series-master/src/GoDock/GoDock.cpp

roomba_500_series-master/CMakeFiles/godock_server.dir/src/GoDock/GoDock.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/godock_server.dir/src/GoDock/GoDock.i"
	cd /home/sou/catkin_ws/build/roomba_500_series-master && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/sou/catkin_ws/src/roomba_500_series-master/src/GoDock/GoDock.cpp > CMakeFiles/godock_server.dir/src/GoDock/GoDock.i

roomba_500_series-master/CMakeFiles/godock_server.dir/src/GoDock/GoDock.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/godock_server.dir/src/GoDock/GoDock.s"
	cd /home/sou/catkin_ws/build/roomba_500_series-master && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/sou/catkin_ws/src/roomba_500_series-master/src/GoDock/GoDock.cpp -o CMakeFiles/godock_server.dir/src/GoDock/GoDock.s

roomba_500_series-master/CMakeFiles/godock_server.dir/src/GoDock/GoDock.o.requires:

.PHONY : roomba_500_series-master/CMakeFiles/godock_server.dir/src/GoDock/GoDock.o.requires

roomba_500_series-master/CMakeFiles/godock_server.dir/src/GoDock/GoDock.o.provides: roomba_500_series-master/CMakeFiles/godock_server.dir/src/GoDock/GoDock.o.requires
	$(MAKE) -f roomba_500_series-master/CMakeFiles/godock_server.dir/build.make roomba_500_series-master/CMakeFiles/godock_server.dir/src/GoDock/GoDock.o.provides.build
.PHONY : roomba_500_series-master/CMakeFiles/godock_server.dir/src/GoDock/GoDock.o.provides

roomba_500_series-master/CMakeFiles/godock_server.dir/src/GoDock/GoDock.o.provides.build: roomba_500_series-master/CMakeFiles/godock_server.dir/src/GoDock/GoDock.o


# Object files for target godock_server
godock_server_OBJECTS = \
"CMakeFiles/godock_server.dir/src/godock_server.o" \
"CMakeFiles/godock_server.dir/src/GoDock/GoDock.o"

# External object files for target godock_server
godock_server_EXTERNAL_OBJECTS =

/home/sou/catkin_ws/devel/lib/roomba_500_series/godock_server: roomba_500_series-master/CMakeFiles/godock_server.dir/src/godock_server.o
/home/sou/catkin_ws/devel/lib/roomba_500_series/godock_server: roomba_500_series-master/CMakeFiles/godock_server.dir/src/GoDock/GoDock.o
/home/sou/catkin_ws/devel/lib/roomba_500_series/godock_server: roomba_500_series-master/CMakeFiles/godock_server.dir/build.make
/home/sou/catkin_ws/devel/lib/roomba_500_series/godock_server: /home/sou/catkin_ws/devel/lib/libcereal_port.so
/home/sou/catkin_ws/devel/lib/roomba_500_series/godock_server: /opt/ros/kinetic/lib/libtf.so
/home/sou/catkin_ws/devel/lib/roomba_500_series/godock_server: /opt/ros/kinetic/lib/libtf2_ros.so
/home/sou/catkin_ws/devel/lib/roomba_500_series/godock_server: /opt/ros/kinetic/lib/libactionlib.so
/home/sou/catkin_ws/devel/lib/roomba_500_series/godock_server: /opt/ros/kinetic/lib/libmessage_filters.so
/home/sou/catkin_ws/devel/lib/roomba_500_series/godock_server: /opt/ros/kinetic/lib/libroscpp.so
/home/sou/catkin_ws/devel/lib/roomba_500_series/godock_server: /usr/lib/x86_64-linux-gnu/libboost_filesystem.so
/home/sou/catkin_ws/devel/lib/roomba_500_series/godock_server: /usr/lib/x86_64-linux-gnu/libboost_signals.so
/home/sou/catkin_ws/devel/lib/roomba_500_series/godock_server: /opt/ros/kinetic/lib/libxmlrpcpp.so
/home/sou/catkin_ws/devel/lib/roomba_500_series/godock_server: /opt/ros/kinetic/lib/libtf2.so
/home/sou/catkin_ws/devel/lib/roomba_500_series/godock_server: /opt/ros/kinetic/lib/libroscpp_serialization.so
/home/sou/catkin_ws/devel/lib/roomba_500_series/godock_server: /opt/ros/kinetic/lib/librosconsole.so
/home/sou/catkin_ws/devel/lib/roomba_500_series/godock_server: /opt/ros/kinetic/lib/librosconsole_log4cxx.so
/home/sou/catkin_ws/devel/lib/roomba_500_series/godock_server: /opt/ros/kinetic/lib/librosconsole_backend_interface.so
/home/sou/catkin_ws/devel/lib/roomba_500_series/godock_server: /usr/lib/x86_64-linux-gnu/liblog4cxx.so
/home/sou/catkin_ws/devel/lib/roomba_500_series/godock_server: /usr/lib/x86_64-linux-gnu/libboost_regex.so
/home/sou/catkin_ws/devel/lib/roomba_500_series/godock_server: /opt/ros/kinetic/lib/librostime.so
/home/sou/catkin_ws/devel/lib/roomba_500_series/godock_server: /opt/ros/kinetic/lib/libcpp_common.so
/home/sou/catkin_ws/devel/lib/roomba_500_series/godock_server: /usr/lib/x86_64-linux-gnu/libboost_system.so
/home/sou/catkin_ws/devel/lib/roomba_500_series/godock_server: /usr/lib/x86_64-linux-gnu/libboost_thread.so
/home/sou/catkin_ws/devel/lib/roomba_500_series/godock_server: /usr/lib/x86_64-linux-gnu/libboost_chrono.so
/home/sou/catkin_ws/devel/lib/roomba_500_series/godock_server: /usr/lib/x86_64-linux-gnu/libboost_date_time.so
/home/sou/catkin_ws/devel/lib/roomba_500_series/godock_server: /usr/lib/x86_64-linux-gnu/libboost_atomic.so
/home/sou/catkin_ws/devel/lib/roomba_500_series/godock_server: /usr/lib/x86_64-linux-gnu/libpthread.so
/home/sou/catkin_ws/devel/lib/roomba_500_series/godock_server: /usr/lib/x86_64-linux-gnu/libconsole_bridge.so
/home/sou/catkin_ws/devel/lib/roomba_500_series/godock_server: roomba_500_series-master/CMakeFiles/godock_server.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/sou/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable /home/sou/catkin_ws/devel/lib/roomba_500_series/godock_server"
	cd /home/sou/catkin_ws/build/roomba_500_series-master && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/godock_server.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
roomba_500_series-master/CMakeFiles/godock_server.dir/build: /home/sou/catkin_ws/devel/lib/roomba_500_series/godock_server

.PHONY : roomba_500_series-master/CMakeFiles/godock_server.dir/build

roomba_500_series-master/CMakeFiles/godock_server.dir/requires: roomba_500_series-master/CMakeFiles/godock_server.dir/src/godock_server.o.requires
roomba_500_series-master/CMakeFiles/godock_server.dir/requires: roomba_500_series-master/CMakeFiles/godock_server.dir/src/GoDock/GoDock.o.requires

.PHONY : roomba_500_series-master/CMakeFiles/godock_server.dir/requires

roomba_500_series-master/CMakeFiles/godock_server.dir/clean:
	cd /home/sou/catkin_ws/build/roomba_500_series-master && $(CMAKE_COMMAND) -P CMakeFiles/godock_server.dir/cmake_clean.cmake
.PHONY : roomba_500_series-master/CMakeFiles/godock_server.dir/clean

roomba_500_series-master/CMakeFiles/godock_server.dir/depend:
	cd /home/sou/catkin_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/sou/catkin_ws/src /home/sou/catkin_ws/src/roomba_500_series-master /home/sou/catkin_ws/build /home/sou/catkin_ws/build/roomba_500_series-master /home/sou/catkin_ws/build/roomba_500_series-master/CMakeFiles/godock_server.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : roomba_500_series-master/CMakeFiles/godock_server.dir/depend

