lista = [1,58,548,7,56,16,296,747]

def merge(v, esq, meio, direita):
	i =	esq
	j =	meio + 1
	for	k in range(esq,direita+1):
		aux[k] = v[k]
		for	k in range(esq,direita+1):
			if i > meio:
				v[k] = aux[j]
				j+=1
			elif j > direita:
				v[k] = aux[i]
				i+=1
			elif aux[i]	> aux[j]:
				v[k] = aux[j]
				j+=1
			else:
				v[k] = aux[i]
				i+=1

def TD_mergesort(v,	esq,	direita):
	if esq >= direita:
		meio = (esq + direita)//2
		TD_mergesort(v,esq,meio)
		TD_mergesort(v,meio+1,direita)
		merge(v,esq,meio,direita)

def mergesort(v,N):
	global	aux
	aux = list(v)
	TD_mergesort(v,0,N-1)
	del aux

	return v

print(mergesort(lista,len(lista)))