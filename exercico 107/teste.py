import moeda

p = float(input('Qual é o preço: '))
t = int(input('Qual é o preço: '))
print(f'O aumento de {p} com a taxa de {t} tornou o preço: {moeda.aumento(p, t)}')
print(f'A diminuição de {t}% no preço de {p} tornou o preço {moeda.diminuição(p, t)}')
print(f'Mas se quiser pagar em duas prestação cada metade de {p} vale {moeda. matade(p)}')
print(f'Se quiser levar 2, dobro de {p} é {moeda.dobro(p)}')