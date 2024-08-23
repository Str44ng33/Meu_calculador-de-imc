nome = input('Qual seu nome? ')
idade = int(input('Qual sua idade? '))  
peso = float(input('Qual seu peso? '))
altura = float(input('Sua altura? '))
imc = peso / (altura * altura)
data = 2024
nascimento = data - idade  

print(f'Você se chama {nome}, sua idade é {idade}')
print(f'Você pesa: {peso} kg e sua altura é {altura} m')
print(f'Seu IMC é: {imc:.2f}')
print(f'E tu nasceu em {nascimento}')
