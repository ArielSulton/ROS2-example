# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_pkg_yaml_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED pkg_yaml_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(pkg_yaml_FOUND FALSE)
  elseif(NOT pkg_yaml_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(pkg_yaml_FOUND FALSE)
  endif()
  return()
endif()
set(_pkg_yaml_CONFIG_INCLUDED TRUE)

# output package information
if(NOT pkg_yaml_FIND_QUIETLY)
  message(STATUS "Found pkg_yaml: 0.0.0 (${pkg_yaml_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'pkg_yaml' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${pkg_yaml_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(pkg_yaml_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${pkg_yaml_DIR}/${_extra}")
endforeach()
