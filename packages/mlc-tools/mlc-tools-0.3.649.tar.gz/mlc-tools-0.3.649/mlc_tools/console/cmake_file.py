
CMAKE = '''cmake_minimum_required(VERSION 3.6.2)
SET(ROOT ${CMAKE_SOURCE_DIR})
project(@{project_name})
file(GLOB_RECURSE SRC ${ROOT}/gen/*.cpp ${ROOT}/external/*.cpp)
if(WIN32)
    add_definitions(-W1 -std=c++14)
else()
    add_definitions(-Wall -std=c++14)
endif()
include_directories(${ROOT}/gen ${ROOT}/external)
add_executable(${PROJECT_NAME} ${SRC} ${ROOT}/__main.cpp)
target_link_libraries(${PROJECT_NAME})'''

MAIN_CPP = '''#include "Main.h"

int main(int argc, char ** args)
{
    mg::Main::main();
    return 0;
}
'''