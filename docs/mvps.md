# Mínimo Produto Viável

Para selecionar nosso MVP (Minimum Viable Product), adotamos a metodologia da Matriz de Priorização. Essa abordagem nos permitiu avaliar e classificar os requisitos do produto com base em critérios específicos, garantindo uma escolha criteriosa. Ao utilizar a matriz, consideramos três dimensões-chave para cada história de usuário: valor de negócios, viabilidade e capacidade técnica da equipe. Cada dimensão foi pontuada em uma escala que inclui "muito alta", "alta", "média", "baixa" e "muito baixa".

Após atribuirmos as pontuações em cada dimensão, calculamos a pontuação total para cada história de usuário somando as avaliações das três dimensões. Com base nessa análise de priorização, selecionamos as histórias de usuário com as pontuações mais elevadas para compor tanto o MVP 1. O MVP 2 foi definido considerando as histórias de usuário com as menores pontuações, para que possamos no início do projeto entregar mais valor ao negócio do cliente.

## Critérios para pontuação

 - MA - MUITO ALTA
 - A - ALTA
 - M - MÉDIA
 - B - BAIXA
 - MB - MUITO BAIXA

## Pontuação das HU´s

| User Stories         | Valor de negócio | Capacidade técnica | Viabilidade | MA | A | M | B | MB | TOTAL |
| -------------------- | ---------------- | ------------------ | ----------- | -- | - | - | - | -- | ----- |
| 2.1.3 - Como aluno, eu quero vizualizar o ranking em PAX de todas as equipes da minha turma          | MA               | A                  | MA            | 10 | 4  | 0 | 0 | 0  | 14    |
| 2.2.2 - Como aluno, eu quero visualizar valor em PAX da atividade                                                                                       | MA               | A                  | MA            | 10 | 4  | 0 | 0 | 0  | 14    |
| 2.3.3 - Como aluno, eu quero editar informações do perfil do meu usuário                                                                                | MA               | A                  | A            | 5  | 8  | 0 | 0 | 0  | 13    |
| 2.1.2 - Como aluno, eu quero contatar os membros da minha equipe por whatsapp                                                                           | A                | A                  | A            | 0  | 12 | 0 | 0 | 0  | 12    |
| 2.2.1 - Como aluno, eu quero visualizar os requisitos para o cumprimento da atividade                                                                   | A                | A                  | A             | 0  | 12 | 0 | 0 | 0  | 12    |
| 2.3.2 - Como aluno, eu quero realizar login para acessar a minha conta                                                                                  | A                | A                  | A             | 0  | 12 | 0 | 0 | 0  | 12    |
| 1.1.1 - Como professor, eu quero importar uma arquivo .xls com a matricula e o email dos alunos para a criação da turma                                 | MA               | B                  | A             | 5  | 4  | 0 | 2 | 0  | 11    |
| 1.1.6 - Como professor, eu quero exportar uma arquivo .xls com matrícula, nome, email, equipe e o saldo de PAXs de todos os alunos da turma selecionada | MA               | B                  | A             | 5  | 4  | 0 | 2 | 0  | 11    |
| 1.2.1 - Como professor, eu quero criar uma atividade para uma turma                                                                                     | A                | M                  | A           | 0  | 8  | 3 | 0 | 0  | 11    |
| 1.3.1 - Como professor, eu quero criar equipes aleatórios de usuários cadastrados para o início da fase de seleção de equipes                           | A                | M                  | A           | 0  | 8  | 3 | 0 | 0  | 11    |
| 2.1.1 - Como aluno, eu quero jogar jogos durante a fase de seleção de equipes                                                                           | A                | M                  | A           | 0  | 8  | 3 | 0 | 0  | 11    |
| 1.2.2 - Como professor, eu quero alterar as informações de uma atividade existente                                                                      | B                | MA                 | M           | 5  | 0  | 3 | 2 | 0  | 10    |
| 2.3.1 - Como aluno, eu quero realizar um cadastro para acessar a plataforma                                                                             | M                | A                  | M           | 0  | 4  | 6 | 0 | 0  | 10    |
| 1.1.3 - Como professor, eu quero arquivar uma turma para possuir um histórico das turmas                                                                | A                | B                  | M           | 0  | 4  | 3 | 2 | 0  | 9     |
| 1.1.4 - Como professor, eu quero adicionar monitores a uma turma para me auxiliarem                                                                     | M                | M                  | M           | 0  | 0  | 9 | 0 | 0  | 9     |
| 1.1.2 - Como professor, eu quero alterar o nome da turma para que eu possa administra-las                                                               | MB               | MA                 | B           | 5  | 0  | 0 | 2 | 1  | 8     |
| 1.1.7 - Como professor, eu quero realizar login para acessar a minha conta de usuário administrador                                                     | B                | M                  | M           | 0  | 0  | 6 | 2 | 0  | 8     |
| 2.2.3 - Como aluno, quero receber avisos das atividades criadas pelo professor                                                                          | B                | M                  | M           | 0  | 0  | 6 | 2 | 0  | 8     |
| 1.1.5 - Como professor, eu quero excluir um monitor de uma turmas                                                                                       | MB               | A                  | B           | 0  | 4  | 0 | 2 | 1  | 7     |
| 1.3.2 - Como professor, eu quero adicionar um aluno a uma equipe                                                                                        | MB               | A                  | B           | 0  | 4  | 0 | 2 | 1  | 7     |
| 1.3.3 - Como professor, eu quero excluir um aluno de uma equipe                                                                                         | MB               | A                  | B           | 0  | 4  | 0 | 2 | 1  | 7     |

Com base na tabela de priorização, podemos observar que as histórias de usuário da persona "Aluno" possuem alta prioridade devido à sua baixa complexidade técnica e alta viabilidade. No entanto, é necessário ter cuidado ao considerar sua inclusão no MVP 1. Isso se deve ao fato de que as histórias de usuário da persona "Professor" são de extrema importância e são fundamentais para viabilizar as histórias de usuário da persona "Aluno". Portanto, é crucial avaliar cuidadosamente a sequência de implementação, levando em consideração a dependência entre as personas e garantindo que as necessidades do professor sejam atendidas antes de priorizar as histórias do aluno.

Além da tabela supracitada, analisamos as relações entre as histórias no que tange a arquitetura do software. Levantado todos esses pontos realizamos a criação de 3 MVP’s.


## MVP 1
1.1.1 - Como professor, eu quero importar uma arquivo .xls com a matricula e o email dos alunos para a criação da turma
1.1.7 - Como professor, eu quero realizar login para acessar a minha conta de usuário administrador
1.2.1 - Como professor, eu quero criar uma atividade para uma turma
1.3.1 - Como professor, eu quero criar equipes aleatórios de usuários cadastrados para o início da fase de seleção de equipes

## MVP 2
1.1.3 - Como professor, eu quero arquivar uma turma para possuir um histórico das turmas
1.1.6 - Como professor, eu quero exportar uma arquivo .xls com matrícula, nome, email, equipe e o saldo de PAXs de todos os alunos da turma selecionada
2.1.1 - Como aluno, eu quero jogar jogos durante a fase de seleção de equipes
2.1.2 - Como aluno, eu quero contatar os membros da minha equipe por whatsapp
2.1.3 - Como aluno, eu quero vizualizar o ranking em PAX de todas as equipes da minha turma
2.2.1 - Como aluno, eu quero visualizar os requisitos para o cumprimento da atividade
2.2.2 - Como aluno, eu quero visualizar valor em PAX da atividade
2.2.3 - Como aluno, quero receber avisos das atividades criadas pelo professor
2.3.3 - Como aluno, eu quero editar informações do perfil do meu usuário
2.3.1 - Como aluno, eu quero realizar um cadastro para acessar a plataforma
2.3.2 - Como aluno, eu quero realizar login para acessar a minha conta

## MVP 3
1.1.2 - Como professor, eu quero alterar o nome da turma para que eu possa administra-las
1.1.4 - Como professor, eu quero adicionar monitores a uma turma para me auxiliarem
1.1.5 - Como professor, eu quero excluir um monitor de uma turmas
1.2.2 - Como professor, eu quero alterar as informações de uma atividade existente
1.3.2 - Como professor, eu quero adicionar um aluno a uma equipe
1.3.3 - Como professor, eu quero excluir um aluno de uma equipe

## Gerenciamento de Riscos 

- Falta de habilidades técnicas:
    - O time não possui habilidades suficientes para a realização do projeto.
    
            Capacitar a equipe constantemente durante o projeto;
            Ajuda constante caso um membro não consiga realizar uma tarefa.

Conforme previsto em nossa análise de riscos, devido à falta de habilidades técnicas, foi necessário criar um terceiro MVP para evitar que as histórias se tornassem débito técnico. O objetivo foi mitigar os riscos identificados e garantir a qualidade do produto final.

## Histórico de versões
 |  Data | Versão | Descrição | Autor(es) |
| :--------: | :----: | :---------------------------------: | :---------: |
| 24/05/2023 |   1.0   | Criação do documento | Vinícius |
| 20/05/2023 |   2.0   | Criação do documento | Vinícius |