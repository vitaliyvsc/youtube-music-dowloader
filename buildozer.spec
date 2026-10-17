[app]
# (str) Title of your application
title = YTDLP Kivy Downloader

# (str) Package name
package.name = ytdlp_downloader

# (str) Package domain (reverse domain)
package.domain = org.example

# (str) Source dir (default '.')
source.dir = .

# (list) Source include patterns
source.include_exts = py,png,jpg,kv,atlas,txt

# (str) Application entry point. For single-file layout this is main.py
entrypoint = main.py

# (str) Application versioning (keep semantic)
version = 0.1

# (list) Permissions
android.permissions = INTERNET

# (str) Supported orientation
orientation = portrait

# (str) Kivy requirements. Add any other packages your app needs.
# Note: Use the pip package names. 'pyopenssl' is used instead of 'openssl'.
requirements = python3, kivy, yt-dlp, certifi, urllib3, idna, charset-normalizer, requests, pyopenssl

# (str) Minimum Android API your app will support
android.api = 31
android.minapi = 24

# (bool) Accept SDK license automatically
android.accept_sdk_license = True

# Android SDK/NDK paths preconfigured for CI environment
# These are used by buildozer when provided and override environment vars.
android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/27.3.13750724

# (str) Android architectures to build for (separate by comma)
# Common choices: armeabi-v7a, arm64-v8a
android.archs = armeabi-v7a, arm64-v8a

# (int) Full debug logging
log_level = 2

# (bool) Copy the whole project dir into the .buildozer dir (safer)
copy_source = True

# (str) Application icon (optional) -- keep default Kivy icon if not provided
# icon.filename = %(source.dir)s/data/icon.png

# (str) Presplash image (optional)
# presplash.filename = %(source.dir)s/data/presplash.png

# (list) List of hostpython modules to include in the build (if needed)
# (uncomment to try to include particular modules that sometimes get missed)
# android.add_src =

# (str) The Android entrypoint and packaging settings are managed by python-for-android
# Additional p4a options can be set with android.p4a_... as needed