#----------------------------------------------------------------
# Generated CMake target import file for configuration "Debug".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "openPMD::openPMD" for configuration "Debug"
set_property(TARGET openPMD::openPMD APPEND PROPERTY IMPORTED_CONFIGURATIONS DEBUG)
set_target_properties(openPMD::openPMD PROPERTIES
  IMPORTED_LOCATION_DEBUG "${_IMPORT_PREFIX}/lib/libopenPMD.so"
  IMPORTED_SONAME_DEBUG "libopenPMD.so"
  )

list(APPEND _IMPORT_CHECK_TARGETS openPMD::openPMD )
list(APPEND _IMPORT_CHECK_FILES_FOR_openPMD::openPMD "${_IMPORT_PREFIX}/lib/libopenPMD.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
