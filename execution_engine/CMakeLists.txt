cmake_minimum_required(VERSION 3.20)
project(execution_engine)

add_library(execution_engine STATIC
    src/order_router.cpp
    src/risk_engine.cpp
)

target_include_directories(execution_engine PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)
