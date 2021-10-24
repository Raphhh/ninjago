import logging
import os

from src.Dummy.DummyFacade import DummyFacade
from src.Ninjago.PrimeEmpireDriverFacade import PrimeEmpireFacade

app_name = 'Prime Empire GA gamer'

generations_number = 250
population_length = 275
chromosome_maximal_length = 60
mutation_frequency = 0.1
gene_duration = 0.25


def define_logger(app_name):
    logger = logging.getLogger(app_name)
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(args)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def prime_empire():
    generations_number = 2
    population_length = 3

    PrimeEmpireFacade(define_logger(app_name)).play(
        generations_number,
        population_length,
        chromosome_maximal_length,
        gene_duration,
        mutation_frequency
    )


def dummy():
    DummyFacade(define_logger(app_name)).play(
        generations_number,
        population_length,
        chromosome_maximal_length,
        mutation_frequency
    )


def main():
    if os.environ.get('NINJAGO') == 'dummy':
        dummy()
    else:
        prime_empire()


if __name__ == '__main__':
    main()

