[app]
title = YouTube Downloader
package.name = youtubedownloader
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,yt-dlp,certifi,urllib3,idna,charset-normalizer==3.3.2,requests,openssl
android.permissions = INTERNET
android.minapi = 24
android.orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 1
