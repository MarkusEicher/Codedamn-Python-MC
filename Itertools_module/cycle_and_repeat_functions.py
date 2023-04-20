from itertools import cycle

instructions = ("eat", "code", "sleep")
counter = 0
for instruction in cycle(instructions):

    print(instruction)
    counter += 1
    if counter == 10: 
        break

from itertools import repeat

for msg in repeat("Keep patience", times=5): # Takes the times argument to set number of repetitions
    print(msg)