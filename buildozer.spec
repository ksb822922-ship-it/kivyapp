[app]

title = My Application
package.name = myapp
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

requirements = python3,kivy

orientation = portrait
fullscreen = 0

# Исправленные настройки Android
android.api = 33
android.minapi = 21
android.ndk = 25c                      # ← ИСПРАВЛЕНО: теперь 25c вместо 23b
android.ndk_api = 24                   # ← добавлено (рекомендуется)
android.sdk = 33
android.archs = arm64-v8a              # одна архитектура для ускорения
android.allow_backup = True
android.accept_sdk_license = True

[buildozer]

log_level = 2
warn_on_root = 1
