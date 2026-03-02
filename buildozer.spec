[app]
# (str) Title of your application
title = ABDO DEMON V33

# (str) Package name
package.name = abdo_demon

# (str) Package domain (needed for android packaging)
package.domain = org.demon

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 3.3

# (list) Application requirements
# تأكد من كتابة هذه المكتبات بدقة ليعمل العربي والأيقونات
requirements = python3, kivy==2.3.0, kivymd==1.2.0, arabic_reshaper, python-bidi, pillow

# (str) Presplash of the application
presplash.filename = splash.png

# (str) Icon of the application
icon.filename = icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) If True, then skip trying to update the Android sdk
android.skip_update = False

# (bool) If True, then automatically accept SDK license
android.accept_sdk_license = True

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = NO, 1 = YES)
warn_on_root = 1
