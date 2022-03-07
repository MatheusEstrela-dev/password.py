import random
import string
import argparse

alfabeto = string.ascii_letters
numeros = string.digits
simbolos = string.punctuation
def GeraSenha(length):
    all = alfabeto + numeros + simbolos
    password = "" . join(random.sample(all,length))
    print("A senha gerada foi: ",password)

def main():
    parser = argparse.ArgumentParser(description='projeto basico senha aleatoria, utilizando a biblioteca Random')
    parser.add_argument('-l', '--length', help = 'Define a quantidade de caracteres', type = int, default =  16)
    args = parser.parse_args()
    length = args.length
    print(length)
    GeraSenha(length)
if __name__=='__main__':
    try:
        main()
    except Exception as erro: print(f"Erro:{erro}")
