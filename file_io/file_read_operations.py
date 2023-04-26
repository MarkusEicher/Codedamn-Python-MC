file = open("test.txt")

contents = file.read()

print(contents)
file.close

# this option closes the file automatically
with open("test.txt") as file:
    contents = file.read()
    print(contents)

with open ("test.txt") as file:
    line1 = file.readline(4)
    file.seek(5)
    line2 = file.readline(2)

print(line1, end="\n")
print(line2)

with open("test.txt") as file:
    lines = file.readlines()

print(lines)   