import random

from src.GA.GeneFactory import GeneFactory
from src.Input.InputGene import InputGene


class PrimeEmpireGeneFactory(GeneFactory):

    def __init__(self, random: random):
        GeneFactory.__init__(self, random, [
            # todo yes, let's cheat a little bit :)

            InputGene.CODE_WAIT,
            InputGene.CODE_ARROW_LEFT,
            InputGene.CODE_ARROW_LEFT,
            InputGene.CODE_ARROW_LEFT,
            InputGene.CODE_ARROW_RIGHT,
            InputGene.CODE_ARROW_RIGHT,
            InputGene.CODE_ARROW_RIGHT,
            InputGene.CODE_ARROW_RIGHT,
            InputGene.CODE_ARROW_RIGHT,
            InputGene.CODE_ARROW_RIGHT,
            InputGene.CODE_ARROW_RIGHT,
            InputGene.CODE_ARROW_RIGHT,
            InputGene.CODE_ARROW_RIGHT,
            InputGene.CODE_ARROW_RIGHT,
            InputGene.CODE_ARROW_RIGHT,
            InputGene.CODE_ARROW_UP,
            InputGene.CODE_ARROW_UP,
            InputGene.CODE_ARROW_UP,
            InputGene.CODE_ARROW_UP,
            InputGene.CODE_ARROW_DOWN,
            InputGene.CODE_CLICK_CENTER,
            InputGene.CODE_CLICK_CENTER,
            InputGene.CODE_CLICK_RIGHT_CORNER,
            InputGene.CODE_CLICK_RIGHT_CORNER,
        ])

    def _instantiate_gene(self, code) -> InputGene:
        return InputGene(code)
