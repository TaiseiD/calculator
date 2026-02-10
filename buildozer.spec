[app]
title = Calculator
package.name = calculator
package.domain = org.test

source.dir = .
source.include_exts = py,kv,png,jpg,atlas

version = 0.1

# Entry point
entrypoint = main.py

# Core requirements ONLY
requirements = python3,kivy

# Orientation & UI
orientation = portrait
fullscreen = 1

# Permissions (only if needed)
android.permissions = INTERNET

# Android configuration (stable)
android.api = 31
android.minapi = 21

# IMPORTANT: NDK version that is known-stable with python-for-android
android.ndk = 25b

android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True

# Prevent buildozer from guessing paths
android.sdk_path =
android.ndk_path =

# Logging
log_level = 2
