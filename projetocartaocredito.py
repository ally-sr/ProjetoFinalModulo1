import funçõescd
print ('Sobre qual tema de cartão de credito deseja falar?')
print ('1 - Desejo saber mais sobre os benefícios do meu cartão atual')
print ('2 - Desejo um novo cartão!')
print ('3 - Desejo obter mais informações sobre a minha fatura')
print ('4 - Desejo receber a minha fatura por e-mail')

selecao = int(input("Escolha uma opção entre 1 e 4: "))

if selecao == 1:
    cartaoAtual = input('Informe a categoria do seu cartão: ')
    beneficiosGold = funçõescd.InformativoBeneficiosGold(cartaoAtual)
    beneficiosBlack = funçõescd.InformativoBeneficiosBlack(cartaoAtual)
    beneficiosPlatinum = funçõescd.InformativoBeneficiosPlatinum(cartaoAtual)
    beneficiosVIP = funçõescd.InformativoBeneficiosVIP(cartaoAtual)

elif selecao == 2:
    cartaoAtual = input('Informe o seu cartão Atual: ')
    cartaoDesejado = input('Qual cartão deseja obter? ')
    desejoCartao = funçõescd.mesmoCartao (cartaoDesejado,cartaoAtual)
    renda = float(input ('Informe a sua renda: '))
    score = float(input('Informe o seu score Serasa: '))
    desejoCartao = funçõescd.novoCartao (cartaoDesejado, renda,score)

elif selecao == 3:
    dataFechamento = float(input('Informe a data de fechamento da sua fatura: '))
    vencimento = funçõescd.venc(dataFechamento)
    melhorCompra = funçõescd.melhorCompra(dataFechamento)

elif selecao == 4:
    email = input('Informe o seu e-mail: ')
    print('Fatura enviada para o e-mail!')
else: 
    print('Opção Inválida. Por favor, tente novamente.')





    
       
    


   
    




    





    

