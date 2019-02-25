cmake_minimum_required (VERSION 2.8)

# projectname is the same as the main-executable
project(modint)

#add_definitions('-g')
#add_definitions('-Wall')
#add_definitions('-std=c++11')

add_library(${PROJECT_NAME} ${PROJECT_NAME}.cpp)
