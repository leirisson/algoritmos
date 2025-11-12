

def pesquisa_binaria(lista, item):
    incio=0
    fim = len(lista) - 1
    
    while(incio <=fim):
        meio = (incio + fim ) // 2
        valor_meio = lista[meio]
        
        print(f"baixo={incio}, alto={fim}, meio={meio} → lista[meio]={valor_meio}")
        
        if valor_meio == item:
            return meio
        elif valor_meio < item:
            incio = meio + 1
        else:
            fim = meio - 1
    return None


def main():
    minha_lista = [-1,0,5,7,9,13,15,90,100,112,130,220,234,300,304,400,432,453]
    
    idince_valor = pesquisa_binaria(minha_lista, 130)
    
    print(f"indice do resultado: ", idince_valor)
    print(f"valor do indice: ", minha_lista[idince_valor])
            

if __name__ == "__main__":
    main()
         
         