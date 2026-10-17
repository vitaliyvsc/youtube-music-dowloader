[app]
title = YouTube Downloader
package.name = youtubedownloader
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.include_dirs = 
source.exclude_exts = spec
source.exclude_dirs = tests, bin, venv
version = 0.1
requirements = python3,kivy,yt-dlp,certifi,urllib3,idna,charset-normalizer==3.3.2,requests,openssl
android.permissions = INTERNET
android.minapi = 24
android.api = 33
android.orientation = portrait
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1

# Використовуємо вже встановлені на серверові GitHub SDK та NDK
android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/27.3.13750724
