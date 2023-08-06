import wx
import sys
from types import SimpleNamespace

from .config import Config
from .download import WorkerThread


class AppGui(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(640, 480))
        self.config = Config()
        self.worker = None

        app_panel = wx.Panel(self)
        main_box = wx.BoxSizer(wx.VERTICAL)

        # settings
        settings_box = wx.StaticBoxSizer(wx.VERTICAL, app_panel, "Settings")

        # path picker
        path_box = wx.BoxSizer(wx.HORIZONTAL)
        label = wx.StaticText(settings_box.GetStaticBox(), label="Game path: ")
        self.dir_picker = wx.DirPickerCtrl(settings_box.GetStaticBox(), path=self.config.path)
        path_box.Add(label, 0, wx.ALL | wx.ALIGN_CENTER, 2)
        path_box.Add(self.dir_picker, 1, wx.ALL | wx.EXPAND, 2)

        # count picker
        count_box = wx.BoxSizer(wx.HORIZONTAL)
        label = wx.StaticText(settings_box.GetStaticBox(), label="Song count: ")
        self.count_picker = wx.SpinCtrl(settings_box.GetStaticBox(), style=wx.ALIGN_RIGHT, min=1, max=1000,
                                        initial=self.config.count)
        count_box.Add(label, 0, wx.ALL | wx.ALIGN_CENTER, 2)
        count_box.Add(self.count_picker, 1, wx.ALL | wx.EXPAND, 2)

        settings_box.Add(path_box, 0, wx.ALL | wx.EXPAND, 2)
        settings_box.Add(count_box, 0, wx.ALL | wx.EXPAND, 2)

        # progress
        progress_box = wx.StaticBoxSizer(wx.VERTICAL, app_panel, "Progress")
        self.progress = wx.Gauge(progress_box.GetStaticBox(), style=wx.GA_SMOOTH)

        # text & start button
        text_box = wx.BoxSizer(wx.HORIZONTAL)
        self.progress_label = wx.StaticText(progress_box.GetStaticBox(), label="Waiting for start")
        self.start_button = wx.Button(progress_box.GetStaticBox(), label="Start")
        text_box.Add(self.progress_label, 1, wx.ALL | wx.EXPAND, 2)
        text_box.Add(self.start_button, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 2)

        progress_box.Add(self.progress, 0, wx.ALL | wx.EXPAND, 2)
        progress_box.Add(text_box, 0, wx.ALL | wx.EXPAND, 2)

        # log
        log_box = wx.StaticBoxSizer(wx.VERTICAL, app_panel, "Log")
        self.log_text = wx.TextCtrl(log_box.GetStaticBox(), style=wx.TE_MULTILINE | wx.TE_READONLY)
        log_box.Add(self.log_text, 1, wx.ALL | wx.EXPAND, 0)

        # main panel
        main_box.Add(settings_box, 0, wx.ALL | wx.EXPAND, 2)
        main_box.Add(progress_box, 0, wx.ALL | wx.EXPAND, 2)
        main_box.Add(log_box, 1, wx.ALL | wx.EXPAND, 2)
        app_panel.SetSizer(main_box)

        # bindings
        self.Bind(wx.EVT_CLOSE, self.on_close)
        self.dir_picker.Bind(wx.EVT_DIRPICKER_CHANGED, self.on_path)
        self.count_picker.Bind(wx.EVT_SPINCTRL, self.on_count)
        self.start_button.Bind(wx.EVT_BUTTON, self.on_start)

        # redirect stdout to logging
        log_class = SimpleNamespace()
        log_class.write = lambda value: wx.CallAfter(lambda: self.log_text.write(value))
        sys.stdout = log_class

        self.Show(True)

    def on_close(self, event):
        if self.worker is not None:
            self.worker.stop()
            self.worker.join()

        self.dir_picker.Destroy()
        sys.stdout = sys.__stdout__
        self.Destroy()

    def on_start(self, event):
        if self.worker is not None and self.worker.working:
            self.worker.stop()
            self.worker.join()
            self.start_button.SetLabel("Start")
        else:
            self.worker = WorkerThread(self, self.config)
            self.start_button.SetLabel("Stop")
            self.log_text.Clear()
            self.worker.start()

    def on_done(self):
        self.start_button.SetLabel("Start")

    def on_path(self, event):
        self.config.path = event.GetPath()
        self.config.save()

    def on_count(self, event):
        self.config.count = event.GetPosition()
        self.config.save()

    def set_progress(self, value: int) -> None:
        wx.CallAfter(lambda: self.progress.SetValue(value))

    def set_label(self, value: str) -> None:
        def _set_label():
            self.progress_label.SetLabel(value)
            self.log_text.AppendText(value + "\n")
        wx.CallAfter(_set_label)


class GuiIter:
    def __init__(self, collection, gui):
        self.size = len(collection)
        self.pos = 0
        self.gui = gui
        self.iter = iter(collection)

    def __iter__(self):
        return self

    def __next__(self):
        self.gui.set_progress(int(self.pos / self.size * 100.0))
        self.pos += 1
        return next(self.iter)
