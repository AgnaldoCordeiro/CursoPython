import hashlib

string = input('Digite o texto a ser gerado: ')

menu = int(input(''' #### MENU - ESCOLHA O TIPO DE HASH ### 
                1) MDS
                2) SHA1
                3) SHA256
                4) SHA512
                Digite o número do hash a ser gerado: '''))

if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8'))
    print('O Hash MDS da string', string, 'é: ', resultado.hexdigest())
elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print('O Hash SHA1 da string', string, 'é: ', resultado.hexdigest())
elif menu ==3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print('O Hash SHA256 da string', string, 'é: ', resultado.hexdigest())
elif menu == 4:
    resultado = hashlib.sha512(string.encode('utf-8'))
    print('O Hash SHA512 da string', string, 'é: ', resultado.hexdigest())
else:
    print('Algo de errago nao deu certo, tente novamnte')
