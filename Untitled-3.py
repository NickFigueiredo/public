n = float(input("Informe a sua altura: "))
m = float(input("Informe o seu peso: "))
imc = m/n **2
if imc<17:
    print("\nVocê está abaixo do peso!\n")
else:
    if(imc>18.5) and (imc<=24.99):
        print("\nSeu peso está normal!\n")
    else:
        if(imc>25) and (imc<=21.99):
            print("\nVocê está acima do peso!\n")
        else:
            if(imc>30) and (imc<=34.99):
                print("\nVocê está obeso!\n")
            else:
                if(imc>35) and (imc<=39.99):
                    print("\nVocê está obeso! (Severo)")
                else:
                    if(imc>40):
                        print("\nVocê está obeso! (Mórbido)")
