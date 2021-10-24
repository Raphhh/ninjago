import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from src.Driver.Driver import Driver


class PrimeEmpireDriver(Driver):

    STATUS_NONE = 'status_none'
    STATUS_READY = 'status_ready'
    STATUS_LOADING = 'status_loading'
    STATUS_WAITING = 'status_waiting'

    GAME_URL = "https://www.lego.com/assets/franchiseSites/Ninjago/primeempire/index.html?locale=fr-be"

    def __init__(self, logger, driver: WebDriver, refresh=0.5):
        self._logger = logger
        self._driver = driver
        self._refresh = refresh
        self._level = 0
        self._set_state(self.STATUS_NONE, 0)
        self._steps = []
        self._fails = 0
        
    def close(self):
        self._driver.close()

    def start(self):
        self._set_state(self.STATUS_LOADING, 0)
        self._driver.get(self.GAME_URL)
        self._wait_for_game_ready(self._refresh)

    def restart_level(self):
        if self._level == 0 or self._level == 1:
            self.start()
        else:
            raise Exception('level not implemented: ' + str(self._level))

    def is_ready(self):
        self._evaluate_log()
        return self._status == self.STATUS_READY

    def is_listening(self):
        # be sure the game is in full screen mode
        return 'hidden' in self._driver.find_element(By.ID, 'invisible').get_attribute('style')

    def calculate_score(self):
        self._evaluate_log()

        score = 0
        current_step = 0
        for step in self._steps:
            current_step += 1
            if step == current_step:
                score += 1
            else:
                score += 0.5
        return score

    def get_fails(self):
        return self._fails

    def _set_state(self, status, level):
        if not level or level != self._level:
            self._fails = 0
            self._steps = []

        self._status = status
        self._level = level
        self._logger.debug('game state updated', {
            'status': self._status,
            'level': self._level,
            'fails': self._fails,
            'steps': self._steps
        })

    def _wait_for_game_ready(self, refresh):
        while True:
            if self.is_ready():
                return True
            time.sleep(refresh)

    def _evaluate_log(self):
        for entry in self._driver.get_log('browser'):
            self._evaluate_log_entry(entry)

    def _evaluate_log_entry(self, entry):
        self._logger.debug('log from browser', entry)

        if 'savepoint restored' in entry['message']:
            self._fails += 1

        elif 'Loading complete' in entry['message']:
            self._set_state(self.STATUS_WAITING, 0)
            time.sleep(2)
            # click on "Enter"
            self._driver.find_element(By.ID, 'fscontainer').click()
            time.sleep(2)
            # click on "Start game"
            self._driver.find_element(By.ID, 'btn').click()
            # the level 1 is loading
            self._set_state(self.STATUS_LOADING, 0)

        elif '01 - Enter' in entry['message']:
            self._set_state(self.STATUS_LOADING, 1)
            # level 1 intro takes 10 sec
            time.sleep(10)
            self._set_state(self.STATUS_READY, 1)
            self._steps.append(1)

        elif '02 - Jump Tutorial' in entry['message']:
            self._steps.append(2)

        elif '03 - Something On Top' in entry['message']:
            self._steps.append(3)

        elif '04 - Jay\'s Weapons' in entry['message']:
            self._steps.append(4)

        elif '05 - Destroy Underwood' in entry['message']:
            self._steps.append(5)

        elif '06 - Use Spinjitzu' in entry['message']:
            self._steps.append(6)

        elif '07 - Level Exit' in entry['message']:
            self._steps.append(7)

