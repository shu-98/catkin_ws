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
CMAKE_SOURCE_DIR = /home/sou/catkin_ws/src/cereal_port-master

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/sou/catkin_ws/build_isolated/cereal_port

# Include any dependencies generated for this target.
include CMakeFiles/cereal_port.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/cereal_port.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/cereal_port.dir/flags.make

CMakeFiles/cereal_port.dir/src/CerealPort.cpp.o: CMakeFiles/cereal_port.dir/flags.make
CMakeFiles/cereal_port.dir/src/CerealPort.cpp.o: /home/sou/catkin_ws/src/cereal_port-master/src/CerealPort.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/sou/catkin_ws/build_isolated/cereal_port/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/cereal_port.dir/src/CerealPort.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/cereal_port.dir/src/CerealPort.cpp.o -c /home/sou/catkin_ws/src/cereal_port-master/src/CerealPort.cpp

CMakeFiles/cereal_port.dir/src/CerealPort.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/cereal_port.dir/src/CerealPort.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/sou/catkin_ws/src/cereal_port-master/src/CerealPort.cpp > CMakeFiles/cereal_port.dir/src/CerealPort.cpp.i

CMakeFiles/cereal_port.dir/src/CerealPort.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/cereal_port.dir/src/CerealPort.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/sou/catkin_ws/src/cereal_port-master/src/CerealPort.cpp -o CMakeFiles/cereal_port.dir/src/CerealPort.cpp.s

CMakeFiles/cereal_port.dir/src/CerealPort.cpp.o.requires:

.PHONY : CMakeFiles/cereal_port.dir/src/CerealPort.cpp.o.requires

CMakeFiles/cereal_port.dir/src/CerealPort.cpp.o.provides: CMakeFiles/cereal_port.dir/src/CerealPort.cpp.o.requires
	$(MAKE) -f CMakeFiles/cereal_port.dir/build.make CMakeFiles/cereal_port.dir/src/CerealPort.cpp.o.provides.build
.PHONY : CMakeFiles/cereal_port.dir/src/CerealPort.cpp.o.provides

CMakeFiles/cereal_port.dir/src/CerealPort.cpp.o.provides.build: CMakeFiles/cereal_port.dir/src/CerealPort.cpp.o


# Object files for target cereal_port
cereal_port_OBJECTS = \
"CMakeFiles/cereal_port.dir/src/CerealPort.cpp.o"

# External object files for target cereal_port
cereal_port_EXTERNAL_OBJECTS =

/home/sou/catkin_ws/devel_isolated/cereal_port/lib/libcereal_port.so: CMakeFiles/cereal_port.dir/src/CerealPort.cpp.o
/home/sou/catkin_ws/devel_isolated/cereal_port/lib/libcereal_port.so: CMakeFiles/cereal_port.dir/build.make
/home/sou/catkin_ws/devel_isolated/cereal_port/lib/libcereal_port.so: CMakeFiles/cereal_port.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/sou/catkin_ws/build_isolated/cereal_port/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX shared library /home/sou/catkin_ws/devel_isolated/cereal_port/lib/libcereal_port.so"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/cereal_port.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/cereal_port.dir/build: /home/sou/catkin_ws/devel_isolated/cereal_port/lib/libcereal_port.so

.PHONY : CMakeFiles/cereal_port.dir/build

CMakeFiles/cereal_port.dir/requires: CMakeFiles/cereal_port.dir/src/CerealPort.cpp.o.requires

.PHONY : CMakeFiles/cereal_port.dir/requires

CMakeFiles/cereal_port.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/cereal_port.dir/cmake_clean.cmake
.PHONY : CMakeFiles/cereal_port.dir/clean

CMakeFiles/cereal_port.dir/depend:
	cd /home/sou/catkin_ws/build_isolated/cereal_port && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/sou/catkin_ws/src/cereal_port-master /home/sou/catkin_ws/src/cereal_port-master /home/sou/catkin_ws/build_isolated/cereal_port /home/sou/catkin_ws/build_isolated/cereal_port /home/sou/catkin_ws/build_isolated/cereal_port/CMakeFiles/cereal_port.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/cereal_port.dir/depend
