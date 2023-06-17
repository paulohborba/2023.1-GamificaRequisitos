# BDD

## FEATURE: Publicar atividade

## 1 PBI: Definir a sequência das atividades e disciplinas

### Cenário 1: Definir a sequência das atividades

**Dado** que estou autenticado como professor

**Quando** defino a atividade "Definição do MVP" como a 5ª da sequência

**Então** a atividade "Definição do MVP" aparece posteriormente a 4ª atividade

### Cenário 2: Verificar a sequência das atividades

**Dado** que estou autenticado como aluno

**Quando** visualizo a atividade "Definição do MVP"

**Então** vejo a atividade posteriormente a 4ª atividade

## 2 PBI: Definir o valor em PAX

### Cenário 1: Definir o valor em PAX para uma atividade

**Dado** que estou autenticado como professor

**Quando** defino o valor de 30 PAXs para a atividade "Apresentação Final"

**Então** o valor em PAX para a atividade é atualizado com sucesso

### Cenário 2: Definir o valor em PAX para uma atividade

**Dado** que estou autenticado como professor

**Quando** defino o valor de A3R0 PAXs para a atividade "Apresentação Final"

**Então** o valor em PAX para a atividade não é atualizado

### Cenário 3: Verificar o valor em PAX de uma atividade

**Dado** que estou autenticado como aluno

**Quando** visualizo a atividade "Apresentação Final", que vale 30 PAX

**Então** vejo o valor de 30 PAX atribuído a atividade

## 3 PBI: Definir datas

### Cenário 1: Definir data de início do semestre

**Dado** que estou autenticado como professor

**Quando** defino a data de início do semestre para 1º de março

**Então** a data de início do semestre é atualizada com sucesso

### Cenário 2: Definir data de término do semestre

**Dado** que estou autenticado como professor

**Quando** defino a data de término do semestre para 30 de junho

**Então** a data de término do semestre é atualizada com sucesso

### Cenário 3: Verificar a data de início do semestre

**Dado** que estou autenticado como professor

**Quando** defino a data de término do semestre para 31 de junho

**Então** a data de término do semestre não é atualizada

### Cenário 4: Definir data de término do semestre

**Dado** que estou autenticado como professor

**Quando** defino a data de término do semestre para 31 de junho

**Então** a data de término do semestre não é atualizada

## FEATURE: Organizar turmas

## 1 PBI: Editar todos os dados das turmas

### Cenário 1: Editar informações de uma turma

**Dado** que estou autenticado como administrador
**Quando** acesso a página de edição da turma "Turma A"
**Quando** modifico as informações da turma
**Então** as informações da turma são atualizadas com sucesso

### Cenário 2: Validar restrições ao editar turma

**Dado** que estou autenticado como administrador
**Quando** tento editar as informações da turma "Turma B"
**Quando** insiro dados inválidos
**Então** recebo uma mensagem de erro informando as restrições de edição
**Quando** as informações da turma não são modificadas

### Cenário 3: Verificar visualização das informações da turma

**Dado** que estou autenticado como professor
**Quando** acesso a página de visualização da turma "Turma C"
**Então** visualizo todas as informações da turma corretamente

## 2 PBI: Criar grupos aleatórios de usuários cadastrados para o início da fase de seleção de grupos

### Cenário 1: Criar grupos aleatórios para uma turma

**Dado** que estou autenticado como administrador
**Quando** crio grupos aleatórios para a turma "Turma A"
**Então** os grupos são criados com sucesso
**Quando** cada grupo possui um número igual de usuários cadastrados

### Cenário 2: Validar quantidade mínima de usuários para criar grupos

**Dado** que estou autenticado como administrador
**Quando** tento criar grupos aleatórios para a turma "Turma B"
**Quando** a quantidade de usuários cadastrados é insuficiente
**Então** recebo uma mensagem de erro informando a quantidade mínima necessária
**Quando** nenhum grupo é criado

### Cenário 3: Verificar a distribuição aleatória dos usuários nos grupos

**Dado** que estou autenticado como professor
**Quando** visualizo a distribuição dos usuários nos grupos da turma "Turma C"
**Então** os usuários estão distribuídos aleatoriamente nos grupos
**Quando** cada grupo possui aproximadamente o mesmo número de usuários

## 3 PBI: Exportar um arquivo .xls com matrícula, nome, email, equipe e o saldo de PAXs de todos os alunos da turma selecionada

### Cenário 1: Exportar dados dos alunos em formato .xls

**Dado** que estou autenticado como administrador
**Quando** seleciono a opção de exportar dados dos alunos da turma "Turma A"
**Então** um arquivo .xls é gerado com sucesso
**Quando** o arquivo contém as colunas de matrícula, nome, email, equipe e saldo de PAXs de todos os alunos da turma

### Cenário 2: Validar permissões de exportação de dados dos alunos

**Dado** que estou autenticado como professor
**Quando** tento exportar dados dos alunos da turma "Turma B"
**Então** recebo uma mensagem de erro informando que não tenho permissão para exportar os dados
**Quando** nenhum arquivo .xls é gerado

### Cenário 3: Verificar a precisão dos dados exportados

**Dado** que estou autenticado como administrador
**Quando** exporto dados dos alunos da turma "Turma C"
**Então** verifico que o arquivo .xls contém as informações corretas de matrícula, nome, email, equipe e saldo de PAXs de todos os alunos da turma

## 4 PBI: Arquivar turmas

### Cenário 1: Arquivar uma turma

**Dado** que estou autenticado como administrador
**Quando** seleciono a opção de arquivar a turma "Turma A"
**Então** a turma é arquivada com sucesso
**Quando** os dados da turma não estão mais visíveis nas consultas e operações regulares

### Cenário 2: Validar restrições ao arquivar turma

**Dado** que estou autenticado como administrador
**Quando** tento arquivar a turma "Turma B"
**Quando** a turma possui atividades ou grupos não concluídos
**Então** recebo uma mensagem de erro informando as restrições de arquivamento
**Quando** a turma não é arquivada

### Cenário 3: Verificar a lista de turmas arquivadas

**Dado** que estou autenticado como professor
**Quando** acesso a lista de turmas arquivadas
**Então** visualizo corretamente todas as turmas arquivadas
**Quando** posso restaurar ou realizar ações específicas em cada turma arquivada

## 5 PBI: Importar um arquivo .xls com matrícula, nome e email de todos os alunos da turma selecionada

### Cenário 1: Importar dados dos alunos a partir de um arquivo .xls

**Dado** que estou autenticado como administrador
**Quando** seleciono a opção de importar dados dos alunos para a turma "Turma A"
**Quando** seleciono um arquivo .xls válido contendo matrícula, nome e email dos alunos
**Então** os dados dos alunos são importados com sucesso para a turma

### Cenário 2: Validar formato inválido do arquivo .xls

**Dado** que estou autenticado como administrador
**Quando** tento importar dados dos alunos para a turma "Turma B"
**Quando** seleciono um arquivo .xls inválido ou com formato incorreto
**Então** recebo uma mensagem de erro informando o formato inválido do arquivo
**Quando** nenhum dado é importado para a turma

### Cenário 3: Verificar a precisão dos dados importados

**Dado** que estou autenticado como administrador
**Quando** importo dados dos alunos para a turma "Turma C" a partir de um arquivo .xls válido
**Então** verifico que os dados de matrícula, nome e email dos alunos são importados corretamente para a turma
