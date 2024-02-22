#  Faça um algoritmo que recebe 4 notas e retorne a media ponderada. 
# A primeira nota tem peso 2, a segunda nota tem peso 4, a terceira 
# nota tem peso 1 e a quarta nota tem peso 3.

# Obs. Não pode utilizar métodos prontos do python, crie sua própria lógica.

notas = []
i=0
for i in range(0,4):
    print(i+1,"º nota: ")
    nota = float(input())
    notas.append(nota)

peso = 2+4+1+3
print(notas)
media = (notas[0] * 2 + notas[1] * 4 + notas[2] * 1 + notas[3] * 3) / peso

print("Sua media é: ", media)
