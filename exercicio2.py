""" 
Programa: Média de aluno
Autor: J. Guilherme
licença: GNU
Data: 2024/05/07
Versãõ: v1
Descrição:  Este programa terá como proposta calcular a médiade um aluno e sua matéria
"""





"""
Crie um programa que após a entrada de um aluno e suas notas
bimestrais, ache a média, porém se a média for maior que 10
ou mneor que 0, informe o usuário média inválida.
Mas, se a média for válida aponte se ele estiver 7 e 10 - aprovado
entre 5 e 7 - recuperação
abaixo de 5 - reprovado
no final imprima o nome, matéria, média e seu resultado
"""
"""
As entradas das notas bimestrais não pode ser menor que zero e nem maior que dez.
Recomendo que crie um laco de repetição até que o usuário faça a entrada de forma correta.
"""
"""
Criar um laço de repetição para inserir novos alunos, porem o usuário terá a opção 1 - sim e 2 - não;
Depois de finalizar quero que imprima no final uma saída com a quantidade de alunos inseridos na lista.
"""
# Contador de quantos alunos entraram e olharam as médias
QA = 0
resp = 1

"""
Caso a opção escolhida seja sim, usar um loop para que outros alunos consigam consultar sua média
""" 
while resp == 1:
    nome = str(input("\nDigite o nome do aluno(a).\n"))
    materia = str(input("\nDigite a máteria.\n"))

    nb1 = float(input("\nDigite a nota do 1º Bimestre\n"))
    while nb1 < 0 or nb1 > 10:
        print("Erro !! Digite o número entre 0 e 10")
        nb1 = float(input("\nDigite a nota do 1º Bimestre\n"))

    nb2 = float(input("\nDigite a nota do 2º Bimestre\n"))
    while nb2 < 0 or nb2 > 10:
        print("Erro !! Digite o número entre 0 e 10")
        nb2 = float(input("\nDigite a nota do 2º Bimestre\n"))

    nb3 = float(input("\nDigite a nota do 3º Bimestre\n"))
    while nb3 < 0 or nb3 > 10:
        print("Erro !! Digite o número entre 0 e 10")
        nb3 = float(input("\nDigite a nota do 3º Bimestre\n"))

    nb4 = float(input("\nDigite a nota do 4º Bimestre\n"))
    while nb4 < 0 or nb4 > 10:
        print("Erro !! Digite o número entre 0 e 10")
        nb4 = float(input("\nDigite a nota do 4º Bimestre\n"))
    
    media = (nb1+nb2+nb3+nb4)/4

    if (media > 10):
        print("\nErro, média não pode ser maior que 10.\n")

    elif (media >= 7 and media <= 10):
        print(f"\nO(A) aluno(a) {nome} na máteria de {materia}, teve uma média de {media} e está Aprovado.\n")

    elif (media >= 5 and media < 7):
        print(f"\nO(A) aluno(a) {nome} na máteria de {materia}, teve uma média de {media} e está de Recuperação.\n")

    elif (media < 5 and media >= 0):
        print(f"\nO(A) aluno(a) {nome} na máteria de {materia}, teve uma média de {media} e está Reprovado.\n")

    else :
        print("\nErro, média menor que 0.\n")

    resp = int(input("\nVocê deseja continuar:"
                   "\n1 - sim"
                   "\n2 - não\n"))
    QA += 1

    while resp < 1 or resp > 2:
        print("Erro - Valor não pode ser diferente de 1 ou 2!")
        resp = int(input("\nVocê deseja continuar:"
                   "\n1 - sim"
                   "\n2 - não\n"))

else:
    print(f"\nMédia foi feita.\n"
      f"Quantidade de alunos {QA}\n")

