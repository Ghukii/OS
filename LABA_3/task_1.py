import sys
import select

def key():
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

def stop():
    print("Программа была прервана")
    sys.exit(0)

exit_key = "e"

while True:
    if key():
        char = sys.stdin.read(1)
        if char == exit_key:
            stop()
