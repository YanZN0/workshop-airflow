# Professor fez esses exemplos para termos uma noção do que o Airflow faz, e esses exemplos nôs mostram se caso quisermos fazer uma orquestração do nosso fluxo de código sem o Airflow ou alguma outra biblioteca mais conhecido como: reeiventar a roda.

from time import sleep
from loguru import logger

logger.add("execution_logs.log", format="{time} - {message}", level="INFO", retention="1 day")

def primeira_atividade():
    logger.info("Minha primeira atividade")
    sleep(2)

def segunda_atividade():
    logger.info("Minha segunda atividade")
    sleep(2)

def terceira_atividade():
    logger.info("Minha terceira atividade")
    sleep(2)

def pipeline_atividades():
    primeira_atividade()
    segunda_atividade()
    terceira_atividade()
    logger.info("Pipeline Finalizada!!")

if __name__ == "__main__":
    while True:
        pipeline_atividades()
        sleep(10)   # Podendo ser a parte de Scherduler