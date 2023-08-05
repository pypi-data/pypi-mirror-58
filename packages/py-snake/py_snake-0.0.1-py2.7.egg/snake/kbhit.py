#!/usr/bin/env python
'''
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

'''

import os
import sys

# Windows
if os.name == 'nt':
    import msvcrt

# Posix (Linux, OS X)
else:
    import sys
    import termios
    import atexit
    from select import select


if sys.version_info.major == 2:
    utf8 = lambda s: s.decode('utf-8')
else:
    utf8 = lambda s: s


class KBHit:
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
            return utf8(msvcrt.getch())

        else:
            c = sys.stdin.read(1)
            if ord(utf8(c)) == 27:
                c2 = sys.stdin.read(1)
                if ord(utf8(c2)) == 91:
                    c3 = sys.stdin.read(1)
                    if ord(utf8(c3)) == 65:
                        return 'up'
                    if ord(utf8(c3)) == 66:
                        return 'down'
                    if ord(utf8(c3)) == 67:
                        return 'right'
                    if ord(utf8(c3)) == 68:
                        return 'left'
                    return ord(utf8(c3))
                return 'esc'
            elif ord(utf8(c)) == 10:
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

        return vals.index(ord(utf8(c)))

    def kbhit(self):
        ''' Returns True if keyboard character was hit, False otherwise.
        '''
        if os.name == 'nt':
            return msvcrt.kbhit()

        else:
            dr, dw, de = select([sys.stdin], [], [], 0)
            return dr != []


# Test
if __name__ == "__main__":

    kb = KBHit()
    while True:
        if kb.kbhit():
            c = kb.getch()
            if c == 'esc':
                break
            print(c)

    print("Done")
