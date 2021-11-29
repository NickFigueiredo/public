idade = int(input("Informe sua idade: "))
if idade > 0 and idade <= 150 :
    if idade < 18:
        print("\nVocê é menor de idade\n")
    else:
        print("\nVocê é maior de idade\n")
else:
    print("\nIdade invalida!\n")