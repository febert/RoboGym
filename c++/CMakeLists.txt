cmake_minimum_required(VERSION 3.2)
set(CMAKE_CXX_STANDARD 11)

project(convertfiles)

#Options
set(SRCS compile.cpp)
set(USE_GL 1) #USE_GL==0 does not work for 131 version since there is no 'nogl' file
set(BIN_NAME ${PROJECT_NAME}_exe)

#Paths
include_directories($ENV{MUJOCO_PY_MJPRO_PATH}/include)
link_directories($ENV{MUJOCO_PY_MJPRO_PATH}/bin)

#Showing path to MuJoCo for checking
message(STATUS "MuJoCo path: " $ENV{MUJOCO_PY_MJPRO_PATH})

#Finding main mujoco library
if(${USE_GL})
    file(GLOB LIB_MUJOCO $ENV{MUJOCO_PY_MJPRO_PATH}/bin/libmujoco[0-9][0-9][0-9].so)
else()
    file(GLOB LIB_MUJOCO $ENV{MUJOCO_PY_MJPRO_PATH}/bin/libmujoco[0-9][0-9][0-9]nogl.so)
endif()
#Showing mujoco library found
message(STATUS "MuJoCo lib: " ${LIB_MUJOCO})

add_executable(${BIN_NAME} ${SRCS})
target_link_libraries(${BIN_NAME} ${LIB_MUJOCO})

#Standard libraries for GL
target_link_libraries(${PROJECT_NAME}_exe GL GLU glut )

#Additional libraries from mujoco package
#target_link_libraries(${PROJECT_NAME}_exe libglew.so )
#target_link_libraries(${PROJECT_NAME}_exe libglfw.so )