from src.Driver.Driver import Driver
from src.GA.Chromosome import Chromosome
from src.GA.ChromosomeExpressor import ChromosomeExpressor


class DriverChromosomeExpressor(ChromosomeExpressor):

    def __init__(self, driver: Driver):
        self._driver = driver

    def express_chromosome(self, chromosome: Chromosome):
        self._driver.restart_level()
        ChromosomeExpressor.express_chromosome(self, chromosome)
