"""This program opens the learning_python.txt file and reads its contents."""

filename = 'learning_python.txt'

print("Read the contents of the file:")
with open(filename) as f:
    contents = f.read()
print(contents)

print("\nLoop over each of the lines in the file:")
with open(filename) as f:
    for line in f:
        print(line.rstrip())

print("\nStore the lines in a list:")
with open(filename) as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip())