bubble_lista = [15,18,4,5,14,1]
selection_lista = [15,18,4,5,14,1]
insertion_lista = [15,18,4,5,14,1]

def trocar(vetor,index1,index0):
	aux = vetor[index1]
	vetor[index1] = vetor[index0]
	vetor[index0] = aux

def bubblesort(vetor,vetor_size):
	for index1 in range(vetor_size-1,0,-1):
		for	index0 in range(0,index1):
			if vetor[index0] > vetor[index0+1]:
				trocar(vetor,index0,index0+1)

	return vetor

print('bubble sort: ',bubblesort(bubble_lista,len(bubble_lista)))

def selectionsort(vetor,vetor_size):
	for	index0 in range(0,vetor_size):
		menor = index0
		for	index1 in range(index0+1,vetor_size):
			if	vetor[menor] > vetor[index1]:
				menor = index1
			trocar(vetor,index0,menor)

	return vetor

print('Select Sort: ',selectionsort(selection_lista,len(selection_lista)))

def insertionsort(vetor,vetor_size):
	for	index0 in range(1,vetor_size):
		aux	= vetor[index0]
		index1 = index0 - 1
		while index1 >= 0 and vetor[index1] > aux:
			vetor[index1+1] = vetor[index1]
			index1 -= 1
			vetor[index1+1] = aux
	return vetor

print('insertionsort: ',insertionsort(insertion_lista,len(insertion_lista)))

# def shellsort(v,	N):
# 	h=1
# 	while h	< N//3:
# 		h =	3*h	+1
# 		while h	>= 1:
# 			for	i in range(h,N):
# 				j = i
# 				while j	>= h and v[j] < v[j-h]:
# 					trocar(v,j,j-h)
# 					j -= h
# 			h//=3
# 	return v

# print('--',shellsort(insertion_lista,len(insertion_lista)))