def cores(opcao):
    c = ('\033[7;37m', '\033[1;35m', '\033[1;33m', '\033[1;31m', '\033[m')
    return c[opcao]


def bordas():
    return '-' * 35


def titulo(txt):
    bordasTitulo = cores(1) + bordas() + cores(4)
    print(bordasTitulo)
    print(f'{cores(1)}{txt.center(len(bordas()))}{cores(4)}')
    print(bordasTitulo)


def opcoes():
    print(f'{cores(2)}1- Mostrar pessoas cadastradas')
    print('2- Cadastrar nova pessoa')
    print('3- Sair do sistema')
    print(bordas() + cores(4))
    opcao = int(input(f'{cores(0)}Escolha uma opção:{cores(4)} '))
    return opcao