def user_info(usuario = "professor"):

  print(f"Olá {usuario}")
  nome = input(f"Digite o seu nome {usuario}: ")
  disciplina = input("Digite a disciplina: ")

  return nome, disciplina

quant = 3
lista_usuarios = []
for i in range(quant):
  print(f"Usuario {i+1}")
  
  print("Digite 1 para professor ou 2 para aluno: ")
  opcao = input()

  
  nome = None
  disciplina = None

  if opcao == '1':
    
    nome, disciplina = user_info()

  elif opcao == '2':
    nome, disciplina = user_info(usuario = "aluno")
  else:
    print("Opção invalida!")

  if nome is not  None and disciplina is not None:
    
    dict_users = {
      'nome': nome,
      'Disciplina': disciplina
    }
    lista_usuarios.append(dict_users)
  else: 
    print("Informações não adicionadas!")
  # FIM DO FOR 


print("Informações: ")
print(lista_usuarios)
  # print("Disciplina: ", disciplina)

