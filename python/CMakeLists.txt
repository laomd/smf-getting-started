smfc_gen(
  PYTHON
  TARGET_NAME DEMO_FBS_PYTHON
  OUTPUT_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
  SOURCES ../src/demo_service.fbs)

# tests
add_custom_target(python_test)
add_dependencies(python_test DEMO_FBS_PYTHON)
