import keyboard
from lib import mouse
from . import ui
from .feature import Store, constant as Co
from .utils import remap_character


def start():
  @keyboard.hook
  def __keyboard_callback__(event):
    ch = remap_character(event.name)
    if event.event_type == 'down':
      length = len(Store.toolbar)
      if length > 0:
        i = [i for i in Store.toolbar if i not in Store.label]
        Store.label.append(''.join(i) + ch)
      else:
        Store.label.append(ch)
      ui.keyboard.render_label()
      if ch in [Co.Ctrl, Co.Cmd, Co.Shift, Co.Alt]:
        ch not in Store.toolbar and Store.toolbar.append(ch)
        ui.keyboard.render_toolbar()
      else:
        if length > 0:
          Store.label.clear()
    elif event.event_type == 'up':
      if ch in [Co.Ctrl, Co.Cmd, Co.Shift, Co.Alt]:
        if ch in Store.toolbar:
          Store.toolbar.remove(ch)
          ui.keyboard.render_toolbar()

  # @mouse.hook
  # def __mouse_callback__(event):
  #   pass
