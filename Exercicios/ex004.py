algo = input('Digite Algo: ')
print('O tipo primitivo desse valor é : ',type(algo))
print('Só tem espaços? ',algo.isspace())
print('É um número? ',algo.isnumeric())
print('É alfabético? ',algo.isalpha())
print('É alfanumérico? ',algo.isalnum())
print('Está em maiúscula? ',algo.isupper())
print('Está em minúscula? ',algo.islower())
print('Está capitalizada? ',algo.istitle())