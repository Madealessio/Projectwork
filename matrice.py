Matrice = [[], [], [], []]
Mat = [[], [], [], []]

for i in range(4):
	for j in range(4):
		Matrice[i].append(j+(i*3))
	#riempimento matrice
	
for i in range(4):
	for j in range(4):
		Mat[-i].append(j+(i*3))
	#riempimento matrice

print(f'Matrice: {Matrice}')
print(f'Mat: {Mat}')

cont=0
for i in range(4):
	for j in range(4):
		if Mat[i][j]==Matrice[i][j]:
			cont=cont+1

print(f'ci sono {cont} elementi uguali che corrispondono')
