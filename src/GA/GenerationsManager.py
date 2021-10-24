from src.GA.PopulationCreator import PopulationCreator


class GenerationsManager:

    def __init__(self, population_creator: PopulationCreator):
        self._population_creator = population_creator

    def make_populations(self, generations_number, population_length, chromosome_maximal_length):
        last_population = None
        for i in range(generations_number):
            if not last_population:
                last_population = self._population_creator.make_new_population(
                    population_length,
                    chromosome_maximal_length
                )
            else:
                last_population = self._population_creator.make_child_population(
                    last_population,
                    chromosome_maximal_length
                )
            yield last_population
