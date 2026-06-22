from dodo import *
from rich import print
from rich import *

def arquivoExiste(nome):
      try:
            a = open(nome, 'rt')
            a.close()
      except FileNotFoundError:
            return False
      else:
            return True
      
def creiarArquivo(nome):
      try:
            a = open(nome, 'wt+')
            a.close
      except:
            print('[red]Houve um ERRO na criação do arquivo![/]')
      else:
            print(f'[green] Cliente {nome} Registrado com sucesso! [/]')


def lerArquivo(nome):
      try:
            a = open(nome, 'rt')
      except:
            print('[red] Erro ao ler Arquivo! [/]')
      else:
            total = 0
            cabeçalho('== Lita de Pagamentos ==')
            for linha in a:
                  dodo = linha.strip().split(';')
                  if len(dodo)  < 2:
                        continue
                  dodo[1] = dodo[1].replace('\n', '')
                  print(f'{dodo[0]:<30}{dodo[1]:>3} kwanzas')
                  idade = int(dodo[1])
                  total += idade     
            print(f'[blue] Total de Pagamentos: {total} Kwanzas [/]')
      finally:
            a.close()





def cadastrar(arq, nome='Desconhhecido', preço=0):
      try:
            a = open(arq, 'at')
      except:
            print('[red] Ouve um erro na abertura do arquivo! [/]')
      else:
            try:
                  a.write(f'{nome};{preço}\n')
            except:
                  print(f'[red] Houve um ERRO na hora de escrever os dados! [/]')
            else:
                  print(f'[green] Novo registo de {nome} adicionado [/]')
                  a.close()