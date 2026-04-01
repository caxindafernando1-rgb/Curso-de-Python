def aumento(preço=0, taxa=10, formato = False):
      """
      --> Calcula o aumento de um determinado preço
      retornando  o resultado como ou sem formatação,
      #Para o preço: o preço que se quer reajustar.
      #Para taxa: qual é a porcentagem do aumento.
      #Para formato: qual a saída formatada ou não?
      #return: o valor reajustado, com ou sem formato
      """
      resp = preço + (preço * (taxa/100))
      return resp if formato is False else moeda(resp)


def diminuição(preço=0, taxa=10, formato=False):
      resp = preço - (preço * (taxa/100))
      return resp if formato is False else moeda(resp)


def dobro(preço=0, Formato=False):
      resp = preço * 2
      return resp if Formato is False else moeda(resp)


def matade(preço=0, Formato=False):
      resp = preço / 2
      return resp if Formato is False else moeda(resp)


def moeda(preço=0, moeda= 'Kzs'):
      return f'{preço:.2f}{moeda}'.replace('.', ',')


def resumo(preço=0, taxaa=10, taxar=-5):
      print('-' * 30)
      print('-' * 30)
      print(f'Analise do preço {moeda(preço)}'.center(30))
      print('~' * 30)
      print(f'Aumento é de \t{aumento(preço, taxaa, True)}')
      print(f'Sem o aumento \t{diminuição(preço, taxar, True)}')
      print(f'O dobro é \t{dobro(preço, True)}')
      print(f'A metade é \t{matade(preço, True)}')
      print('-' * 30)
      print('-' * 30)

