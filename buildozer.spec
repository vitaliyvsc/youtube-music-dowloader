
name: Build Android APK

on:
  workflow_dispatch:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Download project
        uses: actions/checkout@v4

      - name: Build APK
        uses: ArtemSBulgakov/buildozer-action@v1
        with:
          command: buildozer -v android debug

      - name: Save APK
        uses: actions/upload-artifact@v4
        with:
          name: youtube-downloader-apk
          path: bin/*.apk
          if-no-files-found: error
