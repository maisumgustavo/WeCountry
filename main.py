print(
    '-'*4+'Sejam bem vindos!'+'-'*4+
    '\nEste é o WeCountry!'+
    '\nUm pais totalmente digital. Criado por Presidente bolinho do canal PresidenteBolinho na Twich!'+
    '\nAos poucos. Este pais está sendo criado, e logo logo, ele estará pronto para ser usado!'
)

def main():
    print(
        'Agora, para começar, você é: ' +
        '\nHomem;' +
        '\nMulher;'
    )

    opcao = input('Digite uma das opções: ')

    if opcao.lower() == 'homem':
        print('Certo querido.')
    elif opcao.lower() == 'mulher':
        print('Certo querida.')

    
    
main()