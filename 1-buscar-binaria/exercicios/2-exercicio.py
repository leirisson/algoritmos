# Modifique a função para retornar o número de iterações
# necessárias até encontrar o item (ou concluir que não está presente).

def binary_search(lista, item):
    inicio = 0
    fim_lista = len(lista) - 1
    conta_iteracoes = 0 
   
    while inicio <= fim_lista:
        meio = (inicio + fim_lista) // 2
        valor_do_meio = lista[meio]
   
        
        if(valor_do_meio == item):
            conta_iteracoes+=1
            return conta_iteracoes
        elif valor_do_meio > item:
            fim_lista = meio - 1
            conta_iteracoes+=1
        else:
            inicio = meio  + 1
            conta_iteracoes+=1
  

def main():
    minha_list = []
    
    for i in range(100):
        print(i)
        minha_list.append(i)

        
    print(binary_search(minha_list, 8))
    
if __name__ == "__main__":
    main()