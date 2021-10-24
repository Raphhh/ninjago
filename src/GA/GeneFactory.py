import random

from src.GA.Gene import Gene


class GeneFactory:

    def __init__(self, random: random, codes):
        self._random = random
        self._codes = codes

    def create_random_gene(self) -> Gene:
        return self.create_gene(
            self._random.choice(self._codes)
        )

    def create_gene(self, code) -> Gene:
        if code not in self._codes:
            raise Exception('invalide gene code: ' + code)
        return self._instantiate_gene(code)

    def _instantiate_gene(self, code) -> Gene:
        return Gene(code)
