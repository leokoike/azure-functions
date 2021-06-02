import csv
import logging
import os
import random
from io import BytesIO, StringIO


def create_random_csv(id: int) -> BytesIO:

    logging.info(f"Criação do arquivo csv com a seed {id}")
    filename = f"random_csv_{id}.csv"

    data = generate_random_csv(id=id)
    with open(filename, "wb") as csvfile:
        csvfile.write(data)

    with open(filename, "rb") as csvfile:
        file = csvfile.read()
    try:
        os.remove(filename)
        logging.info("Arquivo gerado e excluido do repositorio.")
    except FileNotFoundError:
        logging.exception("Erro ao excluir o arquivo.")

    return (file, filename)


def generate_random_csv(id: int) -> BytesIO:
    logging.info("Geração dos dados do arquivo csv")
    filedata = StringIO()
    writer = csv.writer(filedata, delimiter=";")
    random.seed(id)
    data1 = random.sample(range(1000), 7)
    data2 = random.sample(range(1000), 7)
    writer.writerows([data1, data2])

    filedata.seek(0)

    return filedata.getvalue().encode("latin1")
