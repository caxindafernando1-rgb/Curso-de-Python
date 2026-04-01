def aumento(preço, taxa):
      resp = preço + (preço * (preço/100))
      return resp


def diminuição(preço, taxa):
      resp = preço - (preço * (preço/100))
      return resp


def dobro(preço):
      resp = preço * 2
      return resp


def matade(preço):
      resp = preço / 2
      return resp