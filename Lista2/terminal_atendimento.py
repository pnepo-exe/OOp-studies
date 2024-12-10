from sisbanco import Banco, Conta, ContaEspecial, ContaPoupança
def terminal():
    sisbanco = Banco(0.1125)
    while True:
        print("SisBanco::Bem-Vindo!")
        print(".::Opcoes::.")
        print("[0]-Cadastrar_Conta")
        print("[1]-Creditar")
        print("[2]-Debitar")
        print("[3]-Transferir")
        print("[4]-Consultar_Saldo")
        print("[5]-Render_Juros")
        print("[6]-Render_Bonus")
        print("[7]-Alterar_Taxa_Juros")
        print("[8]-Alterar_Taxa_Imposto")
        print("[9]-Sair")
        opcao = input("Digite:")

        
        if opcao == "0":
            # cadastre o numero da conta
            n = input("Digite o número da conta a ser criada:")
            # escolha o tipo de conta a ser cadastrado
            t = input("Qual tipo de conta a ser criada: S - Simples | P - Poupanca | E - Especial: ")
            if t.upper() == "S":
                contita = Conta(n)
            elif t.upper() == "P":
                contita = ContaPoupança(n)
            elif t.upper() == "E":
                contita = ContaEspecial(n)
            else:
                print("Insira um tipo valido de conta")
                return
            # cadastre a conta no sisbanco
            sisbanco.cadastrar(contita)
        elif opcao == "1":
            # solicite o número da conta alvo
            n1 = input("Digite o número da conta: ")
            # solicite o valor a ser creditado
            value = float(input("Digite o Valor a ser creditado: "))
            # realize a operação de crédito no sisbanco
            sisbanco.creditar(n1,value)
            pass
        elif opcao == "2":
            # solicite o número da conta alvo
            n2 = input("Digite o número da conta: ")
            # solicite o valor a ser debitado
            value1 = float(input("Digite o Valor a ser debitado: "))
            # realize a operação de débito no sisbanco
            sisbanco.debitar(n2,value1)
        elif opcao == "3":
            # solicite o número da conta origem
            n_o = input("Digite o número da conta de origem: ")
            # solicite o número da conta destino
            n_d = input("Digite o número da conta destino: ")
            # solicite o valor a ser transferido
            value2 = float(input("Digite o valor que será transferido: "))
            # realize a operação de transferência no sisbanco
            sisbanco.transferir(n_o,n_d,value2)
        elif opcao == "4":
            # solicite o número da conta alvo
            n_s = input("Digite o número da conta alvo: ")
            # realize a operação de obtenção de saldo no sisbanco
            saldo = sisbanco.saldo(n_s)
            # exiba o saldo na tela
            print(saldo)
        elif opcao == "5":
            # Solicite o número da conta alvo
            n_h = input("Digite o número da conta alvo: ")
            # Realize a operação de correção da poupança no sisbanco
            sisbanco.render_juros(n_h)
        elif opcao == "6":
            # Solicite o número da conta alvo
            n_z = input("Digite o número da conta alvo: ")
            # Realize a operação de conversão/rendimento de bônus no sisbanco
            sisbanco.render_bonus(n_z)

        elif opcao == "7":
            # Solicite a nova taxa de correção da poupança
            n_t = float(input("Digite a taxa de Poupança que você deseja aplicar: "))
            # Realize a operação de alteração da taxa no sisbanco
            sisbanco.set_taxa_poupança(n_t)

        elif opcao == "8":
            # Solicite a nova taxa de imposto
            n_i = float(input("Digite a taxa de imposto que você deseja aplicar: "))
            # Reliza a operação de alteração de taxa de imposto no sisbanco
            sisbanco.set_taxa_imposto(n_i)

        
        elif opcao == "9":
            print("SisBanco::Bye!")
            break






if __name__ == "__main__":
    terminal()
