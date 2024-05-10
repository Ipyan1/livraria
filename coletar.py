from Pessoa import Pessoa

class Pessoa:

    def __init__(self):
        self.nome = nome = ""
        self.telefone = telefone = ""
        self.endereco = endereco = ""
        self.Dt_Nascimento = Dt_Nascimento = ""
        self.login = login = ""
        self.senha = senha = ""

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getTelefone(self):
        return self.telefone

    def setTelefone(self, telefone):
        self.telefone = telefone

    def getEndereco(self):
        return self.endereco

    def setEndereco(self, endereco):
        self.endereco = endereco

    def cadastrarUSuario(self, nome, telefone, endereco):
        self.setNome(nome)

        self.setTelefone(telefone)
        self.setEndereco(endereco)

    def consultarUsuario(self):
        return "Nome: {}, \nTelefone: {}, \nEndereço: {}".format(self.getNome(), self.getTelefone(), self.getEndereco())

    def menuCadastro(self):
        self.nome = input("Bem-vindo a Livraria, " +
                          "Informe os dados para cadastro: " +
                          "\nNome: ")

        self.endereco = input("Endereço: ")
        self.validarNum(self.telefone, "Telefone: ")
        print("Data de Nascimento")
        self.validarData(self.telefone, 1, 31, "Dia: ")
        self.validarData(self.telefone, 1, 12, "Mês: ")
        self.validarAno(self.telefone, 0, "Ano: ")
        self.login = input("Login: ")
         while (self.model.verificarLogin(self.login) != False):
            self.login = input("Login já existente em sistema, por favor informe outro: ")
        self.senha = input("Senha: ")

        print(self.model.realizarCadastro(self.nome, self.endereco, self.telefone, self.dia, self.mes, self.ano,
                                          self.login, self.senha))






