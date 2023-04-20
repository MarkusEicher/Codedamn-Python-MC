from collections import deque

clubs = deque(("ZSC Lions", "SC Bern", "HC Lugano", "EV Zug"))
print (f"Original set of Clubs: {clubs}\n")
clubs.append("HC Ambri-Piotta")
print (f"Used append to add to the end of the list {clubs}\n")
# clubs.appendleft("HC Ambri-Piotta")
# print (f"Used appendleft to add to the start of the list {clubs}\n")

# clubs2 = clubs.append("HC Ambri-Piotta")
# print (f"{clubs2}\n")
# clubs3 = clubs.appendleft("HC Ambri-Piotta")
# print (f"{clubs3}\n")

firstClub = clubs[0] # Sliced out the first element, deque remains the same
print (firstClub)
print (f"{clubs}\n")

secondClub = clubs.popleft() # pops the first element, deque changes
print (secondClub)
print (f"{clubs}\n")