import sys

input = sys.argv[1]

list = [int(x) for x in input.split(' ')]

output = "".join(chr(x) for x in list)
print()
print(output)
