from re import sub

from .helper import interruptible

__all__ = [
    'App',
]


class App:
    def __init__(self):
        pass

    def run(self):
        while True:
            cmd = sub(r'\s+', input('> ').strip(), ' ')
            if cmd in {'exit', 'quit'}:
                return
            else:
                pass
