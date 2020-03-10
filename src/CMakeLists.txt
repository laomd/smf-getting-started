set(SMF_MANAGE_DEPS OFF CACHE "" INTERNAL FORCE)
set(SMF_BUILD_PROGRAMS OFF CACHE "" INTERNAL FORCE)
add_subdirectory(smfrpc EXCLUDE_FROM_ALL)

smfc_gen(
  CPP
  TARGET_NAME DEMO_FBS
  OUTPUT_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
  SOURCES demo_service.fbs)

# server
add_executable(demo_server server/main.cc)
target_link_libraries(demo_server smf::smf)
target_include_directories(demo_server PUBLIC ${CMAKE_CURRENT_BINARY_DIR})
add_dependencies(demo_server DEMO_FBS)

## client
add_executable(demo_client client/main.cc)
target_link_libraries(demo_client smf::smf)
target_include_directories(demo_client PUBLIC ${CMAKE_CURRENT_BINARY_DIR})
add_dependencies(demo_server DEMO_FBS)
