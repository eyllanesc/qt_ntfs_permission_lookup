 
cmake_minimum_required(VERSION 3.5)

project(qt_ntfs_permission_lookup LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include(FetchContent)

FetchContent_Declare(
  pybind11_sources
  GIT_REPOSITORY https://github.com/pybind/pybind11.git
  GIT_TAG        v2.5.0
)

FetchContent_GetProperties(pybind11_sources)

if(NOT pybind11_sources_POPULATED)
  FetchContent_Populate(pybind11_sources)

  add_subdirectory(
    ${pybind11_sources_SOURCE_DIR}
    ${pybind11_sources_BINARY_DIR}
    )
endif()

find_package(Qt5 COMPONENTS Core REQUIRED)
add_definitions(-DQT_NO_KEYWORDS)

# FIND_PACKAGE(SQLite3 REQUIRED)

SET(SOURCE_DIR "qt_ntfs_permission_lookup")
include_directories(${SOURCE_DIR})

file(GLOB SOURCES
    "${SOURCE_DIR}/*.cpp"
)

pybind11_add_module(qt_ntfs_permission_lookup ${SOURCES} "${SOURCE_DIR}/qt_ntfs_permission_lookup.cpp")

target_link_libraries(qt_ntfs_permission_lookup PRIVATE Qt5::Core)