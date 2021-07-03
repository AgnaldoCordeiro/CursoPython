

lista = [1, 10]
arquivo = open('teste.txt', 'r')
try:
    texto = arquivo.read()
    divisao = 10/1
    numero = lista[1]

    #x = a
    
except ZeroDivisionError:
    print('nao é possivel dividir por 0')
except IndexError:
    print('erro ao acessar um indez invalido da lista')
except Exception as ex:
    #print(ex) posso colocar msg tbm
    print('erro desconhecido. Erro: {}'.format(ex))
else:
    print('Exercute quando nao ocorre exceção')
finally:
    print('fechando arquivo')
    arquivo.close()
