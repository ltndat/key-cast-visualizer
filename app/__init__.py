from . import storage
from . import (
    backend,
    ui,
    utils
)


def run():
  utils.single_instance()
  backend.start()
  ui.start()
