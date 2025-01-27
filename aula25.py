
"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')

qtd_caracteres_nome = len(nome) 
qtd_vazio_nome = ''in nome
qtd_letras_nome = qtd_caracteres_nome - qtd_vazio_nome

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {(nome[::-1])}')
    
    if qtd_vazio_nome == True:
        print('Seu nome contém espaços')
    
    print(f'Seu nome tem %d letras' % (qtd_letras_nome))
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[len(nome)-1:len(nome):]}')
else:
    print('Desculpe, você deixou campos vazios.')