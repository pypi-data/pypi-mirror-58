from os.path import join, dirname

with open(join(dirname(dirname(__file__)), 'VERSION')) as version_file:
    __version__ = version_file.read().strip()

