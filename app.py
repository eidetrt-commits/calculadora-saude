#Calculadora de IMC
#Desenvolvido por: Eide Nonato

print("Bem-vindo à Calculadora de Saúde")

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)
print("Seu IMC é:" imc)
