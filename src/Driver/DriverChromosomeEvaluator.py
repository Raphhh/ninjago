from src.Driver.Driver import Driver
from src.GA.Chromosome import Chromosome
from src.GA.ChromosomeEvaluator import ChromosomeEvaluator


class DriverChromosomeEvaluator(ChromosomeEvaluator):

    def __init__(self, driver: Driver):
        self._driver = driver

    def evaluate(self, chromosome: Chromosome, expression):
        chromosome.absolute_evaluation = self._driver.calculate_score()
        # todo
        #  si le score est au max, alors il faut prendre en cosidération la longueur du chromosome:
        #  moins il y a de gènes, plus le chromosome est performant