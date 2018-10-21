class No:
	def __init__(self,chave=None,valor=None):
		self.chave = chave
		self.valor = valor
		self.filho = {}

	def add_no(self,chave,data=None):
		if not isinstance(chave,No):
			self.filho[chave] = No(chave,data)

class Tree_Trie:
	def __init__(self):
		self.cabeca = No()

	def add_palavra(self,palavra):
		node = self.cabeca
		aux = 0

		for i in range(len(palavra)):
			if palavra[i] in node.filho:
				node = node.filho[palavra[i]]
			else:
				node.add_no(palavra[i])
				node = node.filho[palavra[i]]

		node.data = palavra

	def verificar(self, palavra):
		if palavra is None:
			raise KeyError(palavra)

		node = self.cabeca
		flag = True

		for letra in palavra:
			if letra in node.filho:
				node = node.filho[letra]
			else:
				flag = False
				break

		if flag:
			return flag
		return False
