__all__ = [
    'interruptible',
    'error',
]


def interruptible(func):
    def result(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyboardInterrupt:
            error('Keyboard Interruption')


def error(msg):
    print(f'\x1b[91m{msg}\x1b[0m')
