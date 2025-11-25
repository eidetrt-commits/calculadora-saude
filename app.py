#Calculadora de IMC - Versão 2.0
print("Bem-vindo à Calculadora de ´Saúde")

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso/ (altura ** 2)

print(f"Seu IMC é: {imc:.2f}")

#Nova funcionalidade:
Classificação
if imc <18.5:
    print("Classificação: Abaixo do peso")
elif imc < 25:
    print("Classificação: Peso normal")
else:
    print("Classificação: Sobrepeso ou Obesidade")