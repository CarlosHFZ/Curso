





r = "sim"
while r == "sim":
    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))
    media = ((nota1 + nota2)/2)
    if media == 10:
        print(f"Nota final do aluno {media}, !!!Aprovado com Distinção!!!")
    elif media >= 7:
        print(f"Nota final do aluno {media}, Aluno Aprovado")
    elif media < 7:
        print(f"Nota final do aluno {media}, Aluno Reprovado")
    r = input("Desaja calcular nota do Aluno novamente? responda: Sim ou Nao: ").lower()
        
    
    
    
