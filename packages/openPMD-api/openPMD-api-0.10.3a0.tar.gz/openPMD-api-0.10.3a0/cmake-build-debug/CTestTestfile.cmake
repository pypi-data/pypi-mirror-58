# CMake generated Testfile for 
# Source directory: /home/axel/src/openPMD/openPMD-api
# Build directory: /home/axel/src/openPMD/openPMD-api/cmake-build-debug
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(Serial.Core "/home/axel/src/openPMD/openPMD-api/cmake-build-debug/bin/CoreTests")
set_tests_properties(Serial.Core PROPERTIES  WORKING_DIRECTORY "/home/axel/src/openPMD/openPMD-api/cmake-build-debug/bin" _BACKTRACE_TRIPLES "/home/axel/src/openPMD/openPMD-api/CMakeLists.txt;847;add_test;/home/axel/src/openPMD/openPMD-api/CMakeLists.txt;0;")
add_test(Serial.Auxiliary "/home/axel/src/openPMD/openPMD-api/cmake-build-debug/bin/AuxiliaryTests")
set_tests_properties(Serial.Auxiliary PROPERTIES  WORKING_DIRECTORY "/home/axel/src/openPMD/openPMD-api/cmake-build-debug/bin" _BACKTRACE_TRIPLES "/home/axel/src/openPMD/openPMD-api/CMakeLists.txt;847;add_test;/home/axel/src/openPMD/openPMD-api/CMakeLists.txt;0;")
add_test(Serial.SerialIO "/home/axel/src/openPMD/openPMD-api/cmake-build-debug/bin/SerialIOTests")
set_tests_properties(Serial.SerialIO PROPERTIES  WORKING_DIRECTORY "/home/axel/src/openPMD/openPMD-api/cmake-build-debug/bin" _BACKTRACE_TRIPLES "/home/axel/src/openPMD/openPMD-api/CMakeLists.txt;847;add_test;/home/axel/src/openPMD/openPMD-api/CMakeLists.txt;0;")
add_test(MPI.ParallelIO "/usr/bin/mpiexec" "-n" "2" "/home/axel/src/openPMD/openPMD-api/cmake-build-debug/bin/ParallelIOTests")
set_tests_properties(MPI.ParallelIO PROPERTIES  WORKING_DIRECTORY "/home/axel/src/openPMD/openPMD-api/cmake-build-debug/bin" _BACKTRACE_TRIPLES "/home/axel/src/openPMD/openPMD-api/CMakeLists.txt;841;add_test;/home/axel/src/openPMD/openPMD-api/CMakeLists.txt;0;")
subdirs("share/openPMD/thirdParty/json")
subdirs("share/openPMD/thirdParty/pybind11")
