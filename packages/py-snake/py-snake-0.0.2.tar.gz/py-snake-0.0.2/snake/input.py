# -*- coding: utf-8 -*-

import os

# Windows
if os.name == 'nt':
    import msvcrt

# Posix (Linux, OS X)
else:
    import sys
    import termios
    import atexit
    from select import select

__all__ = ['DefaultKeyReader', 'ArrowKeyReader']


class _KeyReader:
    def capture(self):
        raise NotImplemented

    def last_key(self):
        raise NotImplemented


class DefaultKeyReader(_KeyReader):
    def __init__(self):
        self._kb = _KBHit()
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


class ArrowKeyReader(_KeyReader):
    def __init__(self):
        self._kb = _KBHit()
        self._last_key = None
        self._tmp = None

    def capture(self):
        self._tmp = None
        if self._kb.kbhit():
            key = self._kb.getarrow()
            if key != -1:
                self._last_key = ['up', 'right', 'down', 'left'][key]

    def last_key(self):
        if self._tmp:
            return self._tmp
        self._tmp = self._last_key
        self._last_key = None
        return self._tmp


class _KBHit:
    """
    A Python class implementing KBHIT, the standard keyboard-interrupt poller.
    Works transparently on Windows and Posix (Linux, Mac OS X).  Doesn't work
    with IDLE.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    """
    def __init__(self):
        if os.name != 'nt':

            # Save the terminal settings
            self.fd = sys.stdin.fileno()
            self.new_term = termios.tcgetattr(self.fd)
            self.old_term = termios.tcgetattr(self.fd)

            # New terminal setting unbuffered
            self.new_term[3] = (self.new_term[3] & ~termios.ICANON & ~termios.ECHO)
            termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.new_term)

            # Support normal-terminal reset at exit
            atexit.register(self.set_normal_term)

    def set_normal_term(self):
        ''' Resets to normal terminal.  On Windows this is a no-op.
        '''

        if os.name != 'nt':
            termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.old_term)

    def getch(self):
        ''' Returns a keyboard character after kbhit() has been called.
            Should not be called in the same program as getarrow().
        '''

        if os.name == 'nt':
            return msvcrt.getch()

        else:
            c = sys.stdin.read(1)
            if ord(c) == 27:
                c2 = sys.stdin.read(1)
                if ord(c2) == 91:
                    c3 = sys.stdin.read(1)
                    if ord(c3) == 65:
                        return 'up'
                    if ord(c3) == 66:
                        return 'down'
                    if ord(c3) == 67:
                        return 'right'
                    if ord(c3) == 68:
                        return 'left'
                    return ord(c3)
                return 'esc'
            elif ord(c) == 10:
                return 'enter'
            return c

    def getarrow(self):
        ''' Returns an arrow-key code after kbhit() has been called. Codes are
        0 : up
        1 : right
        2 : down
        3 : left
        Should not be called in the same program as getch().
        '''

        if os.name == 'nt':
            msvcrt.getch()  # skip 0xE0
            c = msvcrt.getch()
            vals = [72, 77, 80, 75]

        else:
            c = sys.stdin.read(3)[2]
            vals = [65, 67, 66, 68]

        code = ord(c)
        if code not in vals:
            return -1

        return vals.index(code)

    def kbhit(self):
        ''' Returns True if keyboard character was hit, False otherwise.
        '''
        if os.name == 'nt':
            return msvcrt.kbhit()

        else:
            dr, dw, de = select([sys.stdin], [], [], 0)
            return dr != []


if __name__ == '__main__':
    import time
    k = ArrowKeyReader()

    while True:
        now = time.time()

        while time.time() - now < 1:
            k.capture()

        print(k.last_key())
