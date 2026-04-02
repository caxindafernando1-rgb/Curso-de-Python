from dodo import *

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
            print('Houve um ERRO na criação do arquivo!')
      else:
            print(f'Arquivo {nome} Criado com sucesso!')


def lerArquivo(nome):
      try:
            a = open(nome, 'rt')
      except:
            print('Erro ao ler Arquivo!')
      else:
            cabeçalho('== PESSOAS CADASTRADAS ==')
            for linha in a:
                  dodo = linha.split(';')
                  dodo[1] = dodo[1].replace('\n', '')
                  print(f'{dodo[0]:<30}{dodo[1]:>3} anos')
      finally:
            a.close()


def cadastrar(arq, nome='Desconhhecido', idade=0):
      try:
            a = open(arq, 'at')
      except:
            print('Ouve um erro na abertura do arquivo!')
      else:
            try:
                  a.write(f'{nome};{idade}\n')
            except:
                  print(f'Houve um ERRO na hora de escrever os dados!')
            else:
                  print(f'\033[1;m Novo registo de {nome} adicionado\033[m')
                  a.close()