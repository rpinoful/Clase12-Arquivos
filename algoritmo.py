lista_numeros :list = [70,40,31,96,41]


#função para ordenar
def ordenar_numeros_lista(numeros:list) -> list:
    copia_lista = numeros.copy()
    for i in range(len(copia_lista)): # gera os indice de 0 ate o tamanho da lista neste casso 0 ate 4 
        for j in range(i+1,len(copia_lista)): #gera indice tambem so que começa desde 1 ate 4
            if copia_lista[i] > copia_lista[j]:
                copia_lista[i],copia_lista[j] = copia_lista[j],copia_lista[i]
    
    return copia_lista
    








ordenar_numeros_lista(lista_numeros)