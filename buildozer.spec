[app]
title = YouTube Music Downloader
package.name = youtubemusicdownloader
package.domain = org.lirizin
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# Додали необхідні бібліотеки для коректної роботи yt-dlp та мережі в Android
requirements = python3,kivy,yt-dlp,certifi,urllib3,requests,idna,charset-normalizer

orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# Зменшуємо API до стабільного 33, щоб уникнути помилок компіляції в GitHub Actions
android.api = 33
android.minapi = 24
android.archs = arm64-v8a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 0
