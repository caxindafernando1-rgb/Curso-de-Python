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
            print(f'\033[1;32m Cliente {nome} Registrado com sucesso! \033[m')


def lerArquivo(nome):
      try:
            a = open(nome, 'rt')
      except:
            print('Erro ao ler Arquivo!')
      else:
            cabeçalho('== Lita de Pagamentos ==')
            for linha in a:
                  dodo = linha.split(';').strip()

                  if len(dodo)  < 2:
                        continue
                  dodo[1] = dodo[1].replace('\n', '')
                  print(f'{dodo[0]:<30}{dodo[1]:>3} kwanzas')
      finally:
            a.close()


def somar_idades(nome_arquivo):
    total = 0
    try:
        with open(nome_arquivo, 'r') as f:
            for linha in f:
                dados = linha.strip().split(';')
                idade = int(dados[1])
                total += idade
    except:
        print("Erro ao ler o arquivo.")
    else:
        print(f'Total de idades: {total}')


def cadastrar(arq, nome='Desconhhecido', preço=0):
      try:
            a = open(arq, 'at')
      except:
            print('Ouve um erro na abertura do arquivo!')
      else:
            try:
                  a.write(f'{nome};{preço}\n')
            except:
                  print(f'Houve um ERRO na hora de escrever os dados!')
            else:
                  print(f'\033[1;m Novo registo de {nome} adicionado\033[m')
                  a.close()