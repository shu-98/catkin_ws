# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "ca_msgs: 5 messages, 0 services")

set(MSG_I_FLAGS "-Ica_msgs:/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(ca_msgs_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/Bumper.msg" NAME_WE)
add_custom_target(_ca_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ca_msgs" "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/Bumper.msg" "std_msgs/Header"
)

get_filename_component(_filename "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/ChargingState.msg" NAME_WE)
add_custom_target(_ca_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ca_msgs" "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/ChargingState.msg" "std_msgs/Header"
)

get_filename_component(_filename "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/Mode.msg" NAME_WE)
add_custom_target(_ca_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ca_msgs" "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/Mode.msg" "std_msgs/Header"
)

get_filename_component(_filename "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/PlaySong.msg" NAME_WE)
add_custom_target(_ca_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ca_msgs" "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/PlaySong.msg" ""
)

get_filename_component(_filename "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/DefineSong.msg" NAME_WE)
add_custom_target(_ca_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ca_msgs" "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/DefineSong.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(ca_msgs
  "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/Bumper.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ca_msgs
)
_generate_msg_cpp(ca_msgs
  "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/ChargingState.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ca_msgs
)
_generate_msg_cpp(ca_msgs
  "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/PlaySong.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ca_msgs
)
_generate_msg_cpp(ca_msgs
  "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/Mode.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ca_msgs
)
_generate_msg_cpp(ca_msgs
  "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/DefineSong.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ca_msgs
)

### Generating Services

### Generating Module File
_generate_module_cpp(ca_msgs
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ca_msgs
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(ca_msgs_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(ca_msgs_generate_messages ca_msgs_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/Bumper.msg" NAME_WE)
add_dependencies(ca_msgs_generate_messages_cpp _ca_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/ChargingState.msg" NAME_WE)
add_dependencies(ca_msgs_generate_messages_cpp _ca_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/Mode.msg" NAME_WE)
add_dependencies(ca_msgs_generate_messages_cpp _ca_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/PlaySong.msg" NAME_WE)
add_dependencies(ca_msgs_generate_messages_cpp _ca_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/DefineSong.msg" NAME_WE)
add_dependencies(ca_msgs_generate_messages_cpp _ca_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ca_msgs_gencpp)
add_dependencies(ca_msgs_gencpp ca_msgs_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ca_msgs_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(ca_msgs
  "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/Bumper.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ca_msgs
)
_generate_msg_eus(ca_msgs
  "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/ChargingState.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ca_msgs
)
_generate_msg_eus(ca_msgs
  "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/PlaySong.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ca_msgs
)
_generate_msg_eus(ca_msgs
  "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/Mode.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ca_msgs
)
_generate_msg_eus(ca_msgs
  "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/DefineSong.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ca_msgs
)

### Generating Services

### Generating Module File
_generate_module_eus(ca_msgs
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ca_msgs
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(ca_msgs_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(ca_msgs_generate_messages ca_msgs_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/Bumper.msg" NAME_WE)
add_dependencies(ca_msgs_generate_messages_eus _ca_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/ChargingState.msg" NAME_WE)
add_dependencies(ca_msgs_generate_messages_eus _ca_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/Mode.msg" NAME_WE)
add_dependencies(ca_msgs_generate_messages_eus _ca_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/PlaySong.msg" NAME_WE)
add_dependencies(ca_msgs_generate_messages_eus _ca_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/DefineSong.msg" NAME_WE)
add_dependencies(ca_msgs_generate_messages_eus _ca_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ca_msgs_geneus)
add_dependencies(ca_msgs_geneus ca_msgs_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ca_msgs_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(ca_msgs
  "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/Bumper.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ca_msgs
)
_generate_msg_lisp(ca_msgs
  "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/ChargingState.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ca_msgs
)
_generate_msg_lisp(ca_msgs
  "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/PlaySong.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ca_msgs
)
_generate_msg_lisp(ca_msgs
  "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/Mode.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ca_msgs
)
_generate_msg_lisp(ca_msgs
  "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/DefineSong.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ca_msgs
)

### Generating Services

### Generating Module File
_generate_module_lisp(ca_msgs
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ca_msgs
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(ca_msgs_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(ca_msgs_generate_messages ca_msgs_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/Bumper.msg" NAME_WE)
add_dependencies(ca_msgs_generate_messages_lisp _ca_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/ChargingState.msg" NAME_WE)
add_dependencies(ca_msgs_generate_messages_lisp _ca_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/Mode.msg" NAME_WE)
add_dependencies(ca_msgs_generate_messages_lisp _ca_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/PlaySong.msg" NAME_WE)
add_dependencies(ca_msgs_generate_messages_lisp _ca_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/DefineSong.msg" NAME_WE)
add_dependencies(ca_msgs_generate_messages_lisp _ca_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ca_msgs_genlisp)
add_dependencies(ca_msgs_genlisp ca_msgs_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ca_msgs_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(ca_msgs
  "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/Bumper.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ca_msgs
)
_generate_msg_nodejs(ca_msgs
  "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/ChargingState.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ca_msgs
)
_generate_msg_nodejs(ca_msgs
  "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/PlaySong.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ca_msgs
)
_generate_msg_nodejs(ca_msgs
  "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/Mode.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ca_msgs
)
_generate_msg_nodejs(ca_msgs
  "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/DefineSong.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ca_msgs
)

### Generating Services

### Generating Module File
_generate_module_nodejs(ca_msgs
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ca_msgs
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(ca_msgs_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(ca_msgs_generate_messages ca_msgs_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/Bumper.msg" NAME_WE)
add_dependencies(ca_msgs_generate_messages_nodejs _ca_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/ChargingState.msg" NAME_WE)
add_dependencies(ca_msgs_generate_messages_nodejs _ca_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/Mode.msg" NAME_WE)
add_dependencies(ca_msgs_generate_messages_nodejs _ca_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/PlaySong.msg" NAME_WE)
add_dependencies(ca_msgs_generate_messages_nodejs _ca_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/DefineSong.msg" NAME_WE)
add_dependencies(ca_msgs_generate_messages_nodejs _ca_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ca_msgs_gennodejs)
add_dependencies(ca_msgs_gennodejs ca_msgs_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ca_msgs_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(ca_msgs
  "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/Bumper.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ca_msgs
)
_generate_msg_py(ca_msgs
  "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/ChargingState.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ca_msgs
)
_generate_msg_py(ca_msgs
  "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/PlaySong.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ca_msgs
)
_generate_msg_py(ca_msgs
  "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/Mode.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ca_msgs
)
_generate_msg_py(ca_msgs
  "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/DefineSong.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ca_msgs
)

### Generating Services

### Generating Module File
_generate_module_py(ca_msgs
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ca_msgs
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(ca_msgs_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(ca_msgs_generate_messages ca_msgs_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/Bumper.msg" NAME_WE)
add_dependencies(ca_msgs_generate_messages_py _ca_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/ChargingState.msg" NAME_WE)
add_dependencies(ca_msgs_generate_messages_py _ca_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/Mode.msg" NAME_WE)
add_dependencies(ca_msgs_generate_messages_py _ca_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/PlaySong.msg" NAME_WE)
add_dependencies(ca_msgs_generate_messages_py _ca_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sou/catkin_ws/src/create_autonomy/ca_msgs/msg/DefineSong.msg" NAME_WE)
add_dependencies(ca_msgs_generate_messages_py _ca_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ca_msgs_genpy)
add_dependencies(ca_msgs_genpy ca_msgs_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ca_msgs_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ca_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ca_msgs
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(ca_msgs_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ca_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ca_msgs
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(ca_msgs_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ca_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ca_msgs
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(ca_msgs_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ca_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ca_msgs
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(ca_msgs_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ca_msgs)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ca_msgs\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ca_msgs
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(ca_msgs_generate_messages_py std_msgs_generate_messages_py)
endif()
