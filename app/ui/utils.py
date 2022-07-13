def get_pos_by_config(config=None, screen=None):
  if 'top' in config and 'left' in config:
    return (config['left'], config['top'])
  elif 'top' in config and 'right' in config:
    return (screen.width() - config['right'] - config['width'], config['top'])
  elif 'bottom' in config and 'left' in config:
    return (config['left'], screen.height() - config['bottom'] - config['height'])
  elif 'bottom' in config and 'right' in config:
    return (screen.width() - config['right'] - config['width'], screen.height() - config['bottom'] - config['height'])
