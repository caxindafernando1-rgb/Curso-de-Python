from dodo import *
from time import sleep
from arquivo import *

arq = 'cursoEmVideo.txt'

if not arquivoExiste(arq):
      creiarArquivo(arq)

while True:
      resposta = menu(['Criar Arquivo', 'Cadastrar Pessoas', 'Sair do Programa'])
      if resposta == 1:
            cabeçalho(f'\033{lerArquivo(arq)}\033[m')
      elif resposta == 2:
            cabeçalho('\033[1;35m Opção 2 selecionada\033[m')
      elif resposta == 3:
            cabeçalho('\033[1;35m Saindo do programa... Até logo! \033[m')
            break
      else:
            print(f'\033[1;31m {resposta} Não é uma resposta valida! Tenta novamente\033[m')
      sleep(2)