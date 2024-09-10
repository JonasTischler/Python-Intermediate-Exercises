# Número Reverso: Escreva um programa que solicite ao usuário um número inteiro e, em seguida, exiba o número com seus dígitos invertidos.
# Por exemplo, se o usuário inserir 12345, o programa deve exibir 54321.
#Minha solução com alguns questiomanetos de funcionamento e dinamicas de codigo para o gpt.
while True:
    try:
        print('Digite um número inteiro de dois digitos não identicos ou mais digitos para inverte-los.')
        num_str = input('Digite o número: ')
        num_list = [int(num) for num in num_str]
        invert_list = num_list[::-1]
    
        print('O número invertido é', *invert_list)
    except ValueError:
        print('Entrada inválida.')
    continu = input('Deseja continuar? s/n: ')
    if continu.lower() != 's':
        print('Saindo da aplicação.')
        break    

#Sugestão de melhoria do gpt
# while True:
#     try:
#         print('Digite um número inteiro de dois ou mais dígitos para invertê-los.')
#         num_str = input('Digite o número: ')
        
#         # Inverter diretamente a string
#         invert_num_str = num_str[::-1]
        
#         print('O número invertido é', invert_num_str)
#     except ValueError:
#         print('Entrada inválida.')
    
#     continu = input('Deseja continuar? s/n: ')
#     if continu.lower() != 's':
#         print('Saindo da aplicação.')
#         break