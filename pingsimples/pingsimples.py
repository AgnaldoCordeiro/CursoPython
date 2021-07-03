import os #importa o modulo ou biblioteca do sistema
#para usar os recursos do sistema

print("#" * 60)#imprimindo o #60 vezez
#variavel que recebe o ip ou host
ip_ou_host = input('Digite o IP ou Host a ser verificado: ')
print("-" * 60)

#chamando system da biblioteca os - comando ping
# #-n -num de pactes que serao 6 {} onde passa a formatacao da variavel 
os.system('ping -n 6 {}'.format(ip_ou_host))
print("-" * 60)