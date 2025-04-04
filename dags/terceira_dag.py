# O Professor ensina 3 maneiras de criar uma DAG. Essa é a terceira forma sendo com Decoradores.

from time import sleep
from airflow.decorators import dag

@dag
def pipeline_atividades():  # Chamamos nossas atividades no começo, e não no final...


    def primeira_atividade():
        print("Minha primeira atividade")
        sleep(2)

    def segunda_atividade():
        print("Minha segunda atividade")
        sleep(2)

    def terceira_atividade():
        print("Minha terceira atividade")
        sleep(2)

    def quarta_atividade():
        print("Pipeline Finalizada!!")

    primeira_atividade()
    segunda_atividade()
    terceira_atividade()
    quarta_atividade()