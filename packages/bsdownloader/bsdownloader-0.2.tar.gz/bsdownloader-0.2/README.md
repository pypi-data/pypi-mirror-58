# Beat Saber - Downloader

Allows you to download songs, which gives most <abbr title="Performance Points">PP</abbr>. And creates playlist with that songs, sorted by given PP.

<p align="center">
  <img src="https://raw.githubusercontent.com/Norne9/beatsaber-downloader/master/etc/screenshot.png" align="center" />
</p>

## How to use

Download program from [Releases](https://github.com/Norne9/beatsaber-downloader/releases/latest) page and run it.

Select your game folder and enter how many songs you want to download. Press *Start* and wait until program write *Done!*.

Songs will be automatically downloaded from [BeatSaver](https://beatsaver.com/) and unpacked to CustomLevels folder. Will be created new playlist named "Top PP songs" with songs sorted by PP.

## How to start from source

Program made in Python 3.7.

You need to install requirements:

```console
pip install -r requirements.txt
```

And than you can run program like that:

```console
python -m bsdownloader
```

## How to build

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
