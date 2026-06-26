[app]

title = My Application
package.name = myapp
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

requirements = python3==3.10.0,kivy==2.3.0

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 24
android.ndk = 23b
android.ndk_api = 21
android.sdk = 20
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# Если у вас есть иконка и заставка, раскомментируйте эти строки
# и поместите файлы в папку data/
# icon.filename = %(source.dir)s/data/icon.png
# presplash.filename = %(source.dir)s/data/presplash.png

[buildozer]

log_level = 2
warn_on_root = 1
