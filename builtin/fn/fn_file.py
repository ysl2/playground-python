import pathlib

def _log(file, string):
    print(string)
    f.write(string + '\n')

file_path = pathlib.Path('/tmp/fn_file.txt')
with open(file_path, 'w') as f:
    _log(f, 'hello world')
    _log(f, 'love work')
