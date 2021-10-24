import string

from src.GA.Chromosome import Chromosome
from src.GA.ChromosomeEvaluator import ChromosomeEvaluator


class DummyChromosomeEvaluator(ChromosomeEvaluator):

    def __init__(self, chromosome_maximal_length, number_of_genes=0):
        if number_of_genes == 0:
            number_of_genes = len(string.ascii_lowercase)
        elif number_of_genes > len(string.ascii_lowercase):
            raise Exception('number_of_genes out of bounds')

        self._number_of_genes = number_of_genes
        self._chromosome_maximal_length = chromosome_maximal_length

    def evaluate(self, chromosome: Chromosome, expression):
        chromosome.absolute_evaluation = sum(expression) / (self._number_of_genes * self._chromosome_maximal_length)
