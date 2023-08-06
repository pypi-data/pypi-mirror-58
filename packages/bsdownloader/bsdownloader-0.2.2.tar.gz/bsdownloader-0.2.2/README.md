# Beat Saber - Downloader

Allows you to download songs, which gives most <abbr title="Performance Points">PP</abbr>. And creates playlist with that songs, sorted by given PP.

<p align="center">
  <img src="https://raw.githubusercontent.com/Norne9/beatsaber-downloader/master/etc/screenshot.png" align="center" />
</p>

[![PyPI version](https://badge.fury.io/py/bsdownloader.svg)](https://badge.fury.io/py/bsdownloader)

## How to use on Windows

Download program from [Releases](https://github.com/Norne9/beatsaber-downloader/releases/latest) page, unpack and run it.

Select your game folder and enter how many songs you want to download. Press *Start* and wait until program write *Done!*.

Songs will be automatically downloaded from [BeatSaver](https://beatsaver.com/) and unpacked to CustomLevels folder.

## Install from PyPI (for all other systems)

You need Python 3.7 or later

Install app from PyPI:

```console
pip install bsdownloader
```

And run it by command `bsdownloader` or `bs-downloader`

## How to build from source

You can build standalone app using PyInstaller. Install PyInstaller first:

```console
pip install pyinstaller
```

Install dependencies:

```console
pip install -r requirements.txt
```

Build app:

```console
pyinstaller --window --onefile --name bs-downloader ./start.py
```

Executable file will be in *dist* folder.
