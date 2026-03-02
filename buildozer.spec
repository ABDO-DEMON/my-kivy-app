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

# (str) Application versioning
version = 0.1

# (list) Application requirements
# تأكد من إضافة المكتبات التي استخدمتها في الكود
requirements = python3,kivy==2.2.1,kivymd==1.1.1,arabic_reshaper,python-bidi

# (str) Custom source folders for requirements
# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
presplash.filename = splash.png

# (str) Icon of the application
icon.filename = icon.png

# (str) Supported orientations (landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto backup
android.allow_backup = True