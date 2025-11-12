# Escreva uma função que use busca binária para verificar
# se um número está em uma lista ordenada de 1 a 100.
# Retorne True ou False.

def search_binary(lista, item):
    inicio=0
    fim = len(lista)-1
    
    while inicio <=fim:
        meio = (inicio + fim) // 2
        valor_meio = lista[meio]
        
        if(valor_meio == item):
            return True
        elif valor_meio > item:
            fim = meio - 1
        else:
            inicio = meio + 1
    return False


def main():
    minha_list = []
    
    for i in range(100):
        minha_list.append(i)
    print(search_binary(minha_list, 8))


if __name__ == "__main__":
    main()