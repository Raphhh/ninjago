import random

from src.Dummy.DummyChromosomeEvaluator import DummyChromosomeEvaluator
from src.Dummy.DummyChromosomeExpressor import DummyChromosomeExpressor
from src.Dummy.DummyGeneFactory import DummyGeneFactory
from src.GA.GAManager import GAManager
from src.GA.GenerationsManager import GenerationsManager
from src.GA.PopulationCreator import PopulationCreator


class DummyFacade:

    def __init__(self, logger):
        self._logger = logger

    def play(
        self,
        generations_number,
        population_length,
        chromosome_maximal_length,
        mutation_frequency
    ):
        self._build_gamer(chromosome_maximal_length, mutation_frequency, 7).launch_populations(
            generations_number,
            population_length,
            chromosome_maximal_length
        )

    def _build_gamer(self, chromosome_maximal_length, mutation_frequency, number_of_genes):
        return GAManager(
            self._logger,
            GenerationsManager(
                PopulationCreator(
                    random,
                    DummyGeneFactory(random, number_of_genes),
                    mutation_frequency
                )
            ),
            DummyChromosomeExpressor(),
            DummyChromosomeEvaluator(chromosome_maximal_length, number_of_genes)
        )
