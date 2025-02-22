def inicio2():
    squidBank = int(input("""Como posso ajudar agora? 
    Digite 1 se você já é cliente.
    Digite 2 se quer falar sobre cartão de crédito.
    Digite 3 se quer saber mais sobre investimentos.
    Digite 4 se quer saber mais sobre impréstimos.
    Digite 5 se ainda não é cliente do Banco Squid. 
    """))
    return squidBank

def concluir():
    conclusao = int(input("""Digite 1 se não tem mais dúvidas, ou
    Digite 2 se quiser voltar ao início do atendimento."""))
    if conclusao == 1:
        print("Obrigada e até logo") 
    elif conclusao == 2:
        squidBank = inicio2()
        return squidBank
    else:
        return concluir()

def menu1 ():
    opcaoMenu1 = int(input(""" Olá, cliente do Banco Squid! Você gostaria de mais informações sobre:
    Digite 1 para informações sobre Pix.
    Digite 2 para informações sobre a sua conta Squid.
    Digite 3 para saber mais sobre carteiras digitais.
    Digite 4 para informações sobre Débito Automático.
    Digite 5 para voltar ao menu anterior.
    """))
    return opcaoMenu1

def menu1_pix ():
    opcao_pix = int(input("""Saiba mais sobre o Pix: 
    Digite 1 para saber como fazer uma transferência Pix.
    Digite 2 para saber o que é Pix.
    Digite 3 para saber o que é uma chave Pix.
    Digite 4 para voltar ao menu anterior.
    """))

    if   opcao_pix == 1 :
        print("""""Para fazer uma transferência usando o Pix basta seguir os passos:
        1. Na tela inicial do seu aplicativo SquidBank, clique no atallho "Área Pix;
        2. Digite o valor da transferência;
        3. Insira a chave Pix;
        4. Confirme se os dados de quem irá receber estão corretos;
        5. Clique na opção "Transferir e digite sua senha de 6 dígitos.
        Pronto! Pix enviado!.
        """)
        return 

    elif opcao_pix == 2:
        print("""Pix é um novo meio de pagamentos criado pelo Banco Central do Brasil que facilita a transferência de dinheiro entre pessoas, empresas e até o recolhimento de impostos e taxas de serviço. 
        As transferências via Pix são instantâneas, e podem ser feitas a qualquer momento, 24 horas por dia, 7 dias na semana. Também não é cobrado nenhuma taxa do usuário o realizar a transferência. 
        Além disso, as tranferencias são mais seguras com a utilização de chaves Pix, assim você não precisa enviar seus dados bancários para receber uma transferência. """)
        return 

    elif opcao_pix == 3:
        print("""As chaves pix são como "apelidos" para a sua conta. Você registra uma informação sua como chave e só precisa passar esse dado na hora de receber um pagamento. Você pode registrar como chave Pix o seu e-mail, um telefone, seu CPF ou até mesmo gerar uma chave aleatória pelo aplicativo SquidBank. Dessa forma, quando soliicitarem seus dados para uma transferência, basta informar a chave Pix cadastrada. Entretando, o uso das chaves Pix não é obrigatório - você ainda poderá fazer transferencia Pix utilizando os dados da sua conta bancária. """)
        return

    elif opcao_pix == 4:
        return menu1()
    # return opcao_pix

def menu1_conta():
    opcao_conta = int(input("""Tenha mais informações sobre a sua conta:
    Digite 1 Para saber como categorizar os seus gastos.
    Digite 2 para saber como cancelar sua conta.
    Digite 3 para saber mais sobre portabilidade de salário.
    Digite 4 para voltar ao menu anterior. """))

    if opcao_conta == 1:
        print("""Assim que você realizar um gasto, automaticamente ele irá receber uma categoria (exemplos: Mercado, Telefonia) que ficara visível no seu extrato. Mas você pode mudar essa categoria como preferir. Caso queira alterar uma categoria, basta clicar na transação. Irá aparecer uma tela de detalhes, escolha a opção "Editar" e pronto.""")
    elif opcao_conta == 2:
        print("""Você pode cancelar sua conta direto no aplicativo. Na tela inicial, entre no seu perfil clicando no ícone com seu nome. Escoha a opção 'Configurar conta' e em seguida a opção 'Cancelar conta'. Pronto, sua conta sera encerrada e você receberá um e-mail de confirmação.""") 
    elif opcao_conta == 3:
        print("""A portabilidade de salário é uma autorização que permite que seu pagamento seja transferido automaticamente para sua conta Squid. A empresa continuará depositando seu salário no banco em que processa a folha de pagamento normalmente, e este será o responsável em realizar a transferência para o banco que você escolher.  """)
    elif opcao_conta == 4:
        return menu1()

def menu1_carteira():
    opcao_carteira = int (input("""Saiba mais sobre carteiras digitais:
    Digite 1 para saber quais cartões podem ser adicionados na sua carteira digital.
    Digite 2 para saber se existe limite de compras com carteiras digitais.
    Digite 3 para informações sobre usar mais de um cartão na sua carteira digital.
    Digite 4 para voltar ao menu anterior. """))

    if opcao_carteira == 1:
        print("Qualquer cartão que possua a modalidade crédito, débito ou ambas pode ser adicionado a uma carteira digital. Se o seu cartão possui só uma dessas funções, verifique se está escolhendo a modalidade correta na maquininha na hora de realizar o pagamento. ")
    elif opcao_carteira == 2:
        print("""Por questões de segurança, existe um limite diário no valor de R$ 3 mil reais para transações por meio de carteiras digitais. Esse limite não pode ser alterado pelo aplicativo. """)
    elif opcao_carteira == 3:
        print("""Você pode adicionar mais de um cartão nas suas carteiras digitais.""")
    elif opcao_carteira == 4:
        return menu1()

def menu1_debito():
    opcao_debito = int (input("""Tire suas dúvidas sobre Débito Automático
    Digite 1 para saber a diferença entre débito automático e DDA.
    Digite 2 para saber como cancelar um débito automático.
    Digite 3 para saber o que fazer caso não tenha saldo em conta na hora da efetivação de um débito automático.
    Digite 4 para voltar ao menu anterior."""))

    if opcao_debito == 1:
        print("""Débito automático é um serviço pelo qual você autoriza o SquidBank a debitar o valor do pagamento de uma conta automaticamento do valor da sua conta. DDA (Débido Direto Autorizado) é o serviço pelo qual vocễ consegue visualizar todos os boletos atribuídos ao seu CPF. Você pode autorizar o pagamento com a conta  ou acompanhar as cobranças pelo aplicativo SquidBank.""")
    elif opcao_debito == 2:
        print("""Acesse seu aplicativo SquidBank e vá na aba de "Assistente de Pagamentos". Lá, selecione a conta que deseja cancelar o débito automático e escolha a opção "Descadastrar Conta". Será solicitada sua senha de 6 dígitos para completar a ação. Será cancelado o débido automático a partir do próximo mês. """)
    elif opcao_debito == 3 :
        print("O pagamento da sua conta em débido automático só será efetivo caso haja saldo o suficiente em sua conta corrente até as 23:59 do dia anterior ao dia do vencimento da conta. Caso contrário, o pagamento deve ser feito manualmente.")
    elif opcao_debito == 4 :
        return menu1()

    
