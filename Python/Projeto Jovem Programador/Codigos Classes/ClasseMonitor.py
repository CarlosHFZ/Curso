

class Estudante:
    def __init__(self, nome, matricula) -> None:
        self.nome = nome
        self.matricula = int(matricula)
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
    @property
    def matricula (self):
        return self.__matricula 
    @matricula .setter
    def matricula (self, nova_matricula ):
        self.__matricula  = nova_matricula 
    def printar(self):
        print(f"Nome: {self.nome}\nMatricula: {self.matricula}")
class Funcionario:
    def __init__(self, nome, salario) -> None:
        self.nome = nome
        self.salario = float(salario)
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
    @property
    def salario(self):
        return self.__salario 
    @salario.setter
    def salario(self, novo_salario ):
        self.__salario = novo_salario
    def printar(self):
        print(f"Nome: {self.nome}\nSalario: {self.salario}")

class Monitor(Estudante, Funcionario):
    def __init__(self, nome, matricula, diciplina, salario) -> None:
        super().__init__(nome, matricula)
        Funcionario.__init__(self, nome, salario)
        self.diciplina = diciplina
    @property
    def diciplina(self):
        return self.__diciplina 
    @diciplina.setter
    def diciplina(self, novo_diciplina ):
        self.__diciplina = novo_diciplina
    def mostrarEst(self):
        print(f"Nome do Estudande: {self.nome}\nMatricula: {self.matricula}\nDiciplina: {self.diciplina}")
    def mostrarFunc(self):
        print(f"Nome do Estudande: {self.nome}\nSalario: {self.salario}\nDiciplina: {self.diciplina}")


r = input('1 - Funcionario\n2 - Estudante')
match r:
    case "1":
        fu = input('Nome do funcionario: ') 
        sa = float(input('Seu salario: '))
        di = input("Diciplina: ")
        moni = Monitor(fu,0,di,sa)
        r = input("1 - Confirmar\n2 - Cancelar")
        match r:
            case "1":
                print("")
                moni.mostrarFunc()
            case "2":
                print('Cancelado')
                exit()
            case __:
                print('Opção incorreta')
                exit()
    case "2":
        es = input('Nome do estudande: ') 
        ma = int(input('Sua matricula: '))
        di = input("Diciplina: ")
        moni = Monitor(es,ma,di,0)
        r = input("1 - Confirmar\n2 - Cancelar")
        match r:
            case "1":
                print("")
                moni.mostrarEst()
            case "2":
                print('Cancelado')
                exit()
            case __:
                print('Opção incorreta')
                exit()
    
