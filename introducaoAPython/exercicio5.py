"""Faça uma função que recebe um texto (exemplo logo abaixo) e retorna o texto sem os sinais de pontuação

Exemplo de entrada: "O despertador toca. É hora de acordar! Levanto-me lentamente, 
espreguiçando-me. Olho pela janela: o sol está se levantando. Que belo dia!
Preparo-me para mais uma jornada. Tomo um café da 
manhã reforçado: torradas, ovos e suco de laranja. Estou pronto para enfrentar o mundo."

Exemplo de saída: "O despertador toca É hora de acordar Levanto me lentamente
espreguiçando me Olho pela janela o sol está se levantando Que belo dia 
Preparo me para mais uma jornada Tomo um café da manhã reforçado torradas ovos e suco 
de laranja Estou pronto para enfrentar o mundo" """

texto = input("Digite um texto: ")

dict_pontuacao = {
  "!": " ",
  ":": " ",
  ".": " ",
  ",": " ",
  ";": " ",
  "-": " ",
  "?": " "
}
novo_texto = ''
for letra in texto:
  #print(letra)
  letter = dict_pontuacao.get(letra, letra)  
  novo_texto = novo_texto + letter

print(novo_texto)

