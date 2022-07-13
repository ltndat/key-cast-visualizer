import importlib
import sys
import os
from threading import Thread
from PyQt6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PyQt6.QtGui import QIcon, QAction
from .. import storage

app = QApplication(sys.argv)
Tray = QSystemTrayIcon(QIcon('assets/icon.ico'), app)
keyboard = importlib.import_module('app.ui.keyboard')
mouse = importlib.import_module('app.ui.mouse')


class GUI():
  keyboard = keyboard.GUI
  mouse = mouse.GUI


def start():
  def exit():
    app.exit()

  def open_setting():
    Thread(target=os.system, args=(os.path.join(
        os.getcwd(), 'storage', 'setting.json'),)).start()

  Tray.setToolTip(
      f'{storage.name.capitalize()} make your desktop look good\nv{storage.version}'
  )
  menu = QMenu()
  a1 = QAction("Setting")
  a2 = QAction("Exit")
  menu.addActions([a1, a2])
  a1.triggered.connect(open_setting)
  a2.triggered.connect(exit)
  Tray.setContextMenu(menu)

  Tray.show()
  GUI.keyboard.show()
  app.exec()
