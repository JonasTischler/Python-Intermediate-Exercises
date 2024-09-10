# Ordenação de Lista: Escreva um programa que solicite ao usuário uma lista de números inteiros (separados por espaços) e, em seguida, exiba a lista ordenada em ordem crescente.

# Dicas: Use o método split() para separar os números e sorted() ou o método .sort() para ordenar a lista.


# #Minha tentativa. 
# while True:
# print('faça uma lista de números inteiros em qualquer ordem.')
# num_str = input('Insira os numeros separados por espaço: ')
# num_list = [] 

# num = num_str.split()
# num_int = int(num)
# num_list.append(num_int)
# order = num_list.sort()

# print(num_list)
# print(num_int)
# print(order)

# print('Teste de Passagem numeros ')  

#Minha tentativa com suporte do gpt.  
# while True:
#     print('faça uma lista de números inteiros em qualquer ordem.')
#     num_str = input('Insira os numeros separados por espaço: ')
#     num_list = []
#     for num in num_str.split():
#         num_list.append(int(num))

#     num_list.sort()
#     print(f'A ordem crescente é {num_list}')
        
#     continu = input('Deseja continuar? s/n: ')
#     if continu.lower() != 's':
#         print('Saindo da aplicação.')
#         break
#Versão revisada gpt.
while True:
    print('Faça uma lista de números inteiros em qualquer ordem.')
    num_str = input('Insira os números separados por espaço: ')
    
    try:
        num_list = [int(num) for num in num_str.split()]
        num_list.sort()
        print(f'A ordem crescente é {num_list}')
    except ValueError:
        print('Entrada inválida. Certifique-se de inserir apenas números inteiros separados por espaço.')
    
    continu = input('Deseja continuar? s/n: ')
    if continu.lower() != 's':
        print('Saindo da aplicação.')
        break        