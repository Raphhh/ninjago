from src.GA.Chromosome import Chromosome


class ChromosomeExpressor:

    def express_chromosome(self, chromosome: Chromosome):
        expression = []
        for smooth_gene in self._smooth_chromosome(chromosome):
            expression.append(self._express_gene(smooth_gene['code'], smooth_gene['occurrence']))
        return expression

    def _express_gene(self, code, occurrence):
        pass

    def _smooth_chromosome(self, chromosome):
        result = []
        previous_gene = None

        for gene in chromosome.get_genes():
            if previous_gene is not None and gene.is_smoothable_code() and gene.get_code() == previous_gene['code']:
                previous_gene['occurrence'] += 1
            else:
                previous_gene = {'code': gene.get_code(), 'occurrence': 1}
                result.append(previous_gene)

        return result
