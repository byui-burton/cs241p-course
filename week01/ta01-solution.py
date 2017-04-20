# Team Activity 01
# Author: Br. Burton


# Part 1: Ask the user for their DNA sequence, count the number of A's
dna = input("Please enter your DNA sequence: ")

# This will keep track of our matches
match_count = 0

# Go through the string letter by letter, and count the matches
for letter in dna:
    if letter == 'A':
        match_count += 1

# Output the results:
print("The sequence {} has {} A's.".format(dna, match_count))

# Blank line. Just for fun...
print()

# Part 2/3: Ask for a second person's sequence, and compare them:
dna_friend = input("Please enter your friend's DNA sequence: ")

# set the match count to be 0
match_count = 0

# For part 2, we assume each sequence is 10 characters, and could use this:
#length = 10

# For part 3, we use the smaller of the two:
length = 0
if len(dna) < len(dna_friend):
    length = len(dna)
else:
    length = len(dna_friend)

# Go through that many letters and count the matches
for i in range(length):
    if dna[i] == dna_friend[i]:
        match_count += 1

# Display the results:
match_percent = match_count / length * 100
print("You and your friend had {} matches for {}%".format(match_count, match_percent))