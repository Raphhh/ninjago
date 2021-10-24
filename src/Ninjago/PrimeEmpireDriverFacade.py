import random
import time

import pyautogui as pyautogui

from src.Driver.DriverChromosomeEvaluator import DriverChromosomeEvaluator
from src.GA.GenerationsManager import GenerationsManager
from src.Ninjago.PrimeEmpireDriverFactory import PrimeEmpireDriverFactory
from src.GA.PopulationCreator import PopulationCreator
from src.GA.GAManager import GAManager
from src.Input.InputChromosomeExpressor import InputChromosomeExpressor
from src.Ninjago.PrimeEmpireGeneFactory import PrimeEmpireGeneFactory
from src.Input.InputOrchestror import InputOrchestrator
from src.Selenium.SeleniumDriverFactory import SeleniumDriverFactory


class PrimeEmpireFacade:

    def __init__(self, logger):
        self._logger = logger

    def play(
        self,
        generations_number,
        population_length,
        life_maximal_duration,
        gene_duration,
        mutation_frequency
    ):
        self._build_gamer(gene_duration, mutation_frequency).launch_populations(
            generations_number,
            population_length,
            life_maximal_duration / gene_duration
        )
        self._close()

    def _build_gamer(self, gene_duration, mutation_frequency) -> GAManager:
        self._driver = PrimeEmpireDriverFactory(
            self._logger,
            SeleniumDriverFactory(self._logger)
        ).create_ninjago_driver()

        return GAManager(
            self._logger,
            GenerationsManager(
                PopulationCreator(
                    random,
                    PrimeEmpireGeneFactory(random),
                    mutation_frequency
                )
            ),
            InputChromosomeExpressor(
                time,
                self._driver,
                InputOrchestrator(time, pyautogui),
                gene_duration
            ),
            DriverChromosomeEvaluator(self._driver)
        )

    def _close(self):
        if self._driver:
            self._driver.close()
