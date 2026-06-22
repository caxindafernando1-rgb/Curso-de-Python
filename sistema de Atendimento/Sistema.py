from dodo import *
from time import sleep
from arquivo import *
from rich import print
from rich import *

arq = 'cursoEmVideo.txt'

if not arquivoExiste(arq):
      creiarArquivo(arq)

while True:
      resposta = menu(['Ver Todos os Pagamentos ', 'Registrar Pagamento', 'Sair do Programa'])
      if resposta == 1:
            cabeçalho(f' {lerArquivo(arq)} ')
      elif resposta == 2:
            cabeçalho(' == Registrar Pagamento == ')
            nome = str(input('Nome: '))
            preço = leiaInt('Pagou: ')
            

            cadastrar(arq, nome, preço)      
      elif resposta == 3:
            cabeçalho('[red] Saindo do programa... Até logo! [/]')
            break
      else:
            print(f'[red] {resposta} Não é uma resposta valida! Tenta novamente [/]')
      sleep(2)