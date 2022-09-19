from ClasseBanco import ContaBancaria, ContaEspeçial, ContaPoupança



def main():
    nome = ""
    numero = 0
    saldo = 0
    dia = 0
    limite = 0
    
    conta_bancaria = []

    c = 0
    while True:
        print('Opção 1: Cadastro de cliente\nOpção 2: Depositar\nOpção 3: Sacar\nOpção 4: Seu rendimento\nOpção 5: Seus dados\nOpção 6: Encerrar ')
        r = input('Digite: ')
        print("")             
        match r:
            case "1":
                    nome = input('Nome do cliente: ')
                    numero = int(input('Numero da Conta: '))
                    saldo = float(input('Saldo Inicial: '))
                    dia = int(input('Dia do rendimento da conta: '))
                    limite = float(input('Limite do cliente: '))
                    print("Cadastro concluido")
                    especial = ContaEspeçial(nome, numero, saldo, dia, limite)
                    print("") 
            case "2":
                r = float(input('Digite o Valor a ser Depositado: '))
                especial.deposito(r)
                print("") 
            case "3":
                r = input("1 - Saque Normal\n2 - Saque Especial")
                print("")
                if r == "2":                 
                    r = float(input('Digite o Valor a ser Sacado: '))
                    especial.sacar(r)
                if r == "1":
                    r = float(input('Digite o Valor a ser Sacado: '))
                    especial.Sacar_especial(r)
                    print("") 
            case "4":
                print(f'Seu saldo de R${especial.saldo:.2f} foi para:')
                especial.calcular()
                print(f"Valor de R${especial.valor:.2f} rendido no dia {especial.dia}\nNovo saldo: R${especial.saldo:.2f}\nDivida: {especial.deve}")
                print("") 
            case "5":
                print(especial)
                print("") 
            case "6":
                break
                    
main()