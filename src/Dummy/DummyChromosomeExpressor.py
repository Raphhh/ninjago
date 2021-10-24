import string

from src.GA.ChromosomeExpressor import ChromosomeExpressor


class DummyChromosomeExpressor(ChromosomeExpressor):

    def _express_gene(self, code, occurrence):
        return (string.ascii_lowercase.index(code) + 1) * occurrence
