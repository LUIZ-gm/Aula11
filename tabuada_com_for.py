numero = int(input("Digite o número da tabuada: "))

print ("--- Tabuada do número: {número} ---")

#o for gera numeros na flata (range) de 1 até 10
for i in range(1, 11):
    print(f"{i} x {numero} = {i * numero}")

print("-- fim da tabuad! --")