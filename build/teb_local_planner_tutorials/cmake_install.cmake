# Install script for directory: /home/slabs-036/Escritorio/omni_move/src/teb_local_planner_tutorials

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/slabs-036/Escritorio/omni_move/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/slabs-036/Escritorio/omni_move/build/teb_local_planner_tutorials/catkin_generated/installspace/teb_local_planner_tutorials.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/teb_local_planner_tutorials/cmake" TYPE FILE FILES
    "/home/slabs-036/Escritorio/omni_move/build/teb_local_planner_tutorials/catkin_generated/installspace/teb_local_planner_tutorialsConfig.cmake"
    "/home/slabs-036/Escritorio/omni_move/build/teb_local_planner_tutorials/catkin_generated/installspace/teb_local_planner_tutorialsConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/teb_local_planner_tutorials" TYPE FILE FILES "/home/slabs-036/Escritorio/omni_move/src/teb_local_planner_tutorials/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/teb_local_planner_tutorials" TYPE DIRECTORY FILES
    "/home/slabs-036/Escritorio/omni_move/src/teb_local_planner_tutorials/launch"
    "/home/slabs-036/Escritorio/omni_move/src/teb_local_planner_tutorials/cfg"
    "/home/slabs-036/Escritorio/omni_move/src/teb_local_planner_tutorials/maps"
    "/home/slabs-036/Escritorio/omni_move/src/teb_local_planner_tutorials/stage"
    "/home/slabs-036/Escritorio/omni_move/src/teb_local_planner_tutorials/scripts"
    REGEX "/\\.svn$" EXCLUDE)
endif()
