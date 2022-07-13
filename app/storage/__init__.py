import json
from ..info import *
from .utils import *

setting = force_open_file('setting.json', json.dumps({
    "settings": {
        "timeout": 4
    },
    "keyboard": {
        "bottom": 12,
        "right": 8,
        "line": 1,
        "width": 180,
        "font-size": 24,
        "letter-spacing": 0,
        "font-family": "monospace",
        "font-weight": 500,
        "background-color": "rgba(0, 0, 0, 0.5)",
        "color": "#fff",
        "border-radius": 16
    },
    "mouse": {
        "top": 0,
        "bottom": 0,
        "left": 0,
        "right": 0,
        "line": 2,
        "width": 240,
        "font-size": 24,
        "font-family": "monospace",
        "font-weight": 400,
        "background-color": "rgba(0, 0, 0, 0.2)",
        "color": "#fff",
        "padding": 8,
        "border-radius": "16px"
    }
}))

process = force_open_file('process.json')


def save():
  #   open('storage/setting.json', 'w', encoding='utf-8').write(json.dumps(setting))
  open('storage/process.json', 'w', encoding='utf-8').write(json.dumps(process))
