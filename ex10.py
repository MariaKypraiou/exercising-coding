#Χρησιμοποιώ την βιβλιοθήκη urllib.
import urllib.request


# Ο χρήστης εισάγει μια html ιστοσελίδα.
x = input('Εισάγεται μια ιστοσελίδα HTML: ')
htmlcode = urllib.request.urlopen('https://'+x)
lines=htmlcode.read()

atag = 0
ptag = 0
brtag = 0


#Ανάζτηση και μέτρημα των ετικετών <a , <p , br>.
for line in lines:
	print (line.split(" "))
	a = line.count("<a")
	p = line.count("<p")
	br = line.count("br>")

	atag = a + atag
	ptag = p + ptag
	brtag = br + brtag



print ("Ο αριθμός των <a> είναι:", atag)

print ("Ο αριθμός των <p> είναι:", ptag)

print ("Ο αριθμός των <br> είναι:", brtag)









