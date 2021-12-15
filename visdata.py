import sys

f = open("man.txt", "r")

sys.stdout.write(repr(f.read()))