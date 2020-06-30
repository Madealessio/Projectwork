anni= 0
print("inserisci la tua età ")
anni = input()


if (anni <= 26):
	if (anni <= 18) :
		print("non può votare")
	
	else :
		print("può votare solo alla camera")
	
else :
	print("può votare alla camera e al senato")
