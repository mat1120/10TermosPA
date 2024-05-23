print("~"* 40)
print("10 TERMOS DE UMA PA".center(40))
print("~"* 40)
primeiro = int(input("Digite o primerio: "))
razao = int(input("Digite o ultimo termo: "))
contador = 1
while contador <= 10:
    print("{} - ".format(primeiro), end="")
    primeiro += razao
    contador += 1
usuario = str(input("\nGostaria de inserir mais termo? [S/N]: ")).strip().upper()
print("-=-"*15)
while usuario == "S":
    termos_adicionais = int(input("Quantos termos a mais voce gostaria de inserir: "))
    contador = 1
    while contador <= termos_adicionais:
        print("{} - ".format(primeiro), end="")
        primeiro += razao
        contador += 1
    usuario = str(input("\nGostaria de inserir mais termo? [S/N]: ")).strip().upper()
    print("-=-" * 15)
print("Fim do programa")





