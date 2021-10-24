from src.GA.ChromosomeEvaluator import ChromosomeEvaluator
from src.GA.ChromosomeExpressor import ChromosomeExpressor
from src.GA.GenerationsManager import GenerationsManager


class GAManager:

    def __init__(
            self,
            logger,
            generations_manager: GenerationsManager,
            chromosome_expressor: ChromosomeExpressor,
            chromosome_evaluator: ChromosomeEvaluator
    ):
        self._logger = logger
        self._generations_manager = generations_manager
        self._chromosome_expressor = chromosome_expressor
        self._chromosome_evaluator = chromosome_evaluator

    def launch_populations(
            self,
            generations_number,
            population_length,
            chromosome_maximal_length
    ):
        populations = self._generations_manager.make_populations(
            generations_number,
            population_length,
            chromosome_maximal_length
        )

        for population in populations:
            self._launch_population(population)

    def _launch_population(self, population):
        self._logger.debug('population expression start')

        self._launch_chromosomes(population)
        population_score = self._evaluate_population(population)
        self._normalize_evaluation(population, population_score)

        self._logger.debug('population expression end', {
            'evaluation': population_score
        })

    def _launch_chromosomes(self, population):
        for chromosome in population:
            self._logger.debug('chromosome expression start', {
                'genes': chromosome.to_string(),
                'length': len(chromosome.get_genes())
            })

            expression = self._chromosome_expressor.express_chromosome(chromosome)
            self._chromosome_evaluator.evaluate(chromosome, expression)

            self._logger.debug('chromosome expression end', {
                'absolute_evaluation': chromosome.absolute_evaluation
            })

    def _evaluate_population(self, population):
        result = 0
        for chromosome in population:
            result += chromosome.absolute_evaluation
        return result

    def _normalize_evaluation(self, population, population_score):
        for chromosome in population:
            if population_score:
                chromosome.relative_evaluation = chromosome.absolute_evaluation / population_score

