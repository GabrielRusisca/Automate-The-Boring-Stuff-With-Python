tableData = [['apples', 'oranges', 'cherries',            'banana'],
                      ['Alice', 'Bob', 'Carol', 'David'],
                      ['dogs', 'cats', 'moose', 'goose']]
                      
def table_view(lis) -> None:
	n_listas = len(lis)
	tamanho_cada_lista = len(lis[0])
	maior_palavra_lista = []
	for n in lis:
		maior = 0
		for i in n                                                                                                                                                                                                                                                                                                                                                                                                                                                  :
			if len(i) > maior:
				maior = len(i)
		maior_palavra_lista.append(maior)
	for i in range(tamanho_cada_lista):
		for n in range(n_listas):
			print(f'{lis[n][i]:<{maior_palavra_lista[n]}}',  end=' ')
		print()
	
			
table_view(tableData)