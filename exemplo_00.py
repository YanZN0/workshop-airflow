# Exemplo fluxo de uma ETL.

from time import sleep

def primeira_atividade():
    print("Minha primeira atividade")
    sleep(2)

def segunda_atividade():
    print("Minha segunda atividade")
    sleep(2)

def terceira_atividade():
    print("Minha terceira atividade")
    sleep(2)

def pipeline_atividades():
    primeira_atividade()
    segunda_atividade()
    terceira_atividade()
    print("Pipeline Finalizada!!")

if __name__ == "__main__":
    pipeline_atividades()