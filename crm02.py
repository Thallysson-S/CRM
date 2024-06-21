import mysql.connector

class Cliente:
    def __init__(self, nome, email, endereco, telefone):
        self.nome = nome
        self.email = email
        self.endereco = endereco
        self.telefone = telefone

class SistemaCRM:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="he182555@",
            database="crm_db"
        )
        self.cursor = self.conexao.cursor()

    def adicionar_cliente(self, cliente):
        try:
            sql = "INSERT INTO clientes (nome, email, endereco, telefone) VALUES (%s, %s, %s, %s)"
            val = (cliente.nome, cliente.email, cliente.endereco, cliente.telefone)
            self.cursor.execute(sql, val)
            self.conexao.commit()
            print("Cliente adicionado com sucesso!")
        except mysql.connector.Error as err:
            print(f"Erro ao adicionar cliente: {err}")

    def listar_clientes(self):
        try:
            self.cursor.execute("SELECT * FROM clientes")
            clientes = self.cursor.fetchall()
            if clientes:
                print("Lista de Clientes:")
                for cliente in clientes:
                    print(f"ID: {cliente[0]}, Nome: {cliente[1]}, Email: {cliente[2]}, Endereço: {cliente[3]}, Telefone: {cliente[4]}")
            else:
                print("Não há clientes cadastrados.")
        except mysql.connector.Error as err:
            print(f"Erro ao listar clientes: {err}")

    def iniciar_atendimento(self):
        print("Olá! Como posso te ajudar?")
        while True:
            opcao = input("Opções: 1 - Adicionar Cliente | 2 - Listar Clientes | 3 - Sair\nEscolha uma opção: ")
            if opcao == '1':
                nome = input("Nome do cliente: ")
                email = input("Email do cliente: ")
                endereco = input("Endereço do cliente: ")
                telefone = input("Telefone do cliente: ")
                novo_cliente = Cliente(nome, email, endereco, telefone)
                self.adicionar_cliente(novo_cliente)
            elif opcao == '2':
                self.listar_clientes()
            elif opcao == '3':
                break
            else:
                print("Opção inválida. Por favor, escolha uma das opções disponíveis.")

    def fechar_conexao(self):
        self.cursor.close()
        self.conexao.close()
        print("Conexão com o banco de dados fechada.")

# Execução do programa principal
if __name__ == "__main__":
    sistema_crm = SistemaCRM()
    sistema_crm.iniciar_atendimento()
    sistema_crm.fechar_conexao()
