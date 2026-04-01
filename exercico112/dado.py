def lerNumero(msg):
      valido = False
      while not valido:
            entrada = str(input(msg)).replace(',', '.').strip()
            if entrada.isalpha() or entrada == '':
                  print(f'\033[1;31m ERRO! número \"{entrada}\" é invalido \033[m')
            else:
                  return float(entrada)