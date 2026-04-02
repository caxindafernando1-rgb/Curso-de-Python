def leiaInt(msg):
      while True:
            try:
                  n = int(input(msg))
            except (ValueError, ModuleNotFoundError):
                  print('\033[1;31m ERRO! Digite um número inteiro válido \033[m')
                  continue
            except KeyboardInterrupt:
                  print('\033[1;31m Usuario cancelor sem ter digitado nada \033[m')
                  return 0
            else:
                  return n
            

def linha(tam = 42):
      return '-' * 42


def cabeçalho(txt):
      print(linha())
      print(txt.center(42))
      print(linha())


def menu(lista):
      cabeçalho('== MENU PRINCIPAL ==')
      c = 1
      for item in lista:
            print(f'\033[1;34m{c}\033[m --> \033[1;35m{item}\033[m')
            c += 1
      print(linha())
      opc = leiaInt('Digite uma opção: ')
      return opc
     