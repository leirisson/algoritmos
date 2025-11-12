


def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    
    while baixo <= alto:
        # o mdeio deve ser atualizado
        meio = (baixo + alto) // 2
        valor_meio = lista[meio]
  
        if valor_meio == item:
            return meio
        if valor_meio < item:
            baixo = meio + 1 
        else:
            alto = meio - 1
            
    return None


def main():
    # lista ordenada
    minhalista = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    
    # primeiro teste
    print("Resultado encontrado: ", pesquisa_binaria(minhalista, 3))
    # segundo teste
    print("Resultado encontrado: ", pesquisa_binaria(minhalista, 16))


if __name__ == "__main__":
    main()