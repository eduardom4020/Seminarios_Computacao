import sys

input = sys.argv[1]

output = " ".join(str(ord(x)) for x in input)

print()
print(output)
