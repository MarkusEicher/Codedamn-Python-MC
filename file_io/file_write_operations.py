# This will overwrite the file with the given content
with open ("test copy.txt", "w") as file:
    file.write("Hello World\n")

lines = [
    "This is line 1 of the sample text.\n", 
    "Another line of text. \n",
    "Now this is line 3 of the sample text."
]

with open ("test copy.txt", "w") as file:
    file.writelines(lines)