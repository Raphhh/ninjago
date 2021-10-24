class Chromosome:

    def __init__(self, genes):
        self._genes = genes
        self.absolute_evaluation = 0
        self.relative_evaluation = 0

    def get_genes(self):
        return self._genes

    def to_string(self):
        result = ''
        for gene in self._genes:
            result += gene.to_string()
        return result
