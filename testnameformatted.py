print ("\nEnter as many names as you want in 1 single line")
NameInput=input("Eg SIDDHARTH ARUN VENKATACHALAM SUBRAMANIAM: \n ")
NameSplit=NameInput.split(" ")
print(len(NameSplit))
NameLen=len(NameSplit)-1

print("\nthe number of names you have input is:" ,len(NameSplit),"\n")

for i in range(NameLen,-1,-1):
	print(NameSplit[i], end=" ")
