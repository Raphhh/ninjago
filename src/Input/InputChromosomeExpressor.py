import time

from src.Driver.Driver import Driver
from src.Driver.DriverChromosomeExpressor import DriverChromosomeExpressor
from src.Input.InputGene import InputGene


class InputChromosomeExpressor(DriverChromosomeExpressor):

    def __init__(self, time: time, driver: Driver, input_orchestrator, gene_duration):
        DriverChromosomeExpressor.__init__(self, driver)
        self._time = time
        self._input_orchestrator = input_orchestrator
        self._gene_duration = gene_duration

    def _express_gene(self, code, occurrence):
        while not self._driver.is_listening():
            self._time.sleep(1)

        duration = self._gene_duration * occurrence

        if code == InputGene.CODE_WAIT:
            self._time.sleep(duration)

        elif code == InputGene.CODE_ARROW_LEFT:
            self._input_orchestrator.press_arrow_left(duration)

        elif code == InputGene.CODE_ARROW_RIGHT:
            self._input_orchestrator.press_arrow_right(duration)

        elif code == InputGene.CODE_ARROW_UP:
            self._input_orchestrator.press_arrow_up(duration)

        elif code == InputGene.CODE_ARROW_DOWN:
            self._input_orchestrator.press_arrow_down(duration)

        elif code == InputGene.CODE_CLICK_CENTER:
            self._input_orchestrator.click_on_center(duration)

        elif code == InputGene.CODE_CLICK_RIGHT_CORNER:
            self._input_orchestrator.click_near_the_right_corner(duration)

        else:
            raise Exception('code not implemented: ' + code)
