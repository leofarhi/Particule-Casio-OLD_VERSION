# Configure with [fxsdk build-fx] or [fxsdk build-cg], which provide the
# toolchain file and module path of the fxSDK

cmake_minimum_required(VERSION 3.15)
project(MyAddin)

include(GenerateG1A)
include(GenerateG3A)
include(Fxconv)
find_package(Gint 2.1 REQUIRED)

set(SOURCES
  src/main.cpp
  src/ParticuleEngine.hpp
  src/ParticuleEngine.cpp
  src/List.h
  src/Announcement.h
  src/Ressources.h
  src/ParticuleGraphics.cpp
  src/ParticuleGraphics.hpp
  src/ParticuleBase.cpp
  src/ParticuleBase.hpp
  src/ParticuleGintPatch.cpp
  src/ParticuleGintPatch.hpp
  # ...
)
# Shared assets, fx-9860G-only assets and fx-CG-50-only assets
set(ASSETS
  # ...
)
set(ASSETS_fx
  assets-fx/font.png
  # ...
)
set(ASSETS_cg
  assets-cg/font.png
  # ...
)

fxconv_declare_assets(${ASSETS} ${ASSETS_fx} ${ASSETS_cg} WITH_METADATA)

add_executable(myaddin ${SOURCES} ${ASSETS} ${ASSETS_${FXSDK_PLATFORM}})
target_compile_options(myaddin PRIVATE -Wall -Wextra -Os)
target_link_libraries(myaddin Gint::Gint "${CMAKE_CURRENT_SOURCE_DIR}/libsupc++.a")

if("${FXSDK_PLATFORM_LONG}" STREQUAL fx9860G)
  generate_g1a(TARGET myaddin OUTPUT "MyAddin.g1a"
    NAME "MyAddin" ICON assets-fx/icon.png)
elseif("${FXSDK_PLATFORM_LONG}" STREQUAL fxCG50)
  generate_g3a(TARGET myaddin OUTPUT "MyAddin.g3a"
    NAME "MyAddin" ICONS assets-cg/icon-uns.png assets-cg/icon-sel.png)
endif()
