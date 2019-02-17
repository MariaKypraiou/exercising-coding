#Creating an array for the english alphabet.
LetterFrequencyArray = [0 for i in range(26)]

fin = open("file1.txt", "r")
for line in fin:
    line = str(line)
    line = line.upper()
    for char in line:
        if char >= 'A' and char <= 'Z':
            index = ord(char) - ord('A')
            LetterFrequencyArray[index] += 1
fin.close()

print("Πίνακας Συχνοτήτων για αρχείο file1.txt:")
print(LetterFrequencyArray)

#Finding the most and the least shown letter and replacing them.
least_index = 0
most_index = 0
least_times = LetterFrequencyArray[0]
most_times = LetterFrequencyArray[0]

for i in range(len(LetterFrequencyArray)):
    if LetterFrequencyArray[i] > most_times:
        most_times = LetterFrequencyArray[i]
        most_index = i
    elif LetterFrequencyArray[i] < least_times:
        least_times = LetterFrequencyArray[i]
        least_index = i

least_char = chr(ord('A')+ least_index)
most_char = chr(ord('A') + most_index)

print("Χαρακτήρας που εμφανίζεται περισσότερο:")
print(most_char)
print("Χαρακτήρας που εμφανίζεται λιγότερο:")
print(least_char)

fin = open("file1.txt", "r")
fout = open("file2.txt", "w")

print("Εγγραφή στο αρχείο file2.txt....")
for line in fin:
    line = str(line)
    line_out = line.upper()

    #It's impossible in a text with capital characters to find an 'a'.
    line_out = line_out.replace(most_char, 'a')
    line_out = line_out.replace(least_char, most_char)
    line_out = line_out.replace('a', least_char)
    fout.write(line_out)

fin.close()
fout.close()

print("Τέλος εγγραφής!")
