from src.Ninjago.PrimeEmpireDriver import PrimeEmpireDriver
from src.Selenium.SeleniumDriverFactory import SeleniumDriverFactory


class PrimeEmpireDriverFactory:

    def __init__(self, logger, selenium_driver_factory: SeleniumDriverFactory):
        self._logger = logger
        self._selenium_driver_factory = selenium_driver_factory

    def create_ninjago_driver(self) -> PrimeEmpireDriver:
        return PrimeEmpireDriver(self._logger, self._selenium_driver_factory.create_selenium_driver())
