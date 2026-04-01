def aumento(preço=0, taxa=0, formato = False):
      resp = preço + (preço * (taxa/100))
      return resp if formato is False else moeda(resp)


def diminuição(preço=0, taxa=0, formato=False):
      resp = preço - (preço * (taxa/100))
      return resp if formato is False else moeda(resp)


def dobro(preço=0, Formato=False):
      resp = preço * 2
      return resp if Formato is False else moeda(resp)


def matade(preço=0, Formato=False):
      resp = preço / 2
      return resp if Formato is False else moeda(resp)


def moeda(preço=0, moeda= 'Kzs'):
      return f'{moeda}{preço:.2f}'.replace('.', ',')