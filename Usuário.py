from Pessoa import Pessoa

class Control:

    def __init__(self):
        self.person = Pessoa()

    def Coletar(self):
        print("Informe seu nome: ")
        self.person.setNome(input())
        print("Informe seu telefone: ")
        self.person.setTelefone(input())
        print("Informe seu endereço: ")
        self.person.setEndereco(input())
        print("Informe sua Data de Nascimento: ")
        self.person.setDNascimento(input())


    def Mostrar(self):
        print(self.person.consultarUsuario())

    def menuLogin(self):
        self.login = input("Informe os seguintes dados: " +
                               "\nLogin: ")

        self.senha = input("Senha: ")
            if (self.model.usuarioExistente(self.login, self.senha) != True):
                print("Login e senha não válidos")
            else:
                self.opcao2 = -1
                self.cLivro.loginAtual = self.login
                self.menuUsuarioCompleto()




