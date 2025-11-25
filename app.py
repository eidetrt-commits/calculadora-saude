# Calculadora de IMC - Versão 2.0
print("Bem-vindo à Calculadora de Saúde")

# Correção 1: Fechamos os dois parênteses no final
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)

# Correção no formato do f-string (sem espaços dentro das chaves)
print(f"Seu IMC é: {imc:.2f}")

# #Nova funcionalidade (comentar para não dar erro)
# Classificação

# Correção 2 e 3: Usar IF/ELIF/ELSE e corrigir 'inc' para 'imc'
if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif imc < 25:
    print("Classificação: Peso normal")
else:
    print("Classificação: Sobrepeso ou Obesidade")
