# Mínimo Produto Viável

Para selecionar nosso MVP (Minimum Viable Product), adotamos a metodologia da Matriz de Priorização. Essa abordagem nos permitiu avaliar e classificar os requisitos do produto com base em critérios específicos, garantindo uma escolha criteriosa. Ao utilizar a matriz, consideramos três dimensões-chave para cada história de usuário: valor de negócios, viabilidade e capacidade técnica da equipe. Cada dimensão foi pontuada em uma escala que inclui "muito alta", "alta", "média", "baixa" e "muito baixa".

Após atribuirmos as pontuações em cada dimensão, calculamos a pontuação total para cada história de usuário somando as avaliações das três dimensões. Com base nessa análise de priorização, selecionamos as histórias de usuário com as pontuações mais elevadas para compor tanto o MVP1. O MVP2 foi definido considerando as histórias de usuário com as menores pontuações, para que possamos no início do projeto entregar mais valor ao negócio do cliente.

## Critérios para pontuação

 - MA - MUITO ALTA
 - A - ALTA
 - M - MÉDIA
 - B - BAIXA
 - MB - MUITO BAIXA

## Pontuação das HU´s

| História de Usuário                                                                                                                    | Valor de Negócio | Capacidade Técnica | Viabilidade | TOTAL |
| -------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ------------------ | ----------- | ----- |
| US08- Como estudante, eu quero jogar o jogo da memória durante a fase de seleção de grupos                                             | MA               | A                  | MA          | 14    |
| US14- Como estudante, eu quero visualizar valor dos PAX de cada atividade                                                              | MA               | A                  | A           | 13    |
| US01- Como professor, eu quero importar uma arquivo .xls com a matricula e o email dos alunos para a criação da turma                  | MA               | B                  | MA          | 12    |
| US07- Como professor, eu quero criar grupos aleatórios de usuários cadastrados para o início da fase de seleção de grupos              | MA               | M                  | A           | 12    |
| US09- Como estudante, eu quero vizualizar as informações do meu grupo                                                                  | A                | A                  | A           | 12    |
| US10- Como estudante, eu quero vizualizar as informações dos integrantes do meu grupo                                                  | A                | A                  | A           | 12    |
| US13- Como estudante, eu quero vizualizar os requisitos para o cumprimento das atividades                                              | A                | A                  | A           | 12    |
| US15- Como estudante, eu quero vizualizar o ranking de PAX da minha turma                                                              | MA               | M                  | A           | 12    |
| US02 - Como professor, eu quero editar todos os dados das turmas para que eu possa administra-las                                      | B                | A                  | MA          | 11    |
| US03 - Como professor, eu quero excluir turmas caso seja necessidade para que eu tenha o controle                                      | B                | A                  | MA          | 11    |
| US18- Como professor, eu quero exportar uma arquivo .xls com os dados da turma, como as equipes e o saldo dos PAXs                     | MA               | B                  | A           | 11    |
| US04- Como usuário, eu quero editar informações do meu usuário de turma                                                                | A                | M                  | M           | 10    |
| US05- Como professor, eu quero excluir um aluno ou monitor de uma turma                                                                | B                | M                  | A           | 9     |
| US12- Como estudante, eu quero vizualizar as unidades e atividades                                                                     | M                | M                  | M           | 9     |
| US19 - Como professor, eu quero criar turmas sem a necessidade de importar um arquivo .xls para que eu tenha mais liberdade e controle | MB               | M                  | A           | 8     |
| US11- Como professor, eu quero definir a sequência das atividades e disciplinas                                                        | B                | B                  | M           | 7     |
| US06 - Como monitor, eu quero excluir um aluno de uma turma                                                                            | B                | B                  | B           | 6     |
| US17- Como professor, eu quero arquivar e excluir o arquivamento de uma turma                                                          | MB               | B                  | MB          | 4     |
| US16- Como estudante, eu quero acessar mídias da atividade                                                                             | B                | MB                 | MB          | 4     |


## MVP 1

| Tema |Épico |  HU  | Descrição |
|:----:|:----:|:----:| :-----------------------: |
|  T1    |  E1  | US01 | Como professor, eu quero importar uma arquivo .xls com a matricula e o email dos alunos para a criação da turma                                 |
|   T1   |  E1  | US02 | Como professor, eu quero editar todos os dados das turmas para que eu possa administra-las                                                      |
|   T2   |  E3  | US07 | Como professor, eu quero criar equipes aleatórias de alunos cadastrados para o início da fase de seleção de equipes                             |
|   T2   |  E3  | US08 | Como aluno, eu quero jogar o jogo da memória durante a fase de seleção de equipes                                                                |
|   T2   |  E3  | US09 | Como aluno, eu quero vizualizar as informações do meu grupo                                                                                     |
|   T2   |  E3  | US10 | Como aluno, eu quero vizualizar as informações dos integrantes do meu grupo                                                                     |
|   T2   |  E4  | US13 | Como aluno, eu quero vizualizar os requisitos para o cumprimento das atividades                                                                 |
|   T2   |  E4  | US14 | Como aluno, eu quero visualizar valor dos PAX de cada atividade                                                                                 |
|   T2   |  E4  | US15 | Como aluno, eu quero vizualizar o ranking de PAX da minha turma                                                                                 |

## MVP 2

| Tema |Épico |  HU  | Descrição |
|:----:|:----:|:----:| :-----------------------: |
|  T1    |  E1  | US03 | Como professor, eu quero excluir turmas caso seja necessidade para que eu tenha o controle                                                      |
|  T2    |  E5  | US04 | Como aluno, eu quero editar informações do meu usuário de turma                                                                                 |
|  T1    |  E1  | US05 | Como professor, eu quero excluir um aluno ou monitor de uma turma                                                                               |
|   T1   |  E1  | US06 | Como monitor, eu quero excluir um aluno de uma turma                                                                                            |
|   T2   |  E4  | US11 | Como professor, eu quero definir a sequência das atividades e disciplinas                                                                       |
|  T2    |  E4  | US12 | Como aluno, eu quero vizualizar as unidades e atividades                                                                                        |
|   T2   |  E4  | US16 | Como aluno, eu quero acessar mídias da atividade                                                                                                |
|   T1   |  E1  | US17 | Como professor, eu quero arquivar e excluir o arquivamento de uma turma                                                                         |
|   T1   |  E1  | US18 | Como professor, eu quero exportar uma arquivo .xls com matrícula, nome, email, equipe e o saldo de PAXs de todos os alunos da turma selecionada |
|   T1   |  E1  | US19 | Como professor, eu quero criar turmas sem a necessidade de importar um arquivo .xls para que eu tenha mais liberdade e controle                 |