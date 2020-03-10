smfc_gen(
  PYTHON
  TARGET_NAME demo_fbs_python
  OUTPUT_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
  SOURCES ${PROJECT_SOURCE_DIR}/schema/demo_service.fbs)

# tests
add_custom_target(python_test ALL)
add_dependencies(python_test demo_fbs_python)

file(GLOB TEST_CASES tests/test_*.py)
foreach(test_case ${TEST_CASES})
  get_filename_component(case_name ${test_case} NAME_WE)
  add_custom_target(${case_name}_target DEPENDS demo_fbs_python)
  add_dependencies(python_test ${case_name}_target)
  add_test(NAME ${case_name} 
           COMMAND env FBS_PATH=${CMAKE_CURRENT_BINARY_DIR}/smf_gen ${CMAKE_CURRENT_SOURCE_DIR}/python_env ${test_case})
  add_dependencies(python_test ${case_name}_target)
  add_dependencies(${case_name}_target demo_server)
endforeach()
