from menu import *

criarArquivo = open('cadastro.txt', 'w+')
criarArquivo.close()
while True:
    titulo('MENU')
    resp = opcoes()
    try:
        if resp == 1:
            titulo('PESSOAS CADASTRADAS')
            print(f'{cores(0)}Nomes', end='')
            print(f'Idades{cores(4)}'.rjust(len(bordas()) - 4))
            lerArquivo = open('cadastro.txt', 'r')
            dados = []
            for i in lerArquivo:
                i = i.strip()
                dados.append(i)
            lerArquivo.close()
            for i, v in enumerate(dados):
                if i % 2 == 0:
                    print(f'{v:<{len(bordas()) - 6}}', end='')
                else:
                    print(v)
        elif resp == 2:
            nome = str(input('Nome: ')).title()
            idade = int(input('Idade: '))
            escreverNoArquivo = open('cadastro.txt', 'a')
            escreverNoArquivo.write(f'{nome}\n')
            escreverNoArquivo.write(f'{idade}\n')
            escreverNoArquivo.close()
        elif resp == 3:
            break
    except:
        print(f'{cores(3)}Opção inválida{cores(4)}')