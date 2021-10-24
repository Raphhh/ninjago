import random
import string

from src.GA.GeneFactory import GeneFactory


class DummyGeneFactory(GeneFactory):

    def __init__(self, random: random, number_of_genes=0):
        if number_of_genes == 0:
            number_of_genes = len(string.ascii_lowercase)
        elif number_of_genes > len(string.ascii_lowercase):
            raise Exception('number_of_genes out of bounds')

        GeneFactory.__init__(self, random, list(string.ascii_lowercase)[:number_of_genes])
