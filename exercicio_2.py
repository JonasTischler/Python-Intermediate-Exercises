# Calculadora de Média Ponderada: Escreva um programa que peça ao usuário para inserir três notas e seus respectivos pesos. 
# O programa deve calcular a média ponderada das notas com base nos pesos fornecidos e exibir o resultado.
#Minha solução
# print('Digite as três notas de suas provas abaixo: ')
# score_str1 = input('Nota 1: ')
# score_str2 = input('Nota 2: ')
# score_str3 = input('Nota 3: ')

# print('Agora digite os respectivos pesos abaixo: ')
# weight_str1 = input('Peso 1: ')
# weight_str2 = input('Peso 2: ')
# weight_str3 = input('Peso 3: ')

#Questionando o gpt sobre possiveis soluções, surgiu uma ideia junto a ele com listas.
while True:
    try:
        score_str = input('Digite as três notas separadas por espaço: ').split()
        scores = [float(score) for score in score_str]
        score_num1, score_num2, score_num3 = scores
        print(f'As conversoes {score_num1} {score_num2} {score_num3}')

        weight_str = input('Digite os respectivos pesos para cada nota: ').split()
        weights = [float(weight) for weight in weight_str]
        weight1, weight2, weight3 = weights
        print(f'As conversoes {weight1} {weight2} {weight3}')

        final_score = ((score_num1*weight1)+(score_num2*weight2)+(score_num3*weight3)) / (weight1+weight2+weight3)
        print(f'Sua média ponderada foi de {final_score:.2f}')
    except ValueError:
        print('Por favor, digite apenas numeros válidos separados por espaço.')
        
    continu = input('Deseja continuar? s/n: ')
    if continu.lower() != 's':
        print('Saindo da aplicação.')
        break
    
    
#Uma versão refinada sugerida pelo gpt
# while True:
#     try:
#         # Coleta e validação das notas
#         score_str = input('Digite as três notas separadas por espaço: ').split()
#         if len(score_str) != 3:
#             raise ValueError("Você deve inserir exatamente três notas.")
#         scores = [float(score) for score in score_str]
#         score_num1, score_num2, score_num3 = scores
#         print(f'Notas convertidas: {score_num1} {score_num2} {score_num3}')

#         # Coleta e validação dos pesos
#         weight_str = input('Digite os respectivos pesos para cada nota: ').split()
#         if len(weight_str) != 3:
#             raise ValueError("Você deve inserir exatamente três pesos.")
#         weights = [float(weight) for weight in weight_str]
#         weight1, weight2, weight3 = weights
#         print(f'Pesos convertidos: {weight1} {weight2} {weight3}')

#         # Cálculo da média ponderada
#         final_score = ((score_num1 * weight1) + (score_num2 * weight2) + (score_num3 * weight3)) / (weight1 + weight2 + weight3)
#         print(f'Sua média ponderada foi de {final_score:.2f}')
#     except ValueError as e:
#         print(f'Erro: {e}')
#     except ZeroDivisionError:
#         print('Erro: A soma dos pesos não pode ser zero.')
        
#     continu = input('Deseja continuar? s/n: ')
#     if continu.lower() != 's':
#         print('Saindo da aplicação.')
#         break