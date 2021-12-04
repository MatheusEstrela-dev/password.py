import random
alfabeto = "abcdefghijklmnopqrstuvwxyz"
maiusculo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = "[]{}#()*;._-"

all = alfabeto + maiusculo + numeros + simbolos
length = 9
password = "" . join(random.sample(all,length))
print("A senha gerada foi:",password)