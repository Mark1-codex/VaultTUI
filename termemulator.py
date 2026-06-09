import os
import pty
import sys
import select
import termios
import tty
import signal
import fcntl
import struct

print("Terminal\nHINT: Press Ctrl+Q to exit")
def run_terminal():
    if not sys.stdin.isatty():
        print("ERROR: Must be run from a real terminal.")
        return
    old_tty = termios.tcgetattr(sys.stdin)
    pid, fd = pty.fork()

    if pid == 0:
        os.execvp("bash", ["bash", "-l"])
    else:
        def sigwinch_handler(sig, frame):
            dims = struct.unpack('HHHH', fcntl.ioctl(sys.stdin.fileno(), termios.TIOCGWINSZ, '\0' * 8))
            fcntl.ioctl(fd, termios.TIOCSWINSZ, struct.pack('HHHH', *dims))

        signal.signal(signal.SIGWINCH, sigwinch_handler)
        sigwinch_handler(None, None)  # Set initial size

        try:
            tty.setraw(sys.stdin.fileno())
            while True:
                r, _, _ = select.select([sys.stdin, fd], [], [])
                if sys.stdin in r:
                    data = os.read(sys.stdin.fileno(), 1024)
                    # Exit trigger: Ctrl+Q (ASCII 17)
                    if data == b'\x11':
                        break
                    os.write(fd, data)
                if fd in r:
                    data = os.read(fd, 1024)
                    if not data: break
                    os.write(sys.stdout.fileno(), data)
        finally:
            # Restore settings and ensure child is dead
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_tty)
            os.kill(pid, signal.SIGTERM)
            sys.exit(0)


if __name__ == "__main__":
    run_terminal()