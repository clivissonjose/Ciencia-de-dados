# Faça um algoritmo (utilizando o conceito de funções) que recebe 
# a temperatura em fahrenheit e converte para celsius.

# (32°F − 32) × 5/9 = 0°C


def converte(f):
   celsius = (f - 32) * 5/9
   return celsius


temperatura = float(input("Digite a temperatura em fahrenheit: "))
c = converte(temperatura)

print("Essa temperatura em celsiu é: ", c, "graus");

