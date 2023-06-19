# Behavior Driven Development (BDD)

## Persona: Professor

### Funcionalidade 1: Publicar atividade

#### História 1.1: 

Eu, como **professor** posso **definir a sequência das atividades e disciplinas** para **disponibilizar conteúdo**.

#### Cenário 1: Definir a sequência das atividades

**Dado** que estou autenticado como professor

**Quando** defino a atividade "Definição do MVP" como a 5ª da sequência

**Então** a atividade "Definição do MVP" aparece posteriormente a 4ª atividade

#### Cenário 2: Verificar a sequência das atividades

**Dado** que estou autenticado como aluno

**Quando** visualizo a atividade "Definição do MVP"

**Então** vejo a atividade posteriormente a 4ª atividade

#### História 1.2: 

Eu, como **professor** posso **definir o valor em PAX** para **bonificação clara para trazer motivação**.

#### Cenário 1: Definir o valor em PAX para uma atividade

**Dado** que estou autenticado como professor

**Quando** defino o valor de 30 PAXs para a atividade "Apresentação Final"

**Então** o valor em PAX para a atividade é atualizado com sucesso

#### Cenário 2: Definir o valor em PAX para uma atividade

**Dado** que estou autenticado como professor

**Quando** defino o valor de A3R0 PAXs para a atividade "Apresentação Final"

**Então** o valor em PAX para a atividade não é atualizado

#### Cenário 3: Verificar o valor em PAX de uma atividade

**Dado** que estou autenticado como aluno

**Quando** visualizo a atividade "Apresentação Final", que vale 30 PAX

**Então** vejo o valor de 30 PAX atribuído a atividade

#### História 1.3: 

Eu, como **professor** posso **definir datas** para **gerenciar atividades realizadas**.

#### Cenário 1: Definir data de início do semestre

**Dado** que estou autenticado como professor

**Quando** defino a data de início do semestre para 1º de março

**Então** a data de início do semestre é atualizada com sucesso

#### Cenário 2: Definir data de término do semestre

**Dado** que estou autenticado como professor

**Quando** defino a data de término do semestre para 30 de junho

**Então** a data de término do semestre é atualizada com sucesso

#### Cenário 3: Verificar a data de início do semestre

**Dado** que estou autenticado como professor

**Quando** defino a data de término do semestre para 31 de junho

**Então** a data de término do semestre não é atualizada

#### Cenário 4: Definir data de término do semestre

**Dado** que estou autenticado como professor

**Quando** defino a data de término do semestre para 31 de junho

**Então** a data de término do semestre não é atualizada

### Funcionalidade 2: Organizar turmas

#### História 2.1:

Eu, como **professor** posso **editar todos os dados das turmas** para **centralização dos dados**.

#### Cenário 1: Editar informações de uma turma

**Dado** que estou autenticado como administrador

**Quando** acesso a página de edição da turma "Turma A"

**Quando** modifico as informações da turma

**Então** as informações da turma são atualizadas com sucesso

#### Cenário 2: Validar restrições ao editar turma

**Dado** que estou autenticado como administrador

**Quando** tento editar as informações da turma "Turma B"

**Quando** insiro dados inválidos

**Então** recebo uma mensagem de erro informando as restrições de edição

**Quando** as informações da turma não são modificadas

#### Cenário 3: Verificar visualização das informações da turma

**Dado** que estou autenticado como professor

**Quando** acesso a página de visualização da turma "Turma C"

**Então** visualizo todas as informações da turma corretamente

#### História 2.2: 

Eu, como **professor** posso **criar grupos aleatórios de usuários cadastrados para o início da fase de seleção de grupos** para **centralização dos dados**.

#### Cenário 1: Criar grupos aleatórios para uma turma

**Dado** que estou autenticado como administrador

**Quando** crio grupos aleatórios para a turma "Turma A"

**Então** os grupos são criados com sucesso

**Quando** cada grupo possui um número igual de usuários cadastrados

#### Cenário 2: Validar quantidade mínima de usuários para criar grupos

**Dado** que estou autenticado como administrador

**Quando** tento criar grupos aleatórios para a turma "Turma B"

**Quando** a quantidade de usuários cadastrados é insuficiente

**Então** recebo uma mensagem de erro informando a quantidade mínima necessária

**Quando** nenhum grupo é criado

#### Cenário 3: Verificar a distribuição aleatória dos usuários nos grupos

**Dado** que estou autenticado como professor

**Quando** visualizo a distribuição dos usuários nos grupos da turma "Turma C"

**Então** os usuários estão distribuídos aleatoriamente nos grupos

**Quando** cada grupo possui aproximadamente o mesmo número de usuários

#### História 2.3: 

Eu, como **professor** posso **exportar um arquivo .xls com matrícula, nome, email, equipe e o saldo de PAX de todos os alunos da turma selecionada** para **feedback rápido do desempenho**.

#### Cenário 1: Exportar dados dos alunos em formato .xls

**Dado** que estou autenticado como administrador

**Quando** seleciono a opção de exportar dados dos alunos da turma "Turma A"

**Então** um arquivo .xls é gerado com sucesso

**Quando** o arquivo contém as colunas de matrícula, nome, email, equipe e saldo de PAXs de todos os alunos da turma

#### Cenário 2: Validar permissões de exportação de dados dos alunos

**Dado** que estou autenticado como professor

**Quando** tento exportar dados dos alunos da turma "Turma B"

**Então** recebo uma mensagem de erro informando que não tenho permissão para exportar os dados

**Quando** nenhum arquivo .xls é gerado

#### Cenário 3: Verificar a precisão dos dados exportados

**Dado** que estou autenticado como administrador

**Quando** exporto dados dos alunos da turma "Turma C"

**Então** verifico que o arquivo .xls contém as informações corretas de matrícula, nome, email, equipe e saldo de PAXs de todos os alunos da turma

#### História 2.4: 

Eu, como **professor** posso **arquivar turmas** para **possuir o histórico das turmas**.

#### Cenário 1: Arquivar uma turma

**Dado** que estou autenticado como administrador

**Quando** seleciono a opção de arquivar a turma "Turma A"

**Então** a turma é arquivada com sucesso

**Quando** os dados da turma não estão mais visíveis nas consultas e operações regulares

#### Cenário 2: Validar restrições ao arquivar turma

**Dado** que estou autenticado como administrador

**Quando** tento arquivar a turma "Turma B"

**Quando** a turma possui atividades ou grupos não concluídos

**Então** recebo uma mensagem de erro informando as restrições de arquivamento

**Quando** a turma não é arquivada

#### Cenário 3: Verificar a lista de turmas arquivadas

**Dado** que estou autenticado como professor

**Quando** acesso a lista de turmas arquivadas

**Então** visualizo corretamente todas as turmas arquivadas

**Quando** posso restaurar ou realizar ações específicas em cada turma arquivada

#### História 2.5: 

Eu, como **professor** posso **importar um arquivo .xls com matrícula, nome e email de todos os alunos da turma selecionada** para **centralização dos dados**.

#### Cenário 1: Importar dados dos alunos a partir de um arquivo .xls

**Dado** que estou autenticado como administrador

**Quando** seleciono a opção de importar dados dos alunos para a turma "Turma A"

**Quando** seleciono um arquivo .xls válido contendo matrícula, nome e email dos alunos

**Então** os dados dos alunos são importados com sucesso para a turma

#### Cenário 2: Validar formato inválido do arquivo .xls

**Dado** que estou autenticado como administrador

**Quando** tento importar dados dos alunos para a turma "Turma B"

**Quando** seleciono um arquivo .xls inválido ou com formato incorreto

**Então** recebo uma mensagem de erro informando o formato inválido do arquivo

**Quando** nenhum dado é importado para a turma

#### Cenário 3: Verificar a precisão dos dados importados

**Dado** que estou autenticado como administrador

**Quando** importo dados dos alunos para a turma "Turma C" a partir de um arquivo .xls válido

**Então** verifico que os dados de matrícula, nome e email dos alunos são importados corretamente para a turma

## Persona: Estudante

### Funcionalidade 3: Criação de equipes

#### História 3.1: 

Eu, como **estudante** posso **jogar jogos durante a dase de seleção de grupos** para **um processo fluido, perda de manos tempo de aula**.

#### Cenário 1: Jogar um jogo durante a fase de seleção de grupos

**Dado** que estou autenticado como participante da fase de seleção de grupos

**Quando** acesso a página de jogos disponíveis

**E** seleciono o jogo "Jogo A" para jogar

**Então** sou redirecionado para o jogo

**E** posso jogar o jogo conforme as regras estabelecidas

#### Cenário 2: Validar restrições de acesso aos jogos durante a fase de seleção de grupos

**Dado** que estou autenticado como membro de um grupo formado

**Quando** tento acessar a página de jogos disponíveis

**Então** recebo uma mensagem de erro informando que não posso jogar durante a fase de seleção de grupos

#### Cenário 3: Verificar registro de pontuação do jogo durante a fase de seleção de grupos

**Dado** que estou autenticado como participante da fase de seleção de grupos

**Quando** acesso a página de visualização das pontuações do jogo "Jogo B"

**Então** visualizo a minha pontuação registrada corretamente

#### História 3.2: 

Eu, como **estudante** posso **selecionar participanres para formar minha equipe** para **alterar a equipe de acordo com a dinâmica da aula**.


#### Cenário 1: Selecionar participantes para formar minha equipe

**Dado** que estou autenticado como participante da fase de seleção de grupos

**Quando** acesso a página de seleção de participantes

**E** seleciono os participantes "Participante A" e "Participante B" para a minha equipe

**Então** os participantes são selecionados com sucesso para a minha equipe

#### Cenário 2: Validar restrições na seleção de participantes

**Dado** que estou autenticado como participante da fase de seleção de grupos

**Quando** tento selecionar participantes para a minha equipe, mas já atingi o limite máximo de participantes

**Então** recebo uma mensagem de erro informando que não posso adicionar mais participantes à minha equipe

#### Cenário 3: Verificar a lista de participantes da minha equipe

**Dado** que estou autenticado como participante da fase de seleção de grupos

**Quando** acesso a página de visualização da minha equipe

**Então** visualizo corretamente a lista de participantes da minha equipe

### Funcionalidade 4: Visualizar infomações do grupo

#### História 4.1: 

Eu, como **estudante** posso **visualizar infomações dos integantes de cada grupo** para **centralização das informações**.

#### Cenário 1: Visualizar informações dos integrantes de um grupo

**Dado** que estou autenticado como membro de um grupo

**Quando** acesso a página de visualização do meu grupo

**Então** visualizo as informações dos integrantes do grupo corretamente

#### Cenário 2: Validar restrições de acesso às informações do grupo

**Dado** que estou autenticado como membro de um grupo diferente

**Quando** tento acessar a página de visualização do grupo "Grupo A"

**Então** recebo uma mensagem de erro informando que não tenho permissão para acessar as informações do grupo

#### Cenário 3: Verificar a lista de integrantes do grupo

**Dado** que estou autenticado como professor

**Quando** acesso a página de visualização do grupo "Grupo B"

**Então** visualizo corretamente a lista de integrantes do grupo

#### História 4.2: 

Eu, como **estudante** posso **editar infomações do usuário** para **garantir dados corretos e atualizados**.

#### Cenário 1: Editar informações do usuário

**Dado** que estou autenticado como usuário

**Quando** acesso a página de edição do meu perfil

**E** modifico minhas informações

**Então** minhas informações são atualizadas com sucesso

#### Cenário 2: Validar restrições ao editar informações do usuário

**Dado** que estou autenticado como usuário

**Quando** tento editar informações do perfil

**E** insiro dados inválidos

**Então** recebo uma mensagem de erro informando as restrições de edição

**E** minhas informações não são modificadas

#### Cenário 3: Verificar visualização das informações do usuário

**Dado** que estou autenticado como administrador

**Quando** acesso a página de visualização do perfil de um usuário

**Então** visualizo todas as informações do usuário corretamente

#### História 4.3: 

Eu, como **estudante** posso **visualizar informações do grupo** para **fácil comunicação com toda a equipe**.

#### Cenário 1: Visualizar informações do grupo

**Dado** que estou autenticado como membro de um grupo

**Quando** acesso a página de visualização do meu grupo

**Então** visualizo todas as informações do grupo corretamente

#### Cenário 2: Validar restrições de acesso às informações do grupo

**Dado** que estou autenticado como membro de um grupo diferente

**Quando** tento acessar a página de visualização do grupo "Grupo A"

**Então** recebo uma mensagem de erro informando que não tenho permissão para acessar as informações do grupo

#### Cenário 3: Verificar visualização das informações do grupo como professor

**Dado** que estou autenticado como professor

**Quando** acesso a página de visualização do grupo "Grupo B"

**Então** visualizo todas as informações do grupo corretamente

#### História 4.5: 

Eu, como **estudante** posso **visualizar o ranking de PAX da minha turma** para **observar o progresso de todas as equipes**.

#### Cenário 1: Visualizar ranking de PAX da turma

**Dado** que estou autenticado como aluno de uma turma

**Quando** acesso a página de visualização do ranking de PAX

**Então** visualizo o ranking de PAX da minha turma corretamente

#### Cenário 2: Validar restrições de acesso ao ranking de PAX

**Dado** que estou autenticado como aluno de uma turma diferente

**Quando** tento acessar a página de visualização do ranking de PAX da turma "Turma A"

**Então** recebo uma mensagem de erro informando que não tenho permissão para acessar o ranking de PAX da turma

#### Cenário 3: Verificar visualização do ranking de PAX como professor

**Dado** que estou autenticado como professor

**Quando** acesso a página de visualização do ranking de PAX da turma "Turma B"

**Então** visualizo o ranking de PAX da turma corretamente

### Funcionalidade 5: Visualizar unidades e atividades

#### História 5.1: 

Eu, como **estudante** posso **visualizar as unidades e atividades** para **centralização das informações**.

#### Cenário 1: Visualizar lista de unidades

**Dado** que estou autenticado como membro de um grupo

**Quando** acesso a página de visualização das unidades

**Então** visualizo a lista de unidades corretamente

#### Cenário 2: Validar restrições de acesso às unidades

**Dado** que estou autenticado como membro de um grupo diferente

**Quando** tento acessar a página de visualização das unidades

**Então** recebo uma mensagem de erro informando que não tenho permissão para acessar as unidades

#### Cenário 3: Verificar visualização das atividades de uma unidade

**Dado** que estou autenticado como professor

**Quando** acesso a página de visualização das atividades da unidade "Unidade A"

**Então** visualizo corretamente as atividades da unidade

#### História 5.2: 

Eu, como **estudante** posso **visualizar as regras para o cumprimento das atividades** para **clareza nas propostas das atividades**.

#### Cenário 1: Visualizar as regras para uma atividade específica

**Dado** que estou autenticado como membro de um grupo

**Quando** acesso a página de visualização das regras para a atividade "Atividade A"

**Então** visualizo as regras para cumprir a atividade corretamente

#### Cenário 2: Validar restrições de acesso às regras da atividade

**Dado** que estou autenticado como membro de um grupo diferente

**Quando** tento acessar a página de visualização das regras para a atividade "Atividade B"

**Então** recebo uma mensagem de erro informando que não tenho permissão para acessar as regras da atividade

#### Cenário 3: Verificar visualização das regras para cumprimento das atividades como professor

**Dado** que estou autenticado como professor

**Quando** acesso a página de visualização das regras para a atividade "Atividade C"

**Então** visualizo corretamente as regras para cumprir a atividade

#### História 5.3: 

Eu, como **estudante** posso **visualizar valor dos PAX's de cada atividade** para **pontuação clara**.

#### Cenário 1: Visualizar valor dos PAX de uma atividade específica

**Dado** que estou autenticado como membro de um grupo

**Quando** acesso a página de visualização do valor dos PAX da atividade "Atividade A"

**Então** visualizo corretamente o valor dos PAX da atividade

#### Cenário 2: Validar restrições de acesso ao valor dos PAX da atividade

**Dado** que estou autenticado como membro de um grupo diferente

**Quando** tento acessar a página de visualização do valor dos PAX da atividade "Atividade B"

**Então** recebo uma mensagem de erro informando que não tenho permissão para acessar o valor dos PAX da atividade

#### Cenário 3: Verificar visualização do valor dos PAX das atividades como professor

**Dado** que estou autenticado como professor

**Quando** acesso a página de visualização do valor dos PAX da atividade "Atividade C"

**Então** visualizo corretamente o valor dos PAX da atividade