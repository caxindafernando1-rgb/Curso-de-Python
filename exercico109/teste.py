import moeda

p = float(input('Qual é o preço: '))
t = int(input('Qual é o preço: '))
print(f'O aumento de {t}% ao preço {moeda.moeda(p)} é: {moeda.aumento(p, t, True)}')
print(f'A diminuição de {t}% ao preço de {moeda.moeda(p)} é {moeda.diminuição(p, t, True)}')
print(f'A metade de {moeda.moeda(p)} é {moeda. matade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')