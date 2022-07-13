from threading import Thread
from time import sleep
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QGraphicsOpacityEffect
from PyQt6.QtCore import *
from PyQt6.QtGui import QFont
from BlurWindow.blurWindow import GlobalBlur
from .. import storage
from ..feature import Store, Flag, constant as Co
from .utils import *
from . import app


class Window(QWidget):
  def __init__(self):
    super(Window, self).__init__()
    conf = storage.setting['keyboard']
    size = app.primaryScreen().size()

    self.setWindowTitle('Visualizer')
    GlobalBlur(self.winId(), QWidget=self)
    self.setContentsMargins(0, 0, 0, 0)
    self.setWindowFlags(
        Qt.WindowType.ToolTip |
        Qt.WindowType.X11BypassWindowManagerHint |
        Qt.WindowType.CustomizeWindowHint |
        Qt.WindowType.WindowStaysOnTopHint |
        Qt.WindowType.FramelessWindowHint
    )
    self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
    self.setAttribute(Qt.WidgetAttribute.WA_NoChildEventsForParent)
    self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

    self.setStyleSheet(
        'background-color: rgba(0, 0, 0, 0);'
        'padding: 0;'
        'margin: 0;'
    )
    self.content = QVBoxLayout(self)
    self.content.setContentsMargins(0, 0, 0, 0)

    label = QLabel(self)
    label.setWordWrap(False if conf['line'] == 1 else True)
    label.setAlignment(
        Qt.AlignmentFlag.AlignRight |
        Qt.AlignmentFlag.AlignVCenter
    )
    label.setFont(
        QFont(conf['font-family'], conf['font-size'], conf['font-weight'])
    )
    label.setStyleSheet(';'.join([
        f"background-color: {conf['background-color']}",
        f"color: {conf['color']}",
        f"border-radius: {conf['border-radius']}",
        f"letter-spacing: {conf['letter-spacing'] - 5}px",
        f"padding: {0 if conf['line'] == 1 else 12} 12",
        f"margin: 0",
    ]))
    conf['padding'] = 12
    conf['height'] = label.height() + int(label.height() * 1.1) * \
        conf['line'] + conf['padding'] * 3
    label.setFixedHeight(
        int(label.height() * 1.1) *
        conf['line'] + conf['padding'] * 2
    )
    self.setFixedSize(conf['width'], conf['height'])
    self.move(*get_pos_by_config(conf, size))
    self.content.addWidget(label)
    self.content.label = label

    toolbar = QHBoxLayout()
    toolbar.setContentsMargins(0, 0, 0, 0)

    def set_item_style(items=[]):
      for i in items:
        i.setFont(
            QFont(conf['font-family'], int(conf
                  ['font-size'] * 0.8), conf['font-weight'])
        )
        i.setAlignment(Qt.AlignmentFlag.AlignCenter |
                       Qt.AlignmentFlag.AlignVCenter)
        i.effects = QGraphicsOpacityEffect(i)
        i.effects.setOpacity(0.6)
        i.setGraphicsEffect(i.effects)
        i.setStyleSheet(
            f'color: {conf["color"]};'
            f'background-color: {conf["background-color"]};'
            f'border-radius: {conf["border-radius"]};'
            f'padding: {0};'
            f'margin: {0};'
        )

    toolbar.items = {}
    toolbar.items[Co.Ctrl] = QLabel(Co.Ctrl)
    toolbar.items[Co.Cmd] = QLabel(Co.Cmd)
    toolbar.items[Co.Shift] = QLabel(Co.Shift)
    toolbar.items[Co.Alt] = QLabel(Co.Alt)
    set_item_style([
        toolbar.items[Co.Ctrl],
        toolbar.items[Co.Cmd],
        toolbar.items[Co.Shift],
        toolbar.items[Co.Alt],
    ])
    toolbar.addWidget(toolbar.items[Co.Ctrl])
    toolbar.addWidget(toolbar.items[Co.Cmd])
    toolbar.addWidget(toolbar.items[Co.Alt])
    toolbar.addWidget(toolbar.items[Co.Shift])
    self.content.addLayout(toolbar)
    self.content.toolbar = toolbar


GUI = Window()


def render_label():
  GUI.content.label.setText(' '.join(
      [*[' '.join(i) if len(i) > 1 else i for i in Store.label],
       ' ']
  ))
  Flag.time_count = 0
  if not Flag.clear_running:
    Flag.clear_running = True
    Thread(target=clear).start()


def render_toolbar():
  for hotkey in [Co.Ctrl, Co.Cmd, Co.Shift, Co.Alt]:
    i = GUI.content.toolbar.items[hotkey]
    if hotkey in Store.toolbar:
      i.effects.setOpacity(1)
    else:
      i.effects.setOpacity(0.6)
    i.setGraphicsEffect(i.effects)


def clear():
  timeout = storage.setting['settings']['timeout'] if storage.setting['settings']['timeout'] != 'inf' else 1.2345
  while Flag.time_count < timeout:
    sleep(0.1)
    Flag.time_count += 0.1
    if int(Flag.time_count) == 1:
      Store.label.append('')
  if timeout != 1.2345:
    Store.label.clear()
    GUI.content.label.setText('')
  Flag.clear_running = False
