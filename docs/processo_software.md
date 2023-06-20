# Processo de Desenvolvimento de Software

## Metodologia

### GUPTA

De acordo com as considerações de Gupta (2008)¹, é fundamental que a seleção da abordagem de desenvolvimento de software leve em conta uma série de critérios relevantes. Entre esses critérios estão as necessidades e requisitos específicos do projeto, bem como o ambiente e a cultura organizacional em que o projeto será executado. Além disso, o tamanho e a complexidade do projeto, o risco envolvido, o orçamento disponível e o prazo para a conclusão do projeto também desempenham um papel crucial na escolha adequada da abordagem.

É importante ressaltar que essa decisão não pode ser tomada de forma isolada ou estática. Pelo contrário, ela requer um processo contínuo de revisão e adaptação ao longo do tempo, visando garantir o sucesso do projeto. Dessa forma, é imprescindível monitorar e reavaliar regularmente a abordagem adotada, a fim de assegurar que esteja alinhada com as necessidades e condições do projeto. Veja a tabela abaixo.


| Requisitos | Cascata | Prototipação | Interativo e Incremental | Evolutivo | Spiral | RAD | Nosso Contexto |
| :--------: | :-----: | :----------: | :---------------------:  | :------:  | :-----: | :---: | :------------: |
| Os requisitos são facilmente compreensíveis e definidos? | Sim | Não | Não | Não | Não | Sim | Sim |
| Mudamos os requisitos com bastante frequência? | Não | Sim | Não | Não | Não | Sim | Não |
| Podemos mudar os requisitos no início do ciclo? | Sim | Não | Sim | Sim | Não | Sim | Sim |
| Os requisitos indicam um sistema complexo a ser construído? | Não | Sim | Sim | Sim | Não | Sim | Sim |

<div align="center">
    <h5 class="text-center">Tabela 1 - Análise de processos (Fonte: Gupta, 20019)</h5>
</div>


## Facetas

Diversos aspectos do processo de Engenharia de Requisitos são abordados no IREB (2022)², fornecendo uma estrutura para identificar as características dos requisitos do projeto. A figura 1 apresenta a estrutura do diagrama, destacando os pontos relevantes a serem considerados.

É importante ressaltar que o IREB (2022)² oferece diretrizes valiosas para a análise e compreensão abrangente dos requisitos de um projeto. Ao utilizar essa estrutura, é possível examinar diferentes facetas do processo de Engenharia de Requisitos, permitindo uma identificação mais precisa das necessidades e características essenciais para o sucesso do projeto.
 
 <br>

![facetas](assets/images/Facetas.png)

<div align="center">
    <h5 class="text-center">Figura 1 - Facetas do processo de ER (Fonte: IREB, 2022)</h5>
</div>

<br>

Ao analisar as descrições das facetas do processo de Engenharia de Requisitos, concluímos que o mesmo será caracterizado por ser iterativo, exploratório e orientado ao mercado. Durante essa análise, foram considerados os seguintes aspectos:

- Requisitos não completamente conhecidos desde o início: Reconhecemos que os requisitos do projeto podem evoluir ao longo do tempo e não estar totalmente definidos desde o início. Isso implica em uma abordagem flexível que permita ajustes e adaptações durante o desenvolvimento.

- Ciclos curtos de feedback pela proximidade do time de desenvolvimento com o cliente: A proximidade entre a equipe de desenvolvimento e o cliente possibilita a realização de ciclos curtos de feedback, permitindo uma comunicação eficaz e rápida para entender as necessidades e realizar ajustes ao longo do processo.

- Priorização e negociação de requisitos devido à duração do projeto: Dada a duração do projeto, é necessário estabelecer prioridades e negociar requisitos conforme as restrições de tempo e recursos. Isso envolve tomar decisões estratégicas para garantir a entrega de valor dentro do prazo e do orçamento estabelecidos.

- Foco no desenvolvimento de um produto utilizável por diversos clientes: Embora exista um cliente inicial, o objetivo do projeto é desenvolver um produto que possa ser utilizado por uma ampla gama de clientes, cujos usuários individuais não são identificáveis antecipadamente. Isso requer uma abordagem que leve em consideração as necessidades e expectativas de um público diversificado.

- Participação conjunta da equipe do projeto e do cliente na elicitação de requisitos: Embora a equipe do projeto tenha um papel central na elicitação de requisitos, é importante ressaltar que a participação do cliente é essencial. A colaboração entre ambas as partes contribui para uma compreensão mais abrangente das necessidades e para a definição dos requisitos de forma eficaz.

Portanto, com base nesses aspectos, fica evidente a necessidade de adotar uma abordagem iterativa, exploratória e orientada ao mercado no processo de Engenharia de Requisitos, considerando a natureza dinâmica e a complexidade do projeto em questão. Sendo assim selecionado pela equipe o Scrum e o XP para o desenvolvimento do software.


### Scrum
| |  |  |  |
| :----: | --------------------------------------------------------------------------------------------------------------------------------- | ----------- | ---------- |
| Planejamento da sprint | Reuniao realizada no inicio de cada sprint com o objetivo de definir as Historias de Usuario entregaveis na sprint. | Discord |
| Sprint | Período de realizacao das atividades propostas durante o planejamento da sprint. Definimos a duração da sprint como duas semanas. | Discord |
| Review da sprint | Reuniao realizada pela equipe para revisar as funcionalidades concluidas no final da sprint com o Product owner (PO). | Discord |
| Retrospectiva da sprint | Processo também realizado ao final de cada sprint para verificar a qualidade do produto e da equipe. | Discord |
| Daily Scrum | Reunião diária com duração máxima de 15 minutos, na qual os membros da equipe devem discutir o progresso de trabalho da Sprint desde a última reunião diária. | Discord (Assincrono) |
| Backlog do produto | Lista dos requisitos do produto que necessitam ser desenvolvidos. | Trello |

### XP
| |  |  |  |
| :----: | --------------------------------------------------------------------------------------------------------------------------------- | ----------- | ---------- |
| Toda a Equipe | Ajuda a equipe trabalhar junta para resolver problemas e assim alcançar os objetivos do projeto, aumentando a produtividade e diminuindo conflitos entre os membros da equipe. |
| Ritmo Sustentável | Evita sobrecarga de trabalho e esgotamento físico e mental dos membros da equipe. Testes: Devem ser implementados testes unitários, de integração e de aceitação ao longo do processo de desenvolvimento |
| Design Simples | Projetos com a prática de um design simples sao benéficos, principalmente, para a manutenção do projeto. |
| Refatoração | Prática que envolve a melhoria contínua do código existente sem alterar sua funcionalidade |

### Etapa 1

| Etapa | Método | ferramenta | Entrega |
| :----: | --------------------------------------------------------------------------------------------------------------------------------- | ----------- | ---------- |
| Planejamento de estratégias e métodos de desenvolvimento | Reunião da equipe | Discord da equipe | Estratégias de desenvolvimento definidas |

### Etapa 2

| Etapa | Método | ferramenta | Entrega |
| :----: | --------------------------------------------------------------------------------------------------------------------------------- | ----------- | ---------- |
| Planejar estratégias da equipe | Reunião da equipe | Discord da equipe | Estratégias da equipe |

### Etapa 3

| Etapa | Método | ferramenta | Entrega |
| :----: | --------------------------------------------------------------------------------------------------------------------------------- | ----------- | ---------- |
| Decidir os objetivos de cada sprint | Reunião da equipe | Discord da equipe | O planejamento da sprint da semana |

### Etapa 4

| Etapa | Método | ferramenta | Entrega |
| :----: | --------------------------------------------------------------------------------------------------------------------------------- | ----------- | ---------- |
| Apresentação dos resultados da sprint | Reunião de revisão (Review) | Discord da equipe | Alterações válidas em relação aos resultados da sprint |

### Etapa 5

| Etapa | Método | ferramenta | Entrega |
| :----: | --------------------------------------------------------------------------------------------------------------------------------- | ----------- | ---------- |
| Validação com o cliente | Apresentação de ponto de controle | Discord | Entrega das funcionalidades aprovadas |

### Etapa 6

| Etapa | Método | ferramenta | Entrega |
| :----: | --------------------------------------------------------------------------------------------------------------------------------- | ----------- | ---------- |
| Inspeção da sprint passada | Reunião de retrospectiva | Discord da equipe | Sprint revisada com os pontos de melhoria |

### Etapa 7

| Etapa | Método | ferramenta | Entrega |
| :----: | --------------------------------------------------------------------------------------------------------------------------------- | ----------- | ---------- |
| Levantamento de melhorias para as próximas sprints | Reunião de retrospectiva | Discord da equipe | Pontos de melhoria |

### Etapa 8

| Etapa | Método | ferramenta | Entrega |
| :----: | --------------------------------------------------------------------------------------------------------------------------------- | ----------- | ---------- |
| Avaliação das estratégias de desenvolvimento | Reunião de retrospectiva | Discord da equipe | Pontos positivos e negativos e analisar se precisa de mudanças e quais precisam ser feitas |

### Etapa 9

| Etapa | Método | ferramenta | Entrega |
| :----: | --------------------------------------------------------------------------------------------------------------------------------- | ----------- | ---------- |
| valiação das estratégias da equipe | Reunião de retrospectiva | Discord da equipe | Pontos positivos e negativos da estratégia e pontos de melhoria |

## Histórico de revisão

|  Data | Versão | Descrição | Autor(es) |
| :--------: | :----: | :---------------------------------: | :---------: |
| 26/04/2023 |  1.0   | Criação e estruturação do documento | Paulo Borba |
| 24/05/2023 |  1.1   | Criação e estruturação do documento | Paulo Borba e Falipe Nunes |
| 13/06/2023 |  2.0   | Alterações de acordo com o parecer do professor na entrega 2 | Vinícius |
