cmake_minimum_required(VERSION 3.30)
project(devcontainer-test LANGUAGES ASM C CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_SCAN_FOR_MODULES Off)

FetchContent_Declare(googletest
    URL https://github.com/google/googletest/releases/download/v1.17.0/googletest-1.17.0.tar.gz
)

FetchContent_MakeAvailable(googletest)

include(CTest)
include(GoogleTest)

add_executable(CalculatorTest CalculatorTest.cpp)
target_link_libraries(CalculatorTest PRIVATE gmock_main)
add_test(NAME CalculatorTest COMMAND CalculatorTest)
