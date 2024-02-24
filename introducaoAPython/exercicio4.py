# . Faça uma função que recebe uma lista de valores: [1, 7, 2, 10, 9, 5, 3, 4, 6, 8]
# e retorne os valores em ordem: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].

# Obs. Não pode utilizar métodos prontos do python, crie sua própria lógica.

def insertionSort(valores):
    tam = len(valores)

    for i in range(1,tam):
        
        j= i
        aux = valores[j]

        while j > 0 and aux < valores[j-1]:
            valores[j] = valores[j-1]
            j = j - 1;
        valores[j] = aux

    return valores


valores = [1, 7, 2, 10, 9, 5, 3, 4, 6, 8]

# OUTRAS LISTAS PARA TESTES 
#valores = [30, 5, -6, 70, 5,22,90,-9,21,10]
#valores = [3, 0, 30, 10, -39, 0, 18, 3, 19,8]

valores_ordenado = insertionSort(valores)

print(valores_ordenado)
