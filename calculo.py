altura = float(input("digite seu tamanho: "))
peso = int(input("digite seu peso: "))

valor = peso // altura
valor_total = valor // altura
print(f"seu ICM e : {valor_total}")

if valor_total <= 18.5 :
    print("você esta abaixo do peso")
elif valor_total >= 18.5 and valor_total < 24.9 :
    print("esta no peso ideal ")
elif valor_total >= 25 and valor_total < 29.9 :
    print("você esta acima do peso ")
elif valor_total > 30 :
    print("você esta com obesidade ")
else :
    print("valor não encontrado")
