import calculadora2
from auladiotv import Televisao
from computadorPalavras import contador_letras

calculadora = calculadora2.Calculadora()
print(calculadora.soma(5, 10))
print(calculadora.subtracao(1994, 2021))

tv = Televisao()

print(tv.ligada)
tv.power()
print(tv.ligada)

lista = ['elefante', 'zebra', 'animais', 'agnaldo']
print(contador_letras(lista))

#class Calculadora:
#    def __init__(self, num1, num2):
#        self.a = num1
#        self.b = num2
#
#    def soma(self):
#             return self.a + self.b
#def é igual a metodo
   




#calculadora = Calculadora(50, 2)
#print(calculadora.soma())

#valor1 = int(input("digite o valor: "))
#valor2 = int(input('digide mais um valor: '))
#total = soma(valor1, valor2)
#print(total)










#conjunto = {1, 2 ,3 ,4 ,5}
#conjunto2 = {3, 4, 5, 6, 7, 8, 9, 10}
#conjunto_uniao = conjunto.union(conjunto2)

#print('Uniao {}'.format(conjunto_uniao))
#conjunto_interseccao = conjunto.intersection(conjunto2)
#print(conjunto_interseccao)

#conjunto_diferenca = conjunto2.difference(conjunto)
#print(conjunto_diferenca)










#conjunto = {1, 2, 3, 4}
#conjunto.add(5)
#conjunto.discard(3)
#print(conjunto)



#lista = [12, 10, 7, 5]
#lista_animal = ['cachorro', 'leao', 'gato', 'elefante', 'zebra', 'macaco', 'baleia']

#print(len(lista_animal))


#tupla_animal = tuple(lista_animal)
#print(type(tupla_animal))
#print(tupla_animal)




#lista.sort()
#lista_animal.sort()

#print(lista)
#print(lista_animal)
#print('')
#print('')
#lista.reverse()
#lista_animal.reverse()
#print(lista)
#print(lista_animal)

#print(lista_animal)

#if 'lobo' in lista_animal:
#    print('existe um gato na lista')
#else:
#    print('nao existe um lobo na lista')
#    lista_animal.append('lobo')
#    print(lista_animal)

#lista_animal.pop(1)
#lista_animal.remove('cachorro')
#print(lista_animal)