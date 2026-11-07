# Calcular o IMC (Índice de Massa Corporal)

texto_peso = input("Digite o seu peso em kg exp: 80,5 Digite: ").replace(',', '.')
texto_altura = input("Digite a sua altura em metros exp: 1,72 Digite: ").replace(',', '.')

peso = float(texto_peso)
altura = float(texto_altura)

imc = peso / (altura * altura)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25.0:
    classificacao = "Saudável"
elif imc < 30.0:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

print("\n--- RESULTADO ---")
print(f"O seu IMC é: {imc:.2f}")
print(f"Situação: {classificacao}")