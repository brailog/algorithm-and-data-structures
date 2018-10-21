class No:
	def __init__(self,chave=None,valor=None,esquerda=None,direita=None):
		self.chave = chave
		self.valor = valor
		self.esquerda =	esquerda
		self.direita =	direita

class Arv_binaria:
	def __init__(self):
		self.raiz = None

	def inserir(self,chave,valor):
		self.raiz = self.__inserir(self.raiz,chave,valor)

	def __inserir(self,nodo,chave,valor):
		if nodo is None:
			return No(chave,valor)
		if nodo.chave > chave:
			nodo.esquerda = self.__inserir(nodo.direita,chave,valor)
		elif nodo.chave < chave:
			nodo.direita = self.__inserir(nodo.esquerda,chave,valor)
		else:
			nodo.valor = valor
		return nodo

	def valor(self, chave):
		aux = self.raiz
		while not aux is None:
			if aux.chave == chave:
				return aux.valor
			elif aux.chave < chave:
				aux = aux.direita
			else:
				aux = aux.esquerda
		raise KeyError(chave)

	def remover(self,chave,valor):
		self.__remove(chave,valor,self.raiz)

	def __remove(self,chave,valor,nodo):
		if nodo	is None:
			raise KeyError(chave)
		elif nodo.chave < chave:
			nodo.direita,valor = self.__remove(chave,valor,nodo.direita)
		elif nodo.chave > chave:
			nodo.esquerda,valor = self.__remove(chave,valor,nodo.esquerda)
		else:
			valor =	nodo.valor
			if nodo.direita is None:
				aux = nodo
				nodo = nodo.esquerda
				del aux
			elif nodo.esquerda is None:
				aux = nodo
				nodo = nodo.direita
				del aux
			else:
				nodo.esquerda = self.__antecessor(nodo,nodo.esquerda)
		return nodo,valor

	def __antecessor(self,q,r):
		if not r.direita is None:
			r.direita =	self.__antecessor(q,r.direita)
		else:
			q.valor = r.valor
			aux = r
			r =	r.esquerda
			del aux
		return r

	def em_ordem(self,p):
		if not p is None:
			self.em_ordem (p.esquerda)
			print(p.valor)
			self.em_ordem (p.direita)

	def pre_ordem(self,p):
		if not p is None:
			print(p.valor)
			self.pre_ordem (p.esquerda)
			self.pre_ordem (p.direita)

	def pos_ordem(self,p):
		if not p is None:
			self.pos_ordem(p.esquerda)
			self.pos_ordem(p.direita)
			print(p.valor)