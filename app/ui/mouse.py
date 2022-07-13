from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QGraphicsOpacityEffect
from PyQt6.QtCore import *
from PyQt6.QtGui import QFont
from BlurWindow.blurWindow import GlobalBlur
from .. import storage
from . import app


class Window(QWidget):
  def __init__(self):
    super(Window, self).__init__()
    conf = storage.setting['mouse']
    size = app.primaryScreen().size()

    self.setWindowTitle('Visualizer')
    self.setWindowFlags(
        Qt.WindowType.Tool |
        Qt.WindowType.X11BypassWindowManagerHint |
        Qt.WindowType.CustomizeWindowHint |
        Qt.WindowType.WindowStaysOnTopHint |
        Qt.WindowType.FramelessWindowHint
    )
    self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
    self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)
    self.setAttribute(Qt.WidgetAttribute.WA_NoChildEventsForParent, True)
    GlobalBlur(self.winId(), Dark=True, QWidget=self)


GUI = Window()
