x = "olá"
try:
    print(x)
except NameError:
    print(NameError)
finally:
    print("este script foi testado!")


y = -1

if y < 0:
    raise Exception("Número menor que zero") # imprime no conosole