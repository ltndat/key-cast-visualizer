def force_new_file(path_file=''):
  from os import path, makedirs

  try:
    flag = path.dirname(path_file)
    if flag and not path.exists(flag):
      makedirs(path.dirname(path_file))
    open(path_file, 'x', encoding='utf-8')
  except Exception:
    pass


def force_open_file(file_name='', default_text='{}'):
  import json

  file = None
  try:
    file = open(f'storage/{file_name}', 'r', encoding='utf-8')
  except Exception:
    force_new_file(f'storage/{file_name}')
    open(f'storage/{file_name}', 'w', encoding='utf-8').write(default_text)
  if not file:
    file = open(f'storage/{file_name}', 'r', encoding='utf-8')
  return json.loads(file.read())
