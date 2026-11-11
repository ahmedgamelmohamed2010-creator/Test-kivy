[app]

title = Kivy APK Test
package.name = kivyapktest
package.domain = org.example

source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,json,txt
version = 1.0.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.archs = arm64-v8a
android.minapi = 24
android.accept_sdk_license = True

[buildozer]

log_level = 2
warn_on_root = 1
