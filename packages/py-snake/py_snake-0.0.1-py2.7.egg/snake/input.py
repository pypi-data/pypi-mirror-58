from threading import Thread

from pynput.keyboard import Key, Listener

from .kbhit import KBHit

__all__ = ['DefaultKeyReader', 'NTKeyReader']


class _KeyReader:
    def capture(self):
        raise NotImplemented

    def last_key(self):
        raise NotImplemented


class DefaultKeyReader(_KeyReader):
    def __init__(self):
        self._kb = KBHit()
        self._last_key = None
        self._tmp = None

    def capture(self):
        self._tmp = None
        if self._kb.kbhit():
            self._last_key = self._kb.getch()

    def last_key(self):
        if self._tmp:
            return self._tmp
        self._tmp = self._last_key
        self._last_key = None
        return self._tmp


class NTKeyReader(_KeyReader):
    def __init__(self):
        self._last_key = None

        def target():
            def on_press(key):
                self._last_key = key

            with Listener(on_press=on_press) as listener:
                listener.join()

        t = Thread(target=target)
        t.start()

    def capture(self):
        pass

    def last_key(self):
        key = self._last_key
        if isinstance(key, Key):
            return key.name
        return key


if __name__ == '__main__':
    import time
    k = DefaultKeyReader()

    while True:
        now = time.time()

        while time.time() - now < 1:
            k.capture()

        print(k.last_key())
