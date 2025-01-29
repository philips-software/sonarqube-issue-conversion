cmake_minimum_required(VERSION 3.30)
project(devcontainer-test LANGUAGES ASM C CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_SCAN_FOR_MODULES Off)

include(CPM)

CPMAddPackage(
  GITHUB_REPOSITORY google/googletest
  VERSION 1.15.2
  OPTIONS "INSTALL_GTEST OFF" "gtest_force_shared_crt"
)

include(CTest)
include(GoogleTest)

add_executable(test test.cpp)
target_link_libraries(test PRIVATE gmock_main)
