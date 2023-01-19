from random import *

num = '0123456789'
letra_Minuscula = 'abcdefghijklmnopqrstuvxwyz'
letra_Maiuscula = 'ABCDEFGHIJKLMNOPQRSTUVXWYZ'
caracteres = '!@#$%&*'
senha = ''


for c in range(1, randint(5, 8) ):
    senha = senha + choice(num)
    senha = senha + choice(letra_Maiuscula)
    senha = senha + choice(letra_Minuscula)
    senha = senha + choice(caracteres)
    
print(senha)
print(len(senha))
