
import threading
from pathlib import Path

import yt_dlp

from kivy.app import App
from kivy.clock import Clock
from kivy.utils import platform
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class Downloader(App):

    def build(self):
        self.title = "YouTube Downloader"

        # На Android використовуємо приватну папку застосунку.
        if platform == "android":
            from android.storage import app_storage_path
            self.download_folder = (
                Path(app_storage_path()) / "downloads"
            )
        else:
            self.download_folder = (
                Path(__file__).resolve().parent / "downloads"
            )

        self.download_folder.mkdir(
            parents=True, exist_ok=True
        )

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=12
        )

        layout.add_widget(Label(
            text="YouTube Downloader",
            size_hint_y=0.25
        ))

        self.text_input = TextInput(
            hint_text="Paste YouTube URL here",
            multiline=False,
            size_hint_y=None,
            height=50
        )
        layout.add_widget(self.text_input)

        self.button = Button(
            text="Download",
            size_hint_y=None,
            height=50
        )
        self.button.bind(on_press=self.download)
        layout.add_widget(self.button)

        self.status = Label(
            text="Ready",
            halign="center",
            valign="middle"
        )
        self.status.bind(size=self.update_text_size)
        layout.add_widget(self.status)

        return layout

    def update_text_size(self, widget, size):
        widget.text_size = (size[0] - 20, None)

    def set_status(self, message):
        Clock.schedule_once(
            lambda dt: setattr(
                self.status, "text", message
            ), 0
        )

    def download(self, instance):
        url = self.text_input.text.strip()

        if not url.startswith(("https://", "http://")):
            self.status.text = "Enter a valid URL!"
            return

        self.button.disabled = True
        self.status.text = "Starting download..."

        threading.Thread(
            target=self.download_worker,
            args=(url,),
            daemon=True
        ).start()

    def download_worker(self, url):

        def progress_hook(data):
            if data["status"] == "downloading":
                total = (
                    data.get("total_bytes")
                    or data.get("total_bytes_estimate")
                )

                if total:
                    percent = (
                        data.get("downloaded_bytes", 0)
                        / total * 100
                    )
                    self.set_status(
                        f"Downloading: {percent:.1f}%"
                    )
                else:
                    self.set_status("Downloading...")

            elif data["status"] == "finished":
                self.set_status("Processing file...")

        options = {
            # Один файл, без об'єднання окремих доріжок.
            "format": "best[acodec!=none][vcodec!=none]/best",
            "outtmpl": str(
                self.download_folder / "%(title).100s.%(ext)s"
            ),
            "noplaylist": True,
            "progress_hooks": [progress_hook],
            "quiet": True,
            "no_warnings": True,
            "retries": 3,
            "socket_timeout": 30,
        }

        try:
            with yt_dlp.YoutubeDL(options) as downloader:
                downloader.download([url])

            self.set_status(
                "Download complete!\n"
                f"Saved to:\n{self.download_folder}"
            )

        except Exception as error:
            self.set_status(
                f"Download failed:\n{str(error)[:250]}"
            )

        finally:
            Clock.schedule_once(
                lambda dt: setattr(
                    self.button, "disabled", False
                ), 0
            )


if __name__ == "__main__":
    Downloader().run()
