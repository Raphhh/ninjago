import math
import random

from src.GA.Chromosome import Chromosome
from src.GA.GeneFactory import GeneFactory


class PopulationCreator:

    def __init__(self, random: random, gene_factory: GeneFactory, mutation_frequency):
        self._random = random
        self._gene_factory = gene_factory
        self._mutation_frequency = mutation_frequency

    def make_new_population(self, length, chromosome_maximal_length):
        result = []
        for i in range(length):
            result.append(self._make_new_chromosome(chromosome_maximal_length))
        return result

    def make_child_population(self, parent_population, chromosome_maximal_length):
        return self._make_child_chromosomes(parent_population, chromosome_maximal_length)

    def _make_new_chromosome(self, maximal_length, relative_minimal_size=0.5):
        genes = []
        for i in range(random.randint(maximal_length * relative_minimal_size, maximal_length)):
            genes.append(self._gene_factory.create_random_gene())
        return Chromosome(genes)

    def _make_child_chromosomes(self, parent_population, chromosome_maximal_length):
        mating_pool = self._create_mating_pool(parent_population)
        maximum_index = len(mating_pool) - 1

        result = []
        for i in range(len(parent_population)):
            result.append(
                self._crossover(
                    [
                        mating_pool[self._random.randint(0, maximum_index)],
                        mating_pool[self._random.randint(0, maximum_index)],
                    ],
                    chromosome_maximal_length
                )[0]
            )
        return result

    def _select_chromosomes(self, population, saved_ones):
        population.sort(key=lambda chromosome: chromosome.absolute_evaluation, reverse=True)
        best_chromosomes = []
        for i in range(int(len(population) * saved_ones)):
            best_chromosomes.append(population[i])
        self._random.shuffle(best_chromosomes)
        return best_chromosomes

    def _crossover(self, parents, chromosome_maximal_length):
        length = len(parents)

        genes_list = []
        for i in range(length):
            for j, parent in enumerate(parents):
                if j == len(genes_list):
                    genes_list.append([])
                position = i + j
                if position >= length:
                    position -= length
                # todo je ne connais pas assez python: quid du [i] si array est vide?
                genes_list[position] += self._split_list(parent.get_genes(), length, True)[i]

        result = []
        for genes in genes_list:
            if self._mutation_frequency and self._random.randint(0, int(1 / self._mutation_frequency)) == 0:
                genes = self._mutate(genes, chromosome_maximal_length)
            result.append(Chromosome(genes))
        return result

    def _mutate(self, genes, chromosome_maximal_length):
        index = self._random.randint(0, chromosome_maximal_length-1)
        if index < len(genes):
            genes[index] = self._gene_factory.create_random_gene()
        else:
            genes.append(self._gene_factory.create_random_gene())
        return genes

    def _create_mating_pool(self, population):
        population_length = len(population)
        best_chromosomes = self._select_chromosomes(population, 0.5)

        result = []
        for chromosome in best_chromosomes:
            total = int(chromosome.relative_evaluation * population_length)
            for i in range(total):
                result.append(chromosome)

        if len(result) == 0:
            # todo BUG: ce comportement n'est pas normal!
            result = best_chromosomes

        return result

    def _split_list(self, list, number_of_parts, take_remainder):
        quotient, remainder = divmod(len(list), number_of_parts)

        if take_remainder and remainder:
            quotient += 1

        result = []
        for i in range(number_of_parts):
            start = i * quotient
            end = (i+1) * quotient
            result.append(list[start:end])
        return result
