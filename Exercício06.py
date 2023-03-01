# Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int (input('Digite um número:'))
d = 2 * n
t = 3 * n
r = n ** (1/2)

print ('O dobro é: {}'.format(d))
print ('O triplo é: {}'.format(t))
print ('A raiz quadrada é: {:.2f}'.format(r))
