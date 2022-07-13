from .feature.constant import *


def single_instance():
  import psutil
  import os
  from .storage import process, save
  try:
    p = psutil.Process(process['pid'])
    p.terminate()
  except Exception:
    pass
  process['pid'] = os.getpid()
  save()


def remap_character(name=''):
  if name == 'left':
    return Left
  elif name == 'right':
    return Right
  elif name == 'down':
    return Down
  elif name == 'up':
    return Up
  elif name == 'page up':
    return PageUp
  elif name in ['page down', 'pgdn']:
    return PageDown
  elif name == 'delete':
    return Delete
  elif name == 'insert':
    return Insert
  elif name == 'print screen':
    return Print
  elif name == 'home':
    return Home
  elif name == 'end':
    return End
  elif name == 'menu':
    return Menu
  elif name == 'escape' or name == 'esc':
    return Escape
  elif name == 'tab':
    return Tab
  elif name == 'backspace':
    return Backspace
  elif name == 'enter':
    return Enter
  elif name == 'space':
    return Space
  elif 'windows' in name or 'cmd' in name or 'command' in name:
    return Cmd
  elif 'shift' in name or name in ['skift']:
    return Shift
  elif 'alt' in name:
    return Alt
  elif 'ctrl' in name:
    return Ctrl
  elif 'caps' in name:
    return Caps
  elif len(name) > 1:
    return ''.join(list(map(lambda i: i.capitalize(), name.split(' '))))
  return name
