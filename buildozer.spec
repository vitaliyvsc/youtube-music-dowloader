[app]
title = YTDLP Kivy Downloader
package.name = ytdlp_downloader
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt
entrypoint = main.py
version = 0.1
android.permissions = INTERNET
orientation = portrait

requirements = python3,kivy,yt-dlp,certifi,urllib3,idna,charset-normalizer,requests,pyopenssl

android.api = 31
android.minapi = 24
android.accept_sdk_license = True
android.archs = armeabi-v7a, arm64-v8a
log_level = 2
copy_source = True

android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/27.3.13750724
