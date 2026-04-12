from dodo import *
from time import sleep
from arquivo import *

arq = 'cursoEmVideo.txt'

if not arquivoExiste(arq):
      creiarArquivo(arq)

while True:
      resposta = menu(['Ver pessoas cadastradas', 'Cadastrar Pessoas', 'Sair do Programa'])
      if resposta == 1:
            cabeçalho(f'\033[1;32m {lerArquivo(arq)} \033[m')
      elif resposta == 2:
            cabeçalho(' == Registrar Pagamento == ')
            nome = str(input('Nome: '))
            preço = leiaInt('Pagou: ')
            cadastrar(arq, nome, preço)      
      elif resposta == 3:
            cabeçalho('\033[1;35m Saindo do programa... Até logo! \033[m')
            break
      else:
            print(f'\033[1;31m {resposta} Não é uma resposta valida! Tenta novamente\033[m')
      sleep(2)