# Qual o objetivo desse repositório?

Opa e ai? Estou em um período de estudos e atualmente estou estudando sobre a ferramenta Airflow. Airflow é uma ferramenta muito utilizada no mercado de trabalho hoje, mas que passa e gera nos estudantes da área ou até em pessoas de cargos avançados um frio na barriga de "complexidade". Esse repositório tem como objetivo fazer anotações e acabar com a complexidade do Airflow tentando excplicar da maneira mais didática possível.

### O Que é o Airflow?

Airflow é uma ferramenta em forma de plataforma criada para criar, agendar e monitorar fluxos de códigos de trabalho de forma programática. Ele é muito utilizável para Engenharia de Dados pois com ele conseguimos automatizar e orquestrar tarefas complexas, como processos e tratamento de dados, treinamento de Machine Learning, execução de ETLs etc.


## Por que não conseguimos utilizar o Airflow só com Docker ou com um simples "pip install apache-airflow?

O Apache Airflow é uma ferramenta usada para criar, agendar e gerenciar fluxos de trabalhos de forma programática. Acontece que, ele não é uma simples imagem ou um simples framework (biblioteca), o Airflow é uma ferramenta e na verdade tem uma série de componentes, para a utilização dele precisamos de muito mais do que só dependências instaladas pelo pip ou muito mais do que uma imagem instalada no Docker. Na verdade essas instalações fazem parte de uma das etapas para utilização da ferramenta, a outra parte envolve configurações, para utilizarmos essa ferramenta precisamos de configurações, de uma infraestrutura principalmente para os componentes do Airflow e por isso a ferramenta passa esse “ar de complexidade”. Resumindo o Airflow não é uma biblioteca, o Airflow é uma ferramenta com muitos componentes que necessita de configurações e infraestrutura para a utilização.


## O Que é uma DAG?

O que é uma DAG necessariamente? aposto que todos ja ouviram que é um fluxo de trabalho como "grafo acíclicos", mas todo iniciante em Airflow fica com medo desse nome, a DAG tem um conjunto de tarefas organizadas com depedências e seus relacionamentos. Mas bora resumir isso ai? Com o Python você consegue escrever e configurar sua DAG dentro dela você define: Quais são as tarefas; Qual a ordem entre elas; Quando elas devem rodar.
Resumindo do resumo: A DAG é como se fosse uma pipeline de ETL/ELT, ela tem sua funções e executa em uma ordem basicamente, e sobre o porque ela é "acíclica" pois não pode ter volta, ela sempre vai para frente.  

### 3 Formas de fazer uma DAG:

Com ```with```:

```python
# O Professor ensina 3 maneiras de criar uma DAG. Essa é a primeira sendo com um with, com esse with abrimos e fechamos um processo automaticamente, esse processo sendo a class DAG.

import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator

with DAG(
dag_id="primeira_dag",
start_date=datetime.datetime(2025, 4, 4),
schedule="@daily",
catchup=False
):
    EmptyOperator(task_id="tarefa")
```

Com uma Instância (Variável) :
```python
# O Professor ensina 3 maneiras de criar uma DAG. Essa é a segunda sendo com uma instância (variável ), a nossa class DAG está sendo armazenada em uma instância e no final sendo executada por um Operador.

import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator

minha_dag = DAG(
    dag_id="segunda_dag",
    start_date=datetime.datetime(2025, 4, 4),
    schedule="@daily",
    catchup=False, # Adiciona uma linha
)
EmptyOperator(task_id="tarefa", dag=minha_dag)
```

Com um Decorador (@) :
```python
# O Professor ensina 3 maneiras de criar uma DAG. Essa é a terceira forma sendo com Decoradores.

from time import sleep
from airflow.decorators import dag
from datetime import datetime

@dag(
        dag_id="terceira_pipeline",
        description="ETL MUITO complexa",
        schedule="* * * * *",
        start_date=datetime(2025, 4, 4),
        catchup=False,
)
```


## Como refatorar um código para usar o Airflow?

Para refatorar um código para utilizar o Airflow, é mais simples do que parece. Por exemplo: Sua pipeline de ETL em uma pasta hipotéticamente chamada src, essa pipeline contém um módulo chamado ```__init__.py``` ou ```main.py``` onde inicia todos os passos a passos em código da sua pipeline para chegar no seu objetivo específico, para refatorar esse código é extramente simples e fácil: Esse módulo que inicia seu código você joga na pasta ```dags```, usando a forma com decoradores (**@dag**, **@task**) você só configura a ordem em que as funções são executadas.
