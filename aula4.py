alunos = dict()

matricula = 1

while True:
    escolha = int(input("digite uma das opções:\n" +
                        "1 - cadastrar aluno\n" +
                        "2 - Ver todos os alunos\n" +
                        "0 - Finalizar"))
    
    match escolha:
        case 1:
            nome = input("Digite o nome do aluno: ")
            idade = int(input("Digite a idade do aluno: "))
            sexo = input("Digite o sexo do aluno: ")

            alunos[matricula] = {
                "nome": nome,
                "idade": idade,
                "sexo": sexo
            }

            matricula += 1

        case 2:
            for i, v in alunos.items():
                print(f"O aluno de matricula {i}, tem as seguintes informações {v}")

        case 0: 
            break